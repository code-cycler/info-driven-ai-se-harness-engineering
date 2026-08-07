# VISION · design-Q skill 规格整理(落盘路径配置化 + HLD/LLD 职责区分 + 防简化)

> ⚠️ **2026-08-07 状态更新**:本文「落盘路径配置化(方案 R)」部分**已放弃**([ADR-0011](../../adr/0011-abandon-plan-r-hardcode-harness.md)),回归硬编码 `harness/`;**骨架改造(F007:HLD/LLD 判别法则 + 最小必含 + 分档)部分保留**并已回灌仓库。撤销执行见 [feature-skills-harness-consistency/](../feature-skills-harness-consistency/)。

> 来源:design-questionnaire vision 阶段 W00(15 条,采纳 13 / 留空 2)+ W01(2 题:Q1 自定义「harness 文件与项目文件解耦」→ AskUserQuestion 澄清为方案 R;Q2 采纳 C)+ Q1.1 由 R 推导 = D。2026-08-06。
> 上游决策:[OD-8](../../../docs/OPEN-DECISIONS.md)(引擎副本漂移治理)、[hld_v1/v2 + lld_v1/v2](../hld_v1.md)(简化输出反面案例)、[repo/HLD + repo/LLD](../repo/HLD.md)(完整输出正面案例)、design-Q [DESIGN.md](../../../../.claude/skills/design-questionnaire/DESIGN.md)(D1–D22 决策先例)。
> 本文件 = skill 规格整理的构想层;架构方案见 HLD,落地规格见 LLD(后续阶段产出)。**本次设计产物自身须满足新「最小必含」标准(dogfood,见 V3/V4)**。
> **🔧 grill-Q 压测后修订(2026-08-06/08-07)**:Q6(无 CLAUDE.md)回灌 V2;其余 8 项详 HLD/LLD;Q7(retro 落点 + 路径区分)grill-with-docs 深钻定案——retro 文档项目固有 docs/retro/、落盘根边界 = design/questionnaires/adr 三件、skill 内部 vs 宿主路径区分规则(详 [LLD](LLD.md) 2.6)。

## 目标与受众 (V1)

**核心目标**:整理 design-questionnaire skill 规格,三组改动一并落地——

1. **落盘路径配置化(harness 与项目文件分离)**:design-Q 产物(问卷 + 设计文档 + ADR)落盘根从硬编码 `docs/` 改为 `harness/`(默认)+ 项目 CLAUDE.md 声明覆盖 + 落盘前确认。`docs/` 保留为项目自身文件,与 harness 文件解耦。
2. **HLD/LLD 职责区分**:骨架(STAGE-SKELETONS.md)头部加「HLD/LLD 判别法则」,消除当前两处重叠(H3 接口契约 vs L3 接口规格;H1 系统架构 vs L2 详细设计),防 hld_v1 那种「章节级改写混进 HLD」的越界。
3. **防过度简化(最小必含)**:骨架每项加「最小必含」硬约束 + 「产出形态」引导,防 agent 把 HLD/LLD 写成 hld_v1/v2 那样的开放散文提纲。

**受众**:design-Q 维护者本人 + 复用引擎的 grill-Q / retro-Q / action-Q(漂移治理,改动 1 同步)+ 未来 skill 使用者(其他项目调用 design-Q 时落盘行为可预测)。

## 范围 (V2)

### 做什么

1. **落盘路径(改动 1 · 方案 R)**:design-Q 产物落盘根 = `harness/`(默认,无则懒创建);项目 CLAUDE.md 可声明覆盖(如声明用 `docs/`);**落盘前显式确认**路径(防误落)。声明格式 = 自然语言识别 CLAUDE.md 中「落盘根 / 落盘速查 / harness 区 / 设计产物落」等关键词(零侵入,本仓库 CLAUDE.md「落盘路径速查表」自然命中),关键词命中不到时回落 harness/ 默认 + 确认兜底;🔧 **CLAUDE.md 不存在(新项目)则跳过声明识别,直接默认 harness/ + 确认**(grill-Q Q6)。`CONTEXT.md` / `OPEN-DECISIONS.md` / `TODO.md` 等项目固有文件路径**不动**(各项目已定型,W00 #4)。
2. **HLD/LLD 职责区分(改动 2)**:改 design-Q [STAGE-SKELETONS.md](../../../../.claude/skills/design-questionnaire/STAGE-SKELETONS.md)——骨架头部加判别法则(**HLD = 架构骨架,phase-invariant**:系统由哪些模块/区组成、模块边界与职责、模块间契约、全局选型、部署运维、ADR;**LLD = 构建路径,incremental**:阶段拆分、每阶段详细设计、函数级接口规格、每阶段 DoD、依赖预估);判别问句「它会随阶段拆分变化吗?」;重叠项(H3 接口契约 = 模块间/系统边界粗粒度 vs L3 接口规格 = 函数级/阶段内细粒度)显式区分。
3. **防简化(改动 3)**:骨架每项加「最小必含」子项清单(缺一不算该骨架项完成,计入覆盖度判定,沿 lld_v2「§2.1 四必含」先例)+ 「产出形态」建议(表格 / 清单 / 契约格式 / 图)+ 骨架头部反简化声明(HLD/LLD 是可实现期直接执行的规格,不是提纲);按坍缩档分档调节(完整三阶段档全量 / 坍缩为 hld 档 / 坍缩为 lld 档精简,W00 #12)。
4. **影响面同步**:HLD/LLD 职责区分 + 最小必含**只改 design-Q 骨架**(STAGE-SKELETONS.md 是 design-Q 专属,retro 用四节骨架);落盘路径配置化**同步四份引擎副本**(design-Q / grill-Q / retro-Q / action-Q 的 SKILL.md + PROCESSING-RULES.md,OD-8 重访触发①)。

### 不做什么(scope 边界,W00 #7)

- 不改交互机制(问卷格式 / preview 机制 / 逃生舱 / 小波阈值 / opt-in 开关)
- 不改 grill-Q / retro-Q / action-Q 的骨架(只同步落盘路径配置化)
- 不重构 skill 目录结构(OD-8 已决保留现状)
- 不改 long-running 的 feature_list 机制(只同步它读归档的路径)
- 不改 CONTEXT / OPEN-DECISIONS / TODO 的落盘位置(项目固有文件,各项目自定)

## 核心场景 (V3)

- **design-Q 在本仓库运行**:产物(问卷 / VISION-HLD-LLD / ADR)落 `harness/`(CLAUDE.md「落盘路径速查表」声明命中),`docs/` 保持项目文件(methodology / CONTEXT / OPEN-DECISIONS / LICENSE)洁净——本轮 P1–P6 刚完成的 harness 三区不被污染。
- **design-Q 在无 harness/ 的项目运行**:声明识别命中 → 用声明根;无声明 → 懒创建 `harness/`;落盘前确认。对坚持用 `docs/` 的项目(如参考项目),CLAUDE.md 声明覆盖即可,skill 不强制改造。
- **dogfood(改动 2/3 的第一次实战)**:本次 design-Q 产出的 VISION / HLD / LLD **自身**按新骨架(最小必含 + 产出形态)写成完整版(对照 repo/HLD 的表格 + 被否决项 + 接口契约 + 动作清单密度),不得重蹈 hld_v1/v2 简化覆辙。验收 = 本次 HLD/LLD 通过新「最小必含」自检。

## 验收标准 (V4)

- **DoD-1(骨架职责 + 防简化)**:design-Q STAGE-SKELETONS.md 含:① HLD/LLD 判别法则(头部);② 每项「最小必含」子项 + 「产出形态」;③ 重叠项粒度区分(H3 vs L3);④ 反简化声明;⑤ 坍缩档分档。
- **DoD-2(落盘路径配置化)**:方案 R(默认 `harness/` + CLAUDE.md 声明覆盖 + 自然语言识别 + 落盘前确认)落 design-Q 的 SKILL.md + PROCESSING-RULES.md(落盘映射表)+ STAGE-SKELETONS.md(H5 ADR 路径);`docs/` 硬编码路径全部消除。
- **DoD-3(四份副本同步)**:grill-Q / retro-Q / action-Q 的 PROCESSING-RULES.md(落盘映射)+ SKILL.md(路径字符串)同步方案 R;各 DESIGN.md 声明本次同步(OD-8)。
- **DoD-4(dogfood 自检)**:本次 HLD/LLD 自身通过新「最小必含」自检——逐项对照新骨架的最小必含子项,缺一不算过;对照 repo/HLD 完整度,不得退化为 hld_v1 简化版。

## 风险与约束 (V5)

- **引擎副本漂移(W00 #10)**:改 design-Q 落盘映射须同步 grill-Q / retro-Q / action-Q 三份 PROCESSING-RULES.md 副本 + 各 SKILL.md 路径字符串(确认漂移面:design-Q 3 处 + grill-Q 3 处 + retro-Q 3 处 + action-Q 4 处),否则四 skill 落盘路径分裂。**处置**:四份同步(OD-8 重访触发①命中)。
- **配置化可预测性(W00 #11)**:声明自然语言识别可能漏读(项目 CLAUDE.md 措辞各异)→ **落盘前确认点**兜底,用户可纠正;探测魔法(方案 Q)已弃,改声明 + 确认两道。
- **最小必含 vs 坍缩档(W00 #12)**:过严让小项目坍缩场景负担重 → **分档**:完整档全量最小必含;坍缩为 hld / lld 档只保留该档必需子项。
- **全局生效(W01 Q2 = C)**:改 `~/.claude/skills/design-questionnaire/` 立即影响所有项目下次调用,可回退(文件可改回)但影响面广。**处置**:可逆性不足 ADR 三条件(难逆转性不够)→ 记 design-Q DESIGN.md 决策表(标「全局生效 / 可回退 / 双向门」)+ 本 VISION 风险节一句话,不跨域立 ADR(skill 在 `~/.claude` 非本仓库)。

## 动机与推导 (V6)

**为什么改(三因,W00 #14)**:

1. **skill 规格与项目实践脱节**:skill 硬编码 `docs/`(design-Q/grill-Q/retro-Q/action-Q 共 13 处),但本仓库 CLAUDE.md「落盘路径速查表」已写 `harness/` 路径(harness/questionnaires/archive/、harness/adr/ 等)——项目实践先行、skill 规格滞后。本轮 P1–P6 刚把 harness 三区落地,skill 却仍往 docs/ 落,每次手动挪。
2. **简化输出实证骨架缺约束**:hld_v1/v2 / lld_v1/v2 是典型简化输出——骨架「出题方向」是开放散文(如 H1「模块划分、职责边界、数据流向」),无最小必含硬约束,agent 执行时一笔带过;repo/HLD 详细是因为有表格 + 被否决项 + 动作清单。差距在骨架没强制结构化。
3. **HLD/LLD 职责重叠致越界**:hld_v1 把章节级改写(本属 LLD-L2)混进 HLD,H1 标签被特化成「文档架构(各章怎么改)」,丢掉系统级结构思考——判别法则缺失的实证。

**为什么是现在(W00 #15)**:上轮 P1–P6 刚把本仓库 harness 区落地(CLAUDE.md 落盘速查表、harness/design/ + harness/questionnaires/ + harness/adr/ 迁移完成),skill 规格滞后需追平;dogfood 窗口——刚吃过 harness 迁移链接改造的苦头,对「落盘路径」敏感度最高,改 skill 正当时。
