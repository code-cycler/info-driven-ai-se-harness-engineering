---
stage: grill
wave: 1
created: 2026-08-08
status: pending
---
# 压测问卷 · doctor-for-harness 设计套 W01

> **工件**:[VISION](../design/doctor-harness/VISION.md) + [HLD](../design/doctor-harness/HLD.md) + [LLD](../design/doctor-harness/LLD.md) + [ADR-0012](../adr/0012-harness-layering-rule.md) + [ADR-0013](../adr/0013-harness-layering-migration.md)。
> **模式**:代码库绑定(绿地子模式变体——设计期文档 + 已实现脚本/skill,可对照 F017–F020 实现)。D7「现实」= 实现现状(scripts/harness-check.py + skills/doctor-harness/ + F019 迁移记录)。
> **范围**:doctor-for-harness 设计套完整性 + 设计 vs 实现一致性。
>
> **填写规则**:
>
> 1. 每题勾选 `[x]`;★ = AI 判断(认定/不认定漏洞);opt-in 关不预勾
> 2. 🤔 逃生舱:勾了 = 定不了 → 降风险协议
> 3. ✍️ 自定义(尤其"不认定"时给理由、"部分认定"时给修订方向)
> 4. 排序:非推荐在前 → 🤔 倒数第二 → 推荐最后

## Q1. (D5 盲点 + D7 现实矛盾) 校验脚本不查 design/ 分层——核心规则无校验   [落盘: 处理报告]

<出题依据:核实 scripts/harness-check.py 只有 3 个检查函数(check_naming / check_adr_sequence / check_archive_location),**无 check_design_layering**。但 doctor-harness 的核心规则是 ADR-0012 的 design/ 分层判定句。VISION/HLD 声称校验脚本检查「布局合规」,实际脚本只查命名/ADR编号/归档位置,**不查分层是否合规**——即「feature 级设计是否建了子目录、全局设计是否裸放」无任何自动校验。设计声明的核心能力(规则权威化)与其校验工具脱节。>

- [ ]  A. 认定漏洞 —— 核心规则(分层)无校验,「布局合规校验」名不副实;新 feature 不分层时脚本不会报
- [ ]  B. 不认定 —— 分层判定句(可独立引用/冲突)需要语义判断,非格式检查,脚本难自动化;靠人工 + 文档即可
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定脚本能力缺口,但分层判定确实难全自动化;缓解 = 脚本补「design/ 下文件清单 + 标注裸放/子目录」的**报告模式**(不判定对错,只列出现状供人审),而非强校验

## Q2. (D7 现实矛盾) HARNESS-RULES 实际 5 节 vs LLD 声称「四节」   [落盘: 处理报告]

<出题依据:核实 skills/doctor-harness/HARNESS-RULES.md 实际有 5 个 `##` 节(分层定义/归属判据/命名规范/归档规则/布局合规校验);但 LLD.md 行 13/22/62 三处写「起草四节规则」「grep 四节标题」。实现比设计多一节(第五节「布局合规校验」是 F017 实际加的)。DoD「grep 四节标题」会与实际 5 节不符。>

- [ ]  A. 认定漏洞 —— LLD「四节」与实现「五节」不符,DoD grep 会误判;设计文档与产物脱节
- [ ]  B. 不认定 —— 多一节是合理演进(校验节本就该独立),回灌 LLD 即可,非漏洞
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定文档脱节(回灌 LLD「四节」→「五节」+ DoD grep 同步),但承认第五节是合理补充;修订 = LLD 三处「四节」改「五节」+ 核对 grep DoD

## Q3. (D7 现实矛盾) VISION/ADR-0013「重组 design/」vs F019 实际无物理重组   [落盘: 处理报告]

<出题依据:ADR-0013 标题「设计/归档重组执行决策」+ 必做档「design/ 按 feature 聚合(现状混用最该治)」;VISION 行 42「现状 design/ 子目录与裸放混用 → 按分层规则重组」。但 F019 实际执行发现 design/ **已天然分层**(methodology 裸放 + feature 子目录),无需物理挪文件,只修了 9 处归档链接。设计假设「现状混用需重组」,现实是「天然已分层」——措辞与 dogfood 实际不符,DoD「design/ 按 feature 聚合完成」措辞误导(实际是「确认天然分层」)。>

- [ ]  A. 认定漏洞 —— 设计假设重组,实际无重组;ADR-0013/LLD 的「重组/聚合」措辞与 F019「天然分层确认」现实矛盾,误导后续读者
- [ ]  B. 不认定 —— 现状恰好合规是好事,设计面向的是「不合规时怎么办」,措辞「重组」是能力声明非本次必然动作
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定措辞误导;修订 = ADR-0013/LLD 补「F019 实证:现状已天然分层,本次迁移实为确认 + 归档链接修复」(dogfood 实证回灌),消除「重组」与「确认」的措辞落差

## Q4. (D4 失败模式) 豁免清单(文档)与 EXEMPT_PREFIXES(代码)不同步   [落盘: 处理报告]

<出题依据:核实 HARNESS-RULES.md 第三节「豁免清单」写 feature-skill-* vs feature-skills-*;scripts/harness-check.py 行 24 `EXEMPT_PREFIXES = ("feature-skill-", "feature-skills-")` 硬编码。两处独立维护:若 HARNESS-RULES 新增豁免项,脚本不会自动知道;反之亦然。规则权威(HARNESS-RULES)与执行(脚本)漂移风险。>

- [ ]  A. 认定漏洞 —— 规则权威与校验执行双源,无同步机制,漂移必然发生
- [ ]  B. 不认定 —— 豁免项极少且稳定(历史遗留),双写可接受,不值得引入同步机制
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定漂移风险但当前豁免项稳定;缓解 = harness-check.py 顶部注释标注「豁免清单须与 HARNESS-RULES 第三节同步」+ DESIGN.md 记同步义务,不引入配置文件(最小可用)

## Q5. (D5 盲点) 可选档(questionnaires/adr 分层)标 TBD 无重访触发   [落盘: 处理报告 + OPEN-DECISIONS]

<出题依据:ADR-0013 行 14「可选档(TBD)」+ 行 30「自然演进」;LLD 行 64「可选档标 TBD」。TBD 无重访触发条件——归档平铺膨胀(questionnaires/archive 已 30+ 文件)到什么程度才做可选档?无信号定义,等于永久悬置或随机决策。>

- [ ]  A. 认定漏洞 —— TBD 无重访触发 = 永久悬置风险;归档膨胀无量化触发
- [ ]  B. 不认定 —— 个人项目归档量可控,TBD 留弹性合理,不必预设触发
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定触发缺失;补一条 OD 重访触发(如 archive/ 文件数 > 50 或某 feature 归档 > 10 份时重估可选档),不强制立即做

## Q6. (D4/D7) 归属判据 pwd 校验——设计声明未实现   [落盘: 处理报告]

<出题依据:VISION 关键决策 Q4「前端落盘前轻量校验(pwd 归属)防误落」+ HARNESS-RULES 第二节归属判据。但核实 scripts/ 与 skills/doctor-harness/ **无任何 pwd/归属校验实现**(grep 空)。F017–F020 未实现此功能。设计声明的防误落机制(多项目场景)无落地。>

- [ ]  A. 认定漏洞 —— 防误落机制声明未实现,多项目场景无防护;设计 vs 实现缺口
- [ ]  B. 不认定 —— pwd 校验是各 skill 落盘前的职责(非 doctor-harness 独有工具),doctor-harness 只定义判据,执行在各 skill
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定实现缺口,但 pwd 校验归属应在各 skill 落盘逻辑(非 doctor-harness 脚本);缓解 = HARNESS-RULES 明示「pwd 校验由各 skill 落盘前执行,doctor-harness 只提供判据」+ 标注为待 dogfood(真实多项目场景触发时落地)

## Q7. (D6 可验证性) dogfood 验收标准缺失——F019 passes:true 算 dogfood 通过?   [落盘: 处理报告]

<出题依据:VISION Q9「先 dogfood 后入家族,迁移验证通过后同步第 9 个」;F020 已同步第 9 个(基于 F019 passes:true)。但「dogfood 验证通过」无定义:F019 passes:true(迁移执行 + DoD 绿)是否等价于 dogfood 通过?还是需要「真实使用 doctor-harness 处理一次新 harness 场景」才算?入家族的门槛模糊。>

- [ ]  A. 认定漏洞 —— dogfood 验收标准未定义,入家族门槛模糊;F019 是迁移执行非 doctor-harness 使用验证
- [ ]  B. 不认定 —— F019 迁移本身就是 doctor-harness 首次实战(用它自己的规则 + 脚本 + 流程),passes:true 即 dogfood 通过
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定标准模糊;补定义「dogfood 通过 = 用 doctor-harness 的 HARNESS-RULES + harness-check + MIGRATION-FLOW 完整走通一次真实 harness 场景」(F019 符合:用了规则核对 + 脚本校验 + 链接修复),入家族合理;定义写入 DESIGN.md 防后续争议

## Q8. (D3 替代方案) 校验脚本不查分层——是否权衡过「让脚本校验 design/」   [落盘: 处理报告]

<出题依据:HLD 选型表「校验检查项 = 三合一(命名/ADR/归档)」,被否决项只列「内容语义判断」。但「design/ 分层校验」既非纯格式也非纯语义——可做「report 模式」(列出现状)或「heuristics」(feature 套有 VISION+HLD+LLD 三件 → 应在子目录)。这个中间方案未被权衡。>

- [ ]  A. 认定漏洞 —— 分层校验的中间方案(report / heuristics)未进被否决项,选型不完整
- [ ]  B. 不认定 —— 三合一已够,分层靠人工,不必为完整性硬加
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定被否决项缺失;与 Q1 C 联动——补「report 模式」作被否决项记录(脚本列 design/ 现状,不判定对错),HLD 选型表补此方案及否决/采纳理由

## Q9. (D1 未言明假设) 「演进是常态」——doctor-harness 真会被持续使用吗   [落盘: 处理报告]

<出题依据:VISION Q1 动机「演进是常态(新 feature 持续产生、规范持续修订)→ 立治理 skill」。但本仓库是方法论仓库,harness 演进频率低(repo 设计/v4/skill-spec-revamp/doctor-harness 共 4 次 feature 级设计,跨数周)。若演进实为低频,doctor-harness 可能沦为「一次性迁移工具 + 静态文档」,与「治理 skill 常态职责」定位张力。Q1 自身已部分承认(约束最小可用)。>

- [ ]  A. 认定存疑假设 —— 本仓库演进低频,「常态」假设未经使用数据验证;skill 可能低使用率边缘化(类 OD-12 grill 风险)
- [ ]  B. 不认定 —— skill 定位面向「所有用本方法论的项目」(不只本仓库),跨项目演进是常态;本仓库低频不代表普遍
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定假设未验证;补 OD 重访触发(如 doctor-harness 连续 3 个月零使用,或仅本仓库使用无跨项目,重估定位),与 OD-12 grill 处置先例一致

## Q10. (D8 术语一致性) 「dogfood 验证通过」「布局合规」术语边界   [落盘: CONTEXT.md]

<出题依据:VISION Q9「dogfood 验证通过」作入家族条件但未定义(见 Q7);HARNESS-RULES/SKILL 用「布局合规」指代 harness-check 的检查,但 Q1 显示脚本不查分层——「布局合规」的内涵(含分层 vs 不含)模糊。「dogfood 通过」「布局合规」两词在 VISION/SKILL/HARNESS-RULES 间无统一定义。>

- [ ]  A. 认定冲突 —— 「布局合规」「dogfood 通过」术语内涵模糊且跨文档不统一
- [ ]  B. 不认定 —— 术语在语境中可推断,CONTEXT 已有 skill 家族节,不必为每个短语立条目
- [ ]  🤔 我定不了 → 推迟/降风险
- ✍️ 自定义: __________
- [X]  C. 部分认定 ★推荐 —— 认定边界模糊;补 CONTEXT 或 HARNESS-RULES 定义「布局合规 = 命名/ADR编号/归档位置三检查(脚本可查)+ 分层(人工判据,脚本 report)」,与 Q1/Q7 联动;不进 CONTEXT 主表(属 doctor-harness 内部术语,落 HARNESS-RULES)

## 补充声明

<任何想补充的话:新需求、范围调整,临时发现的风险……没有就留空。agent 处理时必读>