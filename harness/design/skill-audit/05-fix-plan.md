# skill 体系审查修复 · 执行清单(2026-09-27)

> 依据:01/02/03 审查报告 + 问卷 confirm-skill-audit-fix W00(14/14 确认)/W01(Q1-Q6 裁决)+ 04 根因文档。
> 执行纪律:**每条先 grep/Read 定位原文再改**(报告行号可能有偏,以原文为准);改动行遵守 en dash 范围号、`~/` 反引号;**不做清单外改动**。
> 报告误述处理:发现行号/内容不符时按原文修,并在交付说明里记录差异。

## 批次 A · 全局文档(13 项)

| # | 文件 | 修法 |
|---|---|---|
| A1 | `CLAUDE.md:89`(状态节) | 重写为现状快照:日期 2026-09-27;「9 skill 体系稳定」;governance-history-split 已收口(F039–F043 全 passes);i18n 英文镜像首期完成(en 16 件);proj-overview v2 完成(F052)。保留双 canonical 与 ADR-0024 链接语义 |
| A2 | `CLAUDE.md` L59-68 落盘速查表 | 在 grill-Q 行后补一行:`\| grill-with-docs \| 绑库模式:CONTEXT 词条即时更新 / harness/adr/(三条件)/ OPEN-DECISIONS(位置按 HARNESS-RULES 第六节);通用模式零留痕(人要求才写)\|` |
| A3 | `CLAUDE.md` L43-55 协作图 | DOG 节点文字 `DOG["dogfood<br/>产物自验(正交可插入)"]` 改为 `DOG["dogfood<br/>产物自验(非 skill·内嵌机制,正交可插入)"]` |
| A4 | `README.md:160` | 「8 个核心方法论 skill」→「9 个核心方法论 skill」 |
| A5 | `README.md` L46-62 协作图 | DOG 节点同 A3 加「(非 skill·内嵌机制)」 |
| A6 | `TODO.md` | L4 状态行:「proj-overview v2 规格升级中」→「proj-overview v2 完成(F052)」;L5 下一步主线:①proj-overview v2 实现整项移除,原②失忆测试升为①、③哲学挑战一修复包升为②,「其余」保持;L39 F052 行勾销为 `[x]` 并在行尾加「✅(2026-09-26 四步全链,见 STATUS-LOG/commit 654e489)」 |
| A7 | `docs/CONTEXT.md` L160-167 维度表 | 按该表实际列结构补 proj-overview 行(非提问类 / 只读派生人读视图生成 / 无问卷无对抗维度,措辞对齐既有行风格);`en/docs/CONTEXT.md:176` 同步英文行 |
| A8 | `docs/methodology/philosophy_v7.md:299` | 「八个 skill 的共同契约…不是新增第九个总控权威」→「九个 skill 的共同契约…不是新增第十个总控权威」;该处注记块补一行 2026-09-27(注明 proj-overview 入库后计数,出处=skill-audit 修复批);修订记录(L5 附近)补一行;`en/docs/methodology/philosophy_v7.md:306` 同步 |
| A9 | `docs/methodology/practical_v1.md:10` | 「8 个 Claude Code skill」→「9 个」;§8.3 使用时机表补 proj-overview 行(「重载上下文/迷失时生成人读掌控视图」,对齐表内行风格) |
| A10 | `docs/methodology/methodology_v5.md:169` | 「每个环节都有对应的 skill 执行体」→「各环节均有对应方法论承载(环节 3 dogfood 为内嵌自验机制,无独立 skill)」;`en/docs/methodology/methodology_v5.md` 对应句同步 |
| A11 | `docs/OPEN-DECISIONS.md` OD-2 节 | 台账补 proj-overview 注记一行:「proj-overview:无 subagent、无 AskUserQuestion(2026-09-27 skill-audit 实测)」 |
| A12 | `PROJECT-OVERVIEW.md` | 仅手工修两处过期转述:①STATUS-LOG 顶部转述补 09-26 条 ②CHANGELOG「近 5 条」补 09-26 v2 条;**不重生成全文** |
| A13 | `docs/OPEN-DECISIONS.md` OD-23 条 | 核实来源矛盾:查 `harness/questionnaires/archive/` 与 git log,确认 delegate 反馈回路的来源问卷是 grill-questionnaire 压测还是 grill-philosophy-v7-w02,改错的一边使 OD-23 与 delegate SKILL 自述一致 |

注意:A4/A7/A8/A9/A10 对应 en 镜像(`en/README.md:169` 等)一并改;A2/A3/A6/A11/A12/A13 无 en 镜像(不在白名单)。

## 批次 B · 问卷四 skill(17 项)

| # | 文件 | 修法 |
|---|---|---|
| B1 | grill/retro/action 三方 `PROCESSING-RULES.md` 归档节(Q1=C) | 「归档前在文件尾部追加处理报告摘要(落盘文件链接列表)」→「归档前在文件尾部追加**处理报告全文**(每题去向 / 异常 / 逃生舱处置 / 下一波候选 / 覆盖度),顶部保留摘要节(落盘文件链接列表速览)」;action 版保留「行动完成后把执行结果摘要一并追加」附加句 |
| B2 | grill/retro/action 三方 `SKILL.md` | 「尾部附处理报告摘要」类表述同步为「全文」(先 grep「摘要」定位各自实际措辞) |
| B3 | `skills/grill-questionnaire/QUESTIONNAIRE-FORMAT.md` L12 命名行(Q2=C) | init 模式命名行删 LN 枚举,改「`grill-<slug>-w<NN>.md`(NN 从 01 递增)」;L4 头注相应微调(去掉「(L0-vision 等,旧 vision/hld/lld 为别名)」括注,因不再出现 LN 词) |
| B4 | `skills/retro-questionnaire/QUESTIONNAIRE-FORMAT.md` L11 命名行(Q2=C) | 同 B3 改「`retro-<主题>-w<NN>.md`(NN 从 01 递增)」 |
| B5 | `skills/retro-questionnaire/PROCESSING-RULES.md:30-32`(Q2=C) | 映射表「vision 阶段题\|VISION.md」「hld 阶段题\|harness/design/ 的 HLD」「lld 阶段题\|…」三行删除,替换为 retro 实际落盘映射(参照 RETRO-SKELETONS.md:复盘问卷答案 → `docs/retro/<主题>_vN.md`、Action Items → `TODO.md`;以 RETRO-SKELETONS 实际契约为准) |
| B6 | 四方 `PROCESSING-RULES.md`(Q5③) | 在文件头部「引擎复制声明/副本声明」节之后新增小节「## 修订前置检查(OD-8 执行步骤)」:「修改本文件或 QUESTIONNAIRE-FORMAT.md 前,必须先比对其余三方副本(design-Q / grill-Q / retro-Q / action-Q 的同名引擎文件)的对应节:差异属于应同步的修订 → 四方同步;属于本 skill 有意分叉 → 在本 skill DESIGN.md 与 FORK-NOTES.md 声明。二选一并留痕,不允许无声单方修改。」(四方措辞一致,仅副本声明不同) |
| B7 | `skills/design-questionnaire/PROCESSING-RULES.md:37-42` | L38-42 悬空五行补表头「\| 答案类型 \| 落盘目标 \|」+ 分隔行,恢复表格(或并回 L30-35 的 LN 表,二选一,以排版最稳为准) |
| B8 | `skills/design-questionnaire/SKILL.md:78` + `PROCESSING-RULES.md:32-35` | 落盘路径补 feature 段:「`harness/design/`」→「`harness/design/<feature>/`」(与 STAGE-SKELETONS:22/HARNESS-RULES 第七节对齐) |
| B9 | `skills/design-questionnaire/QUESTIONNAIRE-FORMAT.md:87,:121` | 「见规则 15」→「见规则 13」;「按规则 13 居末时」→「按规则 14 居末时」 |
| B10 | `skills/action-questionnaire/QUESTIONNAIRE-FORMAT.md:119` | 「按规则 13 居末时」→「按规则 14 居末时」 |
| B11 | `skills/design-questionnaire/CHANGELOG.md` | 补 2026-09-25 欠账条目(内容语料画像 + MDreader 教训补丁,commit d024d3c,教训日期注记从 SKILL.md 迁来) |
| B12 | `skills/retro-questionnaire/CHANGELOG.md` | 补 2026-09-11 欠账条目(项目搁置/放弃补测式死亡快照触发,commit 08580eb,「2026-09-09 挑战一深钻」日期注记从 SKILL.md 迁来) |
| B13 | `skills/design-questionnaire/SKILL.md:60`、`skills/retro-questionnaire/SKILL.md:26` | 日期注记剥离进 B11/B12 的 CHANGELOG 条目,规则本体只留语义(design 去掉「MDreader 教训 2026-08-26:…拖出 F009 全链返工」日期叙事;retro 去掉「(建议非强制,2026-09-09 挑战一深钻)」) |
| B14 | `skills/retro-questionnaire/SKILL.md:49-50` 主流程末尾 | 补下游衔接一条:「**衔接**:Action Items 中出现 feature 级新需求 → 提议转 design-Q(需设计)或 grill-Q(有工件压测);行动项落地前细节可过 action-Q——新需求/经验回流设计入口(协作图 RETRO→DQ 边)」 |
| B15 | `skills/action-questionnaire/SKILL.md:51`、`QUESTIONNAIRE-FORMAT.md:31` | 「preview 为主、正式题波为兜底」→「confirm-list 为主、正式题波为兜底」(裁决 Q15 术语) |
| B16 | `skills/design-questionnaire/SKILL.md:110`、`skills/grill-questionnaire/SKILL.md:98` 分工表 | 旧三件命名改 LN 表述:「VISION/HLD/LLD」→「层文档(LN 制)」或「L0-vision 等层文档」(对齐各自行文) |
| B17 | grill/retro `FORK-NOTES.md` | 登记两条分叉:①归档粒度本批已四方同步(记录 D34 收口)②命名行本地化(Q2 裁决);grill 侧另补结构分叉声明(无 W00/NN 从 01 递增/命名 grill-<slug>,对齐 retro 的声明粒度) |

附带(共享节措辞统一,报告 01 低3):四方 PR 中 OD 行统一为「(归属见 HARNESS-RULES.md 第六节)」——design/grill 两方改;「『dogfood 修订』节」引用改「设计决策(D13–D22 · dogfood 修订期)」节(报告 01 低4);design SKILL:82-83、PR:24 明显「阶段」残留改「层」(低5,只改清单点名处)。
所有被改 SKILL.md 的 en 镜像(en/skills/<skill>/SKILL.md)同步;引擎文件无 en 镜像。

## 批次 C · 实现治理五 skill(14 项)

| # | 文件 | 修法 |
|---|---|---|
| C1 | `skills/grill-with-docs/SKILL.md` L117-130(Q3=C) | 单 context 示例改 harness 制:`CONTEXT.md`(根)+ `harness/adr/`(0001-…) + OPEN-DECISIONS.md(位置按 HARNESS-RULES 第六节,示例可画根并注明「位置按第六节」);示例前加一行「本 skill 默认绑库模式,以下为 harness 制布局」 |
| C2 | 同文件 L134-146(Q3=C) | 多 context 示例:`CONTEXT-MAP.md` + 各 context `<ctx>/harness/adr/`;「docs/adr/(system-wide)」行改「系统级决策 → 顶层 `harness/adr/`」或按第六节表述,消除 docs/adr 残留 |
| C3 | `skills/grill-with-docs/OPEN-DECISIONS-FORMAT.md:43` | 加一句:「例外:本仓库自身布局例外见 OD-25」(引用宿主仓库语境时) |
| C4 | `skills/doctor-harness/CHANGELOG.md` | 6 处 `../../../harness/` → `../../harness/`(L31、L38、L44×3、L63、L90;先 grep 确认全部实例) |
| C5 | `skills/doctor-harness/HARNESS-RULES.md` 第五节 | 「三检查(问卷命名/ADR 编号/归档位置)」「0 违规无输出」「不强校验分层只报告现状」表述更新为:「四检查(+LN 分层 check_ln_design)+ design/ 分层报告(无条件打印,供人工核对 ADR-0012 判定句);0 违规时仍有报告输出」 |
| C6 | `skills/doctor-harness/SKILL.md` §3、`skills/doctor-harness/DESIGN.md` V7、`scripts/harness-check.py` 模块 docstring | 同 C5 语义四方对齐(脚本 docstring 属代码注释,直接改) |
| C7 | `skills/doctor-harness/HARNESS-RULES.md` 第一节判例清单 | 裸放判例 4 件补全为 7 件(+hld_v1、lld_v1、methodology-audit_v1) |
| C8 | `skills/delegate/SKILL.md` L11/L58、`DESIGN.md` L3/L21/L29、`CHANGELOG.md` L25 | 「『决策下放』OD 条目」→「OD-23(delegate pilot 与可控性验证)」显式编号(与批次 A13 核实结果一致后改;若 A13 查明应改 OD-23 侧则 skill 侧保持「OD-23」即可) |
| C9 | `skills/delegate/templates/delegation-template.md:47` | 「初始枚举定稿(D1–D5)」→「初始枚举定稿(D1–D7)」 |
| C10 | `skills/delegate/SKILL.md:50` | 引号错配:「如『命名引发歧义 1 次」)」→「如『命名引发歧义 1 次』)」 |
| C11 | `skills/doctor-harness/SKILL.md:41` | 「如本次分层落地」→「如 design/ 分层落地」 |
| C12 | `skills/long-running-agent/SKILL.md:175` | 「harness 文件分层见 HARNESS-RULES.md」→「harness 文件分层见 doctor-harness skill 的 HARNESS-RULES.md(本仓库路径 `skills/doctor-harness/HARNESS-RULES.md`)」 |
| C13 | `skills/long-running-agent/SKILL.md`(Q5②) | 治理收尾/DoD 相关节补固定项:「**治理收尾固定项(不可裁剪)**:①TODO.md 对应 feature 块勾销 ②根 CHANGELOG(涉对外可感知变更)与 STATUS-LOG 追加条目 ③本 skill 自身 CHANGELOG(若 skill 有变更)——F052 教训:DoD 漏列 TODO 勾销导致主线状态滞后」(位置与措辞按该文件既有节风格) |
| C14 | `skills/long-running-agent/CHANGELOG.md:19`、`skills/proj-overview/CHANGELOG.md:7` | typo:「harnesss」→「harnesses」;「问卷五份」→「问卷 4 份」(笔误修正,在本次汇总条目中注明) |

所有被改 SKILL.md 的 en 镜像同步;A13 核实结论若影响 C8 措辞,以核实为准。

## 批次 D · 主会话自营(脚本 + OD + 留痕,不在本清单展开)

Q5① `scripts/audit-check.py` 新增;Q5④ `skills-sync-check.py` 双向扫描;OD-30(计数单源化待决)、OD-31(跨会话 handoff 待决)落盘;STATUS-LOG 新条目(含 P4 漏记补注);根 CHANGELOG;各 skill CHANGELOG 汇总条(Q6=C);双侧同步;门禁复跑;问卷处理报告与归档。
