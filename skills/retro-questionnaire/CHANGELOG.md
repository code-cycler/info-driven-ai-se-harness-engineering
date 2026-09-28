# retro-questionnaire · CHANGELOG

> 本 skill 治理历史(创建起源/引擎同步与漂移时间线)。追加式,只增不改;设计决策见 [DESIGN.md](./DESIGN.md),有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。

## 2026-09-27 · skill-audit 修复批(副本侧,confirm-skill-audit-fix 裁决 Q1/Q2/Q5③ + 中-8)

- **变更**:① 归档规则同步为 D34「处理报告全文制」;② PROCESSING-RULES 新增「修订前置检查(OD-8 执行步骤)」节;③ FORMAT 命名行 LN 旧词清除(改 `retro-<主题>-w<NN>`);④ PR 落盘映射表 pre-LN 旧词三行(vision/hld/lld → VISION.md 等)按 RETRO-SKELETONS 契约替换为 retro 实际落盘(docs/retro/ + TODO.md);⑤ SKILL 归档表述「摘要→全文」;⑥ 主流程末尾补下游衔接(Action Items feature 级新需求 → design-Q/grill-Q,落地前可过 action-Q——补协作图 RETRO→DQ 边的协议缺位);⑦ SKILL 日期注记剥离(见 09-11 条);⑧ FORK-NOTES 登记 ×2。
- **原因**:2026-09-27 skill 体系全量审查([报告 01](../../harness/design/skill-audit/01-report-questionnaire-skills.md) 高-1/高-2/中-6/中-7/中-8/低-2);D34/D38 未同步本副本且零声明。
- **影响**:PROCESSING-RULES/SKILL/FORMAT/FORK-NOTES(已双侧同步);明细 = [归档问卷处理报告](../../harness/questionnaires/archive/)。
- **出处**:问卷 confirm-skill-audit-fix-w00/w01 + [修复计划 05](../../harness/design/skill-audit/05-fix-plan.md) 批次 B。

## 2026-09-11 · 项目搁置/放弃触发(补测式死亡快照)

- **变更**:触发节新增「项目搁置/放弃」——补测式死亡快照:受挫死/自然死从仓库客观状态(feature_list/TODO/git)补判,两行记录(死时状态 + 一句话死因),死后任意时刻可补测(术语见本仓库 CONTEXT「推进受挫谱系」节)。原挂 SKILL.md 规则本体的「(建议非强制,2026-09-09 挑战一深钻)」日期注记,2026-09-27 skill-audit 修复批剥离迁入本条,规则本体只留语义。
- **原因**:2026-09-09 挑战一深钻裁决——项目死亡也需 retro 入口,以补测式死亡快照承载(建议非强制,不阻断正常流程)。
- **影响**: SKILL.md#触发
- **出处**: commit 08580eb

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:① SKILL.md 2 处日期剥离 + 头部索引行;② 引擎 FORMAT 6 处 + PROCESSING 5 处日期剥离,头部标记剥日期;③ DESIGN.md 收敛为决策索引 + 现行副本声明——三个历史事件条目、引擎同步记录 ×2、skill-spec-revamp superseded 节迁本 CHANGELOG;④ 新建 FORK-NOTES.md(双侧一致,5 条分叉)。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md、DESIGN.md、QUESTIONNAIRE-FORMAT.md、PROCESSING-RULES.md、FORK-NOTES.md(新)
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-18 · 引擎规则 4 修正(✍️ 位置)

- **变更**:FORMAT 规则 4——「✍️ 自定义」改为「紧跟所有选项之后、固定为题目最后一位」,消除与规则 13 排序矛盾;本副本模板示例同步更新;四副本 × 双侧同批,无新有意分叉。
- **出处**: grill-Q first-principles W01 补充声明

## 2026-08-06/07 · skill-spec-revamp 同步与撤销(superseded)

- **变更**:落盘路径配置化(方案 R)同步到本 skill(仅运行版曾落地;仓库版从未同步)——**2026-08-07 撤销**(ADR-0011),路径回归硬编码 `harness/`。Q7 裁决:retro 文档落点 `docs/retro/` 为项目固有,不纳入落盘根;skill 内部 `./docs/...` 引用不动。Q5:有意分叉区(RETRO-SKELETONS 四节骨架 / 不使用 preview / 调研与核实前置五源)保留;HLD/LLD 判别法则不扩散。
- **出处**: ADR-0011 + grill-skill-spec-revamp-w01

## 2026-08-03 · 预勾开关化 + 调研与核实前置同步

- **变更**:预勾选 opt-in 开关默认关 + 选项排序统一 + 单向门永不预勾(OD-14 修订);「实测与调研前置」同步为本 skill 变体「调研与核实前置」(五源读取的补齐,弱化实测强调核实)。四副本同步(OD-8 重访触发①命中)。
- **出处**: OD-14 + confirm-pregou-switch-w00 / confirm-testing-preflight-w00(archive/_misc/)

## 2026-07-23/24 · 创建 + 引擎复制与同步

- **变更**:① 创建:design-Q 设计(vision W1/W2 + hld W1 三波问卷,两道闸门,坍缩 LLD 直接实现)——本 skill 是 design-Q 的首个 dogfood 载体;② 引擎复制自 design-Q(07-24);③ 引擎同步(07-24,无漂移):双向门逃生舱改「采用推荐项 + 进 OD 标注」(design-Q D22 发起)。
- **出处**: docs/questionnaires/archive/ + design-Q CHANGELOG

## 2026-07-25/27 · preview 漂移两次(声明为设计)

- **变更**:design-Q canonical 演进 preview 预答层(07-25)与 preview 拆独立 W00 波(07-27),本 skill 均不同步——**复盘问卷题量小、通常一波,题型是反思原因假设清单,不适合 yes/no 默认值预答**(项目B dogfood Q5-A 判定:复盘场景 preview 价值不抵复杂度);三方协议下声明为设计(非遗漏)。
- **出处**: design-Q 演进 + 项目B dogfood(现值 = FORK-NOTES 分叉 1)
