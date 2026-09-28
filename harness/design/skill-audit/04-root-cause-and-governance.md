# skill 体系审查 · 根因拷问与预防治理(2026-09-27)

> 伴随产物:三份审查报告(01/02/03 同目录)、修复批(05-fix-plan.md)、问卷 [confirm-skill-audit-fix-w00/w01](../../questionnaires/archive/)。
> 用户指令:「全数修复,并拷问为什么 doctor harness 以及本项目的工作循环会留下这些问题,有什么办法预防和治理」。

## 一、为什么 doctor-harness 没拦住?

1. **检查面错位**。doctor-harness 的职责是**布局合规**——文件放哪、命名、分层、归档;而 41 条发现里绝大多数是**内容真实性**漂移(计数、状态行、规则编号引用、落点声明)。`harness-check.py` 是结构断言:能查「ADR 编号连续」,查不了「CLAUDE.md 说的 P4 状态是否为真」。内容真实性不在任何 skill 的检查面上。
2. **治理者自身无防线**。报告 02 中-4 的反讽:doctor-harness 自己四份文档对 harness-check 行为的描述漂移了(写「三检查、0 违规无输出」,实际已四检查且必打印报告)。治理者的文档同样身处多文件双写模式,没有断言保护——**监督者与被监督者暴露在同样的腐化机制下**。

## 二、为什么工作循环留不下防线?(核心规律 + 六个机制漏洞)

**核心规律:有脚本的地方不漂移,靠人肉清单的地方必漏。**

本次三个 0 违规(`skills-sync-check.py` / `desensitize.py` / `i18n-check.py`)全是机器断言;而 41 条里 30+ 条出在没有脚本的地方。F051 的「十处联动清单」已是相当认真的人肉清单,仍漏了哲学文件与状态节——这不是纪律问题,是**机制形态**问题:人肉枚举没有完备性保证。

漏洞链(每条对应实证):

| # | 漏洞 | 实证 | 治理项 |
|---|---|---|---|
| 1 | 验收门字符串盲区 | F051 验收 grep「8 个核心 skill」精确子串,「8 个核心**方法论** skill」变体漏网(README:160 直达今日) | Q5① 宽松模式断言脚本 |
| 2 | DoD 枚举无元检查 | F052 治理收尾 DoD 漏列「TODO 勾销」,整条链断(报告 03 高3) | Q5② DoD 固定项 |
| 3 | 协议存在但无执行动作 | OD-8 四方考量写在 DESIGN 里,「改引擎前 grep 三副本」非强制步骤;08-20 一天两笔(D34/D38)双双漏走(报告 01 高1/高2) | Q5③ 前置检查步骤 |
| 4 | 留痕通道有旁路 | push 有三道门,但「改 SKILL.md」无必经关卡;09-25 / 09-11 两次本体变更绕过 CHANGELOG(报告 01 中5/中6) | Q5① 断言覆盖 + 流程自觉 |
| 5 | 双写结构本身 | 计数/状态五处双写(CLAUDE 状态节、TODO 头、philosophy_v7、practical_v1、README 树),联动清单漏项即漂移——本批 7 条直接由此产生 | OD-30(单源化待决) |
| 6 | 派生视图单向过期 | PROJECT-OVERVIEW 生成当日即过期两处 summary(步骤顺序:先重生成后写源文件;报告 03 低11) | proj-overview 规格后续修订候选 |

## 三、修复批裁决记录(问卷 confirm-skill-audit-fix W00/W01)

- W00 十四条全勾(理解确认,无纠正)。
- Q1=C:D34 四方同步为「处理报告全文 + 顶部摘要节」,四方 DESIGN/CHANGELOG 留痕。
- Q2=C:grill/retro 副本 LN 词汇行改本 skill 实际命名,FORK-NOTES 登记分叉。
- Q3=C:grill-with-docs 结构示例统一 harness 制(与 ADR-FORMAT/L148/HARNESS-RULES 第六节对齐)。
- Q4=C:计数/状态单源化**不混批**,落 OD-30 待决;本批仅修既有 7 条失真。
- Q5=①②③④⑤全选:预防治理包五项全落地(见下)。
- Q6=C:每 skill CHANGELOG 一条汇总 + 根 CHANGELOG 一条 + STATUS-LOG 一条;逐条明细由归档问卷处理报告承载。
- W01 补充声明新需求(跨会话强制 handoff)→ OD-31 待决 + 本文档 §四回应。

## 四、预防治理落地清单(本批实施)

1. **Q5① 计数/状态断言脚本** `scripts/audit-check.py`(新增):机器断言「全仓 skill 计数一致(含变体模式)+ TODO 主线 vs feature_list passes 一致」——直击漏洞 1/4,防住本批高危 3 条复发。
2. **Q5② 治理收尾 DoD 固定项**:long-running-agent SKILL 补「治理收尾必含 TODO 块勾销 + CHANGELOG/STATUS-LOG 追加」——直击漏洞 2。
3. **Q5③ 引擎前置检查步骤**:四方 PROCESSING-RULES 各加「改引擎文件前强制 grep 其余三副本,同步或声明二选一并留痕」——OD-8 从协议变步骤,直击漏洞 3。
4. **Q5④ sync-check 双向扫描**:`skills-sync-check.py` 增全局侧独有 skill 目录 warning(例外白名单:shadow=OD-13 pilot)——堵方向性盲区。
5. **Q5⑤ 审查知识沉淀**:本目录(skill-audit/)三份报告 + 本文档,问卷处理报告载指针。

## 五、补充声明回应:跨会话强制 handoff(「不留尾巴」)

**现状盘点**:仓库已有四个跨会话载体——long-running 的 `feature_list.json` + `claude-progress.txt`(仅 long-running 模式启用)、TODO.md、STATUS-LOG、PROJECT-OVERVIEW(认读第一入口)。缺口在于:**全部依赖「记得写」,没有会话边界的强制关卡**——本批 41 条里至少 5 条(TODO 滞后、两笔 CHANGELOG 绕过、PROJECT-OVERVIEW 当日过期、STATUS-LOG 漏记)就是「会话尾巴」的直接产物。

**候选方向**(落 OD-31 待决,不在本批实施):
- A. **Claude Code Stop hook / SessionEnd 钩子**:会话结束触发脚本,机器断言「feature_list 有 passes=false 则 TODO 必有未勾项;本会话改过的文件对应 CHANGELOG 是否已追加」——把「擦屁股」变成 exit code 拦截。
- B. **会话收尾 DoD 清单化**(Q5② 的推广):任何会话(不限 long-running)结束前跑一遍固定三问:TODO 勾了吗 / CHANGELOG 记了吗 / 派生视图(PROJECT-OVERVIEW)该刷新吗——靠流程,弱于 A。
- C. **写入即留痕**:把「改 SKILL.md 必同时改 CHANGELOG」做成 pre-commit hook(git 层拦截)——只覆盖 git 提交面,覆盖不了「改了没提交」的会话尾巴。
- 倾向:A + C 组合(会话边界 + 提交边界双闸,B 作为无钩子环境的兜底);实施属新 feature,走 design-Q。

## 六、遗留与下一步

- OD-30(计数单源化)、OD-31(跨会话 handoff)已入 OPEN-DECISIONS,重访触发见各自条目。
- proj-overview 漂移自检扩到 STATUS-LOG/CHANGELOG 转述行(报告 03 低11 的 skill 规格面)——记入 OD 作为该 skill 下次规格修订候选,本批不动 skill 规格(超修复范围)。
- doctor-harness「治理者自身体检」议题(§一之 2):audit-check.py 的计数断言部分覆盖其文档面,更深的内容真实性断言(规则编号引用有效性等)可作后续扩展。
