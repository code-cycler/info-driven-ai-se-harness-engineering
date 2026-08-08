# doctor-harness · harness 演进 CHANGELOG

> harness 组织变更(迁移/规则修订)记录于此,可回溯「harness 为什么长这样」。追加式,只增不改。

## 2026-08-08 · 分层落地(首次)

- **变更**:harness/design/ 按 ADR-0012 判定句确认分层(methodology 裸放 + feature 子目录),修复归档问卷 9 处层级链接(../→../../)。
- **原因**:压测发现 harness 管理无层次化规则;用户裁决严格归 harness/ 父级 + 子文件夹分层,不污染项目根。
- **依据**:ADR-0012 / ADR-0013。

## 2026-08-08 · 归档子目录化(整批迁移)

- **变更**:harness/questionnaires/archive/ 41 份归档按 feature/主题整批迁移至 10 子目录(methodology/ repo-design/ skill-spec-revamp/ doctor-harness/ skills-harness-consistency/ ai-autonomy/ preaction-confirm/ merge-grill-family/ harness-file-mgmt/ _misc/);建 archive/README.md 索引;归档问卷相对链接层级重算(移入子目录加深);修复 doctor-harness 压测问卷 1 处仓库根链接。
- **原因**:用户「整理当前项目的 harness 文件」裁决——归档平铺膨胀检索困难(HARNESS-RULES 第四节由「存量不挪」修订为「允许整批迁移」)。
- **依据**:HARNESS-RULES 第四节(2026-08-08 修订)+ MIGRATION-FLOW 7 步;断链回归 0 新增。