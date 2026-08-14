# TODO

> 追踪文件。建仓:2026-07-28(建仓前经 grill-questionnaire 两波压测驱动筹建)。
> 当前状态:**methodology_v3 已发布(2026-07-29);action-questionnaire 已入库(2026-08-03);2026-08-04 三块拆分(ADR-0007);2026-08-05 repo 级设计完成 + v4 落地 P1–P5 完成**(方法论 + 哲学升 v4(受众收窄 / 第二支柱机制层 / 三学科化)、harness 区物理分离、术语治理、ADR-0008/0009/0010、入口改造)**;2026-08-08 doctor-for-harness 完成(第 9 个 skill)+ harness 治理落地(分层/校验/迁移)+ 格式反馈 + 归档子目录化**。P6 发布门已执行(2026-08-13 推送 7853792..f93cc8b,OD-1 三道过);**dogfood 待执行**。
> 下一步主线:**dogfood**(实操文件一次真实轻量修订任务,用户验收);三文件层级化治理(单独立项);CONTRIBUTING + issue 模板(OD-3);git author 身份决策;术语全面审计(B 方案)。

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
> ✅ **已执行(2026-07-29)**:9 项修订全部落 [HLD_v2](harness/design/hld_v2.md) / [LLD_v2](harness/design/lld_v2.md);Q2+Q12 → [ADR-0005](harness/adr/0005-pillar-standard-wording.md);Q3 章节策略 → **彻底重排**,[ADR-0006](harness/adr/0006-v3-chapter-restructure.md)。归档问卷 [grill-methodology-v3-design-w01](harness/questionnaires/archive/methodology/grill-methodology-v3-design-w01.md)。
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

> 来源:grill-Q 压测 methodology_v2([W01](harness/questionnaires/archive/methodology/grill-methodology-v2-w01.md)),D7 核心发现——第一支柱立论实质偏离作者本意,「AI 幻觉式决策」机制层缺席。详见 [ADR-0004](harness/adr/0004-methodology-v3-hallucination-thesis.md)。
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

> 来源:[grill-preaction-confirm-skill-w01](harness/questionnaires/archive/preaction-confirm/grill-preaction-confirm-skill-w01.md),15 题全答(11 勾选 + 4 自定义)。压测对象:复用 design-Q 引擎 + 阈值 ≤2→4 + preview 保留的行动前确认 skill 提案。
> 核验时机:skill 创建完成时,核对其 DESIGN.md 是否含全部 15 题裁决 + dogfood 跳过理由;同步启动时核对 7→8 六处文件。

- ✅ **创建新 skill**(2026-07-30):[skills/action-questionnaire/](skills/action-questionnaire/)——SKILL.md + 引擎副本×2(含 W00 节改 confirm-list)+ DESIGN.md(15 题裁决全录 + 被否决项 + 漂移声明 + dogfood 范围);脱敏门 0 命中。15 题裁决落实:① 独立新 skill;② 阈值 ≤4(经验估值待校准);③ preview 更名 confirm-list 改确认式;④ confirm-list 为主、正式题波兜底;⑤ 铁律 2 环境现实验证;⑥ 归档留痕 + 三条件升格;⑦ 非正式行动写操作默认确认;⑧ delegate 显式声明继承白名单才豁免;⑨ 隐式骨架六要素终止判据;⑩ 不嵌入 long-running、feature 级转出提醒;⑪ 1 轻量 dogfood 案例作同步门槛;⑫ 引擎第 4 份副本含 W00 节 + 有意分叉声明(OD-11)
- ✅ **命名定 `action-questionnaire`**(2026-07-30,Q14 自定义「action *」解读为 action 前缀 + 问卷族后缀;改目录名双向门可逆)
- ✅ **canonical 同步(7→8)**(2026-08-03,confirm-canonical-sync-7to8-w00 全确认执行):门槛 2026-07-31 已过(action-Q 首案例,见下节🟡);6 文件 7 处全部落地——methodology_v3(§快速上手/§8.3 分类表加「确认」行)、README×2、CLAUDE.md、CONTEXT.md、ADR-0003、OD-2 计数重测(Ask 18 / sub 4);连带修订:CLAUDE.md 状态节刷新至 2026-08-03、OD-13 触发②「第 8 个」措辞、README/v3/CLAUDE 三处 mermaid 图补 action-Q 节点

### 🟡 skill 家族生态位分析产出(action-Q 首次 dogfood,2026-07-30/31)

> 来源:[confirm-skill-niche-overlap-w00](harness/questionnaires/archive/_misc/confirm-skill-niche-overlap-w00.md)。结论:7(+1) skill 无真重叠(三件套 = 连续体 + 交互轴分工);grill 家族不可替代性退守三残差(深依赖链 / 即时反馈偏好 / 零留痕)。
> 本 dogfood 案例同时是上节「canonical 同步(7→8)」的门槛案例——D-1 回修完成 + DESIGN.md 记录后门槛过关。
> 核验时机:F1–F4 下次修订对应文件时逐项核对;F6 以 grill-Q 压测完成清单为准。

- ⏳ **F1 grill / grill-with-docs SKILL.md 路由表补 grill-Q**(pasted-plan 场景无路由;grill 的 supporting-info 仅对比 with-docs)——挂 OD-12(grill 处置重估时一并处理)
- ✅ **F2 grill-Q description「同用途不同交互」措辞修订** —— 2026-08-01 被 R5 吸收执行(80/20 层位表述替换)
- ✅ **F3 v3 §5.3 两族表落盘行拆分 grill vs with-docs** —— 2026-08-01 被 R2 吸收执行(落盘行拆分 + 「判断成本层位」行新增)
- ✅ **F4 v3 §8.3 触发词表补「计划评审」裁决轴** —— 2026-08-01 被 R7 吸收执行(二八判据分流)
- ⏳ **F6 重估 §5.2 / 合并 grill 家族** → 转 grill-Q 压测(W01 已生成);**2026-07-31 W01 作废**(用户裁决):「合并」框架被「grill-Q 原初设计意图(80/20 原则 + 忠于 with-docs 问卷化演进,减少判断成本)」取代,由「生态位区分」行动承接([confirm-grill-niche-distinguish-w00](harness/questionnaires/archive/_misc/confirm-grill-niche-distinguish-w00.md))
- ✅ **D-1 回修 action-Q PROCESSING-RULES 补充声明第四类**(2026-07-31 完成:解析规则 3 + FORMAT 规则 12 补「用户先验结论 → 待验证假设」;repo + 用户级双副本同步;头部分叉声明 #4 + DESIGN.md 有意分叉 #6;用户小波裁决「只改 action-Q」,canonical 未动)
- ✅ **R1–R9 生态位区分文档修订(深度 A)**(2026-08-01,[confirm-grill-niche-doc-revisions-w00](harness/questionnaires/archive/_misc/confirm-grill-niche-doc-revisions-w00.md) 全勾确认):80/20 判断成本原则落 v3(§5.2 保留段改写 / §5.3 两族表层位行+落盘行+选择原则 / §4.2 环节 2 层位与交接 / §8.3 触发词二八分流 / 附录 C 续行)+ CONTEXT Grill 家族节 + grill-Q & with-docs description 层位正名 + grill-Q DESIGN.md 原初原则补记;skill 三文件双副本同步;脱敏扫描发现 OD-4 既有真实名命中(见下,非本次引入)
- ✅ **脱敏门修复(2026-08-01,用户授权选项①+③)**:OD-4 行 47 真名改占位 + tip 提交 amend(b16328e,信息+内容同修;OD-1/OD-12 随 amend 并入);提交内与工作区复扫均 0 命中。流程改进已落:OD-1 占位方案 ② 纳入「git 提交信息」人审(扫描盲区,本次即实例)
- ✅ **脱敏语义人审(subagent×4 全文遍历,2026-08-01)**:🔴0 阻断;技术栈指纹(真实库名/内部 ADR 编号)4 处泛化、取证指针 1 处弱化、单字母「A」正字「作者」、ADR-0001 描述词 2 处删除;方法论 v2 移入 archive/ + 3 处断链修复
- ⏳ **git author 身份决策**(人审遗留):已推送 5 提交携带作者邮箱(QQ 号)+ handle(handle 在脱敏映射表内);选项:接受现状 / 改 git config 止血未来提交 / 历史改写 + 强推(单向门级,破 fork/clone)。建议至少做 config 止血
- ⏳ **已推送历史中的语义指纹**:skills 技术栈细节与 OD-7「另一公开项目」链已随首次推送公开(本轮已 fix-forward);历史是否改写与上一项一并决策

### 🔵 AI 双轨对照 pilot + 问卷默认勾选试点(grill-Q ai-autonomy W01/W02 压测产出,2026-08-01)

> 来源:[grill-ai-autonomy-w01](harness/questionnaires/archive/ai-autonomy/grill-ai-autonomy-w01.md)+ [w02](harness/questionnaires/archive/ai-autonomy/grill-ai-autonomy-w02.md),共 18 题全答,0 逃生舱。压测对象:用户双轨构想(影子模式 + 冠军挑战者)与 skill 改动提案。裁决落 [OD-13](docs/OPEN-DECISIONS.md)(双轨 pilot 立项,含 W02 补正)/ [OD-14](docs/OPEN-DECISIONS.md)(默认勾选试点,5 条边界)。
> 核验时机:各行动完成后,核对是否满足 OD-13/OD-14 的边界条款(单向门豁免 / 选项排序 / 取消率设防 / 禁区保留 / mode: full 底线不变)。

- ✅ **shadow pilot skill 创建 + 首轮 dogfood**(2026-08-01 创建;2026-08-03 首轮反馈沉淀):`~/.claude/skills/shadow/`(SKILL.md + DESIGN.md)——先影子后真实、影子 = 自动 dogfood 不设 N、subagent 仅双轨、权限 = delegate `mode: full` 排除集、验收 = 事前 DoD + 端到端测试 + 人仲裁、日志脱敏(绝对路径 → `~`,相对路径引用允许)。**暂不入家族**(OD-13,家族化 = OD-13 重访触发②);仓库 skills/ 暂不放置(pilot 期不进入分发面)。首轮 dogfood(DOGFOOD 沙盒 shapez-game-test):**「AI 自评可玩 ≠ 人类可玩」实证 + 价值定位调为模板/demo + 升级条件化(人试玩通过)**,数据落 OD-13
- ✅ **design-Q 默认勾选试点执行**(2026-08-01,用户授权执行):QUESTIONNAIRE-FORMAT(W00 预勾 + 选项排序 + 问题级排序 + 单向门豁免)+ PROCESSING-RULES(默认勾选设防节:取消率 / 确认点 / 3 波零取消回退)+ SKILL.md(W00 段/作答/统计);用户级 + 仓库级双副本同步(脱敏差异保持);只改 canonical,四副本同步留 OD-8 重访(OD-14)
- ✅ **delegate 多模式执行**(2026-08-01,用户授权执行):SKILL.md「全权模式(mode: full)」节(白名单反转排除集,底线 + 留痕不变)+ delegation-template.md frontmatter `mode` 字段 + 实测条款「实测(只读)可自主、归类仍交人/入排除集」;双副本同步(OD-13 W02 Q3/Q4)
- ✅ **日志脱敏规则**:已落 shadow SKILL.md 铁律 5 + 落盘表(绝对路径 → `~`,不进公开仓库)(OD-13)

### 🟣 design-Q skill 规格整理(grill-Q skill-spec-revamp W01 压测产出,2026-08-06)

> 来源:[grill-skill-spec-revamp-w01](harness/questionnaires/archive/skill-spec-revamp/grill-skill-spec-revamp-w01.md),11 题(9 认定/部分认定 + 1 不认定 Q9 + 0 逃生舱)。压测对象:design-Q skill 规格整理设计套([VISION](harness/design/skill-spec-revamp/VISION.md) / [HLD](harness/design/skill-spec-revamp/HLD.md) / [LLD](harness/design/skill-spec-revamp/LLD.md))。D1–D8 全覆盖(D3 预审:HLD H2 被否决项充分)。9 项为**设计套(工件)修订建议**——修订完善后进 long-running 实现(P1–P4)。
> 核验时机:设计套修订执行后逐项核对;long-running 实现前设计套须含全部修订。
> **✅ 9 项全执行(2026-08-06/08-07)**:Q3/Q5/Q6/Q1+Q10/Q2/Q4/Q8/Q11 → [LLD](harness/design/skill-spec-revamp/LLD.md)(重写整合,🔧 标注)+ [HLD](harness/design/skill-spec-revamp/HLD.md)/[VISION](harness/design/skill-spec-revamp/VISION.md)(Q6 回灌);下述各项 ⏳ 已随本次执行落地(等价 ✅)。**✅ Q7(retro 落点 + 路径区分)grill-with-docs 深钻定案**——retro 文档项目固有 docs/retro/、落盘根边界 = design/questionnaires/adr 三件、skill 内部 vs 宿主路径区分规则,结论落 LLD 2.6。

- ⏳ **Q3 long-running 改动遗漏**(D5+D7,认定):LLD 补 long-running SKILL.md 改动(§5.3 读归档问卷路径配置化)+ HLD/LLD 对齐——long-running 确读归档(已核实 §5.3),非仅 .claude/feature_list
- ⏳ **Q5 P3 diff 0 vs OD-8**(D4+D7,认定):LLD P3 DoD 界定「diff 0 仅指落盘映射节,不含各副本有意分叉区(action-Q 小波阈值/confirm-list、grill-Q stage 标记)」——防 P3 执行破坏 OD-8
- ⏳ **Q6 无 CLAUDE.md 项目**(D5,认定):方案 R SKILL.md 路径决定第 1 步加「CLAUDE.md 不存在则跳过声明识别,直接默认 harness/ + 落盘前确认」
- ⏳ **Q7 retro 落点 + 路径区分**(D5+D7,认定 + 耦合项):① retro 复盘文档落点归属定(项目固有 docs/retro/ 还是 harness/);② 四副本同步规则补「只改宿主项目落盘路径,skill 自己 SKILL.md/DESIGN.md 引用的 skill 目录内部 docs/ 不动」——**建议转 grill-with-docs 单点深钻(用户标注耦合项)**
- ⏳ **Q1+Q10 声明关键词漏读**(D1+D2,部分认定):SKILL.md 关键词清单标注「非穷举,确认点兜底」+ 落盘前确认提示「未命中声明,将用默认 harness/(显示命中/未命中哪条关键词)」
- ⏳ **Q2 最小必含形式主义**(D1,部分认定):STAGE-SKELETONS 头部反简化声明强调「约束内容非仅结构(可被实现期直接执行,非占位/非『见后』)」
- ⏳ **Q4 确认疲劳**(D4,部分认定):每波处理报告顶部标注「落盘根 = X(首次确认于 Wnn)」,用户每波可见可纠
- ⏳ **Q8 机制回归可验证性**(D6,部分认定):机制回归补可脚本化子检查(生成测试问卷后 grep frontmatter 字段齐全 / grep 🤔 逃生舱每题在位),人跑 + 脚本核
- ⏳ **Q11 落盘根定义显式化**(D8,部分认定):「落盘根」在 design-Q PROCESSING-RULES 落盘映射节显式定义(已隐含),四副本同步扩散;不进 CONTEXT(skill 机制词)
- ✅ **Q9 P4 跨项目验证**(D6,不认定):L5 已说「临时沙盒」,执行时自定即可,无需 LLD 细化

### ⚪ design-Q 未验证假设生命周期管理(2026-08-07,action-Q 确认)

> 来源:[confirm-design-q-unverified-assumptions-w00](harness/questionnaires/archive/_misc/confirm-design-q-unverified-assumptions-w00.md)(W00 15 条确认 + 小波:复用前重验扩散到 action-Q)。缺口:design-Q 验证纪律锚定「出题时」,构想 / 需求随问卷演进,早期未实测信息可能在下一阶段成为规划支撑。机制已落:design-Q SKILL.md §1(台账 + 复用前重验)+ §5(闸门汇报)+ DESIGN.md D27–D30;action-Q SKILL.md 第 1 步(复用前重验)+ DESIGN.md 扩散记录;双副本同步。
> 核验时机:后续真实 design-Q 流程中 dogfood——核对台账落点(处理报告节)与闸门汇报是否如规格运转;机制覆盖度不足或形式主义冒头时回修订。

- ✅ **机制落盘**(2026-08-07):design-Q + action-Q SKILL.md / DESIGN.md 双副本同步完成
- ⏳ **dogfood 验证**:首次真实 design-Q 流程走新机制(台账收集 → 闸门汇报),核对可执行性

### 🟤 harness 文件管理规格压测(grill-Q harness-file-mgmt W01 产出,2026-08-08)

> 来源:[grill-harness-file-mgmt-w01](harness/questionnaires/archive/harness-file-mgmt/grill-harness-file-mgmt-w01.md),14 题(用户以补充声明定向,未逐题勾选)。压测对象:skill 家族 harness 文件管理规格(ADR-0011 硬编码 + 各 SKILL.md 落盘路径)。**用户裁决(补充声明)**:① harness 文件严格归 `harness/` 父级 + 父级下子文件夹分层,**不污染项目根**;② 设计 doctor-for-harness skill 处理演进中的文件迁移/规范;③ 格式反馈:单波次上限 10、直接问答上限 3。
> 立项见 [OD-15](docs/OPEN-DECISIONS.md)。核验时机:✅ 4 项全部执行,逐项核对落地。

- ✅ **doctor-for-harness skill 设计**(2026-08-08,commit 7310dd0):设计套 VISION/HLD/LLD + ADR-0012/0013 + OD-15 更新;分层落地作为其第一个治理任务
- ✅ **harness 分层迁移执行**(2026-08-08,F019,commit 5a0221a):design/ 已天然分层(ADR-0012 判定句确认),本次实为确认 + 归档链接修复(9 处层级链接 + 3 处豁免)
- ✅ **harness 分层落地**(2026-08-08,commit c825e75):41 份归档按 feature/主题迁入 10 子目录(methodology/repo-design/skill-spec-revamp/doctor-harness/skills-harness-consistency/ai-autonomy/preaction-confirm/merge-grill-family/harness-file-mgmt/_misc)+ [archive/README.md](harness/questionnaires/archive/README.md) 索引;HARNESS-RULES 第四节「存量不挪」→「允许整批迁移」;断链回归 0 新增 + harness-check 0 违规
- ✅ **格式反馈落地**(2026-08-08,commit 630fe85):单波次上限 10、小波阈值 ≤3 四副本统一(OD-11 分叉修订)+ MIGRATION-FLOW 迁移流程文档

### 🟠 doctor-for-harness 设计套压测(grill-Q doctor-harness W01 产出,2026-08-08)

> 来源:[grill-doctor-harness-w01](harness/questionnaires/archive/doctor-harness/grill-doctor-harness-w01.md),10 题全认定(A)。压测对象:doctor-harness 设计套(VISION/HLD/LLD + ADR-0012/13)。可沉淀项已落 [OD-16](docs/OPEN-DECISIONS.md)(可选档重访)/ [OD-17](docs/OPEN-DECISIONS.md)(使用率验证)。下述 7 项**工件修订建议已全部执行**(2026-08-08,用户授权,commit 2629e2f)。
> 核验时机:✅ 已执行,逐项核对落地。

- ✅ **Q1+Q8 校验脚本补 design/ report 模式**:harness-check.py 加 report_design_layout(列裸放/子目录现状,不判对错);HLD 选型表补 report 被否决项
- ✅ **Q2 LLD「四节」→「五节」**:LLD 三处 + DoD grep 同步
- ✅ **Q3 ADR-0013/LLD 回灌 F019 实证**:补「design/ 已天然分层,本次实为确认 + 归档链接修复」
- ✅ **Q4 豁免清单同步义务**:harness-check.py EXEMPT_PREFIXES 注释 + HARNESS-RULES 第三节
- ✅ **Q6 HARNESS-RULES 归属校验归属明示**:第二节补「各 skill 落盘前执行,doctor-harness 只给判据」
- ✅ **Q7 dogfood 通过定义**:doctor-harness DESIGN.md 补定义(F019 符合)
- ✅ **Q10 HARNESS-RULES 补「布局合规」定义**:第五节补(脚本可查三检查 + 分层人工判据)

### ✅ 哲学 v4 系统工程视角压测修订包(grill-Q philosophy-v4 W01 产出,2026-08-10,已执行)

> 来源:[grill-philosophy-v4-w01](harness/questionnaires/archive/methodology/grill-philosophy-v4-w01.md),10 题(9 题选 C 推荐 + Q7 澄清为「新开精简小节」),0 逃生舱。压测对象:哲学 v4(canonical),从运筹学 / 人因工程 / 软件工程三学科视角压测。**10 项哲学修订建议已全部执行(用户授权,2026-08-10)**:philosophy_v4.md 8 处 + methodology_v4.md 2 处(§2.1 两套尺度 + §5.2 题量同步);CONTEXT 学科注记 2 处;无新增 ADR/OD(Q9 复用 OD-13)。验证:旧措辞全改 / 新增内容在位 / 脱敏门 0 命中 / 历史 archive 母本不动。
> 核验时机:✅ 已执行;遗留 = OD-4 母本同步(见下)。

- ✅ **Q1 80/20 降格表述**(运筹/D1):哲学 §7.1「运筹学注脚」→「经验启发式(类 Pareto,非定理,无量化模型)」+ 诚实标注事后补述
- ✅ **Q2「决策并行化」措辞精确化**(运筹/D7+D8):哲学 §1.3「决策本身被并行化」→「减少 LLM 串行往返;判断仍逐题串行」
- ✅ **Q3「规划成本可忽略」软化带阈值**(运筹/D1+D4):核心论断 →「相对返工通常较小,但随深度边际递增,过阈值产生形式主义」
- ✅ **Q4 情境意识 / 心智模型拆分双挂**(人因/D8):哲学 §一 拆分双挂;CONTEXT 学科注记已落
- ✅ **Q5 有效上下文两套尺度**(人因/D1):methodology §2.1 + CONTEXT 区分 token 尺度 vs 人认知负荷,标注不可换算
- ✅ **Q6 返工归因加限定 + 被否决项**(软工/D1+D3):哲学 §1.2「信息断层是主要归因」+ 被否决归因(AI 能力边界 / 需求漂移 / 集成意外)
- ✅ **Q7 AI 能力天花板盲点**(软工/D5,澄清为「新开精简小节」):哲学 §一 新增 §1.4「信息流转框架的边界:AI 能力天花板」
- ✅ **Q8 题量数字修正(确凿)**(软工/D7):哲学 §1.3 + 失败模式表「10–15」→「上限 10」+ methodology §5.2 同步(历史 archive 母本不动)
- ✅ **Q9 shadow 双轨 pilot 状态标注**(运筹/D4):哲学 §7.2 加「状态注:pilot 阶段,首轮实证 AI 自评 ≠ 人类可用,价值待定,非已验证方法」
- ✅ **Q10 核心论断代理指标 + 学科挂接诚实标注**(软工/D6):核心论断补代理指标(返工率 / 工时作 retro 自评项)+ 顶部学科挂接标注阐述性借用非经验证
- ⏳ **OD-4 母本同步(仓库外动作,待用户执行)**:W01 + W02 两批 v4 内部修订(未升 v5,共 philosophy 15 处 + methodology 3 处 + CONTEXT 2 处),作者其他位置的 v4 副本内容与本仓库 v4 漂移;需重审 OD-4 策略——同步改副本 或 接受漂移至 v5。属仓库外动作,agent 不代执行。

### ✅ 哲学 v4 压测 W02(§六分工表 + §6.2,2026-08-10,已执行)

> 来源:[grill-philosophy-v4-w02](harness/questionnaires/archive/methodology/grill-philosophy-v4-w02.md),8 题全选 C,0 逃生舱。补压 W01 未审视的 §六分工表 + §6.2 AI 替代角色。**8 项已全部执行**(用户授权):philosophy 7 处 + methodology §十 1 处。无新增 ADR/OD/CONTEXT(Q2 复用 delegate/OD-13,Q5/Q7 指向 §七 + delegate)。验证:8 处在位 / 脱敏 0 / harness-check 0 违规。
> 核验时机:✅ 已执行;OD-4 母本同步并入上一节同一条(本批同属 v4 内部修订)。

- ✅ **W02-Q1 代码审查签字权**(软工/D1+D7):分工表代码审查行 人✅签字权 / AI✅辅助发现问题 + 图例脚注
- ✅ **W02-Q2 白名单单向门风险**(软工/D2):分工表后加「误纳入单向门类(删除/发布/付费/对外传播)+ 禁区清单防线(见 delegate/OD-13)」
- ✅ **W02-Q3 上下文管理拆分**(人因/D1+D8):分工表行拆「决定给人✅ / 执行(检索·压缩·加载)给 AI✅」
- ✅ **W02-Q4 分工表图例脚注**(软工/D6):✅主导 / 辅助 / 执行 / 审阅 / 签字权 最小操作定义
- ✅ **W02-Q5 §6.2 红利来源精确化**(运筹/D1+D5):「消除人际等待与传递失真 vs 单人多任务」+ 单人串行约束
- ✅ **W02-Q6 §6.2 被否决项**(软工/D3):补「保留人工角色 / 部分替代(关键判断仍人)」
- ✅ **W02-Q7 §6.2 单人认知负荷代价**(人因/D4):「判断密度全压单人 → 对策 80/20 分层 + delegate 下放」
- ✅ **W02-Q8 §十「1–2 人」→ 个人开发者**(软工/D7,确凿):与 v4 受众收窄同步

### 🔶 哲学 v5 立论重构(grill-Q discipline-mapping W01 补充声明,2026-08-10)

> 来源:[grill-discipline-mapping-w01](harness/questionnaires/archive/methodology/grill-discipline-mapping-w01.md) **补充声明**:用户提议「开新版哲学文件(philosophy_v5)+ 安全科学升支柱级 + 强调去 AI 黑盒」。这超出 grill-Q(压测)范围,是 **design-Q 级(生成式立论设计)**。grill-Q W01 的 10 项决策(分层策略 / 机制判据 / CONTEXT 学科地图 / OD 回顾)已落 [ADR-0014](harness/adr/0014-discipline-mapping-strategy.md) + [CONTEXT「项目学科地图」节](docs/CONTEXT.md) + [OD-18](docs/OPEN-DECISIONS.md);Q1 哲学挂接 + Q3 元原则注记等哲学正文修订**不在 v4 落地,转 v5**。
> 核验时机:v5 design-Q 设计套产出后,按 P3(类比 v3→v4)执行。

- ✅ **grill-with-docs 深钻「去 AI 黑盒」立论锚点完成**(2026-08-10,6 点结晶):① 黑盒=三层次(过程不透明 / 依据不可追溯 / 结果不可独立验证);② 与第一支柱正交(独立维度);③ 风险=三坏后果(潜伏沉积 / 失控放大 / 信任劫持);④ 对策=统合已有可审计装置 + 形式化 V&V 缺口留 [OD-19](docs/OPEN-DECISIONS.md);⑤ 度=弹性边界(WAI 定底线 / WAD 留空间);⑥ 过程模型术语冲突=区分命名(STAMP 用全称「安全控制过程模型」)。结晶落 [CONTEXT「AI 黑盒」节](docs/CONTEXT.md) + [OD-19](docs/OPEN-DECISIONS.md)。

### 🔷 philosophy_v5 design-Q(feature-philosophy-v5,2026-08-10 进行中)

> 来源:grill-Q discipline-mapping + grill-with-docs 去黑盒深钻 → design-Q v5。设计套 [harness/design/philosophy-v5/](harness/design/philosophy-v5/)。完整档 vision→hld→lld。
> 核验时机:各阶段闸门 + v5 起草后 DoD。

- ✅ **vision 阶段完成**:W00 全采纳(15/15)+ W01 小波(2 题);[VISION](harness/design/philosophy-v5/VISION.md) 落盘
- ✅ **hld 阶段完成**:W00 全采纳(16/16);[HLD](harness/design/philosophy-v5/HLD.md) 落盘 + [ADR-0015](harness/adr/0015-deblackbox-anchor.md)(去黑盒独立锚点)
- ✅ **lld 阶段完成**:W00 全采纳(12/12);[LLD](harness/design/philosophy-v5/LLD.md) 落盘(起草 6 步 P1–P6 + §八 七小节 + DoD)
- ✅ **设计套压测完成**(grill-Q philosophy-v5-design W01):10 题全 C;10 项设计套修订执行(HLD 4 + LLD 6,write→review 闭环);归档 [grill-philosophy-v5-design-w01](harness/questionnaires/archive/philosophy-v5/grill-philosophy-v5-design-w01.md)
- ✅ **起草 philosophy_v5 完成**(2026-08-11,long-running,commit 530d0f4):LLD P1–P5 落地(顶部声明 / §八 新增 / §2.2·§十一 注脚 / 元原则表 / canonical 切换);**P6 = OD-4 母本同步(仓库外)仍 ⏳**,见文件头「下一步主线」

### 🔶 grill-Q philosophy-v5 成稿压测修订包(2026-08-13,**已全部执行**)

> 来源:[grill-philosophy-v5-w01](harness/questionnaires/archive/philosophy-v5/grill-philosophy-v5-w01.md)(10 题:Q1 选 A 改名「第四学科视角」,Q2–Q10 全 C;0 逃生舱;补充声明「关键术语采用中英文」= 修订句中学科关键术语中英文并置)。2026-08-13 用户授权全部执行。
> 核验(2026-08-13 执行后):living 文档旧名 0 残留(留痕/历史记录除外)+ 脱敏门 0 命中 + harness-check 0(exit=0)+ 新增 ADR/OD 链接目标在位。

- ✅ **Q1 改名包「第五 → 第四学科视角」**(用户选 A,推翻推荐 C):philosophy_v5 顶部 + §8.2;ADR-0015 文首更名注记(原文保留);ADR-0014 v5 待定节注记;CLAUDE.md 5 处;README 2 处;CONTEXT 4 处;**设计套(harness/design/philosophy-v5/)与归档问卷 4 份 = 历史原貌不改**
- ✅ **Q2 §8.1 L3 双向精确化**:客观裁决源(oracle:编译 / 测试 / E2E)存在但常 AI 自写(嵌套黑盒,OD-13 实证);判断类产出只能人审;CONTEXT L3 定义同步
- ✅ **Q3 §8.4「黑盒被打开」→「黑盒被制衡,未被完全打开」**(L1 零对策 + 留痕 = AI 自陈);CONTEXT 对策方向同步
- ✅ **Q4 §8.5 末补最小代理指标**(retro 抽查决策依据可重建性,与 §一 同级)
- ✅ **Q5 §8.5 补 WAD 跨主体限定句**(AI 灵活调整含幻觉补全风险;WAD 仅限纯执行 / 可逆;批量留痕 = 有界潜伏窗口,retro 收口)
- ✅ **Q6 §8.3 信任劫持条补循环承认 + 缓解组合**(80/20 压成本 + WAI 底线 + retro 复核;底线 creep 靠 retro 识别)
- ✅ **Q7 §8.4 装置清单补 retro 复盘 + long-running 留痕**(CONTEXT 对策方向同步)
- ✅ **Q8 §八 引言补 ADR-0014/0015 链接行**(立锚决策与被否决项可追溯)
- ✅ **Q9 WAI/WAD 全称**:CONTEXT 注记 + §8.5 首现带全称(Work-As-Imagined / Work-As-Done)+「弥合 WAD 缝隙」→「弥合 WAI–WAD 缝隙」
- ✅ **Q10 §8.3「致灾」语境映射**(= 单向门事故:误删 / 误发布 / 付费 / 外泄)+「dysfunctional 交互致灾」→「系统层交互失控致灾」
- ✅ **TODO 卫生**:「起草 philosophy_v5」改 ✅(P1–P5 落地,P6 = OD-4 母本同步仍 ⏳ 见文件头);「三文件」块内重复条目销项改 ✅
- 观察项(仅记录):① 设计压测 Q4 示例「元原则表点名 Reason 潜伏条件」实际未执行(现为合并行、已指向 §八,可辩护);② methodology §5.2 标题「一问一达」疑为「答」typo(属方法论工件,改会破锚点,转方法论修订时一并评估)——**2026-08-13 W02 Q10 裁决修理,见下块**

### ✅ grill-Q philosophy-v5 成稿压测 W02 修订包(2026-08-13,已执行)

> 来源:[grill-philosophy-v5-w02](harness/questionnaires/archive/philosophy-v5/grill-philosophy-v5-w02.md)(10 题全选 ★推荐项 + 提问波 2 题,0 逃生舱,补充声明空)。焦点:修订后复压 + 跨文件一致性 + 治理空白。2026-08-13 用户授权「立即执行全部」。
> 核验(2026-08-13 执行后):修订点 9 项 grep 全中 / 旧表述清零(「一问一达」「2–3 倍」「可以忽略不计」「考量三方」「只用 grill-Q + VISION」living 0 残留)/ 锚点新 slug 4 处一致 / 脱敏 0 / harness-check exit=0。

- ✅ **Q1 §1.2 口径对齐 +「2–3 倍」软化**(D7+D1):「可以忽略不计」→「通常较小」(同核心论断);「2–3 倍」→「数倍(经验量级)」
- ✅ **Q2 §6.2 DevOps 行补单向门指向**(D2+D4):「(部署执行属单向门类,防线见 §6.1 白名单脚注)」
- ✅ **Q3 CONTEXT Grill 家族节补 action-Q**(D7+D8,处理时即刻落盘):批量问卷族第四成员 + confirm-list 注记;哲学 §7.1 不动
- ✅ **Q4 §8.1 三 bullet 补 L1/L2/L3 标签**(D8);CONTEXT「①②③ = L1/L2/L3」注记(处理时即刻落盘)
- ✅ **Q5 §8.5 代理指标补静默期变体**(D4+D6):「若本周期无 AI 决策故障,随机抽一例近期 AI 决策做重建抽查」
- ✅ **Q6 元原则表引擎漂移行「三方」→「四方(design-Q/grill-Q/retro-Q/action-Q)」**(D7)
- ✅ **Q7 元原则原型流程言明**(D5+D1):「原型项目可精简为:手写 VISION + grill-Q 压测(跳过 design-Q 三阶段)」
- ✅ **Q8 CONTEXT 补「canonical 审查」定义**(D8+D6,处理时即刻落盘);哲学顶部措辞不动
- ✅ **Q9 发布后修订留痕纪律**(D2+D3+D5):顶部新增「修订记录」行(一行一级;W01 9 处首例补记 + 本批 10 处)
- ✅ **Q10 methodology §5.2 标题 typo + 锚点同步**(D7+D8):「一问一达」→「一问一答」;锚点同步实改 3 处(哲学 2 + practical 1,比问卷估计多 1 处);living 清零(TODO/问卷留痕除外)
- ✅ **小波 Q1 嵌套黑盒对策挂接**(提问波「两侧各补一句」):§8.4 缺口注记补「人审测试本身 + 人试玩验收(OD-13 升级仲裁)」+ §6.1 E2E 行注「(测试若 AI 自写 = 嵌套黑盒,人审/试玩兜底,见 §8.1 L3)」
- ✅ **小波 Q2 元原则「双人团队」不修**(提问波,选不修):条件句与 §零「1–5 人可参考」兼容,数字非承重墙;避免引入跨文件 § 引用

### ✅ grill-Q philosophy-v5 成稿压测 W03(2026-08-13,已执行;问卷待归档)

> 来源:[grill-philosophy-v5-w03](harness/questionnaires/archive/philosophy-v5/grill-philosophy-v5-w03.md),10 题全答,0 逃生舱,0 自定义。焦点:W02 执行后的跨文件冲突、概念边界与当前工作树发布状态。用户于 2026-08-13 授权执行全部修订。
> 核验(2026-08-13 执行后):Q1–Q10 修订项已落 living 文档;脱敏 0 命中;harness-check exit=0;旧活措辞清零。问卷处理摘要已归档。

- ✅ **Q1 OD-4 canonical 口径收口**:当时占位方案改为 methodology_v4 + philosophy_v5;历史拆分叙述降为历史裁决;重访触发更新为任一 canonical 成员升版、母本变化或同步策略变化。当前 canonical 哲学文件后来由 v6 接替,现已由 v7 接替;见本文件对应版本条目。
- ✅ **Q2 五环节衔接统一**(用户选 B,非推荐 C):统一为 `design-Q → grill-Q → dogfood → long-running → retro-Q`,同时保留 retro 可任意插入的横切说明,同步 methodology / CONTEXT / README。
- ✅ **Q3 WAD 留痕边界**:哲学 §8.5 改为执行路径可灵活,但已发生的自主决策不得延迟留痕;批量或事后记录仅限非自主决策或预先声明的抽样。
- ✅ **Q4 审计装置状态诚实化**:哲学 §8.4 将「项目已有」改为「项目已定义/可用」,并区分启用与 dogfood 验证状态。
- ✅ **Q5 量化修辞证据边界**:哲学 §1.2 保留「数倍」与「一小时 / 三天」作为作者经验性示例,明确非项目测量结论,并连接返工率 / 返工工时占比代理指标。
- ✅ **Q6 CONTEXT 与哲学术语统一**:新增「判断性决策 / 纯执行类决策」定义,哲学核心句改为「AI 不能自主做判断性决策」。
- ✅ **Q7 Safety-II 跨主体边界**:哲学 §8.5 将 WAD 限定为按批准规格调整执行细节,明确不把人的情境适应能力归因给 AI;Safety-II 只作边界启发,不作因果证明。
- ✅ **Q8 修订状态语义拆分**:哲学头部只记录已提交 / 已发布版本;工作树执行记录留在 TODO / 问卷处理摘要。
- ✅ **Q9 L3 最小验证分流**:哲学补分层原则,实操文件补最低验证表:AI 自写 oracle、用户可玩产物、单向门操作要求人审 / 试玩 / 确认,纯执行可逆项允许抽样复核。
- ✅ **Q10 按用户裁决保留具体名**:哲学 §8.4 保留 `Code Review 人审(pr-review「AI 永不 approve」)`,并注明本仓库当前没有同名 active skill,具体工具由实操层接入。
- ✅ **Q7 深水区候选暂不触发**:本轮已将 Safety-II 适用范围收窄为边界启发;若后续仍需论证其对 AI 执行者的理论适用性,再转 `grill-with-docs` 单点深钻。

### 🔶 三文件层级化治理(宪法→基本法→地方法)— v5 后单独立项

> 来源:philosophy-v5 vision W01 小波补充声明(2026-08-10)。三文件规模不对称:方法论 704 行(基本法)远超哲学 186(宪法)+ 实操 192(地方法);实操停 v1。用户裁决:先内容审计 + 单独立项(不进 v5)。
> 核验时机:v5 完成后立项。

- ⏳ **方法论 704 行内容审计**:派 subagent 审计越界 / 冗余(哪些跑到实操 / 哲学范畴、哪些重复),据审计定瘦身
- ⏳ **三文件层级规则**:明确每层职责边界(宪法=原则 / 为什么;基本法=框架 / 怎么做;地方法=操作 / 怎么用),禁止越界
- ⏳ **实操 v1 升版**:与哲学 / 方法论版本对齐(v1→v?)
- ⏳ **立项方式**:v5 后 grill-Q(压测三文件结构)或 design-Q(治理设计)
- ✅ **philosophy_v5 立论重构**(2026-08-11 完成,commit 530d0f4;与上行「起草 philosophy_v5」同义,历史重复条目销项):① 安全科学作为**第四学科视角**(时称「第五」,2026-08-13 更名)进哲学顶部挂接;② 「去 AI 黑盒」立论;③ v4→v5 升版(OD-4 母本同步仍 ⏳,见文件头「下一步主线」)
- ✅ **「第五支柱」已澄清(2026-08-10)**:= **第五学科视角**(安全科学进哲学顶部学科挂接,非第三支柱,不改双支柱结构)

### 🔶 grill-Q philosophy-v5 对标同级仓库 W04(2026-08-13,处理完成;Q1/Q10 分层深度待决)

> 来源:[grill-philosophy-v5-w04](harness/questionnaires/archive/philosophy-v5/grill-philosophy-v5-w04.md)。10 题全答,0 异常,0 逃生舱;Q1 自定义追问「权威分层是什么学科的知识」已在处理报告解释。Q1 选择完整 Level 1/2/3 与 Q10 选择最小治理切片互相冲突,已进 [OD-20](docs/OPEN-DECISIONS.md),未静默裁决。
> 已即时落盘:[ADR-0016](harness/adr/0016-method-claim-assurance-contract.md) 核心主张验证/变更合同;[CONTEXT](docs/CONTEXT.md) harness 术语边界与证据状态/范围。

- ⏳ **方法不变量**:抽取 6–10 条核心不变量,每条补稳定 ID、违反症状、最小证据、例外边界、唯一权威;核验时机 = 首批验证卡完成时。
- ⏳ **最小验证卡**:为核心主张记录适用范围、反例、代理指标、独立证据、阈值/重访条件;核验时机 = 首轮方法论 dogfood / retro。
- ⏳ **方法级失败处理骨架**:把「影响范围 → 暂停不可逆动作 → 保留事实/副作用 → 恢复/回滚 → 复盘更新」转成哲学修订建议,由用户另行授权后执行;核验时机 = 下一次 canonical 修订。
- ⏳ **核心主张变更清单**:canonical 或不可逆治理变化前记录唯一权威、受影响引用/skill、不变量影响、验证和当前/提交/发布状态;核验时机 = 下一次 canonical 修订。
- ⏳ **AI 替代角色措辞收窄**:把「替代角色」明确为替代可结构化执行任务与等待链,补能力前提和失败升级路径;核验时机 = 下一次哲学 canonical 修订。
- ⏳ **三文件层级审计**:完成既有方法论/哲学/实操文件的越界与重复审计,据此再处理 OD-20 的完整分层 vs 最小切片问题;核验时机 = 审计报告完成。

### ✅ feature-philosophy-governance · 将 Harness 治理经验纳入哲学(2026-08-13)

> 来源:[feature-philosophy-governance-lld-w00](harness/questionnaires/archive/philosophy-v5/feature-philosophy-governance-lld-w00.md),用户 opt-in 采纳 6/6 默认,并补充要求检查文章结构。落盘前已核对哲学 §八 的递进:定义 → 风险 → 装置 → 弹性边界 → 方法治理合同 → 元原则。

- ✅ **哲学 §8.6 方法治理合同**:纳入最小治理切片、唯一权威、主张 → 不变量 → 验证卡、失败状态与恢复边界、规范/实现/证据分离四点。
- ✅ **范围边界**:明确不复制同级对标仓库的完整 Level 1/2/3 运行时架构,具体状态、接口、测试矩阵和执行记录留在 skill / 实操 / `harness/`。
- ⏳ **后续验证**:首批方法不变量与验证卡仍待建立;核验时机 = 首轮方法论 dogfood / retro。完整文档层级是否展开仍由 OD-20 管理。

### ✅ philosophy_v6 · 哲学治理进化升级(2026-08-13)

> 来源:基于 v5 的结构评审与用户授权。v5 保留为历史版本,[philosophy_v6](docs/methodology/archive/philosophy_v6.md) 曾成为 current canonical,后由 v7 接替;本次不复制同级对标仓库的完整 Level 1/2/3,继续遵守 ADR-0016 与 OD-20 的最小治理切片边界。

- ✅ **行文主线**:顶部补「信息断层 → 返工 → 分工 → 判断资源配置 → 黑盒治理 → 方法论治理」阅读路线;§一→§六、§六→§七、§七→§八、§8.5→§8.6 补过渡句。
- ✅ **治理对象澄清**:§8.6 更名为「方法论自身的治理闭环:从主张到证据」,明确前文治理 AI 执行不透明,本节治理方法论漂移、误读与伪验证。
- ✅ **状态一致性**:新增统一模板「主张 → 适用范围 → 当前状态 → 最小证据 → 失效信号 → 重访条件」,并同步 [CONTEXT](docs/CONTEXT.md)。
- ✅ **学科治理映射**:新增系统/需求工程、认识论/测量科学、配置管理/QMS、认知科学/HCI、知识管理/组织学习、信息安全/威胁建模、形式化方法、控制论/决策理论的「学科 → 治理机制 → 最小产物 → 进入条件」路线图;明确不是八个强制流程。
- ✅ **版本与入口**:AGENTS、CLAUDE、README、methodology_v4、practical_v1、CONTEXT、OPEN-DECISIONS 已切换 v6;v5 移入 `docs/methodology/archive/`。
- ⏳ **后续验证**:首批 6–10 条方法不变量和验证卡仍待建立;先执行系统/需求工程、认识论/测量科学、配置管理/QMS 三行最小切片;核验时机 = 首轮方法论 dogfood / retro。信息安全、形式化方法、控制论等按风险与数据触发。

### 🔶 grill-Q philosophy-v6 W01(2026-08-14,已答;W02 澄清中)

> 来源:[grill-philosophy-v6-w01](harness/questionnaires/archive/philosophy-v6/grill-philosophy-v6-w01.md)。本轮 10 题已作答,无逃生舱,但 Q9 单选多勾;同时发现问卷自身多题存在「选项正文」与「★推荐理由」语义错位,受影响题不作猜测,统一转 W02 重出。原始问卷已处理并归档,答复与处理摘要保留原貌。

- **Q1 明确方向**:用户选择 v7 起将哲学正文改为连续独立编号,同时保留旧章节映射与兼容锚点;兼容策略细节受 Q8 题面歧义影响,转 W02 澄清。
- **Q2–Q8、Q10**:虽有勾选,但推荐项的理由与对应选项正文不一致,无法确认用户采纳的是选项正文还是理由指向的另一选项;不静默解释,逐题转 W02 正确题面重出。
- **Q9**:A、B 同时勾选,属于单选冲突,转 W02 澄清「路线图保留」与「前三行增加进入/退出模板」二者是否合并。
- **补充声明**:用户提出「收窄到哲学与方法论,让两者各自演进又相互挑战」。已新增 [OD-21](docs/OPEN-DECISIONS.md),暂不删除、合并或重命名实操文件;W02 新增该结构治理契约题。
- **问卷质量行动**:W02 重出题目时修正推荐项与理由错位;后续出题自检需同时检查「推荐标记所在选项」与「推荐理由描述的方案」一致。

### ✅ grill-Q philosophy-v6 W02(2026-08-14,处理完成;正文修订已授权并执行)

> 来源:[grill-philosophy-v6-w02](harness/questionnaires/archive/philosophy-v6/grill-philosophy-v6-w02.md)。10 题全答,0 逃生舱,0 自定义,0 单选冲突。W01 的题面歧义已逐题澄清,本轮覆盖 D1–D8 与动态双文件治理议题;不再生成 W03。

- ✅ **Q1**:哲学 v7 顶部补「论证骨架与跨文件入口」,不复制方法论正文。
- ✅ **Q2**:增加判断性决策 / 纯执行类决策的最小判别表与反例;基础术语已存在于 CONTEXT,本轮已补判别契约。
- ✅ **Q3**:采用最小方法级状态协议;已补入 [ADR-0016](harness/adr/0016-method-claim-assurance-contract.md) 的实施边界,不建完整状态机或恢复 API。
- ✅ **Q4**:首批不变量与验证卡在建立前标为「目标治理能力 / 未验证」;不以 ADR 接受替代能力验证。
- ✅ **Q5**:保留无阈值代理指标作为反思提示,暂不新增测量契约,不把哲学变成度量规范。
- ✅ **Q6**:在哲学 §4.6 首次比较同级仓库的位置增加 harness 术语边界。
- ✅ **Q7**:v7 连续编号保留历史映射、兼容别名 / 重定向说明,历史问卷与 ADR 不重写;已记录 [ADR-0017](harness/adr/0017-philosophy-section-compatibility.md)。
- ✅ **Q8**:前三类学科治理映射增加最小进入 / 退出模板;具体行动仍待首批治理切片执行。
- ✅ **Q9**:哲学 v7 增加 current 状态注,允许带已知缺口,并区分目标治理、未验证、反思提示与开放问题。
- ✅ **Q10**:采用哲学 + 方法论 canonical 对等双文件,各自演进且每次 canonical 修订要求另一方交叉审查或 grill-Q 一致性检查;实操保留为非 canonical,已记录 [ADR-0018](harness/adr/0018-canonical-dual-challenge-governance.md) 与 [OD-21](docs/OPEN-DECISIONS.md)。
- ✅ **用户授权后修订包**:用户选择“1”后已全部执行:哲学 v7 连续编号与跨文件导航;CONTEXT 最小判别表与例子;§4.6 harness 边界;v7 current 已知缺口状态说明;前三行学科治理进入 / 退出模板;代理指标反思边界;入口文档与历史文件归档。

### ✅ philosophy_v7 · 哲学连续章节与双文件交叉治理(2026-08-14)

> 来源:grill-Q philosophy-v6 W01/W02;用户选择“1”授权执行全部修订。v6 已移入 `docs/methodology/archive/`,W01/W02 已移入 `harness/questionnaires/archive/philosophy-v6/`。

- ✅ **连续章节与独立入口**:正文统一为 §一至§五;顶部保留旧 v3 → v7 映射、跨文件阅读路线与 [ADR-0017](harness/adr/0017-philosophy-section-compatibility.md) 兼容策略。
- ✅ **治理边界与状态诚实化**:§4.6 增加方法论 harness / 运行时 harness 边界;方法不变量与验证卡标为目标治理/未验证;current 明确不等于全部已验证。
- ✅ **最小切片边界**:前三行学科治理映射获得进入/退出模板;代理指标只作反思提示,不新增测量契约或自动验收门;完整 Level 1/2/3 继续由 [OD-20](docs/OPEN-DECISIONS.md) 管理。
- ✅ **双文件治理**:哲学与 methodology_v4 作为 canonical 对等双文件,各自演进并相互交叉审查;实操保留为非 canonical,见 [ADR-0018](harness/adr/0018-canonical-dual-challenge-governance.md) / [OD-21](docs/OPEN-DECISIONS.md)。
- ⏳ **后续验证**:首批方法不变量、验证卡与前三行模板的 dogfood 证据仍待建立;执行窗口 = 首轮方法论 dogfood / retro。
