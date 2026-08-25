# L1-contract-en-mirror-governance.md · 英文镜像治理契约(feature-i18n-support)

> 导览:① 本层位置与职责 = 契约层(L1)——把 L0 的目标与验收操作化为可执行的布局 / 标记 / 检查器 / 术语 / 工作流 / License 六模块契约 ② 覆盖范围 = en/ 镜像树结构、同步标记与漂移检测接口、英文术语表、翻译与回译工作流、License 与 canonical 声明、与既有漂移治理资产(铁律 8 / ADR-0024 / skills-sync-check / OD-8 / OD-24)的接轨边界 ③ 上下游依赖 = 上承 [L0-vision-i18n-support.md](L0-vision-i18n-support.md) 验收七条,下启 L2-build(脚本实现 + 首期翻译执行);实现偏离本契约走 [ADR-0021](../../adr/0021-design-implementation-deviation-governance.md) 治理性偏差路径 ④ 契约项声明 = 标注 **(硬约束)** 的条目(§2 全节 + §1.1 + §3.4 + §6.1 映射表)为 L2 不可偏离契约;其余为实现倾向,允许 L2 在等价范围内细化。
>
> 裁决来源:[feature-i18n-support-L1-contract-w00](../../questionnaires/archive/i18n-support/feature-i18n-support-L1-contract-w00.md)(2026-08-23,21/21 全采纳,取消默认率不适用,转 W01 0 项)。架构决策同录 [ADR-0025](../../adr/0025-english-mirror-drift-governance-integration.md)。

## §1 镜像树布局(模块一)

### 1.1 en/ 映射规则与文件头标记 **(硬约束)**

- `en/` 下文件与中文源**相对路径一一对映**:`en/<zh 相对路径>`(例:`en/docs/CONTEXT.md` ↔ `docs/CONTEXT.md`;`en/skills/design-questionnaire/SKILL.md` ↔ `skills/design-questionnaire/SKILL.md`)。
- 每个 en 镜像文件头部必带三字段标记(YAML frontmatter;已有 frontmatter 的文件如 SKILL.md 在既有 frontmatter 内追加):
  - `lang: en`
  - `en-source: <zh 相对路径>`(孤儿判定与链接检查的锚)
  - `zh-hash: <源指纹>`(见 §2.1)
- 已知渲染代价注记:GitHub 会把 frontmatter 渲染为顶部表格(en/README.md 可见)。这是采纳「frontmatter 三字段」的已知代价;若 L2 期间用户嫌渲染干扰,可换载体为文件首行 HTML 注释 `<!-- i18n: … -->`(语义不变),属等价细化非契约变更(改前须用户确认一次)。

### 1.2 README 切换入口

- 根 README 标题下固定一行:`**中文** · [English](en/README.md)`(当前语言加粗,另一语言为链接;dogfood 修订 2026-08-23:原文 `**English** · [中文](./README.md)` 的链接指向自身,系笔误,按对称语义更正)。
- `en/README.md` 顶部对应:`[中文](../README.md) · **English**`。
- 中文为 GitHub 仓根默认(GitHub 不渲染非根 README 为仓根),英文经链接直达。

### 1.3 en 根导航文件

`en/README.md` 兼作英文镜像根入口,四职:语言切换回链 + canonical 声明(§5.1)+ License 说明(§5.2)+ 镜像树导航(分区块列出全部 en 路径)。en/ 下不另建独立「目录索引」文件(导览集中单点)。

### 1.4 en SKILL.md 内引擎链接策略

首期只镜像 8 个 SKILL.md 本体(引擎文件 QUESTIONNAIRE-FORMAT / PROCESSING-RULES / STAGE-SKELETONS / 各 FORMAT 文件不翻)。en SKILL.md 中指向引擎文件 / CHANGELOG / DESIGN 的相对链接,**保持指向中文原文路径**(链接可点,读者到达中文文件),不新建 en 引擎文件、不留死链。被否决:引擎文件全翻(skills 全量 3,718 行,首期工程量翻倍)。

## §2 同步标记 + 漂移检测接口(模块二 · 核心契约)**(硬约束全节)**

### 2.1 同步标记形态 = 内容 hash

- 每个 en 文件 `zh-hash` = 对应中文源文件**内容 SHA-256 前 12 位**(python3 hashlib 标准库,无外部依赖)。
- 检测规则:en.zh-hash ≠ 当前 zh 源实际 hash → 报「过期」。
- 被否决:git 修订标识(`zh-ref: <commit>`)——依赖 git 历史、worktree / 分支含混、非 git 副本失效;hash 文件自含、跨分支稳定、检查器可独立复算。

### 2.2 i18n-check.py 三检查接口

- **① 结构镜像**:TRANSLATABLE 白名单(§2.3)文件逐个查 en 对映存在,缺 → 「缺镜像」违规。
- **② 源指纹**:en 的 zh-hash ≠ 当前 zh 源实际 hash → 「过期」;en 文件缺 `en-source` / `zh-hash` 字段 → 「缺标记」违规;`en-source` 指向的 zh 源不存在 → 「孤儿」违规。
- **③ 链接**:en 内全部相对链接目标文件存在(指向未翻文件允许指向 zh 原文,与 §1.4 一致),断 → 「断链」。
- CLI:`python3 scripts/i18n-check.py [repo根]`;EXIT 0 = 无违规 / 1 = 有违规;输出按 **缺镜像 / 孤儿 / 过期 / 缺标记 / 断链** 五类分组(缺标记为 §2.2② 拆出的独立输出类);check-only 不改文件、不选边(与 skills-sync-check 同哲学)。

### 2.3 TRANSLATABLE 白名单 = 进白名单即负翻译义务

- 脚本内置数据驱动的「目录白名单 + 文件黑名单」;**白名单 = 已交付翻译义务清单,随阶段扩容**(dogfood 修订 2026-08-23:原「初始白名单 = L0 首期清单一次性全量」与 §4.2「0 违规才提交」在首期实施窗口冲突——P1–P4 期间未翻文件会恒报缺镜像,提交门无法全绿;回修为每阶段把新翻完的文件加入白名单,语义不变:进白名单即负翻译义务,检查 ① 恒可全绿):
  - P2 起:`README.md`
  - P3 后加:`docs/CONTEXT.md`、`docs/OPEN-DECISIONS.md`、`docs/methodology/methodology_v5.md`、`docs/methodology/philosophy_v7.md`、`docs/methodology/practical_v1.md`
  - P4 后加:`skills/*/SKILL.md`(8 个)
  - P5 后加:`CHANGELOG.md`
- 未进白名单(retro / OD 全量 / archive / harness / scripts 等)= **当前无翻译义务**,i18n-check 不报;后续迭代纳入 = 改白名单(代码注明出处,与 skills-sync-check EXCEPTIONS 同精神)**+ 同批交付该组 en 翻译**,保证 ① 恒可全绿。
- **LICENSE 澄清**(W00 #7「LICENSE 声明件」的落地形态):根 LICENSE 与 docs/LICENSE 为法律文本(英文原文),**不作为翻译单元**、不入白名单;en/ 侧以 en 原生声明文件(§5.2)承载归属与变更注明。

### 2.4 EN_NATIVE 豁免集(en 原生文件)

en/ 下少数文件是**原生声明件而非镜像**(无 zh 源),按 §2.2 会误报「孤儿 / 缺标记」——脚本内置 `EN_NATIVE` 豁免集(初始 = `en/README.md` 的 License 节所引声明件,含 `en/docs/LICENSE` translation-notice 文件;后续增删改代码注明出处)。en/README.md 本身仍是镜像(en-source = README.md)。

## §3 术语表契约(模块三)

### 3.1 英文术语落位 = CONTEXT 增设对照节

- `docs/CONTEXT.md` 尾部「英文术语对照(English Glossary)」节:`| 术语 | EN | 定义锚点 |` 三列表,只收**有英译的核心术语**(首批 = 翻首期面时逐文件提取的高频术语,随翻译补齐)。
- 不动既有中文正文定义(中文定义仍是唯一权威,对照节只加译名列);翻译以该节为准,**禁各文件自译**。
- 被否决:独立 GLOSSARY 文件(第二事实源,双写漂移);逐条正文嵌 EN 注(侵入 canonical 中文正文)。

### 3.2 新术语译名归属

新英译名 = agent 起草 + 人确认后落 CONTEXT 对照节(与「新词引入三条件门槛」英文侧对齐);对照节随 CONTEXT 翻译入 en/docs/CONTEXT.md(英文侧术语表 = 对照节的英文化呈现)。

### 3.3 「镜像」消歧(已落位)

CONTEXT 对照节收两条:镜像 = **release mirror**(发布镜像,OD-10)vs 英文镜像 = **translation mirror**(本 feature),显式注记不同义(2026-08-23 已随本契约落盘)。

### 3.4 占位符与不可译元素保持 **(硬约束)**

- en 译文中脱敏占位符(「项目A / 项目B」等)保持原文不译;
- 代码块 / 公式 / URL / 文件路径原样复制不译;
- **mermaid 图内文本标签(label)译英**——语法结构与节点 ID 不动,仅译引号内文本与边标签;渲染验证人审兜底(图坏则回退原文重译)。〔2026-08-23 dogfood 修订:原「mermaid 原样不译」的两条理由复核——「防图漂移」不成立(图在文件内,文件级 zh-hash 已覆盖:中文图变 → hash 变 → 报过期 → 回译同步图),仅语法风险真实且可控;README 协作图是承重件,英文读者在图处断线的代价大于译图成本。触发 = 人审质询,用户裁决「修订并译图」〕
- 中文锚点链接(如 `#四-安全科学视角` 式)按目标文件是否已译决定指向 en 或 zh(§1.4 规则同)。

## §4 翻译工作流契约(模块四)

### 4.1 翻译执行主体与人审分级

AI 起草 + 人审;分级——**门面(README / methodology 三件 / CONTEXT)人必审**,非门面(OPEN-DECISIONS / SKILL.md / CHANGELOG)AI 自查 + 人抽查。全自动无 oracle 拒绝(判断类产出只能人审,ADR-0016 / OD-19 精神)。

### 4.2 增量回译协议(提交门)

- zh 文件被报「过期」→ 进 TODO 待回译队列;
- **i18n-check 并入手动提交门**(与脱敏 / sync-check 同列:涉 en/ 或可翻中文文件的提交,0 违规才提交;无 CI / hook);
- 回译 = AI 起草 + 按分级人审 + 更新 zh-hash → 再检变净。

### 4.3 根 CHANGELOG 翻译增量策略

维持 L0 #20(CHANGELOG 现条目入首期);增量协议 = 新 CHANGELOG 条目发布时同步补 en 对应条目(append-only 镜像)。已知长期负担:每发一条追一条;W00 #15 已显式暴露,维持默认(后续觉负担过重可重访,备选:仅翻里程碑条目 / 英文侧只留最近 N 条)。

## §5 License / canonical 声明(模块五)

### 5.1 canonical 声明块

`en/README.md` 顶部固定 blockquote:**Translation notice** — This is a translation of the Chinese repository. The Chinese text is canonical; in case of conflict, the Chinese version governs.(附中文一句对照)+ 链回根 README。

### 5.2 License 继承与 CC-BY 署名

- en/docs/ 区文件继承 CC-BY 4.0:`en/docs/LICENSE`(EN_NATIVE 声明件,§2.4)载明「Translation of docs/, original licensed CC-BY 4.0; attribution + note of changes」;
- en/skills/ 区继承 MIT(根 LICENSE 适用全仓,译文版权随 MIT);
- en/README.md 的 License 节双注(CC-BY + MIT 分区说明)。

## §6 治理接口(模块六)

### 6.1 L0 验收 → CLI 断言映射表 **(硬约束)**

| L0 验收 | 断言 |
|---|---|
| ① 结构镜像完整 | `i18n-check`「缺镜像」= 0 |
| ② 无孤儿 en | `i18n-check`「孤儿」= 0 |
| ③ en 内链接全通 | `i18n-check`「断链」= 0 |
| ④ 脱敏 0 命中 | `desensitize.py .` EXIT 0 |
| ⑤ 既有合规不破 | `skills-sync-check.py` EXIT 0 |
| ⑥ 过期检出可演示 | 实测改一处中文 → `i18n-check` 报「过期」 |
| ⑦ 首期翻译面覆盖完成 | en 文件清点 = TRANSLATABLE 白名单全集 |

### 6.2 ADR-0025(已同步落盘)

「英文镜像与既有漂移治理资产的接轨协议」——三条件全中(影响 skills/ 同步面边界 + 新增检查器 + 多文件契约;非临时;影响既有用法,提交门扩为四道)。见 [ADR-0025](../../adr/0025-english-mirror-drift-governance-integration.md)。

### 6.3 全局侧接口(零动作)

全局 `~/.claude/skills/` **零动作**(不部署 en、不改 sync-check);en 镜像只随项目仓库分发,英文用户拉库自取;OD-10 分发洁净目标态不因 i18n 改变。

### 6.4 首期执行序(移交 L2 拆分)

机制先于内容:① en/ 目录 + 标记规范 + i18n-check + 术语对照节就位 → ② README → ③ methodology 三件 + CONTEXT → ④ 8 SKILL.md → ⑤ CHANGELOG;每步过 L0 验收 ①–⑥ 再进下一步。阶段拆分与 DoD 归 L2-build。

## §7 全局选型与被否决项汇总(L1 骨架必含)

| 选型点 | 选定 | 被否决(理由) |
|---|---|---|
| 镜像位置 | 顶级 `en/` 镜像树 | en 入 skills/ 本体(sync-check 误报,破坏 ADR-0024);per-目录 en 子目录(结构碎) |
| 检测器归属 | 新建独立 `scripts/i18n-check.py` | 改造 skills-sync-check 支持第三侧(恰好双侧硬编码;逐字一致语义 ≠ 翻译同步语义,不同轴不混) |
| 源指纹形态 | 内容 SHA-256 前 12 位 | git 修订标识(依赖 git 历史 / 分支含混 / 非 git 副本失效) |
| 术语表落位 | CONTEXT 增设对照节 | 独立 GLOSSARY(第二事实源);正文嵌注(侵入 canonical) |
| 镜像粒度 | 文件级 | 段级 / 翻译记忆库(工程复杂度) |
| 提交门形态 | 手动门(第四道) | CI / git hook(仓库无 CI 现状,机制成本最小接入) |
| en 引擎文件 | 不翻,链接指中文原文 | 全翻(工程量 ×2) |
