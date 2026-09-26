# STATUS-LOG · 仓库内部工作状态史

> 承接原 CLAUDE.md「仓库状态」节的历史条目(ADR-0024 P3 迁移,2026-08-20,原文逐字保留)。**只记内部工作状态时间线**;对外可感知变更见仓库根 [CHANGELOG.md](../CHANGELOG.md)(其记录规则明确排除内部治理);当前状态快照见 [CLAUDE.md](../CLAUDE.md)。追加式,只增不改。

## 2026-09-26:proj-overview v2 规格升级(认读第一入口 + summary 职责,F052)

用户对 v1 产物两不满(mermaid 横向可读性差 / 内容不足以一篇掌握)→ design-Q L0+L1 两层(W00 两波 24 采纳 1 取消;补充声明「不设行数硬性上限」+「认读第一入口:人重载上下文从此开始」)+ grill-Q 九题压测(8 采推荐 + Q7 推翻推荐「认读第一入口」进 CONTEXT + Q4 自定义扩展:OD 加状态字段修源,同类问题全仓检查结论 = 唯 OD 缺)单波收口;13 项修订全执行含 ⚠ 两项(方法论 §3.3.1 行同步 + 修订记录行 / OD 29 条状态字段补齐 open 8·观察中 11·已收口 10,OD 文件头格式说明此后状态必填)。F052 四步:① SKILL.md 五处修订 54 行 + en 回译(stamp 9926b5712b94)+ 双侧同步 0 违规;② ADR-0026 修订注记 + 挑战报告 #三 v2 注记;③ 产物八段式重生成 230 行(ADR 26 / OD 29 全量表,全竖向 5 图,分型自检留痕;TODO 头部漂移自检二次触发 → 人拍板草案转写);④ 治理收尾(根 CHANGELOG 中英双落 / README:129·CLAUDE.md:68·en 两镜像描述同步 / skill CHANGELOG / 本条)+ 四门终验。CONTEXT 新词「认读第一入口」(first-reading entry 待人确认)+「人读派生视图」译名尾注清理。失忆测试窗口自 09-26 重算(≥09-29,三问走三分钟导读档;v2 反馈模板三问预置 DESIGN.md)。设计套 [proj-overview-v2/](../design/proj-overview-v2/)。

## 2026-09-25:proj-overview 入库与全链收官(F049–F051,第 9 个 skill)

skill 家族 8→9:skills/proj-overview/(SKILL.md 53 行 + DESIGN + CHANGELOG)+ 全局侧分发洁净同步 + en 首译同批(TRANSLATABLE skills/* 通配实测生效——入库即负翻译义务,欠账窗口 <1 会话即消)。F050 首次 dogfood:harness/PROJECT-OVERVIEW.md 135 行(四层 BFS 分解 + 三条 DFS 关键链),漂移自检分支首次真实触发(TODO 头部滞后 3 处 → 人拍板口述草案转写);逐图渲染验证 4 SVG 过。F051 十处联动:HARNESS-RULES §六新类目(人读派生视图)+ 方法论 §3.3.1 加行(版本内修订 + 记录行)+ README/CLAUDE/CONTEXT 9-skill 表述 + 根 CHANGELOG 中英双落 + CONTEXT 术语「人读派生视图」(译名待人确认)。全局侧 DOGFOOD-LOG 登记(人过目后写入)。四门全绿贯穿。失忆测试窗口自 09-25 起算(≥09-28 人判,结果回写 skills/proj-overview/DESIGN.md)。设计套 [human-project-view/](../design/human-project-view/) + [ADR-0026](../adr/0026-proj-overview-derived-view-route.md)。

## 2026-09-23:human-project-view 设计三层全链(proj-overview skill,挑战三正面回应)

design-Q feature(用户发起:哲学 v7 挑战报告挑战三「元系统膨胀」+ 实践感受「harness 文件人读/AI 读双职责冲突——AI 读要严谨详细重建上下文,人读要认知友好,现状 238 md 致人的注意力不足」)三层问卷 53 要点采纳 50 / 深究 3(L0 W01 十题全采推荐),零逃生舱 → 设计套 [harness/design/human-project-view/](../harness/design/human-project-view/):L0 视图层(只读派生、核心判据「减的负荷 > 加的负荷」、验收锚 = 失忆测试人判非 AI 自评)、L1 契约层(输入·处理·输出三层硬约束 + 选型 14 项含被否决列 + HARNESS-RULES §六新类目 + 联动九处含方法论 §3.3.1 版本内修订加行)、L2 构建层(P0 skill 编写 → P1 本仓库首生成 dogfood → P2 全仓联动,DoD 全脚本化 + 回归项);问卷四份归档 [human-project-view/](../harness/questionnaires/archive/human-project-view/)。skill 定名 **proj-overview**(产物 `harness/PROJECT-OVERVIEW.md`;md+mermaid 首期单格式;BFS 层次分解图 + DFS 每功能逻辑链,混合类型学节点两类边三类;≤250 行 / 图 ≤30 节点 / 图数 ≤12;TODO 头部 = 快照唯一权威源 + 漂移自检提示;完全抽象 + 实例外置;人因四原则 + 文风术语表 20 词内嵌 SKILL.md < 100 行)。挑战报告 #三 反馈行已填;canonical「人读/AI 读分野」论述缓行走独立审查(TODO 在案)。收尾面板裁决:单线程 / dogfood 内建(P1) / **先 grill-Q 压测设计套再实现** / 压测后 long-running 衔接。环境实测:mermaid CDN 可达(jsdelivr 200)+ HTML+mermaid@11 浏览器渲染通过(2026-09-22)。

## 2026-08-26:i18n-support 实现期收官(P3–P5 全绿,首期完成)

long-running 三会话接力:**F046/P3**(五件 en 镜像 1,976 行 + 术语第二批 31 条;七步②.5 首次实证——practical_v1 zh 源缺陷停翻报修;mermaid 转义引号人审实锤 → L1 §3.4 标签引号规则)→ **F047/P4**(八件 SKILL.md en 镜像 1,151 行 + 术语第三批 28 条累计 80;gwd 特例落地;人审裁决 A「文档型围栏块中文文案译出」/ 裁决 B「特例加标准头部」均认可)→ **F048/P5**(CHANGELOG 全译双落(含首期完成条目 append-only 首笔)+ TRANSLATABLE 终扩 + **L0 验收七条终验全过**——⑥ 过期检出二次实测、⑦ en 清点 = 白名单全集 15 件集合相等;收口三件 = 根 CHANGELOG 条目 / 本条 / TODO 块「首期完成,扩面另立」)。en 镜像树 15 件,四门全绿贯穿(i18n 0 / 脱敏 0 / sync 0 / harness 0);术语对照节 80 条为英文翻译唯一事实源。首期后扩面(retro / OD 全量 / archive)另立 TODO,不并入首期;CHANGELOG 逐条追译长期负担回访点在案(L1 §4.3)。

## 2026-08-23:i18n-support 设计三层全链 + dogfood 微闭环(P1+P2)

design-Q feature i18n-support(用户发起,重访 readme-revamp「不做英文 README」已决项)三层问卷全采纳(L0 23 / L1 21 / L2 17,61 条零取消零逃生舱)→ 设计套 [harness/design/i18n-support/](../harness/design/i18n-support/) + [ADR-0025](../harness/adr/0025-english-mirror-drift-governance-integration.md)(英文镜像第三轴:顶级 en/ 镜像树 + en 文件头三字段 + i18n-check 五类漂移检查 + 第四道手动提交门,与双侧同步正交零侵入)+ [CONTEXT「英文术语对照」节](../docs/CONTEXT.md)(镜像消歧 2 条 + 首批 18 条)。收尾面板裁决:单线程 / 先 dogfood / 压测 / 衔接 long-running。dogfood 微闭环:P1 机制([i18n-check.py](../scripts/i18n-check.py) T1–T7 自测全绿)+ P2 README 英译(含 mermaid 图内标签译英——人审质询触发 L1 §3.4 修订)+ 规格缺口 3 处回修(白名单随阶段扩容 / 切换行笔误 / mermaid 译图,记 [L2 §6](../harness/design/i18n-support/L2-build-i18n-phases-dod.md));四门全绿(脱敏 0 / 双侧同步 0 / harness 0 / i18n 0)。**grill-Q 压测轮**([grill-i18n-support-w01](../harness/questionnaires/archive/i18n-support/grill-i18n-support-w01.md),10 题:8 采推荐 + 2 推翻——Q2 程序防御 mtime 拒绝、Q9 维持四道门):8 修订全授权执行(锚点降路径级 / --stamp mtime 前置校验 / DoD 清单扩容子项 + 未入册 note 行 / 场景三范围补注 / 七步 ②.5 停翻报修 / grill-with-docs 特例 / 术语按文件批量 / frontmatter 终裁维持),CONTEXT 加「翻译义务清单(TRANSLATABLE)」消歧行;T8/T8b/T9 自测全过,四门复跑全绿。P3–P5 留 long-running。

## 2026-08-19:grill 家族边界与跑偏治理(深钻 → 复压闭环)

grill-with-docs 深钻四分支(认知状态三态接线 / 入口+中途双检测 / 校准闸门+题级 ❌ 标注双件 / 优化回路 [OD-26](../docs/OPEN-DECISIONS.md) provisional)→ 包一 skill 规格层落地(grill-Q 族间自检/校准闸门/阻塞性逃生舱分流/质量信号节 + FORMAT 规则 15 ❌ 专属分叉 + with-docs 反向相变)→ [grill-boundary-canonical-w01](../harness/questionnaires/archive/_misc/grill-boundary-canonical-w01.md) 复压(9 题全采纳 + Q8 推翻推荐 → 本文件同步三态)→ canonical 版本内修订(哲学 §3.1 认知状态行;方法论 §4.1 接线 / §4.3 优先级 / §3.3.1 指针 / §八 第 25 条;两文件头修订记录行)。斯多葛视角不落盘(对话层)。OD-4 母本同步(仓库外)累计一笔。

## 2026-08-19:skill 双侧同步机制化

2026-08-18 双侧同步(9 skill 双向合并,commit 4fece7c)暴露「项目内修、全局漏修」空隙(8/14 修订落全局漏项目、8/8 归档断链修复落项目漏全局),机制化收口:新增 [scripts/skills-sync-check.py](../scripts/skills-sync-check.py)(check-only 不选边、裁决例外白名单、EXIT 码供例行)+ CLAUDE.md 铁律第 8 条 + 工具命令节扩为两条(提交前例行,暂不入发布门强制清单);问卷 [confirm-skills-sync-mechanism-w00.md](../harness/questionnaires/archive/_misc/confirm-skills-sync-mechanism-w00.md)(14/14 全确认)。

## 2026-08-14:methodology_v5 升级完成(章节连续化 + 契约优先 + action-Q 入族)

grill-Q methodology-improvement W01 压测(10 题,压测对象 = 哲学 v7 + 方法论 v4 + design-Q 规格,参照 同级对标仓库 治理)产出:① 正文连续编号 §零至§九(v4 映射表在文件顶部)+ 全库引用审查;② §4.3 两族表补 action-Q(修 W02 Q3 漏改)+ CLAUDE.md 协作图补节点;③ §5.3 补「时序纪律」(契约层变更先更新 canonical 设计再动工,ADR-0021 通用化);CONTEXT 补规范导航(含设计套「契约优先」裁决)与「暂定」状态词、ADR-0020 补生态位卡载体裁定、新增 OD-24(全局实验/项目 backup/DOGFOOD 实测双副本策略)。**同轮立项**:design-Q 数字层级改造(Q3-A)、dogfood 最优先 + 定义消歧(Q7-A,冻结新机制新增)、方法论 704 行审计优先(Q4-B)——见 [TODO.md](../TODO.md)。v4 归 archive。

## 2026-08-14:philosophy_v7 升级完成(连续章节 + 双文件交叉治理)

在 v6 基础上建立哲学独立阅读入口,将正文统一为 §一至§五并保留旧编号兼容映射;补 harness 术语边界、current 已知缺口状态、前三学科最小进入/退出模板与代理指标反思边界;哲学 + 方法论成为 canonical 对等双文件,由 [ADR-0017](../harness/adr/0017-philosophy-section-compatibility.md) / [ADR-0018](../harness/adr/0018-canonical-dual-challenge-governance.md) 记录治理契约。v6 归 archive,v7 为 current canonical。

## 2026-08-13:grill-Q philosophy-v5 成稿压测 W01 闭环 + 发布门推送

压测 10 题(Q1 用户裁决更名「第五→第四学科视角」:全仓同步 + ADR-0015/0014 更名注记;Q2–Q10 全 C:§八 修订 9 处),全部执行并验证(脱敏 0 / harness-check 0);OD-1 三道过后推送(7853792..f93cc8b,2 commits);F026 OD-4 母本同步用户仓库外执行销项;feature_list 校正(F002/F004/F005 补 passes)。**剩 dogfood(F006 唯一剩余)**。

## 2026-08-13:philosophy_v6 升级完成(结构过渡 + 方法论治理闭环 + 学科治理路线图)

在 v5 基础上新增全文阅读路线与章节过渡;§8.6 明确为「方法论自身的治理闭环」,加入主张状态模板与「学科 → 治理机制 → 最小产物 → 进入条件」映射;v5 归 archive,v6 随后曾为 current canonical,现由 v7 接替。治理深度仍遵守最小治理切片边界,完整 Level 1/2/3 由 [OD-20](../docs/OPEN-DECISIONS.md) 管理。

## 2026-08-11:philosophy_v4 → v5 立论重构完成(安全科学第四学科视角 + 去 AI 黑盒锚点)

经完整 write→review→implement 闭环:grill-Q philosophy-v4(W01/W02,18 处修订)→ discipline-mapping([ADR-0014](../harness/adr/0014-discipline-mapping-strategy.md) 学科挂接分层)→ grill-with-docs(去黑盒 6 点结晶,落 [CONTEXT AI 黑盒节](../docs/CONTEXT.md) + [OD-19](../docs/OPEN-DECISIONS.md))→ design-Q philosophy-v5([VISION/HLD/LLD](../harness/design/philosophy-v5/) + [ADR-0015](../harness/adr/0015-deblackbox-anchor.md))→ 设计套压测(10 项修订)→ long-running 起草(P1-P5,commit 530d0f4);v4 归 archive。新增 OD-18(学科挂接回顾)/ OD-19(形式化 V&V 缺口);v5 §八「去 AI 黑盒」(三层次 + 正交第一支柱 + 三风险 + 统合对策 + 弹性边界)。

## 2026-08-08:doctor-for-harness 完成(第 9 个 skill)+ harness 治理落地

分层规则权威化([HARNESS-RULES.md](../skills/doctor-harness/HARNESS-RULES.md),ADR-0012/0013)+ 校验脚本 [scripts/harness-check.py](../scripts/harness-check.py)(命名/ADR 编号/归档位置三检查);设计套压测 10 题全认定 + 7 项工件修订执行;格式反馈落地(单波次上限 10 / 小波阈值 3 四副本统一);**归档子目录化**(41 份按 feature/主题迁入 10 子目录 + [archive/README.md](../harness/questionnaires/archive/README.md) 索引);MIGRATION-FLOW 迁移流程沉淀。

## 2026-08-07:design-Q skill 规格整理(skill-spec-revamp)→ 撤销方案 R

骨架增强(HLD/LLD 判别法则 + 反简化最小必含 + 坍缩分档,仅 design-Q)**保留并回灌**;落盘路径配置化(方案 R)**已放弃**([ADR-0011](../harness/adr/0011-abandon-plan-r-hardcode-harness.md)),**回归硬编码 `项目根/harness/`**(design/ + questionnaires/ + adr/);两套 skill(skills/ 与 `~/.claude/skills/`)已重建一致(仅脱敏差),设计套 [harness/design/skill-spec-revamp/](../harness/design/skill-spec-revamp/)。

## 2026-08-05:repo 级设计完成,落地执行中

design-Q 三阶段 + grill-Q 压测 12 项回灌(设计套 [harness/design/repo/](../harness/design/repo/));方法论 + 哲学升 **v4**(受众收窄个人 / 第二支柱机制层对称化 / 哲学三学科化(人因/软工/运筹));harness 区物理分离(docs/design/ + docs/questionnaires/ 迁入);术语治理(8 术语全保留 + 新词三条件门槛)。落地执行 P1–P4 完成(P1 迁移 / P2 术语 / P3 v4 / P4 入口),**P5(ADR-0008/0009/0010)与 P6(发布门 + dogfood)待执行**,见 [TODO.md](../TODO.md)。

## 历史线(2026-07-29 起)

2026-07-29 methodology_v3 完成(ADR-0004/5/6);2026-08-01 action-Q 入库(第 8 个 skill)+ 首次推送;2026-08-04 三块拆分(ADR-0007);2026-08-05 repo 级设计 + v4 + harness 迁移;2026-08-08 doctor-harness 完成(第 9 个 skill);2026-08-11 philosophy_v5(安全科学第四视角);2026-08-13 philosophy_v6(治理进化);2026-08-14 philosophy_v7(连续章节与双文件交叉治理)。
