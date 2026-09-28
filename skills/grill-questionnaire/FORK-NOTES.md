# FORK-NOTES · grill-questionnaire 有意分叉声明

> 仅含有意分叉条目;完整设计决策见项目仓库 skills/grill-questionnaire/DESIGN.md。

- 引擎 QUESTIONNAIRE-FORMAT 规则 15:❌ 跑偏标注为本副本专属行(每题 🤔 之后、★推荐之前),其余三副本不加
- 引擎 PROCESSING-RULES:❌ 跑偏解析行 + 「同波 ≥2 题被标 → 停波回炉」+ 处理报告「质量信号」节为本副本专属
- frontmatter `stage` 固定取 `grill`(无 LN 层概念,压测对象非生成式设计)
- 本 skill 无 preview/W00 独立波(压测单次完整为主、按需补波,W 编号 NN 从 01 递增;对齐 retro-Q 的结构声明粒度补记)
- 命名行本地化:FORMAT 命名行用 `grill-<slug>-w<NN>.md`(slug = 工件短名,kebab-case;NN 从 01 递增),不用引擎模板 LN 层名枚举(skill-audit 修复批 Q2 裁决)
- 归档粒度:处理报告全文制 2026-09-27 skill-audit 修复批已四方同步(design-Q D34 决策收口至本副本,此前本副本为摘要制,漂移已消除)
