# STATUS-LOG · 仓库内部工作状态史

> 承接原 CLAUDE.md「仓库状态」节的历史条目(ADR-0024 P3 迁移,2026-08-20,原文逐字保留)。**只记内部工作状态时间线**;对外可感知变更见仓库根 [CHANGELOG.md](../CHANGELOG.md)(其记录规则明确排除内部治理);当前状态快照见 [CLAUDE.md](../CLAUDE.md)。追加式,只增不改。

## 2026-08-19:grill 家族边界与跑偏治理(深钻 → 复压闭环)

grill-with-docs 深钻四分支(认知状态三态接线 / 入口+中途双检测 / 校准闸门+题级 ❌ 标注双件 / 优化回路 [OD-26](../docs/OPEN-DECISIONS.md) provisional)→ 包一 skill 规格层落地(grill-Q 族间自检/校准闸门/阻塞性逃生舱分流/质量信号节 + FORMAT 规则 15 ❌ 专属分叉 + with-docs 反向相变)→ [grill-boundary-canonical-w01](../harness/questionnaires/archive/_misc/grill-boundary-canonical-w01.md) 复压(9 题全采纳 + Q8 推翻推荐 → 本文件同步三态)→ canonical 版本内修订(哲学 §3.1 认知状态行;方法论 §4.1 接线 / §4.3 优先级 / §3.3.1 指针 / §八 第 25 条;两文件头修订记录行)。斯多葛视角不落盘(对话层)。OD-4 母本同步(仓库外)累计一笔。

## 2026-08-19:skill 双侧同步机制化

2026-08-18 双侧同步(9 skill 双向合并,commit 4fece7c)暴露「项目内修、全局漏修」空隙(8/14 修订落全局漏项目、8/8 归档断链修复落项目漏全局),机制化收口:新增 [scripts/skills-sync-check.py](../scripts/skills-sync-check.py)(check-only 不选边、裁决例外白名单、EXIT 码供例行)+ CLAUDE.md 铁律第 8 条 + 工具命令节扩为两条(提交前例行,暂不入发布门强制清单);问卷 [confirm-skills-sync-mechanism-w00.md](../harness/questionnaires/archive/_misc/confirm-skills-sync-mechanism-w00.md)(14/14 全确认)。

## 2026-08-14:methodology_v5 升级完成(章节连续化 + 契约优先 + action-Q 入族)

grill-Q methodology-improvement W01 压测(10 题,压测对象 = 哲学 v7 + 方法论 v4 + design-Q 规格,参照 同级对标仓库 治理)产出:① 正文连续编号 §零至§九(v4 映射表在文件顶部)+ 全库引用审查;② §4.3 两族表补 action-Q(修 W02 Q3 漏改)+ CLAUDE.md 协作图补节点;③ §5.3 补「时序纪律」(契约层变更先更新 canonical 设计再动工,ADR-0021 通用化);CONTEXT 补规范导航(含设计套「契约优先」裁决)与「暂定」状态词、ADR-0020 补生态位卡载体裁定、新增 OD-24(全局实验/项目 backup/DOGFOOD 实测双副本策略)。**同轮立项**:design-Q 数字层级改造(Q3-A)、dogfood 最优先 + 定义消歧(Q7-A,冻结新机制新增)、方法论 704 行审计优先(Q4-B)——见 [TODO.md](../TODO.md)。v4 归 archive。

## 2026-08-14:philosophy_v7 升级完成(连续章节 + 双文件交叉治理)

在 v6 基础上建立哲学独立阅读入口,将正文统一为 §一至§五并保留旧编号兼容映射;补 harness 术语边界、current 已知缺口状态、前三学科最小进入/退出模板与代理指标反思边界;哲学 + 方法论成为 canonical 对等双文件,由 [ADR-0017](../harness/adr/0017-philosophy-section-compatibility.md) / [ADR-0018](../harness/adr/0018-canonical-dual-challenge-governance.md) 记录治理契约。v6 归 archive,v7 为 current canonical。

## 2026-08-13:grill-Q philosophy-v5 成稿压测 W01 闭环 + 发布门推送

压测 10 题(Q1 用户裁决更名「第五→第四学科视角」:全仓同步 + ADR-0015/0014 更名注记;Q2–Q10 全 C:§八 修订 9 处),全部执行并验证(脱敏 0 / harness-check 0);OD-1 三道过后推送(7853792..f93cc8b,2 commits);F026 OD-4 母本同步用户仓库外执行销项;feature_list 校正(F002/F004/F005 补 passes)。**剩 dogfood(F006 唯一剩余)**。

## 2026-08-13:philosophy_v6 升级完成(结构过渡 + 方法论治理闭环 + 学科治理路线图)

在 v5 基础上新增全文阅读路线与章节过渡;§8.6 明确为「方法论自身的治理闭环」,加入主张状态模板与「学科 → 治理机制 → 最小产物 → 进入条件」映射;v5 归 archive,v6 随后曾为 current canonical,现由 v7 接替。治理深度仍遵守最小治理切片边界,完整 Level 1/2/3 由 [OD-20](../docs/OPEN-DECISIONS.md) 管理。

## 2026-08-11:philosophy_v4 → v5 立论重构完成(安全科学第四学科视角 + 去 AI 黑盒锚点)

经完整 write→review→implement 闭环:grill-Q philosophy-v4(W01/W02,18 处修订)→ discipline-mapping([ADR-0014](../harness/adr/0014-discipline-mapping-strategy.md) 学科挂接分层)→ grill-with-docs(去黑盒 6 点结晶,落 [CONTEXT AI 黑盒节](../docs/CONTEXT.md) + [OD-19](../docs/OPEN-DECISIONS.md))→ design-Q philosophy-v5([VISION/HLD/LLD](../harness/design/philosophy-v5/) + [ADR-0015](../harness/adr/0015-deblackbox-anchor.md))→ 设计套压测(10 项修订)→ long-running 起草(P1-P5,commit 530d0f4);v4 归 archive。新增 OD-18(学科挂接回顾)/ OD-19(形式化 V&V 缺口);v5 §八「去 AI 黑盒」(三层次 + 正交第一支柱 + 三风险 + 统合对策 + 弹性边界)。

## 2026-08-08:doctor-for-harness 完成(第 9 个 skill)+ harness 治理落地

分层规则权威化([HARNESS-RULES.md](../skills/doctor-harness/HARNESS-RULES.md),ADR-0012/0013)+ 校验脚本 [scripts/harness-check.py](../scripts/harness-check.py)(命名/ADR 编号/归档位置三检查);设计套压测 10 题全认定 + 7 项工件修订执行;格式反馈落地(单波次上限 10 / 小波阈值 3 四副本统一);**归档子目录化**(41 份按 feature/主题迁入 10 子目录 + [archive/README.md](../harness/questionnaires/archive/README.md) 索引);MIGRATION-FLOW 迁移流程沉淀。

## 2026-08-07:design-Q skill 规格整理(skill-spec-revamp)→ 撤销方案 R

骨架增强(HLD/LLD 判别法则 + 反简化最小必含 + 坍缩分档,仅 design-Q)**保留并回灌**;落盘路径配置化(方案 R)**已放弃**([ADR-0011](../harness/adr/0011-abandon-plan-r-hardcode-harness.md)),**回归硬编码 `项目根/harness/`**(design/ + questionnaires/ + adr/);两套 skill(skills/ 与 `~/.claude/skills/`)已重建一致(仅脱敏差),设计套 [harness/design/skill-spec-revamp/](../harness/design/skill-spec-revamp/)。

## 2026-08-05:repo 级设计完成,落地执行中

design-Q 三阶段 + grill-Q 压测 12 项回灌(设计套 [harness/design/repo/](../harness/design/repo/));方法论 + 哲学升 **v4**(受众收窄个人 / 第二支柱机制层对称化 / 哲学三学科化(人因/软工/运筹));harness 区物理分离(docs/design/ + docs/questionnaires/ 迁入);术语治理(8 术语全保留 + 新词三条件门槛)。落地执行 P1–P4 完成(P1 迁移 / P2 术语 / P3 v4 / P4 入口),**P5(ADR-0008/0009/0010)与 P6(发布门 + dogfood)待执行**,见 [TODO.md](../TODO.md)。

## 历史线(2026-07-29 起)

2026-07-29 methodology_v3 完成(ADR-0004/5/6);2026-08-01 action-Q 入库(第 8 个 skill)+ 首次推送;2026-08-04 三块拆分(ADR-0007);2026-08-05 repo 级设计 + v4 + harness 迁移;2026-08-08 doctor-harness 完成(第 9 个 skill);2026-08-11 philosophy_v5(安全科学第四视角);2026-08-13 philosophy_v6(治理进化);2026-08-14 philosophy_v7(连续章节与双文件交叉治理)。
