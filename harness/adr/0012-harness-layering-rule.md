# ADR-0012: harness 内部组织形态——分层规则(平铺 vs 按 feature 聚合)

- 状态:proposed→accepted(2026-08-08,design-Q hld W00 #13 裁定:立 ADR)
- 日期:2026-08-08

## 背景

harness 文件管理规格(ADR-0011 硬编码 `项目根/harness/`)只定义了落盘根,未定义 harness **内部**的组织形态(design/ + questionnaires/ + adr/ 三件如何组织)。现状已出现两种形态并存:

- `harness/design/` 下:子目录(`repo/`、`skill-spec-revamp/`、`feature-skills-harness-consistency/`)与裸放文件(`VISION.md`、`hld_v2.md`、`lld_v2.md`、`hld-methodology-separation.md`)共存;
- 规格(SKILL.md「阶段文档 → `harness/design/`」)未声明子目录机制,新会话 agent 无法从规格判断新 feature 该建目录还是裸放。

压测源头:[grill-harness-file-mgmt-w01](../questionnaires/archive/harness-file-mgmt/grill-harness-file-mgmt-w01.md)(2026-08-08 Q2/Q3 认定「规格缺失层次化规则,现状已混用」)。用户裁决:harness 文件**严格**归 `harness/` 父级 + 父级下子文件夹分层,**不污染项目根**。

## 决策

1. **分层规则**(harness 内部组织形态,不推翻 ADR-0011 的硬编码根):
   - **design/ 分层判定句**:feature 级设计(会被独立引用 / 与其它 feature 冲突)建 `design/<feature-slug>/` 子目录;全局/单文件设计(如 methodology 修订)裸放 `design/` 根下。
   - **归属判据**:子模块有独立 CLAUDE.md / git / 发布边界 → 子模块根建自己的 `harness/`;否则归主根。
   - **命名规范**:问卷命名保持 S2 各模式(init/feature/grill/retro/confirm),slug 规范见 HARNESS-RULES.md。
   - **归档规则**:新归档按 feature/主题建 `archive/<feature>/` 子目录;存量不挪(信息不丢失 + 链接不动);补归档 README 索引过渡。
2. **规则权威落点**:完整分层规则(判定句 + 归属判据 + 命名规范 + 归档规则)记 **HARNESS-RULES.md**(doctor-for-harness 独立规范文档),被各 SKILL.md 引用(「分层见 HARNESS-RULES.md」),不逐 skill 内联复制。
3. **迁移执行**:分层落地(本仓库现状重组)作为独立行动项带 DoD,见 [ADR-0013](0013-harness-layering-migration.md)。

## 替代方案(被否决项)

- **维持平铺 + 文件名前缀区分**:现状继承自安装初版,无权衡记录。否决——多 feature 并行时跨目录碎片化,回读成本高;压测 Q3/Q5 认定归档/设计检索成本随生命周期线性增长。
- **全部进子目录(design/ 根下零裸放)**:规则最简单,但方法论修订等全局/单文件设计也进目录,过度结构化。否决——保留裸放区给全局设计。
- **doctor-for-harness 只做迁移工具不立规则**:一次迁移后无常态机制。否决——harness 持续演进(新 feature / 规范修订),需要规则权威 + 迁移 + 校验常态职责。

## 后果

- (+) 分层规则一处权威,新会话 agent 按判定句决定建目录/裸放,不靠临场判断;
- (+) 跨目录碎片化缓解:feature 级产物可聚合回读(design/<feature>/)。
- (−) 存量已偏离项(如 feature-skill-* vs feature-skills-* 近似 slug)作为已知豁免清单,不清扫(最小可用,不追求全量规范);
- (−) 分层迁移会破坏既有相对链接,需一次性迁移 + 断链回归(见 ADR-0013)。