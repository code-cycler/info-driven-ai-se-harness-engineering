# TODO

> 追踪文件。建仓:2026-07-28(建仓前经 grill-questionnaire 两波压测驱动筹建)。
> 当前状态:**methodology_v3 已发布(2026-07-29);action-questionnaire 已入库(2026-08-03);2026-08-04 三块拆分(ADR-0007);2026-08-05 repo 级设计完成 + v4 落地 P1–P5 完成**(方法论 + 哲学升 v4(受众收窄 / 第二支柱机制层 / 三学科化)、harness 区物理分离、术语治理、ADR-0008/0009/0010、入口改造)**。P6(发布门 + dogfood)待执行**。
> 下一步主线:**P6 发布门**(OD-4 母本同步(用户配合)+ 语义人审 + dogfood(用户验收));CONTRIBUTING + issue 模板(OD-3);git author 身份决策;grill-Q 压测 v4 成稿(可选)。

## 已完成(2026-07-28 建仓)

- ✅ 定名 `info-driven-ai-se-harness-engineering`(双支柱方向:信息驱动 × AI+软件工程 = 驾驭工程)
- ✅ 本地建仓 + 目录结构 + README / LICENSE(双协议) / .gitignore
- ✅ 复制 7 个核心方法论 skill + methodology_v2 + 归档问卷
- ✅ 脱敏脚本 [scripts/desensitize.py](scripts/desensitize.py) + 机械脱敏(skills 39 处 + v2 3 处,**脚本 0 命中**)
- ✅ methodology_v2 订正(3 处立论改写 + v1 断链处理)
- ✅ ADR-0001/0002/0003 + OD-1～9 + CONTEXT 迁移(脱敏重写、重编号)

## 待办(新会话 design-Q 起点)

### 🟠 v3 设计修订项(grill-Q v3-design W01 产出)

> 来源:grill-Q 压测 v3 设计套(VISION/HLD/LLD),12 题全采纳。挖出设计期盲点,回灌 HLD/LLD。
> ✅ **已执行(2026-07-29)**:9 项修订全部落 [HLD_v2](harness/design/hld_v2.md) / [LLD_v2](harness/design/lld_v2.md);Q2+Q12 → [ADR-0005](harness/adr/0005-pillar-standard-wording.md);Q3 章节策略 → **彻底重排**,[ADR-0006](harness/adr/0006-v3-chapter-restructure.md)。归档问卷 [grill-methodology-v3-design-w01](harness/questionnaires/archive/grill-methodology-v3-design-w01.md)。
> ✅ **已落地(2026-07-29,long-running 会话 001)**:9 项随 v3 起草全部实现并 DoD 验证(grep 证据见 `.claude/claude-progress.txt`)。

- ✅ **HLD#11 标准措辞按 [ADR-0005](harness/adr/0005-pillar-standard-wording.md) 修订**:定义版(CONTEXT/README/CLAUDE)+ 完整版(v3§2.1),核心子串四处 grep 一致
- ✅ **HLD#9 三层立论模型表加因果方向**(Q1):v3 §2.1 表头「层(因果方向 ↓)」+ ↓导致/↓表现 行
- ✅ **HLD#1 章节策略**(Q3):**结论 = 彻底重排**(用户定夺,见 [ADR-0006](harness/adr/0006-v3-chapter-restructure.md));v3 章节按新立论重排,锚点全量重写
- ✅ **LLD 加 §2.1 改写回归 DoD**(Q4):LLD_v2 L4 已加;v3 grep 验证「有效上下文/120k/400k/双支柱」全在
- ✅ **LLD#7 v3 文件头写完整谱系**(Q5):v1 单支柱 → v2 双支柱 → v3 补机制层 + 推导链
- ✅ **LLD 补 §十一 失败模式表更新**(Q6):v3 §十一 #19–22(三层误读 / 双靶子失衡 / (a)(b) 混淆 / 标准句脱节)
- ✅ **LLD#12 DoD 脚本具体化**(Q7+Q8):核心子串 grep + 章节清单核对 + § 引用 Python 校验,均已在 v3 发布门执行
- ✅ **LLD#13 回归 DoD 措辞修正**(Q9):LLD_v2 已修;v3 按「内容不丢」执行关键概念 grep 全过
- ✅ **HLD#8 CONTEXT 术语清单扩展**(Q10+Q11):CONTEXT 新增「第一支柱术语分层(v3)」节,8 术语全部落盘标层级

### 🔴 methodology_v3 起草工作包(grill-Q W01 产出 · ADR-0004)

> 来源:grill-Q 压测 methodology_v2([W01](harness/questionnaires/archive/grill-methodology-v2-w01.md)),D7 核心发现——第一支柱立论实质偏离作者本意,「AI 幻觉式决策」机制层缺席。详见 [ADR-0004](harness/adr/0004-methodology-v3-hallucination-thesis.md)。
> ⚠️ **实现规格以 [LLD_v2](harness/design/lld_v2.md) 为准**(P0 章节设计 → P1–P4,5 阶段);本块为 ADR-0004 时期的初始拆分,章节策略已升级为彻底重排(ADR-0006)。

- ✅ **升 methodology_v3,补全第一支柱机制层**(ADR-0004 决策 1,2026-07-29 完成):
  - ✅ 两类信息断层(v3 §1.2:人与人 → AI 替代角色挂 §6.2;人与AI → 问答对齐挂第五章),返工框架保留为症状层
  - ✅ §2.1 正面因果立论:「背景缺失 → AI 在信息真空中的幻觉式自作主张决策 → 返工。问答逐步对齐需求,是对抗此机制的直接手段」(blockquote 独立引用形式,DoD Q8 核验通过)
  - ✅ §2.1/§7.6 过载对策链:design-Q 沉淀落盘 → /compact 压缩;点明「缺失 vs 过载两环节不矛盾」
  - ✅ §5.1 (a)(b) 盲区小节,grill 锚定 (b);§十二 加背景缺失自查项
  - ✅ 双靶子:vibe coding 主叙事限 §一 + 立论挂接点,传统 SDLC 原位保留为对照(grill-with-docs 压测定案)
- ✅ **CONTEXT.md 同步**(ADR-0004 决策 3,2026-07-29):第一支柱换 ADR-0005 定义版;8 术语分层清单落盘
- ✅ **README.md / 项目 CLAUDE.md 开篇同步**(2026-07-29):双支柱表述与 v3 一致;另修复 CLAUDE.md 两处——导航节 v2→v3 链接、脱敏映射真实名复述(脱敏门 2 命中 → 0)
- ✅ **OD-4 母本同步**(2026-08-01 执行,commit b16328e):作者另外两个仓库副本均已标注「开发副本,以 v3 为准」(仓库外动作)
- ✅ **v3 起草驱动方式抉择**(2026-07-29):design-Q 设计套 + long-running-agent 起草 + grill-with-docs 压测 P0 章节大纲,未裸写;**遗留可选质量门:grill-Q 压测 v3 成稿**

### 其他待办

- ⏳ **术语全面审计(B 方案)**(2026-08-05,repo 级设计 vision Q4 自定义入档):v4 术语折中审计落地后执行——逐术语判定保留/合并/删除/换学科标准词,CONTEXT 重写,方法论全文 + skill 规格同步(人因工程/软件工程/运筹学学科对接)

### 🔴 repo 级设计落地执行(2026-08-05 设计完成,规格 = [LLD](harness/design/repo/LLD.md))

> 来源:repo 级 design-Q(vision→hld→lld 全流程,参考「项目A」架构;设计套 = VISION/HLD/LLD + 问卷 4 份)。规格见 [harness/design/repo/](harness/design/repo/)。P1–P5 已由 long-running 执行(commit: cb68950 / cb04faf / 9686a61 / 1e2ee28 / 6bd7aed),每阶段 DoD 全绿(脱敏 0 / 断链仅豁免 / 内容不丢)。

- ✅ **P1 harness 区迁移 + 链接改造**(2026-08-05):docs/design/ + docs/questionnaires/ → harness/(git mv);129 处字符串替换 + 相对链接重算;5 skill 落盘路径同步;断链 96 → 7 豁免
- ✅ **P2 术语判定表 + CONTEXT 更新**(2026-08-05):8 术语全保留(学科参照注记)+ 新词三条件门槛;ADR-0005 核查无替换无需修订
- ✅ **P3 方法论 + 哲学 v4 内容修订**(2026-08-05):§零 受众收窄个人 / §2.2 机制层对称化(无护栏 → 劣化)/ 哲学三学科化(§一 人因、§六 软工、§七 运筹新节)/ v3 归档 archive/ / 全库 v4 链接
- ✅ **P4 实操同步 + 入口**(2026-08-05):CLAUDE.md 瘦身 6 节(规范优先级唯一权威处)+ AGENTS.md 零内容路由 + README 三区模型与发布说明;实操文件无受众表述无需改(压测 Q9)
- ✅ **P5 ADR + 归档**(2026-08-05):ADR-0008/0009/0010 落地;v3 移 archive/ + 谱系更新
- ⏳ **P6 发布门 + dogfood**(进行中):① OD-4 母本同步——**已执行**(2026-08-05,7 处副本标注「开发副本,以 v4 为准」,复核发现 07-30 标注因清理丢失已重标,证据入 OD-4);② 语义人审(含 git 提交信息,OD-1 ②);③ dogfood——实操文件一次真实轻量修订任务按新规范走通(**验收 = 用户实际执行**,压测 Q11)

- ✅ **脱敏语义人审**(OD-1 ②,2026-08-01 完成):subagent×4 全文遍历执行(归档问卷 / docs+根 / skills+scripts / git 层),占位通顺度与语义指纹均审;发现与修复见🟡节两条 ✅;遗留 git author 身份与历史指纹两项决策(见下)
- ⏳ **design-questionnaire 正式设计**:vision → HLD → LLD。本批 [ADR](harness/adr/) / [OD](docs/OPEN-DECISIONS.md) 作输入
- ✅ **远程仓库建立 + push**(2026-07-29):[code-cycler/info-driven-ai-se-harness-engineering](https://github.com/code-cycler/info-driven-ai-se-harness-engineering),首次推送 2 个 commit(建仓全量 + long-running 工件);push 前 OD-1 三道门全绿(脚本 0 命中 / 语义人审已过 / 映射表外置)
- ⏳ **CONTRIBUTING + issue 模板**(OD-3):experimental 维护声明落地
- ⏳ **skill 内容审校**:复制的 7 skill 是否完整;引擎副本漂移(OD-8)是否需在 skill 区 README 说明
- ⏳ **可迁移性单点深钻**(可选):对 OD-2 逐 skill 盘 Claude Code 依赖,产出「理念 vs 执行依赖」清单(用 grill-with-docs)
- ✅ **methodology_v3 三块拆分执行**(2026-08-04 完成,ADR-0007 + [HLD](harness/design/hld-methodology-separation.md),long-running-agent 驱动):三文件迁移(methodology_v3.md 678 行 / philosophy_v1.md / practical_v1.md,28 块回归验证内容不丢)+ 问题引子段 + 17 处跨文件 § 引用改造 + §7.4-7.6 移实操 + action-Q 机制论述(候选③消项)+ 导航 4 处 + 回归 DoD 全绿(章节 22 项/核心子串 14 项/链接 81 个)+ 脱敏门 0 命中;**验收信号(压测 Q10):拆分落地后首次实操文件修订走轻量流程(免 OD-4/四处锁定)成功走通——待观察**
- ⏳ **引擎副本 §8.8 旧锚点漂移处置**(ADR-0007 知识发现,2026-08-03):三份 QUESTIONNAIRE-FORMAT(grill-Q:83 / design-Q:131 / retro-Q:82)引「方法论 §8.8」为 v2 旧锚点,v3 已无此节——更新为 v3 对应节或改为不标节号

### 🟢 行动前细节确认 skill(grill-Q W01 压测产出,2026-07-30)

> 来源:[grill-preaction-confirm-skill-w01](harness/questionnaires/archive/grill-preaction-confirm-skill-w01.md),15 题全答(11 勾选 + 4 自定义)。压测对象:复用 design-Q 引擎 + 阈值 ≤2→4 + preview 保留的行动前确认 skill 提案。
> 核验时机:skill 创建完成时,核对其 DESIGN.md 是否含全部 15 题裁决 + dogfood 跳过理由;同步启动时核对 7→8 六处文件。

- ✅ **创建新 skill**(2026-07-30):[skills/action-questionnaire/](skills/action-questionnaire/)——SKILL.md + 引擎副本×2(含 W00 节改 confirm-list)+ DESIGN.md(15 题裁决全录 + 被否决项 + 漂移声明 + dogfood 范围);脱敏门 0 命中。15 题裁决落实:① 独立新 skill;② 阈值 ≤4(经验估值待校准);③ preview 更名 confirm-list 改确认式;④ confirm-list 为主、正式题波兜底;⑤ 铁律 2 环境现实验证;⑥ 归档留痕 + 三条件升格;⑦ 非正式行动写操作默认确认;⑧ delegate 显式声明继承白名单才豁免;⑨ 隐式骨架六要素终止判据;⑩ 不嵌入 long-running、feature 级转出提醒;⑪ 1 轻量 dogfood 案例作同步门槛;⑫ 引擎第 4 份副本含 W00 节 + 有意分叉声明(OD-11)
- ✅ **命名定 `action-questionnaire`**(2026-07-30,Q14 自定义「action *」解读为 action 前缀 + 问卷族后缀;改目录名双向门可逆)
- ✅ **canonical 同步(7→8)**(2026-08-03,confirm-canonical-sync-7to8-w00 全确认执行):门槛 2026-07-31 已过(action-Q 首案例,见下节🟡);6 文件 7 处全部落地——methodology_v3(§快速上手/§8.3 分类表加「确认」行)、README×2、CLAUDE.md、CONTEXT.md、ADR-0003、OD-2 计数重测(Ask 18 / sub 4);连带修订:CLAUDE.md 状态节刷新至 2026-08-03、OD-13 触发②「第 8 个」措辞、README/v3/CLAUDE 三处 mermaid 图补 action-Q 节点

### 🟡 skill 家族生态位分析产出(action-Q 首次 dogfood,2026-07-30/31)

> 来源:[confirm-skill-niche-overlap-w00](harness/questionnaires/archive/confirm-skill-niche-overlap-w00.md)。结论:7(+1) skill 无真重叠(三件套 = 连续体 + 交互轴分工);grill 家族不可替代性退守三残差(深依赖链 / 即时反馈偏好 / 零留痕)。
> 本 dogfood 案例同时是上节「canonical 同步(7→8)」的门槛案例——D-1 回修完成 + DESIGN.md 记录后门槛过关。
> 核验时机:F1–F4 下次修订对应文件时逐项核对;F6 以 grill-Q 压测完成清单为准。

- ⏳ **F1 grill / grill-with-docs SKILL.md 路由表补 grill-Q**(pasted-plan 场景无路由;grill 的 supporting-info 仅对比 with-docs)——挂 OD-12(grill 处置重估时一并处理)
- ✅ **F2 grill-Q description「同用途不同交互」措辞修订** —— 2026-08-01 被 R5 吸收执行(80/20 层位表述替换)
- ✅ **F3 v3 §5.3 两族表落盘行拆分 grill vs with-docs** —— 2026-08-01 被 R2 吸收执行(落盘行拆分 + 「判断成本层位」行新增)
- ✅ **F4 v3 §8.3 触发词表补「计划评审」裁决轴** —— 2026-08-01 被 R7 吸收执行(二八判据分流)
- ⏳ **F6 重估 §5.2 / 合并 grill 家族** → 转 grill-Q 压测(W01 已生成);**2026-07-31 W01 作废**(用户裁决):「合并」框架被「grill-Q 原初设计意图(80/20 原则 + 忠于 with-docs 问卷化演进,减少判断成本)」取代,由「生态位区分」行动承接([confirm-grill-niche-distinguish-w00](harness/questionnaires/archive/confirm-grill-niche-distinguish-w00.md))
- ✅ **D-1 回修 action-Q PROCESSING-RULES 补充声明第四类**(2026-07-31 完成:解析规则 3 + FORMAT 规则 12 补「用户先验结论 → 待验证假设」;repo + 用户级双副本同步;头部分叉声明 #4 + DESIGN.md 有意分叉 #6;用户小波裁决「只改 action-Q」,canonical 未动)
- ✅ **R1–R9 生态位区分文档修订(深度 A)**(2026-08-01,[confirm-grill-niche-doc-revisions-w00](harness/questionnaires/archive/confirm-grill-niche-doc-revisions-w00.md) 全勾确认):80/20 判断成本原则落 v3(§5.2 保留段改写 / §5.3 两族表层位行+落盘行+选择原则 / §4.2 环节 2 层位与交接 / §8.3 触发词二八分流 / 附录 C 续行)+ CONTEXT Grill 家族节 + grill-Q & with-docs description 层位正名 + grill-Q DESIGN.md 原初原则补记;skill 三文件双副本同步;脱敏扫描发现 OD-4 既有真实名命中(见下,非本次引入)
- ✅ **脱敏门修复(2026-08-01,用户授权选项①+③)**:OD-4 行 47 真名改占位 + tip 提交 amend(b16328e,信息+内容同修;OD-1/OD-12 随 amend 并入);提交内与工作区复扫均 0 命中。流程改进已落:OD-1 占位方案 ② 纳入「git 提交信息」人审(扫描盲区,本次即实例)
- ✅ **脱敏语义人审(subagent×4 全文遍历,2026-08-01)**:🔴0 阻断;技术栈指纹(真实库名/内部 ADR 编号)4 处泛化、取证指针 1 处弱化、单字母「A」正字「作者」、ADR-0001 描述词 2 处删除;方法论 v2 移入 archive/ + 3 处断链修复
- ⏳ **git author 身份决策**(人审遗留):已推送 5 提交携带作者邮箱(QQ 号)+ handle(handle 在脱敏映射表内);选项:接受现状 / 改 git config 止血未来提交 / 历史改写 + 强推(单向门级,破 fork/clone)。建议至少做 config 止血
- ⏳ **已推送历史中的语义指纹**:skills 技术栈细节与 OD-7「另一公开项目」链已随首次推送公开(本轮已 fix-forward);历史是否改写与上一项一并决策

### 🔵 AI 双轨对照 pilot + 问卷默认勾选试点(grill-Q ai-autonomy W01/W02 压测产出,2026-08-01)

> 来源:[grill-ai-autonomy-w01](harness/questionnaires/archive/grill-ai-autonomy-w01.md)+ [w02](harness/questionnaires/archive/grill-ai-autonomy-w02.md),共 18 题全答,0 逃生舱。压测对象:用户双轨构想(影子模式 + 冠军挑战者)与 skill 改动提案。裁决落 [OD-13](docs/OPEN-DECISIONS.md)(双轨 pilot 立项,含 W02 补正)/ [OD-14](docs/OPEN-DECISIONS.md)(默认勾选试点,5 条边界)。
> 核验时机:各行动完成后,核对是否满足 OD-13/OD-14 的边界条款(单向门豁免 / 选项排序 / 取消率设防 / 禁区保留 / mode: full 底线不变)。

- ✅ **shadow pilot skill 创建 + 首轮 dogfood**(2026-08-01 创建;2026-08-03 首轮反馈沉淀):`~/.claude/skills/shadow/`(SKILL.md + DESIGN.md)——先影子后真实、影子 = 自动 dogfood 不设 N、subagent 仅双轨、权限 = delegate `mode: full` 排除集、验收 = 事前 DoD + 端到端测试 + 人仲裁、日志脱敏(绝对路径 → `~`,相对路径引用允许)。**暂不入家族**(OD-13,家族化 = OD-13 重访触发②);仓库 skills/ 暂不放置(pilot 期不进入分发面)。首轮 dogfood(DOGFOOD 沙盒 shapez-game-test):**「AI 自评可玩 ≠ 人类可玩」实证 + 价值定位调为模板/demo + 升级条件化(人试玩通过)**,数据落 OD-13
- ✅ **design-Q 默认勾选试点执行**(2026-08-01,用户授权执行):QUESTIONNAIRE-FORMAT(W00 预勾 + 选项排序 + 问题级排序 + 单向门豁免)+ PROCESSING-RULES(默认勾选设防节:取消率 / 确认点 / 3 波零取消回退)+ SKILL.md(W00 段/作答/统计);用户级 + 仓库级双副本同步(脱敏差异保持);只改 canonical,四副本同步留 OD-8 重访(OD-14)
- ✅ **delegate 多模式执行**(2026-08-01,用户授权执行):SKILL.md「全权模式(mode: full)」节(白名单反转排除集,底线 + 留痕不变)+ delegation-template.md frontmatter `mode` 字段 + 实测条款「实测(只读)可自主、归类仍交人/入排除集」;双副本同步(OD-13 W02 Q3/Q4)
- ✅ **日志脱敏规则**:已落 shadow SKILL.md 铁律 5 + 落盘表(绝对路径 → `~`,不进公开仓库)(OD-13)
