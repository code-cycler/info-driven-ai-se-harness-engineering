---
mode: feature
wave: 0
stage: L1-contract
created: 2026-08-23
status: archived
---
# 问卷 feature-i18n-support L1-contract W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的契约决策逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(默认关):全部 `[ ]`,人逐条作答;勾 `[x]` = 采纳默认按默认落盘
> - **取消勾选(留空)= 不采纳** → 该要点转入 W01 单独拷问(出选项深究)
> - **单向门要点永不预勾**;本波无 🤔(真定不了 → 取消勾选转 W01)
> - 若"大体同意但要改一两处" → 取消勾选,转 W01 时给自定义值
>
> 默认来源标注于〔〕。硬约束条目以 **(硬约束)** 标注(将写为 L2 实现的不可偏离契约)。

> **出题依据摘要**(2026-08-23,一手核实):
>
> - **L0 已决 23 条全采纳**([L0-vision-i18n-support.md](../../design/i18n-support/L0-vision-i18n-support.md)):中文 canonical + 顶级 en/ 镜像、漂移三类检出、文件级粒度、首期 = 门面 + 核心、en 不入 skills-sync-check 扫描面、独立 i18n-check.py。
> - **CONTEXT 结构实测**:纯术语表、分节组织、术语多为条目式(bullet)非表格、正文全中文(202 行)——「新增英文对照节」侵入最小;CONTEXT 现有「新词引入三条件门槛」可对齐英文侧。〔docs/CONTEXT.md 全文〕
> - **提交门现状实测**:无 CI / 无 git hook;现有门 = 手动(push 前三道门:脱敏脚本 0 命中 + 语义人审 + 脱敏报告;改 skill 任一侧后 sync-check 0 违规才提交)。i18n-check 接入 = 并入手动门,非自动化。〔CLAUDE.md 工具命令节 + OD-1〕
> - **翻译面边界张力**:L0 #4 镜像范围(对外门面)含 retro,但 L0 #20 首期面不含 retro——「可翻集」与「当前翻译义务集」需分层定义,否则 i18n-check ① 对未翻 retro 恒红。〔L0 文档自洽性分析〕
> - **skills 镜像粒度**:L0 #4/#20 定首期只翻 8 个 SKILL.md 本体;引擎文件(QUESTIONNAIRE-FORMAT / PROCESSING-RULES / STAGE-SKELETONS / 格式文件)不翻首期 → en SKILL.md 内指引擎的相对链接需定策略。〔skills/ 目录清单实测〕
> - **hash 可行性**:SHA-256 由 python3 hashlib 原生支持,无外部依赖(环境现实验证:python3 标准库,与既有三脚本同栈,无需实测编译链接)。
> - **无未验证假设**(续 L0 台账:archive 判定 + 检查器接口细节 = 本层裁决,非待验事实)。

## 决策默认值清单

### 一、镜像树布局(模块一)

- [X]  **1 en/ 映射规则与 en 文件头标记 (硬约束)**:`en/` 下文件与中文源**相对路径一一对映**(`en/docs/CONTEXT.md` ↔ `docs/CONTEXT.md`);每个 en 文件顶部 frontmatter 必带三字段:`lang: en` + `en-source: <zh 相对路径>` + `zh-hash: <源指纹>`(zh-hash 形态见 #5)。en-source 是孤儿判定与链接检查的锚。〔L0 #7 文件级 + #15 标记方向〕
- [X]  **2 README 切换入口具体形态**:根 README 标题下固定一行 `**English** · [中文](./README.md)`;`en/README.md` 顶部对应 `[English] · **中文**([返回中文 README](../README.md))`。中文为 GitHub 仓根默认,英文经链接直达。〔L0 #12 方向 + GitHub 渲染事实〕
- [X]  **3 en 根导航文件职责**:`en/README.md` 兼作英文镜像根入口,承担四职:语言切换回链 + canonical 声明(#16)+ License 说明 + 镜像树导航(分区块列出全部 en 路径);en/ 下不另建独立「目录索引」文件。〔GitHub 不渲染 en/README 为仓根,须自建入口;导览集中单点〕
- [X]  **4 en SKILL.md 内引擎链接策略**:首期只镜像 8 个 SKILL.md 本体(引擎文件不翻);en SKILL.md 中指向引擎文件 / CHANGELOG / DESIGN 的相对链接,默认**保持指向中文原文路径**(链接可点,读者到达中文文件),不新建 en 引擎文件、不留死链。备选(被否决倾向):引擎文件全翻——skills 全量 3,718 行,首期工程量翻倍。〔L0 #4/#20 + 翻译面控制;链接可达优先于全英文环境〕

### 二、同步标记 + 检测接口(模块二 · 核心契约)

- [X]  **5 同步标记形态 = 内容 hash (硬约束)**:每个 en 文件 frontmatter `zh-hash` = 对应中文源文件**内容 SHA-256 前 12 位**;i18n-check 重算对比,不匹配 → 报「过期」。备选:git 修订标识(`zh-ref: <commit>`)——依赖 git 历史、worktree/分支含混、非 git 副本(全局侧类场景)失效,默认弃。〔L0 #15;文件自含、跨分支稳定、检查器可独立复算〕
- [X]  **6 i18n-check.py 三检查接口 (硬约束)**:① **结构镜像**:TRANSLATABLE 白名单文件逐个查 en 对映存在,缺 → 「缺镜像」违规;② **源指纹**:en 的 zh-hash ≠ 当前 zh 源实际 hash → 「过期」;③ **链接**:en 内全部相对链接目标文件存在(指向未翻文件允许指向 zh 原文,与 #4 一致),断 → 「断链」。CLI = `python3 scripts/i18n-check.py [repo根]`,EXIT 0/1,输出按 缺镜像 / 孤儿 / 过期 / 断链 四类分组;check-only 不改文件、不选边(与 skills-sync-check 同哲学)。〔L0 #14/#19;既有漂移治理资产同款运行语义〕
- [X]  **7 TRANSLATABLE 白名单 = 进白名单即负翻译义务 (硬约束)**:脚本内置「目录白名单 + 文件黑名单」数据驱动集;**初始白名单 = L0 #20#20 首期清单**(根 README / CHANGELOG / docs 根三件(CONTEXT、OPEN-DECISIONS、LICENSE 声明件)/ methodology current 三件 / 8 个 SKILL.md),**含 retro / OD 全量 / archive 等未进白名单 = 当前无翻译义务**(i18n-check 不报);后续迭代纳入时 = 改白名单(代码注明出处,与 EXCEPTIONS 同精神)+ 同批交付该组 en 翻译,保证 ① 恒可全绿。〔L0 #4 与 #20 的范围分层张力,出题依据第 4 条;「承诺即交付」防检查器永久红灯〕
- [X]  **8 孤儿判定与强制标记 (硬约束)**:en 文件的 `en-source` 指向的 zh 源不存在(被删 / 改名)→ 「孤儿」违规;en 文件缺 `en-source` 或 `zh-hash` 字段 → 「缺标记」违规。三字段(#1)为 en 文件合法性前提。〔L0 #10;无标记则孤儿 / 过期判定无锚〕

### 三、术语表契约(模块三)

- [X]  **9 英文术语落位 = CONTEXT 增设对照节**:CONTEXT 尾部新增「英文术语对照(English Glossary)」节——`| 术语 | EN | 定义锚点 |` 三列表,只收**有英译的核心术语**(首批 = 翻首期面时逐文件提取的高频术语);不动既有中文正文定义(中文定义仍是唯一权威,对照节只加译名列)。翻译以该节为准,禁各文件自译。备选:独立 GLOSSARY 文件(第二事实源,双写漂移)或逐条正文嵌 EN 注(侵入 canonical 中文正文)——默认增节。〔L0 #16 + CONTEXT 条目式结构实测;哲学 WAI/WAD 中英并置先例〕
- [X]  **10 新术语译名归属**:需要新英译名的术语 = agent 起草译名 + 人确认后落 CONTEXT 对照节;对照节自身随 CONTEXT 翻译入 en/docs/CONTEXT.md(英文侧术语表 = 对照节的英文化呈现)。〔CONTEXT「新词引入三条件门槛」英文侧对齐 + 单一事实源〕
- [X]  **11 「镜像」消歧落位**:CONTEXT 对照节收两条:「镜像 = release mirror(发布镜像,OD-10)」与「英文镜像 = translation mirror(本 feature)」,显式注记不同义。〔L0 #18 + 出题依据术语冲突预警〕
- [X]  **12 占位符与不可译元素保持规则 (硬约束)**:en 译文中脱敏占位符(「项目A / 项目B」等)保持原文不译;代码块 / mermaid 图 / 公式 / URL / 文件路径原样复制不译;中文锚点链接(#四-安全科学视角 式)按目标文件是否已译决定指向 en 或 zh(#4 规则同)。〔L0 #21④ + 脱敏门 + 验收③〕

### 四、翻译工作流契约(模块四)

- [X]  **13 翻译执行主体与人审分级**:AI 起草 + 人审;分级——**门面(README / methodology 三件 / CONTEXT)人必审**,非门面(OPEN-DECISIONS / SKILL.md / CHANGELOG)AI 自查 + 人抽查。全自动无 oracle 拒绝(判断类产出只能人审,ADR-0016 / OD-19 精神)。〔CONTEXT 证据状态节 + 人机分工术语〕
- [X]  **14 增量回译协议(提交门)**:zh 文件被报「过期」→ 进 TODO 待回译队列;i18n-check 并入**手动提交门**(与脱敏 / sync-check 同列:涉 en/ 或可翻中文文件的提交,0 违规才提交;无 CI / hook);回译 = AI 起草 + 按分级人审 + 更新 zh-hash → 再检变净。〔L0 #19⑥ + 仓库手动门现状;最小机制成本接入〕
- [X]  **15 根 CHANGELOG 翻译增量策略**:维持 L0 #20(CHANGELOG 现条目入首期);增量协议 = 新 CHANGELOG 条目发布时同步补 en 对应条目(append-only 镜像)。张力显式暴露:CHANGELOG 只增不减,英译长期负担 = 每发一条追一条;若觉负担过重,取消勾选 → W01 深究备选(从首期剔除 / 仅翻里程碑条目 / 英文侧只保留「最近 N 条」)。〔L0 #20 已决 + append-only 性质实测〕

### 五、License / canonical 声明(模块五)

- [X]  **16 canonical 声明块**:en/README.md 顶部固定 blockquote:**Translation notice** — This is a translation of the Chinese repository. The Chinese text is canonical; in case of conflict, the Chinese version governs.(中文一句对照)+ 链回根 README。〔L0 #17 + CC-BY 语境〕
- [X]  **17 License 继承与 CC-BY 署名**:en/docs/ 区文件继承 CC-BY 4.0——en/docs/LICENSE(或 LICENSE-EN)载明「Translation of docs/, original licensed CC-BY 4.0;attribution + note of changes」;en/skills/ 区继承 MIT(根 LICENSE 适用于全仓代码 / 配置,译文版权随 MIT)。en/README.md 的 License 节双注。〔docs/LICENSE + 根 LICENSE + ADR-0002 双分区〕

### 六、治理接口(模块六)

- [X]  **18 L0 验收操作化映射**:L1 文档记映射表——L0 验收 ①②③⑥ = i18n-check 四类输出;④ = desensitize 0 命中;⑤ = skills-sync-check 0 违规;⑦ = en 文件清点 = 白名单全集。验收从「描述」变「CLI 断言」。〔L0 #19 + ADR-0016 主张-证据精神〕
- [X]  **19 ADR 识别(三条件核对,达标)**:产生 1 份 ADR「英文镜像与既有漂移治理资产的接轨协议」——决策影响 skills/ 同步面边界(第三轴正交)+ 新增检查器 + 多文件契约,非临时,影响既有用法(提交门扩为四道)→ 三条件全中。默认 = L1 契约落盘时同步写 ADR-0025。〔ADR-0012 识别条件 + L0 #13/#14 架构裁决〕
- [X]  **20 全局侧接口(防遗漏确认)**:全局 `~/.claude/skills/` **零动作**(不部署 en、不改 sync-check);en 镜像只随项目仓库分发,英文用户拉库自取。OD-10 分发洁净目标态不因 i18n 改变。〔L0 #13 + ADR-0024 双侧常态分工〕
- [X]  **21 首期执行序(移交 L2 拆分)**:机制先于内容——① en/ 目录 + 标记规范 + i18n-check + 术语对照节就位 → ② README → ③ methodology 三件 + CONTEXT → ④ 8 SKILL.md → ⑤ CHANGELOG;每步过 L0 验收 ①–⑥ 再进下一步。阶段拆分与 DoD 细化归 L2-build。〔L0 #20「先机制后覆盖」〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-23,W00 处理)

**作答解析**:21/21 答毕,无异常。无 🤔 逃生舱。

**preview 统计**:勾选采纳 **21** · 取消勾选 **0** · 转 W01 正式题 **0**。opt-in 未启用,取消默认率不适用。补充声明为空。

**每题去向**:21 条全按默认落盘 [L1-contract-en-mirror-governance.md](../../design/i18n-support/L1-contract-en-mirror-governance.md)(六模块 + 验收映射表 + 选型/被否决汇总)。落盘时的两处等价澄清(不改变决策语义,记此处备查):① #7「LICENSE 声明件」落地形态 = LICENSE 法律文本不作翻译单元,en 侧以 EN_NATIVE 声明件承载归属(L1 §2.3/§2.4);② #6 输出类在「四类」基础上把「缺标记」拆为独立输出类 = 五类(L1 §2.2,与 #8 强制标记一致)。

**同步产出**:[ADR-0025](../../adr/0025-english-mirror-drift-governance-integration.md)(接轨协议,三条件全中);[CONTEXT.md](../../../docs/CONTEXT.md) 新增「英文术语对照(English Glossary)」节(含 #11 镜像/英文镜像消歧两条即刻落位,首批术语随首期翻译补齐)。

**下一波候选(L2 W00 要点登记)**:① i18n-check.py 实现规格(五类检查的数据结构与输出格式);② 首期执行序五阶段的任务拆分与 DoD(P1 机制 → P2 README → P3 methodology+CONTEXT → P4 SKILL.md → P5 CHANGELOG);③ 翻译流程模板(AI 起草提示词骨架 + 人审记录形态);④ zh-hash 标记的写入工具(手工 vs 脚本辅助);⑤ readme-revamp 重访留痕两处的执行时点并入 P1。

**未验证假设台账**:无新增未验证假设(SHA-256 由 python3 标准库支持,无外部依赖需实测;提交门无 CI 现状已核实)。L0 台账两项开放判定(archive 纳入 / 同步标记形态)已由本层关闭(archive 未进白名单 = 当前无义务;标记 = 内容 hash)。

**状态**:pending → processed(2026-08-23)→ archived(同日,目录 i18n-support/)。
