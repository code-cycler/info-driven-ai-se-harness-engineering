#!/usr/bin/env python3
"""skill 体系内容真实性断言脚本(2026-09-27 skill-audit 修复批 Q5①,confirm-skill-audit-fix W01)。

背景:「有脚本的地方不漂移,靠人肉清单的地方必漏」——双侧同步/脱敏/i18n 三道门
均为机器断言(该次审查 0 违规),而 skill 计数与主线状态全靠人肉联动清单维护,
产生该批高危 3 条(CLAUDE.md 状态节过期、README 中英残留旧计数、TODO 滞后于
feature_list)。本脚本补第四道机器断言:

  A. skill 计数一致性(宽松模式,防「8 个核心方法论 skill」类变体漏网——
     F051 验收用精确子串 grep 的教训):skills/ 目录实数 vs 全仓已知计数表述;
     含「收为/增为/曾经/历史」等叙事词的行视为历史注记,不计入断言
  B. TODO 主线 vs feature_list:passes=true 的 feature 仍列于 TODO 未勾
     `- [ ]` 清单 → 违规;TODO 已勾 `- [x]` 而 passes 未 true → 提示

check-only:只报告,绝不修改文件。
用法:
  python3 scripts/audit-check.py                 # repo 根 = 脚本上级目录
  python3 scripts/audit-check.py /path/to/repo   # 显式指定 repo 根

EXIT 码:0 = 无违规;1 = 有违规(供提交前例行检查/钩子使用)。
"""
import json
import re
import sys
from pathlib import Path

# 计数表述扫描面(中文文件 + en 镜像;新增双写点须同步扩此表)
COUNT_FILES = [
    "CLAUDE.md",
    "README.md",
    "TODO.md",  # 只扫头部状态区(前 12 行)
    "docs/methodology/practical_v1.md",
    "docs/methodology/philosophy_v7.md",
    "docs/CONTEXT.md",
    "en/README.md",
]
# 中文数字映射(计数表述用)
CN_NUM = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}
# 历史注记豁免词:行内含这些词 → 该行计数为叙事(如「9 收为 8」),不断言
# (「✅」豁免历史完成行,如 TODO 时间线「✅ 复制 7 个核心方法论 skill」)
HIST_WORDS = ("收为", "增为", "曾经", "历史", "v4 时期", "旧编号", "✅")
# 计数模式:中文「N 个(核心)?(方法论 )?skill」/ 英文「the N core ... skills」
RE_ZH = re.compile(r"([0-9]{1,2}|[一二三四五六七八九十]{1,3})\s*个\s*(?:核心\s*)?(?:方法论\s*)?skill")
RE_EN = re.compile(r"the\s+([0-9]{1,2})\s+core", re.IGNORECASE)
# feature 区间引用形态:F039-F043 / F039–F043
RE_FRANGE = re.compile(r"F(\d+)\s*[-–]\s*F(\d+)")
RE_FONE = re.compile(r"F(\d{3,4})")
RE_TODO_OPEN = re.compile(r"^\s*-\s*\[\s\]\s")
RE_TODO_DONE = re.compile(r"^\s*-\s*\[x\]\s", re.IGNORECASE)


def to_int(tok: str) -> int | None:
    if tok.isdigit():
        return int(tok)
    # 中文数字(仅支持十以内与十)
    if tok == "十":
        return 10
    if len(tok) == 1:
        return CN_NUM.get(tok)
    if len(tok) == 2 and tok[0] == "十":
        v = CN_NUM.get(tok[1])
        return 10 + v if v else None
    if len(tok) == 2 and tok[1] == "十":
        v = CN_NUM.get(tok[0])
        return v * 10 if v else None
    return None


def feature_ids_in(line: str) -> set[str]:
    """提取该行引用的 feature id 集合(展开 F039-F043 区间形态)。"""
    ids: set[str] = set()
    consumed: list[tuple[int, int]] = []
    for m in RE_FRANGE.finditer(line):
        a, b = int(m.group(1)), int(m.group(2))
        if a < b and b - a < 60:  # 防误配(如 F1-F2 页码)
            ids.update(f"F{n:03d}" for n in range(a, b + 1))
            consumed.append(m.span())
    for m in RE_FONE.finditer(line):
        if any(s <= m.start() < e for s, e in consumed):
            continue
        ids.add(f"F{int(m.group(1)):03d}")
    return ids


def check_counts(repo: Path, actual: int) -> tuple[list[str], list[str]]:
    violations: list[str] = []
    notes: list[str] = []
    for rel in COUNT_FILES:
        f = repo / rel
        if not f.is_file():
            notes.append(f"[count] {rel}: 文件不存在(跳过)")
            continue
        lines = f.read_text(encoding="utf-8").splitlines()
        head_only = rel == "TODO.md"
        for i, line in enumerate(lines, 1):
            if head_only and i > 6:  # 只扫头部状态区(当前状态 + 下一步主线)
                break
            if any(w in line for w in HIST_WORDS):
                continue
            for m in list(RE_ZH.finditer(line)) + list(RE_EN.finditer(line)):
                n = to_int(m.group(1))
                if n is None:
                    continue
                if n != actual:
                    violations.append(
                        f"[count] {rel}:{i}: 计数 {n} != 实际 {actual} —— {line.strip()[:80]}"
                    )
                else:
                    notes.append(f"[count] {rel}:{i}: 计数 {n} = 实际(OK)")
    return violations, notes


def check_todo_vs_features(repo: Path) -> tuple[list[str], list[str]]:
    violations: list[str] = []
    notes: list[str] = []
    fl_path = repo / ".claude" / "feature_list.json"
    todo_path = repo / "TODO.md"
    if not fl_path.is_file() or not todo_path.is_file():
        notes.append("[todo] feature_list.json 或 TODO.md 缺失(跳过)")
        return violations, notes
    data = json.loads(fl_path.read_text(encoding="utf-8"))
    features = data.get("features", []) if isinstance(data, dict) else data
    passes = {}
    for f in features:
        fid, ok = f.get("id"), f.get("passes")
        if isinstance(fid, str) and isinstance(ok, bool):
            passes[fid] = ok
    open_ids: dict[str, str] = {}  # fid -> 行摘录
    done_ids: set[str] = set()
    for i, line in enumerate(todo_path.read_text(encoding="utf-8").splitlines(), 1):
        ids = feature_ids_in(line)
        if not ids:
            continue
        if RE_TODO_OPEN.match(line):
            for fid in ids:
                open_ids.setdefault(fid, f"TODO.md:{i}")
        elif RE_TODO_DONE.match(line):
            done_ids.update(ids)
    for fid, loc in sorted(open_ids.items()):
        if passes.get(fid) is True:
            violations.append(f"[todo] {loc}: {fid} 已 passes=true 但 TODO 仍为未勾 `- [ ]` —— {fid} 主线状态滞后")
    for fid in sorted(done_ids):
        if passes.get(fid) is False:
            notes.append(f"[todo] {fid}: TODO 已勾但 feature_list passes=false(非 passes=true 校验口径,提示)")
    return violations, notes


def main() -> int:
    repo = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) > 1
        else Path(__file__).resolve().parent.parent
    )
    skills_dir = repo / "skills"
    if not skills_dir.is_dir():
        print(f"错误: 未找到 skills/ 目录({skills_dir})", file=sys.stderr)
        return 1
    actual = len([p for p in skills_dir.iterdir() if p.is_dir()])

    v1, n1 = check_counts(repo, actual)
    v2, n2 = check_todo_vs_features(repo)
    violations = v1 + v2
    notes = n1 + n2

    print(f"skill 目录实数 = {actual};计数表述扫描 {len(COUNT_FILES)} 文件。")
    for line in violations:
        print(line)
    print(f"-- 提示 {len(notes)} 条(OK 行/跳过/非违规提示,从略;--verbose 可看)--")
    if "--verbose" in sys.argv:
        for line in notes:
            print(line)

    if violations:
        print(f"\n共 {len(violations)} 处内容真实性违规。修复后复跑本脚本。")
        return 1
    print("内容真实性断言通过:计数一致 + TODO 主线与 feature_list 无冲突。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
