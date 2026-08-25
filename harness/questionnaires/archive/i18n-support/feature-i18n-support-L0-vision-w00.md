---
mode: feature
wave: 0
stage: L0-vision
created: 2026-08-22
status: archived
---
# 问卷 feature-i18n-support L0-vision W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的决策点逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(默认关):仅当你启动本 skill 时明确说「预勾选」,要点才预勾 `[x]`(勾 = 采纳默认);未启用时全部 `[ ]`,人逐条作答
> - **取消勾选(留空)= 不采纳** → 该要点转入 W01 单独拷问(出选项深究)
> - **单向门要点(发布 / 删除 / 花钱 / 脱敏等不可逆)永不预勾**,强制人逐条显式勾选确认
> - 本波**不用 🤔**(yes/no 二选一,无中间态);真定不了 → 取消勾选即可,转 W01 深究
> - 若"大体同意但要改一两处" → 取消勾选,转 W01 时在深究题里给自定义值
>
> 默认来源标注于〔〕。

> **出题依据摘要**(2026-08-22 探索,事实已核实):
>
> - **语言现状**:全库纯中文唯一主语言,无任何 i18n 基础设施。英文仅存在于 3 处非主面(grill-with-docs 的 SKILL.md + ADR/CONTEXT/OPEN-DECISIONS-FORMAT 三个格式文件、waste/skills/grill/、个别 frontmatter description);哲学文档「关键术语采用中英文」(WAI = Work-As-Imagined)为唯一中英并置先例(用户裁决)。〔subagent 全库扫描 + README/CONTEXT/方法论文档实测〕
> - **规模基线**:全库 230 个 .md、23,576 行(含 archive 与内部产物);对外文案主面 = README 170 + docs 根 526 + docs/methodology current 三件 1,353 + skills/ 3,718(规则本体 SKILL.md 约 1,000 行)。〔wc -l 分组统计〕
> - **既有已决项「不做英文 README」**:2026-08-20 readme-revamp L0 设计文档 `harness/design/readme-revamp/L0-vision-readme-first-impression.md:22`「不做英文 README(列为未来可选项,外部反馈出现需求时再议,在 CHANGELOG 记一笔留痕)」+ 归档问卷要点 12(`feature-readme-revamp-L0-vision-w00.md:51`)。本次 i18n 立项 = 该「未来可选项」的触发条件满足,属**对既有已决项的重访**,需显式留痕。
> - **既有漂移治理资产**(接轨对象):铁律 8 双侧同步 = 规则本体(SKILL.md/引擎/FORK-NOTES)项目↔全局逐字节一致 + 历史层(CHANGELOG/DESIGN)仅项目侧 + 全局私有类(DOGFOOD-LOG)仅全局侧;skills-sync-check.py **恰好双侧硬编码**(路径 `skills/` vs `~/.claude/skills/` + HISTORY_LAYER/GLOBAL_ONLY 类规则 + EXCEPTIONS 白名单 + 存在性/内容两类检查,无第三侧抽象);ADR-0024 双侧常态性形态分工;OD-8 引擎副本漂移声明(FORK-NOTES 载体);OD-24 双副本实验策略。〔ADR-0024 全文 + skills-sync-check.py 源码逐行 + CLAUDE.md 铁律 8〕
> - **术语冲突预警**:仓库现有「镜像」一词指 **skill 发布镜像**(分发副本语义,OD-10),与本次「英文镜像翻译」不同义——进 CONTEXT 术语表须消歧(建议称「英文镜像 / translation mirror」),防术语撞名。
> - **双 License 分区**:docs/= CC-BY 4.0(署名转载)、skills/+scripts/= MIT;译本继承原协议,CC-BY 要求署名 + 变更注明。〔docs/LICENSE + LICENSE + ADR-0002〕
> - **用户定模裁决**(2026-08-22 入口校准闸门):框架理解正确;L0+L1+L2 三层、多文件形态。
> - **无未验证假设**:出题依据全部一手核实(读原文 / 跑脚本 / 分组统计);无外部依赖选型需实测(i18n 不引第三方库)。

## 决策默认值清单

### 一、目标与动机

- [X]  **1 feature 一句话目标**:为仓库建立「中文 canonical + 英文镜像」的 i18n 支持——中文为唯一权威源,英文以顶级 `en/` 文件夹镜像派生并受漂移治理(结构失配 / 过期 / 链接三类可检出),服务英文读者理解并引用方法论体系。〔用户请求「首选中文、支持英语、单独文件夹治理、与中文同步、重点关注漂移治理」〕
- [X]  **2 服务对象定标**:英文镜像第一受众 = 潜在**英文采用者 / 方法论读者**(分发展示:能读懂方法论、能导航到任一文档、能引用);「让英文用户全量**运行** 8 个 skill 工作流」默认 = 范围外(运行级 = 每 skill 双语言执行体,工程量 ×2 且与「中文是唯一生产车间」相悖;英文用户如要运行按需手动适配)。〔readme-revamp「第一受众 = 潜在采用者」类比 + 用户「首选语言中文」〕
- [X]  **3 canonical 方向(单向)**:中文 = 唯一权威源;英文 = 单向派生的镜像,**英文永不回灌中文**(反向不成立);中文每次修订 → 对应英文镜像进入「待翻译 / 过期」状态。同步语义 = 结构镜像 + 源指纹检出 + 人驱动回译,**非自动机械改写**。〔用户「首选中文」「与中文同步」〕

### 二、范围边界(做什么 / 明确不做什么)

- [X]  **4 「全仓库」的镜像边界**(对用户「范围全仓库」的界定重访):默认 = 只镜像**对外消费内容**——根 README、根 CHANGELOG(对外变更记录)、docs/(CONTEXT / OPEN-DECISIONS / methodology current 三件 / retro)、skills/ 各 SKILL.md(规则本体的英文说明);**明确排除内部治理产物**:harness/ 全部(ADR / design 层文件 / 归档问卷 / STATUS-LOG)、TODO.md、CLAUDE.md、AGENTS.md、scripts/、waste/。理由:内部产物是「AI 生产车间」+ 历史事实,无英文读者、归档问卷/ADR 不可译(历史记录),且每次演进都同步 = 超额漂移成本;「范围全仓库」应解读为「全对外门面」。〔探索:内部产物语义 + readme-revamp「README 与 CLAUDE.md 分工维持」〕
- [X]  **5 脚本输出 / docstring 默认不翻**:scripts/ 三个 py 的中文消息与 docstring 是内部工具产物,不纳入英文镜像。〔探索:脚本输出语言随用者,非对外文案〕
- [X]  **6 archive/ 历史文档默认不翻首期**:docs/methodology/archive/ 六件(约 3,012 行历史母本)与 philosophy archive 默认首期排除,只镜像 current/canonical 三件 + practical_v1;archive 是否纳入英文镜像留 L1 定(不预设)。〔探索:archive = 历史母本,读者应读 current;工程量控制〕
- [X]  **7 镜像粒度 = 文件级**(不做到段级):以「文件」为最小镜像单元,不做逐段对齐(翻译记忆库式段级 = 工程复杂度高,首期不值)。〔漂移治理最小可行 + 成本控制;W01 可重访更细粒度〕

### 三、核心场景

- [X]  **8 场景一·英文读者到达**:英文开发者到 GitHub → 从根 README 顶部语言切换链接进入 `en/README.md` → 读英文方法论三件 → 理解双支柱与体系 → 深读 8 个 skill 英文 SKILL.md → 引用 / 试用。〔验收:en/ 根为可导航入口,从根可达任一镜像文件〕
- [X]  **9 场景二·中文演进 → 过期检出**(漂移治理核心场景):中文某文件修订 → 漂移检测器报「该文件源已变、英文镜像过期」→ 人 / agent 安排回译 → 回译后镜像的同步标记更新 → 再检变净。〔验收:实测改一处中文,检测器即报「过期」〕
- [X]  **10 场景三·结构失配检出**:中文新增可翻文件 → en 缺镜像 = 违规;中文删除文件 → en 孤儿(无中文源)= 违规。检测器两类都报。〔验收:i18n-check 对「缺镜像」与「孤儿」分别报出〕

### 四、布局与接轨治理资产的方向(细节契约落 L1)

- [X]  **11 目录布局方向**:仓库根新增顶级 `en/` 目录,内部**镜像中文相对结构**(`en/README.md` ↔ `README.md`;`en/docs/methodology/methodology_v5.md` ↔ `docs/methodology/methodology_v5.md`;`en/skills/design-questionnaire/SKILL.md` ↔ `skills/design-questionnaire/SKILL.md`)。单顶级镜像树,不建 per-目录 en 子目录。即「单独文件夹治理」的字面落地。〔用户「单独文件夹治理」+ GitHub 呈现 + 结构清晰优先〕
- [X]  **12 语言切换入口**:根 README 顶部加「English / 中文」切换链接 → `en/README.md`;`en/README.md` 顶部反向链接回根中文 README。中文仍为根默认 README(GitHub 首页展示),英文经链接直达。〔GitHub 不渲染非根 README 的事实 + 用户「首选中文」〕
- [X]  **13 英文镜像与 skill 双侧同步的关系**(关键架构裁决):英文镜像文件放 `en/skills/...`(**顶级 en/ 内**),**不进** `skills/` 本体 → **不进入 skills-sync-check 扫描面**,现有双侧同步语义(规则本体逐字节一致 + 历史层类规则)零扰动;全局侧 `~/.claude/skills/` 默认**不加英文**(中文生产车间保持原样)。英文翻译同步 = 独立第 3 轴(zh↔en),与双侧(项目↔全局)正交。理由:把 en 塞进 skills/ 会使 sync-check 误报「仅项目侧存在」,破坏 ADR-0024 逐字一致语义;顶级 en/ 隔离 = 无侵入接轨。〔ADR-0024 + skills-sync-check.py 源码:目录对 / 存在性分支 / 输出类别均硬编码恰好双侧〕
- [X]  **14 漂移检测机制接轨路径**:新建独立 `scripts/i18n-check.py`(结构镜像存在性 + 源指纹过期 + 链接三类检查),**不改造** skills-sync-check.py(其「逐字节一致」语义与翻译同步本质不同,二者是不同轴);提交前两脚本并联跑。[〔skills-sync-check.py 分析 + 用户「接轨」而非「混入」〕
- [X]  **15 源指纹 / 同步标记方向**:每个可翻中文文件配套一个**同步标记**(记录「回译所依据的中文源指纹」= 内容 hash 或修订标识);检测规则 = 中文源当前指纹 ≠ 镜像标记 → 该镜像「过期」。文件级,不做段级(见 #7)。〔最小可行漂移检测;宁可整文件重译也防「改一行静默过时」〕
- [X]  **16 术语一致方向**:英文术语**单点落位** = CONTEXT 术语表增「英文术语」列(或独立双语术语节),翻译以该列为准,**禁各文件自行英译**(防术语漂移);与哲学「术语中英文并置」(WAI/WAD)用户裁决先例一致。〔CONTEXT = 术语唯一权威源 + 哲学中英并置先例〕
- [X]  **17 License 与 canonical 声明**:译文继承原内容 License(译 docs/ 部分 → CC-BY 4.0、译 skills/ 部分 → MIT);`en/` 镜像根放一行 canonical 声明:「EN 为译本,原文以中文为准」,CC-BY 的署名与变更注明照章执行。〔docs/LICENSE + 根 LICENSE + ADR-0002 / CC-BY 要求〕
- [X]  **18 「镜像」术语消歧**:新概念命名采用「**英文镜像 / translation mirror**」,与仓库既有「镜像(发布镜像 / release mirror, OD-10)」在 CONTEXT 术语表显式区分,防撞名污染既有术语。〔探索发现:现有「镜像」= skill 发布分发副本语义〕

### 五、验收标准(可独立验证条目式)

- [X]  **19 验收主集默认**:
  - ① 结构镜像完整:`python3 scripts/i18n-check.py` 对每一「可翻文件」报「缺镜像」为 0(全部有一一对映 en);
  - ② 无孤儿 en:同脚本「无中文源」报为 0;
  - ③ en 内链接全通:提取 en/ 全部相对链接逐条核通(含锚点);
  - ④ 脱敏:`python3 scripts/desensitize.py .` 0 命中(英文镜像占位符如「项目X」保持一致,不误译);
  - ⑤ 既有合规不破:`python3 scripts/skills-sync-check.py` 仍 0 违规(经 #13 隔离,英文镜像不入扫描面);
  - ⑥ 过期检出可演示:实测改一处中文源 → i18n-check 报「中文已变、英文过期」;
  - ⑦ 首期翻译面覆盖完成(见 #20 清单)。〔L0 骨架「可独立验证条目式」+ ADR-0016 主张-证据精神〕
- [X]  **20 首期翻译面(交付范围,不追一次翻全)**:默认首期 = 门面与核心 = 根 README + docs/methodology current 三件(methodology_v5 / philosophy_v7 / practical_v1)+ docs/CONTEXT + docs/OPEN-DECISIONS + 8 个 skill 的 SKILL.md + 根 CHANGELOG 现条目;**架构(目录/检查器/术语/工作流)一次到位,翻译分步推进**——首期之后的覆盖面(OD 全量 / archive / retro 等)由后续迭代补,不在首次交付承诺。理由:全库 2.36 万行一次翻完 = 超长尾、必然中途漂移;先定机制再滚量。〔工程量基线 + 漂移治理「先机制后覆盖」〕

### 六、风险与约束

- [X]  **21 风险登记默认**:① 双写 / 漂移(本 feature 的核心对抗对象——中文演进后英文静默过期)→ 对策 = 独立检查器 + 提交前门(强制跑 #19 ①–⑦);② 术语不一致(各文件自行英译)→ 对策 = #16 CONTEXT 单点英文术语列;③ 链接重写错(en 内互链指错)→ 对策 = 验收③链接检查;④ 占位符 / 脱敏误译(「项目X」被当普通词译掉)→ 对策 = 译文占位符保持原文 + 验收④;⑤ 工程量(2.36 万行)→ 对策 = #20 分步首期。〔探索:全库规模基线 + 既有治理先例〕
- [X]  **22 既有已决项重访(显式留痕)**:readme-revamp「不做英文 README(列为未来可选项)」已决项 → 本次 i18n 立项 = 该未来可选项触发条件满足,默认**正式推翻该决、执行英文镜像**,并在两处留痕:① `harness/design/readme-revamp/L0-vision-readme-first-impression.md` 该行加重访注记;② 根 CHANGELOG 记一条「i18n 立项 = 重访 readme-revamp 英文 README 决项」。不得静默执行。〔readme-revamp 设计文档 / 归档问卷一手核实 + 「改已决事项先查 OPEN-DECISIONS 与 ADR」治理〕
- [X]  **23 价值排序**:漂移治理(不腐坏)> 术语一致 > 覆盖全面 > 译文润色;首期使命 = **立起可复跑的治理机制 + 门面译文**,不追求一次翻全。〔用户「重点关注漂移治理」〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-22,W00 处理)

**作答解析**:23/23 答毕,无异常(无多勾、无留空)。W00 无 🤔 逃生舱。

**preview 统计**:勾选采纳 **23** · 取消勾选 **0** · 转 W01 正式题 **0**。opt-in 预勾开关未启用(全程 `[ ]` 人逐条作答),取消默认率不适用。补充声明为空(无新增需求)。

**每题去向**:23 条全按默认落盘 [L0-vision-i18n-support.md](../../design/i18n-support/L0-vision-i18n-support.md)(2026-08-22 成稿)。L0 骨架七项(目标 / 范围 / 核心场景 / 验收 / 风险 / 动机 / L0 自检节)全覆盖,无开放必答项 → L0 **无 W01**,直接进入层闸门。

**下一波候选(L1 W00 要点登记)**:① en/ 目录布局与 README 切换入口;② 同步标记具体形态(源指纹 hash vs 修订标识);③ CONTEXT 英文术语列粒度与落位;④ archive/ 是否纳入英文镜像(不预设);⑤ 增量/回译工作流(中文修订后谁触发、回译如何验收);⑥ i18n-check 三类检查接口(结构镜像 / 源指纹 / 链接)。

**未验证假设台账**:无新增未验证假设(出题依据全部一手核实:skills-sync-check.py 逐行读、ADR-0024 / HARNESS-RULES / readme-revamp 设计文档 / CONTEXT / OPEN-DECISIONS 读原文、全库 .md 分组统计由 subagent 提供并以 wc 复核)。待 L1 重验的规划支撑 = archive/ 判定 + 检查器接口细节。

**状态**:pending → processed(2026-08-22)→ archived(同日,目录 i18n-support/)。
