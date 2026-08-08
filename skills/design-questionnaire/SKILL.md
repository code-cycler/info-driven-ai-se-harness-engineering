---
name: design-questionnaire
description: 项目启动初始化与重大功能设计的批量问卷式 grill。生成多波次 Markdown 问卷(选项勾选 + 逃生舱 + 自定义回答),用户离线作答后按类型落盘到 VISION / DESIGN(HLD/LLD) / ADR / OPEN-DECISIONS / CONTEXT,已用问卷归档。阶段内循环直到再无可盘问的信息,跨阶段必须过用户闸门。与一问一答的 grill / grill-with-docs 并存分工(它们管实现期单点深钻)。触发:新项目初始化、新功能设计、"帮我做设计"、"出问卷"、"初始化项目设计"、构想/全局设计/分阶段设计阶段。Use when starting a project or feature and the VISION→HLD→LLD design should be completed via batched questionnaires instead of one-by-one Q&A.
---

<what-to-do>

把「一问一答的 grill」改为「多波次问卷的 grill」:每一波生成一份 Markdown 问卷文件,用户离线作答(编辑文件或对话速答),作答后逐题解析落盘,阶段内循环直到再无可盘问的信息。

## 铁律(不可违反)

1. **AI 不替人决策** — 问卷提供 ★推荐 和利弊分析,选择永远是人的。agent 的角色是出题、验证、落盘。
2. **逃生舱绝不重问** — 用户勾了 🤔(或对话速答中表达「不确定/你决定」),走降风险协议(见 [PROCESSING-RULES.md](./PROCESSING-RULES.md)),不得换个说法再逼问同一题。
3. **即时沉淀,不批处理** — 每波问卷处理完,立即写入对应文档(阶段文档 / ADR / OPEN-DECISIONS / CONTEXT),不攒到阶段末。
4. **原始信息不丢失** — 问卷文件是唯一事实源;对话速答必须逐字转写进问卷文件;已处理问卷归档(只移不删)。
5. **先验证再出题** — subagent 探索到的事实,凡要引用进问卷的,主 agent 必须核实原文,不得凭转述出题。
6. **阶段闸门必须过人** — 阶段内终止由 agent 判断并出示覆盖清单;跨阶段必须用户显式确认。

## 主流程

### 0. 触发与定模

- 判断 mode:
  - `init` — 新项目 / 从零开始:完整 vision → hld → lld 三阶段。
  - `feature` — 已有项目的新功能设计:同样三阶段,骨架按 [STAGE-SKELETONS.md](./STAGE-SKELETONS.md) 的 feature 栏裁剪;探索现有代码库是必须前置步骤。
- 若用户没有给初始描述,先要「一句话念头 + 动机」。这是用户的作业,agent 不代写构想。
- **阶段坍缩判断**:按「经验 × 规模」给坍缩建议,AskUserQuestion 询问用户确认:
  - 用户自认有经验 → 完整 vision → hld → lld 三阶段;
  - 用户没经验 → 坍缩为 hld(详细设计不预先写,实现中边做边调,沉淀的详细决策即时落盘);
  - 小项目(skill、脚本、小工具) → 坍缩为 lld(hld 不单独写;选型/ADR 识别若有实质内容,并入 lld 文档或单独 ADR)。
  坍缩方向骨架见 [STAGE-SKELETONS.md](./STAGE-SKELETONS.md) 坍缩节。

### 1. 探索与验证

- 主 agent 快读文档地图:CLAUDE.md(已自动加载)、docs/ 索引、已有 VISION / CONTEXT / ADR / OPEN-DECISIONS。
- 读 `<项目根>/TODO.md`(若存在):未完成行动项纳入出题上下文。
- 按需派 1–3 个 Explore subagent(自适应分工):现有文档、代码库、外部调研。绿地项目无代码可探则跳过代码 subagent。
- subagent 只返回结构化事实清单(事实 + 出处),不写分析散文。
- 主 agent 对将引用进问卷的关键事实(已有决策、术语定义、接口契约、与代码的矛盾点)逐条核实原文;不做全量复核。
- **环境现实验证**:凡问卷将涉及**外部依赖**(图形/GUI/网络/数据库等库、工具链、本机资源路径、版本)的选型/路径/版本,出题前必实测——不只 `--version`/`brew list`(库存在≠能用),须**实测编译链接**:写最小程序(如 `gcc + 库` 一行),跑通 `init`/链接/基本调用。证据(命令、输出、最小程序)写入出题依据;无法实测的假设在题干显式标注「未验证假设」。不把计划建立在「以为装了就能用」的假设上(项目B dogfood 实证:某图形库实为兼容层 / 某配套字体库未装 / 构建脚本不含库链接,三假设全错,迟至实现期才暴露)。

- **实测与调研前置(标准流程,2026-08-03 起)**:提出问卷前,完成「调研现状 → 不假设 → 多实测 → 多获取信息 → 及时保存」闭环——
  1. **调研现状**:读 CLAUDE.md / CONTEXT / ADR / OPEN-DECISIONS / TODO / 相关代码区,不凭记忆出题;
  2. **不假设**:凡要引用进问卷的事实,不凭转述/记忆,必须核实原文或实测;
  3. **多实测**:不只查存在(`--version`/`brew list`),须实际跑通(编译链接 / 运行 / 调用级);证据(命令 + 输出 + 最小程序)记入出题依据;
  4. **多获取信息**:实测中发现的额外信息(版本差异、隐藏依赖、行为细节)一并记录;
  5. **及时保存信息**:证据与发现**立即**写入问卷出题依据 / 处理文件,不攒到出题后;无法实测的显式标「未验证假设」并放问卷最前(衔接问题级排序)。

- **未验证假设生命周期管理(2026-08-07 起)**:验证纪律(铁律5 / 环境现实现证 / 实测前置)锚定「出题时」,但构想 / 需求随问卷演进,早期未实测信息可能在下一阶段成为规划支撑。补三件套:
  ① **台账维护**:每波处理时,把「出题依据标注的未验证假设 + 用户回答引出的新信息 + 上波遗留未验证项」收进台账,跨波持续追踪,不随波次丢弃。台账记录:假设 + 出处(问卷+题号)+ 涉及阶段 + 状态(pending / verified / stale);落点 = 每波处理报告新增「未验证假设台账」节(随归档问卷尾部留存,单文件可回溯)。只跟踪「将影响后续规划」的信息,不追求穷举(防形式主义)。
  ② **复用前重验**:某信息即将成为**下一阶段文档的规划基础**时,起草前先重验(实测 / 核实原文);无法验证 → 显式标注「未验证 + 将作为 X 的规划基础」,提交用户确认或走降风险协议,不得静默进入 VISION / HLD / LLD 文档。

### 2. 生成问卷

- **preview(每阶段强制,独立 wave 0)**:每阶段先生成一份独立的 **W00 preview 问卷**(`<stage>-w00.md`),**不与 W01 同出**。preview = 决策默认值清单,一要点一行 = 本阶段将盘问的决策点 + AI 默认倾向 + 来源;每条**预勾与否由 opt-in 开关决定**(2026-08-03 起,默认关:用户启动本 skill 时明确说「预勾选」才预勾 `[x]`,勾 = 采纳默认按默认落盘;未启用时全部 `[ ]` 人逐条作答),**取消勾选(留空)= 不采纳**(该要点转入 W01 单独拷问);**单向门要点永不预勾**(发布/删除/花钱/脱敏,强制显式勾选)。W00 **不用 🤔**(yes/no 二选一,无中间态;真定不了即取消勾选转 W01);底部「补充声明」栏保留。W01 正式题 = W00 留空(不采纳)要点的深究 + 不适合 yes/no 的开放型骨架必答项(多选/方向题)。格式见 [QUESTIONNAIRE-FORMAT.md](./QUESTIONNAIRE-FORMAT.md)「文件结构(§ W00 preview 问卷模板)」;解析见 [PROCESSING-RULES.md](./PROCESSING-RULES.md)。后续波次(W02+)由缺口驱动,不再出 preview。
- 问题来源 = **阶段骨架**([STAGE-SKELETONS.md](./STAGE-SKELETONS.md) 当前阶段的未覆盖必问项,优先) + **动态盲点**(探索发现的矛盾/冲突/未定义边界、上轮回答引出的新问题)。
- 格式严格按 [QUESTIONNAIRE-FORMAT.md](./QUESTIONNAIRE-FORMAT.md)。
- 写到 `harness/questionnaires/<stage>-w<NN>.md`(feature 模式:`feature-<slug>-<stage>-w<NN>.md`),status: pending。目录懒创建。**harness 文件分层见 HARNESS-RULES.md**(doctor-harness 规范权威,不内联复制)。
- 题量:每波 10–15 题;超出拆子波(`<stage>-w<NN>a.md`、`<stage>-w<NN>b.md`)。
- **小波阈值**:若本波问题数 ≤ 2,不生成问卷文件,改用 AskUserQuestion 直接提问(仍给 ★推荐与 🤔 逃生舱);问题、答案、处理结果逐字记入处理报告,摘要追加到最近一份归档问卷尾部。

### 3. 用户作答

- 默认:用户直接编辑问卷文件(opt-in 开关开启时:预勾项取消 / 未预勾项勾选;开关关闭时全部逐条勾选;填 ✍️ 自定义行),保存后通知 agent。
- 也接受:对话速答(如「Q1: A;Q2: 自定义……」),agent **逐字**转写进问卷文件,然后以文件为准解析。
- 用户宣布「答完了」之前不解析。

### 4. 处理与落盘

- 按 [PROCESSING-RULES.md](./PROCESSING-RULES.md) 逐题解析(含异常:单选多勾、必答未答、条件题误答)。
- 逐题落盘:阶段文档(VISION/HLD/LLD) → `harness/design/`;ADR → `harness/adr/NNNN-<slug>.md`;**CONTEXT.md / OPEN-DECISIONS.md / TODO.md 为项目固有文件,路径不动**(各项目已定型),**本波处理完即刻写**。行动项(处理报告/复盘产出)写入 `<项目根>/TODO.md`(格式:问题 → 行动 → 核验时机)。
- 生成新问卷、阶段闸门、DoD 核验、新会话恢复时,先读 TODO.md。
- 🤔 逃生舱 → 降风险协议,绝不重问。
- 输出**处理报告**(对话内,格式见 PROCESSING-RULES.md):每题去向、新增/更新的文件、异常处理、逃生舱处置、下一波候选、本阶段覆盖度。
- 每阶段 W00 的处理报告必须含 preview 统计(勾选采纳数、取消勾选不采纳数、转 W01 正式题数)+ 取消默认率(opt-in 开关开启时,见 PROCESSING-RULES.md「预勾设防」);阶段覆盖清单必须检查 W00 存在性——无 W00 的阶段视为流程缺口。
- 用户无异议 → 问卷 status: processed → archived,移入 `harness/questionnaires/archive/`。

### 5. 循环与终止

- 判断当前阶段是否**再无可盘问的信息**,判据:阶段骨架必答项全覆盖 + 动态盲点清零 + 逃生舱项已全部进 OPEN-DECISIONS。
  - 还有 → wave+1,回第 2 步。
  - 没了 → 出示覆盖清单,然后过**阶段闸门**:用 AskUserQuestion 单独确认一次「本阶段还有要补充的吗?」。
    - 有补充 → 生成补充波。
    - 无 → 进入下一阶段;lld 完成则进入收尾。
  - **闸门汇报(2026-08-07 起)**:出示覆盖清单时,一并出示「下一阶段将依赖的未验证信息」清单(来源:台账,见 §1「未验证假设生命周期管理」)——闸门确认时用户可见哪些未验证信息将进入下阶段规划,可当场要求重验或调整。
- **delegate 衔接(若项目启用决策下放)**:init 起草可在工程一开始;**激活统一定在 vision 阶段闸门**——闸门确认时人一并审查 delegation.md 定稿,此前按「全部问人」运行。机制与白名单治理见 delegate skill;preview 与问卷流程归本 skill,delegate 只引用。
- 收尾:输出设计完成清单(VISION / HLD / LLD / ADR / OPEN-DECISIONS 的文件链接汇总),提醒用户按方法论进入实现阶段(TDD、小步提交;实现期二义性改用 grill-with-docs 单点深钻)。
- **可选:dogfood 验证** — 若设计产物是可自用的工具 / 流程 / 模板(skill、方法论、问卷本身),收尾前向用户提供可选项:用产物在真实小案例上完整走一遍闭环。dogfood 发现的格式 / 流程缺口即时回修规格(本 skill 的 dogfood 曾修正「补充声明区」「小波阈值」「preview 拆独立 W00」三个缺口)。用户可跳过;跳过与结果都记入 DESIGN.md。
- **可选:提议压测(grill-questionnaire 衔接)** — 输出设计清单后,用 AskUserQuestion 提议「要不要用 grill-questionnaire 压测刚产出的设计?」,接上 write→review 闭环。用户可拒,拒绝即跳过。不按项目规模收窄(小项目也提议,由用户自判压测价值)——2026-07-24 grill-Q dogfood Q1=A / Q8=B。
- **可选:提议 long-running-agent 衔接(grill-Q 之后)** — grill-Q 提议被**拒**时,紧接提议「是否进入长期实现(long-running-agent)?」;grill-Q 被**接受**时,压测完成后再提议。用户可拒,拒绝即跳过,后续用户随时可手动调用 long-running-agent。衔接时 long-running-agent 从本 skill 产出的 VISION/HLD/LLD 重建 feature_list,不依赖会话上下文。设计→实现跨阶段衔接,由人决定是否进入——2026-07-28 某 long-running 衔接压测问卷 Q11 裁决。

## 与 grill / grill-with-docs 的分工

| | design-questionnaire | grill / grill-with-docs |
|---|---|---|
| 场景 | 启动初始化、功能设计(批量决策) | 实现期单点二义性、计划评审(单点深钻) |
| 交互 | 多波次问卷,用户离线作答 | 一问一答,逐轮等待 |
| 落盘 | VISION / HLD / LLD / ADR / OD / CONTEXT | CONTEXT / ADR / OD |
| 终止 | 再无可盘问的信息(覆盖清单 + 闸门) | 共享理解达成 |

问卷处理中若发现某单点是不确定性深水区(答案引出大量纠缠子问题),在处理报告里建议用户对该点单独跑 grill-with-docs,然后回来继续问卷流程。

</what-to-do>

<supporting-info>

- 问卷格式规范(引擎,可被 retro-questionnaire 等复用):[QUESTIONNAIRE-FORMAT.md](./QUESTIONNAIRE-FORMAT.md)
- 解析与落盘规则(引擎,可被 retro-questionnaire 等复用):[PROCESSING-RULES.md](./PROCESSING-RULES.md)
- 三阶段固定骨架(本 skill 的模板):[STAGE-SKELETONS.md](./STAGE-SKELETONS.md)
- 本 skill 的设计决策记录:[DESIGN.md](./DESIGN.md)

</supporting-info>
