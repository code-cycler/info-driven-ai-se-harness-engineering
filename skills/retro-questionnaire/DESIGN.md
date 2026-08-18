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

## 引擎同步记录(2026-08-03)

- **预勾选开关化 + 选项排序统一**(OD-14 修订,用户裁决,action-Q 确认清单 confirm-pregou-switch-w00 全确认):
  - 预勾选 = **opt-in 开关,默认关**——仅当用户启动 skill 时明确说「预勾选」才预勾推荐选项;未启用时全部 `[ ]`;
  - **选项排序(非推荐在前 → 逃生舱倒数第二 → 推荐最后)= 默认行为,不依赖开关**;
  - **单向门题(发布/删除/花钱/脱敏)永不预勾**;预勾设防(取消率 / 确认点 / 3 波零取消警告)开关开启时适用;
  - 本 skill 与 design-Q / grill-Q / retro-Q / action-Q **四份副本同步**(OD-8 重访触发①命中);问题级排序仅 design-Q 保留。
- **实测与调研前置标准流程**(2026-08-03,action-Q 确认清单 confirm-testing-preflight-w00 全确认):SKILL.md「生成问卷」前新增标准步骤「实测与调研前置」(调研现状 / 不假设 / 多实测 / 多获取信息 / 及时保存);retro-Q 版为「调研与核实前置」(五源读取的补齐);既有铁律段(环境现实现证 / 先验证再出题 / 先核实再列清单)保留引用。

## skill-spec-revamp 同步记录(2026-08-06/07,OD-8 重访触发①)

> ⚠️ **2026-08-07 superseded**:本节记录的方案 R(落盘路径配置化)已放弃,回归硬编码 `harness/`(见 ADR-0011)。本节内容为历史叙述保留(原始信息不丢失铁律),**不再有效**——其中描述的 `<根>` / `<落盘根>` 配置化机制已撤销,PROCESSING-RULES / SKILL / QUESTIONNAIRE-FORMAT / RETRO-SKELETONS 已回硬编码 `harness/`。Q7 retro 文档落点 `docs/retro/` 不变(项目固有,本就独立于方案 R 边界);skill 内部 `./docs/...` 引用不动。
>
> 历史背景:方案 R 于 2026-08-07 在 `~/.claude/skills/` 落地,但本仓库 `skills/`(发布镜像)从未同步方案 R——仓库版一直在硬编码状态。ADR-0011 决定撤销运行版方案 R、回归硬编码后,两边状态一致(均硬编码 `harness/`)。以下为运行版当时的同步记录,保留作历史。

- **落盘路径配置化同步(仅运行版 `~/.claude/skills/` 曾落地)**:运行版本 skill(PROCESSING-RULES 落盘映射 + 落盘根定义 + SKILL 路径决定 + QUESTIONNAIRE-FORMAT 文件约定 + RETRO-SKELETONS 问卷归档)曾与 design-Q canonical 同步——路径配置化为 `<根>` / `<落盘根>`,四 skill(design-Q / grill-Q / retro-Q / action-Q)沿用同一根约定(方案 R)。
- 🔧 **Q7 retro 文档项目固有**:retro 文档落点 = `docs/retro/`(项目阶段历史档案,人读、长期保存),**不纳入落盘根配置化**(落盘根边界 = 通用三件 design/ + questionnaires/ + adr/);SKILL.md / RETRO-SKELETONS / 本 DESIGN 决策索引的 `docs/retro/` 保持不动。
- 🔧 **Q7 路径区分**:本 skill DESIGN.md / SKILL.md 内 `[docs/...](./docs/...)` 为 skill 自身目录内部引用(VISION / hld_v1 / 归档问卷),**不动**;配置化只改「描述宿主项目落盘路径」的字符串。
- 🔧 **Q5 同步范围**:仅「落盘映射节」diff 0;retro-Q 有意分叉区(RETRO-SKELETONS 四节骨架 / 不使用 preview / 调研与核实前置五源)原样保留。
- HLD/LLD 判别法则 + 最小必含 = design-Q 专属骨架,**不扩散**到 retro-Q(RETRO-SKELETONS 是方法论四节 + Action Items,性质不同)。

## 引擎同步记录(2026-08-18,first-principles W01 补充声明)

- QUESTIONNAIRE-FORMAT **规则 4 修正**:「✍️ 自定义」位置由「紧跟 🤔 逃生舱之后」改为「紧跟所有选项(含 ★推荐)之后、固定为题目最后一位」——消除与规则 13(选项排序:推荐居末)的顺序矛盾;该矛盾是「✍️ 行结构性遗漏」的根源(grill-Q first-principles W01 曾 10 题全漏,靠出题自检 grep 抓回)。
- grill-Q / retro-Q 的模板示例同步更新为规则 13 选项顺序(★推荐从 A 位移至 🤔 之后的 C 位,✍️ 行标注「题目最后一位」);design-Q / action-Q 模板本已合规,仅规则 4 措辞统一。
- 四副本 × 双侧(repo `skills/` + 全局 `~/.claude/skills/`)同批同步,无新有意分叉(OD-8/OD-11 边界不变)。
\n