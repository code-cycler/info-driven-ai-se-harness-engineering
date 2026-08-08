---
mode: feature
wave: 1
stage: vision
created: 2026-08-08
status: archived
---
# 问卷 vision W01 · doctor-for-harness 开放题

> **工件**:[VISION](../../../design/doctor-harness/VISION.md(W00 20 条全采纳落盘)。
> **本波是 W00 之后的正式题波**:W00 无留空项,故本波 = 开放型骨架必答项(V6 动机 + 骨架需具体化的决策点),不适合 yes/no 速答,逐题拷问。
> **前置探索**:已核实——家族 8 个 skill 表述(CLAUDE.md + CONTEXT);压测 [grill-harness-file-mgmt-w01](../../../questionnaires/archive/grill-harness-file-mgmt-w01.md 的 14 题发现;ADR-0011 硬编码;2026-08-05 harness 迁移先例(96 断链 → 7 豁免);现状 harness/design/ 子目录与裸放混用(repo/、skill-spec-revamp/、feature-skills-harness-consistency/ 是目录;VISION.md、hld_v2.md、lld_v2.md、hld-methodology-separation.md 裸放)。
>
> **填写规则**:
>
> 1. 每题勾选 `[x]`;★ = 推荐选项;opt-in 关不预勾
> 2. 🤔 逃生舱:勾了 = 定不了 → 降风险协议
> 3. ✍️ 自定义(尤其"不认定"时给理由、"部分认定"时给修订方向)
> 4. 排序:非推荐在前 → 🤔 倒数第二 → 推荐最后

## Q1. (V6 动机) doctor-for-harness 的动机推导——为什么是「治理 skill」而不是「一次性迁移脚本」   [落盘: VISION#动机]

<出题依据:VISION 目标已写四项职责(规则权威化 / 迁移 / 校验 / 留痕)。但动机需显式化:压测 14 题发现 harness 管理「静态平铺无层次化」,用户裁决「设计 skill 处理演进」——隐含假设:harness 会**持续演进**,需要常态机制而非一次性工具。若 harness 其实稳定(分层落地后不再变),skill 就是过度工程。>

- [ ]  A. 一次性迁移脚本即可 —— harness 分层落地后结构稳定,演进是低频事件,脚本 + 文档够用,不必立 skill
- [X]  B. 治理 skill 是必要的 —— 演进不是一次性(新 feature 持续产生、规范持续修订),skill 承载「规则 + 流程 + 校验」常态职责,与既有 8 skill 家族一致
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 立 skill(演进是常态,家族一致),但**约束最小可用**:skill 只做「规则权威 + 迁移流程 + 校验脚本 + 留痕」四件事,校验脚本可复用、迁移流程可手动跟随,不预设自动化框架

## Q2. (V2 范围) 分层方案的形态——harness/design/ 的聚合规则怎么定   [落盘: VISION#范围 + HLD#分层规则]

<出题依据:压测 Q2/Q3 认定「feature 级建 design/<feature></feature>/」,但形态未定案。现状 chaos:repo/、skill-spec-revamp/、feature-skills-harness-consistency/ 是子目录,而 VISION.md、hld_v2.md、lld_v2.md、hld-methodology-separation.md 裸放。分层规则需回答:哪些文件进 feature 子目录、哪些裸放、判定句是什么。>

- [ ]  A. 全部进子目录 —— 每个设计套(哪怕单文件)都建 design/<slug></slug>/ 目录,根下零裸放,规则最简单
- [X]  B. 按「是否 feature 级设计」判定 —— feature 级(有独立设计套、与其它 feature 冲突)建目录;全局/单文件设计(如 methodology 修订)裸放根下——判定句:该设计是否会被独立引用 / 与其它 feature 冲突
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 采用 B 的判定句,但**给存量定案**:现有裸放文件(VISION.md / hld_v2.md / lld_v2.md / hld-methodology-separation.md)按新规则归类——methodology 系列是全局设计(裸放保留),feature 系列(repo/skill-spec-revamp/feature-skills-harness-consistency)已建目录(保留);判定句进文档,存量按判定句逐条核对

## Q3. (V2 范围) archive/ 的组织形态——归档分层还是维持平铺+索引   [落盘: VISION#范围 + HLD#归档规则]

<出题依据:压测 Q5 认定归档膨胀,推荐「archive/<feature></feature>/ 子目录 + 只移不删」。但 archive 现状 30+ 文件已按 confirm/feature/grill 前缀平铺,重构会破坏既有相对链接。且「原始信息不丢失」铁律要求只移不删。>

- [X]  A. archive/<feature></feature>/ 子目录 —— 按 feature/主题聚合,检索友好;但需迁移存量 + 重链
- [ ]  B. 维持平铺 + 归档 README 索引 —— 不挪存量(信息不丢失 + 链接不动),补一个索引文件列出归档内容,检索靠索引
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 新归档按 feature/主题建子目录(医生 skill 的迁移流程管),**存量不挪**(避免破坏既有链接 + 铁律),补归档 README 索引作为过渡;子目录化随自然演进(新问卷进新结构)

## Q4. (V2 范围) 归属判据——何时子项目独立 harness、何时归主根   [落盘: VISION#范围 + HLD#归属判据]

<出题依据:压测 Q1/Q9 认定「无子项目 harness 边界判据」。判定句在压测 Q9 推荐 = 子模块有独立 CLAUDE.md / 独立 git / 独立发布边界 → 子模块根建自己的 harness/;否则归主根。需确认是否采纳。>

- [ ]  A. 不需要判据 —— 个人项目基本单仓库,子项目独立成仓,无需规格化
- [X]  B. 采纳判据句 —— 子模块有独立 CLAUDE.md / git / 发布边界 → 独立 harness;否则归主根
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 采纳判据句,但**下沉为轻量规则**(doctor-harness DESIGN.md 而非 ADR):个人单仓库场景判据基本不触发,等价于「默认归主根,子模块独立时另建」;前端落盘前轻量校验(pwd 归属)防误落

## Q5. (V3 场景) 校验脚本的触发时机与形态   [落盘: VISION#场景 C + HLD#校验机制]

<出题依据:压测 Q14 认定「一次性脚本,不进每次流程」。形态待定:独立脚本(scripts/harness-check.py)vs skill 内嵌;触发时机:发布前 DoD vs 定期 vs 手动。现有脱敏门用 scripts/desensitize.py 作发布前 DoD,校验脚本可并行。>

- [ ]  A. 独立脚本 + 发布前 DoD —— scripts/harness-check.py,与 desensitize.py 并列进发布门
- [ ]  B. skill 内嵌说明 + 手动触发 —— 脚本放 skill 目录,需要时手动跑,不进发布门
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [X]  C. 部分认定 ★推荐 —— 独立脚本放 scripts/(与 desensitize.py 并列),**首次迁移作为 DoD 强制跑**,之后手动/发布前可选;脚本输出「违规清单 + 0 违规提示」,不误报

## Q6. (V4 验收) 分层迁移的边界——「分层落地」做到什么程度算完成   [落盘: VISION#验收标准 + LLD#阶段拆分]

<出题依据:压测 Q6 裁决「一次性完整迁移,独立行动项带 DoD」。但「完整」的边界需定:只分 design/?还是 questionnaires/ + adr/ 也动?迁移范围扩大 → 断链风险与工作量上升。>

- [ ]  A. 只分 design/ —— 只重组 design/ 为 feature 子目录,questionnaires/ + adr/ 维持现状,最小迁移面
- [X]  B. 三件全分 —— design/ + questionnaires/(新归档子目录)+ adr/(按 feature 分组)全部按新规则重组,迁移面最大
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 分阶段:VISION 级定「分层规则」,迁移分两档——**必做档**:design/ 按 feature 聚合(现状混用最该治);**可选档**:questionnaires/ 新归档入子目录(存量不挪)+ adr/ 维持编号平铺(ADR 编号连续是硬约束,不因 feature 分组破坏)——迁移 DoD 以必做档为准,可选档标注 TBD

## Q7. (V4 验收) 校验脚本的检查项清单   [落盘: VISION#验收标准 + LLD#DoD]

<出题依据:压测 Q14 认定脚本检查「命名正则 / ADR 编号连续 / 归档位置」。需具体化检查项,决定脚本能报什么违规。现状可核实的违规源:命名不规范(如 feature-skill-* vs feature-skills-* 混淆)、ADR 编号跳号、归档文件不在 archive/。>

- [ ]  A. 只查命名正则 —— 问卷命名是否符合 feature-<slug></slug>-<stage></stage>-w<NN></nn> 等模式
- [X]  B. 命名 + ADR 编号 + 归档位置 —— 三合一:命名正则 + ADR 编号连续 + 归档文件位置
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— B 三合一为基线,但**保守实现**:只报「格式偏离」不报「内容语义」(如不判断 slug 是否合理);误报门 = 无违规时 0 输出;存量已偏离项(如 feature-skill-*)作为已知豁免清单,不报

## Q8. (V5 风险) 两套 skill 副本的同步策略   [落盘: VISION#风险 + LLD#阶段拆分]

<出题依据:VISION #19 默认「照 skill-spec-revamp 先例,仅脱敏差」。但 doctor-for-harness 含校验脚本(代码),脚本同步 = 复制字节,非「仅脱敏差」。需确认脚本在两套副本间的定位。>

- [ ]  A. 脚本只在仓库 skills/ —— 发布镜像含脚本,~/.claude 全局版不含(全局版只放 skill 文档,脚本从仓库取)
- [X]  B. 脚本双副本同字节 —— 仓库 + ~/.claude 都放同字节脚本,同步照旧(仅脱敏差)
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 脚本进仓库 `scripts/`(与 desensitize.py 并列,发布镜像唯一权威),~/.claude 全局版 SKILL.md 引用仓库脚本路径或复制同字节;同步策略照 skill-spec-revamp 先例(仅脱敏差),脚本复制不含脱敏(代码无命名)

## Q9. (V6 动机) 家族身份确认——第 9 个 skill 还是 dogfood 先行   [落盘: VISION#家族身份 + CLAUDE.md/CONTEXT 同步]

<出题依据:VISION #3 默认「第 9 个核心 skill,治理型横切」。但 OD-13 shadow 有「先不入家族、dogfood 先行」先例——若 doctor-for-harness 也先 dogfood(在真实 harness 上跑分层迁移),家族身份可后定。且「第 9 个」会触发 CLAUDE.md/CONTEXT 家族表述同步(8 → 9)。>

- [ ]  A. 直接入家族 —— 第 9 个核心 skill,同步 CLAUDE.md / CONTEXT / 落盘速查表
- [ ]  B. dogfood 先行 —— 先不入家族,在真实 harness 分层迁移上跑通,验证后再定家族身份(照 OD-13 shadow 先例)
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [X]  C. 部分认定 ★推荐 —— **先 dogfood 后入家族**:skill 设计与实现先做,分层迁移作为首个实战 dogfood;迁移验证通过后,家族表述同步「第 9 个」——一条行动项,避免过早承诺家族位
- [X]  就拿本项目做

## Q10. (V5 风险) 分层规则的权威落点——并入 SKILL.md 还是独立规范文档   [落盘: VISION#产物清单 + HLD#规范权威]

<出题依据:VISION #13 默认「规范可并入 SKILL.md 或独立文件」。分层规则是各 skill 落盘路径的权威引用(source),若并入 SKILL.md 则 SKILL.md 变长;若独立文件则多一个引用链。先例:引擎文件独立(QUESTIONNAIRE-FORMAT),骨架独立(STAGE-SKELETONS),SKILL.md 保持主流程。>

- [ ]  A. 并入 SKILL.md —— 分层规则作为一节写进 SKILL.md,单文件自包含
- [X]  B. 独立规范文档 —— 如 HARNESS-RULES.md,SKILL.md 引用;规则与主流程解耦,可独立修订
- [ ]  🤔 我定不了 → 推迟/降风险

- ✍️ 自定义: __________

- [ ]  C. 部分认定 ★推荐 —— 独立规范文档(HARNESS-RULES.md 或并入 DESIGN.md),SKILL.md 只写主流程 + 引用;拆分层规则为「被各 SKILL.md 引用」的权威源,与引擎/骨架独立文件先例一致

## 补充声明

> **用户作答(2026-08-08,对话速答)**:「我已答完,重新读文档」——裁定 = 10 题全部按 ★推荐 落盘(C 选项),无改题。agent 逐字转写:处理时重读 VISION 与前置文档后逐题落盘。

---

## 处理报告摘要(W01,2026-08-08)

- **preview 统计**:10 题全采纳 ★推荐(C),0 逃生舱,0 自定义。取消默认率 0/10 = 0%。
- **格式缺陷修复**:出题时漏了 ✍️ 自定义行(违反 FORMAT 规则 4)→ 用户指出后批量补上;**教训记入本摘要,防再犯**。
- **落盘**:VISION 更新(`harness/design/doctor-harness/VISION.md`)——追加「关键决策具体化」节(10 条裁定)+ 家族身份改为「先 dogfood 后入家族」;无 ADR(分层 ADR 待迁移涉链接时补);无 OD 升格。
- **下一阶段**:vision 覆盖清单 + 阶段闸门(用户确认后进 HLD)。
