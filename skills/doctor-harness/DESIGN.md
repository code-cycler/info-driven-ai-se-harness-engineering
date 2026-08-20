# doctor-harness · 设计文档

> 本 skill 的设计决策记录(定位 / 设计决策 / 已知限制三节);治理历史见 [CHANGELOG.md](./CHANGELOG.md)。
> 设计套:harness/design/doctor-harness/(VISION / HLD / LLD);决策依据:ADR-0012 / ADR-0013 / ADR-0011 + OD-15。

## 设计决策

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
| V11 | 「dogfood 通过」定义 | = 用 doctor-harness 的 HARNESS-RULES(判定句核对)+ harness-check(脚本校验)+ MIGRATION-FLOW(迁移流程)完整走通一次真实 harness 场景(F019 分层迁移符合即通过) | grill-Q Q7 回灌 |
| V12 | 治理历史职责 | 载体(CHANGELOG/FORK-NOTES/DOGFOOD-LOG/STATUS-LOG)布局与增量记录归本 skill 第七职责面(HARNESS-RULES 第九节) | ADR-0024 |

## 已知限制

- 未验证假设台账:无(纯 Markdown + 纯 Python 标准库脚本,无外部依赖;压测/设计期关键事实已核实)。
- 本 skill 无规则本体级分叉,故无 FORK-NOTES(双侧差异仅 CHANGELOG 历史层,由 sync-check 类规则管)。