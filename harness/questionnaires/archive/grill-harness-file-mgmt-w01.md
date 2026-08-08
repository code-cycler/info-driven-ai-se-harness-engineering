---
stage: grill
wave: 1
created: 2026-08-08
status: archived
---
# 压测问卷 · skill 家族 harness 文件管理规格 W01

> **工件**:skill 家族的「harness 文件管理规格」——各 skill SKILL.md 的落盘路径句 + [ADR-0011](../../adr/0011-abandon-plan-r-hardcode-harness.md)(硬编码 `harness/`)+ 各 DESIGN.md 相关决策(design-Q D11/D23、skill-spec-revamp LLD 2.6 落盘根边界)。
> **模式**:代码库绑定(本仓库有 CONTEXT/ADR/docs 体系)。D7「现实」= 仓库实际文件组织(`harness/` 现状)+ 既有决策(ADR-0011 / ADR-0009 三区模型/OD-8)。
> **触发**:用户指出「当前 skill 做的 harness 文件管理比较简单,没有考虑实际情况——层次化设计、feature 级别或子项目没有单独文件夹、边缘场景与实际工程场景」。
>
> **工件关键声明清单**(压测对象,每条应被 ≥1 维度审视):
>
> - **S1 落盘根**:4 问卷 skill + long-running 落盘路径**硬编码** `项目根/harness/`(ADR-0011 决策 1),含 design/ + questionnaires/ + adr/ 三件。
> - **S2 问卷命名**:init `<stage>-w<NN>.md`;feature `feature-<slug>-<stage>-w<NN>.md`;grill `grill-<slug>-w<NN>.md`;retro `retro-<主题>-w<NN>.md`;confirm `confirm-<slug>-w00.md`——全部平铺 `harness/questionnaires/`。
> - **S3 设计文档**:VISION/HLD/LLD → `harness/design/`(SKILL.md 只此一句,无子目录规则)。
> - **S4 ADR**:`harness/adr/NNNN-<slug>.md`,编号顺延。
> - **S5 归档**:`harness/questionnaires/archive/`,文件名不变,只移不删。
> - **S6 项目固有**:CONTEXT.md / OPEN-DECISIONS.md / TODO.md / docs·retro/ 维持三区模型项目固有位置(ADR-0011 决策 3)。
> - **S7 long-running**:从 `harness/questionnaires/archive/` 归档问卷 + `.claude/feature_list.json` + `.claude/claude-progress.txt` 重建上下文。
>
> **填写规则**:
>
> 1. 每题勾选 `[x]`;★ = AI 判断(认定/不认定漏洞);opt-in 关不预勾
> 2. 🤔 逃生舱:勾了 = 定不了 → 降风险协议
> 3. ✍️ 自定义(尤其"不认定"时给理由、"部分认定"时给修订方向)
> 4. 排序:非推荐在前 → 🤔 倒数第二 → 推荐最后

## Q1. (D1 未言明假设) 落盘根单一 `项目根/harness/`——假设每个项目只有一个根    [落盘: 处理报告]

<出题依据:ADR-0011 决策 1 硬编码 `项目根/harness/`。隐含假设:项目 = 单一根目录,所有 AI 流程产物归这一个根。实际工程场景:monorepo / 多子项目仓库(如 `~/code/城市低空无人机仿真评估平台/` 下多个子模块)、嵌套项目(项目内嵌独立 git 仓库)、或作者在 `~/` 下多个并列项目共享同一套 skill —— 此时「项目根」指哪一层?子模块的 feature 设计是否也与主项目混在同一个 harness/?>

- [ ]  A. 认定漏洞 —— skill 无「子项目 / 模块 / 嵌套仓库」的 harness 归属规则,多根场景落哪一个根全靠 agent 临场判断,易误落
- [ ]  B. 不认定 —— 个人开发者单仓库场景,子项目各自独立仓库,harness 随各自根走即可,无需规格化
- [ ]  🤔 我定不了 → 推迟/降风险
- [X]  C. 部分认定 ★推荐 —— 单根假设对「个人单仓库」成立,但「多子项目仓库 + 共享 skill」是真实场景;至少补一条「harness 归属判据」(如:子模块有自己的 CLAUDE.md/git → 子模块根自行 harness;无 → 归主根),不必全自动化

## Q2. (D5 盲点) design/ 无 feature 聚合目录——多个 feature 并行时设计文档如何处理   [落盘: 处理报告]

<出题依据:S3 规格只写「VISION/HLD/LLD → `harness/design/`」。仓库现状已出现两种形态并存:`repo/`、`skill-spec-revamp/`、`feature-skills-harness-consistency/` 是子目录,而 `VISION.md`(methodology_v3)、`hld_v2.md`、`lld_v2.md`、`hld-methodology-separation.md` 裸放在根下。**规格未定义何时用子目录、何时裸放**——现状态依赖人工约定,无规则可循。>

- [X]  A. 认定漏洞 —— 规格缺失层次化规则,现状已混用(sub 目录 vs 裸放),新会话 agent 无法从规格判断新 feature 该建目录还是裸放
- [ ]  B. 不认定 —— design/ 根下文件少,裸放也能找;子目录是历史偶然,不必规格化
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 至少定义分层规则:feature 级设计(多文件、可独立引用)建 `design/<feature-slug>/`;全局/单文件设计(如 methodology 修订)裸放根下;判定句如「该设计是否会被独立引用/与其它 feature 冲突」

## Q3. (D5 盲点) feature 级产出的三块碎片——design/ 与 questionnaires/ 与 adr/ 不按 feature 聚合   [落盘: 处理报告]

<出题依据:S2/S3/S4 三个目录各自平铺。一个 feature(如 skill-spec-revamp)的产物散落:设计文档在 `design/skill-spec-revamp/`、问卷在 `questionnaires/feature-skill-spec-revamp-*.md`、ADR 在 `adr/0011-*.md`。回读「这个 feature 到底设计过什么、有哪些决策」需跨三目录拼装,无聚合入口。>

- [X]  A. 认定漏洞 —— 跨目录碎片化,feature 级回读/审计成本高,无「feature 产物清单」式索引
- [ ]  B. 不认定 —— 文件名 slug 已含 feature 标识,`find` 一下即可聚合,不值得为聚合引入目录结构
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 不必物理聚合(动目录高风险),但可补轻量索引:design/<feature></feature>/ 下放 README 或 INDEX 列出该 feature 的问卷(含归档)与 ADR;或 CONTEXT/harness README 维护「feature → 产物」映射

## Q4. (D1 未言明假设) 问卷命名 slug 唯一性——两个 feature 用相近 slug 时冲突与混淆   [落盘: 处理报告]

<出题依据:S2 命名 `feature-<slug>-<stage>-w<NN>.md`,slug 为「功能短名 kebab-case」。现状册账:仓库已有 `feature-methodology-*`(4 份)、`feature-repo-*`(5 份)、`feature-skill-*`(6 份)、`feature-skills-*`(1 份)并存——`feature-skill-*` 与 `feature-skills-*` 前缀几乎相同;`grill-methodology-*` 与 `feature-methodology-*` 同 feature 不同 skill 类型。slug 无规范化、无冲突检测,近似 slug 会混淆(读错文件)、编号 w<NN></nn> 无全局唯一保证。>

- [X]  A. 认定漏洞 —— slug 无定义(取词规则、去重、长度上限),近似 slug 已实际存在,回读会串
- [ ]  B. 不认定 —— 文件名 + 时间戳足够区分,混淆是低概率事件,不值得加规则
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 至少定义 slug 规范(来源 = feature 名 / 主题名,去重原则,禁通用词如 skill/design),并在生成问卷时自查同 prefix 已有文件

## Q5. (D4 失败模式) 归档只增不整理——archive/ 平铺膨胀后的检索与重载   [落盘: 处理报告]

<出题依据:S5 归档「只移不删,文件名不变」。现状 archive/ 已 30+ 文件平铺,按 confirm/feature/grill 前缀区分。长期项目(数月)后卷数×波次叠加,retro/confirm/grill 混杂;long-running(S7)从 archive/ 重建上下文时,如何定位「本 feature 的问卷」?归档无 README、无 feature 聚合、无日期分层。>

- [X]  A. 认定漏洞 —— 归档无限平铺,检索成本随项目生命周期线性增长,无归档组织规则
- [ ]  B. 不认定 —— 归档是「原始信息不丢失」的留痕区,检索靠 grep/find,个人项目规模可承受
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 归档保持「原始信息不丢失」铁律(不删不重排),但补轻量组织:按 feature/主题建 `archive/<feature>/` 子目录(仍只移不删),或归档 README 索引;重载路径(skill 读归档)相应更新

## Q6. (D2 单向门 / 可逆性) 引入层次化结构(如 feature 子目录)的可逆性与迁移成本   [落盘: 处理报告]

<出题依据:若 Q2–Q5 认定要引入 harness 分层(design/<feature></feature>/、archive/<feature></feature>/、adr 分组),这是对既有目录结构的**重组**。仓库现状的裸放文件 + 子目录共存,迁移涉及:已有归档问卷的相对链接(问卷尾部追加的处理报告摘要里大量 `../design/...`、`../adr/...` 相对链接)、skill 规格字符串、long-running 读取路径。重组可逆但迁移成本真实。>

- [X]  A. 认定单向门风险 —— 迁移会破坏既有相对链接与 skill 路径字符串,需一次性迁移 + 断链回归,中途退出会留下半迁移状态
- [ ]  B. 不认定 —— 纯目录移动 + git 可回退,链接重算有先例(2026-08-05 harness 迁移做过),双向门
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 分层若做,须一次性完整迁移(挪文件 + 重算链接 + skill 规格同步 + 断链回归),作为独立行动项带 DoD,不渐进半途;或先只对新 feature 生效、旧文件不动(混合态,声明清楚)

## Q7. (D3 替代方案) 层次化 vs 平铺计数器——被否决项缺失   [落盘: 处理报告]

<出题依据:ADR-0011 决策「硬编码 `harness/`」只权衡了「配置化 vs 硬编码」,**未权衡 harness 内部的组织形态**(平铺 vs 分层 vs 索引)。S2–S5 的平铺组织(全部文件名前缀区分)是继承自安装初版,无「当时还考虑过 feature 子目录 / 按 skill 分目录 / 带索引」的决策记录。>

- [X]  A. 认定漏洞 —— 平铺是默认继承而非权衡结果,组织形态无决策记录,后续演进无依据
- [ ]  B. 不认定 —— 组织形态是「怎么放」的次要问题,不达 ADR 门槛,现状够用无需回溯
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 本次压测即补上权衡:若结论要改组织,记一条 DESIGN.md/ADR 级决策(平铺 vs 分层的利弊 + 被否决项),否则维持平铺并声明「组织形态维持平铺系有意为之」

## Q8. (D4 失败模式) 多项目 / 多子项目并行时 harness 混淆   [落盘: 处理报告]

<出题依据:S1 硬编码 `项目根/harness/`。工程场景:作者在 `~/code/` 下多个项目同时活跃,每个项目跑 design-Q/grill-Q 产出各自 harness/。若某次会话工作目录错位(如从 `~/` 启动而非项目根)、或子项目嵌套,问卷/ADR 会写入错的 harness/,且无「归属校验」。>

- [ ]  A. 认定漏洞 —— 无「当前 harness 归属」校验,工作目录错位即误落,污染他项目 harness;混淆无提示
- [ ]  B. 不认定 —— 会话从项目根启动是基本纪律,误落属操作失误非规格缺口
- [ ]  🤔 我定不了 → 推迟/降风险
- [X]  C. 部分认定 ★推荐 —— 落盘前轻量校验(pwd 是否在含 harness/ 的项目根,或 frontmatter 记 created 项目名),一次确认防误落;不引入运行时配置化(不违背 ADR-0011)

## Q9. (D5 盲点) 子项目有自己的逻辑边界——「子项目不共用 harness」的判定缺失   [落盘: 处理报告]

<出题依据:用户触发原话「feature 级别或子项目没有单独文件夹」。S1 只有「项目根」一个层级。工程场景:一个仓库内含多个子项目(每个有自己的 README/CLAUDE.md/独立功能),它们的设计产物应各自独立(子项目 A 的 feature 与子项目 B 的 feature 不应混在同一个 design/、同一个 archive/)。现规格无「何时子项目独立 harness、何时归主 harness」的判据。>

- [ ]  A. 认定漏洞 —— 无子项目 harness 边界判据,多子项目仓库的 AI 产物必然混流,回读/归档无法按子项目切分
- [ ]  B. 不认定 —— 子项目若够大应独立成仓库,单仓库内多子项目是少数场景,不值得规格化
- [ ]  🤔 我定不了 → 推迟/降风险
- [X]  C. 部分认定 ★推荐 —— 补一条判据:子模块有独立 CLAUDE.md / 独立 git / 独立发布边界 → 子模块根建自己的 harness/;否则归主根。与 Q1 合并为「harness 归属判据」统一治理

## Q10. (D5 盲点) long-running 与 harness 的衔接——feature_list 与 harness 产物无关联   [落盘: 处理报告]

<出题依据:S7 long-running 读 `harness/questionnaires/archive/` 归档问卷 + `.claude/feature_list.json` 重建。但 feature_list.json 在 `.claude/`(项目固有),harness 产物在 `harness/`——两者无交叉引用:feature_list 的 feature 不链接到对应设计文档/问卷,设计文档也不标注「已进 feature_list F00X」。实现期回看「这个 feature 的设计在哪」需人工映射。>

- [ ]  A. 认定漏洞 —— 设计产物与实现跟踪(design ↔ feature_list)断裂,feature 级设计完成后进实现的衔接无记录
- [ ]  B. 不认定 —— feature_list 是轻量进度表,与设计文档的映射靠文件名/记忆即可,不必强耦合
- [ ]  🤔 我定不了 → 推迟/降风险
- [X]  C. 部分认定 ★推荐 —— 低耦合补强:feature_list.json 的 feature 条目加 `designRef` 字段写设计文档路径,或 LLD 阶段拆分标注对应 feature_list 项;一次性落盘,不引入运行时读取

## Q11. (D7 与现实矛盾) 规格「阶段文档 → design/」vs 现状「子目录 + 裸放共存」   [落盘: 处理报告]

<出题依据:规格 S3 只写「VISION/HLD/LLD → `harness/design/`」,但仓库现状的 design/ 已是混合态:`repo/`、`skill-spec-revamp/`、`feature-skills-harness-consistency/` 子目录与 `VISION.md`、`hld_v2.md` 裸放并存。**规格与现状不一致**——规格未声明子目录机制,现状却用了;新 agent 读规格会以为全部裸放,实际需遵循潜在(未写明的)子目录约定。>

- [ ]  A. 认定漏洞 —— 规格 vs 现状脱节,规格无子目录规则但现状已用,新会话会按规格裸放而违反现状约定
- [ ]  B. 不认定 —— 现状子目录是历史偶然,规格应回灌成「裸放为默认」,现有子目录保留即可,无需改规格
- [ ]  🤔 我定不了 → 推迟/降风险
- [X]  C. 部分认定 ★推荐 —— 二选一(规格回灌现状 = 定义子目录规则、或现状回灌规格 = 声明裸放 + 子目录为特例),须显式定案消除脱节,不能继续无声共存

## Q12. (D8 术语一致性) 「harness 区」「项目固有」「落盘根」三术语的执行边界   [落盘: CONTEXT.md]

<出题依据:三区模型(ADR-0009)定义「harness 区 = AI 流程产物,与项目文件 docs/ 物理分离」。但术语使用在规格中不统一:CLAUDE.md 用「harness 区」「落盘路径速查」;ADR-0011 用「落盘根边界设计/问卷/adr 三件」;skill-spec-revamp LLD 2.6 定义「落盘根边界 = 通用三件 design/ + questionnaires/ + adr/」;SKILL.md 出现「项目固有文件,路径不动」。**「项目固有」的边界**:CONTEXT/OPEN-DECISIONS/TODO/docs·retro 是项目固有(S6),但 `.claude/feature_list.json`、`delegation.md`、`docs/retro/` 分落三处——「项目固有 vs harness 区」的执行判定规则无单一权威。>

- [X]  A. 认定冲突 —— 「harness 区 / 项目固有 / 落盘根」三词在 CLAUDE.md / ADR / SKILL.md 中边界表述不一,执行时判据不明
- [ ]  B. 不认定 —— 三词各有所指(物理区 / 归属 / 前缀),CLAUDE.md 已给出落盘速查表,够用
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 在 CONTEXT 补一条执行判定规则(放 harness 还是项目固有:AI 流程产物 vs 项目自身的文档/跟踪;一条判据句),不重写既有措辞

## Q13. (D5 盲点) 跨 feature 交叉引用的相对链接——分层后链接失效   [落盘: 处理报告]

<出题依据:若 Q2–Q5 认定引入 feature 子目录,design/ 内文档的相对链接(如 `hld_v2.md` 引用 `../../adr/0004-*.md`)层级会变;问卷尾部的处理报告摘要里大量 `../design/...`、`../adr/...` 相对链接也会失效。现状已存在跨目录引用(design ↔ adr ↔ questionnaires/archive),分层迁移必须重算。>

- [ ]  A. 认定漏洞 —— 分层方案的链接失效范围未评估,迁移会破坏既有引用(有 2026-08-05 迁移先例,曾 96 断链)
- [ ]  B. 不认定 —— 若保持现状不平铺改动,无链接问题;分层只是假设场景
- [ ]  🤔 我定不了 → 推迟/降风险
- [X]  C. 部分认定 ★推荐 —— 分层若做,迁移 DoD 必须含「相对链接重算 + 断链回归(参照 harness 迁移先例)」;若不做分层,本问题不存在,标注即弃

## Q14. (D6 可验证性) harness 组织规则可检查吗——有无「布局合规」DoD   [落盘: 处理报告]

<出题依据:S2–S5 的命名/归档规则无校验手段:问卷命名是否符合 `feature-<slug>-<stage>-w<NN>`、归档是否在 archive/、ADR 编号是否顺延——全靠 agent 自觉,无脚本化检查(对照脱敏门有 `desensitize.py`,harness 组织无对应检查)。>

- [X]  A. 认定漏洞 —— 组织规则有约束无校验,违反(如命名拼错、ADR 跳号)无声发生,无回归保障
- [ ]  B. 不认定 —— 组织规则是「怎么放」的软约定,agent 自觉 + git diff 可见,不值得脚本检查
- [ ]  🤔 我定不了 → 推迟/降风险
- [ ]  C. 部分认定 ★推荐 —— 轻量校验:一次性脚本检查 harness 布局(命名正则 / ADR 编号连续 / 归档位置),发布前或定期跑,不进每次流程

## 补充声明

> **用户作答(2026-08-08,对话内补充声明,逐字转写)**:
> 「当前问卷偏长,将单波次上限调整为10个,直接问答上限调整为不多于3个；针对harness工程一直进化的现状,有必要设计一个doctor-for-harness skill,处理演进过程中文件迁移、各类规范等问题；harness文件严格放入harness父级文件夹,在父级文件夹下建立子文件夹,不污染项目目录结构」
>
> 解析:① 格式反馈(单波次上限 10 / 直接问答上限 3);② 新需求(doctor-for-harness skill);③ 核心裁决(harness 文件严格归 harness/ 父级 + 内部子文件夹分层,不污染项目根)。用户未逐题勾选,以补充声明定向 + 委托。

---

## 处理报告摘要(2026-08-08 · grill W01 → archived)

- **作答方式**:用户未逐题勾选,以**补充声明定向**(三裁决)+ 委托 doctor-for-harness 承载细节——14 题不逐题判定,统一按用户裁决落向。
- **用户三条裁决**:
  1. **格式反馈**:单波次上限收紧到 10(原 10–15);直接问答(小波阈值)上限 ≤3;
  2. **新需求**:设计 doctor-for-harness skill,处理 harness 演进中的文件迁移与规范;
  3. **核心裁决**:harness 文件**严格**归 `harness/` 父级 + 父级下子文件夹分层,不污染项目根。
- **落盘**:
  - **OD-15**(新立项):doctor-for-harness skill——harness 演进治理(组织规则权威化 / 迁移工具 + 断链回归 / 布局校验 / 演进留痕)→ [OPEN-DECISIONS.md](../../../docs/OPEN-DECISIONS.md)
  - **TODO 🟤 节**:doctor-for-harness 立项 + harness 分层落地 + 格式反馈落地(→ [TODO.md](../../../TODO.md))
  - **0 ADR**(分层=目录组织,双向门可逆;难逆转性不足 ADR 三条件)/ **0 CONTEXT**(无新术语冲突——「harness 父级」沿用既有词)
- **grill-Q 铁律守**:只产出发现 + 用户裁决,未替改工件;harness 分层/doctor-for-harness 落地由人授权发起
- **覆盖度**:D1–D8 全开;工件关键声明(S1–S7)均被 14 题覆盖,用户裁决统一收束至「分层 + 立项」方向当前问卷偏长，将单波次上限调整为10个，直接问答上限调整为不多于3个；针对harness工程一直进化的现状，有必要设计一个doctor-for-harness skill，处理演进过程中文件迁移、各类规范等问题；harness文件严格放入harness父级文件夹，在父级文件夹下建立子文件夹，不污染项目目录结构
