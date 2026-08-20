# design-questionnaire · 设计文档

> 本 skill 的设计决策记录(定位 / 设计决策 D1–D38 / 已知限制);治理历史(创建起源/引擎同步/压测裁决时间线)见 [CHANGELOG.md](./CHANGELOG.md)。
> 元注:本 skill 自身是用一问一答的 grill-with-docs 设计的——11 轮串行问答正是它要解决的效率问题的现场例证。

## 动机与范围

grill / grill-with-docs 一问一答,每问都要等一轮 LLM 输出,项目启动前的完整设计(数十个决策点)被交互延迟拖垮。但启动前的初始化恰恰最需要工程纪律:VISION、HLD、LLD、ADR、OPEN-DECISIONS 一样不能少。

**解法**:把 grill 的「逐支追问」改为「多波次 Markdown 问卷」——问题批量生成,用户离线作答,答案按类型落盘。

- **做**:项目启动初始化(init)+ 重大功能设计(feature)的批量问卷式 grill;L0 → L1 → L2 层级闭环(LN 制)。
- **不做**:实现期单点二义性深钻(grill-with-docs 保留);项目复盘(retro-questionnaire,复用本 skill 引擎)。

## 设计决策(D1–D12 · 创建期)

| # | 决策 | 结论 | 理由 / 被否决项 |
|---|---|---|---|
| D1 | 适用范围 | 启动闭环 + 功能设计通用 | 否决「仅启动」(功能设计同样需要纪律)与「完全通用无固定阶段」(失去骨架对「启动前该想清楚什么」的引导力) |
| D2 | 分支机制 | 混合:浅分支内联(限 1 层)+ 深分支分波 | 否决纯分波(轮次多,放大等待问题)与纯问卷内跳转(认知负担重,大量不适用问题) |
| D3 | 与现有 grill 关系 | 并存分工,CLAUDE.md 写触发边界 | 实现期单点深钻仍需要轻便的对话式工具;否决全面替代 |
| D4 | 存放位置 | 用户级 `~/.claude/skills/`,自包含 | 方法论是跨项目个人工作流;项目 CLAUDE.md 可覆盖落盘路径 |
| D5 | RETRO | 独立 retro-questionnaire skill,后做,复用引擎 | 复盘与「启动前」时机矛盾;引擎(格式规范 + 处理规则)与模板(骨架)解耦,复用件独立成文 |
| D6 | 分波组织 | 层内多波(w1,w2,…→ 闸门 → 下一层 …),层闸门必须用户确认;OD/ADR 每波处理完即刻写 | 用户明示;符合「即时沉淀,不批处理」;闸门保证跨层决策权在人 |
| D7 | 终止条件 | 再无可盘问的信息 = 骨架全覆盖 + 动态盲点清零 + 逃生舱项全进 OD;agent 出示覆盖清单,人确认 | 用户明示;骨架让「无可盘问」可判定,防分析瘫痪也防过早停 |
| D8 | 问题来源 | 层固定骨架(优先)+ 动态盲点(探索发现) | 骨架保证纪律不缺项;盲点保证结合项目实际 |
| D9 | 探索与验证 | 按需 1–3 个 Explore subagent 收集事实清单,主 agent 关键点验证(引用进问卷的事实逐条核实原文) | 否决全量复核(违背效率初衷)与不验证(幻觉污染落盘文档) |
| D10 | 作答方式 | 问卷文件是唯一事实源;默认编辑文件,也接受对话速答逐字转写 | 否决仅文件(长问卷繁琐)与仅对话(转写失真、看不到全貌) |
| D11 | 归档 | `harness/questionnaires/archive/`,文件名不变,尾部附处理报告摘要,只移不删 | 原始信息不丢失;git 可 diff;单文件可回溯 |
| D12 | 命名 | design-questionnaire(与 retro-questionnaire 构成 -questionnaire 家族) | 否决 grill-questionnaire(体现机制不体现目的)与 init-design(不体现问卷机制) |

## 设计决策(D13–D22 · dogfood 修订期)

| # | 决策 | 结论 | 来源 |
|---|---|---|---|
| D13 | 问卷模板末尾固定「补充声明」自由书写区,agent 处理时必读 | 已入 QUESTIONNAIRE-FORMAT.md 规则 12 | retro vision W2 用户补充声明 |
| D14 | 小波阈值:新一波问题数过小时不生成问卷文件,改用 AskUserQuestion 提问,摘要追加到最近归档问卷(现值 ≤3,见格式参数节) | 已入 SKILL.md 第 2 步、PROCESSING-RULES.md 归档节 | retro vision W2 用户补充声明 |
| D15 | TODO.md 机制:行动项落 `<项目根>/TODO.md`,生成问卷 / 层闸门 / DoD 核验 / 新会话恢复四个时机必读 | 已入 SKILL.md、PROCESSING-RULES.md 落盘映射 | retro vision W2-Q1 自定义答案 |
| D16 | dogfooding 作为可选验证步骤:产物可自用时,收尾前提供「真实小案例走一遍闭环」的选项,缺口即时回修规格 | 已入 SKILL.md 收尾面板第 2 问 | 用户明确指示 |
| D17 | 小项目坍缩选项:定模时询问是否坍缩(附坍缩骨架;后由 LN 制「初始层数 = 最小 1 层」承接) | 已入 SKILL.md 第 0 步、STAGE-SKELETONS.md | retro hld-W1 补充声明 |
| D18 | 引擎复用改为「复制 + 双向声明 + 漂移声明是否为设计」(否决了 D5 的引用假设) | 引擎复制声明见下节 | retro hld-W1-Q1 选 B |
| D19 | 坍缩规则细化(修订 D17):有经验 → 完整三层;没经验 → 坍缩边做边调;小项目 → 单层;agent 给建议、用户定 | 已入 SKILL.md 第 0 步、STAGE-SKELETONS.md | retro hld 闸门用户指示 |
| D20 | 整理降噪:用户指示「只清过程性内容」,面对不可逆删除清单时决定全部保留,一字不删 —— 信息不丢失铁律优先于降噪 | 无文件变更 | grill-with-docs 会话,用户撤回 |
| D21 | 引擎第三方复用:grill-questionnaire 复制引擎(D18 机制扩展)。grill-Q 定位为「已有工件的批量问卷式压测」,与 design-Q(生成式)正交。双向门,不达 ADR 门槛 | grill-Q 已建(引擎副本两份) | grill-with-docs 设计 grill-Q,G1–G8 全接受推荐 |
| D22 | 引擎修改·逃生舱双向门进 OD:降风险协议 step 1 + 落盘映射由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注(双向门/provisional/重访触发)」 | 三份同步,无漂移 | grill-Q dogfood W01 补充声明 |

## 引擎复制声明(现行规则,OD-8/OD-11 治理)

- 本 skill 引擎(QUESTIONNAIRE-FORMAT.md、PROCESSING-RULES.md)为 **canonical**。现有三份副本:retro-questionnaire、grill-questionnaire、action-questionnaire,共四份。
- 修改本 skill 引擎时,必须考量是否同步另三方副本,并在**四处** DESIGN.md(design-Q / retro-Q / grill-Q / action-Q)各记一笔;各副本的有意分叉见各自 FORK-NOTES.md。
- 若某副本已漂移,漂移方必须声明该漂移「是否为设计」;历史同步事件见 CHANGELOG。

## 设计决策(D23–D26 · skill-spec-revamp)

| # | 决策 | 结论 | 出处 |
|---|---|---|---|
| D23 | 落盘路径配置化(方案 R) | **superseded:方案 R 已放弃,回归硬编码 `harness/`**(ADR-0011) | hld W01 + grill-Q Q1/Q4/Q6/Q10/Q11 |
| D24 | HLD/LLD 判别法则 | phase-invariant(契约层)vs incremental(构建层)+ 两句判别问句 + 职责不重叠;落 STAGE-SKELETONS.md 头部节 | hld W01 Q2=A |
| D25 | 最小必含 + 产出形态 | 每项骨架加「最小必含」子项(约束内容非仅结构,防简化)+ 「产出形态」标注;H1–H5 + L1–L5 共 10 项;坍缩档不免除最小必含 | hld W01 Q3 + Q4 + grill-Q Q2 |
| D26 | 全局生效 | 改 `~/.claude/skills/` 全局生效(所有项目下次调用);不跨域立 ADR | vision W01 Q2=C |

HLD/LLD 判别法则 + 最小必含 = design-Q 专属,**不扩散**到 retro/grill/action 骨架(改动边界硬约束)。

## 设计决策(D27–D30 · 未验证假设生命周期管理)

> 缺口背景:验证纪律(铁律5 / 环境现实现证 / 实测前置)全部锚定「出题时」;构想 / 需求随问卷演进,早期未实测信息可能在下一阶段成为规划支撑,无跨波台账、闸门不查下阶段依赖。

| # | 决策 | 结论 |
|---|---|---|
| D27 | 未验证假设台账 | 每波处理时从三处收集(出题依据标注 + 用户回答引出 + 上波遗留)进台账,跨波追踪,记录假设 / 出处(问卷+题号)/ 涉及阶段 / 状态(pending / verified / stale);落点 = 每波处理报告「未验证假设台账」节(随归档问卷尾部留存);只跟踪影响后续规划的信息,防形式主义 |
| D28 | 复用前重验 | 信息成为下一阶段文档规划基础前,先实测 / 核实原文;无法验证 → 显式标注「未验证 + 将作为 X 的规划基础」提交用户确认或走降风险协议,不静默采用 |
| D29 | 阶段闸门汇报 | 闸门出示覆盖清单时,一并出示「下一阶段将依赖的未验证信息」清单(来源:台账) |
| D30 | 扩散 action-Q | 「复用前重验」扩散到 action-Q confirm-list;台账 + 闸门汇报不扩散(action-Q 无阶段概念) |

## 格式参数(四副本统一)

| 项 | 现值 | 落点 |
|---|---|---|
| 题量上限 | 每波 10(原 10–15,grill-Q 压测裁决收紧) | 四份 QUESTIONNAIRE-FORMAT 规则 8 |
| 小波阈值 | 四份统一 ≤3(action-Q 原 ≤4 有意分叉修订,不撤销 confirm-list 语义分叉) | 四份 SKILL.md 第 2 步 + PROCESSING-RULES 提问波 |

## 设计决策(D31–D38 · grill-design-q 三透镜压测)

| # | 决策 | 结论 | 出处 |
|---|---|---|---|
| D31 | W00 价值定位 | 全量维持,防漏优先于防重复问;**护栏观测与机制审判分离**——质量信号(全采纳率,防默认效应)落地,统计验证不做,防混用 | Q6-C + Q4-A |
| D32 | 入口校准闸门 | 每层生成 W00 前出示「项目理解摘要 + 本层设计焦点」AskUserQuestion 确认;轻量模式豁免;与 grill-Q 入口闸门对称 | Q3-A |
| D33 | 收尾面板化 | 四项衔接(dogfood/压测/多线程必停/long-running)合并为单次 AskUserQuestion 多问题面板;多线程必停居首问,裁决语义不变 | Q7-A |
| D34 | 处理报告全文归档 | 归档时全文追加问卷尾部,摘要节保留速览——「原始信息不丢失」覆盖解析产物 | Q9-A |
| D35 | W00 推理句分级 | 高 stakes/单向门要点默认倾向后附一句推理(不限字数);低 stakes 从简——L2 留痕按哲学「度」分级 | Q8-B + ✍️ |
| D36 | delegate 白名单接口 | 触发三条件与(feature 模式 + delegation.md 存在且开关开 + **人当次会话明示**);白名单内不出独立题、合并**单题「白名单包确认」**;留痕双落(处理报告清单 + delegation-log 逐例);残余张力落 OD-27 | Q5-C + ⚠ 三点细则 |
| D37 | 形态×协议交叉表 | STAGE-SKELETONS 补「形态 × 协议」交叉表;「修订自检清单」不建,进 OD-28 观察(对齐 ADR-0023 升格机制) | Q10-A |
| D38 | 规格同步修复 | 落盘映射表 + SKILL.md 落盘行修 LN 制(旧三件仅存量豁免);W00→W01 时序明确(W00 处理后生成 W01),FORMAT「追加区」机制废止 | Q1-B + Q2-A |

## 问卷格式核心(详见 QUESTIONNAIRE-FORMAT.md)

- frontmatter:mode / wave / stage / created / status(支持多问卷追踪与归档)
- 每题:选项数不限 + ★推荐(附理由,至多一个)+ 🤔 逃生舱 + ❌ 跑偏标注(grill-Q 专属)+ ✍️ 自定义(题目最后一位)+ [落盘:] 提示
- 浅分支内联限 1 层;题量每波上限 10,超量拆子波

## 落盘映射(详见 PROCESSING-RULES.md)

层题 → LN 层文件;术语 → CONTEXT.md;满足三条件 → ADR;逃生舱 → 降风险协议(双向门直接推荐项 + 进 OD 标注,单向门进 OD 含重访触发条件)。每波处理完即刻写。

## 验收标准(DoD)

- [x] 5 文件齐全:SKILL.md / QUESTIONNAIRE-FORMAT.md / PROCESSING-RULES.md / STAGE-SKELETONS.md / DESIGN.md
- [x] 格式规范自洽(示例结构可通过自己的解析规则)
- [x] dogfood:retro-questionnaire 全程实跑(vision W1/W2 + hld W1 三波问卷走通全链路,两道闸门通过;产出 D13–D19;retro 本体已按坍缩决策直接实现)
- [x] 全局 CLAUDE.md 与宿主项目 CLAUDE.md(+ AGENTS.md 同步)更新触发边界

## 已知限制与风险

| 项 | 说明 / 缓解 |
|---|---|
| 问卷形式主义(题目空泛、照抄骨架) | 规则 7:探索发现的题必须附出题依据与出处 |
| 用户不答必答题 | 解析规则:必答未答下一波重出并标注 |
| 引擎与三副本漂移 | 引擎独立成两文件,复用方只换骨架;改动时四方同步检查(OD-8/OD-11) |
| 层间依赖出错(L1 基于错误 L0) | 层闸门:进下一层前用户显式确认上一层定稿 |
| 本 skill 为引擎 canonical,自身无规则本体级分叉 | 无 FORK-NOTES;下游副本分叉见各 skill FORK-NOTES |
