# doctor-harness · harness 演进 CHANGELOG

> harness 组织变更(迁移/规则修订)记录于此,可回溯「harness 为什么长这样」。追加式,只增不改。

## 2026-08-08 · 分层落地(首次)

- **变更**:harness/design/ 按 ADR-0012 判定句确认分层(methodology 裸放 + feature 子目录),修复归档问卷 9 处层级链接(../→../../)。
- **原因**:压测发现 harness 管理无层次化规则;用户裁决严格归 harness/ 父级 + 子文件夹分层,不污染项目根。
- **依据**:ADR-0012 / ADR-0013。