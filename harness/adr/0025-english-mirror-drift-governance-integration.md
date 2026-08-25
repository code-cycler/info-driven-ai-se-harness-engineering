# ADR-0025: 英文镜像与既有漂移治理资产的接轨协议

- 状态:accepted(2026-08-23,design-Q feature i18n-support,L0+L1 两层)
- 决策日期:2026-08-23

## 背景

全库纯中文唯一主语言(230 个 .md / 23,576 行),无任何 i18n 基础设施。2026-08-23 用户发起 i18n 支持(首选中文、支持英语、单独文件夹治理、与中文同步、重点关注漂移治理,接轨既有漂移治理资产:铁律 8 / OD-8 / OD-24 / ADR-0024 / skills-sync-check,范围全仓库,镜像翻译)。同期发现 readme-revamp(2026-08-20)曾决「不做英文 README(列为未来可选项,外部反馈出现需求时再议)」——本次立项即该触发条件满足,属对既有已决项的显式重访(L0 W00 #22,推翻并双处留痕,见 TODO 对应行动项)。

接轨对象现状(一手核实):铁律 8 / ADR-0024 双侧常态性形态分工 = 规则本体(SKILL.md / 引擎 / FORK-NOTES)项目↔全局**逐字节一致** + 历史层(CHANGELOG / DESIGN)仅项目侧 + 全局私有类(DOGFOOD-LOG)仅全局侧;`skills-sync-check.py` 为**恰好双侧**硬编码(目录对 / 存在性分支 / 输出类别均无第三侧抽象);提交门 = 手动三道门(脱敏 0 命中 + 语义人审 + 脱敏报告;skill 改侧后 sync-check 0 违规),无 CI。

## 决策

1. **独立第三轴,顶级 en/ 隔离**:中文 = 唯一 canonical,英文 = 单向派生镜像(英文永不回灌中文);镜像树 = 仓库根 `en/` 下与中文源**相对路径一一对映**(文件级);en 镜像**不入** `skills/` 本体 → 不进入 skills-sync-check 扫描面;全局侧 `~/.claude/skills/` 零动作。翻译同步(zh→en)与双侧同步(项目↔全局)正交,是漂移治理的独立第三轴。
2. **en 文件头三字段标记**:每个 en 镜像文件必带 `lang: en` + `en-source: <zh 相对路径>` + `zh-hash: <源指纹>`;zh-hash = 中文源内容 **SHA-256 前 12 位**(弃 git 修订标识:依赖 git 历史、分支含混、非 git 副本失效);en 原生声明件(如 en/docs/LICENSE notice)入 EN_NATIVE 豁免集。
3. **新建独立 `scripts/i18n-check.py`**(不改 skills-sync-check):三检查五类输出——① 结构镜像(TRANSLATABLE 白名单文件缺 en 对映 =「缺镜像」)、② 源指纹(zh-hash ≠ 当前 hash =「过期」;缺字段 =「缺标记」;源不存在 =「孤儿」)、③ 链接(en 内相对链接断 =「断链」,指向未翻中文原文合法);CLI `python3 scripts/i18n-check.py [repo根]`,EXIT 0/1,check-only 不改文件、不选边(与 sync-check 同哲学)。
4. **TRANSLATABLE 白名单 = 进白名单即负翻译义务**:初始白名单 = L0 首期清单(README / CHANGELOG / docs 根两件 / methodology current 三件 / 8 个 SKILL.md);LICENSE 法律文本不作为翻译单元;后续迭代纳入新组 = 改白名单(代码注明出处)+ 同批交付该组 en 翻译,保证检查 ① 恒可全绿。
5. **手动提交门扩为第四道**:涉 en/ 或可翻中文文件的提交,前置 `i18n-check` 0 违规(与脱敏 / sync-check / 语义人审同列;不设 CI / hook)。
6. **英文术语单点事实源**:`docs/CONTEXT.md` 增设「英文术语对照(English Glossary)」节,翻译以该节为准,禁各文件自译;新译名 = agent 起草 + 人确认入表;「镜像 = release mirror(OD-10)」与「英文镜像 = translation mirror(本 feature)」显式消歧。
7. **License 继承 + canonical 声明**:译 docs/ 区继承 CC-BY 4.0(署名 + 变更注明,EN_NATIVE notice 承载)、skills/ 区继承 MIT;en/README.md 顶部固定 canonical 声明块(中文为准)。

## 替代方案(被否决)

- **改造 skills-sync-check.py 支持第三侧**——该脚本为恰好双侧设计(路径 / 分支 / 输出类别硬编码),且「逐字节一致」语义与翻译同步本质不同,混入破坏既有语义;两脚本并联跑。
- **en 放 skills/ 本体内**——sync-check 误报「仅项目侧存在」,破坏 ADR-0024 常态分工。
- **git 修订标识做源指纹**——依赖 git 历史、worktree / 分支含混、非 git 副本失效;hash 文件自含可独立复算。
- **段级镜像 / 翻译记忆库**——工程复杂度高,首期文件级够用(改一行整文件重译可接受)。
- **独立 GLOSSARY 术语文件**——第二事实源,双写漂移;CONTEXT 增节单点。
- **CI / git hook 自动门**——仓库无 CI 现状,手动门机制成本最小接入。
- **引擎文件全翻**(skills 3,718 行)——首期工程量 ×2;en SKILL.md 链接指中文原文即可达。

## 后果

- (+) 英文镜像零侵入接轨:既有双侧同步、脱敏门、harness 布局检查全部不受扰动(sync-check 实测仍 0 违规)。
- (+) 漂移三类(结构失配 / 过期 / 断链)+ 缺标记全部可检出、可演示,验收从描述变 CLI 断言。
- (+) 术语单点 + 占位符保持规则,防翻译侧术语漂移与脱敏误译。
- (−) en 文件头 frontmatter 在 GitHub 渲染为顶部表格(已知代价;可等价细化为 HTML 注释载体,改前须用户确认)。
- (−) CHANGELOG append-only 英译长期负担(每发一条追一条,W00 #15 显式接受,备选重访路径已记)。
- (−) 白名单是承诺集:新增可翻组必须同批交付翻译,扩面有一次性成本。

## 关联

- 来源:[feature-i18n-support L0-vision W00 + L1-contract W00](../questionnaires/archive/i18n-support/)(2026-08-22/23,L0 23/23 + L1 21/21 全采纳)。
- 设计套:[L0-vision-i18n-support.md](../design/i18n-support/L0-vision-i18n-support.md) / [L1-contract-en-mirror-governance.md](../design/i18n-support/L1-contract-en-mirror-governance.md)。
- 相关:[ADR-0024](0024-governance-history-split-dual-form.md)(双侧常态分工,本 ADR 第三轴与之正交)、[ADR-0021](0021-design-implementation-deviation-governance.md)(实现偏离路径)、[OD-8](../../docs/OPEN-DECISIONS.md)(引擎副本漂移)、[OD-10](../../docs/OPEN-DECISIONS.md)(分发洁净,全局侧零动作)、[OD-24](../../docs/OPEN-DECISIONS.md)(双副本实验策略)、readme-revamp L0 设计文档(「不做英文 README」已决项,本次重访推翻,留痕见 TODO)。
- 执行:HARNESS-RULES 布局不受影响(en/ 顶级目录非 harness 区);CONTEXT 英文术语对照节已随本 ADR 落位。
