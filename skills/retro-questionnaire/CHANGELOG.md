# retro-questionnaire · CHANGELOG

> 本 skill 治理历史(创建起源/引擎同步与漂移时间线)。追加式,只增不改;设计决策见 [DESIGN.md](./DESIGN.md),有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。

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
