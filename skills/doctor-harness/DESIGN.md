# doctor-harness · 设计文档

> 本 skill 的设计决策记录 + 演进留痕索引。
> 设计套:harness/design/doctor-harness/(VISION / HLD / LLD);决策依据:ADR-0012 / ADR-0013 / ADR-0011 + OD-15。

## 起源(2026-08-08)

压测 [grill-harness-file-mgmt-w01](../../harness/questionnaires/archive/grill-harness-file-mgmt-w01.md) 发现:harness 文件管理规格「简单未考虑实际情况」——无层次化设计、feature/子项目无单独文件夹、边缘与实际工程场景未覆盖。用户裁决(补充声明):harness 文件**严格**归 `harness/` 父级 + 子文件夹分层,不污染项目根;设计 skill 处理演进。立项 [OD-15](../../docs/OPEN-DECISIONS.md)。

## 关键决策记录(W00/W01 全采纳)

| # | 决策点 | 裁定 | 出处 |
|---|---|---|---|
| V1 | 核心目标 | harness 演进治理四职责:组织规则权威化 / 迁移 + 断链回归 / 布局校验 / 演进留痕 | VISION W00 #1 |
| V2 | 家族身份 | **先 dogfood 后入家族**——分层迁移验证通过后,家族表述同步「第 9 个」 | VISION W01 Q9 |
| V3 | 管辖边界 | 只管 harness/ 三件;不碰 CONTEXT/OD/TODO 项目固有文件 | VISION W00 #4/#5 |
| V4 | 分层判定句 | feature 级(可独立引用/冲突)建 design/<feature>/,全局设计裸放 | ADR-0012 |
| V5 | 归属判据 | 独立 CLAUDE.md/git/发布边界 → 独立 harness,否则归主根 | ADR-0012 |
| V6 | 归档规则 | 新归档按 feature/主题建子目录;存量不挪;README 索引 | VISION W01 Q3 |
| V7 | 校验脚本 | scripts/harness-check.py,三检查(命名/ADR 编号/归档位置),0 违规 0 输出 | VISION W01 Q5 |
| V8 | 迁移方式 | 一次性完整迁移 + 断链回归,不自动化脚本 | ADR-0013 |
| V9 | 规范落点 | HARNESS-RULES.md 独立文档,各 SKILL.md 引用不复制 | VISION W01 Q10 |
| V10 | 脚本双副本 | 脚本进仓库 scripts/,~/.claude 引用或复制同字节 | VISION W01 Q8 |

## 演进记录

| 日期 | 变更 | 原因 |
|---|---|---|
| 2026-08-08 | 设计套完成(VISION/HLD/LLD + ADR-0012/0013) | 压测产出 direction,用户裁决先设计后实现 |
| 2026-08-08 | P1 规则权威:HARNESS-RULES.md 起草 + 6 skill 引用句 | LLD P1 |
| 2026-08-08 | P2 校验脚本:harness-check.py 实现 + 现状跑通/违规样本验证 | LLD P2 |
| 2026-08-08 | P3 分层迁移:design/ 天然分层确认 + 归档 9 处层级链接修复 | LLD P3(dogfood) |
| 2026-08-08 | P4 双副本 + 家族表述(本 DESIGN) | LLD P4;家族表述待迁移验证通过后落第 9 个 |

## 未验证假设台账

- 无(纯 Markdown + 纯 Python 标准库脚本,无外部依赖;压测/设计期关键事实已核实)。

## 家族身份状态

**pending**:先 dogfood 后入家族(OD-15 重访触发②)。分层迁移已验证通过(F019 passes:true),家族表述同步「第 9 个」待用户确认后落地(CLAUDE.md 家族图 / CONTEXT skill 家族节 / 落盘速查表)。