# grill-questionnaire · 设计文档

> 2026-07-24 由 grill-with-docs 单点深钻定稿(8 个决策,全部接受推荐)。
> 本 skill 的决策进本文件;**不污染宿主项目(项目A)的 CONTEXT/ADR/OD**——skill 自身的设计与宿主项目正交。
> 元注:本 skill 是用一问一答的 grill-with-docs 设计的,而它本身正是为了把 grill 的一问一答改为批量问卷。设计它用的工具,正是它要替代的工具。

## 动机

grill / grill-with-docs 的压测用途(找漏洞、找盲点、找单向门、降风险)至今仍是一问一答,每问等一轮 LLM 输出。design-questionnaire 与 retro-questionnaire 已把「生成式设计」和「事后复盘」改成了批量问卷,但**事前压测**这一用途还卡在一问一答。grill-questionnaire 补这个缺口:把 grill 的压测用途改成多波次问卷。

**原初设计原则补记**(2026-07-31 作者陈述,此前未落盘):设计前提 = 对抗幻觉;核心原则 = **80/20 判断成本原则**——批量问卷以 20% 时间高速处理 80% 可预知的基础问题(D1–D8 本质是已知攻击面的知识沉淀),依赖链深、需即时反馈的 20% 关键问题(本 skill 的「深水区」)转 grill-with-docs 一问一答深钻,人投 80% 时间;目的 = 减少人的判断成本;定位 = design 系列流程的 review 步。谱系:本 skill 是 grill-with-docs 的问卷化演进(忠于其最初设计,改善问答机制)。认定:G1「仅压测」的出生 scoping 决定后续漂移化为「与 with-docs 的用途切割」——工具链路自洽,但文档长期未承认 80/20 分层(依据:2026-07-31 生态位区分分析,归档 confirm-grill-niche-distinguish-w00)。

## 范围

- **做**:压测一份已有工件(计划 / 决策 / 架构提案 / ADR 草稿 / 设计文档),批量问卷式找漏洞、盲点、单向门;发现按类型落盘(CONTEXT / ADR / OD + 工件修订建议)。
- **不做**:从零生成设计(design-questionnaire 管);事后复盘(retro-questionnaire 管);实现期单点深钻(grill / grill-with-docs 管)。

## 术语

- **工件 (artifact)**:grill-Q 的压测对象。一份已有的、承载决策内容的文档——计划、决策记录、架构提案、ADR 草稿、HLD/LLD 草稿等。可以是项目里的文件,也可以是用户粘贴的文本。区别于 design-Q 产出的「草稿」:工件强调「已经存在、要被挑战」,而非「正在生成」。

## 关键决策记录

| # | 决策 | 结论 | 理由 / 被否决项 | 来源 |
|---|---|---|---|---|
| G1 | 核心定位 | 压测已有工件(对抗式,无固定骨架,工件驱动出题) | design-Q 的分工表已把「计划评审」划给 grill,design-Q 自身不做压测——缺口真实。否决「也含未成形念头」(与 design-Q feature 模式边界模糊) | Q1 |
| G2 | 代码库绑定 | 绑定为默认;无项目上下文(纯计划文本)时降级为纯逻辑压测,产出审阅报告入 `~/notes/` | 压测最值钱的部分是「工件与现实/既有决策的矛盾」,必须绑代码库才能查;与 design-Q/retro-Q 同源。一个 skill,行为随上下文自适应,避免 grill/grill-with-docs 的双 skill 分裂 | Q2 |
| G3 | 出题模型 | 混合:固定压测维度(D1–D8)+ 工件驱动具体化 + 探索盲点 | 镜像 design-Q「骨架+盲点」。固定维度保证覆盖通用攻击面(防 agent 只问软柿子题);工件驱动保证题目具体不空泛。否决「纯工件驱动无固定维度」(无覆盖保证) | Q3 |
| G4 | 工件修订 | 只产出发现,不替改工件文件 | 对标 retro「只记录不决策」+ grill-with-docs 即时沉淀。发现分两类:① 工件漏洞/盲点/单向门 → 处理报告(对话内,人决定是否修订,grill-Q 不碰工件文件);② 可沉淀的决策/风险/术语 → 即时写 CONTEXT/ADR/OD。守住「AI 不替人决策」。否决「直接回写工件」(越界替人改决策工件)与「纯对话不落盘」(丢沉淀) | Q4 |
| G5 | 触发 | 手动为主 + design-Q 收尾后主动提议一次 | 手动:用户「压测/审一下/挑毛病」+ 指向工件。主动:仅 design-Q 产设计草稿收尾时提议一次,接上 write→review 闭环。不做「任何不可逆实现前」的泛化主动提议(太吵且难判定) | Q5 |
| G6 | 波次与终止 | 单次完整压测 + 按需补波;终止 = 8 维度全覆盖 + 工件关键声明逐条审视 + 盲点清零 + 逃生舱进 OD | 对标 retro-Q。工件有限,一轮把 8 维度套到工件每条关键声明;题量超 15 拆子波;仅当答案引出新漏洞/新盲点时出补充波。否决 design-Q 式多波循环(工件有限时易注水,且无阶段闸门可过) | Q6 |
| G7 | 引擎复用 | 沿用 D18:复制两份 + 三方 drift 声明,design-Q 为 canonical | 引擎至今仅 dogfood 改过一次(D13–D19),retro 副本与原件只差一行标记,漂移可控。否决「重构共享引擎目录」(跨 skill 相对引用在 Claude Code 按需加载下断裂风险,D18 否决过;且要回改 retro 副本)。双向门,不达 ADR 门槛 | Q7 |
| G8 | 文件结构 | SKILL.md + GRILL-SKELETON.md(独立成文)+ 引擎副本两份 + DESIGN.md;问卷 `harness/questionnaires/grill-<slug>-w<NN>.md`(slug=工件短名),归档同目录 | 与 design-Q(STAGE-SKELETONS)/ retro-Q(RETRO-SKELETONS)家族一致,骨架独立成文。否决「骨架内联进 SKILL.md」(与家族不一致,SKILL.md 变长) | Q8 |

### dogfood 修订(2026-07-24,自压测 DESIGN.md)

用 grill-Q 压测自己的 DESIGN.md(8 维度套 G1–G8)。问卷归档于 [grill-own-design-w01.md](./docs/questionnaires/archive/grill-own-design-w01.md)。抓出 8 个缺口 + 1 条补充声明,全部已落盘。

| # | 决策 | 结论 | 来源 |
|---|---|---|---|
| D22 | dogfood Q1–Q8 修订 | 接受推荐:Q1(design-Q 收尾加 grill-Q 提议 hook)、Q2(项目A 衔接已含,核对无操作)、Q4(修订建议 ≥15 题按严重度排序,GRILL-SKELETON)、Q5(超大工件分块,SKILL 第 1 步)、Q6(安全由 D1/D4/D5 交叉覆盖,GRILL-SKELETON)、Q7(定义「关键声明」,SKILL 第 1 步 + GRILL-SKELETON 覆盖度)。否决推荐:Q3(维度集不记被否决划分法——接受 D3 自相矛盾代价,维度集视为实践提炼非关键决策)、Q8(主动提议不收窄——小项目噪音由用户自拒)。Q3/Q8 为 conscious choice,记此防再问 | dogfood W01 Q1–Q8 |
| D23 | 逃生舱 family-wide 进 OD(引擎修改) | 双向门逃生舱由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注(双向门/provisional/重访触发)」。三份引擎同步(design-Q D22 / retro-Q 引擎声明 / 本文件),无漂移。权衡:信息不丢失优先;代价是 OD 可能多轻量 provisional 条目(后续观察是否需细化阈值,如「仅单向门 + 高风险双向门进 OD」) | dogfood W01 补充声明 |

## 压测维度(grill 骨架,详见 GRILL-SKELETON.md)

固定维度 = 通用压测攻击面清单;每维度下的题结合工件具体化(不得照抄维度名);探索盲点补充。

**两模式通用**
- D1 未言明假设 — 工件建立在哪些没说出口的假设上?逐条列,标 成立/存疑/失效
- D2 单向门/可逆性 — 哪些选择难逆转?是否标了可逆性?该进 ADR 还是 OD?
- D3 替代方案/被否决项 — 关键决策是否给了被否决项?还是只有一个方案?
- D4 失败模式/爆炸半径 — 出错时怎样?能否降级?影响面多大?
- D5 盲点 — 该说没说的:边界/错误路径/并发/回滚/迁移
- D6 可验证性 — 验收/DoD 可检查还是空话?

**仅代码库绑定模式**
- D7 与现实的矛盾 — 工件说 X,但代码/CONTEXT/ADR 是 Y(压测最值钱的一项)
- D8 术语一致性 — 用词与 CONTEXT 定义是否冲突/重载/模糊?

## 引擎复制声明(2026-07-24,G7)

- grill-questionnaire 持有 design-questionnaire 引擎(QUESTIONNAIRE-FORMAT.md、PROCESSING-RULES.md)的**副本**。design-Q 引擎为 canonical。
- 修改任一方的引擎时,必须考量另两方(design-Q、retro-Q、grill-Q 三副本),并在三处 DESIGN.md 各记一笔。
- 若某副本已漂移,漂移方必须在自己的 DESIGN 文档中声明该漂移「是否为设计」。
- 三副本头部各标「副本,以 design-Q 为准,故意漂移需声明」。
- **2026-07-24 引擎修改(本 skill dogfood 发起,三方同步)**:PROCESSING-RULES 降风险协议 step 1 + 落盘映射——双向门逃生舱由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注」。来源:本 skill dogfood W01 补充声明(见 D23)。三方已同步(design-Q D22 / retro-Q 引擎声明 / 本文件)。
- **2026-07-27 引擎漂移(本 skill 不同步,声明为设计)**:design-Q canonical 演进——preview 拆独立 W00 波(勾=采纳/留空=不采纳、无 🤔,与 W01 分开交付)。本 skill(grill-Q)**不使用 preview**(压测场景工件已存在,无阶段默认值可预答),故不同步该引擎改动; FORMAT/RULES 副本维持 2026-07-24 版本。retro-Q 同理不使用 preview。三方协议下,此漂移**声明为设计**(非遗漏),待 preview 机制在 design-Q 经更多样本验证后,再评估是否需要统一 preview 概念或引擎单源化(见 M7/观察项)。
- **2026-07-25 引擎修改(design-Q dogfood 发起,本副本暂未同步)**:design-Q 在 QUESTIONNAIRE-FORMAT 增加「preview 预答层」规范(文件结构模板 + 规则 13)、PROCESSING-RULES 增加 preview 预答解析与处理报告统计行。来源:delegate × design-Q dogfood round 1(宿主项目某 dogfood 问卷)。按三方协议先只在 design-Q 生效(dogfood 验证中),验证有效后回同步——**声明:此漂移为设计**。

## 问卷格式核心(详见 QUESTIONNAIRE-FORMAT.md · 引擎副本)

- frontmatter:mode / wave / stage(此处 stage 固定 `grill`)/ created / status
- 每题:选项数不限 + ★推荐(附理由,至多一个)+ 🤔 逃生舱 + ✍️ 自定义 + [落盘:] 提示
- 浅分支内联限 1 层;题量每波上限 10 题(2026-08-08 收紧,原 10–15),超量拆子波;≤3 题走 AskUserQuestion(小波阈值,引擎规则)

## 落盘映射(详见 PROCESSING-RULES.md · 引擎副本 + GRILL-SKELETON.md 维度落盘)

- 工件漏洞/盲点/单向门/缺失替代方案 → **处理报告(对话内)**,人决定是否修订工件(grill-Q 不碰工件文件)
- 难逆转+会困惑+真权衡 → harness/adr/
- 其余单向门 / 重大风险 / 存疑假设 → OPEN-DECISIONS.md(归属见 HARNESS-RULES.md 第六节,2026-08-14 修订)
- 术语冲突 → CONTEXT.md
- 纯逻辑模式(无项目上下文)→ 审阅报告入 `~/notes/`,不写 CONTEXT/ADR/OD

## 验收标准(DoD,待实现勾选)

- [x] 5 文件齐全:SKILL.md / GRILL-SKELETON.md / QUESTIONNAIRE-FORMAT.md(副本)/ PROCESSING-RULES.md(副本)/ DESIGN.md
- [x] GRILL-SKELETON.md 含 D1–D8 维度 + 出题方向 + 落盘映射 + 两模式说明
- [x] 引擎副本含三方 drift 标记注释
- [x] 全局 CLAUDE.md 与 项目A CLAUDE.md(+ AGENTS.md 同步)家族表加 grill-questionnaire 行
- [x] dogfood:2026-07-24 自压测——用 grill-Q 压测自己的 DESIGN.md,问卷归档 [grill-own-design-w01.md](./docs/questionnaires/archive/grill-own-design-w01.md),抓出 8 缺口 + 1 补充声明,修订见 D22/D23

## 已知风险

| 风险 | 缓解 |
|---|---|
| 维度形式主义(题目空泛、照抄维度名) | 引擎规则 7:探索发现的题必须附出题依据与出处;维度下的题必须结合工件具体化 |
| 压测发现无人修订工件(发现落了灰) | 处理报告明确标「工件修订建议」;纯逻辑模式落 ~/notes/ 持久化;代码库模式可挂 TODO.md;**第 5 步收尾主动询问是否执行修订**(2026-07-28,参照 grill-with-docs 主动决策风格)——完成清单输出后不静默等待,立即 AskUserQuestion 把"是否落地修订"作为显式决策点,用户授权后才执行(询问+授权=人发起,不违反铁律 2) |
| 与 design-Q feature 模式混淆 | G1 边界:design-Q 生成式(从零、固定骨架),grill-Q 对抗式(已有工件、无骨架);design-Q 收尾主动提议 grill-Q 是衔接点 |
| 三副本引擎漂移 | G7 三方 drift 声明 + 副本头部标记;引擎极少改 |
| 降级模式(纯逻辑)力度弱 | D7/D8 失效时明确告知用户「未对照代码库,建议在有项目上下文时复压」 |
| 框架级理解跑偏(整卷在错误框架内自洽,题内裁决碰不到——CONTEXT「AI 同源出题限定」的出题层同构) | 入口校准闸门(SKILL 第 1 步末,轻量豁免)+ ❌ 题级跑偏标注(FORMAT 规则 15)+ 同波 ≥2 题被标 → 停波回炉(PROCESSING-RULES);跨波优化走处理报告质量信号节 → retro 聚合 → ADR-0023 升格(OD-26 provisional) |
| 绿地项目(有 docs 无代码)D7 误判为无效 | GRILL-SKELETON D7 + SKILL 模式判定补「绿地子模式」:D7 的「现实」转为既有设计文档/ADR/约束(工件内部一致性 + 设计 vs 既有约束),D1–D8 全开。项目B dogfood Q15 实证:绿地模式 D7 抓出既有 ADR 与 LLD 数据结构选型不一致(2026-07-27) |

## 引擎同步记录(2026-08-03)

- **预勾选开关化 + 选项排序统一**(OD-14 修订,用户裁决,action-Q 确认清单 confirm-pregou-switch-w00 全确认):
  - 预勾选 = **opt-in 开关,默认关**——仅当用户启动 skill 时明确说「预勾选」才预勾推荐选项;未启用时全部 `[ ]`;
  - **选项排序(非推荐在前 → 逃生舱倒数第二 → 推荐最后)= 默认行为,不依赖开关**;
  - **单向门题(发布/删除/花钱/脱敏)永不预勾**;预勾设防(取消率 / 确认点 / 3 波零取消警告)开关开启时适用;
  - 本 skill 与 design-Q / grill-Q / retro-Q / action-Q **四份副本同步**(OD-8 重访触发①命中);问题级排序仅 design-Q 保留。
- **实测与调研前置标准流程**(2026-08-03,action-Q 确认清单 confirm-testing-preflight-w00 全确认):SKILL.md「生成问卷」前新增标准步骤「实测与调研前置」(调研现状 / 不假设 / 多实测 / 多获取信息 / 及时保存);retro-Q 版为「调研与核实前置」(五源读取的补齐);既有铁律段(环境现实现证 / 先验证再出题 / 先核实再列清单)保留引用。

## skill-spec-revamp 同步记录(2026-08-06/07,OD-8 重访触发①)

- **落盘路径配置化同步**:本 skill(PROCESSING-RULES 落盘映射 + 落盘根定义 + SKILL 路径决定 + QUESTIONNAIRE-FORMAT 文件约定 + GRILL-SKELETON 落盘指引)已与 design-Q canonical 同步——路径配置化为 `<根>` / `<落盘根>`,四 skill(design-Q / grill-Q / retro-Q / action-Q)沿用同一根约定(方案 R)。
- 🔧 **Q5 同步范围**:仅「落盘映射节」diff 0(路径 + 落盘根定义机制一致);grill-Q 有意分叉区(stage 固定 grill / GRILL-SKELETON 独立 / 不产生阶段题)原样保留。
- 🔧 **Q7 路径区分**:本 skill DESIGN.md / SKILL.md 内 `[docs/...](./docs/...)` 为 skill 自身目录内部引用(归档问卷 / 设计文档),**不动**;配置化只改「描述宿主项目落盘路径」的字符串。
- HLD/LLD 判别法则 + 最小必含 = design-Q 专属骨架,**不扩散**到 grill-Q(GRILL-SKELETON 是固定压测维度 D1–D8,性质不同)。
- **2026-08-07 撤销**:方案 R 已放弃(ADR-0011),上述路径配置化(`<根>` / `<落盘根>`)已撤销,PROCESSING-RULES / SKILL / QUESTIONNAIRE-FORMAT / GRILL-SKELETON 落盘路径回归硬编码 `harness/`(四 skill 同步)。本节作为历史叙述保留。

## dogfood 教训:✍️ 自定义行反复遗漏(2026-08-08,grill-doctor-harness 压测)

> 缺口:FORMAT 规则 4「✍️自定义每题必有」是散文规则,**无出题后强制自检**,导致出题 agent 两次遗漏(design-Q vision W01 + grill-Q doctor-harness W01,均 10 题全漏 ✍️ 自定义行)。用户两次指出。
> 回修:① 四副本 FORMAT 规则 4 加「出题后自检」(grep 🤔 数 == ✍️ 数);② grill-Q SKILL.md 第 2 步加「出题自检(强制)」子条,给可执行命令。机制回归可脚本化(FORMAT 规则 12「Markdown 排版」同源的「可检查 DoD」思路)。
> 四副本同步(OD-8 重访触发①)。双向门,可回退。

## 引擎同步记录(2026-08-18,first-principles W01 补充声明)

- QUESTIONNAIRE-FORMAT **规则 4 修正**:「✍️ 自定义」位置由「紧跟 🤔 逃生舱之后」改为「紧跟所有选项(含 ★推荐)之后、固定为题目最后一位」——消除与规则 13(选项排序:推荐居末)的顺序矛盾;该矛盾是「✍️ 行结构性遗漏」的根源(grill-Q first-principles W01 曾 10 题全漏,靠出题自检 grep 抓回)。
- grill-Q / retro-Q 的模板示例同步更新为规则 13 选项顺序(★推荐从 A 位移至 🤔 之后的 C 位,✍️ 行标注「题目最后一位」);design-Q / action-Q 模板本已合规,仅规则 4 措辞统一。
- 四副本 × 双侧(repo `skills/` + 全局 `~/.claude/skills/`)同批同步,无新有意分叉(OD-8/OD-11 边界不变)。

## 引擎有意分叉声明(2026-08-19,grill 边界深钻;OD-8/OD-11 治理)

- **❌ 跑偏标注(本副本专属,四副本不同步)**:QUESTIONNAIRE-FORMAT 规则 15 + 模板/填写规则/规则 4 自检/规则 13 排序 + PROCESSING-RULES ❌ 解析行与「≥2 停波回炉」+ 处理报告「质量信号」节——仅 grill-Q 副本持有,design-Q / retro-Q / action-Q 三副本不加。**声明为设计(非遗漏)**。理由:「框架跑偏」是压测场景特有失败模式(AI 出题者对工件的理解框架错误,整卷在错误框架内自洽);design-Q 对应物 = preview 留空、action-Q = confirm-list 纠正、retro-Q = 四节自由书写,无需同构行。
- **同批 skill 层机制(非引擎副本)**:SKILL.md 第 0 步族间自检(批量 vs 单点)+ 第 1 步末入口校准闸门(轻量模式豁免)+ 第 4 步阻塞性逃生舱分流(转 with-docs 深钻,人拍板)+ 处理报告质量信号要求;grill-with-docs 侧反向相变条款(发现批量性 → 提议转 grill-Q)。
- **来源**:grill-with-docs「grill 家族边界与跑偏治理」深钻(2026-08-19,四分支裁决:认知状态三态接线 / 入口+中途双检测 / 校准闸门+题级标注双件 / 优化回路 [OD-26](../../docs/OPEN-DECISIONS.md) provisional),用户授权「包一全授权」执行;canonical 层(哲学 §3.1 路由表加行 + 方法论 §4.1↔§4.3 接线)走 grill-Q 复压批次,见 TODO「grill 边界与跑偏治理修订包」。
- **关联**:[ADR-0023](../../harness/adr/0023-skill-md-layered-slimming.md)(同类归因 ≥2 次升格收口)、CONTEXT「Grill 家族 · 认知状态三态」。
- **顺手修复(同批)**:本文件尾部字面残留 `\n` 已清除;FORMAT / PROCESSING-RULES 头部「共三份」陈旧表述更正为四份(action-Q 早已是第四副本,OD-11)。