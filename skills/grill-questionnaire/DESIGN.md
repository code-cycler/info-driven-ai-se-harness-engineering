# grill-questionnaire · 设计文档

> 本 skill 的设计决策记录(定位 / 设计决策 G1–G8 + D22–D23 / 已知限制);治理历史(创建起源/引擎同步/分叉裁决时间线)见 [CHANGELOG.md](./CHANGELOG.md);有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。
> 本 skill 的决策进本文件;**不污染宿主项目的 CONTEXT/ADR/OD**——skill 自身的设计与宿主项目正交。
> 元注:本 skill 是用一问一答的 grill-with-docs 设计的,而它本身正是为了把 grill 的一问一答改为批量问卷。设计它用的工具,正是它要替代的工具。

## 动机与范围

grill / grill-with-docs 的压测用途(找漏洞、找盲点、找单向门、降风险)至今仍是一问一答,每问等一轮 LLM 输出。design-questionnaire 与 retro-questionnaire 已把「生成式设计」和「事后复盘」改成了批量问卷,但**事前压测**这一用途还卡在一问一答。grill-questionnaire 补这个缺口:把 grill 的压测用途改成多波次问卷。

**原初设计原则**(作者陈述,补记时间线见 CHANGELOG):设计前提 = 对抗幻觉;核心原则 = **80/20 判断成本原则**——批量问卷以 20% 时间高速处理 80% 可预知的基础问题(D1–D8 本质是已知攻击面的知识沉淀),依赖链深、需即时反馈的 20% 关键问题转 grill-with-docs 一问一答深钻,人投 80% 时间;目的 = 减少人的判断成本;定位 = design 系列流程的 review 步。谱系:本 skill 是 grill-with-docs 的问卷化演进。

- **做**:压测一份已有工件(计划 / 决策 / 架构提案 / ADR 草稿 / 设计文档),批量问卷式找漏洞、盲点、单向门;发现按类型落盘。
- **不做**:从零生成设计(design-questionnaire 管);事后复盘(retro-questionnaire 管);实现期单点深钻(grill-with-docs 管)。

**术语 · 工件 (artifact)**:压测对象。一份已有的、承载决策内容的文档,区别于 design-Q 正在生成的「草稿」。

## 关键决策记录(G1–G8 · 创建期)

| # | 决策 | 结论 | 理由 / 被否决项 |
|---|---|---|---|
| G1 | 核心定位 | 压测已有工件(对抗式,无固定骨架,工件驱动出题) | design-Q 的分工表已把「计划评审」划给 grill,缺口真实。否决「也含未成形念头」(与 design-Q feature 模式边界模糊) |
| G2 | 代码库绑定 | 绑定为默认;无项目上下文时降级为纯逻辑压测,产出审阅报告入 `~/notes/` | 压测最值钱的是「工件与现实的矛盾」,必须绑代码库;一个 skill 行为随上下文自适应 |
| G3 | 出题模型 | 混合:固定压测维度(D1–D8)+ 工件驱动具体化 + 探索盲点 | 固定维度保证覆盖通用攻击面;工件驱动保证题目具体。否决「纯工件驱动无固定维度」 |
| G4 | 工件修订 | 只产出发现,不替改工件文件 | 发现分两类:工件漏洞 → 处理报告(人决定);可沉淀项 → 即时写 CONTEXT/ADR/OD。守住「AI 不替人决策」 |
| G5 | 触发 | 手动为主 + design-Q 收尾后主动提议一次 | 不做「任何不可逆实现前」的泛化主动提议(太吵且难判定) |
| G6 | 波次与终止 | 单次完整压测 + 按需补波;终止 = 8 维度全覆盖 + 关键声明逐条审视 + 盲点清零 + 逃生舱进 OD | 工件有限,一轮套完;否决 design-Q 式多波循环(易注水) |
| G7 | 引擎复用 | 沿用 D18:复制两份 + 四方 drift 声明,design-Q 为 canonical | 否决「重构共享引擎目录」(跨 skill 相对引用断裂风险)。双向门 |
| G8 | 文件结构 | SKILL.md + GRILL-SKELETON.md(独立成文)+ 引擎副本两份 + DESIGN.md;问卷 `harness/questionnaires/grill-<slug>-w<NN>.md` | 与家族一致,骨架独立成文。否决「骨架内联进 SKILL.md」 |

## 关键决策记录(D22–D23 · dogfood 修订,自压测 DESIGN.md)

用 grill-Q 压测自己的 DESIGN.md(8 维度套 G1–G8)。问卷归档于 [grill-own-design-w01.md](./docs/questionnaires/archive/grill-own-design-w01.md)。

| # | 决策 | 结论 |
|---|---|---|
| D22 | dogfood Q1–Q8 修订 | 接受推荐:Q1(design-Q 收尾加提议 hook)、Q4(修订建议按严重度排序)、Q5(超大工件分块)、Q6(安全由 D1/D4/D5 交叉覆盖)、Q7(定义「关键声明」)。否决推荐:Q3(维度集不记被否决划分法)、Q8(主动提议不收窄)——conscious choice,记此防再问 |
| D23 | 逃生舱 family-wide 进 OD(引擎修改) | 双向门逃生舱由「采用推荐项,不进 OD」改为「采用推荐项 + 进 OD 标注(双向门/provisional/重访触发)」。四方同步无漂移 |

## 压测维度(grill 骨架,详见 GRILL-SKELETON.md)

固定维度 = 通用压测攻击面清单;每维度下的题结合工件具体化(不得照抄维度名);探索盲点补充。

**两模式通用**:D1 未言明假设 / D2 单向门·可逆性 / D3 替代方案·被否决项 / D4 失败模式·爆炸半径 / D5 盲点 / D6 可验证性
**仅代码库绑定模式**:D7 与现实的矛盾(压测最值钱的一项)/ D8 术语一致性

## 问卷格式核心(详见 QUESTIONNAIRE-FORMAT.md · 引擎副本)

- frontmatter:mode / wave / stage(此处 stage 固定 `grill`)/ created / status
- 每题:选项数不限 + ★推荐 + 🤔 逃生舱 + ❌ 跑偏标注(本副本专属)+ ✍️ 自定义 + [落盘:] 提示
- 浅分支内联限 1 层;题量每波上限 10,超量拆子波;≤3 题走 AskUserQuestion(小波阈值)

## 落盘映射(详见 PROCESSING-RULES.md · 引擎副本 + GRILL-SKELETON.md 维度落盘)

- 工件漏洞/盲点/单向门/缺失替代方案 → **处理报告(对话内)**,人决定是否修订工件
- 难逆转+会困惑+真权衡 → harness/adr/;其余单向门/重大风险/存疑假设 → OPEN-DECISIONS.md(归属见 HARNESS-RULES.md 第六节)
- 术语冲突 → CONTEXT.md;纯逻辑模式 → 审阅报告入 `~/notes/`

## 验收标准(DoD)

- [x] 5 文件齐全:SKILL.md / GRILL-SKELETON.md / QUESTIONNAIRE-FORMAT.md(副本)/ PROCESSING-RULES.md(副本)/ DESIGN.md
- [x] GRILL-SKELETON.md 含 D1–D8 维度 + 出题方向 + 落盘映射 + 两模式说明
- [x] 引擎副本含四方 drift 标记注释
- [x] 全局 CLAUDE.md 与宿主项目 CLAUDE.md(+ AGENTS.md 同步)家族表加 grill-questionnaire 行
- [x] dogfood:自压测 DESIGN.md(grill-own-design-w01 归档),抓出 8 缺口 + 1 补充声明,修订见 D22/D23

## 已知风险

| 风险 | 缓解 |
|---|---|
| 维度形式主义(题目空泛、照抄维度名) | 引擎规则 7:探索发现的题必须附出题依据与出处 |
| 压测发现无人修订工件 | 处理报告标「工件修订建议」;第 5 步收尾**主动询问**是否执行修订(参照 grill-with-docs 主动决策风格),用户授权后才执行 |
| 与 design-Q feature 模式混淆 | G1 边界:design-Q 生成式(从零、固定骨架),grill-Q 对抗式(已有工件、无骨架) |
| 四副本引擎漂移 | G7 四方 drift 声明 + 副本头部标记;引擎极少改 |
| 降级模式(纯逻辑)力度弱 | D7/D8 失效时明确告知「未对照代码库,建议有项目上下文时复压」 |
| 框架级理解跑偏(整卷在错误框架内自洽) | 入口校准闸门(轻量豁免)+ ❌ 题级跑偏标注(FORMAT 规则 15)+ 同波 ≥2 题被标 → 停波回炉;跨波优化走质量信号节 → retro 聚合 → ADR-0023 升格(OD-26 provisional) |
| 绿地项目(有 docs 无代码)D7 误判为无效 | GRILL-SKELETON D7 + SKILL 模式判定补「绿地子模式」:D7 的「现实」转为既有设计文档/ADR/约束(绿地模式 D7 抓出既有 ADR 与 LLD 选型不一致有实证) |
