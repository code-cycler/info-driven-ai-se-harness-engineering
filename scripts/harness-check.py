#!/usr/bin/env python3
"""harness 布局合规校验脚本(doctor-harness 场景 C)。

检查 harness/ 区三件(design/ + questionnaires/ + adr/)的布局合规:
  ① 问卷命名正则(init/feature/grill/retro/confirm 各模式)
  ② ADR 编号连续(0001 起,无跳号)
  ③ 归档位置(processed/archived 状态的问卷在 archive/)

输出违规清单(逐条「路径: 违规类型」);0 违规时无输出(误报门)。
保守实现:只报格式偏离,不报内容语义(如不判断 slug 是否合理)。

用法:
  python3 scripts/harness-check.py ./harness          # 默认查问卷+ADR
  python3 scripts/harness-check.py ./harness --json   # 结构化输出
"""
import argparse
import json
import re
import sys
from pathlib import Path

# 问卷命名模式(HARNESS-RULES.md 三节;archive/ 内文件同为命名检查对象)
NAME_PATTERNS = {
    "init": re.compile(
        r"^(vision|hld|lld)-w\d{2}(a|b)?\.md$"
    ),
    "feature": re.compile(
        r"^feature-[a-z0-9-]+-(vision|hld|lld)-w\d{2}(a|b)?\.md$"
    ),
    "grill": re.compile(
        r"^grill-[a-z0-9-]+-w\d{2}(a|b)?\.md$"
    ),
    "retro": re.compile(
        r"^retro-[^/]+-w\d{2}(a|b)?\.md$"
    ),
    "confirm": re.compile(
        r"^confirm-[a-z0-9-]+-w\d{2}(a|b)?\.md$"
    ),
}

# 已知豁免(存量已偏离,不清扫;HARNESS-RULES.md 三节豁免清单)
EXEMPT_PREFIXES = ("feature-skill-", "feature-skills-")

ADR_RE = re.compile(r"^(\d{4})-[a-z0-9-]+\.md$")


def check_naming(qdir: Path, violations: list) -> None:
    """① 问卷命名正则:questionnaires/(含 archive/)下 .md 须匹配任一模式或豁免。"""
    if not qdir.is_dir():
        return
    for p in sorted(qdir.rglob("*.md")):
        name = p.name
        if name.startswith(EXEMPT_PREFIXES):
            continue
        if "README" in name:
            continue  # 归档 README 索引豁免
        if not any(pat.match(name) for pat in NAME_PATTERNS.values()):
            violations.append(f"{p.relative_to(qdir.parent)}: 命名不符合问卷模式(init/feature/grill/retro/confirm)")


def check_adr_sequence(adr_dir: Path, violations: list) -> None:
    """② ADR 编号连续:adr/ 下 NNNN-slug.md 编号从 0001 起,无跳号。"""
    if not adr_dir.is_dir():
        return
    nums = []
    for p in adr_dir.glob("*.md"):
        m = ADR_RE.match(p.name)
        if m:
            nums.append(int(m.group(1)))
        else:
            violations.append(f"adr/{p.name}: ADR 文件名不符合 NNNN-slug.md")
    nums.sort()
    if not nums:
        return
    if nums[0] != 1:
        violations.append(f"adr/: ADR 编号应从 0001 起,实际首个 = {nums[0]:04d}")
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            violations.append(f"adr/: ADR 编号跳号 {nums[i-1]:04d} → {nums[i]:04d}(缺 {nums[i-1]+1:04d})")


def check_archive_location(qroot: Path, violations: list) -> None:
    """③ 归档位置:问卷状态 processed/archived 应已移入 archive/;archive/ 外不应有 archived 状态问卷。"""
    archive_dir = qroot / "archive"
    for p in sorted(qroot.glob("*.md")):
        if p == archive_dir:
            continue
        if p.is_file():
            text = p.read_text(encoding="utf-8")
            if re.search(r"^status:\s*(processed|archived)\s*$", text, re.MULTILINE):
                violations.append(f"{p.relative_to(qroot.parent)}: status 为 processed/archived 但未在 archive/")


def collect(harness_root: Path) -> list:
    violations = []
    check_naming(harness_root / "questionnaires", violations)
    check_adr_sequence(harness_root / "adr", violations)
    check_archive_location(harness_root / "questionnaires", violations)
    return violations


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("harness_root", nargs="?", default="./harness")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = Path(args.harness_root)
    if not root.is_dir():
        print(f"harness 目录不存在: {root}", file=sys.stderr)
        sys.exit(1)

    violations = collect(root)

    if args.json:
        print(json.dumps({"harness_root": str(root), "violations": violations,
                          "count": len(violations)}, ensure_ascii=False, indent=2))
    else:
        for v in violations:
            print(v)

    # exit 0(违规存在也 0,人读输出决定;目录不存在才 exit 1)


if __name__ == "__main__":
    main()