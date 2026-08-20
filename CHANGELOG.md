# 更新日志(CHANGELOG)

> 仓库级对外变更的唯一记录(自 README「发布说明」节迁入,2026-08-20)。

> **记录规则**:本节是仓库级对外变更的唯一记录——凡**采用者可感知**的变更(skill 行为 / 产物结构 / 方法论内容)必记,纯仓库内部治理(问卷归档、链接修复等)不记。倒序排列。skill 无独立版本号,这里是感知 `skills/` 变更的唯一窗口。

## skill 演进(2026-08-20,治理历史分离 + 双侧形态分工,ADR-0024)

- **每个 skill 新增 `CHANGELOG.md`(治理历史,仅本仓库持有)**:SKILL.md 内带日期的裁决出处注记全部迁出,SKILL.md 只留规则现值 + 头部一行索引导向——**SKILL.md 常驻上下文密度提升**(第一支柱落到仓库自身形态);三份问卷 skill 另增 `FORK-NOTES.md`(有意分叉声明,双侧一致)。设计决策仍见各 `DESIGN.md`(收敛为纯决策表)。
- **双侧常态性形态分工(装法变化)**:`~/.claude/skills/`(用户全局)转为**分发洁净形态**——只含 SKILL.md + 引擎/模板文件 + FORK-NOTES,不再含 DESIGN.md / CHANGELOG.md(开箱即用,无演进噪音);本仓库 `skills/` = 车间完整形态。已装用户:全局侧 DESIGN.md/CHANGELOG.md 已随升级移除,历史全部保留在本仓库(信息零丢失,doctor-harness 外部实操明细在全局侧 `DOGFOOD-LOG.md` 私有持有)。
- **配套机制**:`skills-sync-check.py` 升级类规则(历史层文件仅项目侧存在 = 合法;DESIGN/CHANGELOG 属历史层);项目 CLAUDE.md 铁律 8 语义随之更新;`harness/STATUS-LOG.md` 新建承接仓库内部状态史(CLAUDE.md 状态节瘦身为 3 行快照)。

## README 重构 + 发布说明外移(2026-08-20)

- **README 升级为对外第一印象形态**:「8 个核心 skill」由一句话表格升级为卡片式(每 skill:定位 / 触发 / 产物 / 核心维度或机制);新增「各 skill 提问/确认维度速查」表(权威 = CONTEXT「提问维度速查」节,README 为导览副本);最小采用切片升格独立小标题;章节顺序重组 + 轻量 badge。
- **发布说明外移至本文件**:README「发布说明」节全部历史条目迁至仓库根 CHANGELOG.md(GitHub 自动识别);README 原位置只留链接一行。记录规则照旧。
- **伴随漂移修复**:实操 §8.3 三处 grill 退役残留 + CONTEXT 速查表节头同步指针(F035)。

## skill 演进(2026-08-19,grill 家族治理日:退役 + 形态修订 + 边界机制)

- **grill 退役,家族 9 → 8**:`/grill` 移除(归 `waste/skills/grill/`,可回退);其「通用 × 单点深钻」生态位由 grill-with-docs 新增的**通用模式**承接(不绑库 + 零留痕;入口确认 + 中途切回双兜底)。已装 grill 的采用者:卸装,通用问题直接用 grill-with-docs。
- **轻量模式(action-Q / grill-Q / design-Q)**:轻任务时 AI 提议、人拍板走精简管道(调研分级 / 小波直问 / 免归档),「初步结论先行 + 人工轻验证」;不假设 / 先验证铁律不因轻量豁免。
- **grill-Q 防跑偏机制**:入口校准闸门(出题前向人确认「工件理解摘要 + 关键声明清单 + 压测焦点」)+ 每题 ❌ 跑偏标注(同波 ≥2 题被标 → 停波回炉校准框架)+ 阻塞性逃生舱可转 grill-with-docs 单点深钻 + 处理报告质量信号节。
- **SKILL.md 分层原则确立**([ADR-0023](harness/adr/0023-skill-md-layered-slimming.md)):规则留 SKILL、教训移 DESIGN,同一错误重复 ≥2 次才升格常驻;渐进执行。
- **canonical 版本内修订**(不升版):哲学 §3.1 路由表加「认知状态」行(两族分流判据锚);方法论 §4.1/§4.3 接线(认知状态三态 + 判据冲突优先级 + 存疑从重)。经 grill-boundary-canonical-w01 复压(9 题,[归档问卷](harness/questionnaires/archive/_misc/grill-boundary-canonical-w01.md))。

## skill 演进(2026-08-19,双侧同步机制化)

- **skill 双侧同步检查上线**:新增 [scripts/skills-sync-check.py](scripts/skills-sync-check.py)——改 `skills/`(本仓库)或 `~/.claude/skills/`(用户全局)任一侧后,提交前跑检查,**0 违规才提交**;脚本 check-only 不选边,哪侧为准是语义判断、永远由人定(裁决例外白名单内置)。背景:2026-08-18 双向合并(9 skill 核对 + 8/14 修订回灌)暴露「项目内修、全局漏修」空隙,机制化收口。

## skill 演进(2026-08-16/17,design-Q 层级制 LN 改造)

- **design-Q 产物结构升 LN 制**:VISION/HLD/LLD 三件套 → **LN 分层设计**——L0-vision(目标层)恒在,L1+/L2 按需动态增层,旧三件套降为别名兼容;骨架增强(HLD/LLD 判别法则 + 反简化最小必含 + 坍缩分档)保留,见 [ADR-0022](harness/adr/0022-design-questionnaire-digital-levels.md)。
- **doctor-harness 承接层级治理**:HARNESS-RULES 新增第七节(LN 布局/导览/存量豁免)与第八节(存量结构改造流程 + 旧档迁移映射表);本仓库存量设计套(repo/ 三件)git mv 迁 LN 化演练完成。
- **全链闭环**:F027–F034 全绿(端到端测试通过);DOGFOOD 案例 1 用户实测确认;首份 retro 文档产出(retro-questionnaire 首跑)。

## methodology_v5(2026-08-14,方法论章节连续化与契约优先)

- **方法论文件升 v5**:正文连续编号 §零至§九(v4 映射表在文件顶部)+ 全库引用审查;§4.3(旧 §5.3)两族表补 action-Q 入族;§5.3(旧 §7.3)补「时序纪律」——契约层变更必须**先更新 canonical 设计、再继续不可逆动作**(ADR-0021 通用化)。
- **伴随项**:CONTEXT 补规范导航与「暂定」状态词;同轮立项 design-Q 数字层级改造、dogfood 定义消歧、方法论 704 行审计(见 [TODO.md](TODO.md))。
- **版本处置**:v4 保留在 [`docs/methodology/archive/`](docs/methodology/archive/) 作为历史母本。

## v7(2026-08-14,哲学独立文章与双文件治理)

- **哲学文件升 v7**:正文统一为连续章节 §一至§五,增加独立阅读入口,保留 v3 旧章节映射、兼容别名 / 重定向说明与历史问卷/ADR 回溯;补方法论 harness 与运行时 harness 的术语边界。
- **治理边界诚实化**:补 current 已知缺口状态、前三学科最小进入/退出模板,并将返工与去黑盒代理指标明确为反思提示而非效果验证或自动验收门。
- **版本处置**:v6 保留在 [`docs/methodology/archive/`](docs/methodology/archive/) 作为历史母本,v7 成为 current canonical;哲学与 methodology(同日升 v5)按 [ADR-0018](harness/adr/0018-canonical-dual-challenge-governance.md) 作为对等 canonical 双文件交叉治理。

## v6(2026-08-13,哲学治理进化)

- **哲学文件升 v6**:在 v5 的安全科学第四学科视角与「去 AI 黑盒」基础上,补全文阅读路线与章节过渡;§8.6 明确为「方法论自身的治理闭环」,加入统一主张状态模板与学科治理路线图。
- **治理进化路径**:将系统/需求工程、认识论与测量科学、配置管理/QMS、认知科学/HCI、知识管理/组织学习、信息安全/威胁建模、形式化方法、控制论/决策理论映射到治理机制、最小产物与进入条件;不把它们变成个人项目的强制流程。
- **版本处置**:v5 保留在 [`docs/methodology/archive/`](docs/methodology/archive/) 作为历史母本,v6 曾成为 current canonical,现由 v7 接替并一并归档。

## v5(2026-08-11,philosophy 立论重构)

- **哲学文件升 v5**:新增 **§八 安全科学视角:去 AI 黑盒**(第四学科视角;黑盒三层次定义 + 与第一支柱正交 + 三风险 + 统合已有可审计装置对策 + 弹性边界 WAI/WAD);顶部学科挂接扩为四(人因 / 软工 / 运筹 / 安全科学);元原则失败模式表加「黑盒信任劫持」。v4 归 archive。
- **学科挂接分层**([ADR-0014](harness/adr/0014-discipline-mapping-strategy.md)):哲学正文只挂「立论核心学科」,CONTEXT「项目学科地图」承载全景(系统工程 / CM / QMS / PM / KM / 认知科学 + 安全 / 可靠性 / 韧性术语三分)。
- **完整 write→review→implement 闭环**:grill-Q philosophy-v4(W01/W02,18 处修订)→ discipline-mapping → grill-with-docs(去黑盒 6 点结晶)→ design-Q(VISION/HLD/LLD + [ADR-0015](harness/adr/0015-deblackbox-anchor.md))→ 设计套压测(10 项修订)→ long-running 起草(commit 530d0f4)。

## skill 演进(2026-08-08,doctor-harness 第 9 个 skill)

- **harness 演进治理 skill 上线**:组织 harness 区(分层 / 迁移 / 校验 / 留痕),规则权威 [HARNESS-RULES.md](skills/doctor-harness/HARNESS-RULES.md)(ADR-0012/0013);校验脚本 [scripts/harness-check.py](scripts/harness-check.py)(命名正则 / ADR 编号连续 / 归档位置三检查)。
- **归档子目录化**:41 份归档问卷按 feature/主题迁入 `harness/questionnaires/archive/` 下 10 个子目录,附 [README 索引](harness/questionnaires/archive/README.md)。
- **格式反馈落地**:问卷单波次上限 10、小波(直接问答)阈值 3,四副本(design-Q / grill-Q / retro-Q / action-Q)统一;新增 [MIGRATION-FLOW](skills/doctor-harness/MIGRATION-FLOW.md) 迁移流程文档。

## skill 演进(2026-08-07,design-Q 规格整理)

- **落盘路径回归硬编码 `harness/`**(2026-08-07 撤销方案 R,看 [ADR-0011](harness/adr/0011-abandon-plan-r-hardcode-harness.md)):design-Q + grill-Q/retro-Q/action-Q + long-running 的问卷/ADR 落盘路径**一律硬编码 `项目根/harness/`**(design/ + questionnaires/ + adr/);CONTEXT/OPEN-DECISIONS/TODO 为项目固有文件,路径不动。
- **design-Q 骨架增强**:HLD/LLD 判别法则(phase-invariant vs incremental + 两句判别问句)+ 反简化最小必含(H1–H5/L1–L5 共 10 项,约束内容非仅结构)+ 坍缩分档。仅 design-Q 骨架,不扩散到 grill/retro/action。

## v4(2026-08-05)

- **方法论 + 哲学升 v4**:受众收窄为**个人开发者**;第二支柱补机制层立论(「无护栏 → AI 产出悄悄劣化」);哲学文件学科化(人因工程 / 软件工程 / 运筹学三视角)。
- **术语版本注**:8 术语**全保留**(未换词),新增学科参照注记 + 新词引入三条件门槛(见 [CONTEXT 术语治理节](docs/CONTEXT.md));旧版 skill 副本无需术语迁移,但落盘路径(harness/)与规范优先级以本仓库为准。
- **仓库结构**:harness/(设计文档 + 归档问卷)与 docs/(项目文件)物理分离;新增 AGENTS.md(Codex 入口路由)。
- **规范优先级**:方法论主张(canonical)> ADR > CONTEXT 术语 > skill 规格 > 实操(见 [CLAUDE.md](CLAUDE.md));v3 保留作历史母本。

