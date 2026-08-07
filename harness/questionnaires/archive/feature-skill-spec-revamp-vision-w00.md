---
mode: feature
wave: 0
stage: vision
created: 2026-08-06
status: processed
---
# 问卷 vision W00 · Preview(决策默认值 yes/no 速答)

> **本次设计对象**:整理 design-questionnaire skill 规格——三组改动:① 落盘路径配置化(harness/ 与项目文件分离)② HLD/LLD 职责区分 ③ 防过度简化(最小必含)。
> **feature 模式**:已有 skill 的新改动;探索已完成(读 design-Q 五件套 + 对照 hld_v1/v2 简化版 vs repo/HLD 完整版 + 四 skill 漂移面确认)。
>
> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的决策点逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(2026-08-03 起,默认关):本次未启用,全部 `[ ]`,人逐条作答
> - **勾 `[x]` = 采纳默认**(按该倾向落盘);**留空 = 不采纳** → 转入 W01 单独拷问(出选项深究)
> - **单向门要点永不预勾**:本阶段无单向门(改 skill 规格可回退,不涉发布/删除/花钱/脱敏)
> - 本波**不用 🤔**(yes/no 二选一);真定不了 → 留空转 W01
> - 若"大体同意但要改一两处" → 留空,转 W01 时给自定义值
>
> 默认来源标注于〔〕。

## 决策默认值清单

### V1 目标与受众

- [X]  **1 三组改动一起做**:落盘路径配置化 + HLD/LLD 职责区分 + 防简化最小必含,一次设计一并落地(不分批) 〔用户指令明确给出三组;三组在骨架层耦合——职责区分与最小必含都改同一个 STAGE-SKELETONS.md〕
- [X]  **2 影响面 = design-Q canonical + 四份引擎副本**:HLD/LLD 职责区分 + 最小必含**只改 design-Q 骨架**(STAGE-SKELETONS.md 是 design-Q 专属,retro 用四节骨架);落盘路径配置化**同步四份**(design-Q / grill-Q / retro-Q / action-Q 的 SKILL.md + PROCESSING-RULES.md 副本) 〔OD-8 引擎漂移治理;骨架归属探明〕

### V2 范围(做什么 / 不做什么)

- [ ]  **3 落盘路径配置化机制 = 声明优先 + 探测兜底 + 落盘前确认**:① 读项目 CLAUDE.md/AGENTS.md 是否有「设计产物落盘根」声明 → 用声明值;② 无声明 → 探测:存在 `harness/` 目录用 `harness/`,否则默认 `docs/`;③ 落盘前向用户显式确认探测/声明的路径(防误落)。声明格式(机器可识别)在 hld 阶段定 〔通用 skill 不能硬编码 harness/——项目A 用 docs/、本仓库用 harness/,skill 须两者兼容;本仓库 CLAUDE.md 已有「落盘路径速查表」节可作声明锚点〕
- [X]  **4 配置粒度 = 单一「落盘根」统一前缀**:design/ + questionnaires/ + adr/ 共用一个根前缀(如 `harness/`);CONTEXT.md / OPEN-DECISIONS.md / TODO.md 等项目固有文件路径**不动**(各项目已定型,且 CONTEXT 常在根、OPEN-DECISIONS 在 docs/ 等) 〔单一根覆盖绝大多数项目结构;减少配置复杂度,避免逐目录可配的认知负担〕
- [X]  **5 HLD/LLD 职责区分落地 = 改 STAGE-SKELETONS.md**:骨架头部加「HLD/LLD 判别法则」(HLD = 架构骨架,phase-invariant;LLD = 构建路径,incremental)+ 每项标注所属层 + 重叠项(H3 接口契约 vs L3 接口规格)显式区分粒度 〔骨架是 design-Q 专属文件,改一处即可;hld_v1 越界(章节级改写混进 HLD)是判别法则缺失的实证〕
- [X]  **6 防简化机制 = 骨架每项加「最小必含」硬约束 + 「产出形态」引导**:① 每项列最小必含子项(缺一不算该骨架项完成,计入覆盖度判定);② 产出形态建议(表格/清单/契约格式/图),引导结构化而非散文;③ 骨架头部加反简化声明(HLD/LLD 是可实现期直接执行的规格,不是提纲) 〔lld_v2「§2.1 四必含」先例;hld_v1 反面案例:开放散文出题方向 → agent 一笔带过;repo/HLD 正面案例:表格+被否决项+动作清单 = 详细〕
- [X]  **7 不做(scope 边界)**:不改交互机制(问卷格式 / preview 机制 / 逃生舱 / 小波阈值)、不改 grill-Q/retro-Q/action-Q 的骨架(只同步落盘路径)、不重构 skill 目录结构(OD-8 已决保留现状)、不改 long-running 的 feature_list 机制(只同步它读归档的路径) 〔scope 控制;交互机制稳定是 skill 可靠性基础〕

### V3 核心场景

- [X]  **8 dogfood 验收 = 本次 design-Q 产物自身满足新「最小必含」标准**:本次产出的 HLD/LLD 必须按新骨架写成(repo/HLD 那样的完整版:表格 + 被否决项 + 接口契约 + 动作清单),**不得**重蹈 hld_v1/v2 的简化覆辙。即"用新规范产出新规范的规格"——改动 2/3 的第一次实战就是本次设计本身 〔用户明确指 hld_v1/v2/lld_v1/v2 为"典型简化输出";dogfood = 自用自证〕

### V4 验收标准

- [X]  **9 DoD 四条**:① design-Q STAGE-SKELETONS.md 含 HLD/LLD 判别法则 + 每项最小必含 + 产出形态;② 落盘路径配置化(声明优先+探测兜底)落 design-Q 的 SKILL.md + PROCESSING-RULES.md + STAGE-SKELETONS.md;③ 四份引擎副本落盘路径同步(OD-8 重访触发①);④ 本次 HLD/LLD 自身通过"最小必含"自检(dogfood) 〔覆盖三组改动 + 漂移治理 + dogfood〕

### V5 风险(与现有系统冲突)

- [X]  **10 引擎副本漂移 = 同步四份**:改 design-Q 落盘映射必须同步 grill-Q / retro-Q / action-Q 三份 PROCESSING-RULES.md 副本 + 各 SKILL.md 路径字符串,否则四 skill 落盘路径分裂(本仓库用 harness/、其他项目可能用 docs/) 〔OD-8 引擎漂移治理;确认漂移面:design-Q 3 处 + grill-Q 3 处 + retro-Q 3 处 + action-Q 4 处〕
- [X]  **11 配置化可预测性 = 强制落盘前确认点**:探测机制(无声明时看 harness/ 存不存在)可能误判(如项目有 harness/ 但不用来放设计产物)→ 落盘前显式确认路径,用户可纠正 〔防误落;探测是启发式非权威,确认点兜底〕
- [X]  **12 最小必含 vs 坍缩档 = 分档调节**:完整三阶段档 = 全量最小必含;坍缩为 hld 档 / 坍缩为 lld 档 = 精简版最小必含(只保留该档必需子项)。避免过严让小项目负担重 〔D17/D19 阶段坍缩机制;skill 已有坍缩分支,最小必含须适配〕
- [ ]  **13 全局生效 = 记风险不立 ADR**:改 `~/.claude/skills/` 下 skill 立即影响所有项目下次调用 design-Q,影响面广但**可回退**(文件可改回)→ 不达 ADR 三条件(难逆转性不足),记入 design-Q DESIGN.md 决策记录即可 〔可逆性判断;ADR 门槛〕

### V6 动机(feature 必答)

- [X]  **14 为什么改(三因)**:① skill 规格(硬编码 docs/)与项目实践(harness/ 分离)脱节——本仓库 CLAUDE.md 落盘速查已 harness/,skill 规格滞后;② hld_v1/v2/lld_v1/v2 简化输出实证骨架缺约束(开放散文 → 一笔带过);③ HLD/LLD 职责重叠致越界(hld_v1 把章节级改写混进 HLD)。默认按此三因并述 〔探索发现〕
- [X]  **15 为什么是现在**:上轮 P1–P6 刚把本仓库 harness 区落地(CLAUDE.md 落盘速查表、harness/design/ + harness/questionnaires/ + harness/adr/ 迁移完成),skill 规格滞后需追平;dogfood 窗口(刚吃过 harness 迁移的链接改造苦头,对"落盘路径"敏感度最高) 〔仓库状态;时机〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-06 · W00 → processed)

- **preview 统计**:勾选采纳 13 / 留空不采纳 2 / 转 W01 正式题 2;opt-in 开关未启用,无取消率;单向门 0
- **采纳 13 条**(按默认落盘):第 1(三组一起)、2(影响面 design-Q+四副本)、4(单一落盘根)、5(改 STAGE-SKELETONS)、6(最小必含+产出形态)、7(scope 边界)、8(dogfood 验收)、9(DoD 四条)、10(同步四份)、11(强制确认点)、12(分档调节)、14(三因)、15(时机)
- **留空转 W01 2 条**:第 3(落盘路径配置化机制)→ W01 Q1+Q1.1;第 13(全局生效处置)→ W01 Q2
- **去向**:留空 2 条 → [vision W01](feature-skill-spec-revamp-vision-w01.md) 深究
- **VISION.md**:待 W01 答完后落盘 `harness/design/skill-spec-revamp/VISION.md`(落盘根本仓库 = harness/,本项目实践优先)
- **归档**:W00 待 W01 处理后连同归档 `archive/`
