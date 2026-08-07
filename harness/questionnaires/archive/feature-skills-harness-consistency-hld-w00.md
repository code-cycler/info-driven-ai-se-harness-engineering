---
mode: feature
wave: w00
stage: hld
created: 2026-08-07
status: archived
slug: skills-harness-consistency
title: 撤销方案 R + 重建 skills/ 一致性(hld · W00 preview)
---
# W00 preview · hld 决策默认值清单

> **背景(已确认,非决策点)**:用户决策 = ① 放弃方案 R(路径配置化);② harness 三件(design/ + questionnaires/ + adr/)硬编码写死 `项目根/harness/`;③ CONTEXT/OPEN-DECISIONS/TODO/docs·retro/ 维持项目固有位置(ADR-0009 三区模型不动)。
> **本轮盘问**:在「本仓库 `skills/`(硬编码 harness/,符合要求)」与「`~/.claude/skills/`(方案 R 配置化,且与仓库漂移 30 文件)」已漂移的前提下,怎么撤销方案 R、保留该保留的、重建两套一致性。
> **作答规则**(opt-in 开关默认关):`勾 [x]` = 采纳 AI 默认倾向、按此落盘;`留空` = 不采纳、转 W01 单独深究。单向门要点永不预勾。底部「补充声明」可自由书写。

## 同步策略与边界(hld 关键决策)

- [X]  **D1. 同步策略方向** — AI 默认倾向:**以本仓库 `skills/` 为权威骨架**(硬编码 harness/ 已符合要求,ADR-0001 source of truth),从 `~/.claude/skills/` 挑出「该保留的改动」回灌仓库,撤销方案 R 的路径配置化,脱敏后双向同步,最终两套一致。来源:ADR-0001 + 用户「放弃方案 R」决策。
- [X]  **D2. 撤销范围** — AI 默认倾向:**仅撤销方案 R 的路径配置化部分**(design-Q/grill-Q/retro-Q/action-Q 的 PROCESSING-RULES 落盘映射 `<根>`→`harness/`、SKILL.md「确定落盘根」子步删除、long-running §5.3 归档路径、design-Q DESIGN.md 的 D23 路径决策/D26);非路径改动一律不动。来源:skill-spec-revamp/LLD §2.2–2.6 + 用户「仅 harness 三件」边界。
- [X]  **D3. F007 骨架改造处置** — AI 默认倾向:**保留并回灌仓库**(判别法则节 / 反简化声明 / 最小必含子块 H1–H5·L1–L5 / 分档节——这是 STAGE-SKELETONS 内容增强,**与方案 R 路径无关**,别因放弃方案 R 连它一起扔)。来源:F007 = design-Q STAGE-SKELETONS,路径在 PROCESSING-RULES/SKILL,两件事独立。
- [X]  **D4. 脱敏处理** — AI 默认倾向:回灌时把 `~/.claude` 版的真实项目名替换为占位(项目A/B/C/某 GUI 库/某结构性种类),保持仓库脱敏(OD-1 发布门槛)。来源:delegate/DESIGN.md diff 实证 + OD-1。
- [X]  **D5. feature_list F007–F010 处置** — AI 默认倾向:F008/F009/F010(路径配置化相关)标注「方案 R 已于 2026-08-07 放弃,撤销」、`passes` 改回 `false` 或加废弃标记;F007(骨架改造)若 D3 采纳则标注「保留、已回灌」。**不删历史记录**(原始 notes 留存)。来源:long-running 铁律(passes 必须真实)+ OD-10。
- [X]  **D6. skill-spec-revamp 设计文档处置** — AI 默认倾向:在 `harness/design/skill-spec-revamp/` 三件(LLD/HLD/VISION)**顶部加标注**「路径配置化(方案 R)部分已于 2026-08-07 放弃,回归硬编码 harness/;骨架改造(F007)部分保留」;**不删设计文档**(留历史,符合「原始信息不丢失」)。来源:铁律 4。
- [X]  **D7. 执行顺序** — AI 默认倾向:**先改仓库(`skills/` 权威),再同步到 `~/.claude/skills/`(运行副本)**;每步独立 DoD + 脱敏门 0 命中。来源:ADR-0001 source of truth 在仓库。
- [X]  **D8. 坍缩档确认** — AI 默认倾向:**vision 省略**(目标已由用户决策明确)+ **hld**(本波:同步策略/边界)+ **lld**(下一步:分步执行清单 + 每步 DoD)。不另起 vision 波。来源:design-Q 坍缩规则(D19)。

---

## 补充声明(✍️ 自由书写,agent 处理时必读)

<!--
(对上述默认倾向的纠正、额外约束、或你想补充的边界,写在这里)
-->

---

## 处理报告(2026-08-07,agent 解析)

- 作答:D1–D8 全部勾选 [X](全采纳 AI 默认倾向);补充声明空(无纠正)。
- 解析:无异常,8 决策全采纳,hld 策略定稿。
- 落盘:hld 决策 → `harness/design/feature-skills-harness-consistency/HLD.md`;ADR 候选(放弃方案 R,建议 ADR-0011)待 lld 定编号。
- 去向:hld 闸门 → lld(分步执行清单 + 每步 DoD)→ 转 long-running-agent 执行。
