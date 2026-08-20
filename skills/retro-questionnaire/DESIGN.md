# retro-questionnaire · DESIGN(决策索引)

> 本 skill 的设计决策索引;治理历史(创建起源/引擎同步与漂移时间线)见 [CHANGELOG.md](./CHANGELOG.md);有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。
> 由 design-questionnaire 设计(vision W1/W2 + hld W1 三波问卷,两道闸门通过,坍缩 LLD 直接实现);问卷归档于 [docs/questionnaires/archive/](./docs/questionnaires/archive/),完整论证见 [docs/VISION.md](./docs/VISION.md) 与 [docs/design/hld_v1.md](./docs/design/hld_v1.md)。

## 决策索引

| 决策 | 结论 | 出处 |
|---|---|---|
| 核心目标 | 防省略(有触发、有结构、有落盘) | vision-w01 Q1 |
| 触发 | 阶段 DoD 核验后 agent 主动提议 + 手动随时(类似 memory) | vision-w01 Q2/Q2.1 + 自定义 |
| 题型 | 与决策题同构;反思题选项 = 常见原因假设清单 | vision-w01 Q3 |
| 不做 | 不自动修改设计文档 | vision-w01 Q4 |
| 架构偏离 | 只记录,后续动作由人发起 | vision-w01 Q5 |
| 验收标准 | 一次真实阶段复盘走通闭环 | vision-w01 Q6 |
| 风险缓解 | 复盘问题 → 行动项落 TODO.md,四时机必读 | vision-w02 Q1 自定义 |
| 落盘命名 | `docs/retro/<主题>_vN.md`(项目固有,不纳入落盘根边界) | vision-w01 Q8 + Q7 深钻 |
| 引擎复用 | 复制两份 + 四方声明 + 漂移声明是否为设计(OD-8/OD-11) | hld-w01 Q1 + 自定义 |
| 骨架结构 | 方法论四节 + Action Items;§0 上份 Action Items 回顾 | hld-w01 Q2 |
| 出题数据源 | 五源(设计文档 / git log / TODO.md / 上份 retro / 对话有价值内容) | hld-w01 Q3 + 自定义 |
| 防漂移同步 | 引擎修改在四方 DESIGN.md 各记一笔 | hld-w01 Q4 |
| 作用对象 | 宿主项目(问卷、retro 文档、TODO.md 均落宿主项目) | hld 处理报告推导 |

## 引擎副本声明(现行)

- 本目录 QUESTIONNAIRE-FORMAT.md / PROCESSING-RULES.md 复制自 design-questionnaire(canonical);四方副本修改需考量四方同步;本 skill 有意分叉见 [FORK-NOTES.md](./FORK-NOTES.md)。
- 历史漂移与同步事件(2026-07-24 同步 / 07-25、07-27 preview 漂移声明为设计 / 08-03 / 08-06-07 方案 R 同步与撤销 / 08-18 规则 4 修正)见 CHANGELOG。
