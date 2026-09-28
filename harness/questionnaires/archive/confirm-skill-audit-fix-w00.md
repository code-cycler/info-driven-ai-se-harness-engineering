---
mode: feature
wave: 0
stage: confirm
created: 2026-09-27
status: archived
---
# 问卷 confirm W00 · 细节确认清单(AI 汇报理解,人核对)

> **本波是细节确认清单**(独立 wave 0):把 AI 对本次行动细节的理解逐条列出,人只做「对/不对」核对。
>
> **作答规则**:
>
> - 勾 `[x]` = **理解正确**(按该理解执行)
> - 留空 `[ ]` = **理解有误或要改** → 该要点转正式题深究(或小波直接问)
> - 本波**不用 🤔**(对/不对二选一,无中间态);「大体对但要改一两处」→ 留空,转正式题时在深究题里给正确值
>
> 来源标注于〔〕:**〔推断〕= AI 填的,重点核对**;〔用户原话 / 代码 / 文档〕= 有据。

## 细节确认清单

### 目标

- [X] **1 修复范围 = 全数 41 条 + 1 条主会话自查**:三份审查报告去重合并后的高 6 / 中 17 / 低 18 全部立即修复,含低危(不等「下次顺带」);外加主会话发现的 skills-sync-check.py 双向扫描盲区(以「确认补盲/登记待决」方式处理,详见 W01 Q5)。〔用户原话「全数修复」+ 审查汇总报告〕
- [X] **2 根因拷问是本次交付物的一半**:产出「为什么 doctor-harness 与本项目工作循环留下这些问题」的分析(不是只修条目),连同预防治理方案一并落盘留痕,候选去向 = 归档问卷处理报告 + OPEN-DECISIONS(机制级待决项)。〔用户原话「拷问为什么…有什么办法预防和治理」〕
- [X] **3 修复语义 = 纠偏,不越界**:只修 41+1 条清单内的问题;清单外的「顺手改进」一概不做(含发现的 typo 仅清单内 2 处:long-running CHANGELOG「harnesss」、proj-overview CHANGELOG「五份→实为 4 份」)。〔推断,据用户「全数修复」限定为审查发现〕

### 输入

- [X] **4 高危 6 条已由主会话亲自逐条复核证实**(非仅采信 subagent):CLAUDE.md:89 过期、README:160/en:169 残留「8 个」、TODO F052 滞后(与 STATUS-LOG/CHANGELOG/git 654e489 三源互证)、D34「全文 vs 摘要」漂移、grill FORMAT L4/L12 自相矛盾 + retro PR LN 旧词、grill-with-docs 结构示例 `docs/adr/` vs `harness/adr/` 双说(行号修正为 SKILL.md L117-130/L134-146)。〔主会话实测 grep/Read〕
- [X] **5 中低危 31 条按 subagent 报告执行,逐条「先读原文再改」**:修复中若发现报告误述(行号偏/内容不符),以原文为准修正并在处理报告记录差异,不机械照改。〔推断——仅高危与部分中危经主会话复核,其余信任报告但动手前必读原文〕

### 输出

- [X] **6 修复后全部门禁复跑**:`skills-sync-check.py` 0 违规(涉 skill 改动双侧逐字节同步到 `~/.claude/skills/`)、`i18n-check.py` 0 违规(受影响 en 镜像同步)、`desensitize.py` 0 命中、`harness-check.py` 可跑。〔铁律 8 + i18n 门〕
- [X] **7 留痕四件套**:① 各被改 skill 的 CHANGELOG 补条目(含 design-Q 补 09-25、retro-Q 补 09-11 两笔欠账)② 根 CHANGELOG 一条 ③ STATUS-LOG 一条 ④ 本问卷归档(处理报告含 41+1 条逐条去向)。〔仓库治理惯例〕
- [X] **8 文档原地修订 + 版本语义不变**:按仓库既有惯例(文档类原文件修订,不建 _vN 副本;版本号约束针对脚本类)。〔推断,据仓库文档修订惯例〕

### 约束

- [X] **9 已决项语义不动,修法须过协议**:D34/D38 引擎漂移的修复不违反「禁止擅自统一/抽取共享文件」——本批修复或「四方同步」或「四方 DESIGN 声明分叉」,方向由 W01 Q1/Q2 裁决;ADR-0011(harness 硬编码)、ADR-0024(形态分工)等裁决不在触碰范围。〔OD-8 已决约束〕
- [X] **10 排版与图示合规随修订生效**:改动行遵守 en dash 范围号、`~/` 反引号、mermaid;CLAUDE.md/README 协作图 DOG 节点补「非 skill」标识属低危清单内条目。〔铁律 7 + 全局排版规范〕

### 边界

- [X] **11 三处「治理机制变更」不在本批擅自实施,进 W01 裁决**:① 家族计数/主线状态单源化(动 CLAUDE/README/philosophy 多文件结构)② 验收 grep 宽松化/脚本化 ③ sync-check 双向扫描扩展——若裁决「做」,哪些本批做、哪些进 OPEN-DECISIONS 由 W01 Q4/Q5 定。〔推断——机制变更属决策,不是修复〕
- [X] **12 en/ 白名单外文件不动;waste/ 目录不进不出**;PROJECT-OVERVIEW 的两处过期 summary 按清单修(C11),不触发整份重生成。〔审查报告 + 全局废弃目录规则〕

### 依赖

- [X] **13 双侧可写性**:全局侧 `~/.claude/skills/` 本次为「改」非「删」,不触发删除前 diff 抢救流程;改后 sync-check 复验。〔铁律 8〕
- [X] **14 审查原始报告为修复依据,随归档沉淀**:三份 subagent 报告全文(高 6/中 5+9+4/低 18 明细)将作为附录写入本问卷处理报告,防「修完即失据」。〔推断——原始信息不丢失〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

# 处理报告(2026-09-27,agent 生成;skill-audit 修复批)

## confirm-list 统计

- 确认正确:14 / 14(全勾,零留空)
- 留空纠正:0;转 W01 深究:0
- W01 六题裁决:Q1=C(D34 四方同步全文制)/ Q2=C(副本本地化命名)/ Q3=C(grill-with-docs 示例 harness 制)/ Q4=C(单源化落 OD-30)/ Q5=①②③④⑤全选(治理包五项全落地)/ Q6=C(每 skill CHANGELOG 一条汇总)
- 逃生舱:0;异常(单选多勾/必答未答):0
- W01 补充声明新需求:跨会话强制 handoff → 分析回应落 [harness/design/skill-audit/04-root-cause-and-governance.md](../../design/skill-audit/04-root-cause-and-governance.md) §五 + OD-31 待决

## 逐条去向(41+1 条,按执行批次)

### 批次 A · 全局文档(subagent 执行,13 项)

| 发现 | 去向 |
|---|---|
| 高1 CLAUDE.md 状态节过期 | ✅ 重写为 2026-09-27 快照(9 skill/gov-split 收口/i18n 完成/F052 完成);实际行 L90 |
| 高2 README 中英「8 个核心方法论 skill」 | ✅ README.md:160 + en/README.md:169 → 9 |
| 高3 TODO F052 滞后 | ✅ L4/L5 刷新 + L39 勾销 [x] + 行尾核验注(commit 654e489 已核) |
| 中C4+B中1 速查表缺 grill-with-docs 行 | ✅ CLAUDE.md 表补行(grill-Q 行后) |
| 中C5 CONTEXT 维度表缺 proj-overview | ✅ docs/CONTEXT.md + en 镜像补行 |
| 中C6 philosophy_v7 计数止步八个 | ✅ 「九个/第十个」+ 注记 + 修订记录 + en 三处 |
| 中C7 practical_v1 未同步第 9 skill | ✅ 计数 + §8.3 表补行 + en 两处 |
| 中C8 methodology_v5 §三导语 | ✅ 改「各环节均有对应方法论承载(dogfood 内嵌机制)」+ en |
| 中C9 DOG 节点未标非 skill | ✅ CLAUDE.md + README(中英)图节点加「非 skill·内嵌机制」 |
| 中C10 OD-2 台账缺 proj-overview | ✅ 补注(无 subagent/AskUserQuestion 实测) |
| 中C11 PROJECT-OVERVIEW 当日过期 | ✅ 两处转述手工修正(STATUS-LOG 09-26 条/CHANGELOG 近 5 条),未重生成 |
| 中C12 STATUS-LOG 缺 P4 收口条 | ✅ 以本次 STATUS-LOG 新条目内补注方式留痕(不伪造时序) |
| 中B中3+中3 OD-23 来源矛盾 | ✅ A13 核实:两来源各自成立(skill 本体=grill-Q 压测 2026-07-25;OD-23=grill-philosophy-v7-w02 Q5/Q6),OD-23 条目内补注双来源,两侧原文未删 |

### 批次 B · 问卷四 skill(subagent 执行,17 项 + 附带 3)

| 发现 | 去向 |
|---|---|
| 高4 D34 漂移(全文 vs 摘要) | ✅ Q1=C:四方归档规则统一「处理报告全文 + 顶部摘要节」;三 SKILL「摘要→全文」;FORK-NOTES 登记;本报告本身即新规则首次应用 |
| 高5 LN 副本漂移 | ✅ Q2=C:grill FORMAT L12 → `grill-<slug>-w<NN>`(L4/L12 矛盾消除);retro FORMAT L11 → `retro-<主题>-w<NN>`;retro PR 映射三行旧词按 RETRO-SKELETONS 契约替换;两方 FORK-NOTES 登记 |
| 中A1 映射表结构破损 | ✅ 悬空五行并回 LN 主表,单表头连续 9 行 |
| 中A2 落盘路径漏 feature 段 | ✅ SKILL:78 + PR 四处补 `<feature>/` |
| 中A3+A4 规则编号引用错位 | ✅ design FORMAT ×2(15→13、13→14)+ action FORMAT ×1(13→14) |
| 中A5/A6 CHANGELOG 欠账 | ✅ design 补 2026-09-25 条 / retro 补 2026-09-11 条(四要素格式,commit 出处已核) |
| 中A7 日期注记回流 | ✅ 两处剥离迁入上述欠账条目,规则本体只留语义 |
| 中A8 retro 无下游衔接 | ✅ 主流程补第 6 条衔接(RETRO→DQ 协作边) |
| 中A9 preview 废弃称谓 | ✅ ×3(SKILL:51/FORMAT:31/description 中英第三处同类延伸,主会话补) |
| 低A1 分工表旧三件命名 | ✅ design/grill 各 1 行 LN 化 + grill 骨架行同类延伸(主会话补) |
| 低A2 FORK-NOTES 粒度 | ✅ grill 补 3 条结构分叉声明,对齐 retro 粒度 |
| 低A3 OD 行措辞漂移 | ✅ design/grill 统一「(归属见 HARNESS-RULES 第六节)」 |
| 低A4 节名引用 | ✅ 按 DESIGN 实际节名「设计决策(D13–D22 · dogfood 修订期)」修正 |
| 低A5 阶段/层混用 | ✅ design SKILL ×3 + PR ×1(清单点名处) |

### 批次 C · 实现治理五 skill(subagent 执行,14 项)

| 发现 | 去向 |
|---|---|
| 高6 grill-with-docs ADR 落点双说 | ✅ Q3=C:单/多 context 双示例统一 harness 制;OPEN-DECISIONS 位置按第六节并注 OD-25 例外;行号实证 L117-146 |
| 中B中2 doctor CHANGELOG 断链 | ✅ 实测 7 处 `../../../harness/` 全改 `../../`;范围外同类 1 处 `../../../docs/`(主会话裁决补修) |
| 中B中3 delegate 悬空引用 | ✅ ×6 处改显式「OD-23」(SKILL ×2/DESIGN ×3/CHANGELOG ×1) |
| 中B中4 四处同源失真 | ✅ HARNESS-RULES 第五节/SKILL §3/DESIGN V7/harness-check.py docstring 四处对齐实测行为(四检查+分层报告无条件打印) |
| 中B中5 TODO 滞后(=高3) | ✅ 同高3 |
| 低B1 模板 D1–D5 | ✅ → D1–D7 |
| 低B2 引号错配 | ✅ 按文件「」风格修复(实际字符与报告描述略异,按原文) |
| 低B3 CHANGELOG 时序倒挂 | ✅ 存量不重排,本次条目内声明「自本条起统一按记录日期新在上」 |
| 低B4 判例清单过时 | ✅ 4 件 → 7 件 |
| 低B5 引用无路径 | ✅ 补 doctor-harness 定位 + 本仓库路径 |
| 低B6 「本次」残留 | ✅ → 「如 design/ 分层落地」 |
| 低B7 OD-25 缺引 | ✅ FORMAT 补例外注 |
| 低B8 typo ×2 | ✅ harnesss→harnesses;五份→4 份 |
| Q5② 治理收尾固定项 | ✅ long-running §10 新增不可裁剪固定项(F052 教训) |

### 批次 D · 主会话自营

| 项 | 去向 |
|---|---|
| 主会话自查 sync-check 盲区 | ✅ Q5④:双向扫描 + FAMILY_MARKERS 分流(全局独有含家族特征文件→违规;个人 skill→汇总提示);shadow 登记 OD-13 例外 |
| Q5① audit-check.py | ✅ 新增(计数宽松模式断言 + TODO vs feature_list 断言);自测两轮修正两个误报(个人 skill 误报为违规/TODO 历史行误报) |
| Q4 计数单源化 | ✅ OD-30(open,重访触发三条) |
| W01 补充声明 handoff | ✅ OD-31(open,候选 A/B/C + 倾向 A+C)+ 04 文档 §五分析回应 |
| Q5⑤ 审查知识沉淀 | ✅ harness/design/skill-audit/ 五件(三报告 + 根因拷问 + 修复计划) |
| Q6 CHANGELOG 记法 | ✅ 9 skill 各一条汇总 + 根 CHANGELOG 中英双落 + STATUS-LOG 一条(含 P4 补注) |
| 双侧同步 | ✅ 22 个规则本体文件拷全局侧;收尾发现:全局侧 proj-overview/DESIGN.md 被某次 dogfood 错当生成留痕载体(某外部项目 @c8e8202),已抢救迁移至全局侧 DOGFOOD-LOG.md 并删除错位文件(铁律 8「不一致先抢救」流程) |

## 覆盖度(隐式骨架六要素)

目标 ✅(41+1 全数修复 + 根因拷问落盘 04)/ 输入 ✅(高危主会话复核 + 中低危先读原文)/ 输出 ✅(留痕四件套 + 门禁复跑)/ 约束 ✅(已决项语义未动,OD-8 走声明或同步)/ 边界 ✅(清单外仅三处同类延伸,均主会话裁决并记录:grill 骨架行 LN 化/action description preview/doctor L90 docs 断链)/ 依赖 ✅(双侧同步完成)。

## 下一波候选

1. proj-overview 漂移自检扩到 STATUS-LOG/CHANGELOG 转述行(低11 的 skill 规格面)——已记 04 §六,OD 挂账,下次该 skill 规格修订时处理。
2. OD-31 跨会话 handoff 若决定实施 → design-Q 立项(Stop hook + pre-commit 双闸)。
3. audit-check 后续扩展:规则编号引用有效性断言(04 §六之 doctor 自身体检议题)。

## 报告误述差异汇总(三批次 + 主会话,计 15 条)

行号偏移 3 处(CLAUDE.md:89→90、附带3 SKILL:82-83→82、grill-with-docs 示例区间);计数偏差 2 处(断链 6→7 实为 8 含范围外 1、问卷五份→4);字符与报告描述略异 1 处(C10 引号);同类延伸主会话裁决 3 处;其余为合理执行裁量(B1 补全 design 完整句/B3 slug 定义补回/B5 双落点按契约/A6 日期标注更新/A13 双来源并存)。明细见三批次交付报告(对话存档)与各 skill CHANGELOG 09-27 条。
