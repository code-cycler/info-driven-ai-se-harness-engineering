---
mode: feature
wave: 0
stage: hld
created: 2026-08-06
status: processed
---
# 问卷 hld W00 · Preview(决策默认值 yes/no 速答)

> **本阶段定位**:三组改动的**架构方案**——改动落哪些 skill 文件、方案 R 怎么落进 skill 机制、骨架新结构、副本同步契约、ADR 识别。判别法则精确表述 + 每项「最小必含」子项等开放型深究留 W01。
> **feature 模式 hld 裁剪**:H1 = 新增/修改哪些 skill 文件、现有 skill 哪些行为会变;H2 = 方案 R 与现有 skill 机制契合;H3 = skill 内部 + 副本间契约;H4 = skill 生效与维护;H5 = ADR 识别。
>
> **作答规则**:
>
> - opt-in 开关未启用,全部 `[ ]`,人逐条作答
> - **勾 `[x]` = 采纳默认**;**留空 = 不采纳** → 转 W01 深究
> - 本阶段无单向门(改 skill 规格可回退)
> - 不用 🤔;真定不了 → 留空转 W01
>
> 默认来源标注于〔〕。

## 决策默认值清单

### H1 系统架构(skill 文件改动地图)

- [X]  **1 改动落点文件清单**:design-Q 改 4 个文件——① [STAGE-SKELETONS.md](../../../../../.claude/skills/design-questionnaire/STAGE-SKELETONS.md(改动 2/3:判别法则 + 最小必含 + 产出形态 + 分档);② [SKILL.md](../../../../../.claude/skills/design-questionnaire/SKILL.md(改动 1:路径决定逻辑,3 处 docs/ 字符串);③ [PROCESSING-RULES.md](../../../../../.claude/skills/design-questionnaire/PROCESSING-RULES.md(改动 1:落盘映射表 docs/ → 配置化根);④ [DESIGN.md](../../../../../.claude/skills/design-questionnaire/DESIGN.md(记决策 D23+)。四副本同步 = grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md(落盘映射)+ SKILL.md(路径字符串) 〔探索确认漂移面;改动 2/3 骨架仅 design-Q 有,改动 1 路径四份都有〕
- [X]  **2 骨架(STAGE-SKELETONS.md)新结构 = 四块**:① 头部新增「HLD/LLD 判别法则」节(定义 + 判别问句);② 每项加「最小必含」子项清单(硬约束);③ 每项加「产出形态」建议(表格/清单/契约/图);④ 坍缩档分档(完整三阶段全量 / 坍缩 hld / 坍缩 lld 精简)。现有骨架表(vision/hld/lld 三表)保留,四块作为增强层叠加 〔VISION 改动 2/3;lld_v2「§2.1 四必含」先例;repo/HLD 正面密度〕

### H2 技术选型(方案 R 的 skill 机制)

- [X]  **3 方案 R 三步落进 skill**:① SKILL.md 主流程第 2 步「生成问卷」加路径决定(读 CLAUDE.md 声明 → 命中用声明根 / 未命中默认 harness/ 懒建 → 落盘前确认);② 第 4 步「处理与落盘」落盘映射用配置化根(非硬编码 docs/);③ PROCESSING-RULES.md 落盘映射表 `docs/design/` `docs/questionnaires/` `docs/adr/` → `<落盘根>/design/` 等 〔VISION 方案 R;SKILL.md 第 54/67/72 行 + PROCESSING-RULES 落盘映射表是改动 1 落点〕
- [X]  **4 声明识别关键词清单** = 「落盘根 / 落盘速查 / harness 区 / 设计产物落 / harness 文件」——skill 自然语言匹配 CLAUDE.md 中这些关键词,命中即取该节指示的根;本仓库 CLAUDE.md「skill 家族协作 · 落盘路径速查表」节自然命中 → harness/ 〔W01 Q1.1 推导 = D;零侵入,本仓库已命中〕
- [X]  **5 落盘前确认形态 = 首次确认 + 结构变化时复确认**:同一项目首次落盘(或探测到项目结构变化)用 AskUserQuestion 确认根路径,后续波次沿用(处理报告标注「根 = X,沿用首次确认」);不每波都问(避免退化成一问一答) 〔VISION 方案 R 第三道防线;W00 #11 确认点;兼顾可预测与效率〕

### H3 接口契约(skill 内部 + 副本同步)

- [X]  **6 引擎副本同步契约**:design-Q PROCESSING-RULES.md 为 canonical(落盘映射节改方案 R);grill-Q / retro-Q / action-Q 三份 PROCESSING-RULES.md 副本同步(落盘映射表统一改);四份 DESIGN.md 各记一笔「2026-08-06 落盘路径配置化同步(OD-8 重访触发①)」;QUESTIONNAIRE-FORMAT.md 的「文件约定」节(docs/questionnaires/ → 配置化根)四份同步 〔OD-8 引擎漂移治理;canonical + 副本声明 + DESIGN.md 记录〕
- [X]  **7 骨架归属契约**:STAGE-SKELETONS.md 仅 design-Q 持有(改动 2/3 判别法则 + 最小必含只改此一份);retro 用 RETRO-SKELETONS.md、grill 用 GRILL-SKELETON.md、action 无骨架——均不动(改动 2/3 与它们无关);long-running 只同步读归档路径(feature_list 机制不动) 〔探索确认骨架归属;VISION scope 边界〕

### H4 部署与运维(skill 生效与维护)

- [X]  **8 skill 改动即时生效**:改 `~/.claude/skills/` 下文件 = 下次任何项目调用 design-Q 即用新规格,无构建/无重启/无版本号(用户级 skill,文件即规格)。维护 = 改完跑一次 dogfood 自检(DoD-4)确认无回归 〔skill 物理特性;W01 Q2=C 全局生效〕
- [X]  **9 dogfood 验收点**:本次 HLD/LLD 产出后,对照新骨架「最小必含」逐项自检——HLD 文档含 H1–H5 每项最小必含子项 + 产出形态;LLD 文档含 L1–L5 每项最小必含。自检不通过则补全(这就是改动 3 的第一次实战) 〔VISION DoD-4 + V3 dogfood;hld_v1 反面、repo/HLD 正面〕

### H5 架构决策识别

- [ ]  **10 本次不新增 ADR(全记 design-Q DESIGN.md)**:三组改动均可回退(文件改回即可,骨架/路径/配置皆双向门),难逆转性不足 ADR 三条件(难逆转 + 会困惑 + 真权衡)→ 不立 ADR,全记 design-Q DESIGN.md 决策表(D23 落盘路径配置化 / D24 HLD-LLD 判别法则 / D25 最小必含 / D26 全局生效);全局生效(W01 Q2=C)亦记 DESIGN.md。若你认为某项该立 ADR,留空转 W01 〔ADR 三条件;W01 Q2 已定全局生效不跨域立 ADR〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-06 · hld W00 → processed)

- **preview 统计**:采纳 9 / 留空 1 / 转 W01 题 1;opt-in 关无取消率;单向门 0
- **采纳 9 条**:第 1(改动落点 4 文件 + 四副本同步)、2(骨架四块结构)、3(方案 R 三步落 skill)、4(声明关键词清单)、5(首次确认 + 后续沿用)、6(副本同步契约 + OD-8 声明)、7(骨架归属:仅 design-Q STAGE-SKELETONS)、8(即时生效无构建)、9(dogfood 自检)
- **留空转 W01 1 条**:第 10(不新增 ADR)→ W01 Q1 深究 D23–D26 哪些立 ADR
- **开放型骨架必答项转 W01**:判别法则表述(Q2)+ 最小必含表(Q3,H1–H5/L1–L5 共 10 项)+ 产出形态力度(Q4)+ 坍缩分档(Q5)
- **HLD.md**:待 W01 答完后落盘 `harness/design/skill-spec-revamp/HLD.md`
- **归档**:W00 待 W01 后连同归档 `archive/`
