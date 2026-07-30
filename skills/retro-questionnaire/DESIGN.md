# retro-questionnaire · DESIGN(决策索引)

> 本 skill 由 design-questionnaire 设计(2026-07-23 至 2026-07-24):vision W1/W2 + hld W1 三波问卷,两道闸门通过,坍缩 LLD 直接实现。
> 问卷全部归档于 [docs/questionnaires/archive/](./docs/questionnaires/archive/);完整论证见 [docs/VISION.md](./docs/VISION.md) 与 [docs/design/hld_v1.md](./docs/design/hld_v1.md)。本文档是决策索引与引擎副本声明。

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
| 落盘命名 | `docs/retro/<主题>_vN.md` | vision-w01 Q8 |
| 引擎复用 | 复制两份 + 双向声明 + 漂移声明是否为设计 | hld-w01 Q1 + 自定义 |
| 骨架结构 | 方法论四节 + Action Items | hld-w01 Q2 |
| 出题数据源 | 五源(设计文档 / git log / TODO.md / 上份 retro / 对话有价值内容) | hld-w01 Q3 + 自定义 |
| 防漂移同步 | 引擎修改在两个 skill 的 DESIGN.md 各记一笔 | hld-w01 Q4 |
| 作用对象 | 宿主项目(问卷、retro 文档、TODO.md 均落宿主项目) | hld 处理报告推导,闸门无异议 |

## 引擎副本声明

- 本目录的 [QUESTIONNAIRE-FORMAT.md](./QUESTIONNAIRE-FORMAT.md)、[PROCESSING-RULES.md](./PROCESSING-RULES.md) 复制自 design-questionnaire(design-Q 为 canonical;2026-07-24 复制)。
- 现共三份副本方:design-Q(canonical)、retro-Q、grill-Q。修改任一方引擎时,需考量是否同步另两方,并在**三处** DESIGN.md 各记一笔。
- 当前漂移:三个副本文件头部各加了一行副本标记注释 —— **声明:此为设计**(便于识别副本身份);grill-Q 副本另补了本 skill 导读行。除此之外无漂移。
- **2026-07-24 引擎同步(无漂移)**:PROCESSING-RULES 降风险协议 step 1 + 落盘映射——双向门逃生舱改为「采用推荐项 + 进 OD 标注」。来源:grill-Q dogfood W01 补充声明(design-Q DESIGN.md D22)。本副本已同步,与 canonical 一致。
- **2026-07-27 引擎漂移(本 skill 不同步,声明为设计)**:design-Q canonical 演进——preview 拆独立 W00 波(勾=采纳/留空=不采纳、无 🤔)。本 skill(retro-Q)**不使用 preview**(复盘问卷题量小、通常一波,且题型是反思原因假设清单,不适合 yes/no 默认值预答),故不同步该引擎改动;FORMAT/RULES 副本维持 2026-07-24 版本。项目B dogfood Q5-A 判定:复盘场景 preview 价值不抵复杂度。三方协议下,此漂移**声明为设计**(非遗漏)。
- **2026-07-25 引擎修改(design-Q dogfood 发起,本副本暂未同步)**:design-Q 在 QUESTIONNAIRE-FORMAT 增加「preview 预答层」规范(文件结构模板 + 规则 13)、PROCESSING-RULES 增加 preview 预答解析与处理报告统计行。来源:delegate × design-Q dogfood round 1(宿主项目某 dogfood 问卷)。先只在 design-Q 生效(dogfood 验证中),验证有效后回同步——**声明:此漂移为设计**。
