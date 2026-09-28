# 审查报告 02 · 实现期/治理类五 skill(long-running / delegate / grill-with-docs / doctor-harness / proj-overview)

> 来源:2026-09-27 skill 体系全量审查(三路并行 subagent 之二,只读)。
> 主会话复核注:高-1 的行号已修正——docs/adr/ 示例实际在 `skills/grill-with-docs/SKILL.md` L117-130(单 context)与 L134-146(多 context),矛盾本身证实。

## 正面结论

- frontmatter:5 个 name 均与目录名一致(含 long-running-agent);description 与正文功能相符。
- 双侧同步:5 个 SKILL.md、HARNESS-RULES.md、MIGRATION-FLOW.md、grill-with-docs 三个 FORMAT、delegate 两个 template 全部与 `~/.claude/skills/` 逐字节一致;CHANGELOG 仅项目侧;DOGFOOD-LOG.md 仅全局侧(doctor-harness、proj-overview 各一);5 skill 均无 FORK-NOTES 且与 CHANGELOG「无分叉」声明一致。
- 落盘路径与约定一致(long-running/delegate/doctor-harness/proj-overview)。
- doctor-harness 专项:HARNESS-RULES 第九节确为「治理历史布局」;MIGRATION-FLOW 7 步与 SKILL.md §2 一致;design/ 裸放 7 文件 = 合规历史遗留(harness-check 该报告为 informational,不计入 violations,第七节 legacy 豁免覆盖)。
- grill 退役叙事全仓一致(OD-12、CONTEXT、methodology §3.3.1、CLAUDE.md、README、waste/skills/grill/、grill-with-docs 口径统一);全局侧已无 grill 目录。
- 交叉引用抽查(HARNESS-RULES 第六节、第九节、L1-contract-gov-history-split、OD-12/13/15/17/26、归档问卷、docs/retro/designq-digital-levels_v1)有效。
- 流程图合规:5 skill 文档内无 ASCII 流程/架构图(仅目录树 `├──`,非铁律 7 禁区)。

## 高(1)

**高-1|grill-with-docs 规则本体内部自相矛盾:ADR 落点两套并存(docs/adr/ vs harness/adr/)**
- 位置:`skills/grill-with-docs/SKILL.md` L117-130、L134-146(结构示例)vs `ADR-FORMAT.md:3`、`SKILL.md:148`
- 证据:单 context 示例画 `docs/adr/`(0001-event-sourced-orders.md 等)+ `docs/OPEN-DECISIONS.md`;多 context 示例又画系统级 `docs/adr/` + 各 context `src/ordering/harness/adr/` 混用;而 ADR-FORMAT.md L3 明言「ADRs live in `harness/adr/`」,SKILL.md L148 也说「If no `harness/adr/` exists, create it when the first ADR is needed」。疑为 mattpocock 上游原文(docs/adr)适配 harness 制时未清干净。

## 中(5)

**中-1|CLAUDE.md「落盘路径速查表」缺 grill-with-docs 行**
- 位置:`CLAUDE.md` L59-68(8 行表覆盖 9 skill)
- 核实:grill-with-docs 实际落盘 = 绑库模式(默认)即时更新宿主项目 CONTEXT.md / harness/adr/(懒创建)/ OPEN-DECISIONS.md(位置引 HARNESS-RULES 第六节);通用模式零留痕。速查表其他 8 skill 均有行,唯缺它。

**中-2|doctor-harness/CHANGELOG.md 6 处相对链接多一层,全部断链**
- 位置:L31、L38、L44(×3)、L63、L90 用 `../../../harness/...`(从 skills/doctor-harness/ 解析出仓库外);同文件 L9、L17 用正确的 `../../harness/...`。断链回归(MIGRATION-FLOW 第 4 步「存量断链登记豁免」)未见这批登记。

**中-3|delegate 的反馈落点「决策下放」OD 条目不存在(悬空引用)**
- 位置:`skills/delegate/SKILL.md` L11、L58;`DESIGN.md` L3、L21、L29;`CHANGELOG.md` L25
- 证据:全仓 grep「决策下放」在 OPEN-DECISIONS.md 0 命中;实际相关条目为 OD-23「delegate pilot 与可控性验证」(来源写 grill-philosophy-v7-w02 Q5/Q6,与 SKILL 自述「grill-questionnaire 压测产出」不一致)与 OD-13(有效)。

**中-4|「三检查 / 0 违规无输出」文档表述已漂移于脚本实际行为(四处同源失真)**
- 位置:`skills/doctor-harness/HARNESS-RULES.md` 第五节、`SKILL.md` §3、`DESIGN.md` V7、`scripts/harness-check.py` docstring
- 证据:四处均称「三检查(问卷命名/ADR 编号/归档位置)」「0 违规时无输出」「脚本不强校验分层只报告现状」;实际脚本已实现第 ④ 类违规检查 check_ln_design(LN 层文件裸放 design/ 根、feature 目录缺 L0、LN 命名偏离 → 计入 violations),且文本模式无条件打印 design/ 分层报告——0 违规仍有输出。

**中-5|TODO.md 的 F052 状态滞后于 STATUS-LOG/CHANGELOG/git**
- 位置:`TODO.md` L4-5、L39 vs STATUS-LOG 顶部 F052 条、proj-overview CHANGELOG 09-26 条、commit 654e489
- 证据:三源均记 F052 四步全绿;TODO L39 仍为 `[ ]`,头部仍写「v2 规格升级中」。根因:F052 治理收尾 DoD 清单不含 TODO 块勾销。

## 低(8)

**低-1** `skills/delegate/templates/delegation-template.md` L47:Changelog 示例「初始枚举定稿(D1–D5)」与同表 D1–D7 不符。
**低-2** `skills/delegate/SKILL.md` L50 引号错配:「如『命名引发歧义 1 次」)」全角后引号应为 `」`。
**低-3** `skills/doctor-harness/CHANGELOG.md` 条目时序倒挂:「08-11 至 08-19」条目排在三条 08-20 之上;08-16 三条排在 08-17 之上(与追加式新在上惯例不一致)。
**低-4** `skills/doctor-harness/HARNESS-RULES.md` 第一节裸放判例清单过时:列 4 件,实际裸放 7 件(漏 hld_v1、lld_v1、methodology-audit_v1)。
**低-5** `skills/long-running-agent/SKILL.md` L175:「harness 文件分层见 HARNESS-RULES.md」不带路径,宿主项目读者无法定位。
**低-6** `skills/doctor-harness/SKILL.md` §2 L41:「如本次分层落地」——2026-08-08 首次迁移现场措辞残留在活规则中。
**低-7** `skills/grill-with-docs/OPEN-DECISIONS-FORMAT.md` L43:harness 仓一律「place it at harness/OPEN-DECISIONS.md」,未交叉引用 OD-25(本仓库例外);另 CHANGELOG「影响:SKILL.md#判定」锚点「判定」非节标题。
**低-8** 文字瑕疵:`skills/long-running-agent/CHANGELOG.md` L19「Effective harnesss」(三 s);`skills/proj-overview/CHANGELOG.md` L7「问卷五份归档」实为 4 份。

## 总计:高 1 / 中 5 / 低 8
