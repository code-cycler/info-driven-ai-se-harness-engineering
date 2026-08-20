---
mode: feature
wave: 0
stage: L1-contract
created: 2026-08-20
status: archived
---
# 问卷 feature-governance-history-split L1-contract W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的决策点逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(2026-08-03 起,默认关):仅当你启动本 skill 时明确说「预勾选」,要点才预勾 `[x]`(勾 = 采纳默认);未启用时全部 `[ ]`,人逐条作答
> - **取消勾选(留空)= 不采纳** → 该要点转入 W01 单独拷问(出选项深究)
> - **单向门要点(发布 / 删除 / 花钱 / 脱敏等不可逆)永不预勾**,强制人逐条显式勾选确认
> - 本波**不用 🤔**(yes/no 二选一,无中间态);真定不了 → 取消勾选即可,转 W01 深究
> - 若"大体同意但要改一两处" → 取消勾选,转 W01 时在深究题里给自定义值
>
> 默认来源标注于〔〕。

> **出题依据摘要**(2026-08-20,事实已核实):
>
> - 根 CHANGELOG.md(72 行)记录规则原文 = 「凡**采用者可感知**的变更必记,**纯仓库内部治理(问卷归档、链接修复等)不记**」——纯对外发布说明语义(F036 刚立,GitHub 侧栏展示),与 CLAUDE.md 状态节的内部工作状态史**不兼容**;W00-12「职责重叠、不新造载体」前提有误,CLAUDE.md 域落点在本层重裁决(要点 10)
> - doctor-harness/CHANGELOG.md 现役格式 = `## 日期 标题` + 变更 + 原因,追加式只增不改——skill 域条目格式的直接先例
> - sync-check.py EXCEPTIONS 机制已读原文(类规则可实现性无障碍);harness-check 三检查(问卷命名/ADR 编号/归档位置)与治理历史无交集
> - DESIGN.md 分叉声明现状:action-Q(6 条有意分叉清单)/ grill-Q(有意分叉声明)/ retro-Q(副本声明)等,均为可整体抽出的独立节
> - grill-with-docs 与 long-running-agent 无 DESIGN.md;skills/ 下无 FORK-NOTES/HISTORY 类文件(命名无冲突)

## 决策默认值清单

### 一、载体契约

- [X]  **1 CHANGELOG 粒度 = 每 skill 一份**:`skills/<skill>/CHANGELOG.md`,仅项目侧存在;skill 自包含(迁移/检索/升格判定都在 skill 目录内完成);被否决 = 家族级一份 `skills/CHANGELOG.md`(集中检索但破坏 skill 自包含,条目跨 skill 横跳)〔doctor-harness 现役先例 + W01-Q2/Q3 裁决链〕
- [X]  **2 CHANGELOG 条目格式**(追加式只增不改,继承 doctor-harness 先例并扩展):
  ```
  ## YYYY-MM-DD <类型>:<一句话标题>
  - <内容:裁决/修订/教训,原注记信息逐字保留>
  - 影响: <文件>#<节标题>(反向指针,多目标逗号分隔)
  - 出处: <问卷/ADR/裁决链接>
  ```

  类型枚举 = **裁决 / 修订 / dogfood / 同步 / 升格**五类〔doctor-harness CHANGELOG 格式 + L0 验收 6「≤2 跳」的反向指针要求〕
- [X]  **3 反向指针语法 = 节标题锚点,禁行号**:`影响: SKILL.md#主流程` 形态(行号随修订漂移不可用;节标题锚点 GitHub 可跳转)〔ADR-0023 索引行语义 + Markdown 锚点稳定性〕
- [X]  **4 FORK-NOTES.md 模板**(双侧逐字节一致,<10 行量级):
  ```
  # FORK-NOTES · <skill> 有意分叉声明
  > 仅含有意分叉条目;完整设计决策见项目仓库 skills/<skill>/DESIGN.md。
  - <日期> <分叉点>:<内容>〔出处〕
  ```

  分叉变更时双侧同步更新(常规共有文件,sync-check 零新语义)〔W01 小波澄清裁决〕
- [X]  **5 DESIGN.md 收敛结构**(仅项目侧):三节 = 定位 / 设计决策(含被否决项)/ 已知限制;历史节全迁 CHANGELOG、分叉声明迁 FORK-NOTES;**grill-with-docs 与 long-running 维持无 DESIGN.md**(其历史从 SKILL.md 迁 CHANGELOG 后不新建,防为收敛而新建的形式主义)〔W00-10 + subagent 量化事实〕

### 二、脚本契约

- [X]  **6 sync-check 类规则实现**:`HISTORY_LAYER = {"CHANGELOG.md"}`(相对路径精确匹配);该类文件——仅项目侧存在 = 合法(输出提示行「历史层,仅项目侧:正常」)、仅全局侧存在 = 违规、双侧共有且内容不一致 = 违规;**EXCEPTIONS 清空**(doctor-harness/CHANGELOG.md 现例随 P4 迁移转入类规则,白名单机制保留给未来非历史层的裁决例外)〔W01-Q3-C + sync-check.py 原文核实〕
- [X]  **7 harness-check 不改**:其三检查(问卷命名/ADR 编号/归档位置)与治理历史无交集;CHANGELOG.md 无 `L<N>-` 前缀,LN 命名正则天然不匹配,无需豁免代码——仅在 HARNESS-RULES 新节注明「CHANGELOG.md 不受 LN 命名规则约束」〔harness-check.py 职责核实〕

### 三、存量→新载体映射规则

- [X]  **8 skill 域映射**:SKILL.md 日期注记逐条 → CHANGELOG 条目(类型按内容判:裁决出处型 = 裁决,dogfood 叙述 = dogfood 等);DESIGN.md 历史节 → CHANGELOG(原节标题作条目标题,内容整节保留);DESIGN.md 分叉声明 → FORK-NOTES;DESIGN.md 其余三节保留〔W01-Q1-C + L0 画像〕
- [X]  **9 harness/design/ 域载体**:`design/<feature>/CHANGELOG.md`(feature 目录内,与 skill 域命名统一);裸放全局档(hld_v2 / lld_v2 / VISION.md 等)内嵌历史 → `design/CHANGELOG.md`(全局档共用一份,**仅在有可迁内容时建**,纯空载体不预建);`history/` 版本子目录机制维持原语义不动(整文件版本史 ≠ 条目式治理历史,两者并存不混)〔W00-11 + HARNESS-RULES 第一节/第七节〕
- [X]  **10 CLAUDE.md 域落点重裁决(W00-12 前提修正)**:内部状态史迁 **`harness/STATUS-LOG.md`(新载体)**,不迁根 CHANGELOG——理由:根 CHANGELOG 记录规则明确排除内部治理(F036 刚立的对外纯净语义,GitHub 侧栏展示,混入内部史稀释其定位);STATUS-LOG 按 HARNESS-RULES 第六节「治理文件归 harness/ 根」落位,格式与 CHANGELOG 条目同构;「不新造载体」原则基于错误前提(以为根 CHANGELOG 兼容),修正后新载体是必要成本〔根 CHANGELOG.md 记录规则原文核实 + HARNESS-RULES 第六节〕
- [X]  **11 迁移对照表**:`harness/design/governance-history-split/migration-map_v1.md`;每行 = 源(文件#节)→ 目标(载体#条目)→ 内容摘要;作为 L0 验收 2「逐字可查」的核对基准 + 迁移后人工抽检底册〔L0 验收 2 + 风险①防护〕

### 四、增量协议条款

- [X]  **12 增量触发时机五类 + 写入责任**:① skill 规格修订(SKILL.md/引擎文件)② 裁决产生(问卷处理落盘**同事件同时**)③ dogfood 轮次 ④ 双侧同步动作 ⑤ 教训升格;写入责任 = 处理该事件的 agent,与铁律 2「即时沉淀」同节奏(不批处理、不事后补)〔W00-9 + 铁律 2〕
- [X]  **13 ADR-0023 升格衔接**:同类教训在 CHANGELOG 累计 ≥2 条 → 第 2 条写入时同步升格回 SKILL.md 规则本体(双侧同形保证同步),该 CHANGELOG 条目标注「已升格」;SKILL.md 被升格处不留日期注记(升格即规则化)〔ADR-0023 决策 2 + W01-Q1-C〕

### 五、权威落位

- [X]  **14 HARNESS-RULES 新增第九节「治理历史布局」**:五内容——① 载体命名与粒度(skill 域/feature 域/全局档/STATUS-LOG)② 历史层仅项目侧存在规则 + sync-check 类规则引用 ③ 索引指针要求(迁出处必留一行)④ 增量记录规则(触发五类)⑤ CHANGELOG.md 与 LN 命名规则的关系注记;doctor-harness/CHANGELOG.md 现例的规则本体迁此节;修订走其自身 CHANGELOG 留痕〔W00-17 + HARNESS-RULES 头部权威声明〕
- [X]  **15 铁律 8 措辞更新**(项目 CLAUDE.md):「skill 双侧同步」语义改为——**规则本体(SKILL.md/引擎文件/FORK-NOTES)双侧逐字节一致;历史层(CHANGELOG)仅项目侧存在**;提交前例行照跑(升级后语义的脚本);doctor-harness/CHANGELOG.md 白名单例外条目从铁律 8 注记中移除〔W01-Q2/Q3 裁决 + CLAUDE.md 铁律 8 现文〕
- [X]  **16 CLAUDE.md 联动改造**:「仓库状态」节 = 当前快照(≤5 行)+ 双指针(STATUS-LOG + 根 CHANGELOG);「落盘路径速查」表 doctor-harness 行补「治理历史载体(CHANGELOG/STATUS-LOG 维护)」〔L0 画像 CLAUDE.md 域 + W00-13〕

### 六、模块边界(新增/修改/删除清单 = P0–P4 执行输入)

- [X]  **17 文件变更清单**:**新增** = 8× `skills/<skill>/CHANGELOG.md`(项目侧)+ N× `FORK-NOTES.md`(存在分叉的 skill:action-Q/grill-Q/retro-Q 至少三份,P1 盘点定全量)+ `design/<feature>/CHANGELOG.md` 若干 + `design/CHANGELOG.md`(有可迁内容时)+ `harness/STATUS-LOG.md` + `migration-map_v1.md`;**修改** = 8× SKILL.md(双侧同形)+ 6× DESIGN.md(项目侧收敛)+ sync-check.py + HARNESS-RULES.md + doctor-harness/SKILL.md + 项目 CLAUDE.md;**删除(= git mv 归档,不真删)** = 全局侧 6× DESIGN.md + 全局侧 doctor-harness/CHANGELOG.md(P4 重整时)〔subagent 文件清单 + Q4-B〕
- [X]  **18 选型被否决项汇总表**(≥1 为 L1 最小必含):发布管道(Q3-B,留 OD-10 终态候选)/ 白名单大扩展(Q3-A)/ archive 子文件夹(Q2 小波 B)/ 家族级 CHANGELOG / 压缩引用式(Q1-B)/ 根 CHANGELOG 兼收内部史(要点 10)——六项各附一句被否决理由,进 L1 文档选型表〔L0/L1 裁决链汇总〕

### 七、ADR 识别

- [X]  **19 立 ADR-0024「治理历史分离与双侧常态性形态分工」**:三条件核对——① 跨 skill 影响(8 skill × 双侧 + doctor-harness 机制)✓ ② 长期治理契约(改变铁律 8 语义、推翻 ADR-0023 缓行评估、全局侧文件删除)✓ ③ 未来重访挂钩(OD-10/OD-24)✓;ADR-0023 补「后续演进」注记(2026-08-19 缓行评估被 2026-08-20 立项推翻,出处本 feature 问卷)〔ADR 三条件 + ADR-0023 原文〕
- [X]  **20 OD 联动三条**:OD-10(分发洁净——全局侧提前达成目标态,重访触发①「dogfood 收尾」语义更新)/ OD-24(双副本策略——「有意分叉」从实验期临时态升为常态分工,补注)/ OD-8(引擎漂移——分叉声明抽 FORK-NOTES 后双侧可见,漂移记录落点从 DESIGN.md 改为 FORK-NOTES + CHANGELOG,补注)〔对应 OD 原文 + W01-Q2 裁决〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-20,L1 W00 处理)

**作答解析**:20/20 答毕,无异常;**全采纳 20/20**(零留空、零自定义);补充声明空。W00 无 🤔 逃生舱。

**preview 统计**:勾选采纳 20 · 取消勾选 0 · 转 W01 正式题 0。opt-in 预勾未启用,取消默认率不适用。

**层内盘问点判断**:L1 骨架最小必含全覆盖——① 模块/边界(要点 17)② 接口契约(要点 1–13:载体格式/锚点语法/脚本契约/映射规则/增量条款)③ 全局选型 + 被否决项(要点 18,六项表)④ 部署运维(要点 15 提交例行 + 要点 6/7 脚本契约)⑤ ADR 识别(要点 19/20)⑥ 导览块契约项声明(随 L1 文档落盘);动态盲点 = 0(补充声明空);逃生舱项 = 0。→ **无 W01 必要,直接层闸门**。

**落盘文件**:① [L1-contract-gov-history-split.md](../../design/governance-history-split/L1-contract-gov-history-split.md)(本层成稿);② L0 文档 W00-12 落点句同步修正(STATUS-LOG,版本内修订一行)。

**未验证假设台账**:无新增(根 CHANGELOG 记录规则/sync-check 机制/harness-check 职责均核实原文后出题)。

**状态**:pending → answered → processed(2026-08-20)→ archived(同日,目录 governance-history-split/)。
