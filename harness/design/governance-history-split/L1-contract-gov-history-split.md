# L1-contract-gov-history-split.md · governance-history-split(治理历史分离机制契约)

> **导览块**
> - 本层位置与职责:契约层——治理历史分离机制的全部契约规格:载体格式、双侧同步规则、存量映射、增量协议、权威落位与文件变更清单。
> - 覆盖范围:三域(skill / harness/design / CLAUDE.md)载体契约 + 脚本契约 + 迁移映射规则 + 增量条款;不含迁移执行的阶段编排(P0–P4 时序见 L0 范围,执行走 long-running)。
> - 上下游依赖:继承 L0 六条验收与双侧形态分工画像(硬约束);下游无层——存量迁移执行与本机制增量维护以本层契约为直接规格。
> - 契约项声明(下层/执行期硬约束):**① 双侧文件集分工(全局侧无 DESIGN.md/无 CHANGELOG)② CHANGELOG/FORK-NOTES/STATUS-LOG 载体格式 ③ sync-check 类规则语义 ④ 索引指针与反向指针要求 ⑤ 增量触发五类 + agent 写入责任 ⑥ 迁移只移不删 + 迁移对照表**——执行期偏离任一项须走 ADR-0021 治理性偏差路径。

> 裁决来源:[feature-governance-history-split-L1-contract-w00](../../questionnaires/archive/governance-history-split/feature-governance-history-split-L1-contract-w00.md)(20/20 全采纳,2026-08-20);上层 [L0-vision-scope-acceptance.md](L0-vision-scope-acceptance.md)。

## 模块与边界(新增/修改/删除清单)

| 动作 | 对象 | 说明 |
|---|---|---|
| 新增(项目侧) | 8× `skills/<skill>/CHANGELOG.md` | 每 skill 一份,追加式 |
| 新增(双侧一致) | N× `skills/<skill>/FORK-NOTES.md` | 存在有意分叉的 skill(action-Q/grill-Q/retro-Q 至少三份,P1 盘点定全量) |
| 新增(项目侧) | `design/<feature>/CHANGELOG.md` 若干 + `design/CHANGELOG.md`(有可迁内容时) | feature 目录内 + 全局档共用;纯空载体不预建 |
| 新增(项目侧) | `harness/STATUS-LOG.md` | 仓库内部工作状态史(承 CLAUDE.md 状态节历史) |
| 新增(项目侧) | `harness/design/governance-history-split/migration-map_v1.md` | 迁移对照表(核对基准) |
| 新增(全局侧私有) | `~/.claude/skills/doctor-harness/DOGFOOD-LOG.md` | 外部实操明细(真实名),压测 Q2-C;sync-check 白名单登记 |
| 修改 | 8× SKILL.md(双侧同形)/ 6× DESIGN.md(项目侧收敛)/ sync-check.py / HARNESS-RULES.md / doctor-harness SKILL.md / 项目 CLAUDE.md | 见下各契约节 |
| 删除(**项目侧** git mv 归档不真删;**全局侧**走删除前置检查,见下) | 全局侧 6× DESIGN.md + 全局侧 doctor-harness/CHANGELOG.md | P4 全局侧重整时;**全局侧 `~/.claude/skills/` 无版本控制(实测非 git),删除不可逆** |

**全局侧删除前置检查(压测 Q1-C,⚠ 单向门防护)**:P4 每删一个全局侧文件前必跑 diff——双侧逐字节一致 → 可删(项目侧 git 副本即存档);**不一致 → 暂停,全局侧独有内容先抢救**(按 Q2 双载体规则并入项目侧或迁 DOGFOOD-LOG)后才可删。已实测当前双侧 6 份 DESIGN.md 完全一致(删除前提当下成立),条款防的是未来增量漂移。

## 载体契约(接口规格,硬约束)

**「规则本体」定义(压测 Q7-C)**:规则本体 = skill 文件中去除治理历史后的现行有效内容,含 frontmatter、机制条款、自检命令、索引导向行;**FORK-NOTES.md 整体属规则本体**(分叉是现行状态声明,非历史),走共有文件逐字节一致路径。此词为铁律 8 新措辞与 sync-check 判定的精确锚点。

### CHANGELOG.md(skill 域 + design 域通用)

- **粒度**:每 skill 一份 `skills/<skill>/CHANGELOG.md`(仅项目侧);design 域每 feature 一份 `design/<feature>/CHANGELOG.md` + 裸放全局档共用 `design/CHANGELOG.md`(仅有可迁内容时建)。
- **条目格式**(追加式只增不改):
  ```
  ## YYYY-MM-DD <类型>:<一句话标题>
  - <内容:裁决/修订/教训,原注记信息逐字保留>
  - 影响: <文件>#<节标题>(反向指针,多目标逗号分隔)
  - 出处: <问卷/ADR/裁决链接>
  ```
- **类型枚举五类**:裁决 / 修订 / dogfood / 同步 / 升格。
- **反向指针语法 = 节标题锚点,禁行号**(行号随修订漂移;节标题锚点 GitHub 可跳转)。

### FORK-NOTES.md(双侧逐字节一致;条目级精简,压测 Q10-B)

```
# FORK-NOTES · <skill> 有意分叉声明
> 仅含有意分叉条目;完整设计决策见项目仓库 skills/<skill>/DESIGN.md。
- <日期> <分叉点>:<内容>〔出处〕
```

分叉变更时双侧同步更新(常规共有文件)。来源 = 现 DESIGN.md 的分叉声明节(action-Q 六条清单 / grill-Q / retro-Q)整体抽出 + **引擎文件头部的分叉/漂移条目**(压测 Q3-C:引擎文件头部拆分——一行副本标记「本文件是 design-Q 引擎复用件」为身份声明,留头部;分叉/漂移条目迁本文件)。**条目级精简:一行一条为纪律,不设数字上限**(压测 Q10-B 推翻 <10 行数字预期,靠纪律维持,不设可核验锚点)。

### DOGFOOD-LOG.md(全局侧私有,仅 doctor-harness,压测 Q2-C)

- 承载外部项目实操明细(**含真实项目名与路径**,OD-1 脱敏约束禁入公开仓库的内容);不进项目侧公开仓库。
- 非 CHANGELOG 名 → 不触发历史层类规则「仅项目侧存在」;**sync-check 白名单登记**(P0 脚本升级时一并)。
- 项目侧 doctor-harness/CHANGELOG 对应条目脱敏泛化(真实名 → 泛化描述)并注「实操明细见全局侧日志」——公开可追溯 + 私密保真双全。

### SKILL.md 索引行(统一头部,压测 Q8-C)

frontmatter 后首行统一:

```
> 治理历史见本目录 CHANGELOG.md;有意分叉见 FORK-NOTES.md
```

8 个 skill 迁移时统一落位;与 HARNESS-RULES「头部导览块」风格一致(导览前置)。

### STATUS-LOG.md(harness/ 根,仅项目侧)

- 承载仓库内部工作状态史(原 CLAUDE.md「仓库状态」节历史条目);格式与 CHANGELOG 条目同构(日期 + 标题 + 内容)。
- 根 CHANGELOG.md **保持纯对外语义不动**(记录规则原文「凡采用者可感知的变更必记,纯仓库内部治理不记」——内部史混入会稀释 F036 刚立的对外定位)。
- 落位依据 = HARNESS-RULES 第六节「治理文件归 harness/ 根」。

### DESIGN.md 收敛结构(仅项目侧)

三节 = 定位 / 设计决策(含被否决项)/ 已知限制;历史节全迁 CHANGELOG、分叉声明迁 FORK-NOTES。grill-with-docs 与 long-running-agent **维持无 DESIGN.md**(不新建,防形式主义)。

## 脚本契约

### sync-check.py 升级(类规则)

- `HISTORY_LAYER = {"CHANGELOG.md"}`(相对路径精确匹配,任意 skill);该类文件判定:
  - 仅项目侧存在 = **合法**(输出提示行「历史层,仅项目侧:正常」);
  - 仅全局侧存在 = 违规;
  - 双侧共有且内容不一致 = 违规(共有本身不禁止,但内容必须一致)。
- **EXCEPTIONS 清空**:doctor-harness/CHANGELOG.md 现例随 P4 迁移转入类规则;白名单机制保留给未来非历史层的裁决例外。

### harness-check.py 不改

三检查(问卷命名/ADR 编号/归档位置)与治理历史无交集;CHANGELOG.md 无 `L<N>-` 前缀,LN 命名正则天然不匹配,无需豁免代码——HARNESS-RULES 第九节注明「CHANGELOG.md 不受 LN 命名规则约束」。

## 存量→新载体映射规则(P1–P3 执行规格)

| 源 | 目标 | 规则 |
|---|---|---|
| SKILL.md 日期注记 | 同 skill `CHANGELOG.md` 条目 | 逐条迁;类型按内容判(裁决出处型 = 裁决,dogfood 叙述 = dogfood 等);原信息逐字保留 |
| DESIGN.md 历史节 | 同 skill `CHANGELOG.md` 条目 | 原节标题作条目标题,内容整节保留 |
| DESIGN.md 分叉声明 | 同 skill `FORK-NOTES.md` | 整节抽出,条目化 |
| DESIGN.md 其余(定位/决策/限制) | 原地保留 | 不动 |
| design/ 层文件内嵌历史 | `design/<feature>/CHANGELOG.md` | 同 CHANGELOG 条目格式;层文件本体留当前设计 + 一行索引 |
| 裸放全局档内嵌历史 | `design/CHANGELOG.md` | 共用一份(仅有可迁内容时建) |
| CLAUDE.md「仓库状态」节历史条目 | `harness/STATUS-LOG.md` | 逐条迁,原文保留;状态节改 ≤5 行快照 + 双指针(STATUS-LOG + 根 CHANGELOG) |
| 全局侧 doctor-harness/CHANGELOG 外部实证条目(真实名) | 规则性/演进性内容**脱敏泛化后**并入项目侧 doctor-harness/CHANGELOG;实操明细(真实名)→ 全局侧 `DOGFOOD-LOG.md`;项目侧条目注「实操明细见全局侧日志」 | 压测 Q2-C 双载体:公开可追溯 + 私密保真 + OD-1 脱敏约束不破;化解与 2026-08-18「外部实证条目留全局」裁决的冲突 |
| TODO.md 头部状态叙述 | 压缩为「当前状态一行 + STATUS-LOG 指针」;**活待办(如「下一步主线」)保留在 TODO**,纯历史叙述(建仓/已完成时间线)进 STATUS-LOG | 压测 Q9-C 顺手项(压缩不迁移):TODO 本职 = 追踪待办,排除的是历史不是状态;防三处双写漂移 |
| `history/` 版本子目录 | **维持原语义不动** | 整文件版本史 ≠ 条目式治理历史,两者并存不混 |

**迁移对照表** `migration-map_v1.md`:每行 = 源(文件#节)→ 目标(载体#条目)→ 内容摘要;L0 验收 2 的核对基准 + 人工抽检底册。

## 增量协议条款

- **触发时机五类 + 写入责任**:① skill 规格修订(SKILL.md/引擎文件)② 裁决产生(问卷处理落盘**同事件同时**)③ dogfood 轮次 ④ 双侧同步动作 ⑤ 教训升格——写入责任 = 处理该事件的 agent,与铁律 2「即时沉淀」同节奏(不批处理、不事后补)。
- **节标题改名的指针更新义务(压测 Q4-C)**:修订 SKILL.md/引擎文件的**节标题**时,同事件 grep 本 skill CHANGELOG 中指向该文件的「影响:」指针并同步更新锚点(改标题者是唯一知道新旧标题映射的时点;不建自动校验,三脚本不查锚点有效性)。
- **ADR-0023 升格衔接**:同类教训在 CHANGELOG 累计 ≥2 条 → 第 2 条写入时同步升格回 SKILL.md 规则本体(双侧同形保证同步),该条目标注「已升格」;SKILL.md 被升格处**不留日期注记**(升格即规则化)。
- **索引指针要求**:凡历史迁出处,原位置必留一行指针(L0 硬约束在此实例化)。

## 全局选型与被否决项

| 候选 | 裁决 | 被否决理由 |
|---|---|---|
| 发布管道(项目→全局生成产物) | 否,留 OD-10 终态候选 | 新建转换管道工程量最大;全局侧临时手改无处安放 |
| sync-check 白名单大扩展 | 否 | 8 skill × N 文件清单膨胀,每新增历史文件要改代码,例外失焦 |
| 全局侧 archive/ 子文件夹收 DESIGN.md | 否 | 需「仅全局侧存在」又一反向豁免类,复杂度上升;DESIGN 全文仍占全局 |
| 家族级一份 CHANGELOG | 否 | 集中检索但破坏 skill 自包含,条目跨 skill 横跳 |
| SKILL.md 压缩引用式注记 | 否 | 逐条短引用仍占行,编目工作量大 |
| 根 CHANGELOG 兼收内部状态史 | 否 | 记录规则明确排除内部治理;GitHub 侧栏展示混入内部史稀释对外定位 |

## 权威落位与部署运维

- **HARNESS-RULES.md 新增第九节「治理历史布局」**(五内容):① 载体命名与粒度(skill 域/feature 域/全局档/STATUS-LOG)② 历史层仅项目侧存在规则 + sync-check 类规则引用 ③ 索引指针要求 ④ 增量记录规则(触发五类)⑤ CHANGELOG.md 与 LN 命名规则的关系注记;doctor-harness/CHANGELOG.md 现例规则本体迁此节;修订走其自身 CHANGELOG 留痕。
- **doctor-harness SKILL.md 职责补条**:治理历史载体的维护/迁移触发/增量记录规则。
- **铁律 8 措辞更新**(项目 CLAUDE.md):「skill 双侧同步」语义改为——**规则本体(SKILL.md/引擎文件/FORK-NOTES)双侧逐字节一致;历史层(CHANGELOG)仅项目侧存在**;提交前例行照跑(升级后语义);doctor-harness/CHANGELOG.md 白名单例外条目从注记移除。
- **CLAUDE.md 联动**:「仓库状态」节 = 快照(≤5 行)+ 双指针;「落盘路径速查」表 doctor-harness 行补「治理历史载体(CHANGELOG/STATUS-LOG 维护)」。
- **部署例行**:提交前三脚本(脱敏 + harness-check + skills-sync-check)照常;sync-check 以升级后语义判定。**根 CHANGELOG 记录义务(压测 Q6-C)**:P4 完成后,本 feature 变更按根 CHANGELOG 记录规则(采用者可感知)写入**一条**(全局侧装法变化 / SKILL.md 形态 / FORK-NOTES / STATUS-LOG / DOGFOOD-LOG 新载体),与既有「skill 演进」条目格式一致——契约显式化,防跨会话执行遗漏。

## ADR 识别

- **立 ADR-0024「治理历史分离与双侧常态性形态分工」**(三条件全中:跨 8 skill × 双侧 + doctor-harness 机制 / 长期治理契约——改变铁律 8 语义、推翻 ADR-0023 缓行评估、全局侧文件删除 / OD-10·OD-24 挂靠重访);随 L1 定稿落 `harness/adr/0024-*.md`。
- **ADR-0023 补「后续演进」注记**:2026-08-19「全量迁移低收益缓行」评估被 2026-08-20 本 feature 立项推翻(Q1-C 裁决),出处本 feature 问卷。
- **OD 联动三条**:OD-10(全局侧提前达成分发洁净目标态,重访触发①语义更新)/ OD-24(「有意分叉」从实验期临时态升为常态分工,补注)/ OD-8(分叉声明落点从 DESIGN.md 改为 FORK-NOTES + CHANGELOG,漂移记录双侧可见,补注)。
