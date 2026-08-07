# LLD · design-Q skill 规格整理(分阶段落地规格)

> ⚠️ **2026-08-07 状态更新**:本文「落盘路径配置化(方案 R)」部分(§2.2/§2.3/§2.4/§2.6 落盘根相关)**已放弃**([ADR-0011](../../adr/0011-abandon-plan-r-hardcode-harness.md)),回归硬编码 `harness/`;**骨架改造(F007:判别法则 + 最小必含 + 分档)部分保留**并已回灌仓库。撤销执行见 [feature-skills-harness-consistency/](../feature-skills-harness-consistency/)。

> 来源:design-questionnaire lld 阶段 W00(10 条全采纳)+ W01(5 题草案全采纳)。2026-08-06。
> **🔧 grill-Q 压测后修订(2026-08-06/08-07)**:8 项认定/部分认定发现回灌(Q3 long-running 遗漏 / Q5 P3 diff 范围 / Q6 无 CLAUDE.md / Q1+Q10 关键词漏读 / Q2 形式主义 / Q4 确认疲劳 / Q8 机制回归 / Q11 落盘根定义);Q7(retro 落点 + 路径区分)经 grill-with-docs 单点深钻定案(retro 文档项目固有 docs/retro/ + 落盘根边界三件 + skill 内部 vs 宿主路径区分规则),结论落 2.6。修订处标 🔧。
> 上游:[VISION](VISION.md) + [HLD](HLD.md)。本文 = 落地规格;执行时每阶段按 DoD 验证,全部完成后走 dogfood 自检 + 衔接实现期。
> **dogfood 声明**:本 LLD 自身按新骨架(改动 2/3)写——含 L1–L5 每项「最小必含」+ 五块改写文本(实现期直接 copy 的 source of truth),末尾附最小必含自检。

## L1 阶段计划(4 阶段,可独立交付/验证)

依赖链:**P1 → P2 → P3 → P4**(P1/P2 不同文件可并行但串行更稳;P3 依赖 P2 canonical 先改;P4 依赖 P1+P2+P3)。

| 阶段 | 目标 | 关键动作 | 独立 DoD |
|---|---|---|---|
| **P1 骨架改造** | 改动 2/3 落 STAGE-SKELETONS.md | 头部判别法则节(🔧 Q2 内容约束) + 每项最小必含/产出形态子块 + 坍缩分档节 | grep 关键节标题 + 人审结构(L4 P1) |
| **P2 design-Q 路径配置化** | 改动 1 的 design-Q 部分 | SKILL.md 路径决定逻辑(🔧 Q6 无 CLAUDE.md / Q1+Q10 关键词 / Q4 确认标注)+ PROCESSING-RULES.md 落盘映射(🔧 Q11 落盘根定义)+ QUESTIONNAIRE-FORMAT.md 文件约定 + DESIGN.md D23–D26 | docs/ 字符串 0 命中 + 配置化逻辑在位(L4 P2) |
| **P3 四副本 + long-running 同步** | 改动 1 扩散 | grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md + SKILL.md + QUESTIONNAIRE-FORMAT.md 同步 + 各 DESIGN.md 记录;🔧 **+ long-running SKILL.md §5.3 读归档问卷路径配置化**(Q3) | 落盘映射节 diff 0(🔧 Q5 仅映射节,不含分叉区)+ long-running 归档路径配置化 + DESIGN.md 记录在位(L4 P3) |
| **P4 dogfood 自检** | 验证 | 本次 LLD 对照新骨架自检 + 跨项目落盘验证(本仓库 + 无 harness/ 沙盒) | 自检通过(🔧 Q8 含脚本化子检查)+ 跨项目落盘正确(L4 P4) |

## L2 详细设计(每文件改写规格 · 实现期 source of truth)

### 2.1 design-Q STAGE-SKELETONS.md 改造(P1)

**a. 头部新增「HLD 与 LLD 的职责区分(判别法则)」节**(放「使用方式」之后、「Stage: vision」之前):

```markdown
## HLD 与 LLD 的职责区分(判别法则)

> hld / lld 两阶段易混淆越界(实证:hld_v1 把章节级改写混进 HLD)。出题与落盘前,先用判别法则判定每条内容属 HLD 还是 LLD。

**HLD = 架构骨架(phase-invariant)**:回答「系统长什么样、各部分如何衔接」,跨所有实现阶段稳定。= 模块/区边界与职责 + 全局选型(含被否决项)+ 模块间契约 + 部署运维 + ADR 识别。

**LLD = 构建路径(incremental)**:回答「分几步建、每步具体做什么、何时算完」,随实现推进而细化。= 阶段拆分(依赖链)+ 每阶段详细设计 + 函数级接口规格 + 每阶段 DoD + 依赖与预估。

**判别问句**:① 「这条内容会随阶段拆分变化吗?」会 → LLD;否(系统级稳定事实)→ HLD。② 「它是模块边界,还是模块内部?」边界 → HLD;内部 → LLD。

> HLD 不写「怎么逐步实现」(那是 LLD 的阶段拆分 + 详细设计);LLD 不重写「系统由什么组成」(那是 HLD 的架构)。两阶段职责不重叠。
```

**🔧 反简化声明(Q2 grill-Q 修订,最小必含约束内容非仅结构)**——判别法则节之后(或 STAGE-SKELETONS 头部「使用方式」内)补:

```markdown
> **最小必含约束的是内容,不止结构**:每项的「最小必含」子项,内容须可被实现期直接执行——非占位、非「见后」、非一句话带过。填了子项标题但内容空泛(如「被否决项」填「无」、「回归验证」填「测试通过」)不算满足。这是 hld_v1 简化变体(有结构但浅)的对症约束。
```

**b. 每项「最小必含 + 产出形态」标注格式**:表格保留作总览,每项下加子块(hld W01 Q3 定稿 10 项)。格式示例:

```markdown
## Stage: hld
| # | 必问项 | 出题方向 | 落盘 | 必答 |
|---|---|---|---|---|
| H1 | 系统架构 | 模块划分、职责边界、数据流向 | HLD#架构 | ✅ |
(……现有表格保留)

### 最小必含 + 产出形态(hld 阶段各项)

**H1 系统架构** · 产出形态:模块表 或 架构图
- 最小必含:① 模块/区划分清单 ② 每模块职责一句话边界 ③ 数据/控制流向(图或文字链路)

**H2 技术选型** · 产出形态:选型表,含被否决列
- 最小必含:① 选型项(技术栈/库/协议/机制) ② 选它的理由 ③ 被否决项(至少 1 个)

**H3 接口契约** · 产出形态:契约清单
- 最小必含:① 模块/系统边界处的契约(数据格式/协议/调用方向) ② 哪些是硬约束(实现期不能偏离)

**H4 部署与运维** · 产出形态:运维清单
- 最小必含:① 怎么跑起来(启动/入口) ② 怎么监控/验证健康 ③ 怎么排查问题

**H5 架构决策识别** · 产出形态:ADR 候选表
- 最小必含:① 逐条核对 ADR 三条件 ② 不满足三条件的决策记哪(DESIGN.md/OD)
```

(lld 阶段 L1–L5 同构,子块如下:)

```markdown
### 最小必含 + 产出形态(lld 阶段各项)

**L1 阶段拆分** · 产出形态:阶段表
- 最小必含:① 阶段列表 ② 依赖链(谁前置谁) ③ 每阶段独立 DoD(不能独立验证 = 粒度太粗)

**L2 详细设计** · 产出形态:图 或 结构清单,按需
- 最小必含:① 按阶段列模块内部结构(类/序列/Schema/状态机,按需不必全画)

**L3 接口规格** · 产出形态:接口签名表
- 最小必含:① 入参/出参 ② 错误码/异常

**L4 DoD** · 产出形态:DoD 清单
- 最小必含:① 每阶段验收条件 ② 可脚本化的项标出(脚本化优先) ③ 回归验证(不破坏现有功能)

**L5 依赖与预估** · 产出形态:依赖/预估清单
- 最小必含:① 前置依赖 ② 外部资源 ③ 工作量排序
```

**c. 「阶段坍缩与最小必含分档」节**(替换现有「阶段坍缩(可选)」节):

```markdown
## 阶段坍缩与最小必含分档

默认 vision → hld → lld 三阶段(完整档,全量最小必含)。定模时按「经验 × 规模」给坍缩建议,用户确认。

| 档 | 阶段 | 最小必含(防简化) |
|---|---|---|
| **完整档** | vision → hld → lld | H1–H5 + L1–L5 全量 |
| **坍缩 hld 档**(没经验) | vision → hld | 只 hld 五项(H1–H5);lld 不预先写,实现中边做边调,沉淀的详细决策即时落盘 |
| **坍缩 lld 档**(小项目:skill/脚本/小工具) | vision → lld | 只 lld 五项(L1–L5);H2 选型 / H5 ADR 若有实质内容,并入 lld 文档或单独 ADR |

> 各档保留该档必需的最小必含约束——坍缩档**不免除**最小必含(否则回退 hld_v1 简化状况)。
> 判据来源:D19(2026-07-23 retro hld 闸门用户指示)。
```

### 2.2 design-Q SKILL.md 路径决定逻辑(P2)

**第 2 步「生成问卷」内新增路径决定子步**(替换硬编码 `docs/questionnaires/`):

```markdown
- **确定落盘根**(方案 R:声明优先 + 默认兜底 + 落盘前确认):
  1. 读项目 CLAUDE.md,匹配声明关键词〔「落盘根 / 落盘速查 / harness 区 / 设计产物落 / harness 文件」——🔧 **非穷举清单,常见措辞覆盖,漏读由步骤 3 确认点兜底**(Q1+Q10)〕→ 命中取该节指示的根(权威)
     - 🔧 **CLAUDE.md 不存在**(Q6)(新项目/空项目)→ 跳过声明识别,直接步骤 2 默认
  2. 未命中(或无 CLAUDE.md)→ 默认 `harness/`(懒创建)
  3. AskUserQuestion 确认根路径(首次或项目结构变化时);🔧 **确认提示显示「声明命中/未命中(哪条关键词或未命中)→ 将用根 X」**(Q1+Q10),让漏读可见可纠。后续波次沿用,🔧 **每波处理报告顶部标注「落盘根 = X(首次确认于 Wnn)」**(Q4),用户每波可见,发现错误可随时要求重确认
- 写到 `<落盘根>/questionnaires/<stage>-w<NN>.md`(feature 模式:`feature-<slug>-<stage>-w<NN>.md`),status: pending。目录懒创建。
```

**第 4 步「处理与落盘」落盘句改写**(替换 `docs/adr/`):

```markdown
- 逐题落盘到 `<落盘根>/` 下:阶段文档 → `<落盘根>/design/`(VISION/HLD/LLD);ADR → `<落盘根>/adr/NNNN-<slug>.md`;**CONTEXT.md / OPEN-DECISIONS.md / TODO.md 为项目固有文件,路径不动**(各项目已定型)。本波处理完即刻写。
```

### 2.3 design-Q PROCESSING-RULES.md 落盘映射表(P2)

替换现有「落盘映射」表。🔧 **「落盘根」显式定义**(Q11,跨 skill 共用概念,四副本 + long-running 引用):

```markdown
## 落盘映射

所有落盘**本波处理完即刻执行**,不批处理。目标文件不存在时懒创建;命名沿用项目既有约定(如 `_vN` 版本规则)。

**落盘根 `<根>`** = design-Q 产物的统一落盘前缀(design/ + questionnaires/ + adr/ 共用此根)。由 design-Q 主流程第 2 步确定(方案 R:CLAUDE.md 声明优先 → 默认 `harness/` → 落盘前确认)。项目可在 CLAUDE.md 声明覆盖(如 `docs/`)。CONTEXT/OPEN-DECISIONS/TODO 为项目固有文件,不属落盘根。

| 答案类型 | 落盘目标 |
|---|---|
| vision 阶段题 | `<根>/design/` 的 VISION.md |
| hld 阶段题 | `<根>/design/` 的 HLD 文档 |
| lld 阶段题 | `<根>/design/` 的 LLD 文档 |
| 术语定义类 | CONTEXT.md(项目固有,路径不动) |
| 满足 ADR 三条件的决策 | `<根>/adr/NNNN-<slug>.md`(编号顺延现有) |
| 🤔 逃生舱(单向门) | OPEN-DECISIONS.md(项目固有,路径不动) |
| 🤔 逃生舱(双向门) | 采用 ★推荐项 **且进 OD 标注**(标「双向门 / 采用推荐项 X / provisional」+ 重访触发条件) |
| 行动项 | `<项目根>/TODO.md`(项目固有,路径不动;懒创建) |

ADR 三条件(缺一不写):难逆转 + 缺上下文会让人困惑 + 经过真实权衡。
```

### 2.4 design-Q QUESTIONNAIRE-FORMAT.md「文件约定」节(P2)

「文件约定」节中 `docs/questionnaires/` → `<落盘根>/questionnaires/`(配置化根);frontmatter / 模板不变。

### 2.5 design-Q DESIGN.md(P2)

新增决策 D23–D26(落盘路径配置化 / HLD-LLD 判别法则 / 最小必含 + 产出形态 / 全局生效),各标「双向门,可回退」+ 出处(hld W01 / vision W01 Q2)。同步记录「2026-08-06 落盘路径配置化 + 骨架增强同步」(OD-8 重访触发①)。

### 2.6 四副本 + long-running 同步(P3)

| 副本/skill | PROCESSING-RULES.md | SKILL.md | QUESTIONNAIRE-FORMAT.md | DESIGN.md |
|---|---|---|---|---|
| grill-Q | 落盘映射表 → `<根>` 配置化 | 路径字符串配置化 | 文件约定节路径 | 记同步(OD-8) |
| retro-Q | 同上 | 同上 | 同上 | 同上 |
| action-Q | 同上 | 同上 | 同上 | 同上 |
| 🔧 **long-running**(Q3) | —(无此文件) | **§5.3 读归档问卷路径 → 配置化根**(feature_list/progress 不动) | — | 记同步 |

各副本 DESIGN.md 追加:「2026-08-06 落盘路径配置化同步(OD-8 重访触发①);HLD/LLD 判别法则 + 最小必含仅 design-Q 骨架,不扩散」。

🔧 **同步范围界定(Q5,OD-8 守)**:diff 0 / 配置化同步**仅指「落盘映射节」**,不含各副本有意分叉区(action-Q 小波阈值 ≤4 / confirm-list 语义;grill-Q stage 固定标记;retro 骨架)。P3 执行时只改落盘映射节,分叉区原样保留。

> 🔧 **Q7 深钻结论(2026-08-07 grill-with-docs)**:
> - **retro 文档落点 = 项目固有 `docs/retro/`**(不纳入落盘根配置化)。**落盘根边界 = 通用三件 `design/` + `questionnaires/` + `adr/`**;retro 文档是项目阶段历史档案(人读、长期保存,偏叙事),归项目 docs/,与 design-Q 的 design 文档(AI 流程产物)性质不同。retro-Q SKILL.md:42 `docs/retro/` 保持不动(项目固有,P3 四副本同步不碰)。
> - **skill 内部路径 vs 宿主落盘路径区分规则**:四副本同步只改「skill 规格里**描述宿主项目落盘路径**的字符串」(如 SKILL.md「写到 docs/questionnaires/」);**不改**「skill 自己引用**自身目录文件**的相对链接」(实例:retro-Q SKILL.md:54 `[docs/design/hld_v1.md](./docs/design/hld_v1.md)`、retro-Q/DESIGN.md:4 `[docs/VISION.md]`、grill-Q/DESIGN.md:37 `[docs/questionnaires/archive/grill-own-design-w01.md](./...)`)。判据:`./docs/...`(相对路径,指 skill 目录内部)vs 描述宿主落盘的 `docs/...`。

## L3 接口规格

### 路径决定逻辑接口

- **入参**:项目 CLAUDE.md 文本(声明关键词匹配结果;🔧 CLAUDE.md 不存在 → 空输入)
- **出参**:落盘根路径(如 `harness/`)
- **异常处理**:🔧 CLAUDE.md 不存在(Q6)→ 跳过声明识别,默认 `harness/` + 确认;关键词未命中 → 默认 `harness/`(懒创建)+ 落盘前确认(提示未命中);声明与默认冲突 → 以声明为权威 + 确认

### 各文件改动清单

| 文件 | 改动 | 阶段 |
|---|---|---|
| design-Q STAGE-SKELETONS.md | 判别法则节(🔧 Q2 内容约束)+ 最小必含子块 + 分档节 | P1 |
| design-Q SKILL.md | 第 2/4 步路径决定(🔧 Q6/Q1+Q10/Q4)+ docs/ 字符串清除 | P2 |
| design-Q PROCESSING-RULES.md | 落盘映射表配置化(🔧 Q11 落盘根定义) | P2 |
| design-Q QUESTIONNAIRE-FORMAT.md | 文件约定节路径 | P2 |
| design-Q DESIGN.md | D23–D26 | P2 |
| grill/retro/action × (PROCESSING-RULES + SKILL + QUESTIONNAIRE-FORMAT + DESIGN) | 同步(🔧 Q5 仅映射节)+ 记录 | P3 |
| 🔧 long-running SKILL.md(Q3) | §5.3 读归档问卷路径 → 配置化根 | P3 |

## L4 DoD

### 统一回归(每阶段必跑)

1. **机制回归**:改动不破坏 skill 现有机制(问卷格式 / preview / 逃生舱 / 小波阈值 / opt-in 开关行为不变)。🔧 **可脚本化子检查(Q8)**:改后生成一份测试问卷 → grep frontmatter 字段齐全(mode/wave/stage/created/status)+ grep 🤔 逃生舱每题在位 + grep ★ 推荐至多一个;人跑一次确认交互正常
2. **脱敏门**:本次 skill 改动 .md 经 `python3 scripts/desensitize.py .` 0 命中(skill 文件在 ~/.claude 非本仓库,但若复制/引用进本仓库则扫)

### 各阶段 DoD(可脚本化)

- **P1**:STAGE-SKELETONS.md 含 ①「HLD 与 LLD 的职责区分」节 ② 反简化声明(🔧 Q2)③「最小必含 + 产出形态」子块(H1–H5/L1–L5)④「阶段坍缩与最小必含分档」节(grep 节标题 + 人审)
- **P2**:design-Q SKILL/PROCESSING-RULES/QUESTIONNAIRE-FORMAT 中 `docs/questionnaires` `docs/design` `docs/adr` 字符串 **0 命中**(grep);路径决定含 🔧 无 CLAUDE.md 分支 + 关键词非穷举 + 确认提示 + 处理报告根标注;DESIGN.md D23–D26 在位
- **P3**:grill/retro/action 三副本 PROCESSING-RULES.md **落盘映射节**与 design-Q canonical **diff 0**(🔧 Q5 仅映射节,不含分叉区);🔧 long-running SKILL.md §5.3 归档路径配置化;各 DESIGN.md 有同步记录
- **P4**:① 本 LLD 对照新骨架最小必含自检通过(见下);② 本仓库(声明命中 harness/)+ 一个无 harness/ 沙盒(🔧 Q9:/tmp 临时项目,跑完即弃,不碰真实项目)落盘路径正确

## L5 依赖与预估

- **外部依赖**:无(纯 skill Markdown 规格,不涉编译/运行);P4 跨项目验证用 /tmp 临时沙盒(非真实项目)
- **工作量排序**:P1(骨架重写最重)> P3(四副本 + long-running 同步)> P2(design-Q 路径,4 文件)> P4(自检 + 验证)
- **实现期建议**:long-running-agent 驱动(feature_list 从 P1–P4 反推)或手动按阶段推进;P1 判别法则表述已在 hld W01 Q2 定稿;🔧 Q7(retro 落点 + 路径区分)grill-with-docs 深钻结论补 2.6 节后再进 P3

---

## LLD 自身最小必含自检(dogfood,改动 3 实战)

对照新骨架 LLD 五项的最小必含子项(hld W01 Q3 定稿):

| 骨架项 | 最小必含子项 | 本 LLD 落点 | 自检 |
|---|---|---|---|
| L1 阶段拆分 | a 阶段列表 | L1 表(4 阶段) | ✓ |
| | b 依赖链 | L1 依赖链 P1→P2→P3→P4 | ✓ |
| | c 每阶段独立 DoD | L1 表「独立 DoD」列 + L4 各阶段 | ✓ |
| L2 详细设计 | a 按阶段列模块内部结构 | L2.1–L2.6(每文件改写规格 + 文本,🔧 含 grill-Q 修订) | ✓ |
| L3 接口规格 | a 入参/出参 | L3 路径决定接口(入参/出参/异常,🔧 含无 CLAUDE.md) | ✓ |
| | b 错误码/异常 | L3 异常处理(未命中/冲突/无 CLAUDE.md) | ✓ |
| L4 DoD | a 每阶段验收条件 | L4 各阶段 DoD | ✓ |
| | b 可脚本化的项标出 | L4(grep/diff/0 命中 + 🔧 Q8 机制回归子检查) | ✓ |
| | c 回归验证 | L4 统一回归「机制回归」(🔧 Q8 脚本化) | ✓ |
| L5 依赖与预估 | a 前置依赖 | L5(无外部依赖) | ✓ |
| | b 外部资源 | L5(P4 /tmp 沙盒) | ✓ |
| | c 工作量排序 | L5(P1>P3>P2>P4) | ✓ |

**自检结果**:LLD 五项 × 最小必含子项全部覆盖;L2 含五块实现期可直接 copy 的改写文本(判别法则节 / 最小必含子块 / 分档节 / SKILL 路径逻辑 / RULES 映射表),🔧 grill-Q 8 项修订已整合(Q7 待深钻)。本 LLD 非简化版(对照 lld_v1 反面:仅章节级提纲无落地文本)。dogfood 通过。
