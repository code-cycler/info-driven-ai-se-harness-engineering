---
mode: feature
wave: 0
stage: vision
created: 2026-08-08
status: archived
---
# 问卷 vision W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的决策点逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(默认关,本次未启用):全部 `[ ]`,人逐条作答
> - **勾 `[x]` = 采纳默认** → 按该默认落盘; **取消(留空)= 不采纳** → 该要点转入 W01 单独拷问
> - **单向门要点(发布 / 删除 / 花钱 / 脱敏等不可逆)永不预勾**,强制人逐条显式勾选确认
> - 本波**不用 🤔**(yes/no 二选一,无中间态);真定不了 → 留空即可,转 W01 深究
> - 若"大体同意但要改一两处" → 留空,转 W01 时在深究题里给自定义值
>
> 默认来源标注于〔〕。
>
> **设计背景**(供作答参考):doctor-for-harness 立项于 [OD-15](../../../docs/OPEN-DECISIONS.md(压测 [grill-harness-file-mgmt-w01](../../../questionnaires/archive/grill-harness-file-mgmt-w01.md 产出,2026-08-08)。用户裁决:harness 文件**严格**归 `harness/` 父级 + 父级下子文件夹分层,**不污染项目根**;doctor-for-harness 处理 harness 演进中的文件迁移、规范权威化、迁移工具、布局校验。**第一个治理任务 = harness 分层落地**(本仓库现状 design/ 子目录 + 裸放混用,先设计再迁移)。

## 决策默认值清单

### 目标

- [X]  **1 设计核心目标** = 建立 doctor-for-harness 作为 **harness 演进治理 skill**:① 组织规则权威化(分层定义 + 归属判据 + 命名规范);② 迁移工具/流程(目录重组 + 相对链接重算 + 断链回归);③ 布局合规校验(命名正则 / ADR 编号连续 / 归档位置);④ 演进记录(组织变更留痕)。〔OD-15 职责清单 + 用户裁决〕
- [X]  **2 主要受益对象** = 维护者本人 + AI 代理(Claude Code);与既有 8 skill 定位一致。〔推断——重点核对:是否只服务本仓库,还是像 long-running 一样「通用开发工具」〕
- [X]  **3 家族身份** = 第 9 个核心 skill,治理型、横切属性(类似 delegate 横切任意环节,不锁死在线性阶段)。〔推断——重点核对:或像 OD-13 shadow 一样先不入家族、dogfood 先行?〕

### 范围

- [X]  **4 管辖边界** = 只管 `harness/` 区(design/ + questionnaires/ + adr/)的组织、迁移与校验;**不碰** CONTEXT.md / OPEN-DECISIONS.md / TODO.md / docs·retro/ 项目固有文件(除非确需修订先例)。〔S6 + ADR-0011 决策 3〕
- [X]  **5 不做什么** = 不重写问卷引擎(QUESTIONNAIRE-FORMAT / PROCESSING-RULES)、不替 OD-8(引擎副本)/ OD-10(分发洁净)/ OD-12(grill 处置)决策、不改方法论三块内容、**不推翻 ADR-0011 的「硬编码 harness/」**(分层是 harness **内部**组织形态,不是落盘根配置化回归)。〔已核实:ADR-0011 + OD 清单〕
- [X]  **6 与既有 skill 落盘路径的关系** = doctor-for-harness 的规范文档成为各 skill 落盘路径的**权威引用**(source),但各 SKILL.md 仍硬编码 `harness/`(ADR-0011),分层规则由 doctor-for-harness 文档承载、被 SKILL.md 引用,不逐 skill 内联复制。〔ADR-0011 + 反漂移考量〕
- [X]  **7 第一个治理任务** = **harness 分层落地**(本仓库):现状 design/ 子目录与裸放混用 → 按分层规则重组 + 迁移 + 断链回归,作为 doctor-for-harness 设计与实现的**首个实战**(dogfood)。〔用户裁决 + 压测 Q2/Q6/Q11/Q13〕
- [X]  **8 本次产物** = 设计文档(doctor-for-harness VISION / HLD / LLD + 必要的 ADR/OD 修订)+ 实现(新 skill 文件 + 校验脚本 + 分层迁移执行);分层迁移作为独立行动项带 DoD,不随设计自动执行。〔design-Q 惯例 + 压测 Q6 一次性迁移裁决〕

### 核心场景

- [X]  **9 场景 A · 新 feature 设计启动** = agent 按分层规则决定新 feature 的 design/ 建不建子目录、问卷/ADR 落哪——规则一处权威,不靠 agent 临场判断。〔压测 Q2/Q3 裁决:feature 级建 `design/<feature>/`〕
- [X]  **10 场景 B · harness 结构迁移** = 需要重组 harness 目录(如本次分层)时,执行迁移流程:设计新布局 → 挪文件 → 相对链接重算 → 断链回归 → 规格同步。〔压测 Q6/Q13 + 2026-08-05 迁移先例〕
- [X]  **11 场景 C · 布局合规校验** = 定期/发布前跑校验脚本,检查 harness 布局合规(问卷命名正则 / ADR 编号连续 / 归档位置 / 文件都在应处)。〔压测 Q14 裁决:一次性脚本,不进每次流程〕
- [X]  **12 场景 D · 演进留痕** = harness 组织变更(迁移/规则修订)记录在案,可回溯「harness 为什么长这样」。〔OD-15 职责④ + 原始信息不丢失铁律〕

### 验收标准

- [X]  **13 产物清单** = 新 skill 目录(如 `skills/doctor-harness/`):SKILL.md + DESIGN.md + 校验脚本(如 `scripts/harness-check.py`)+ 规范权威文档(分层规则 / 归属判据 / 命名规范,可并入 SKILL.md 或独立文件)。〔推断——重点核对产物形态〕
- [X]  **14 校验脚本事实 DoD** = 对当前仓库跑:能准确报出真实违规(如 ADR 编号跳号、命名不规范、文件不在应处);分层迁移后跑:0 违规 + 0 断链。错误不误报(无违规时 0 输出)。〔推断——可脚本化,进 LLD 细化〕
- [X]  **15 分层迁移 DoD** = 本仓库 harness/ 分层完成:design/ 按 feature 聚合、archive/ 按 feature/主题聚合(或用户裁决的其它形态)、相对链接全部重算、断链回归 0 新增、各 SKILL.md 引用同步。〔压测 Q6 + 2026-08-05 先例的 DoD 参照〕
- [X]  **16 家族回归** = 新增 skill 不破坏既有 8 skill 的触发/落盘/引擎机制;CLAUDE.md 家族图 / CONTEXT skill 家族节 / 落盘速查表同步第 9 个。〔已核实:家族 8 个表述 + 同步先例〕

### 风险与约束

- [X]  **17 与 ADR-0011 的关系** = 分层不推翻「硬编码 harness/」,但分层规则本身是 harness 内部组织形态的**新决策**——记 DESIGN.md 级(双向门)还是新 ADR(难逆转性不足)?默认:分层规则记 doctor-for-harness DESIGN.md + 若迁移涉及既有链接破坏则补 ADR。 〔推断——需确认〕
- [X]  **18 迁移断链风险** = 分层迁移会破坏相对链接(先例:2026-08-05 harness 迁移曾 96 断链 → 7 豁免)。迁移必须一次性完整 + 断链回归,不渐进半途。〔压测 Q6 + 已核实迁移先例〕
- [X]  **19 两套 skill 副本同步** = 本仓库 `skills/`(发布镜像)与 `~/.claude/skills/`(全局生效)需同步新 skill(照 skill-spec-revamp 先例,仅脱敏差)。〔已核实:两套已重建一致〕
- [X]  **20 过度工程风险** = doctor-for-harness 可能滑向「为治理而治理」——约束:规则只覆盖真实已出现的场景(分层 / 归属 / 命名 / 校验),不预设过度机制;最小可用优先。〔推断——治理型 skill 的共性风险〕

## 补充声明

> **用户作答(2026-08-08,对话速答)**:「全部采纳默认」——20 条决策默认值全采纳,无留空转 W01。agent 逐字转写:处理时全部按默认落盘。

---

## 处理报告摘要(W00,2026-08-08)

- **preview 统计**:勾选采纳 20 / 留空不采纳 0 / 转 W01 正式题 0;取消默认率 0/20 = 0%(对话速答「全部采纳」)。
- **补充声明解读**:无补充内容。
- **落盘**:VISION [`harness/design/doctor-harness/VISION.md`](../../../design/doctor-harness/VISION.md(新建,20 条默认全采纳落盘);无 ADR(设计期,分层 ADR 待迁移涉链接时补);无 OD 升格(OD-15 已在位)。
- **下一波**:W01 = 无留空深究项,出**开放型骨架必答项**(V6 动机/推导 + 分层方案形态 + 归属判据细则 + 校验脚本 DoD 具体化 + 家族身份确认 + 迁移边界)。
