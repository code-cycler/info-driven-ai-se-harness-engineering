---
name: doctor-harness
description: harness 演进治理 skill——处理「项目根/harness/」区(design/ + questionnaires/ + adr/)的组织规则权威化、迁移工具/流程、布局合规校验与演进留痕。harness 文件**严格**归 `harness/` 父级 + 父级下子文件夹分层,不污染项目根;分层规则见 HARNESS-RULES.md(唯一权威源)。触发:harness 分层/重组、harness 文件迁移、校验 harness 布局、「harness 怎么放」「这个文件放哪」、harness 组织混乱需要治理。Use when harness file organization, migration, or layout validation is needed.
---

<what-to-do>

处理 harness 区(`项目根/harness/`)的**演进治理**:组织规则权威化 + 迁移 + 校验 + 留痕。harness 文件**严格**归 `harness/` 父级,内部按 feature/主题分层子文件夹,**不污染项目目录结构**。

## 铁律(不可违反)

1. **AI 不替人决策** — 规则修订、迁移执行与否由人决定;agent 提供方案与校验结果。
2. **只组织,不替改** — 压测/校验产出发现与建议,不直接重排用户未授权的目录;迁移作为独立行动项带 DoD,人发起。
3. **原始信息不丢失** — 迁移只移不删,文件名不变;归档不重排存量。
4. **规则一处权威** — HARNESS-RULES.md 是唯一权威源;各 skill SKILL.md 只引用「分层见 HARNESS-RULES.md」,不内联复制。
5. **不推翻 ADR-0011** — 分层是 harness **内部**组织形态,不回归落盘根配置化;`harness/` 硬编码不动。

## 主流程

### 0. 触发与定模

- **手动触发**:「分层一下」「校验 harness」「harness 文件怎么放」;或 harness 组织混乱(design/ 混用、命名偏离、归档膨胀)时。
- **判定**:本次是要① 组织规则(落到 HARNESS-RULES.md)② 迁移执行(重组目录)③ 校验(跑脚本)④ 留痕(记录变更)——可单独或组合。

### 1. 规则权威(组织规则)

- 读 [HARNESS-RULES.md](./HARNESS-RULES.md)(唯一权威源),确认是否覆盖当前场景:
  - **分层定义**:design/<feature>/ 判定句(feature 级 = 会被独立引用/与其它 feature 冲突 → 子目录;全局/单文件设计裸放);
  - **归属判据**:子模块有独立 CLAUDE.md/git/发布边界 → 独立 harness,否则归主根;
  - **命名规范**:init/feature/grill/retro/confirm 各模式正则 + 豁免清单;
  - **归档规则**:新归档按 feature/主题建子目录,存量不挪,README 索引。
- 规则有缺口(新场景未覆盖)→ 起草修订建议,人确认后更新 HARNESS-RULES.md + CHANGELOG 留痕。

### 2. 迁移流程(重组 + 断链回归)

有目录重组需求时(如本次分层落地),执行 [MIGRATION-FLOW.md](./MIGRATION-FLOW.md) 的 7 步流程:

1. **设计新布局**(判定句逐条核对归属)→ 2. **挪文件**(git mv 只移不删)→ 3. **相对链接重算**(归档问卷层级)→ 4. **断链回归**(本次引入 0)→ 5. **跑校验**(harness-check.py 0 违规)→ 6. **规格同步**(SKILL.md 引用)→ 7. **留痕**(CHANGELOG)。

### 3. 布局合规校验

- **脚本**:`python3 scripts/harness-check.py [harness_root]`——三检查(问卷命名正则 / ADR 编号连续 / 归档位置),0 违规时无输出(误报门)。
- **触发**:迁移作为 DoD 强制跑;之后手动/发布前可选;不进任何 skill 每次流程。
- 违规清单 → 人决定是否修(agent 给修订方向,不擅自改)。

### 4. 演进留痕

- 每次迁移/规则修订,在 doctor-harness [CHANGELOG.md](./CHANGELOG.md) 追加一条(日期 + 变更 + 原因),可回溯「harness 为什么长这样」。

## 与家族的分工

| skill | 场景 | 与 doctor-harness 关系 |
|---|---|---|
| design-Q / grill-Q / retro-Q / action-Q | 生成问卷 / 压测 / 复盘 / 行动确认 | 落盘路径按 HARNESS-RULES.md 分层(引用不复制) |
| long-running | 跨会话实现 | 从 harness/questionnaires/archive/ 重建上下文,遵循分层归档 |
| delegate | 决策下放 | 横切;harness 组织决策默认不下放(规则权威在人) |

**衔接**:doctor-harness 是横切治理 skill,不锁死在线性阶段;任何 skill 落盘遇到「放哪」歧义时,按 HARNESS-RULES.md 裁决。

</what-to-do>

<supporting-info>

- harness 组织权威规则(唯一 source):[HARNESS-RULES.md](./HARNESS-RULES.md)
- 目录迁移执行流程:[MIGRATION-FLOW.md](./MIGRATION-FLOW.md)
- 演进变更记录:[CHANGELOG.md](./CHANGELOG.md)
- 校验脚本:`python3 scripts/harness-check.py`(仓库 `scripts/`,与 desensitize.py 并列)
- 本 skill 设计决策记录:[DESIGN.md](./DESIGN.md) + 设计套 `harness/design/doctor-harness/`(VISION/HLD/LLD)
- 决策依据:[ADR-0012](../../harness/adr/0012-harness-layering-rule.md)(分层规则)+ [ADR-0013](../../harness/adr/0013-harness-layering-migration.md)(迁移执行)+ [ADR-0011](../../harness/adr/0011-abandon-plan-r-hardcode-harness.md)(硬编码 harness/)

</supporting-info>