---
mode: init
wave: 1
stage: hld
created: 2026-07-23
status: archived
---
# 问卷 hld W1 · retro-questionnaire 全局设计

> 填写规则:
>
> 1. 每题勾选 `[x]`;默认单选,标「(多选)」可勾多个,选项数不限
> 2. ★ = 推荐选项,附推荐理由
> 3. 每题末尾 🤔 是逃生舱:勾了 = 我定不了 → agent 走降风险协议,绝不重问
> 4. 选项都不合适 → 在 ✍️ 自定义 后自由书写
> 5. 标「条件:Qn 选 X 才答」的是内联浅分支,条件不满足直接跳过

项目:retro-questionnaire(复盘问卷 skill)
前置:vision 已定稿(2026-07-23 闸门通过),见 docs/VISION.md
出题来源:HLD 骨架 H1–H5 + 动态盲点(引擎复用方式、改动同步);H4 部署位置已定(~/.claude/skills/retro-questionnaire/),不单独出题。

## Q1. 引擎复用方式:retro-questionnaire 怎么复用 design-questionnaire 的引擎文件?   [落盘: HLD#选型]

出题依据:VISION 决策「复用同一套逻辑」;引擎 = QUESTIONNAIRE-FORMAT.md + PROCESSING-RULES.md 两文件。这是本阶段唯一的高 stakes 决策。

- [ ]  A. 相对路径引用:retro 的 SKILL.md 写明「读取 ../design-questionnaire/ 的两个引擎文件」  ★推荐 —— 单一事实源,引擎改一处两个 skill 同时生效;代价:design-questionnaire 被移动/删除则引用断(用 Q4 的同步规则兜底)
- [X]  B. 复制两份 —— 各自独立,但必然漂移(DESIGN.md 已知风险表已列)
- [ ]  C. 抽取共享:引擎移到 ~/.claude/questionnaire-engine/,两个 skill 都引用 —— 最干净,但要回改已交付的 design-questionnaire,且多一个无 skill 外壳的游离目录
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________在两个skill中都补充说明，改动其中一个需要考量是否需要同步改动另外一个；若已经存在漂移，需要声明是否为设计

## Q2. retro 骨架模板按什么结构组织复盘问题?   [落盘: HLD#架构]

出题依据:方法论§阶段6 复盘内容(What went well / What went wrong / 架构偏离 / 学到什么)+ VISION 决策(Action Items 节、反思题选项 = 假设清单)。

- [X]  A. 按方法论四节 + Action Items:进展顺利 / 出问题与原因假设 / 架构偏离 / 学到什么,外加固定 Action Items 节  ★推荐 —— 直接来自方法论,与 VISION 已决项严丝合缝
- [ ]  B. 按开发流程阶段:计划 / 执行 / 验证 / 收尾逐段复盘 —— 更贴时间线,但与方法论四节不兼容,且 Action Items 无处安放
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q3. 生成 retro 问卷时,出题依据从哪来?   [落盘: HLD#接口契约]

- [X]  A. 阶段设计文档 + git log(本阶段提交)+ TODO.md 未完成项 + 上一份 retro 的 Action Items  ★推荐 —— 四源交叉,「Action Items 回顾」节(VISION 已决)有了数据来源;都是低成本读取
- [ ]  B. 仅靠用户叙述 —— 最轻,但用户记忆正是复盘要对抗的东西,退化为形式主义
- [ ]  C. 全量文档 + 全量 diff 重读 —— 最全,但上下文膨胀,违背精准投喂原则
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________与用户交流的有价值的内容也都可触发

## Q4. 引擎文件改动时,怎么保证两个 skill 不漂移?   [落盘: HLD#部署运维]

- [X]  A. 同步规则:任何引擎修改,在两个 skill 的 DESIGN.md 各记一笔,并检查引用方是否受影响  ★推荐 —— 与「即时沉淀」一致,成本一次一行字
- [ ]  B. 只靠相对路径天然同步(配合 Q1 选 A 即可,不需要额外规则) —— 文件内容确实同步,但「这次改动是否破坏引用方的骨架模板」无人检查
- [ ]  C. 引擎文件加版本号,引用方声明依赖版本 —— 严格,但两个个人 skill 用版本依赖是过度工程
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

---

## 补充声明

<任何想补充的话:新需求、格式反馈、范围调整、临时想到的风险……没有就留空。agent 处理时必读>在design-questionnaire中优化design阶段：若正在处理小项目可以不用分hld和lld时，询问用户是否坍缩为单一的design

---

## 处理报告摘要(2026-07-23)

- 落盘:Q1–Q4 → [../design/hld_v1.md](../../design/hld_v1.md)(架构/选型/接口契约/部署运维)
- 新增文件:docs/design/hld_v1.md
- 异常:无(无单选多勾、必答题全答)
- 逃生舱:无
- 自定义处理:
  - Q1 ✍️「两 skill 双向声明 + 漂移声明是否为设计」→ HLD#选型 防漂移声明机制;同步声明已登记到 design-questionnaire/DESIGN.md「引擎复制声明」节
  - Q3 ✍️「与用户交流的有价值的内容也都可触发」→ HLD#接口契约 数据源第 5 条
- 补充声明处理(1 条规格反馈,已即时修规格):
  1. 小项目可询问用户是否坍缩 HLD/LLD 为单一 design 阶段 → 已改 design-questionnaire/SKILL.md 第 0 步与 STAGE-SKELETONS.md(坍缩骨架),记为 D17
- ADR 识别(H5):Q1 判双向门,不达门槛,无 ADR
- 覆盖度:HLD 骨架 H1–H5 全覆盖;动态盲点清零 → 本阶段再无可盘问的信息,进入阶段闸门
