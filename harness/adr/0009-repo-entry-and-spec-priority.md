# ADR-0009: 仓库入口与规范优先级(三区模型 + 唯一权威处)

- 日期:2026-08-05
- 状态:accepted
- 来源:repo 级 design-Q(hld W00 #1-4 + Q1 自定义「harness 依赖文件与项目文件分开」+ 小波澄清「物理目录分离」)+ grill-Q 压测回灌(Q1 skill 路径同步 / Q10 AGENTS.md 零内容 / Q12 协调注)

## 背景

CLAUDE.md 9.5KB 承载方法论摘要 + skill 家族 + 铁律 + 状态 + 导航(harness 入口文件与项目内容混放);无 AGENTS.md(Codex / GitHub 规范入口缺失);docs/ 下混放项目文件(docs/methodology/、CONTEXT、ADR)与 AI 流程产物(docs/design/ 设计文档、docs/questionnaires/ 问卷)。用户裁决:「harness 依赖文件与项目文件分开,docs 默认是项目文件」。

## 决策

1. **三区物理分离模型**(2026-08-05 修订:用户裁决 adr/ 亦移入 harness):
   - **项目文件区** `docs/`:方法论三块(方法论 + 哲学 + 实操)、CONTEXT、OPEN-DECISIONS、LICENSE。
   - **harness 依赖区** `harness/`(决策记录 + AI 流程产物):adr/(架构决策记录,2026-08-05 移入)、design/(设计文档套 + repo 级设计套)、questionnaires/(归档问卷)。
   - **根级入口与产物**:CLAUDE.md / AGENTS.md / README(工具约定必须留根,只做路由)+ skills/ scripts/ .claude/。
2. **规范优先级声明(CLAUDE.md「规范优先级」节,唯一权威处,不复制到其他文件)**:
   **方法论主张(方法论 + 哲学文件,canonical)> ADR > CONTEXT 术语 > skill 规格(SKILL.md + DESIGN.md 同层)> 实操文件**。冲突按序裁决,且必须显式说明,不静默选择。协调注:ADR 中的术语定义以 CONTEXT 为准(ADR 记决策,CONTEXT 记活术语)。
3. **CLAUDE.md 瘦身**(9.5KB → 6KB):6 节结构(定位 / 规范优先级 / 导航 / license + skill 家族 / 铁律 / 状态),方法论摘要压缩指向方法论文件。
4. **AGENTS.md 新增,零内容路由**(<30 行):读 CLAUDE.md + 指向 docs 的链接 + Codex 专属约束;不放清单/表(双入口零内容 = 零漂移,选读表只在 CLAUDE.md 一处)。
5. **skill 落盘路径随迁移同步**(5 个 skill 的 SKILL.md/DESIGN.md + CLAUDE.md 落盘速查表:docs/questionnaires/ → harness/questionnaires/)——路径字符串替换是规格同步,skill 行为逻辑不变。

## 替代方案

- **职责分离(不物理移动)**:harness 入口只做路由、内容归 docs/,不移动文件。用户裁决否决——选物理目录分离。
- **AGENTS.md 全量单源**(「项目A」模式):本仓库已有 ADR + OD-4 规范体系,全量复制 = 制造新同步源(引擎四副本漂移教训,OD-8)。否决。
- **规范优先级独立文件**(如 docs/RULES.md):裁决依据必须「在场」(CLAUDE.md 自动加载可见),独立文件依赖读者主动打开。否决。
- **docs/ 目录级重排**:链接大面积失效,回归成本高;标注归属 + 物理分离已够。否决。

## 后果

- (+) 入口收敛:读者从任一入口(CLAUDE.md / AGENTS.md / README)可达全部权威文档;规范优先级冲突时可指出听谁的。
- (+) harness 区物理分离,项目文件区纯净。
- (−) 迁移 = 44 文件 129 处链接改造(已执行,断链仅豁免项)。
- (−) skill 规格路径同步 = 机制级变更声明(与 OD-8「保留现状」精神需在 DESIGN.md 声明——路径同步非引擎内容统一)。
