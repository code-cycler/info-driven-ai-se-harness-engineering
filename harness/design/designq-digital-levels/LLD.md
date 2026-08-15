# LLD · design-Q 数字层级改造(feature-designq-digital-levels)

> **导览块**
> - 本层位置:lld(构建路径,incremental);上游 [HLD](HLD.md)(架构契约已定案含压测修订)/ [VISION](VISION.md)(验收判据已可核验化)
> - 覆盖:八阶段构建计划(P0–P7,doctor 优先序)、每阶段文件级改动清单、DoD、依赖与预估
> - 上下游依赖:HLD §2 命名/§3 协议/§4 停点双模式/§6 部署为硬约束;执行序按 lld W00 补充声明「doctor-H 优先测试」调整
> - 契约项声明:P0 双向同步与 P1 backup 顺序不可换;P6 前置 = P2–P5 全 DoD;P7 前置 = P6 人确认

## L1 阶段拆分(依赖链)

| 阶段 | 内容 | 依赖 | DoD(可验证) |
|---|---|---|---|
| **P0 双向同步** | 全局⇄项目三 skill **分类同步**(通用改进双向同步;豁免差不同步) | — | 同步后 `diff -rq` 剩余差**仅豁免类**并具豁免清单(执行修正 2026-08-16:① doctor DESIGN.md = 宿主适配路径差,各自正确;② doctor CHANGELOG.md = 用户跨项目私有日志含真实名,**单向防火墙禁止全局→项目**,防脱敏事故;「两侧完全一致」原判据不现实) |
| **P1 backup** | 同步后全局版三 skill 目录 diff 存档至本 feature `global-backup/` | P0 | 三套 patch 齐全 + 存档清单 |
| **P2 doctor 拓展先行** ⭐(用户优先测试) | HARNESS-RULES 增补(层级规则/存量改造/迁移映射表)+ SKILL.md 触发词 + harness-check.py(LN 校验 + 豁免清单) | P0/P1 | grep 锚点核验 + harness-check 对 LN 样例通过 + **用户优先测试 doctor 能力**(存量改造/迁移映射小案例) |
| **P3 design-Q 主改造** | STAGE-SKELETONS 四部分重写 + SKILL.md(定模/层闸门/L0 自检/收尾停点链) | P0/P1(P2 的 LN 命名规范已在 HLD 定案,不阻塞) | 反简化核对 + 模板库五件齐全 + 停点链 grep |
| **P4 引擎四副本同步** | stage 枚举改层名语义 + 命名 LN 制,四 skill 的 FORMAT/PROCESSING 各两处 | P3(术语依赖) | 四副本 × 两处 grep 一致;OD-8 联动记录 |
| **P5 long-running 双模式** | 单 agent 默认 + 准备/执行模式节 + 任务包 schema + 反推规则 LN 制 + 三处禁令限定式(provisional)+ 多 agent 通信(SendMessage) | P0/P1 | 六节改动 grep + 禁令三处 provisional 标注 |
| **P6 装载 + DOGFOOD** | 改造文件替换全局版 → DOGFOOD 双案例(小 2 层 / 中 3 层含插层) | P2–P5 全 DoD | 走通三要素(LN 产物 + 自检真实触发留痕 + 人确认可用)+ 过程信号即时留痕 |
| **P7 回灌 + 收尾** | 全局版合并回项目版(脱敏差)→ OD-24 关闭 → retro-Q | P6 人确认 | harness-check exit=0 + 脱敏 0 + retro 完成 |

**执行序**:P0 → P1 → **P2(doctor,优先测试)** → P3 → P4 → P5 → P6 → P7(lld W00 补充声明裁决;P2 提前不破坏依赖——LN 命名规范以 HLD §2 为准)。

## L2 各阶段文件级改动清单

**P2 doctor 拓展**(全局版三个文件 + 项目 scripts 一个):
- `HARNESS-RULES.md` 增补:六、层级设计文档规则(LN 命名 `L<N>-<功能1>-<功能2>….md` / 布局:feature 目录或单文件多节 / 存量豁免清单);七、存量结构改造流程(盘点既有文档 → 语义映射到 LN 结构(最小必含总览为核对基准)→ 缺项标「待补」不代写 → 人确认成档);附:旧档迁移映射表(坍缩 hld 档 → L0+L1;坍缩 lld 档 → L0+L2;完整档 → 三层;每行「旧语义 → 新落点」)。
- `SKILL.md`:触发词补「层级改造/迁移/存量规范化」。
- `scripts/harness-check.py`(项目侧):LN 命名正则校验 + L0 缺失提示(feature 目录有 L1+ 无 L0 = 违规)+ EXEMPT 存量旧命名(VISION/HLD/LLD 至迁移完成)。

**P3 design-Q 主改造**(全局版两个文件):
- `STAGE-SKELETONS.md` 全文重写:① 总则(混合制:L0-vision 固定 + L1+ 浮动自声明 + 常用模板;命名规范;单/多文件形态)② 最小必含总览表(层 × 最小必含 × 反简化锚点)③ 模板库(L0-vision 含自检节与写法约束「验收按可独立验证条目写」/ L1-contract / L2-build / 自声明模板)④ 协议集(判别三问/裁决双落点/插层/回退/自检五信号⑤双签);头部导览块;旧术语别名注记(VISION= L0、HLD= L1、LLD= L2)。
- `SKILL.md`:§0 定模节改层数判定(最小 1 层 + 自检);§2 W00 归属按形态分派;§5 循环终止改层闸门(重开只重过受影响层);§5 收尾停点链(压测提议 → **多线程询问(必停)** → long-running 衔接)。

**P4 引擎四副本**(全局版四 skill × 2 文件,仅两处):stage 枚举注释 + 问卷命名规则;PROCESSING-RULES 若有 stage 词汇同步。

**P5 long-running**(全局版 SKILL.md):§3 任务包字段规范;§5.3 反推规则(最低构建语义层 + L0 兜底);§5.4 停点衔接;新增「准备模式/执行模式」节(单默认/多拓展、Claude Code 后台 agent + SendMessage、合并三层防线);§6/§8/§10 禁令限定式(provisional);description 补触发词。

## L3 接口规格

- **LN 文件 schema**:frontmatter(`level: 0/1/…`、`feature: <slug>`、`status`)+ 头部导览块四行(位置职责/覆盖/上下游依赖/契约项声明)。
- **任务包 schema**(HLD §4 已定):线程名/分支、范围(L0 验收锚点)、DoD、依赖与线程边界、禁止越界项。
- **变更留痕接口**:每阶段 patch 存 `changesets/P<n>.patch` + 变更清单 md;过程信号即时入处理报告/TODO(压测补充声明)。

## L4 DoD 汇总(每阶段 + 回归)

- 每阶段完成即跑:harness-check.py(项目侧)+ 脱敏门(变更内容记录前)。
- P6 走通三要素为硬验收(见 L1 表);L0 自检真实触发至少一次(两案例合计)。
- 反简化核对:STAGE-SKELETONS 总览表逐行核对 P6 案例产物。

## L5 依赖与预估

- P0/P1:半会话(同步 + 存档);P2:1 会话(含用户优先测试);P3:1 会话(最重);P4:半会话;P5:1 会话;P6:1–2 会话(真实案例不可压缩);P7:半会话 + retro。
- **总计约 3–4 个工作会话**;关键路径 = P3 → P4 → P6。
- 外部依赖:DOGFOOD 沙盒可用(题材 P6 人选题);Claude Code Agent tool/SendMessage(多 agent 拓展,P6 案例若用多线程则验证)。
