# grill-with-docs · CHANGELOG

> 本 skill 治理历史。本 skill 无 DESIGN.md(决策直接进 SKILL.md 规则本体与 CONTEXT/ADR/OD);无规则本体级双侧分叉(非引擎副本),故无 FORK-NOTES。追加式,只增不改。

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:SKILL.md 7 处日期注记剥离(含 description)+ 头部索引行;OPEN-DECISIONS-FORMAT 1 处剥离;新建本 CHANGELOG(此前历史散在 SKILL.md 注记,现集中于此);维持无 DESIGN.md(历史迁 CHANGELOG 后不新建)。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md、OPEN-DECISIONS-FORMAT.md
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-19 · 通用模式新增(承载 grill 生态位)+ 边界深钻三精确化

- **变更**:① 新增通用模式(不绑库 + 零留痕纯对话),承载 grill 退役后的「通用 × 单点深钻」生态位;② 深钻精确化:可操作判别(适用三情景 + 反边界)/ 误判兜底两道(入口确认 + 中途切回)/ 零留痕边界(AI 提议 + 人拍板,替代原 grill「仅用户明确要求才写」的被动式);③ 中途相变条款(发现批量性 → 提议转 grill-Q);④ 通用模式规格深钻首用(元问题场景验证可承载)。
- **背景**:grill 退役(OD-12 观察期终止,用户显式裁决——grill 派生自 mattpocock grill-with-docs、适用场景少);grill 边界深钻四分支(认知状态三态接线/入口+中途双检测/校准闸门+题级标注双件/优化回路 OD-26)。
- **影响**: SKILL.md#模式、#中途相变、#判定
- **出处**: OD-12 + grill 边界深钻会话 + grill-boundary-canonical-w01(archive/_misc/)

## 2026-07-24 · 逃生舱机制与 questionnaire 家族对齐

- **变更**:双向门逃生舱改「采用推荐项 + 仍进 OD 标注 provisional」(信息不丢失;与 design-Q D22 / grill-Q D23 同批对齐)。
- **出处**: design-Q dogfood W01 补充声明(家族三方同步)
