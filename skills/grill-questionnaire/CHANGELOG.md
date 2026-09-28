# grill-questionnaire · CHANGELOG

> 本 skill 治理历史(创建起源/引擎同步与漂移/分叉裁决时间线)。追加式,只增不改;规则现值见 SKILL.md 与引擎文件,设计决策见 [DESIGN.md](./DESIGN.md),有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。

## 2026-09-27 · skill-audit 修复批(副本侧,confirm-skill-audit-fix 裁决 Q1/Q2/Q5③)

- **变更**:① 归档规则同步为 D34「处理报告全文制」(与 canonical 一致);② PROCESSING-RULES 新增「修订前置检查(OD-8 执行步骤)」节;③ FORMAT 命名行 LN 枚举清除(L4/L12 同文件矛盾修复:改 `grill-<slug>-w<NN>`);④ SKILL 归档表述「摘要→全文」;⑤ 分工表 design-Q 列旧三件命名 LN 化 ×2(含骨架行);⑥ FORK-NOTES 登记 ×3(全文制收口/命名本地化/结构分叉声明补全)。
- **原因**:2026-09-27 skill 体系全量审查([报告 01](../../harness/design/skill-audit/01-report-questionnaire-skills.md) 高-1/高-2/中-9 涉本 skill/低-1/低-2);D38 LN 制修订单方落在 design-Q 未同步本副本。
- **影响**:PROCESSING-RULES/SKILL/FORMAT/FORK-NOTES(已双侧同步);明细 = [归档问卷处理报告](../../harness/questionnaires/archive/)。
- **出处**:问卷 confirm-skill-audit-fix-w00/w01 + [修复计划 05](../../harness/design/skill-audit/05-fix-plan.md) 批次 B。

## 2026-08-20 · P1 治理历史迁移(governance-history-split F040)

- **变更**:① SKILL.md 11 处日期注记剥离 + 头部索引行;② 引擎 FORMAT/PROCESSING 15 处日期剥离 + 头部拆分(副本标记留头部剥日期,有意分叉声明迁 FORK-NOTES.md 双侧);③ GRILL-SKELETON 2 处剥离;④ DESIGN.md 收敛三节——引擎复制声明内三个事件、引擎同步记录 ×3、dogfood 教训叙述、引擎有意分叉声明迁本 CHANGELOG / FORK-NOTES;⑤ 新建 FORK-NOTES.md(双侧一致)。
- **原因**:ADR-0024 治理历史分离 P1。
- **影响**: SKILL.md、DESIGN.md、QUESTIONNAIRE-FORMAT.md、PROCESSING-RULES.md、GRILL-SKELETON.md、FORK-NOTES.md(新)
- **出处**: [L1 契约](../../harness/design/governance-history-split/L1-contract-gov-history-split.md) + ADR-0024

## 2026-08-19 · 引擎有意分叉(❌ 跑偏标注族)

- **变更**:❌ 跑偏标注族成为本副本专属有意分叉——FORMAT 规则 15(每题 ❌ 行)+ 模板/填写规则/规则 4 自检/规则 13 排序 + PROCESSING ❌ 解析行与「≥2 停波回炉」+ 处理报告「质量信号」节;SKILL 层同批机制(族间自检/入口校准闸门/阻塞性分流/质量信号);grill-with-docs 侧反向相变条款。声明为设计(非遗漏)。现值已迁 FORK-NOTES.md。
- **原因**:grill-with-docs「grill 家族边界与跑偏治理」深钻(四分支裁决:认知状态三态接线/入口+中途双检测/校准闸门+题级标注双件/优化回路 OD-26 provisional),用户授权「包一全授权」执行;canonical 层走 grill-boundary-canonical-w01 复压。
- **关联**: ADR-0023(升格收口)、CONTEXT「Grill 家族 · 认知状态三态」、OD-26
- **出处**: grill 边界深钻会话 + grill-boundary-canonical-w01(archive/_misc/)

## 2026-08-18 · 引擎规则 4 修正(✍️ 位置)

- **变更**:FORMAT 规则 4——「✍️ 自定义」改为「紧跟所有选项之后、固定为题目最后一位」,消除与规则 13 排序矛盾(根源 = 「✍️ 行结构性遗漏」,first-principles W01 曾 10 题全漏);本副本与 retro-Q 模板示例同步;四副本 × 双侧同批,无新有意分叉。
- **出处**: grill-Q first-principles W01 补充声明

## 2026-08-08 · dogfood 教训:✍️ 自定义行反复遗漏(已升格)

- **变更**:缺口 = FORMAT 规则 4 散文规则无出题后强制自检,两次遗漏(design-Q vision W01 + grill-Q doctor-harness W01,均 10 题全漏),用户两次指出。回修 = 四副本 FORMAT 规则 4 加「出题后自检」(grep 🤔 数 == ✍️ 数)+ 本 skill SKILL 第 2 步加「出题自检(强制)」可执行命令。**此教训与 2026-08-18 修正同主题(✍️ 遗漏)累计 ≥2 次,按 ADR-0023 已升格为常驻自检规则。**
- **出处**: grill-doctor-harness 压测轮

## 2026-08-06/07 · skill-spec-revamp 同步与撤销

- **变更**:落盘路径配置化(方案 R)同步到本 skill(仅落盘映射节 diff 0,有意分叉区保留);**2026-08-07 撤销**——方案 R 放弃(ADR-0011),路径回归硬编码 `harness/`。
- **出处**: ADR-0011 + grill-skill-spec-revamp-w01

## 2026-08-03 · 预勾开关化 + 实测前置同步

- **变更**:预勾选 opt-in 开关默认关 + 选项排序统一为默认行为 + 单向门永不预勾(OD-14 修订);「实测与调研前置」标准流程入 SKILL。四副本同步(OD-8 重访触发①命中)。
- **出处**: OD-14 + confirm-pregou-switch-w00 / confirm-testing-preflight-w00(archive/_misc/)

## 2026-07-24/25/27 · 创建与引擎漂移三事件

- **变更**:① 2026-07-24 创建:grill-with-docs 单点深钻定稿(G1–G8 全接受推荐)+ dogfood 自压测(D22/D23)+ 引擎修改三方同步(逃生舱进 OD,D23);② 2026-07-25 引擎漂移(design-Q dogfood 发起 preview 预答层,本副本暂未同步——**声明为设计**);③ 2026-07-27 引擎漂移(design-Q canonical 演进 preview 拆独立 W00 波,本 skill 不使用 preview——压测场景工件已存在无阶段默认值可预答,**声明为设计**,待 preview 机制验证后评估)。
- **出处**: grill-with-docs 设计会话 + grill-own-design-w01(docs/questionnaires/archive/)+ 生态位区分分析(confirm-grill-niche-distinguish-w00)

## 2026-07-31 · 原初设计原则补记

- **变更**:作者陈述补记落盘——设计前提 = 对抗幻觉;核心原则 = 80/20 判断成本原则(批量 20% 时间处理 80% 可预知问题,深水区转 grill-with-docs 深钻);认定 G1 出生 scoping 与 80/20 分层长期未在文档承认的历史。现值已入 DESIGN.md「动机与范围」。
- **出处**: confirm-grill-niche-distinguish-w00(archive/_misc/)
