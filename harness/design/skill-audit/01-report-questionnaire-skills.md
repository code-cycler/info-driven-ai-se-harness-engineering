# 审查报告 01 · 问卷类四 skill(design-Q / grill-Q / retro-Q / action-Q)

> 来源:2026-09-27 skill 体系全量审查(三路并行 subagent 之一,只读)。
> 主会话复核注:高危 2 条(D34/D38 漂移)已亲自 grep 证实;中低危按本报告执行,动手前以原文为准。

## 正面结论

- 4 个 SKILL.md 的 `name` 均与目录名一致,frontmatter YAML 全部可解析,description 357–656 字符、触发词与正文一致。
- 双侧同步健康:4 skill 全部规则本体与 `~/.claude/skills/` 同名文件 `cmp` 逐字节一致,`scripts/skills-sync-check.py` 0 违规。
- 外部引用抽查(HARNESS-RULES 第四/六/七/八/九节、OD-8/11/13/14/19/26/27/28、ADR-0023、STAGE-SKELETONS 第二部分/总则、GRILL-SKELETON「落盘契约」、RETRO-SKELETONS 四节、CONTEXT「推进受挫谱系」、各 DESIGN 指向的归档问卷路径)全部真实存在且节号对得上。

## 高(2)

**高-1|OD-8 四方考量协议违反:08-20 引擎修订(D34)未同步三副本且零声明**
- 位置:`skills/design-questionnaire/DESIGN.md:89`(D34)+ 三副本 PROCESSING-RULES 归档节
- 证据:design-Q 于 2026-08-20(grill-design-q 三透镜压测 Q9-A)把 canonical 归档规则改为「追加处理报告全文」(`design-questionnaire/PROCESSING-RULES.md:82`),但 `grill-questionnaire/PROCESSING-RULES.md:80`、`retro-questionnaire/PROCESSING-RULES.md:75`、`action-questionnaire/PROCESSING-RULES.md:74` 仍是「追加处理报告摘要」;三份 SKILL.md 同样仍写「尾部附处理报告摘要」(grill:79、retro:48、action:78)。design-Q 的「引擎复制声明」明文要求「修改本 skill 引擎时,必须考量是否同步另三方副本,并在四处 DESIGN.md 各记一笔」;对比同批其他修订(08-03/08-08/08-18 条目均写明「四份副本同步」),D34 既未同步、也未在任何一方 DESIGN/FORK-NOTES/CHANGELOG 声明「仅 canonical」。属未声明的悄悄漂移。

**高-2|LN 制(D38)半同步:retro 副本漂移完全未声明,grill 副本文件内自相矛盾**
- 位置:`retro-questionnaire/PROCESSING-RULES.md:30-32`;`grill-questionnaire/QUESTIONNAIRE-FORMAT.md:4` vs `:12`;`retro-questionnaire/QUESTIONNAIRE-FORMAT.md:11`
- 证据:① retro PR 落盘映射仍为 pre-LN 旧词——「| vision 阶段题 | VISION.md(位置按项目现状:根目录或 docs/) |」等三行,且 retro 副本头部只有泛化副本声明,没有 grill 那句「下表 vision/hld/lld 行是 design-Q 词汇,本 skill 不用」的免责注,retro 的 DESIGN/FORK-NOTES/CHANGELOG 也无此漂移记录;② grill FORMAT 第 4 行头注说「LN 层名(L0-vision 等)是 design-Q 的词汇,本 skill 不用」,第 12 行命名却写「stage ∈ LN 层名(L0-vision | L1-contract | L2-build | 自声明)」,同文件两处直接矛盾;retro FORMAT 第 11 行有同样的 LN 命名行且全文无任何免责,与 FORK-NOTES「stage 恒 retro」相左。action-Q 已彻底本地化(无 stage 行、命名 confirm-<slug>),无此问题。

## 中(9)

**中-1|canonical 引擎落盘映射表 markdown 结构破损**
- 位置:`design-questionnaire/PROCESSING-RULES.md:37-42`
- 证据:D38 修 LN 制时,LN 表之后插入独立段落「旧三件命名(VISION/HLD/LLD)仅存量文件豁免;新产物一律 LN 制。」(L37),随后五行映射(L38-42:术语/ADR/OD 单向门/OD 双向门/行动项)悬空——无表头无分隔行,GFM 不会渲染为表格。

**中-2|design-Q 落盘路径两处写法不一:漏 `<feature>/` 段**
- 位置:`design-questionnaire/SKILL.md:78`、`PROCESSING-RULES.md:32-35` vs `STAGE-SKELETONS.md:22`
- 证据:SKILL L78 写「层文档…→ harness/design/」、PR 映射写「harness/design/ 的 L0-<功能>.md」,而 STAGE-SKELETONS 总则写「目录 harness/design/<feature>/」,HARNESS-RULES 第七节与本仓实际布局均为子目录。

**中-3|design FORMAT 规则编号引用失效(两处)**
- 位置:`design-questionnaire/QUESTIONNAIRE-FORMAT.md:87`、`:121`
- 证据:W01 模板 L87「预勾选 = opt-in 开关(默认关;见规则 15)」——规则 15 现为「问题级排序(OD-14 试点)」,预勾规则在规则 13;规则 4 L121「推荐选项按规则 13 居末时」——选项级排序是规则 14,规则 13 是 preview。

**中-4|action FORMAT 规则 4 引用在本副本编号体系下错位**
- 位置:`action-questionnaire/QUESTIONNAIRE-FORMAT.md:119`
- 证据:规则 4 写「推荐选项按规则 13 居末时」,但 action 副本规则 13 = confirm-list、选项级排序 = 规则 14——从 design-Q 原样继承的陈旧引用。

**中-5|design CHANGELOG 缺 09-25 条目**
- 位置:`design-questionnaire/CHANGELOG.md`(尾条目 2026-08-20)vs `SKILL.md:60`
- 证据:SKILL.md L60 于 2026-09-25(commit d024d3c)写入「内容语料画像 + MDreader 教训补丁」规则本体变更,CHANGELOG 无对应条目。

**中-6|retro CHANGELOG 缺 09-11 条目**
- 位置:`retro-questionnaire/CHANGELOG.md`(尾条目 2026-08-20)vs `SKILL.md:26`
- 证据:SKILL 触发节于 2026-09-11(commit 08580eb)新增「项目搁置/放弃:补测式死亡快照」触发,CHANGELOG 无条目。

**中-7|带日期治理注记回流规则本体(违背 ADR-0024 P1 剥离纪律)**
- 位置:`design-questionnaire/SKILL.md:60`、`retro-questionnaire/SKILL.md:26`
- 证据:08-20 治理历史迁移刚把带日期注记剥离进 CHANGELOG,之后新增两处又内嵌日期教训——design L60「MDreader 教训 2026-08-26」、retro L26「(建议非强制,2026-09-09 挑战一深钻)」。

**中-8|retro SKILL 主流程末尾无下游衔接**
- 位置:`retro-questionnaire/SKILL.md:49-50`(主流程第 5 步「终止」即止)
- 证据:项目 CLAUDE.md 协作图约定「RETRO -.->|新需求/经验| DQ」且衔接协议详见各 SKILL.md 主流程末尾;design-Q/grill-Q/action-Q均有末尾衔接,唯 retro 无。

**中-9|action-Q 残留已裁决废弃的「preview」称谓**
- 位置:`action-questionnaire/SKILL.md:51`、`QUESTIONNAIRE-FORMAT.md:31`
- 证据:两处均写「preview 为主、正式题波为兜底」,而 DESIGN.md 裁决 Q15 明确「preview 术语漂移 → 更名『细节确认清单(confirm-list)』」,FORK-NOTES 分叉 1 亦同。

## 低(5)

**低-1** 分工表仍用旧三件命名:design `SKILL.md:110` 落盘行「VISION / HLD / LLD / ADR / OD / CONTEXT」、grill `SKILL.md:98` design-Q 列同。
**低-2** FORK-NOTES 声明粒度不一:retro 明列「无 preview/W00、命名、stage 恒 retro」,grill 只列 3 条未收「无 W00/NN 从 01 递增/命名 grill-<slug>」。
**低-3** 四副本共享节注记措辞漂移未声明:retro/action PR 的 OD 行写「(归属见 HARNESS-RULES.md 第六节)」,design/grill 写「(项目固有,路径不动)」。
**低-4** 节名引用对不上:design `SKILL.md:100` 说 dogfood 结果「记入 DESIGN.md 的『dogfood 修订』节」,实际节名「设计决策(D13–D22 · dogfood 修订期)」。
**低-5** 「阶段/层」术语混用:design `SKILL.md:82-83`、PR `:24` 等处仍用「阶段」,与 LN 制「层」并存。

## 总计:高 2 / 中 9 / 低 5
