#!/usr/bin/env python3
"""脱敏检查/替换脚本(OD-1 DoD ①)。

扫描 .md 文件中的敏感词(项目名 / 路径 / 人名):
  --check   只报告命中,不改文件(发布前 DoD:要求 0 命中)
  --apply   按映射表执行替换

映射表机制(2026-07-29 起外置):
  真实「敏感词 → 替换词」映射表在本地文件 scripts/desensitize_map.local.json
  (gitignored,不入库)——公开仓库中的本脚本不含真实名,防映射本身随仓库泄漏。
  未找到映射文件时以空映射运行:check 报告「未加载映射表」并视为 0 命中
  (公开克隆者无害空转;作者本地有映射文件,门照常工作)。

用法:
  python3 scripts/desensitize.py .                       # check 全仓库
  python3 scripts/desensitize.py skills docs/questionnaires --apply
  python3 scripts/desensitize.py . --exclude docs/methodology
"""
import argparse
import json
import re
from pathlib import Path

MAP_FILE = Path(__file__).parent / "desensitize_map.local.json"


def load_replacements():
    """从本地映射文件加载(敏感词 → 替换词);不存在则返回空映射(公开仓库常态)。

    映射约定:语义化占位;项目名用「项目X」占位,归档示例语境可读。
    """
    if MAP_FILE.is_file():
        return json.loads(MAP_FILE.read_text(encoding="utf-8"))
    return {}


def build_pattern(replacements):
    return re.compile("|".join(re.escape(k) for k in replacements))


def iter_files(roots, exclude):
    for root in roots:
        for p in Path(root).rglob("*.md"):
            if not p.is_file():
                continue
            if exclude and any(e in str(p) for e in exclude):
                continue
            yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--exclude", nargs="*", default=[])
    args = ap.parse_args()

    replacements = load_replacements()
    if not replacements:
        print(f"⚠️ 未找到映射文件 {MAP_FILE},以空映射运行(公开仓库常态;作者本地应有该文件,见脚本 docstring)。")
        print("合计 0 处命中,0 个文件。")
        return

    pat = build_pattern(replacements)
    hits = {}
    for p in iter_files(args.roots, args.exclude):
        text = p.read_text(encoding="utf-8")
        found = pat.findall(text)
        if found:
            hits[p] = found

    total = sum(len(v) for v in hits.values())

    if not args.apply:
        for p, found in sorted(hits.items()):
            counts = {w: found.count(w) for w in sorted(set(found))}
            print(f"{p}: {len(found)} 处 {counts}")
        print(f"\n合计 {total} 处命中,{len(hits)} 个文件。--check 模式未修改;加 --apply 执行替换。")
        return

    for p, found in hits.items():
        text = p.read_text(encoding="utf-8")
        new = pat.sub(lambda m: replacements[m.group(0)], text)
        p.write_text(new, encoding="utf-8")
    print(f"已替换 {total} 处,{len(hits)} 个文件。")


if __name__ == "__main__":
    main()
