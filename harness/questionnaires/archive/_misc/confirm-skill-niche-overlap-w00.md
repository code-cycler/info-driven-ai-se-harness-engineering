---
mode: feature
wave: 0
stage: confirm
created: 2026-07-30
status: archived
---
# 问卷 confirm W00 · 细节确认清单(AI 汇报理解,人核对)

> **行动**:分析 methodology_v3.md 所列 7 个 skill 是否存在生态位重叠(重点 grill / grill-with-docs / grill-Q),并把本次会话作为 action-questionnaire 的 dogfood。
>
> **本波是细节确认清单**(独立 wave 0):把 AI 对本次行动细节的理解逐条列出,人只做「对/不对」核对。
>
> **作答规则**:
>
> - 勾 `[x]` = **理解正确**(按该理解执行)
> - 留空 `[ ]` = **理解有误或要改** → 该要点转正式题深究(或小波直接问)
> - 本波**不用 🤔**(对/不对二选一,无中间态);「大体对但要改一两处」→ 留空,转正式题时在深究题里给正确值
>
> 来源标注于〔〕:**〔推断〕= AI 填的,重点核对**;〔用户原话 / 代码 / 文档〕= 有据。

## 细节确认清单

### 目标

- [X]  **1 分析任务**:判定 methodology_v3.md 所列 7 个 skill(design-Q / grill-Q / retro-Q / long-running / delegate / grill / grill-with-docs)是否存在生态位重叠,重点是 grill / grill-with-docs / grill-Q 三件套。〔用户原话〕
- [X]  **2 dogfood 双重身份**:本次会话同时是 action-questionnaire 自身的 dogfood——确认流程本身是自验对象,流程中发现的格式/流程缺口要记录。〔用户原话〕

### 输入

- [X]  **3 主分析对象** = `docs/methodology/methodology_v3.md`(用户 @ 引用,已读全文)。〔用户原话〕
- [X]  **4 核实依据** = 仓库内 `skills/*/SKILL.md` 原文——分析中引用任一 skill 的行为/定位时,不凭 v3 或 description 转述,以 SKILL.md 原文为准(8 份已全部读过)。〔推断,已核实〕
- [X]  **5 「7 个 skill」范围** = v3 §8.3 家族成员;**但 action-questionnaire(仓库第 8 个 skill,今天刚经 grill-Q 压测设计、未入 v3)也纳入分析**——它与 design-Q preview、grill 单点确认的边界恰是重叠问题的最新实例,且本次 dogfood 结论直接相关。〔推断——重点核对〕

### 输出

- [X]  **6 分析报告** = 对话内输出:逐「疑似重叠对」给出判定(真重叠 / 名义重叠实分工 / 有分工但文档表述不一致)+ v3 与 SKILL.md 的证据出处。〔推断〕
- [X]  **7 不改文档**:本行动**不直接修改** methodology_v3.md 或任何 SKILL.md;若分析结论要落成修订,另起行动(多文件结构性修订可能升级为 feature 级 → 转 grill-Q / design-Q,本 skill 只留确认记录)。〔推断——重点核对〕
- [X]  **8 dogfood 记录方式**:流程缺口即时记入处理报告(对话内);行动完成后摘要追加进本归档问卷尾部;是否回修 action-questionnaire 规格文件(SKILL.md / 引擎副本 / DESIGN.md)由用户逐条授权。〔推断〕

### 约束

- [X]  **9 AI 不替人决策**:重叠判定只给证据与倾向,是否接受结论、改不改文档由人拍板。〔skill 铁律〕
- [X]  **10 「生态位重叠」操作定义**:两个 skill 在同一触发场景下,用户无法从 description / 方法论文档判定该用哪个,或两者职责声明实质相同 → 算重叠;仅名义相似(如都含「压测」「确认」)但触发场景 / 交互形态 / 落盘三者可区分 → 不算真重叠。〔推断——重点核对〕

### 边界

- [X]  **11 三件套已核实的分工事实**(分析出发点):grill = 通用问题、不绑代码库、纯对话默认不写任何文件、绝不自动写 CONTEXT/ADR/OD;grill-with-docs = 绑代码库领域模型、边问边自动写 CONTEXT/ADR/OD;grill-Q = 批量问卷压测**已有工件**、代码库绑定为默认(纯逻辑模式降级)、只产出发现绝不替改工件(但可沉淀项仍落 CONTEXT/ADR/OD)。〔已核实:三份 SKILL.md 原文〕
- [X]  **12 非目标**:不重新设计家族结构、不提议合并/删除任何 skill、不动引擎漂移已决项(OD-8 保留现状);「改 skill 家族结构」是 feature 级行动,发现即转出。〔推断〕

### 依赖

- [X]  **13 背景工件**:归档问卷 `grill-preaction-confirm-skill-w01.md`(action-Q 的设计压测,2026-07-30)——其中 Q1 已裁决「为什么独立新 skill 而不扩展现有 skill」、Q2 已裁决「与 §5.2 保留一问一答场景是否矛盾」,是重叠问题的**既有裁决**,分析须对照而非重新发明。〔已核实存在〕
- [X]  **14 方法论 canonical 参照**:v3 §5.2(保留一问一答的场景)、§5.3(两族 Grill 分工表)、§8.3(skill 使用时机表)是判定重叠的方法论依据。〔文档〕

## 补充声明

<任何想补充的话:范围调整、判定标准修正、输出形式偏好……没有就留空。agent 处理时必读>我心中的答案是grill、grill with docs已经可以被questionnaire家族替代

---

## 处理报告摘要(归档前追加,2026-07-31)

- confirm-list 统计:确认正确 14 / 留空纠正 0 / 转正式题或小波 0;无异常;W00 无 🤔。
- 补充声明:用户先验结论(「grill / grill-with-docs 已可被问卷家族替代」)→ 按「待验证假设」纳入分析,不预设为结论(规格外第四类,记 dogfood 缺口 D-1)。
- 落盘:无 ADR/OD/CONTEXT 升格项;常规留痕 = 本问卷;行动项 F1–F6 → TODO.md。
- 覆盖度:六要素 6/6,动态盲点 0,确认循环一轮终结。

## 执行结果摘要(行动完成后追加,2026-07-31)

- 行动:7(+1) skill 生态位重叠分析(对话内报告,2026-07-30)。
- 结论:按 W00 #10 操作定义,**无真重叠**——grill 三件套是「连续体 + 交互轴」分工:grill(通用问题/零工件可启动/纯对话零落盘)、grill-with-docs(绑代码库领域模型/边问边写 CONTEXT·ADR·OD)、grill-Q(批量问卷压测已有工件/只产出发现不替改)。
- 用户先验检验:能力层面大体成立(问卷家族已吸收「少题 / 无代码库 / 落盘」场景),残差三条在收窄——深依赖链、即时反馈偏好、零留痕轻量;§5.2 保留论据与家族演进存在张力 → F6 战略决策点留人拍板。
- 发现:F1 grill / grill-with-docs 路由表无 grill-Q;F2 grill-Q description「同用途」与自身分工表冲突;F3 v3 §5.3 落盘行对 grill 不成立(D7 型矛盾);F4「计划评审」§5.2/§8.3 两处归属;F5 action-Q 小波阈值观察项。
- dogfood(action-Q 首案例):D-1 补充声明第四类规格缺口(用户授权回修);D-2 confirm-list 一轮终结顺畅;D-3 两次串行等待轻摩擦。**本案例即 action-Q DESIGN.md「dogfood 范围决策」的 canonical 同步(7→8)门槛案例**。
- 后续:F1–F4 入 TODO.md;D-1 回修 action-Q PROCESSING-RULES(小波确认);F6 用户拍板(2026-07-31)转 grill-Q 压测。
- 归档闸门:用户选择后续行动(③④)且未对处理报告/分析提异议,视同无异议。

---

## 提问波(2026-07-31,2 题 ≤ 4 未生成问卷文件;问答逐字转写)

**Q1(D-1 传播范围)**:补充声明第四类「用户先验结论 → 待验证假设(分析中检验,不预设为结论,处理报告标注)」是否传播到其他三份引擎副本(design-Q canonical / grill-Q / retro-Q)?
- 选项:A. 只改 action-Q(★推荐:repo + 用户级双副本同步,声明有意分叉;canonical 跟进与否由 design-Q 上下文另决)/ B. 四份同改,回写 canonical / C. 🤔 降风险
- **用户答:A. 只改 action-Q**
- 处理:repo + 用户级双副本已同步改(PROCESSING-RULES 解析规则 3 + FORMAT 规则 12 + 头部分叉声明 #4);DESIGN.md 记有意分叉 #6 与 dogfood 案例;canonical 未动。

**Q2(grill-Q 启动)**:「重估 §5.2 / 合并 grill 家族」提案(F6)的 grill-Q 压测何时启动?
- 选项:A. 现在本会话启动(★推荐:上下文热,8 份 SKILL.md 已核实)/ B. 另开新会话启动 / C. 🤔 降风险(挂 OD)
- **用户答:A. 现在本会话启动**
- 处理:工件 = 本次分析(对话内)+ 本归档问卷 + v3 §5.2/§5.3 + grill 三件套 SKILL.md;绿地代码库绑定模式(D7 对照 v3/SKILL.md/CONTEXT/ADR/OD 现状);F1–F4 文档修订项已入 TODO.md,独立于压测。
