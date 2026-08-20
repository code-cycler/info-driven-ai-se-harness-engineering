# governance-history-split · design 域 CHANGELOG

> 本 feature 设计文档(L0/L1/migration-map)的治理历史与自身事件记录。ADR-0024 验收 5「增量协议活体」的 design 侧载体——本 feature 执行期产生的治理事件按新协议记录于此。追加式,只增不改。

## 2026-08-20 · P2 design 域迁移执行判据(F041)

- **变更**:① 本 CHANGELOG 建立;② L0 的 CLAUDE.md 域「落点修正 2026-08-20 L1 W00-10」内嵌注记迁本条(原句见下);③ 全 design/ 域盘点结论:**LN 层文件与裸放档的日期行绝大多数为出处引用/裁决出处/版本出处**(设计档案可追溯性的正当结构),非修订记录节——**可迁内容 ≈ 1 处**(本条),repo/ 与 readme-revamp/ 的 LN 文件不建 CHANGELOG(纯空载体不预建),旧三件(VISION/HLD/LLD)为存量豁免档案(待 TODO AI-2 批量迁移),global-backup/ 与 changesets/ 本身是历史档案文件(不动)。
- **影响**: L0-vision-scope-acceptance.md#目标状态画像
- **出处**: [L1 契约](L1-contract-gov-history-split.md)「仅有可迁内容时建」+ ADR-0024

## 2026-08-20 · L0 落点修正(原内嵌注记,自 L0 迁入)

- **内容**:「CLAUDE.md 域(W00-12,落点修正):『仓库状态』节瘦身为当前状态快照(≤5 行)+ 双指针;历史条目迁 **`harness/STATUS-LOG.md`(新载体)**——修正原因:L1 核实根 CHANGELOG.md 记录规则原文『凡采用者可感知的变更必记,纯仓库内部治理不记』,与内部状态史不兼容,W00-12『职责重叠』前提有误;根 CHANGELOG 保持纯对外语义。」——L1 W00-10 裁决,压测前即已执行修正。
- **影响**: L0-vision-scope-acceptance.md#CLAUDE.md 域(现文只留指针)
- **出处**: L1-contract W00 要点 10 + 根 CHANGELOG.md 记录规则原文核实

## 2026-08-20 · 本 feature 自身治理事件(验收 5 抽查基准)

- **事件链**(均已按新协议入各 skill CHANGELOG / 本文件):① ADR-0024 落盘(design-Q 收尾)→ doctor-harness CHANGELOG 记 P0 条;② grill-Q 压测 10 项修订执行 → ADR-0024 补 Q2 特例与回灌注;③ P0 协议落盘(HARNESS-RULES 第九节 + sync-check 类规则 + 铁律 8)→ doctor-harness CHANGELOG;④ P1 8 skill 迁移 → 8×CHANGELOG;⑤ P2 本条。
- **出处**: ADR-0024 + migration-map_v1
