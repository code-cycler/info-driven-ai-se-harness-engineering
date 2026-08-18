# doctor-harness · harness 演进 CHANGELOG

> harness 组织变更(迁移/规则修订)记录于此,可回溯「harness 为什么长这样」。追加式,只增不改。

## 2026-08-16 · 第八节补「存量治理文件迁移」+「自包含大文档映射策略」

- **变更**:第八节新增两条:① 存量治理文件迁移(CONTEXT → harness 根;docs/adr/ 整体迁 harness/adr/ 保留原编号、新建续号;断链走 MIGRATION-FLOW);② 自包含大文档(构想+架构+实现合一)映射二选一(单文件多节保整体 / 拆层多文件利演进,判据 = 是否仍频繁整体修订,原文件均保留不删)。
- **原因**:外部项目独立会话测试前的能力补强——测试对象为存量结构改造场景(已有自包含设计文档 + CONTEXT + ADR 目录,无 harness 区),第八节原流程未覆盖这两类形态。

## 2026-08-16 · 第八节增补「构想直生模式」(grill-with-docs 深钻)

- **变更**:第八节新增「构想直生模式」四步(提取归位零改写 / 骨架补全标待补 / 层范围内容驱动·纯空层不预建 / 人确认成档后可转 design-Q 续深化)。
- **原因**:用户深钻指出缺口——「全局没有支持从基础构想文件直接到 LN 的能力」:五步主流程只映射不生成(缺项标待补),design-Q 只认「一句话念头」走问卷,手持构想文件的用户无直达路径。裁决链:载体 = doctor 八节扩展;边界 = 提取+骨架(AI 不新增设计内容,不代写铁律不破);层范围 = 内容驱动(与最小 1 层 + 反形式主义设计原则自洽)。
- **依据**:grill-with-docs 单点深钻 Q1/Q2/Q3 全选推荐。

## 2026-08-16 · P2 拓展先行(feature-designq-digital-levels)

- **变更**:HARNESS-RULES 增补第七节(层级设计文档规则:LN 命名/布局/导览块/存量豁免)与第八节(存量结构改造流程五步 + 旧档迁移映射表);SKILL.md 触发词补「层级改造/迁移/存量规范化」+ 判定场景⑤⑥ + 规则清单扩两行。
- **原因**:design-Q 数字层级改造 P2 doctor 先行(用户优先测试裁决);design-Q 产物结构 VISION/HLD/LLD → LN 制后,doctor 承载层级布局规则 + 旧档迁移 + 无 harness 项目的存量规范化(补充声明「拓展 doctor 任务范围」)。
- **依据**:[HLD §2](项目 harness/design/designq-digital-levels/HLD.md)+ [LLD P2](同 L2);F029。

## 2026-08-14 · 规则三增补 + 引擎副本同步(superseded 流转移植)

- **变更**:① HARNESS-RULES 三增补(用户裁决三项全做):第三节补「活跃区子目录合法化」;第四节补「superseded 问卷处置」;新增第六节「治理文件归属」——OPEN-DECISIONS/TODO/CONTEXT 归 harness/ 根,ADR 归 harness/adr/(无 harness/ 的项目沿用 skill 原约定);顺手修复第五节「见第六节」悬空引用。② 引擎副本同步:QUESTIONNAIRE-FORMAT.md ×4(design-Q canonical + grill-Q + retro-Q + action-Q)status 流转补 superseded 作废分支;7 个 skill 文件的 `docs/OPEN-DECISIONS.md` 硬编码改引用 HARNESS-RULES.md 第六节(action-Q SKILL/PROCESSING-RULES、retro-Q PROCESSING-RULES、grill-Q DESIGN、grill-with-docs SKILL/FORMAT);delegate ×2、doctor-harness DESIGN 中真实项目名历史出处置留不改(2026-08-18 双侧同步已统一为脱敏措辞)。
- **原因**:外部项目治理校验发现 4 个语义层问题(脚本查不出):孤儿未答问卷无处置条款、活跃区子目录无规则背书、OD/TODO 归属规则缺口(本地适配「OD 落 harness/ 根」本次升格为权威规则)、无 adr/ 目录(非违规,记录备查)。
- **依据**:HARNESS-RULES.md 三/四/六节(本次修订)+ 第四节归档规则;harness-check.py 复跑 0 违规。

## 2026-08-08 · 分层落地(首次)

- **变更**:harness/design/ 按 ADR-0012 判定句确认分层(methodology 裸放 + feature 子目录),修复归档问卷 9 处层级链接(../→../../)。
- **原因**:压测发现 harness 管理无层次化规则;用户裁决严格归 harness/ 父级 + 子文件夹分层,不污染项目根。
- **依据**:ADR-0012 / ADR-0013。

## 2026-08-08 · 归档子目录化(整批迁移)

- **变更**:harness/questionnaires/archive/ 41 份归档按 feature/主题整批迁移至 10 子目录(methodology/ repo-design/ skill-spec-revamp/ doctor-harness/ skills-harness-consistency/ ai-autonomy/ preaction-confirm/ merge-grill-family/ harness-file-mgmt/ _misc/);建 archive/README.md 索引;归档问卷相对链接层级重算(移入子目录加深);修复 doctor-harness 压测问卷 1 处仓库根链接。
- **原因**:用户「整理当前项目的 harness 文件」裁决——归档平铺膨胀检索困难(HARNESS-RULES 第四节由「存量不挪」修订为「允许整批迁移」)。
- **依据**:HARNESS-RULES 第四节(2026-08-08 修订)+ MIGRATION-FLOW 7 步;断链回归 0 新增。