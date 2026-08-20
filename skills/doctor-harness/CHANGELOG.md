# doctor-harness · harness 演进 CHANGELOG

> harness 组织变更(迁移/规则修订)记录于此,可回溯「harness 为什么长这样」。追加式,只增不改。

## 2026-08-20 · P1 治理历史迁移(自身收尾;F040)

- **变更**:① SKILL.md 加头部索引行;② MIGRATION-FLOW 依据行日期注记压缩(先例细节留正文表);③ DESIGN.md 收敛为三节(定位/设计决策 V1–V12/已知限制)——起源节、演进记录表、家族身份状态迁本 CHANGELOG(见上条回填);④ 无 FORK-NOTES(无规则本体级分叉)。
- **原因**:governance-history-split P1(ADR-0024)——本 skill 作为零注记先例反向收尾:历史从 DESIGN 迁 CHANGELOG,DESIGN 收敛为纯设计决策。
- **影响**: SKILL.md#头部、DESIGN.md#全部、MIGRATION-FLOW.md#头部
- **出处**: [L1 契约](../../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024(F040/P1)

## 2026-08-20 · 第九节「治理历史布局」(ADR-0024 P0)

- **变更**:新增第九节——① 载体命名与粒度(skill CHANGELOG 仅项目侧/FORK-NOTES 双侧一致/DOGFOOD-LOG 仅全局侧/design 域 CHANGELOG/STATUS-LOG);② 历史层单侧存在规则 + sync-check 类规则引用(HISTORY_LAYER/GLOBAL_ONLY,与 EXCEPTIONS 白名单正交);③ 索引指针要求(SKILL.md 头部统一一行);④ 增量记录规则(五类触发 + 节标题改名时的锚点更新义务);⑤ CHANGELOG/FORK-NOTES 等非 LN 文件不受第七节命名正则约束;另「规则本体」判定词定义。doctor-harness SKILL.md 补治理历史职责条;项目 CLAUDE.md 铁律 8 语义改写。
- **原因**:治理历史分离 feature(design-Q governance-history-split,L0+L1 设计套 + grill-Q 压测 10 项修订)——三域治理历史「移层不删除」,双侧常态性形态分工(全局 = 分发洁净开箱,项目 = 车间完整)。
- **依据**:[ADR-0024](../../../harness/adr/0024-governance-history-split-dual-form.md) + [L1 契约](../../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + [grill-gov-history-split-w01](../../../harness/questionnaires/archive/governance-history-split/grill-gov-history-split-w01.md)(F039/P0)。
- **影响**: HARNESS-RULES.md#九、治理历史布局、SKILL.md#主流程、CLAUDE.md#铁律
- **出处**: ADR-0024 + 归档问卷(同上)

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
## 2026-08-08 · skill 创建(起源 + 设计实现 + 入家族;历史回填自 DESIGN.md)

- **变更**:① 设计套完成(VISION/HLD/LLD + ADR-0012/0013)——起源:压测 [grill-harness-file-mgmt-w01](../../../harness/questionnaires/archive/harness-file-mgmt/grill-harness-file-mgmt-w01.md) 发现 harness 文件管理规格「简单未考虑实际情况」(无层次化设计、feature/子项目无单独文件夹、边缘与实际工程场景未覆盖),用户裁决 harness 文件**严格**归 `harness/` 父级 + 子文件夹分层、不污染项目根,设计 skill 处理演进,立项 [OD-15](../../../docs/OPEN-DECISIONS.md);② P1 规则权威:HARNESS-RULES.md 起草 + 6 skill 引用句;③ P2 校验脚本:harness-check.py 实现 + 现状跑通/违规样本验证;④ P3 分层迁移:design/ 天然分层确认 + 归档 9 处层级链接修复(LLD P3 dogfood);⑤ P4 双副本 + 家族表述;⑥ **家族身份 done**:先 dogfood 后入家族(OD-15 重访触发②),F020 已同步「第 9 个」(CLAUDE.md 家族图 / CONTEXT skill 家族节 / 落盘速查表)——F019 分层迁移符合「dogfood 通过」定义(规则核对 + 脚本 0 违规 + 断链回归)。
- **原因**:压测产出 direction,用户裁决先设计后实现。
- **影响**: DESIGN.md#设计决策(V1–V12 决策表留在 DESIGN,本条为其时间线背景)
- **出处**: VISION/HLD/LLD 设计套 + grill-harness-file-mgmt-w01
