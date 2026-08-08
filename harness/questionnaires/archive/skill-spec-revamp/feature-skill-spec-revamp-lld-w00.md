---
mode: feature
wave: 0
stage: lld
created: 2026-08-06
status: processed
---
# 问卷 lld W00 · Preview(决策默认值 yes/no 速答)

> **本阶段定位**:把 HLD 落地动作清单(8 条)拆成可独立验证的阶段,定每阶段 DoD + 接口规格 + 依赖。L2 详细设计(骨架新节最终文本 / SKILL 路径逻辑 / PROCESSING-RULES 映射表新格式)留 W01 出草案。
> **feature 模式 lld**:不裁剪;每阶段 DoD 必含「不破坏现有功能」回归验证。
>
> **作答规则**:
>
> - opt-in 开关未启用,全部 `[ ]`,人逐条作答
> - **勾 `[x]` = 采纳默认**;**留空 = 不采纳** → 转 W01 深究
> - 本阶段无单向门(改 skill 规格可回退;P4 跨项目验证只读/懒创建不破坏他项目)
> - 不用 🤔;真定不了 → 留空转 W01
>
> 默认来源标注于〔〕。

## 决策默认值清单

### L1 阶段拆分

- [X]  **1 四阶段 + 依赖链 P1→P2→P3→P4**:
  - **P1 骨架改造**(HLD 动作 1):改 design-Q STAGE-SKELETONS.md——判别法则节 + 每项最小必含 + 产出形态 + 坍缩分档节。改动 2/3 核心。
  - **P2 design-Q 路径配置化**(HLD 动作 2/3/4/5):改 design-Q SKILL.md(路径决定逻辑)+ PROCESSING-RULES.md(落盘映射)+ QUESTIONNAIRE-FORMAT.md(文件约定)+ DESIGN.md(D23–D26)。改动 1 的 design-Q 部分。
  - **P3 四副本同步**(HLD 动作 6/7):grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md + SKILL.md + QUESTIONNAIRE-FORMAT.md 同步 + 各 DESIGN.md 记录(OD-8)。改动 1 扩散。
  - **P4 dogfood 自检**(HLD 动作 8):本次 LLD 对照新骨架自检 + 跨项目落盘验证。
  - 依赖链:P1/P2 可并行(不同文件无依赖)但**串行更稳**(一次一个功能,long-running 原则);P3 依赖 P2(canonical 先改);P4 依赖 P1+P2+P3 〔HLD 落地动作清单 8 条归并;long-running「一次只处理一个功能」〕

### L3 接口规格

- [X]  **2 路径决定逻辑接口**:**入参** = 项目 CLAUDE.md 文本(声明关键词命中结果);**出参** = 落盘根路径(如 `harness/`);**异常处理** = 关键词未命中 → 默认 `harness/`(懒创建)+ 落盘前确认;声明与探测冲突 → 以声明为权威 + 确认 〔HLD H1.2 路径决定流;HLD H3.2 硬约束〕

### L4 DoD(每阶段独立可验证)

- [X]  **3 P1 DoD(骨架改造)**:design-Q STAGE-SKELETONS.md 含:① 头部「HLD/LLD 判别法则」节(定义 + 两句问句);② 每项「最小必含」子项(H1–H5/L1–L5,Q3 定稿);③ 每项「产出形态」建议;④ 坍缩档分档节。验证 = grep 关键节标题 + 人审结构 〔hld W01 Q2/Q3/Q4/Q5 定稿〕
- [X]  **4 P2 DoD(design-Q 路径配置化)**:design-Q SKILL.md + PROCESSING-RULES.md + QUESTIONNAIRE-FORMAT.md 中 `docs/questionnaires` `docs/design` `docs/adr` 字符串 **0 命中**(grep);路径决定逻辑(声明→默认→确认)在位;DESIGN.md D23–D26 在位 〔HLD H2 方案 R;漂移面 design-Q 3 处〕
- [X]  **5 P3 DoD(四副本同步)**:grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md 落盘映射表与 design-Q canonical **diff 0**(落盘映射节);各副本 SKILL.md 路径字符串配置化;四份 DESIGN.md 各有「2026-08-06 落盘路径配置化同步」记录 〔OD-8;漂移面 grill 3 + retro 3 + action 4〕
- [X]  **6 P4 DoD(dogfood 自检)**:① 本次 LLD 文档对照新骨架「最小必含」自检通过(逐项);② 跨项目落盘验证——本仓库(声明命中 harness/)+ 一个无 harness/ 项目(懒创建/声明覆盖)落盘路径正确 〔VISION DoD-4;HLD H4 监控验证〕
- [X]  **7 回归验证(每阶段必含)**:改动**不破坏 skill 现有机制**——问卷格式 / preview 机制 / 逃生舱 / 小波阈值 / opt-in 开关 行为不变(本次只改路径 + 骨架增强层,不动交互机制,VISION scope 边界)。验证 = 改后跑一次 design-Q 问卷生成确认机制正常 〔feature 模式 lld 裁剪;VISION 不做什么〕

### L5 依赖与预估

- [X]  **8 依赖**:HLD 定稿无阻塞;纯 skill 文档改动**无外部依赖**(不需环境实测,不涉编译/运行——skill 是 Markdown 规格);P4 跨项目验证需一个无 harness/ 的测试项目(可用参考项目或临时沙盒) 〔HLD 已定;skill 物理特性〕
- [X]  **9 预估 + 实现期建议**:工作量 **P1 最重**(STAGE-SKELETONS 骨架重写:判别法则 + 10 项最小必含 + 产出形态 + 分档节)> P3(四副本机械同步)> P2(design-Q 路径,3 文件)> P4(自检 + 验证)。实现期 = long-running-agent 驱动(feature_list 从 P1–P4 反推)或手动按阶段推进 〔HLD 落地动作;long-running 衔接〕

### L2 详细设计(方向,具体文本留 W01)

- [X]  **10 L2 详细设计 = 按阶段列每文件具体改写文本,W01 出草案**:① STAGE-SKELETONS 判别法则节最终文本 + 每项最小必含/产出形态标注格式 + 坍缩分档节文本;② SKILL.md 第 2/4 步路径决定逻辑改写;③ PROCESSING-RULES.md 落盘映射表新格式(配置化根)。W01 每块给默认草案,你认可/改 〔LLD 骨架 L2;hld W01 Q2 判别法则表述已定方向〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-06 · lld W00 → processed)

- **preview 统计**:采纳 10 / 留空 0 / 转 W01 题 0;opt-in 关无取消率;单向门 0
- **采纳 10 条**:第 1(四阶段 P1→P2→P3→P4)、2(路径决定接口)、3(P1 DoD 骨架节齐全)、4(P2 DoD docs/ 0 命中)、5(P3 DoD 四副本 diff 0)、6(P4 DoD 自检+跨项目)、7(回归验证不破坏机制)、8(无外部依赖)、9(预估 P1 最重 + long-running)、10(L2 文本留 W01)
- **L1/L3/L4/L5 全定;L2 详细设计文本 → W01 Q1–Q5 出五块草案**(判别法则节 / 最小必含标注格式 / 分档节 / SKILL 路径逻辑 / RULES 映射表)
- **opt-in 关,无取消率;无逃生舱;无异常**
- **LLD.md**:待 W01 答完后落盘 `harness/design/skill-spec-revamp/LLD.md`
- **归档**:W00 待 W01 后连同归档 `archive/`
