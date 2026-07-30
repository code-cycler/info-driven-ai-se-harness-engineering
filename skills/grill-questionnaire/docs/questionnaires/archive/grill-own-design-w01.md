---
mode: init
wave: 1
stage: grill
created: 2026-07-24
status: archived
---
# 问卷 grill W01 · 自压测 grill-questionnaire 的 DESIGN.md(dogfood)

> 工件:[../../DESIGN.md](../../DESIGN.md)(grill-Q 自己的设计决策记录)
> 用 grill-Q 压测它自己的设计——8 维度套到 G1–G8 + 维度集 + DoD 上。一个「压测已有工件」的 skill 压测自己的设计,是最直接的自检。
>
> 填写规则:
>
> 1. 每题勾选 `[x]`;默认单选,选项数不限
> 2. ★ = 推荐选项,附推荐理由
> 3. 每题末尾 🤔 是逃生舱:勾了 = 我定不了 → agent 走降风险协议,绝不重问
> 4. 选项都不合适 → 在 ✍️ 自定义 后自由书写
> 5. 所有题都是 dogfood 发现的「工件修订建议」,落盘 = 处理报告 + 你批准后我回修 grill-Q 的规格文件(DESIGN.md / SKILL.md / GRILL-SKELETON.md / PROCESSING-RULES.md)

## Q1. [D7 与现实矛盾 · 最重大] G5 依赖 design-Q 收尾主动提议 grill-Q,但 design-Q SKILL.md 收尾步没有这个 hook,闭环是断的。补不补?   [落盘: design-questionnaire/SKILL.md 收尾步 + 本 skill DESIGN.md D22]

出题依据:核实 design-Q [SKILL.md](file://~/.claude/skills/design-questionnaire/SKILL.md) 收尾步——只输出清单 + 提醒进实现 + 可选 dogfood,**无任何提及 grill-questionnaire 的 hook**。G5 的「主动提议」在 grill-Q 这边声明了,但触发方 design-Q 不知道它存在 → 闭环断点。

- [X]  A. 补 hook  ★推荐 —— design-Q SKILL.md 收尾步(dogfood 选项之后)加「可选:提议 grill-questionnaire 压测刚产出的设计」(AskUserQuestion,用户可拒)。闭环才真打通;与 G5 一致。
- [ ]  B. 不补 —— G5 只在 grill-Q 这边声明,design-Q 不动。代价:主动触发形同虚设,实际只能靠用户手动记起「该压测了」。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q2. [D7 同源] Q1 若补 hook,要不要同步进 项目A CLAUDE.md / AGENTS.md 的「场景分工」(那里目前只写了 grill-Q 存在,没写 design-Q 收尾会提议)?   [落盘: 项目A CLAUDE.md + AGENTS.md 场景分工段]

出题依据:全局 CLAUDE.md 家族表写了「design-Q 收尾后主动接上 write→review 闭环」,但 项目A 两处只写了 grill-Q 存在,没写触发衔接。三处描述粒度不一。

- [X]  A. 同步补一句  ★推荐 —— 项目A 场景分工段补「design-questionnaire 收尾后接上 grill-questionnaire」(全局表已这么说,对齐即可)。
- [ ]  B. 不补 —— 项目A 不必这么细,全局表说了就行。代价:三处粒度不一,未来可能漂移。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q3. [D3 替代方案] 维度集 D1–D8 没有记录「为何这样划分 / 被否决的划分法」(如时间轴划分、STPA/FTA)。grill-Q 自己 D3 要求工件记被否决项,自己却没记。补不补?   [落盘: GRILL-SKELETON.md 维度集来源注]

出题依据:D3 压测别人工件时会问「关键决策是否给了被否决项」,而维度集本身是个关键决策,GRILL-SKELETON 只写了「维度可增减」,没写「为何是这 8 个、否决了什么」。自洽缺口。

- [ ]  A. 补记被否决划分法  ★推荐 —— GRILL-SKELETON 维度集注补「采用『决策攻击面』划分;被否决:时间轴划分(事前/事中/事后,不通用)、STPA/FTA(过重,非问卷能承载)」。满足 D3 自洽。
- [X]  B. 不补 —— 维度集是实践提炼,记替代是过度。代价:D3 自相矛盾(要求别人记,自己不记)。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q4. [D4 失败模式] 压测大工件可能产出几十条修订建议,处理报告当前无优先级,用户易淹没。加排序吗?   [落盘: PROCESSING-RULES.md 处理报告模板 + GRILL-SKELETON.md 落盘契约]

出题依据:D4 追问「失败模式」,大工件压测的失败模式之一就是「发现太多、用户淹没、修订建议落灰」(已知风险里提了落灰,但缓解只靠 TODO.md,没靠排序)。

- [ ]  A. 按严重度排序  ★推荐 —— 处理报告「工件修订建议」按 单向门/安全 > 逻辑漏洞 > 盲点 > 风格 排序;PROCESSING 处理报告模板 + GRILL-SKELETON 落盘契约各注一笔。
- [ ]  B. 不排序 —— 保持发现原序,排序留给用户。代价:大工件体验差,违背「用户可操作性」。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: ______仅限大问卷，不少于15个问题的问卷____

## Q5. [D4 失败模式] 超大工件(整份 HLD+LLD)如何分块未定义——子波拆分只管题量,不管工件本身的分块。补吗?   [落盘: SKILL.md 第 1 步]

出题依据:SKILL 第 2 步说「超 15 题拆子波」,但那是题量维度的拆分。工件本身若是多章节大文档,「关键声明清单」会很长,按什么分块压测未定义。

- [X]  A. 补工件分块策略  ★推荐 —— SKILL 第 1 步加「超大工件按声明组(如 HLD 章节)分块,每块独立压测,跨块矛盾单列成题」。题量与工件分块两个维度分开处理。
- [ ]  B. 不补 —— 子波拆分够用。代价:超大工件子波间依赖易乱,覆盖清单难呈现。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q6. [D5 盲点] D1–D8 无专门「安全」维度(认证/授权/加密/注入/密钥)。安全设计类工件怎么压?   [落盘: GRILL-SKELETON.md 维度集注]

出题依据:D5 追问「该说没说」。安全在 design-Q/方法论里是一等公民,grill-Q 维度集却无专门维度。选项是「声明交叉覆盖」还是「单列 D9」。

- [X]  A. 声明交叉覆盖  ★推荐 —— GRILL-SKELETON 注「安全由 D1(安全假设)+ D4(安全失败模式)+ D5(安全盲点)交叉覆盖,不单列;安全关键设计在出题依据标『需人逐行审查』」。避免维度膨胀,且安全非问卷能解。
- [ ]  B. 单列 D9 安全维度 —— 维度集加「认证/授权/加密/注入/密钥」。代价:膨胀,且给人「问卷能解决安全」的错觉。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q7. [D6 可验证性] G6 终止条件里的「工件关键声明」判据模糊——谁判断哪些算「关键声明」?   [落盘: SKILL.md 第 1 步 + GRILL-SKELETON.md 覆盖度判定]

出题依据:D6 追问「可检查还是空话」。终止条件「工件每条关键声明都被审视」里,「关键声明」无定义 → 终止条件本身不可验证(D6 自相矛盾)。

- [X]  A. 定义「关键声明」  ★推荐 —— SKILL 第 1 步明确「关键声明 = 决策点 / 假设 / 接口与约束 / 验收标准(第 1 步提取的清单);背景叙述与修辞不强制审视」。GRILL-SKELETON 覆盖度判定对齐。
- [ ]  B. 不定义 —— 留给 agent 临场判断。代价:终止条件可验证性弱,不同 agent 结果不一。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

## Q8. [D1 未言明假设] G5 假设「design-Q 收尾提议不扰民」,但坍缩为 LLD 的小项目(skill/脚本)压根没设计草稿值得压,提议无意义。要不要收窄主动提议的条件?   [落盘: grill-Q SKILL.md G5 + design-Q SKILL.md hook]

出题依据:D1 追问「未言明假设」。G5 的主动提议假设「产出了值得压测的设计」,但 design-Q 的坍缩为 LLD 场景(D19)产物是 lld,小项目 lld 压测价值低,提议成噪音。

- [ ]  A. 收窄触发条件  ★推荐 —— design-Q hook 仅在「产出了 HLD 或完整 design 草稿」时提议;坍缩为 LLD 的小项目不提议。grill-Q G5 同步注明。
- [X]  B. 不收窄 —— 一律提议,用户自己拒。代价:小项目场景噪音。
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

---

## 补充声明

<dogfood 中发现的、上面 8 题没覆盖的缺口,或任何想补充的话。没有就留空。>grill和questionnaire系列中的逃生舱一方面采用推荐项，一方面也要进OD并标注

---

## 处理报告摘要(2026-07-24 归档)

- **落盘(全部已执行)**:
  - Q1=A → design-questionnaire/SKILL.md 收尾步加「提议压测(grill-Q 衔接)」hook(Q8=B 不收窄,小项目也提议)
  - Q2=A → 项目A CLAUDE.md/AGENTS.md 衔接已在构建期写入,核对无操作
  - Q3=B → GRILL-SKELETON 不改;grill-Q DESIGN.md D22 记 conscious choice(维度集不记被否决划分法)
  - Q4=✍️(仅限 ≥15 题的大问卷) → GRILL-SKELETON 落盘契约加「修订建议排序(仅大问卷)」
  - Q5=A → grill-Q SKILL.md 第 1 步加「超大工件分块」
  - Q6=A → GRILL-SKELETON 维度集注加「安全由 D1/D4/D5 交叉覆盖,不单列」
  - Q7=A → grill-Q SKILL.md 第 1 步 + GRILL-SKELETON 覆盖度定义「关键声明 = 决策点/假设/接口约束/验收标准」
  - Q8=B → 不收窄;design-Q hook 注明 + D22 记 conscious choice
- **补充声明(全家桶引擎修改)**:双向门逃生舱 → 「采用推荐项 + 进 OD 标注」。三份 PROCESSING-RULES(design-Q / retro-Q / grill-Q)同步 + 三份 DESIGN.md drift(design-Q D22 / retro-Q 引擎声明 / grill-Q D23)
- **异常**:无(无逃生舱触发、无必答未答、无单选多勾)
- **覆盖度**:D1–D8 全部套用到 G1–G8 + 维度集 + DoD;工件关键声明逐条审视;盲点清零;无逃生舱。再无可压测的点,闭环结束。
- **修订文件清单**:design-Q(SKILL.md、PROCESSING-RULES.md、DESIGN.md)/ retro-Q(PROCESSING-RULES.md、DESIGN.md)/ grill-Q(SKILL.md、GRILL-SKELETON.md、PROCESSING-RULES.md、DESIGN.md)
