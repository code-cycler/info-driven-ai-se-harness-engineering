# VISION · doctor-for-harness

> 来源:design-questionnaire feature 模式 vision 阶段 W00(2026-08-08,20/20 全采纳预答)+ [W01](../../questionnaires/archive/doctor-harness/feature-doctor-harness-vision-w01.md)(10/10 全采纳 ★推荐)。
> 上游决策:[OD-15](../../../docs/OPEN-DECISIONS.md)(立项)+ [ADR-0011](../../adr/0011-abandon-plan-r-hardcode-harness.md)(硬编码 harness/)+ 压测 [grill-harness-file-mgmt-w01](../../questionnaires/archive/harness-file-mgmt/grill-harness-file-mgmt-w01.md)(14 题,用户裁决)。
> 本文件 = doctor-for-harness 的构想层;架构设计见 HLD,落地规格见 LLD(后续阶段产出)。

## 目标

建立 **doctor-for-harness** 作为 **harness 演进治理 skill**,四项职责:

1. **组织规则权威化** —— 分层定义 + 归属判据 + 命名规范,一处权威,不靠 agent 临场判断;
2. **迁移工具/流程** —— 目录重组 + 相对链接重算 + 断链回归;
3. **布局合规校验** —— 命名正则 / ADR 编号连续 / 归档位置,可脚本化检查;
4. **演进记录** —— 组织变更留痕,可回溯「harness 为什么长这样」。

**受益对象**:维护者本人 + AI 代理(Claude Code),与既有 8 skill 定位一致。

**家族身份**:治理型、横切属性(类似 delegate 横切任意环节,不锁死在线性阶段);**先 dogfood 后入家族**(W01 Q9 裁定)——设计与实现先做,harness 分层迁移作为首个实战 dogfood,验证通过后家族表述同步「第 9 个」。

## 范围

### 做(管辖边界)

- `harness/` 区三件(`design/` + `questionnaires/` + `adr/`)的**组织、迁移与校验**;
- 分层规则 / 归属判据 / 命名规范的定义与权威化;
- 迁移工具与流程(目录重组 + 链接重算 + 断链回归)。

### 不做(边界与约束)

- **不碰** CONTEXT.md / OPEN-DECISIONS.md / TODO.md / docs·retro/ 项目固有文件(除非确需修订先例);
- **不重写**问卷引擎(QUESTIONNAIRE-FORMAT / PROCESSING-RULES);
- **不替** OD-8(引擎副本)/ OD-10(分发洁净)/ OD-12(grill 处置)决策;
- **不改**方法论三块内容;
- **不推翻** ADR-0011 的「硬编码 harness/」——分层是 harness **内部**组织形态,不是落盘根配置化回归。

### 与既有 skill 落盘路径的关系

doctor-for-harness 的规范文档成为各 skill 落盘路径的**权威引用**(source);各 SKILL.md 仍硬编码 `harness/`(ADR-0011),分层规则由 doctor-for-harness 文档承载、被 SKILL.md 引用,不逐 skill 内联复制(反漂移)。

### 第一个治理任务

**harness 分层落地**(本仓库):现状 design/ 子目录与裸放混用 → 按分层规则重组 + 迁移 + 断链回归,作为 doctor-for-harness 设计与实现的**首个实战**(dogfood)。

### 本次产物

设计文档(doctor-for-harness VISION / HLD / LLD + 必要的 ADR/OD 修订)+ 实现(新 skill 文件 + 校验脚本 + 分层迁移执行);分层迁移作为独立行动项带 DoD,不随设计自动执行。

## 核心场景

| # | 场景 | 描述 |
|---|---|---|
| A | 新 feature 设计启动 | agent 按分层规则决定新 feature 的 design/ 建不建子目录、问卷/ADR 落哪——规则一处权威,不靠临场判断 |
| B | harness 结构迁移 | 需要重组 harness 目录时执行迁移流程:设计新布局 → 挪文件 → 相对链接重算 → 断链回归 → 规格同步 |
| C | 布局合规校验 | 定期/发布前跑校验脚本,检查 harness 布局合规(命名正则 / ADR 编号连续 / 归档位置) |
| D | 演进留痕 | harness 组织变更(迁移/规则修订)记录在案,可回溯 |

## 验收标准

- **产物清单**:新 skill 目录 `skills/doctor-harness/` = SKILL.md + DESIGN.md + 校验脚本(`scripts/harness-check.py`)+ 规范权威文档(分层规则 / 归属判据 / 命名规范,可并入 SKILL.md 或独立文件);
- **校验脚本事实 DoD**:对当前仓库跑能准确报出真实违规;分层迁移后跑 0 违规 + 0 断链;错误不误报(无违规时 0 输出);
- **分层迁移 DoD**:本仓库 harness/ 分层完成(design/ 按 feature 聚合、archive/ 按 feature/主题聚合或用户裁决形态)、相对链接全部重算、断链回归 0 新增、各 SKILL.md 引用同步;
- **家族回归**:不破坏既有 8 skill 的触发/落盘/引擎机制;CLAUDE.md 家族图 / CONTEXT skill 家族节 / 落盘速查表同步第 9 个。

## 关键决策具体化(W01,10/10 ★推荐)

> 本节把 vision 层的决策点落到可执行粒度;架构/接口细节进 HLD,阶段拆分进 LLD。

| # | 决策点 | 裁定 |
|---|---|---|
| Q1 | 动机 | 演进是常态(新 feature 持续产生、规范持续修订)→ 立治理 skill;**约束最小可用**:只做「规则权威 + 迁移流程 + 校验脚本 + 留痕」四件事,脚本可复用、流程可手动跟随,不预设自动化框架 |
| Q2 | design/ 分层判定句 | feature 级设计(会被独立引用 / 与其它 feature 冲突)建 `design/<feature>/`;全局/单文件设计裸放根下。**存量定案**:methodology 系列(VISION.md/hld_v2/lld_v2/hld-methodology-separation)是全局设计 → 裸放保留;feature 系列(repo/skill-spec-revamp/feature-skills-harness-consistency)已建目录 → 保留;判定句进文档,存量逐条核对 |
| Q3 | archive/ 组织 | 新归档按 feature/主题建子目录(医生 skill 迁移流程管);**存量不挪**(信息不丢失 + 链接不动);补归档 README 索引过渡;子目录化随自然演进 |
| Q4 | 归属判据 | 子模块有独立 CLAUDE.md / git / 发布边界 → 独立 harness;否则归主根。**下沉轻量规则**(DESIGN.md 非 ADR):个人单仓库基本不触发,等价「默认归主根,子模块独立时另建」;前端落盘前轻量校验(pwd 归属)防误落 |
| Q5 | 校验脚本触发 | 独立脚本 `scripts/harness-check.py`(与 desensitize.py 并列);**首次迁移作为 DoD 强制跑**,之后手动/发布前可选;输出「违规清单 + 0 违规提示」,不误报 |
| Q6 | 迁移边界 | 分两档:**必做档** = design/ 按 feature 聚合(现状混用最该治);**可选档** = questionnaires/ 新归档入子目录(存量不挪)+ adr/ 维持编号平铺(ADR 编号连续是硬约束)。迁移 DoD 以必做档为准,可选档标 TBD |
| Q7 | 校验检查项 | 三合一(命名正则 + ADR 编号连续 + 归档位置);**保守实现**:只报格式偏离不报内容语义;误报门 = 无违规时 0 输出;存量已偏离项(如 feature-skill-*)作已知豁免清单 |
| Q8 | 脚本双副本 | 脚本进仓库 `scripts/`(发布镜像唯一权威);~/.claude 全局版 SKILL.md 引用仓库脚本路径或复制同字节;同步照 skill-spec-revamp 先例(仅脱敏差),脚本复制不含脱敏 |
| Q9 | 家族身份 | 先 dogfood 后入家族(见「家族身份」节);迁移验证通过后家族表述同步「第 9 个」——一条行动项,避免过早承诺 |
| Q10 | 规范权威落点 | 独立规范文档(HARNESS-RULES.md),SKILL.md 只写主流程 + 引用;分层规则为「被各 SKILL.md 引用」的权威源,与引擎(QUESTIONNAIRE-FORMAT)/骨架(STAGE-SKELETONS)独立文件先例一致 |

## 风险与约束

| 风险 | 约束/缓解 |
|---|---|
| 与 ADR-0011 关系 | 分层不推翻硬编码;分层规则记 doctor-for-harness DESIGN.md(双向门),若迁移涉及既有链接破坏则补 ADR |
| 迁移断链风险 | 一次性完整迁移 + 断链回归,不渐进半途(先例:2026-08-05 harness 迁移曾 96 断链 → 7 豁免) |
| 两套 skill 副本同步 | 本仓库 `skills/` 与 `~/.claude/skills/` 需同步新 skill(照 skill-spec-revamp 先例,仅脱敏差) |
| 过度工程风险 | 规则只覆盖真实已出现的场景(分层/归属/命名/校验),不预设过度机制;最小可用优先 |