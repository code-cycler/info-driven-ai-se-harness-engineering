#!/usr/bin/env python3
"""i18n 英文镜像漂移检查(ADR-0025 / feature-i18n-support)

中文源 = 唯一 canonical;`en/` 下为翻译镜像(单向派生,英文永不回灌中文)。
本脚本检查三类漂移,输出五类结果:

  缺镜像  —— TRANSLATABLE 白名单内的 zh 文件没有对应 en/ 镜像(结构失配)
  孤儿    —— en 文件的 en-source 指向的 zh 源不存在(被删/改名)
  过期    —— en 文件记录的 zh-hash ≠ 当前 zh 源实际 hash(中文已变,待回译)
  缺标记  —— en 文件缺 frontmatter 或缺 lang/en-source/zh-hash 三字段之一
  断链    —— en 文件内相对链接目标文件不存在

用法:
  python3 scripts/i18n-check.py [repo根]        # 检查(默认,零写入,check-only 不选边)
  python3 scripts/i18n-check.py --stamp en/<相对路径> [repo根]
                                               # 显式写操作:回译完成后把该 en 文件
                                               # 的 zh-hash 更新为当前 zh 源 hash。
                                               # 只提供单文件粒度,无批量(过期标记是
                                               # 漂移证据,只能逐文件回译后显式消除)。

约定(L1 契约 harness/design/i18n-support/L1-contract-en-mirror-governance.md):
  * en 文件头 frontmatter 必带三字段:lang: en / en-source: <zh相对路径> / zh-hash: <12hex>
  * hash 口径 = 文本 "\\r\\n" 归一为 "\\n" 后 SHA-256 hexdigest 前 12 位
    (防编辑器换行差异假报过期;代价 = 与原始字节 hash 不一致,属有意选择)
  * TRANSLATABLE 白名单 = 「已交付翻译义务」清单(dogfood 修订 2026-08-23:
    随阶段扩容而非一次性全量——L1 §2.3 原文「初始白名单 = L0 首期清单」与 §4.2
    「0 违规才提交」在首期实施窗口冲突,回修为随交付扩容;每阶段把新翻完的文件
    加入,进白名单即负翻译义务,保证检查①恒可全绿)
  * EN_NATIVE = en/ 下原生声明件(无 zh 源,如 License notice),豁免孤儿/缺标记判定

出口码:0 = 无违规;1 = 有违规(供提交前手动门判断)。
"""

import hashlib
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 数据驱动配置(改动须注明出处;与 skills-sync-check 的 EXCEPTIONS 同精神)
# ---------------------------------------------------------------------------

# TRANSLATABLE 白名单:zh 相对路径(glob 模式),进白名单即负翻译义务。
# 出处:ADR-0025 决策 4 + L1 §2.3;首期采用随阶段扩容(dogfood 修订 2026-08-23)。
# 当前进度:P3 完成(README + docs 五件已交付)。
TRANSLATABLE = [
    "README.md",
    # P3 扩容(2026-08-25,F046 交付,出处 L1 §2.3 + L2 §2 P3):
    "docs/CONTEXT.md", "docs/OPEN-DECISIONS.md",
    "docs/methodology/methodology_v5.md",
    "docs/methodology/philosophy_v7.md",
    "docs/methodology/practical_v1.md",
    # P4 后加入: "skills/*/SKILL.md",
    # P5 后加入: "CHANGELOG.md",
]

# EN_NATIVE:en/ 下原生声明件(相对 en/ 的路径),无 zh 源,豁免孤儿/缺标记/过期。
# 出处:L1 §2.4。
EN_NATIVE = [
    "docs/LICENSE",  # CC-BY 翻译声明件(法律文本本身不翻译,ADR-0025 决策 4)
]

LANG_KEYS = ("lang", "en-source", "zh-hash")
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
KV_RE = {k: re.compile(rf"^{re.escape(k)}:\s*(\S+)\s*$", re.MULTILINE) for k in LANG_KEYS}
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def norm_hash(path: Path) -> str:
    """规范化 hash:文本 \r\n→\n 后 SHA-256 前 12 位(L1 §2.1 / 本脚本 docstring)。"""
    text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def parse_frontmatter(text: str):
    """返回 frontmatter 块内三字段的 dict;无 frontmatter 块返回 None。"""
    m = FM_RE.match(text)
    if not m:
        return None
    block = m.group(1)
    fields = {}
    for k in LANG_KEYS:
        km = KV_RE[k].search(block)
        if km:
            fields[k] = km.group(1)
    return fields


def expand_translatable(repo: Path):
    """把白名单 glob 模式展开为实际存在的 zh 文件集合。"""
    files = []
    for pattern in TRANSLATABLE:
        if "*" in pattern:
            files.extend(sorted(str(p.relative_to(repo)) for p in repo.glob(pattern) if p.is_file()))
        else:
            f = repo / pattern
            if f.is_file():
                files.append(pattern)
            else:
                # 白名单点名但文件不存在:数据错误,按缺源报出(防白名单腐化)
                files.append(pattern)
    return files


def collect_en_files(en_root: Path):
    """en/ 下全部 .md 文件(相对 en/ 路径);EN_NATIVE 豁免三类判定但仍查断链。"""
    if not en_root.is_dir():
        return []
    return sorted(str(p.relative_to(en_root)) for p in en_root.rglob("*.md") if p.is_file())


def check_links(en_file: Path, en_rel: str, out: list):
    """检查 en 文件内 Markdown 相对链接目标存在(http(s)/mailto/锚点跳过)。"""
    text = en_file.read_text(encoding="utf-8", errors="replace")
    # 去掉代码块,防示例链接误报
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]*`", "", text)
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = target.split("#", 1)[0]
        if not path_part:
            continue  # 纯锚点
        candidate = (en_file.parent / path_part).resolve()
        if candidate.exists():
            continue
        out.append(f"[断链] en/{en_rel} -> {target}")


def main() -> int:
    args = [a for a in sys.argv[1:]]
    stamp = None
    if args and args[0] == "--stamp":
        if len(args) < 2:
            print("用法: i18n-check.py --stamp en/<相对路径> [repo根]")
            return 2
        stamp = args[1].removeprefix("en/")
        args = args[2:]

    repo = Path(args[0]).resolve() if args else Path(__file__).resolve().parent.parent
    en_root = repo / "en"

    # --stamp 模式:单文件显式写操作(L2 §1.4)
    if stamp is not None:
        en_file = en_root / stamp
        if not en_file.is_file():
            print(f"[错误] en 文件不存在: en/{stamp}")
            return 2
        fields = parse_frontmatter(en_file.read_text(encoding="utf-8", errors="replace"))
        if not fields or "en-source" not in fields:
            print(f"[错误] en/{stamp} 缺 frontmatter 或 en-source 字段,无法定位源")
            return 2
        zh_file = repo / fields["en-source"]
        if not zh_file.is_file():
            print(f"[错误] zh 源不存在: {fields['en-source']}(先处理孤儿)")
            return 2
        # 前置校验(grill-Q Q2 裁决 A,程序防御):en mtime 早于 zh 源 → 译文可能未基于
        # 最新源回译,拒绝盖戳。启发式(可被 touch 绕过),最后一道防线仍是人审。
        if en_file.stat().st_mtime < zh_file.stat().st_mtime:
            print(f"[拒绝] en/{stamp} 的 mtime 早于 zh 源 {fields['en-source']}——"
                  f"译文可能未基于最新源回译;先完成回译再 stamp(不能为消红直接盖戳)。")
            return 2
        new_hash = norm_hash(zh_file)
        content = en_file.read_text(encoding="utf-8")
        content, n = re.subn(rf"({re.escape('zh-hash')}:\s*)\S+",
                             rf"\g<1>{new_hash}", content, count=1)
        if n == 0:
            print(f"[错误] en/{stamp} 无 zh-hash 行可更新")
            return 2
        en_file.write_text(content, encoding="utf-8")
        print(f"已更新 en/{stamp} 的 zh-hash = {new_hash}(依据当前 {fields['en-source']})")
        return 0

    # 检查模式:零写入
    violations = {"缺镜像": [], "孤儿": [], "过期": [], "缺标记": [], "断链": []}
    notes = []

    # ① 结构镜像:白名单 zh 文件必须有 en 对映
    for zh in expand_translatable(repo):
        if not (repo / zh).is_file():
            violations["缺镜像"].append(f"[缺镜像] {zh}: 白名单点名但 zh 源不存在(白名单腐化?)")
            continue
        if not (en_root / zh).is_file():
            violations["缺镜像"].append(f"[缺镜像] {zh}: 缺 en/{zh}")

    # ② 源指纹 + 孤儿 + 缺标记(逐 en 文件)
    for rel in collect_en_files(en_root):
        en_file = en_root / rel
        if rel in EN_NATIVE:
            notes.append(f"en/{rel}: EN_NATIVE 原生声明件(合法豁免)")
            check_links(en_file, rel, violations["断链"])
            continue
        fields = parse_frontmatter(en_file.read_text(encoding="utf-8", errors="replace"))
        if fields is None:
            violations["缺标记"].append(f"[缺标记] en/{rel}: 无 frontmatter 块")
            check_links(en_file, rel, violations["断链"])
            continue
        missing = [k for k in LANG_KEYS if k not in fields]
        if missing:
            violations["缺标记"].append(f"[缺标记] en/{rel}: 缺字段 {'/'.join(missing)}")
            check_links(en_file, rel, violations["断链"])
            continue
        zh_rel = fields["en-source"]
        zh_file = repo / zh_rel
        if not zh_file.is_file():
            violations["孤儿"].append(f"[孤儿] en/{rel}: zh 源不存在 {zh_rel}")
        elif fields["zh-hash"] != norm_hash(zh_file):
            violations["过期"].append(
                f"[过期] en/{rel}: zh 源 {zh_rel} 已变(记录 {fields['zh-hash']} ≠ 当前),待回译")
        check_links(en_file, rel, violations["断链"])

    # 「已翻未入册」提示(grill-Q Q3 裁决 C:翻完忘扩 TRANSLATABLE = 漂移检查静默
    # 缺口;note 行非违规,漏扩容兜底)
    listed = set(expand_translatable(repo))
    for rel in collect_en_files(en_root):
        if rel in EN_NATIVE:
            continue
        f2 = parse_frontmatter((en_root / rel).read_text(encoding="utf-8", errors="replace"))
        if f2 and f2.get("en-source") and f2["en-source"] not in listed:
            notes.append(f"en/{rel}: 已翻但 zh 源 {f2['en-source']} 不在翻译义务清单"
                         f"(TRANSLATABLE)——漏扩容?(grill-Q Q3 note)")

    # 输出(仿 skills-sync-check 风格)
    total = 0
    for cat in ("缺镜像", "孤儿", "过期", "缺标记", "断链"):
        items = violations[cat]
        if items:
            print(f"\n== {cat}({len(items)}) ==")
            for line in items:
                print(line)
            total += len(items)
    if notes:
        print()
        for n in notes:
            print(n)
    if total:
        print(f"\n共 {total} 处漂移。回译/补镜像后用 --stamp 显式消除;哪侧为准是语义判断,由人定。")
        return 1
    print(f"i18n 检查通过:镜像/标记/指纹/链接 0 违规(en 文件 {len(collect_en_files(en_root))} 个)。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
