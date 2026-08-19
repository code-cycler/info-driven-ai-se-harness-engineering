#!/usr/bin/env python3
"""skill 双侧同步校验脚本(2026-08-19 机制化,confirm-skills-sync-mechanism-w00 全确认)。

对比 repo skills/ 下每个 skill 与 ~/.claude/skills/<同名>/ :
  ① 双向存在性(仅项目有 / 仅全局有的文件)
  ② 两侧共有文件的逐字节内容一致

check-only:只报告差异,绝不修改文件、不做自动选边——哪侧内容正确是语义判断
(2026-08-18 双侧同步的教训:同一批漂移里修订在全局侧对、路径修复在项目侧对,
自动选边必然错一半),处置永远由人决定。

裁决例外(EXCEPTIONS):用户裁决双侧有意不逐字节一致的文件,豁免「内容不同」
不算违规(存在性差异不豁免)。新增例外必须改代码并注明裁决出处,保持例外显式、
可追溯。例外项若两侧重新一致,输出提示建议移除白名单。

用法:
  python3 scripts/skills-sync-check.py                 # repo 根 = 脚本上级目录
  python3 scripts/skills-sync-check.py /path/to/repo   # 显式指定 repo 根

EXIT 码:0 = 无违规;1 = 有违规(供提交前例行检查/钩子使用)。
"""
import sys
from pathlib import Path

# 已知裁决例外:skill 相对路径 → 裁决出处(只豁免「内容不同」,不豁免存在性差异)
EXCEPTIONS = {
    "doctor-harness/CHANGELOG.md": (
        "2026-08-18 用户裁决:外部项目实证条目留全局、仅规则性增补进项目版,"
        "双侧不逐字节一致(confirm-action-q-sync-w00,archive/_misc/)"
    ),
}


def collect_files(root: Path) -> set[str]:
    """收集目录下全部文件的相对路径集合(POSIX 风格)。"""
    return {
        p.relative_to(root).as_posix()
        for p in root.rglob("*")
        if p.is_file()
    }


def main() -> int:
    repo_root = (
        Path(sys.argv[1]).resolve()
        if len(sys.argv) > 1
        else Path(__file__).resolve().parent.parent
    )
    repo_skills = repo_root / "skills"
    global_skills = Path.home() / ".claude" / "skills"

    if not repo_skills.is_dir():
        print(f"错误: 未找到 repo skills/ 目录({repo_skills})", file=sys.stderr)
        return 1
    if not global_skills.is_dir():
        print(f"错误: 未找到全局 skill 目录({global_skills})", file=sys.stderr)
        return 1

    violations: list[str] = []
    exempted: list[str] = []
    stale_exceptions: list[str] = []

    for skill_dir in sorted(p for p in repo_skills.iterdir() if p.is_dir()):
        skill = skill_dir.name
        gdir = global_skills / skill
        if not gdir.is_dir():
            violations.append(f"{skill}: 全局侧缺失整个 skill 目录")
            continue

        p_files = collect_files(skill_dir)
        g_files = collect_files(gdir)

        for rel in sorted(p_files - g_files):
            violations.append(f"{skill}/{rel}: 仅项目侧存在(全局缺失)")
        for rel in sorted(g_files - p_files):
            violations.append(f"{skill}/{rel}: 仅全局侧存在(项目缺失)")
        for rel in sorted(p_files & g_files):
            key = f"{skill}/{rel}"
            if (skill_dir / rel).read_bytes() != (gdir / rel).read_bytes():
                if key in EXCEPTIONS:  # 例外按 skill/相对路径 精确匹配
                    exempted.append(f"{key}: 豁免(裁决出处: {EXCEPTIONS[key]})")
                else:
                    violations.append(f"{key}: 内容不一致")

    for key in EXCEPTIONS:
        skill, _, rel = key.partition("/")
        p_file = repo_skills / skill / rel
        g_file = global_skills / skill / rel
        if p_file.is_file() and g_file.is_file():
            if p_file.read_bytes() == g_file.read_bytes():
                stale_exceptions.append(f"{key}: 例外项两侧已一致,可考虑移除白名单")

    for line in violations:
        print(line)
    for line in exempted:
        print(line)
    for line in stale_exceptions:
        print(line)

    if violations:
        print(f"\n共 {len(violations)} 处漂移。双侧哪侧为准需人判定后手动同步;处理后复跑本脚本。")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
