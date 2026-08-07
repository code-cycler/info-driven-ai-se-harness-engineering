# HLD · 撤销方案 R + 重建 skills/ 一致性

> 来源:feature-skills-harness-consistency hld W00(2026-08-07,D1–D8 全采纳,问卷归档 `harness/questionnaires/archive/feature-skills-harness-consistency-hld-w00.md`)。
> 上游决策:用户「放弃方案 R,硬编码 harness 三件,固有文件不动」(confirm-skill-harness-sink-w00 补充声明 + hld W00 D1–D8)。
> 下游:LLD(分步执行清单 + DoD)→ long-running-agent 执行。

## 目标

撤销方案 R(路径配置化:读 CLAUDE.md 声明 → 默认 → 落盘前确认),回归**硬编码 `项目根/harness/`**(design/ + questionnaires/ + adr/);重建本仓库 `skills/` 与 `~/.claude/skills/` 的一致性(已漂移约 30 文件);CONTEXT.md / OPEN-DECISIONS.md / TODO.md / docs·retro/ 维持项目固有位置(ADR-0009 三区模型不动)。

## 关键决策(hld W00 D1–D8,全采纳)

| # | 决策 |
|---|---|
| D1 | 同步策略:本仓库 `skills/` 为权威骨架(ADR-0001),从 `~/.claude/skills/` 挑保留项回灌,撤销方案 R,脱敏后双向同步 |
| D2 | 撤销范围:仅方案 R 路径配置化;非路径改动不动 |
| D3 | F007 骨架改造(判别法则/反简化/最小必含/分档)保留并回灌——与路径无关 |
| D4 | 回灌真实标识 → 占位脱敏(OD-1) |
| D5 | feature_list F008/09/10 标撤销(passes 改回 false/废弃标记)、F007 标回灌,不删历史 |
| D6 | skill-spec-revamp 设计文档顶部标注「路径配置化部分放弃,骨架部分保留」,不删 |
| D7 | 执行顺序:先仓库(git 权威)后 `~/.claude`(运行副本) |
| D8 | 坍缩:vision 省(目标已明确)+ hld + lld |

## 撤销 / 保留范围(hld 边界,文件级)

**撤销(方案 R 路径配置化 → 硬编码 `harness/`)**:
- design-Q:SKILL.md「确定落盘根」子步删除、PROCESSING-RULES 落盘映射 `<根>`→`harness/`、QUESTIONNAIRE-FORMAT 文件约定、DESIGN.md D23(路径配置化)/D26
- grill-Q / retro-Q / action-Q:PROCESSING-RULES 落盘映射 + SKILL 路径决定 + QUESTIONNAIRE-FORMAT 文件约定
- long-running-agent:SKILL.md §5.3 归档问卷路径配置化

**保留回灌(非路径,从 `~/.claude` 取)**:
- F007:design-Q STAGE-SKELETONS 判别法则节 / 反简化声明 / 最小必含子块(H1–H5·L1–L5)/ 坍缩分档节
- 各 skill 的 dogfood 修订(内容增强,逐文件判定)

**不动**:
- 本仓库 `skills/`(已硬编码 `harness/`,符合要求)
- CONTEXT.md / OPEN-DECISIONS.md / TODO.md / docs·retro/(项目固有,三区模型)

## 同步契约(架构)

- **仓库 `skills/`**(脱敏、git、source of truth)= 权威
- **`~/.claude/skills/`**(未脱敏、本地、运行副本)= 部署目标
- 改仓库 → 脱敏版覆盖 `~/.claude` 对应文件 → 两套一致(仅脱敏差异保留:仓库占位、`~/.claude` 真实名)

## ADR 识别(H5)

「放弃方案 R 回归硬编码」判三条件:① 难逆转 = 中等(改回配置化可逆,但 skill 若已分发则半单向);② 会困惑 = 是(未来读者疑问件 R 为何放弃);③ 真权衡 = 是(配置化 vs 硬编码有 dogfood 数据支撑)。→ **三条件满足,建议立 ADR-0011**(lld 执行时定稿)。

## 已知风险

| 风险 | 缓解 |
|---|---|
| 回灌时误带方案 R 残留 | 每文件改后 grep「落盘根\|`<根>`\|确定落盘\|声明命中」0 命中(运行版),仓库版本就 0 |
| 脱敏遗漏(真实名进仓库) | 回灌后跑 `scripts/desensitize.py` + 人审(OD-1 三道门) |
| `~/.claude` 与仓库同步二次漂移 | 同步作为 lld 显式步骤,DoD = diff 仅剩脱敏差异 |
