# L2-build-proj-overview-phases-dod.md · human-project-view feature

> 导览：① 位置与职责 = **构建层**（分几步建 / 每步做什么 / 何时算完）② 覆盖 = P0 skill 编写、P1 首次生成 dogfood、P2 全仓联动同步三阶段的详细设计、DoD 与依赖预估 ③ 上下游 = 受 [L1-contract](L1-contract-proj-overview.md) 全部硬约束（接口契约 / 选型 / 图规格 / HARNESS-RULES 类目 / 联动清单）；继承 [L0-vision](L0-vision-human-project-view.md) 验收 ④ **契约项声明（验收硬约束）**：本文「每阶段 DoD」为验收硬约束，DoD 通过才算阶段完成（long-running 反推 feature_list 的 passes 判据源）。
> 状态：L2 W00 已处理（13/13 全采纳，无转正式题）；2026-09-23。

## 阶段拆分

| 阶段 | 内容 | 可独立交付物 | 依赖 |
|---|---|---|---|
| **P0 skill 编写** | `skills/proj-overview/` 三文件 + 全局侧同步 | SKILL.md（<100 行）+ DESIGN.md + CHANGELOG.md；sync-check 0 违规 | 无 |
| **P1 首次生成 dogfood** | 以本仓库为对象执行 skill 生成首份视图 + 一次性规格自检 + 失忆测试预约 | `harness/PROJECT-OVERVIEW.md` + 自检证据 + TODO 核验项 | P0（验证规格可执行） |
| **P2 全仓联动同步** | 九处联动 + HARNESS-RULES 新类目 + en 镜像 + 四门终验 | 联动完成 + 四门全绿 + 根 CHANGELOG 条目 | P1 产物定稿（防规格返工连带改两遍） |

依赖链线性：P0 → P1 → P2。每阶段一 commit（约定式）：`feat(skill): proj-overview 入库（P0）` / `feat(harness): 首份 PROJECT-OVERVIEW 生成（P1）` / `docs: 全仓联动同步至 9 skill（P2）`。

## 详细设计（按阶段）

### P0 · skill 编写

- **SKILL.md 行数预算（总计 < 100 行硬约束）**：frontmatter + 定位与边界 ~15 / 主流程四步（扫描 → 抽取 → 组织 → 渲染，每步 3–5 行要点）~30 / 输出规格摘要（五段结构 + 图规格参数表，参数以 L1 契约为准）~25 / 人因四原则 + 文风规范（禁令 + 术语表全量成文）~20 / 触发词与自检 ~10。
- **信息源分级读取三档（grill W01 Q5，写进主流程「扫描」步）**：结构类全读 / 治理类头读（ADR 标题行、OD 条目头）/ 关键 N 份选读——防重生成演变为全仓深读（隐性成本与设计取向直接冲突）。
- **文风术语表（20 词，P0 一次成文）**：模块 / 接口 / 依赖 / 基线 / 追溯性 / 验证 / 配置项 / 职责 / 边界 / 约束 / 入口 / 流转 / 状态 / 快照 / 层级 / 覆盖 / 偏差 / 裁决 / 触发 / 交付——各行业系统工程通用交集，不引用单一标准。
- **DESIGN.md（30–50 行）**：设计套链接 + L0/L1 关键裁决摘要（选型表指针）。
- **全局侧同步**：分发洁净形态（仅 SKILL.md），提交前 skills-sync-check 0 违规。

### P1 · 首次生成 dogfood

- 执行 SKILL.md 四步，信息源 = 本仓库实例清单（生成时实例化进产物「信息源指纹」）。
- **BFS 分层 = 生成期判断，不预设死**：候选视角（理念层 → 流程层 → 执行层 → 治理产物层，或三区空间切）由生成时信息实况判断，分层依据以注记记录在产物「结构全景」段。
- **DFS 关键功能按 L1 判据生成时反推**（TODO 主线 + 验收锚点）；候选预填 = 推进受挫谱系修复包 / governance-history-split（P4 未完）/ human-project-view 自身（grill W01 Q10 替换已收官的 i18n，对齐「当前主线/高风险」判据），以生成时 TODO 实况为准。
- **失忆测试预约**：P1 完成时在 TODO 建核验项「隔 ≥3 天执行失忆测试回填」（预写失败路径：两轮迭代内通过，否则降级定位并记 OD——grill W01 Q3），结果回写 skills/proj-overview/DESIGN.md「dogfood 修订」节（仅项目侧）。
- **dogfood 留痕双载体**：项目侧 DESIGN.md 节 + 全局侧 DOGFOOD-LOG.md 记一行（skill 首次 dogfood 事件）。

### P2 · 全仓联动同步（内部顺序：治理规则先行 → 活文档 → 镜像 → 终验）

1. HARNESS-RULES §六新类目「PROJECT-OVERVIEW.md（人读派生视图）」+ 特性声明四条 + doctor-harness CHANGELOG 留痕——规则先行：产物类目合法化后，后续文档引用才不自相矛盾。
2. README（卡片 + 协作图 + 「8 个」→「9 个」三处）→ 项目 CLAUDE.md（协作图 + 速查表 + 家族节）→ CONTEXT（家族节 + 术语对照 proj-overview 译名，agent 起草人确认）→ 方法论 §3.3.1 路由表加行（canonical 版本内修订，grill 退役先例）。
3. TRANSLATABLE 登记 + `en/skills/proj-overview/SKILL.md` 首译（同批交付不留欠账）。
4. 根 CHANGELOG 记一条（对外可感知：新 skill 入库）。
5. 四门终验（见 DoD）。

## 接口规格（P0 交付物 = SKILL.md 内容规格）

- frontmatter：`name: proj-overview`；description 含触发词（项目地图 / 项目全景 / 掌握恢复 / 重新定向 / 我迷失了 / 重新生成项目视图）。
- 首行治理索引指针（HARNESS-RULES:143 格式）：治理历史见 CHANGELOG（仅项目侧）；无 FORK-NOTES = 无规则本体级分叉。
- 五节结构与行数预算见「详细设计 P0」；输出规格参数表与处理契约全文以 L1「接口契约」节为准（SKILL.md 摘要 + 参数，不复制 L1 全文——<100 行约束下摘要即契约的执行视图）。

## 每阶段 DoD（脚本化优先 + 回归验证）

### P0 DoD

- [ ] `wc -l skills/proj-overview/SKILL.md` < 100
- [ ] 五节标题结构 grep 齐（定位边界 / 主流程 / 输出规格 / 人因与文风 / 触发自检）
- [ ] 术语表 20 词 grep 齐；触发词在 description
- [ ] skills-sync-check 0 违规（**回归：全仓跑，不影响既有 8 skill**）
- [ ] CHANGELOG.md / DESIGN.md 存在且非空

### P1 DoD

- [ ] `wc -l harness/PROJECT-OVERVIEW.md` ≤ 250
- [ ] 五段标题 grep 齐；文件头三件套 grep 齐（时间戳 / 源清单 / 派生声明）
- [ ] mermaid 图块计数 **≤ 12**（上限约束；BFS 总图 1 + DFS 子图若干）且 ≥ 2（BFS + DFS 各至少 1）
- [ ] 单图节点粗检 ≤ 30（生成时自数）
- [ ] 逐图渲染验证：各 mermaid 块嵌入临时 HTML（mermaid CDN 链路，2026-09-22 实测同法）浏览器验证渲染成功，验证后删临时文件（grill W01 Q4）
- [ ] TODO 失忆测试核验项已建（格式：问题 → 行动 → 核验时机）
- [ ] **回归：harness-check 无新增告警**（产物落 harness/ 根不破坏既有布局；既存告警如 LN 正则待修项标注豁免）
- [ ] 自检证据（命令 + 输出）记入 P1 commit message 或 DESIGN.md——一次性命令，不立常驻脚本

### P2 DoD

- [ ] HARNESS-RULES §六新类目 grep 命中 + doctor-harness CHANGELOG 留痕
- [ ] 全仓 grep「8 个核心 skill」0 命中（README/CLAUDE/CONTEXT 三处 + 协作图节点 = 9）
- [ ] 方法论 §3.3.1 路由表含 proj-overview 行（canonical 版本内修订）
- [ ] TRANSLATABLE 含 `skills/proj-overview/SKILL.md`；en 镜像文件存在且头三字段合规
- [ ] 方法论 §3.3.1 修订同步文件头「修订记录行」（版本内修订惯例，grill W01 Q9）
- [ ] 全局侧 DOGFOOD-LOG 写入内容先在对话出示、人过目后写入（`~/.claude/skills/` 无版本控制，铁律 8 精神，grill W01 Q9）
- [ ] **四门全绿**：desensitize 0 命中 / skills-sync-check 0 违规 / i18n-check 0 违规 / harness-check 0 **新增**告警（既存项区分标注）
- [ ] 根 CHANGELOG 新条目存在
- [ ] **回归：既有 skill 行为不变**（联动仅表述同步，无规则本体变更）

## 依赖与预估

- **实现路径 = long-running 单线程串行**：从本层反推 feature_list 三项（P0/P1/P2），端到端 DoD 通过才 passes:true。
- 预估（经验值非承诺）：P0 半会话 / P1 半会话（生成 + 自检）/ 失忆测试 +3 天异步等待窗 / P2 一个会话；总计约 2 个工作会话 + 3 天等待。
- 外部依赖无阻塞：mermaid 多环境渲染链路已实测（2026-09-22，HTML+CDN 通过、GitHub/VSCode 原生路径已知）。
- 跨会话状态载体：`.claude/feature_list.json`（三项）+ `.claude/claude-progress.txt`。
