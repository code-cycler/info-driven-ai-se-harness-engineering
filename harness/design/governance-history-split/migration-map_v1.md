# migration-map_v1 · governance-history-split 迁移对照表

> F040(P1 skill 域)迁移对照:源(文件#节)→ 目标(载体#条目)→ 内容摘要。验收 2「逐字可查」核对基准 + 人工抽检底册。P2/P3 域完成后续表(本文件追加)。

## skill 域(P1,2026-08-20)

| skill | 源 | 目标 | 内容摘要 |
|---|---|---|---|
| doctor-harness | DESIGN.md#起源 / #演进记录 / #家族身份状态 | CHANGELOG#2026-08-08·skill 创建(历史回填) | 压测起源叙述 + P1–P4 时间线 + 家族 done 状态;「dogfood 通过」定义保留 DESIGN(V11) |
| doctor-harness | MIGRATION-FLOW.md#头部依据行 | CHANGELOG#P1 条目(日期压缩记录) | 「2026-08-05/08 两次迁移先例」日期引用(先例表正文保留) |
| design-Q | SKILL.md 17 处日期注记 | CHANGELOG 对应时间线条目 | LN 制/题量 10/小波 3/轻量模式/未验证假设/入口闸门/时序/delegate 接口/收尾面板等出处 |
| design-Q | DESIGN.md#引擎同步记录 ×3 / #SKILL.md 分层迁移评估 / 引擎复制声明内事件 / 格式反馈事件 | CHANGELOG 对应条目(评估条含「被 ADR-0024 推翻」注记) | 08-03 预勾/08-06-07 revamp/08-08 格式/08-18 规则4/08-19 评估 |
| grill-Q | SKILL.md 11 处 + 引擎 15 处 + GRILL-SKELETON 2 处 | CHANGELOG + FORK-NOTES | 族间自检/入口闸门/阻塞性分流/质量信号/❌ 分叉族等出处 |
| grill-Q | DESIGN.md#引擎复制声明事件 ×3 / #同步记录 ×3 / #有意分叉声明 | CHANGELOG(分叉现值迁 FORK-NOTES) | 07-24/25/27 漂移与同步 + 08 系同步 + ❌ 分叉族 |
| action-Q | SKILL.md 8 处(含 description)+ 引擎头部 6 条分叉清单 | CHANGELOG + FORK-NOTES | 轻量下限/轻量模式/复用前重验/阈值收紧出处;6 条分叉现值迁 FORK-NOTES |
| action-Q | DESIGN.md#dogfood 案例两例 / #同步记录 ×3 / #revamp(superseded) / #复用前重验扩散 | CHANGELOG 对应条目 | D-1/D-2/D-3 与两案例观察全录 |
| retro-Q | SKILL.md 2 处 + 引擎 11 处 | CHANGELOG + FORK-NOTES | 调研与核实前置/阈值出处;5 条分叉现值迁 FORK-NOTES |
| retro-Q | DESIGN.md#副本声明事件 ×3 / #同步记录 ×2 / #revamp(superseded) | CHANGELOG | 07-24/25/27 preview 漂移两次声明为设计 + 08 系同步 |
| grill-with-docs | SKILL.md 7 处 + OD-FORMAT 1 处 | CHANGELOG(新建,本无 DESIGN) | 通用模式新增与深钻精确化/中途相变/零留痕边界/逃生舱对齐 |
| long-running | SKILL.md 4 处(P5 系) | CHANGELOG(新建) | P5 双模式/LN 衔接/限定式修订出处;JSON 示例时间戳豁免 |
| delegate | SKILL.md 4 处 + DESIGN.md 表内日期与 round 详录 | CHANGELOG(新建) | 创建+round1 详录/round2/full 模式;G 表保留 round 出处 |

**双侧形态**:规则本体(SKILL/引擎/FORK-NOTES)双侧逐字节一致;CHANGELOG ×8 仅项目侧(sync-check 类规则合法);DESIGN.md 6 份仅项目侧(全局侧重整待 P4);grill-with-docs/long-running/delegate 无 FORK-NOTES(无规则本体级分叉)。

## design 域(P2,2026-08-20)

| 源 | 目标 | 内容摘要 |
|---|---|---|
| governance-history-split/L0#CLAUDE.md 域修正注记 | 本 feature CHANGELOG#L0 落点修正条 | 「落点修正 2026-08-20 L1 W00-10」内嵌注记(唯一可迁修订记录) |
| (其余 design/ 全部) | **不迁** | 判据:LN 层文件与裸放档的日期行均为出处引用/裁决出处/版本出处(档案可追溯性正当结构),非修订记录节,可迁内容 = 0 → repo/、readme-revamp/ 不建 CHANGELOG(纯空载体不预建);旧三件 = 存量豁免(待 TODO AI-2);global-backup/、changesets/ = 历史档案文件本体,不动 |
