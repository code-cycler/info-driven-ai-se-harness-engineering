# HARNESS-RULES · harness 文件组织权威规则

> harness 区(`项目根/harness/`)文件组织的**唯一权威源**。各 skill SKILL.md 落盘路径不再内联复制本规则,只引用「分层见 HARNESS-RULES.md」。
> 权威性:[ADR-0012](../../harness/adr/0012-harness-layering-rule.md)(分层规则)+ [ADR-0013](../../harness/adr/0013-harness-layering-migration.md)(迁移执行)+ [ADR-0011](../../harness/adr/0011-abandon-plan-r-hardcode-harness.md)(硬编码 harness/)。
> 修订:改本文件 = 改 harness 组织规则,须同步 [CHANGELOG](CHANGELOG.md) 留痕。

## 一、分层定义(design/)

`harness/design/` 下的设计文档按是否「feature 级设计」分层:

**判定句**:该设计是否会被独立引用 / 与其它 feature 冲突?
- **是 → `design/<feature-slug>/` 子目录**(feature 级设计:有独立设计套 VISION/HLD/LLD,可独立引用);
- **否 → 裸放 `design/` 根下**(全局/单文件设计,如方法论修订)。

示例判例(本仓库现状):
- feature 级(子目录):`repo/`、`skill-spec-revamp/`、`feature-skills-harness-consistency/`、`doctor-harness/`;
- 全局设计(裸放):`VISION.md`(methodology v3 设计套)、`hld_v2.md`、`lld_v2.md`、`hld-methodology-separation.md`。

**版本历史子目录**(2026-08-17 增补,外部项目 dogfood 触发):feature 目录内被新版本取代的工件版本(如 `roadmap_v1`、`report_v1` 等历史版本)移入 `design/<feature>/history/`——只移不删、文件名不变、当前版本留 feature 根;迁移走 MIGRATION-FLOW(相对链接重算 + 断链回归 + 校验);`history/` 内文件的区外相对链接同步重算(如 `../evidence/`)。

## 二、归属判据(哪个根建 harness)

一句判据:**子模块有独立 CLAUDE.md / 独立 git / 独立发布边界 → 子模块根建自己的 `harness/`;否则归主根。**

- 默认:单仓库场景归主根 `项目根/harness/`;
- 多子项目仓库:子模块满足上面任一条件才独立建 harness,否则与主项目共用;
- 落盘前轻量校验(pwd 是否在含 harness/ 的项目根),防工作目录错位误落。**归属校验由各 skill 落盘前执行**(grill-Q Q6 回灌:doctor-harness 只提供判据,不提供校验工具);多项目场景的真实落地待 dogfood(触发时各 skill 补 pwd 检查)。

## 三、命名规范(questionnaires/)

问卷命名模式(各 skill 生成问卷时遵守):

| 模式 | 命名 | 示例 |
|---|---|---|
| init | `<stage>-w<NN>.md`(stage ∈ vision/hld/lld) | `vision-w01.md` |
| feature | `feature-<slug>-<stage>-w<NN>.md` | `feature-repo-design-hld-w00.md` |
| grill | `grill-<slug>-w<NN>.md` | `grill-repo-design-w01.md` |
| retro | `retro-<主题>-w<NN>.md` | `retro-repo-design-w01.md` |
| confirm | `confirm-<slug>-w00.md` | `confirm-skill-harness-sink-w00.md` |

**slug 规范**:来源 = feature 名 / 主题名 kebab-case;去重(生成前自查同 prefix 已有文件);禁通用词(skill/design 等易混淆词)。

**活跃区子目录**(2026-08-14 增补):活跃问卷默认可按 feature/主题建 `questionnaires/<feature>/` 子目录(与 `archive/<feature>/` 对称,便于同 feature 多份活跃问卷归拢);归档时移入对应 `archive/<feature>/`,子目录空了即删。

**豁免清单**(存量已偏离,不清扫,作已知项):`feature-skill-*` vs `feature-skills-*` 近似前缀(历史遗留,读文件时注意区分)。

## 四、归档规则(archive/)

- **归档按 feature/主题**建 `archive/<feature>/` 子目录(新归档 + 存量整批迁移,2026-08-08 用户裁决由「存量不挪」修订为「允许整批迁移」,走 MIGRATION-FLOW 断链回归);
- 非单一 feature 归属的散件(如 confirm-list)入 `archive/_misc/`;
- **归档 README 索引**:列出子目录与归档问卷,便于检索;
- 只移不删,文件名不变。
- **superseded(作废)问卷**(2026-08-14 增补):未答完即被问卷外路径取代的问卷,按 superseded 处置——status 改 `archived`、文件尾部加作废注记(日期 + 取代路径 + 「不作为设计决策依据」),迁入对应 `archive/<feature>/`;不删除、不留在活跃区。status 定义见各问卷引擎 QUESTIONNAIRE-FORMAT.md。

## 五、布局合规校验

`python3 scripts/harness-check.py [harness_root]` 检查:问卷命名正则 / ADR 编号连续(0001 起无跳号)/ 归档位置(processed/archived 问卷在 archive/)。违规清单输出,0 违规时无输出。分层迁移后跑 0 违规 + 0 断链。

**「布局合规」定义**(grill-Q Q10 回灌):= 命名/ADR 编号/归档位置三检查(**脚本可查**,harness-check.py 覆盖)+ design/ 分层(**人工判据**,脚本 report 模式列出供人审,判定句见第一节)。分层判定句需语义判断(可独立引用/冲突),非纯格式,故脚本不强校验分层对错,只报告现状。

## 六、治理文件归属(OPEN-DECISIONS / TODO / CONTEXT / ADR)

2026-08-14 用户裁决(openorbbecsdk dogfood 触发):

- 项目已建 `harness/` 的:**OPEN-DECISIONS.md / TODO.md / CONTEXT.md 归 `harness/` 根**;ADR 归 `harness/adr/`(懒创建,0001 起编号)。治理文件是 harness 内部组织形态,不污染项目根 `docs/`(与 ADR-0011/0012 同一精神)。
- 项目无 `harness/` 的:沿用各 skill 原约定(grill-with-docs:`docs/OPEN-DECISIONS.md` 或 CONTEXT 旁)。
- 各 skill 文档不内联复制本条路径,引用「治理文件归属见 HARNESS-RULES.md」。

## 七、层级设计文档规则(design/ LN 制,2026-08-16 P2 增补)

> 来源:feature-designq-digital-levels(P2 doctor 拓展先行);design-Q 数字层级制的布局侧规则,模板与协议细节见 design-Q STAGE-SKELETONS.md(层级制,P3 落地)。

**命名**:`L<N>-<功能1>-<功能2>….md`——数字-功能式,尾缀 kebab-case 且**覆盖该层所有主要功能**(一眼可识);L0 固定以 `vision` 起头(如 `L0-vision-scope-acceptance.md`、`L1-contract-interface.md`、`L2-build-dod.md`)。

**布局**:同一 feature 的层文件归 `design/<feature>/`;两种合法形态——① 多文件(每层一文件);② 单文件多节(小项目,文件内 `## L0-vision-…` 节标题分节,文件头做全层导览)。

**头部导览块**(每层文件开头,四行):本层位置与职责 / 覆盖范围 / 上下游层依赖 / 契约项声明(本层哪些项是下层硬约束)。

**豁免清单(存量合法至迁移完成)**:`VISION.md` / `HLD.md` / `LLD.md` / `hld_v2.md` / `lld_v2.md` 等旧三件命名(含大小写变体)在存量设计套中合法;存量套迁移按第八节映射表执行,迁移完成前 harness-check 不报违规。

**层级顺序**:feature 目录含 L1+ 层文件而无任何 L0-* 文件 = 违规(L0 恒在);LN 文件名格式偏离 `L\d+-[a-z0-9-]+\.md` = 违规。

## 八、存量结构改造流程(无 harness 文件 → 标准结构,2026-08-16 P2 增补)

> 将**无 harness 文件**的项目(可能有基本构想、基本设计、散落决策文档)改造为当前方法论的标准结构。铁律:AI 只组织与映射,不代写设计(缺项标「待补」,由人后续填)。

流程五步:

1. **盘点**:扫描项目根/文档区,识别既有方法论工件(构想/基本设计/决策记录/问卷散件),列清单(文件 × 内容语义);
2. **建区**:按第二节归属判据确定 harness 根,建 `harness/`(design/ + questionnaires/ + adr/ 按需懒创建);
3. **语义映射**:按下方迁移映射表把既有内容映射到 LN 结构(或无 LLD 时代的旧三件结构——尚未启用层级制的项目按 design-Q 现行制);**最小必含核对**:以 design-Q STAGE-SKELETONS 的总览为基准逐项对照;
4. **缺项标注**:映射后缺失的最小必含项在对应层文件中标 `<!-- 待补:xxx —— 原始信息缺失,需人补写 -->`,不代写;待补清单同步写入项目 TODO;
5. **人确认成档**:映射结果 + 待补清单交人审查,人确认后文件落位,CHANGELOG 留痕。

**DoD = 标完即成档**:改造交付 = 结构 + 缺口标注;「人填完待补设计」不计入改造验收(设计归人)。

**构想直生模式**(2026-08-16 grill-with-docs 深钻增补):输入只有**基础构想文件**(无任何设计文档)时的特例路径——「从构想直接到 LN」:

1. **提取归位**:构想文件内容按 LN 模板**零改写落位**(原句保留:目标/范围/场景/验收 → L0;契约性内容如选型/模块边界 → L1;阶段/构建想法 → L2);
2. **骨架补全**:模板中构想未覆盖的节,建空骨架 + 标 `<!-- 待补:xxx —— 需人补写 -->`;**AI 不新增任何设计内容**(组织与代写的边界 = 层文件里每句实质内容都必须来自构想文件原文;结构模板是方法论资产,不是设计);
3. **层范围 = 内容驱动**:L0 必生(哪怕构想只有一句话);构想能支撑的层才生成;**纯空层不预建**——需要时按 L0 自检信号/插层协议增层(防形式主义);
4. **人确认成档**:直生产物 + 待补清单交人审查确认;成档后如需深化,转 design-Q 从对应层续走问卷。

与主流程的关系:有设计文档(基本设计/散落决策)→ 走五步主流程(语义映射);只有构想 → 走直生模式。两条路径共用 DoD(标完即成档)与铁律(不代写)。

**存量治理文件迁移**(2026-08-16 补,存量改造场景常见形态——项目已有部分治理文件但无 harness/ 区):

- 已有 `CONTEXT.md`(在项目根或 docs/):整体迁 `harness/` 根(第六节),内容不改;
- 已有 `docs/adr/`(或同类 ADR 目录):**整体迁入 `harness/adr/`,保留原编号与内容**——不重编号、不改写正文;与第六节「0001 起编号」的关系:新建 ADR 续存量最大号递增,不与存量冲突;
- 已有 OPEN-DECISIONS / TODO / 复盘文档:迁 `harness/` 根(第六节),路径变化后修复引用断链(MIGRATION-FLOW 第 3 步)。

**自包含大文档的映射策略**(2026-08-16 补):单份设计文档同时含构想 + 架构 + 模块/实现细节(v0.x 演化型自包含文档)时,二选一由人定:① **单文件多节形态**——文档按 LN 节结构重组(原文件保留不删,移入 `design/<feature>/` 并在头部导览标注层对应关系);② **拆层多文件**——按章语义拆到 L0/L1/L2 多文件(原文件移 `design/<feature>/legacy/` 或标 superseded 留档)。判据:文档是否仍被频繁整体修订(是 → ① 保整体;否 → ② 利于层独立演进)。

**旧档迁移映射表**(VISION/HLD/LLD 旧三件 → LN 新制;存量套迁移与存量改造共用):

| 旧产物/旧档 | 新落点 | 说明 |
|---|---|---|
| VISION.md(目标/范围/场景/验收/风险) | `L0-vision-<…>.md` | L0 恒在;验收标准按可独立验证条目写 |
| HLD 契约类内容(接口契约/全局选型/模块边界) | `L1-contract-<…>.md` | 契约项在导览块声明 |
| HLD 非契约内容(部署运维等稳定架构事实) | `L1-<相应功能>.md` 自声明层 | 混合制:职责自声明 |
| LLD.md(阶段拆分/详细设计/DoD/依赖) | `L2-build-<…>.md` | 阶段拆分是 feature 反推源(long-running) |
| 旧坍缩 hld 档(vision→hld 两件) | L0 + L1 两层 | 语义等价映射 |
| 旧坍缩 lld 档(vision→lld 两件) | L0 + L2 两层(契约内容并入 L0 或 L2 标注) | 语义等价映射 |
| 旧完整档(三件) | 三层(L0/L1/L2) | 一一对应 |
| hld_v2/lld_v2 等版本号变体 | 同上映射,版本号入尾缀或历史注记 | 历史版本本身不迁移(留原位) |

## 九、治理历史布局(2026-08-20 P0 增补,[ADR-0024](../../harness/adr/0024-governance-history-split-dual-form.md))

> 治理历史(裁决出处注记/修订史/dogfood 记录/同步记录/漂移历史)与规则本体分离——「移层不删除」,换 LLM 上下文纯净与单一检索去处。规格全文见 [L1-contract-gov-history-split](../../harness/design/governance-history-split/L1-contract-gov-history-split.md);本节为布局侧权威摘要。

**① 载体命名与粒度**:

| 域 | 载体 | 存在侧 |
|---|---|---|
| skill 域 | `skills/<skill>/CHANGELOG.md`(每 skill 一份,追加式条目:日期+五类枚举[裁决/修订/dogfood/同步/升格]+反向指针`影响:<文件>#<节标题锚点>`+出处) | **仅项目侧** |
| skill 域 | `skills/<skill>/FORK-NOTES.md`(有意分叉声明,条目级精简一行一条,不设数字上限) | 双侧逐字节一致 |
| skill 域(特例) | `~/.claude/skills/doctor-harness/DOGFOOD-LOG.md`(外部项目实操明细,含真实名,禁入公开仓库) | **仅全局侧** |
| design 域 | `design/<feature>/CHANGELOG.md`(feature 目录内);裸放全局档内嵌历史 → `design/CHANGELOG.md`(仅有可迁内容时建) | 项目侧 |
| 仓库内部状态史 | `harness/STATUS-LOG.md`(承 CLAUDE.md 状态节历史;根 CHANGELOG.md 保持纯对外语义) | 项目侧 |

**② 历史层单侧存在规则**:CHANGELOG / DESIGN 类(`HISTORY_LAYER`,DESIGN 为 2026-08-20 P4 执行期增补——Q2-A 裁决全局侧无 DESIGN 的直接后果)仅项目侧存在 = 合法,仅全局侧存在 = 违规;DOGFOOD-LOG 类(`GLOBAL_ONLY`)仅全局侧存在 = 合法——由 `scripts/skills-sync-check.py` 类规则判定(与 EXCEPTIONS 白名单正交:白名单管「内容不同的裁决例外」,类规则管「历史层单侧存在的常态」)。**双侧常态性形态分工**:全局侧 = 分发洁净形态(SKILL.md + 引擎/模板 + FORK-NOTES),无 DESIGN.md、无 CHANGELOG;项目侧 = 车间完整形态。

**③ 索引指针要求**:凡历史迁出处,原位置必留一行指针;SKILL.md 索引行统一落头部(frontmatter 后首行):`> 治理历史见本目录 CHANGELOG.md;有意分叉见 FORK-NOTES.md`。

**④ 增量记录规则(五类触发,处理事件的 agent 同事件写入,不批处理)**:① skill 规格修订 ② 裁决产生(问卷处理落盘同时)③ dogfood 轮次 ④ 双侧同步动作 ⑤ 教训升格(同类 ≥2 条按 [ADR-0023](../../harness/adr/0023-skill-md-layered-slimming.md) 升格回规则本体,条目标「已升格」)。附:修订节标题时同事件更新指向该文件的「影响:」锚点。

**⑤ 与 LN 命名规则的关系**:CHANGELOG.md / FORK-NOTES.md / DOGFOOD-LOG.md / STATUS-LOG.md 非 LN 层文件,**不受第七节 `L\d+-` 命名正则约束**,harness-check 不报违规。

**「规则本体」判定词**(sync-check 与铁律 8 用词):= skill 文件中去除治理历史后的现行有效内容,含 frontmatter、机制条款、自检命令、索引导向行;FORK-NOTES.md 整体属规则本体(分叉是现行状态声明)。