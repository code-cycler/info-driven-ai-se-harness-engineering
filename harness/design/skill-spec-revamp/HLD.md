# HLD · design-Q skill 规格整理(架构方案)

> ⚠️ **2026-08-07 状态更新**:本文「落盘路径配置化(方案 R)」部分**已放弃**([ADR-0011](../../adr/0011-abandon-plan-r-hardcode-harness.md)),回归硬编码 `harness/`;**骨架改造(F007)部分保留**并已回灌仓库。撤销执行见 [feature-skills-harness-consistency/](../feature-skills-harness-consistency/)。

> 来源:design-questionnaire hld 阶段 W00(10 条,采纳 9 / 留空 1)+ W01(5 题:Q1=D 不立 ADR / Q2=A 判别法则默认表述 / Q3 最小必含表 10 项全量采纳 / Q4=A 建议形态非强制 / Q5=A 分档)。2026-08-06。
> 上游:[VISION](VISION.md)(2026-08-06)。本文 = 三组改动的架构方案;落地规格见 LLD,详细决策按 H5 落 design-Q DESIGN.md。
> **dogfood 声明**:本 HLD 自身按新骨架(改动 2/3)写——含 H1–H5 每项「最小必含」子项 + 产出形态,末尾附最小必含自检。即改动 3 的第一次实战。
> **🔧 grill-Q 压测后修订(2026-08-06/08-07)**:Q6(无 CLAUDE.md 项目)回灌 H1.2 路径决定流;Q3(long-running)/Q5(diff 范围)/Q1+Q10(关键词)/Q2(形式主义)/Q4(确认疲劳)/Q8(机制回归)/Q11(落盘根定义)详 [LLD](LLD.md);Q7(retro 落点 + 路径区分)grill-with-docs 深钻定案——retro 文档项目固有 docs/retro/、落盘根边界三件、skill 内部 vs 宿主路径区分(详 LLD 2.6)。

## H1 系统架构(skill 文件改动地图 + 数据流向)

### 1.1 模块/区划分(本次改动的 skill 文件作为模块)

| 模块 | 所属 | 本次改动 | 职责边界 |
|---|---|---|---|
| [STAGE-SKELETONS.md](../../../../.claude/skills/design-questionnaire/STAGE-SKELETONS.md) | design-Q 专属 | 改动 2(判别法则)+ 改动 3(最小必含/产出形态/分档) | 三阶段骨架模板,仅 design-Q 持有 |
| [SKILL.md](../../../../.claude/skills/design-questionnaire/SKILL.md)(design-Q) | design-Q | 改动 1(路径决定逻辑,主流程第 2/4 步 + 3 处 docs/ 字符串清除) | skill 主流程与铁律 |
| [PROCESSING-RULES.md](../../../../.claude/skills/design-questionnaire/PROCESSING-RULES.md)(design-Q) | design-Q canonical | 改动 1(落盘映射表 docs/ → 配置化根) | 解析与落盘规则引擎(canonical) |
| [QUESTIONNAIRE-FORMAT.md](../../../../.claude/skills/design-questionnaire/QUESTIONNAIRE-FORMAT.md)(design-Q) | design-Q canonical | 改动 1(「文件约定」节路径) | 问卷格式引擎(canonical) |
| [DESIGN.md](../../../../.claude/skills/design-questionnaire/DESIGN.md)(design-Q) | design-Q | 记 D23–D26 决策 | skill 设计决策记录 |
| grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md + SKILL.md + QUESTIONNAIRE-FORMAT.md | 四副本 | 改动 1 同步(落盘路径配置化) | 引擎副本(OD-8 漂移治理) |
| long-running | 相关 skill | 只同步读归档路径(feature_list 机制不动) | 跨会话实现约束 |

**骨架归属契约**:STAGE-SKELETONS.md 仅 design-Q(retro 用 RETRO-SKELETONS.md、grill 用 GRILL-SKELETON.md、action 无骨架——改动 2/3 不扩散到它们)。

### 1.2 数据/控制流向

**路径决定流**(改动 1 核心,方案 R):
```
skill 启动
  → 读项目 CLAUDE.md,自然语言匹配声明关键词
    〔「落盘根 / 落盘速查 / harness 区 / 设计产物落 / harness 文件」〕
    🔧 CLAUDE.md 不存在(新项目/空项目)→ 跳过声明识别,直接默认(Q6)
  → 命中:取该节指示的根(权威)
  → 未命中(或无 CLAUDE.md):默认 harness/(懒创建)
  → 落盘前 AskUserQuestion 确认根路径(首次 + 项目结构变化时)
  → 后续波次沿用(处理报告标注「根 = X,沿用首次确认」)
```

**副本同步流**(改动 1 扩散):
```
design-Q PROCESSING-RULES.md(canonical)改落盘映射
  → grill-Q / retro-Q / action-Q 三副本同步
  → 四份 DESIGN.md 各记「2026-08-06 落盘路径配置化同步」(OD-8 重访触发①)
```

**产出形态**:模块表(H1.1)+ 流向图(H1.2)。

## H2 技术选型(机制方案 + 被否决项)

| 选型项 | 采纳方案 | 理由 | 被否决项(防再提议) |
|---|---|---|---|
| 落盘路径机制 | **方案 R**:默认 `harness/` + CLAUDE.md 声明覆盖 + 落盘前确认 | 通用 skill 不能硬编码;本仓库实践需 harness/;声明权威+默认兜底+确认防误落,三兼顾 | 固定 docs/(痛点不解决)/ 纯探测(魔法不可预测)/ 纯声明(新项目负担)/ 每次问人(退化一问一答)/ 配置化三道防线 Q(复杂,探测层魔法) |
| 声明识别格式 | **自然语言关键词匹配**(零侵入) | CLAUDE.md 是人读的,强制机器格式破坏可读性;本仓库「落盘路径速查表」自然命中 | 固定标题节(侵入 CLAUDE.md 结构)/ HTML 注释标记(对人不透明)/ frontmatter 键值(CLAUDE.md 通常无 frontmatter) |
| 骨架新结构 | **四块增强层叠加现有三表** | 判别法则 + 最小必含 + 产出形态 + 分档,作为增强层不破坏现有 vision/hld/lld 三表 | 推翻现有三表重写(失稳定性)/ 统一强制表格(僵化,类图难进表)/ 不标产出形态(回退 hld_v1 散文) |
| HLD/LLD 判别 | **phase-invariant vs incremental**(定义 + 两句判别问句) | 定义让新人理解,问句让 agent 可操作 | 只给判别问句不写定义(新人难理解) |
| 最小必含分档 | **完整档全量 / 坍缩档精简** | 沿 D19 坍缩规则,各档保留必需约束 | 三档统一全量(小项目负担)/ 坍缩档免最小必含(失防简化) |

**产出形态**:选型表含被否决列。

## H3 接口契约(skill 内部 + 副本间 + 项目间)

### 3.1 边界契约

| 边界 | 契约 | 类型 |
|---|---|---|
| design-Q ↔ 项目 CLAUDE.md | 声明识别:skill 读 CLAUDE.md 关键词,命中取该节指示的落盘根 | 软契约(自然语言) |
| design-Q canonical ↔ 四副本 | 落盘映射同步:canonical 改 → 副本同步 → 各 DESIGN.md 记录(OD-8) | 硬契约 |
| design-Q ↔ long-running | 归档路径:long-running 读 `<落盘根>/questionnaires/archive/`;机制不动,只路径配置化 | 硬契约 |
| skill ↔ 项目固有文件 | CONTEXT.md / OPEN-DECISIONS.md / TODO.md 路径**不动**(项目自定) | 硬约束 |

### 3.2 硬约束(实现期不能偏离)

1. **声明识别关键词清单固定**:「落盘根 / 落盘速查 / harness 区 / 设计产物落 / harness 文件」(Q1.1 D);新增关键词需 design-Q DESIGN.md 记录。
2. **落盘前确认点不可省**:首次落盘 + 探测到项目结构变化时,必须 AskUserQuestion 确认根路径。
3. **四副本落盘映射必须一致**:canonical 与三副本的落盘映射表逐字一致,否则 skill 落盘分裂。
4. **骨架归属不扩散**:判别法则 + 最小必含只进 design-Q STAGE-SKELETONS.md,不进 retro/grill/action 骨架。

**产出形态**:契约清单。

## H4 部署与运维(skill 生效与维护)

- **怎么跑起来**:改 `~/.claude/skills/` 下文件 = 下次任何项目调用 design-Q 即用新规格。无构建、无重启、无版本号(用户级 skill,文件即规格)。
- **怎么监控/验证健康**:① dogfood 自检——本次 HLD/LLD 对照新骨架「最小必含」逐项核对(DoD-4);② 跨项目调用验证——本仓库(声明命中 harness/)+ 无 harness/ 项目(懒创建/声明覆盖)落盘路径正确。
- **怎么排查问题**:落盘位置异常 → 查 CLAUDE.md 声明是否命中关键词 → 查落盘前确认记录 → 查 design-Q DESIGN.md 决策(D23–D26)。

**产出形态**:运维清单。

## H5 架构决策识别(ADR 三条件核对)

| 决策 | 难逆转 | 会困惑 | 真权衡 | 去向 |
|---|---|---|---|---|
| **D23 落盘路径配置化(方案 R)** | ✗(文件可改回) | ✓ | ✓ | 难逆转性不足 → design-Q DESIGN.md |
| **D24 HLD/LLD 判别法则** | ✗(骨架可改回) | ✓ | ✓ | 难逆转性不足 → design-Q DESIGN.md |
| **D25 最小必含 + 产出形态** | ✗(骨架可改回) | ✓ | ✓ | 难逆转性不足 → design-Q DESIGN.md |
| **D26 全局生效** | ✗(文件可改回) | ✓ | ✓ | W01 Q2 已定 → design-Q DESIGN.md(不跨域立 ADR) |

**本次不新增 ADR**(W01 Q1=D 裁决):四项均双向门,难逆转性不足 ADR 三条件,全记 design-Q DESIGN.md(D23–D26)。若日后某改动证明需重访(如方案 R 在多项目引发落盘混乱),再升 ADR。

**产出形态**:ADR 候选表(本次 0 条 ADR / 4 条 DESIGN.md)。

---

## 落地动作清单(hld → lld 输入)

1. design-Q STAGE-SKELETONS.md 改造:头部「HLD/LLD 判别法则」节(定义 + 两句问句)+ 每项「最小必含」子项 + 每项「产出形态」+ 坍缩档分档节
2. design-Q SKILL.md:主流程第 2 步(路径决定)+ 第 4 步(落盘映射配置化)+ 3 处 `docs/` 字符串清除
3. design-Q PROCESSING-RULES.md:落盘映射表 `docs/design/` `docs/questionnaires/` `docs/adr/` → `<落盘根>/`
4. design-Q QUESTIONNAIRE-FORMAT.md:「文件约定」节路径配置化
5. design-Q DESIGN.md:D23–D26 决策记录
6. 四副本同步:grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md(落盘映射)+ SKILL.md(路径字符串)+ QUESTIONNAIRE-FORMAT.md(文件约定)
7. 四副本 DESIGN.md 各记「2026-08-06 落盘路径配置化同步」(OD-8 重访触发①)
8. dogfood 自检:本次 HLD/LLD 对照新骨架最小必含(见下 + LLD 末尾)

---

## HLD 自身最小必含自检(dogfood,改动 3 实战)

对照新骨架 HLD 五项的最小必含子项(Q3 确认稿),逐项核对本 HLD:

| 骨架项 | 最小必含子项 | 本 HLD 落点 | 自检 |
|---|---|---|---|
| H1 系统架构 | a 模块/区划分清单 | H1.1 模块表(7 行) | ✓ |
| | b 每模块职责一句话边界 | H1.1 表「职责边界」列 | ✓ |
| | c 数据/控制流向 | H1.2 路径决定流 + 副本同步流 | ✓ |
| H2 技术选型 | a 选型项 | H2 表(5 项) | ✓ |
| | b 选它的理由 | H2 表「理由」列 | ✓ |
| | c 被否决项(≥1) | H2 表「被否决项」列 | ✓ |
| H3 接口契约 | a 边界处契约 | H3.1 边界契约表(4 边界) | ✓ |
| | b 硬约束 | H3.2 硬约束(4 条) | ✓ |
| H4 部署运维 | a 怎么跑起来 | H4「即时生效」 | ✓ |
| | b 怎么监控/验证健康 | H4「dogfood 自检 + 跨项目验证」 | ✓ |
| | c 怎么排查问题 | H4「排查链」 | ✓ |
| H5 ADR 识别 | a 逐条核对三条件 | H5 表(D23–D26 × 三条件) | ✓ |
| | b 不满足的记哪 | H5「全记 DESIGN.md」 | ✓ |

**自检结果**:HLD 五项 × 最小必含子项全部覆盖,产出形态(模块表/流向图/选型表/契约清单/运维清单/ADR 表)齐备。本 HLD 非简化版(对照 hld_v1 反面:开放散文 + 章节级越界)。dogfood 通过。
