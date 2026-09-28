# 审查报告 03 · 全局文档与 skill 家族实际状态一致性

> 来源:2026-09-27 skill 体系全量审查(三路并行 subagent 之三,只读)。
> 主会话复核注:高 1/2/3 已亲自证实(grep 原文 + feature_list/git 三源互证)。

## 基线核实补充

- skills/ 确为 9 目录;`~/.claude/skills/` 含 shadow(OD-13 裁决暂不入家族,合法)。
- feature_list.json F039-F043 全部 passes=true(含 F042 P3、F043 P4);F052 passes=true。
- 链接抽查 31/31 全部存在(CLAUDE.md/README 指向 docs、harness、skills、scripts、en 的相对链接无一失效)。

## 高(3)

**1. CLAUDE.md 仓库状态节整行过期:8 skill +「P4 待执行」双重失真**
- 位置:`CLAUDE.md:89`
- 原文:「当前(2026-08-20):…+ 8 skill 体系稳定;governance-history-split 治理历史分离迁移执行中…F039 协议 / F040 skill 域 / F041 design 域全绿,P4 全局侧重整待执行」
- 矛盾:① 同文件 L41「9 个 skill 构成 5 环节闭环」;② TODO.md:4「governance-history-split 收口(F039-F043)」+ F042/F043 passes=true。该节被 STATUS-LOG:3 指定为「当前状态快照」,失真被放大。09-25 F051 联动清单(TODO.md:37「CLAUDE 三处」)漏改了状态节。

**2. README(中英)仓库结构行残留「8 个核心(方法论) skill」**
- 位置:`README.md:160`「skills/ 8 个核心方法论 skill(MIT)」;`en/README.md:169`「the 8 core methodology skills (MIT)」
- 矛盾:同文件 README.md:16(目录)与 L74-76 均「9 个核心 skill」,9 张卡片与速查表也是 9;en/README:23/82 同为 9。
- 元发现:TODO.md:37 F051 核验记「『8 个核心 skill』全仓 0 命中」——精确子串 grep 漏掉「8 个核心方法论 skill」变体。

**3. TODO 主线状态与 STATUS-LOG/CHANGELOG/feature_list 矛盾:F052 已完成 vs「规格升级中」**
- 位置:`TODO.md:4`、`:5`、`:39` vs feature_list F052 passes=true、STATUS-LOG 09-26 条、根 CHANGELOG 09-26 v2 条、commit 654e489
- 根因:STATUS-LOG 09-26 条目④「治理收尾」清单不含 TODO 块勾销——F052 的 DoD 本身漏了 TODO 同步。

## 中(4)

**4. CLAUDE.md 落盘路径速查表缺 grill-with-docs 行**
- 位置:`CLAUDE.md:59-68`(表仅 8 行)
- 证据:grill-with-docs 绑库模式自动写 CONTEXT/harness/adr/OPEN-DECISIONS 三类工件,与 grill-Q 行语义相反,是表中独有行为却无行。

**5. CONTEXT「提问维度速查」表缺 proj-overview 行,权威表落后于导览副本**
- 位置:`docs/CONTEXT.md:160-167`(末行仍 long-running / delegate / doctor-harness);en 镜像 `en/docs/CONTEXT.md:176` 同
- 证据:README:145 导览副本已含 proj-overview;CONTEXT.md:158 同步指针明文「修订本表维度列时,README 表必同步(权威 = 本表)」——副本比权威多一行。

**6. philosophy_v7(canonical)家族计数止步「八个」,无 8→9 注记**
- 位置:`docs/methodology/philosophy_v7.md:299`(「八个 skill 的共同契约……不是新增第九个总控权威」;注记仅到 2026-08-19);修订记录(:5)止于 08-19;en 镜像 :306 同
- 证据:methodology_v5:317 有双向注记(9 收为 8;8 增为 9);F051 十处联动清单未含哲学文件——违反 ADR-0018 双文件交叉治理。

**7. practical_v1 计数与使用时机表未随第 9 skill 入库同步**
- 位置:`docs/methodology/practical_v1.md:10`(「8 个 Claude Code skill 是它的执行体」);§8.3 使用时机表无 proj-overview 行
- 证据:README:66/72 把 §8.3 作为「快速上手」指定读物。

## 低(5)

**8.** methodology_v5 §三导语(:169)「每个环节都有对应的 skill 执行体」与 dogfood 非 skill 事实不符(§3.2 环节 3 = dogfood 无 skill;CONTEXT:140「dogfood 是正交方法论」)。三处实质定位一致,仅此 canonical 导语以偏概全。
**9.** 协作图 DOG 节点未标非-skill 身份:CLAUDE.md L43-55(10 节点)、README L46-62(11 节点)——图与正文无数值矛盾,但 DOG 与 9 个 skill 节点视觉无区分。
**10.** OD-2 依赖边界台账缺 proj-overview 核实注记(OPEN-DECISIONS.md:30;实测 proj-overview 无 subagent、无 AskUserQuestion 使用,README:150「subagent 仅 design-Q / grill-Q」成立——结论不受影响,仅台账缺行)。
**11.** PROJECT-OVERVIEW 生成当日即过期两处 summary:STATUS-LOG 顶部转述列 09-25 为最新(实际 09-26)、CHANGELOG「近 5 条」缺 09-26 v2 条(F052 步骤顺序③重生成→④治理收尾所致)。
**12.** STATUS-LOG 缺 governance-history-split P4 收口条目(08-19 与 08-23 条之间无 F042-F043 收口条;证据由 feature_list/TODO/CHANGELOG 间接承载)。

## 专项结论(无发现)

- **shadow 归属**:一致无缺口。OD-13(已收口)裁决「暂不入 skill 家族」;TODO.md:165 明文「仓库 skills/ 暂不放置(pilot 期不进入分发面)」。CLAUDE/CONTEXT 不提 shadow 符合决策;shadow 全局侧持有 DESIGN.md 不违反 ADR-0024(该分工只约束家族 9 skill)。
- **三态一致性**:「认知状态三态」三处表述一致(CLAUDE.md:70、CONTEXT:149、methodology_v5 §4.3:422 与 §3.3.1 注:331)。
- **README 对外描述**:除发现 2 外一致。
- **引用抽查**:31/31 存在。

## 总计:高 3 / 中 4 / 低 5

## 共性根因(报告自带)

1. 「家族规模/主线状态」类事实在 CLAUDE.md 状态节、TODO 头部、philosophy_v7、practical_v1、README 结构树五处双写,联动清单漏项即漂移——与 CONTEXT「两类漂移」自述病理同构。
2. 验收门 grep 用精确子串存在变体漏网,核验模式宜宽松化或脚本化。
