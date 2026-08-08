# design-questionnaire · 设计文档

> 本 skill 的 VISION + HLD 合并设计文档,记录 2026-07-23 用 grill-with-docs 追问定稿的全部关键决策。
> 元注:本 skill 自身是用一问一答的 grill-with-docs 设计的——11 轮串行问答正是它要解决的效率问题的现场例证。

## 动机

grill / grill-with-docs 一问一答,每问都要等一轮 LLM 输出,项目启动前的完整设计(数十个决策点)被交互延迟拖垮。但启动前的初始化恰恰最需要工程纪律:VISION、HLD、LLD、ADR、OPEN-DECISIONS 一样不能少。

**解法**:把 grill 的「逐支追问」改为「多波次 Markdown 问卷」——问题批量生成,用户离线作答,答案按类型落盘。

## 范围

- **做**:项目启动初始化(init)+ 重大功能设计(feature)的批量问卷式 grill;vision → hld → lld 三阶段闭环。
- **不做**:实现期单点二义性深钻(grill / grill-with-docs 保留);项目复盘(未来的 retro-questionnaire,复用本 skill 引擎)。

## 关键决策记录

| # | 决策 | 结论 | 理由 / 被否决项 |
|---|---|---|---|
| D1 | 适用范围 | 启动闭环 + 功能设计通用 | 否决「仅启动」(功能设计同样需要纪律)与「完全通用无固定阶段」(失去骨架对「启动前该想清楚什么」的引导力) |
| D2 | 分支机制 | 混合:浅分支内联(限 1 层)+ 深分支分波 | 否决纯分波(轮次多,放大等待问题)与纯问卷内跳转(认知负担重,大量不适用问题) |
| D3 | 与现有 grill 关系 | 并存分工,CLAUDE.md 写触发边界 | 实现期单点深钻仍需要轻便的对话式工具;否决全面替代 |
| D4 | 存放位置 | 用户级 `~/.claude/skills/`,自包含 | 方法论是跨项目个人工作流;不依赖 项目A 的 reference 文档;项目 CLAUDE.md 可覆盖落盘路径 |
| D5 | RETRO | 独立 retro-questionnaire skill,后做,复用引擎 | 复盘与「启动前」时机矛盾;引擎(格式规范 + 处理规则)与模板(骨架)解耦,复用件独立成文 |
| D6 | 分波组织 | 阶段内多波(vision w1,w2,…→ 闸门 → hld …),阶段闸门必须用户确认;OD/ADR 每波处理完即刻写 | 用户明示;符合「即时沉淀,不批处理」;闸门保证跨阶段决策权在人 |
| D7 | 终止条件 | 再无可盘问的信息 = 骨架全覆盖 + 动态盲点清零 + 逃生舱项全进 OD;agent 出示覆盖清单,人确认 | 用户明示;骨架让「无可盘问」可判定,防分析瘫痪也防过早停 |
| D8 | 问题来源 | 阶段固定骨架(优先)+ 动态盲点(探索发现) | 骨架保证纪律不缺项;盲点保证结合项目实际 |
| D9 | 探索与验证 | 按需 1–3 个 Explore subagent 收集事实清单,主 agent 关键点验证(引用进问卷的事实逐条核实原文) | 否决全量复核(违背效率初衷)与不验证(幻觉污染落盘文档) |
| D10 | 作答方式 | 问卷文件是唯一事实源;默认编辑文件,也接受对话速答逐字转写 | 否决仅文件(长问卷繁琐)与仅对话(转写失真、看不到全貌) |
| D11 | 归档 | `harness/questionnaires/archive/`,文件名不变,尾部附处理报告摘要,只移不删 | 原始信息不丢失;git 可 diff;单文件可回溯 |
| D12 | 命名 | design-questionnaire(与 retro-questionnaire 构成 -questionnaire 家族) | 否决 grill-questionnaire(体现机制不体现目的)与 init-design(不体现问卷机制) |

### dogfood 修订(2026-07-23,retro-questionnaire vision W1/W2 实跑产出)

| # | 决策 | 结论 | 来源 |
|---|---|---|---|
| D13 | 问卷模板末尾固定「补充声明」自由书写区,agent 处理时必读 | 已入 QUESTIONNAIRE-FORMAT.md 规则 12 | W2 用户补充声明 |
| D14 | 小波阈值:新一波问题数 ≤ 2 时不生成问卷文件,改用 AskUserQuestion 提问,摘要追加到最近归档问卷 | 已入 SKILL.md 第 2 步、PROCESSING-RULES.md 归档节 | W2 用户补充声明 |
| D15 | TODO.md 机制:行动项落 `<项目根>/TODO.md`,生成问卷 / 阶段闸门 / DoD 核验 / 新会话恢复四个时机必读 | 已入 SKILL.md、PROCESSING-RULES.md 落盘映射 | W2-Q1 自定义答案 |
| D16 | dogfooding 作为可选验证步骤:产物可自用时,收尾前提供「真实小案例走一遍闭环」的选项,缺口即时回修规格 | 已入 SKILL.md 收尾节 | 用户明确指示 |
| D17 | 小项目坍缩选项:定模时询问是否将 HLD/LLD 坍缩为单一 design 阶段(附坍缩骨架) | 已入 SKILL.md 第 0 步、STAGE-SKELETONS.md | retro hld-W1 补充声明 |
| D18 | 引擎复用改为「复制两份 + 双向声明 + 漂移声明是否为设计」(retro hld-W1-Q1 选 B,否决了 D5 的引用假设) | 已入 retro hld_v1;引擎复制声明见下节 | retro hld-W1-Q1 + 自定义 |
| D19 | 坍缩规则细化(修订 D17 的「单一 design 阶段」):有经验 → 完整 HLD+LLD;没经验 → 坍缩为 HLD 边做边调;小项目 → 坍缩为 LLD(HLD 不单独写);agent 给建议、用户定 | 已入 SKILL.md 第 0 步、STAGE-SKELETONS.md 坍缩节 | retro hld 闸门用户指示 |
| D20 | 整理降噪:2026-07-24 用户指示「只清过程性内容」,面对不可逆删除清单时决定全部保留,一字不删 —— 信息不丢失铁律优先于降噪 | 无文件变更 | grill-with-docs 会话,用户撤回 |
| D21 | 引擎第三方复用:grill-questionnaire 复制引擎(D18 机制扩展为三方)。grill-Q 定位为「已有工件的批量问卷式压测」,补 grill 一问一答压测用途的效率缺口;与 design-Q(生成式)正交。双向门,不达 ADR 门槛。drift 声明见上节 | grill-Q 已建:SKILL.md / GRILL-SKELETON.md / 引擎副本两份 / DESIGN.md | grill-with-docs 设计 grill-Q,G1–G8 全接受推荐 |
| D22 | 引擎修改·逃生舱双向门进 OD:降风险协议 step 1 + 落盘映射由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注(双向门/provisional/重访触发)」。来源 grill-Q dogfood 补充声明(逃生舱采用推荐项也要进 OD 留痕,信息不丢失优先)。三份同步,无漂移 | design-Q / retro-Q / grill-Q 三份 PROCESSING-RULES + 三份 DESIGN.md | grill-Q dogfood W01 补充声明 |

## 引擎复制声明(2026-07-23 retro 加入;2026-07-24 grill 加入,扩为三方)

- 本 skill 引擎(QUESTIONNAIRE-FORMAT.md、PROCESSING-RULES.md)为 **canonical**。现有两份副本:retro-questionnaire、grill-questionnaire,共三份。
- 修改本 skill 引擎时,必须考量是否同步另两方副本,并在**三处** DESIGN.md(design-Q / retro-Q / grill-Q)各记一笔(D18 retro 同步规则、G7 grill 同步规则)。
- 若某副本已漂移,漂移方必须在自己的 DESIGN 文档中声明该漂移「是否为设计」。已知漂移:三个副本头部各加了副本标记注释(声明为设计,便于识别副本身份);grill-Q 副本额外在标记下补了一行「stage 固定 grill / 落盘见 GRILL-SKELETON」的本 skill 导读(声明为设计)。
- **2026-07-24 引擎修改(三方同步,无漂移)**:PROCESSING-RULES 降风险协议 step 1 + 落盘映射——双向门逃生舱由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注」。来源:grill-Q dogfood W01 补充声明(D22)。三份已同步。

## 问卷格式核心(详见 QUESTIONNAIRE-FORMAT.md)

- frontmatter:mode / wave / stage / created / status(支持多问卷追踪与归档)
- 每题:选项数不限 + ★推荐(附理由,至多一个)+ 🤔 逃生舱 + ✍️ 自定义 + [落盘:] 提示
- 浅分支内联限 1 层;题量每波 10–15 题,超量拆子波

## 落盘映射(详见 PROCESSING-RULES.md)

阶段题 → VISION / HLD / LLD;术语 → CONTEXT.md;满足三条件 → ADR;逃生舱 → 降风险协议(双向门直接推荐项,单向门进 OD 含重访触发条件)。每波处理完即刻写。

## 验收标准(DoD)

- [x] 5 文件齐全:SKILL.md / QUESTIONNAIRE-FORMAT.md / PROCESSING-RULES.md / STAGE-SKELETONS.md / DESIGN.md
- [x] 格式规范自洽(示例结构可通过自己的解析规则)
- [x] dogfood:retro-questionnaire 全程实跑。vision W1/W2 + hld W1 三波问卷走通「生成 → 作答 → 解析 → 落盘 → 归档」全链路,两道闸门通过;产出规格修订 D13–D19;retro 本体已按坍缩决策直接实现(2026-07-24)
- [x] 全局 CLAUDE.md 与 项目A CLAUDE.md(+ AGENTS.md 同步)更新触发边界

## 已知风险

| 风险 | 缓解 |
|---|---|
| 问卷形式主义(题目空泛、照抄骨架) | 规则 7:探索发现的题必须附出题依据与出处 |
| 用户不答必答题 | 解析规则:必答未答下一波重出并标注 |
| 引擎与 retro-questionnaire 漂移 | 引擎独立成两文件,复用方只换骨架;改动时同步检查复用方 |
| 阶段间依赖出错(HLD 基于错误 VISION) | 阶段闸门:进下一阶段前用户显式确认上阶段定稿 |

## 引擎同步记录(2026-08-03)

- **预勾选开关化 + 选项排序统一**(OD-14 修订,用户裁决,action-Q 确认清单 confirm-pregou-switch-w00 全确认):
  - 预勾选 = **opt-in 开关,默认关**——仅当用户启动 skill 时明确说「预勾选」才预勾推荐选项;未启用时全部 `[ ]`;
  - **选项排序(非推荐在前 → 逃生舱倒数第二 → 推荐最后)= 默认行为,不依赖开关**;
  - **单向门题(发布/删除/花钱/脱敏)永不预勾**;预勾设防(取消率 / 确认点 / 3 波零取消警告)开关开启时适用;
  - 本 skill 与 design-Q / grill-Q / retro-Q / action-Q **四份副本同步**(OD-8 重访触发①命中);问题级排序仅 design-Q 保留。
- **实测与调研前置标准流程**(2026-08-03,action-Q 确认清单 confirm-testing-preflight-w00 全确认):SKILL.md「生成问卷」前新增标准步骤「实测与调研前置」(调研现状 / 不假设 / 多实测 / 多获取信息 / 及时保存);retro-Q 版为「调研与核实前置」(五源读取的补齐);既有铁律段(环境现实现证 / 先验证再出题 / 先核实再列清单)保留引用。

## skill-spec-revamp 修订(2026-08-06/07,design-Q 三组改动)

> 来源:design-questionnaire 三阶段设计(vision/hld/lld)+ grill-Q 压测(11 题,9 项回灌)+ grill-with-docs Q7 深钻。设计套 `harness/design/skill-spec-revamp/`(VISION/HLD/LLD)。🔧 HLD/LLD 判别法则 + 最小必含仅 design-Q 骨架,不扩散到 retro/grill/action(改动 2/3 边界)。

### 新增决策(均双向门,可回退;难逆转性不足 ADR 三条件,记本 DESIGN.md)

| # | 决策 | 结论 | 出处 |
|---|---|---|---|
| D23 | 落盘路径配置化(方案 R) | 默认 `harness/` + CLAUDE.md 声明覆盖(关键词非穷举)+ 落盘前确认(首次 + 结构变化)+ 无 CLAUDE.md 跳过默认;落盘根边界 = 通用三件(design/ + questionnaires/ + adr/),CONTEXT/OPEN-DECISIONS/TODO 项目固有路径不动 **(2026-08-07 superseded:方案 R 已放弃,回归硬编码 `harness/`,见 ADR-0011)** | hld W01 + vision W01 Q2=C + 🔧 grill-Q Q1/Q4/Q6/Q10/Q11 |
| D24 | HLD/LLD 判别法则 | phase-invariant(HLD)vs incremental(LLD)+ 两句判别问句 + 职责不重叠;落 STAGE-SKELETONS.md 头部节 | hld W01 Q2=A |
| D25 | 最小必含 + 产出形态 | 每项骨架加「最小必含」子项(约束内容非仅结构,防简化)+ 「产出形态」标注;H1–H5 + L1–L5 共 10 项;坍缩档不免除最小必含 | hld W01 Q3(10 项全量)+ Q4(形态非强制)+ 🔧 grill-Q Q2 |
| D26 | 全局生效 | 改 `~/.claude/skills/` 全局生效(所有项目下次调用);不跨域立 ADR | vision W01 Q2=C |

### 引擎同步记录(OD-8 重访触发①命中)

- **2026-08-06 落盘路径配置化同步**:design-Q canonical(PROCESSING-RULES 落盘映射 + 落盘根定义 + SKILL 路径决定 + QUESTIONNAIRE-FORMAT 文件约定)改后,**四副本(grill-Q / retro-Q / action-Q)落盘映射节同步**(🔧 Q5:仅落盘映射节 diff 0,不含各副本有意分叉区——action-Q 小波阈值 ≤4 / confirm-list;grill-Q stage 标记;retro 骨架);**long-running SKILL.md §5.3 读归档问卷路径配置化**(🔧 Q3)。
- 🔧 **Q7 深钻结论(2026-08-07 grill-with-docs)**:retro 文档落点 = 项目固有 `docs/retro/`(不纳入落盘根配置化);四副本同步只改「描述宿主项目落盘路径」的字符串,**不改** skill 自身目录内部相对引用(判据:`./docs/...` 指 skill 内部 vs `docs/...` 描述宿主)。
- HLD/LLD 判别法则 + 最小必含 = design-Q 专属,**不扩散**到 retro/grill/action 骨架(改动 2/3 边界硬约束)。

## 未验证假设生命周期管理(2026-08-07,action-Q 确认清单 confirm-design-q-unverified-assumptions-w00)

> 来源:action-Q confirm-list(W00 15 条确认 + 小波裁决「复用前重验扩散到 action-Q」)。双向门,难逆转性不足 ADR 三条件,记本 DESIGN.md 不立 ADR。
> 缺口:验证纪律(铁律5 / 环境现实现证 / 实测前置)全部锚定「出题时」;构想 / 需求随问卷演进,早期未实测信息可能在下一阶段成为规划支撑,无跨波台账、闸门不查下阶段依赖。本次补「生命周期管理」,不推翻既有纪律。

| # | 决策 | 结论 |
|---|---|---|
| D27 | 未验证假设台账 | 每波处理时从三处收集(出题依据标注 + 用户回答引出 + 上波遗留)进台账,跨波追踪,记录假设 / 出处(问卷+题号)/ 涉及阶段 / 状态(pending / verified / stale);落点 = 每波处理报告「未验证假设台账」节(随归档问卷尾部留存);只跟踪影响后续规划的信息,防形式主义 |
| D28 | 复用前重验 | 信息成为下一阶段文档规划基础前,先实测 / 核实原文;无法验证 → 显式标注「未验证 + 将作为 X 的规划基础」提交用户确认或走降风险协议,不静默采用 |
| D29 | 阶段闸门汇报 | 闸门出示覆盖清单时,一并出示「下一阶段将依赖的未验证信息」清单(来源:台账) |
| D30 | 扩散 action-Q | 「复用前重验」扩散到 action-Q confirm-list(引用之前确认过但从未实测的信息时,先重验再列入);台账 + 闸门汇报不扩散(action-Q 无阶段概念)——action-Q DESIGN.md 另行记录 |
