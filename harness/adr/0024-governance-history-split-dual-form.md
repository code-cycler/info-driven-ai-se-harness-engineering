# ADR-0024: 治理历史分离与双侧常态性形态分工

- 状态:accepted(2026-08-20,design-Q feature governance-history-split,L0+L1 两层全链)
- 决策日期:2026-08-20

## 背景

治理历史(裁决出处注记 / 修订史 / dogfood 记录 / 同步记录)散落三域:8 个 SKILL.md 的日期注记(design-Q 16 行最多)、DESIGN.md 治理历史占比 40–85%、项目 CLAUDE.md「仓库状态」节 25 行(自动加载的常驻上下文)。SKILL.md 是每次触发的常驻 token 成本——第一支柱「有效上下文」在自家仓库违例。ADR-0023 已立「出处/日期移 DESIGN.md」分层原则,但 2026-08-19 评估「注记多为规则出处不可分割,全量迁移低收益缓行」。2026-08-20 用户立项设计(grill-boundary-canonical-w01 补充声明①升级为 design-Q feature),并裁决双侧形态分工:全局 skill 不再记录演进(模拟开发者开箱即用),项目内 skill 保留演进历史。

## 决策

1. **注记全迁**:SKILL.md 出处型与叙述型注记**全部**迁出(推翻 2026-08-19「缓行」执行判断,ADR-0023 决策 1 原原则回归);SKILL.md 两侧同形,只留规则现值 + 文件级一行索引导向。
2. **双侧常态性形态分工**:全局侧(`~/.claude/skills/`)= 分发洁净形态——文件集 = SKILL.md + 引擎/模板文件 + FORK-NOTES.md(有意分叉声明,双侧逐字节一致),**无 DESIGN.md、无 CHANGELOG**;项目侧(`skills/`)= 车间完整形态。双侧从「逐字节一致(仅白名单例外)」转为常态分工。**(压测 Q2-C 补充)**全局侧 doctor-harness 特例可有 `DOGFOOD-LOG.md`——外部项目实操明细(含真实项目名)的私有日志,语义 = 实操记录而非 skill 演进史,不触发历史层类规则(非 CHANGELOG 名),sync-check 白名单登记;公开侧对应条目脱敏后并入项目侧 CHANGELOG 并注「实操明细见全局侧日志」。
3. **载体三件**:① `skills/<skill>/CHANGELOG.md` 每 skill 一份,仅项目侧,追加式条目(日期 + 五类枚举 + 反向指针「影响:文件#节标题锚点」+ 出处);② `FORK-NOTES.md` 分叉声明双侧一致;③ `harness/STATUS-LOG.md` 仓库内部工作状态史(根 CHANGELOG 保持纯对外语义,记录规则原文排除内部治理)。
4. **sync-check 升级为类规则**:`HISTORY_LAYER = {"CHANGELOG.md"}`——仅项目侧存在 = 合法;EXCEPTIONS 白名单清空(doctor-harness/CHANGELOG.md 现例转入类规则);铁律 8 语义改写为「规则本体双侧一致 + 历史层仅项目侧」。
5. **增量协议**:五类触发(规格修订/裁决产生/dogfood/双侧同步/教训升格)由处理事件的 agent 同事件写入;ADR-0023 升格机制衔接(同类 ≥2 条升格回 SKILL.md 规则本体,条目标「已升格」)。
6. **存量迁移一次收口**:单次 long-running 分阶段 P0 协议落盘 → P1 skill 域 → P2 harness/design/ 域 → P3 CLAUDE.md 域 → P4 全局侧重整 + 三脚本验收;迁移对照表 `migration-map_v1.md` 为「逐字可查」核对基准;全局侧删除走 git mv 归档不真删。

## 替代方案(被否决)

- **发布管道**(项目→全局生成产物)——工程量最大,全局侧临时手改无处安放;留 OD-10 终态候选。
- **sync-check 白名单大扩展**——8 skill × N 文件清单膨胀,例外失焦。
- **全局侧 archive/ 子文件夹收 DESIGN.md**——需又一反向豁免类,复杂度上升。
- **家族级一份 CHANGELOG**——破坏 skill 自包含。
- **SKILL.md 压缩引用式注记**——逐条短引用仍占行,编目量大。
- **根 CHANGELOG 兼收内部状态史**——其记录规则明确排除内部治理,GitHub 侧栏混入内部史稀释对外定位。

## 后果

- (+) SKILL.md 常驻上下文成本下降,第一支柱落到仓库自身形态;全局侧开箱即用 = OD-10 分发洁净目标态提前达成。
- (+) 治理历史单一去处 + 双向指针(正向索引行 / 反向「影响」指针),检索 ≤2 跳。
- (+) 教训有升级通道(ADR-0023 衔接),历史层不丢信息(移而非删)。
- (−) 单读 SKILL.md 失去「为什么」——索引行 + 反向指针对冲(ADR-0023 已认此代价)。
- (−) 迁移工程量 = 8 skill × 双侧 + 三域(P0–P4 一次收口摊薄)。
- (−) 双侧不再全同,同步语义复杂度上升——由类规则 + 铁律 8 新措辞承载。

## 关联

- 来源:[feature-governance-history-split L0-vision W00/W01 + L1-contract W00](../questionnaires/archive/governance-history-split/)(2026-08-20,W00 18/19 + W01 5 题 + 小波澄清 1 + L1 W00 20/20 全采纳)。
- **压测回灌**:[grill-gov-history-split-w01](../questionnaires/archive/governance-history-split/grill-gov-history-split-w01.md)(2026-08-20,10 题:9 采推荐 + Q10 推翻推荐选 B;0 逃生舱/0 跑偏;10 项修订全授权执行——含决策 2 补 DOGFOOD-LOG 特例、L1 补全局侧删除前置检查/引擎头部拆分/锚点更新义务/「规则本体」定义/索引行落位/根 CHANGELOG 义务/TODO 头部压缩/FORK-NOTES 条目级精简)。
- 设计套:[L0-vision-scope-acceptance.md](../design/governance-history-split/L0-vision-scope-acceptance.md) / [L1-contract-gov-history-split.md](../design/governance-history-split/L1-contract-gov-history-split.md)。
- 相关:[ADR-0023](0023-skill-md-layered-slimming.md)(分层原则与本 ADR 的被推翻/衔接关系)、[OD-10](../../docs/OPEN-DECISIONS.md)(分发洁净)、[OD-24](../../docs/OPEN-DECISIONS.md)(双副本策略)、[OD-8](../../docs/OPEN-DECISIONS.md)(引擎漂移)、CLAUDE.md 铁律 8(语义改写随 P0)。
- 执行:HARNESS-RULES 第九节 + sync-check 类规则(含 DOGFOOD-LOG 白名单登记)随 P0 落盘;迁移 P1–P4 见 L1 契约。
