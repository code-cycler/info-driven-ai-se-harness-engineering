# retro: skill 家族使用体验复盘(v1)

> 复盘日期:2026-08-19。主题:9 个核心 skill 的真实使用体验——使用频次 / 走形式环节 / 轻任务耗时 → 家族级裁剪清单。
> 来源:grill-Q skill-family W01 Q10-A 裁决专门开设;retro 问卷 [retro-skill-family-w01](../../harness/questionnaires/archive/_misc/retro-skill-family-w01.md)(7 题,含主观自评)。

## 五源读取

1. 阶段设计文档:本次为体验复盘,非 feature 阶段——以 grill-Q skill-family W01 处理报告为输入
2. `git log`:本阶段未独立提交(随 skill 修订);修订证据见 skills/ 双侧
3. `TODO.md` 未完成项:skill 家族形态修订块(轻量模式 / 措辞对齐 / 分层迁移已销项)
4. 上一份 retro 的 Action Items:[designq-digital-levels_v1](designq-digital-levels_v1.md)(本次非其后续,无承接项)
5. 用户交流有价值内容:压测自定义「过度依赖 LLM,可人工轻验证」「模型判轻任务应主动问用户是否轻量执行」;retro 补充声明「提问维度需塞入用户积极查看处」

## 1. 进展顺利(What went well)

- **压测 → 修订闭环跑得顺**:grill-Q W01 10 题 → 用户授权「立即执行全部」→ 轻量模式规范 / action-Q 措辞对齐 / 分层样板 + 评估当轮落地,双侧同步 0 违规。
- **形态层裁决务实**:grill 合并提案被否(维持 OD-12 生态位),第 5 份隐性副本(提问方法论)纳入 OD-8 治理——克制合并冲动,先补治理。
- **Q3 自评「都不走形式」**:各环节价值被认可,说明流程设计本身立得住——痛点不在「环节多余」,在「轻任务错配重流程」。

## 2. 出问题与原因假设(What went wrong)

- **轻任务过度准备被实证(Q4:流程耗时 >> 任务本身)**:单行修复级任务走全流程,耗时远超任务价值。原因假设(已部分对治):**规格层无轻重分级**——前置调研五步闭环 / confirm-list / 全量文档地图对轻重任务一视同仁;W01 已加轻量模式 + action-Q 轻量下限,待 dogfood 验证是否切中。
- **delegate 未 pilot、grill 零使用(Q1/Q2/Q6)**:delegate 自入库从未真实启用(OD-23 已记),grill 因触发词易混淆 + 零留痕设计使用率趋零(OD-12 已降为作者自省)。原因:装置只进不出、缺退役出口(压测 W01 Q6 已识别,裁决不立事前门槛)。

## 3. 架构偏离

无设计文档与实现的形式偏离。一处**规格与体验的张力**:轻量模式是 2026-08-19 新加规格,尚未经真实轻任务验证——属「规范已定义 / 未实测」状态(审计装置四分法),待 dogfood。

## 4. 学到什么

- **轻任务痛点的正解是「触发分级」不是「砍环节」**:Q3(都不走形式)+ Q4(流程耗时 >> 任务)并存,证明该治的是「轻任务触发重流程」的错配,而非环节本身——轻量模式(AI 提议、人拍板)是对的方向。
- **skill 维度可见性缺口(补充声明)**:各 skill 的提问维度(design-Q 层骨架 / grill-Q D1–D8 / retro 四节 / action-Q 六要素)散落在各 SKILL.md,用户需逐个反看 skill 才能发现;应聚合到用户积极查看的入口(README / CONTEXT),提升家族可发现性。
- **裁剪共识(Q7 双勾)**:形态基本合理(微调已做)+ 有结构性冗余需裁剪——指向「保留 7 个高频 skill + delegate/grill 走使用率重访审查」,而非推翻形态。

## 5. Action Items

| 问题 | 行动 | 核验时机 |
|---|---|---|
| 轻任务过度准备(Q4) | 轻量模式规范已落地(W01 Q4);需真实轻任务 dogfood 验证是否切中 | 下次轻任务自然触发时 |
| delegate 未 pilot(Q6) | 走 [OD-23](../OPEN-DECISIONS.md) 既有重访(首批三次运行或 30 天窗口),不擅自退役 | OD-23 触发条件命中 |
| grill 零使用(Q6) | 走 [OD-12](../OPEN-DECISIONS.md) 收窄后重访(触发词混淆实例 / 作者主动重估),不擅自删 | OD-12 触发条件命中 |

> **收尾注记(2026-08-19 同日)**:上表 grill 行已被当日的正式退役 supersede——用户显式裁决移除 grill(派生自 mattpocock grill-with-docs、适用场景少),grill 已归 `waste/skills/grill/`,生态位由 grill-with-docs 通用模式承接(见 [OD-12](../OPEN-DECISIONS.md));家族由 9 收为 8。本 retro 主体(复盘时点「9 个核心 skill」「grill 零使用」等表述)按 retro「只记录原貌」原则不改,仅以此注记标记演进。delegate 行走 OD-23 重访,不变。
| 维度可见性缺口(补充声明) | 聚合各 skill 提问维度到 CONTEXT「skill 家族」节(用户积极查看处) | 本轮 retro 处理时即做 |
