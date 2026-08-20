# L0-vision-readme-first-impression.md · README 优化(feature-readme-revamp)

> 导览:① 本层位置与职责 = 目标层(L0 单层交付,2026-08-20 层闸门人拍板,五信号全不中)② 覆盖范围 = 仓库根 README.md 重构 + 根 CHANGELOG.md 新建 + 实操 §8.3 节内 3 处顺手修 ③ 上下游依赖 = 实现期(README 起草)直接按本文件执行,不依赖会话上下文 ④ 契约项声明 = 下文「验收标准」七条与本文件全部结构裁决为实现硬约束;实现偏离走 ADR-0021 治理性偏差路径。
> 裁决来源:[feature-readme-revamp-L0-vision-w00](../../questionnaires/archive/readme-revamp/feature-readme-revamp-L0-vision-w00.md)(2026-08-20,19/19 全采纳,取消默认率 0%,opt-in 预勾开启)+ [grill-readme-revamp-l0-w01](../../questionnaires/archive/readme-revamp/grill-readme-revamp-l0-w01.md) 压测修订 9 条(2026-08-20 用户授权全部执行)。

## 目标与受众

- **第一受众 = 潜在采用者**(个人开发者,想直接把 skill 拿去自己项目用);README 一切内容决策以「能不能快速开始用」为第一优先级。
- **第二受众 = 方法论研究者 / 路过浏览者**:能从 README 理解双支柱立论与体系结构,并找到深读入口(方法论三块 / CONTEXT / ADR)。
- **第一屏 30 秒目标**:读者在第一屏同时获得三件事——① 这是什么(方法论 + 可直接运行的 skill 执行体一体化);② 差异在哪(同类多是「只有文章」或「只有框架」,本仓库是文章 + 执行体一体);③ 怎么开始(安装一行命令 + 最小采用切片指引)。
- **差异化节(「为什么是这个」)扩充**:主张一句 + 被否决对照(纯文章派:知其然不知其行 / 纯框架派:能跑但不知为何)+ 诚实标注「定位待市场验证,见 OD-6」。

## 范围(做什么;明确不做什么)

**做**:
1. 重构仓库根 `README.md`(结构见「实现蓝图」节);
2. 新建 `CHANGELOG.md`(**仓库根**):迁移 README 现有「发布说明」节全部条目(约 63 行)+ 顶部保留「记录规则」+ 顶部首条「README 重构 + 发布说明外移(2026-08-20)」;README 原位置只留链接一行,不留摘要(2026-08-20 grill-Q W01 Q3:摘要 = 三对策未覆盖的永久双写点,去掉)。**位置决策(W01 Q5)**:选仓库根——CHANGELOG 是与 README/LICENSE 同层的对外仓库级文件(GitHub 自动识别),根级属 MIT 治理区 License 归属清晰;被否决:docs/(治理记录混入 CC-BY 区、分区归属模糊、偏离行业惯例)/ harness/(对外文件放内部产物区,门面读者不易发现)。**同名消歧**:`skills/doctor-harness/CHANGELOG.md` 是该 skill 内部演进日志(裁决豁免件),与本文件(仓库对外变更日志)不同层级不同语义;
3. 顺手修 `docs/methodology/practical_v1.md` §8.3 节内**全部** grill 退役残留——实测 3 处(2026-08-20 grill-Q W01 Q1 grep):L133 表格行「单点 | grill / grill-with-docs」拆为 grill-with-docs 含通用模式 / L134 doctor-harness「2026-08-08 入库第 9 个」过期计数删除 / L145 原则段「单点深钻走 grill/grill-with-docs」去 grill,与 README 修订同 commit——理由:README 卡片/速查表将引用实操 §8.3,引用前须先消漂移。

**明确不做**:
- 不动 CLAUDE.md / CONTEXT.md / 方法论三块 / skills(README 与 CLAUDE.md 分工维持:README = 对外门面,CLAUDE.md = 会话工作指令)。**例外**(2026-08-20 grill-Q W01 Q2):CONTEXT「提问维度速查」节头部加一行反向指针(「本表修订时 README 维度速查表必同步」)——同步义务必须挂在触发现场(CONTEXT 修订者读 CONTEXT 自身)才有效,一行机械改动,非范围蔓延;
- 不做英文 README(列为未来可选项,外部反馈出现需求时再议,在 CHANGELOG 记一笔留痕);
- 不加「端到端使用叙事」长节(一天开发走全环节的完整故事)——该需求由协作图 + 卡片触发场景 + 实操 §8.3 时机表链接覆盖;
- 不做装饰性 badge 堆砌(只引入要点 13 的 2–3 枚)。

## 核心场景(新读者旅程)

1. **30 秒**:到达 README 首屏 → 明白是什么 / 差异 / 怎么开始三件事;
2. **3 分钟**:按「快速上手」安装 skill(拷贝或软链)→ 看协作图理解主路径 → 按最小采用切片(3 文件起步)开始用;
3. **10 分钟**:读 8 个 skill 卡片(定位 / 触发 / 产物 / 核心维度 / 机制)→ 需要深读时点入各 `skills/<name>/SKILL.md`、CONTEXT 速查表、实操 §8.3;
4. **回访**:通过根 CHANGELOG.md 感知 skill 演进与版本变化。

## 实现蓝图(README 结构规格)

**章节顺序**(自上而下):

1. 标题 + 一句话定位(blockquote)+ experimental 声明(原位保留)+ badge 行(2–3 枚:License 双协议 CC-BY 4.0 + MIT / Claude Code 依赖 / experimental);
2. 目录(重组后全量重生成,锚点全通);
3. 「这是什么」:双支柱两条(现有内容保留微调);
4. 「为什么是这个(差异化)」:扩充版(见目标节);
5. 「快速上手:skill 使用流程」:安装说明 + mermaid 协作图(保留)+ 图下补一句「5 环节闭环 + 横切」导航句 + **最小采用切片独立小标题**(紧随协作图,从括号说明升格);
6. **「8 个核心 skill」**:每 skill 一张卡片 + 末尾「各 skill 提问/确认维度速查」表;
7. 「工具边界(请先读)」(保留);
8. 「仓库结构(三区模型)」(保留微调);
9. 「License」(保留);
10. 尾部:「更新日志见 [CHANGELOG.md](CHANGELOG.md)」链接一行(不带摘要,W01 Q3)+ 备注(现有内容合并)。

**skill 卡片模板**(每 skill 一张,四行字段):

```
### /<skill-name> —— <定位一句话>
- **触发**:<典型触发词/场景>
- **产物**:<落盘去向>
- **核心维度 / 机制**:<维度名清单(提问类)或核心机制(非提问类),一行>
```

**第四行语义自适应**(2026-08-20 grill-Q W01 Q4):提问类 5 skill(action-Q / design-Q / grill-Q / grill-with-docs / retro-Q)填「核心维度」,取自 CONTEXT「提问维度速查」节,只列名称不复制定义(如 grill-Q = D1 未言明假设 / D2 单向门 / D3 替代方案 / D4 失败模式 / D5 盲点 / D6 可验证性 / D7 与现实矛盾 / D8 术语一致性);非提问类 3 skill 填「核心机制」,机械转写自各 SKILL.md 既有描述——long-running = feature_list 跟踪 + 端到端测试验证;delegate = 白名单 / 禁区 / 开关 + 逐例留痕;doctor-harness = 分层 / 迁移 / 校验 / 留痕。「不得出现 CONTEXT 没有的维度行」约束限维度速查表,卡片机制行是另一字段。

**维度速查表**(卡片节末尾):表前一句总引导——「维度 = 各 skill 向你提问 / 确认的角度,名称与权威定义见 CONTEXT」(解掉首访者「这些词是什么类别」的困惑,不复制定义零双写,2026-08-20 grill-Q W01 Q6);每 skill 一行 = skill 名 + 核心维度 + 骨架出处链接(同 CONTEXT 速查表列结构);**表头固定标注「权威 = [CONTEXT 提问维度速查](docs/CONTEXT.md),此处为导览,漂移以 CONTEXT 为准」**;README 表不得出现 CONTEXT 表没有的维度行。

**CHANGELOG.md 结构**(仓库根):顶部「记录规则」(从 README 发布说明节原样迁移)+ **首条「README 重构 + 发布说明外移(2026-08-20)」**(「内容不改写,仅迁移」规则不适用此条——README 重构是采用者可感知变更,按继承的记录规则必记,否则新文件开局即破规;2026-08-20 grill-Q W01 Q7)+ 倒序条目(全部现有条目迁移,内容不改写,仅迁移)。

## 验收标准(可独立验证条目式)

1. README 内所有相对链接可达:grep 全量提取 + 逐条核通;
2. 8 个 skill 每个有卡片且四行字段齐全,「核心维度 / 机制」行:提问类 5 skill 与 CONTEXT「提问维度速查」节逐 skill 一致、非提问类 3 skill 与各 SKILL.md 描述一致(人工逐条对照);
3. README 总长 ≤ 250 行(`wc -l`);
4. `python3 scripts/desensitize.py .` 0 命中;
5. `python3 scripts/skills-sync-check.py` 0 违规(未改 skill 侧,应自然通过);
6. 根 CHANGELOG.md 首建,含 README 迁移出的全部发布说明条目(条目数不少于一一对应)+ 记录规则 + 首条「README 重构 + 发布说明外移」;README 内不再保留多于一条的发布说明正文;
7. 若推送:推送前完成 OD-1 ②语义人审 + ③脱敏报告(README 是对外门面、长文重写,脱敏/语义风险最高面;2026-08-20 grill-Q W01 Q7)。

**核验命令示例**(2026-08-20 grill-Q W01 Q8;一次性、内联 python3,跑完即弃不入库——验收从「人感觉对」升到「机器判对」,跨会话可复跑):① 链接全通 = 提取 README 全部相对链接逐个核目标文件存在(`python3 -c "import re,pathlib; [print(t, pathlib.Path(t).exists()) for t in re.findall(r'\]\((?!http|#)([^)#]+)', open('README.md').read())]"`);② 速查表一致 = README 速查表 8 行与 CONTEXT「提问维度速查」表对应行逐行 diff(人工或脚本比对 skill 名 + 维度列两列)。

## 风险与约束

- **双写漂移风险**(主风险):README 维度表与 CONTEXT「提问维度速查」构成新双写点(方法论 audit_v1 已实证「单点事实多处双写导致同步漂移」)。对策三条(2026-08-20 grill-Q W01 Q2 修订②):① README 表头权威声明(见实现蓝图);② **双落**——CONTEXT「提问维度速查」节头反向指针(**触发现场**:CONTEXT 修订者改前读 CONTEXT 自身,义务在此生效,落盘见范围节例外)+ CHANGELOG 记录规则(消费侧提醒);③ README 表不出现 CONTEXT 表没有的行(单向同步义务)。
- **外移断链风险**:发布说明外移后,全库引用「README#发布说明」锚点处需 grep 排查并改为 CHANGELOG 链接。**预销注记**(2026-08-20 grill-Q W01 Q9 预排查):活文档引用 = 0(仅 TODO.md:85 历史完成记录 + harness/design/repo/ 两处已完成阶段设计,皆历史原貌不改),AGENTS.md 实测零内容路由不引用 README 章节结构——风险预销;实现期仍跑一次 grep 复核防排查后新增。
- **长度张力**:卡片化增量 vs 250 行上限,靠发布说明外移(约 −63 行)冲抵;若实现时超限,压缩对象 = 卡片触发行措辞,不砍维度行(本次核心需求)。
- **顺手项约束**(2026-08-20 grill-Q W01 Q1 修订):实操 §8.3 残留修是 git 可回退的独立小改动(实测 3 处,节内同源同性质,机械同步);若 **§8.3 节外**出现残留,退回 TODO「五处分工冗余顺手收敛」条款处理,不扩本次范围。

## 动机

用户发起(2026-08-20):「当前 skill 没有任何地方有介绍,包括各个维度设计,而 README 是本项目其他人的第一印象。」现状核实:README 对 skill 家族仅一句话表格 + mermaid 图;各 skill 的维度设计(grill-Q 8 压测维度 D1–D8、design-Q LN 层级、action-Q confirm-list 六要素、retro-Q 四节、认知状态三态路由等)只散落在 CONTEXT 速查表 / 各 SKILL.md / 实操 §8.3 等内部文档,README 未承载——第一印象与体系实际丰富度严重不匹配。

## L0 自检节

- [x] ① 多模块/多子系统?**否**(README.md + 根 CHANGELOG.md 两个文件,无子系统)
- [x] ② 外部依赖 ≥ 2 类?**否**(纯 Markdown,无外部依赖)
- [x] ③ 跨会话实现(需 feature_list)?**否**(单会话可完成,无需 long-running feature_list)
- [x] ④ 验收含性能/安全门槛?**否**(脱敏/sync-check 为仓库例行门槛,非本 feature 新增性能/安全设计)
- [x] ⑤ AI 判定构造细节不足以直接实现?**否**(章节顺序 / 卡片四字段 / 速查表列 / CHANGELOG 结构 / 七条验收均已具体化到可直接起草)
- → **全不中 = 单层交付合法**;2026-08-20 层闸门人拍板:不增层,L0 即末层,过闸收尾。
