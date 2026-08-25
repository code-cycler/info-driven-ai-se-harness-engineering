# L2-build-i18n-phases-dod.md · i18n 首期五阶段与构建规格(feature-i18n-support)

> 导览:① 本层位置与职责 = 构建层(L2,末层)——i18n-check.py 实现规格、首期翻译五阶段拆分与 DoD、翻译流程模板、执行衔接 ② 覆盖范围 = 仅首期(L0 #20 清单);后续白名单扩面迭代不在本层 ③ 上下游依赖 = 全部实现受 [L1-contract-en-mirror-governance.md](L1-contract-en-mirror-governance.md) 硬约束(§2 全节 + §1.1 + §3.4 + §6.1)与 [ADR-0025](../../adr/0025-english-mirror-drift-governance-integration.md) 约束;偏离走 [ADR-0021](../../adr/0021-design-implementation-deviation-governance.md) ④ 契约项声明 = 本层 DoD 为验收硬标准;实现规格(#1–#5)为脚本硬规格。
>
> 裁决来源:[feature-i18n-support-L2-build-w00](../../questionnaires/archive/i18n-support/feature-i18n-support-L2-build-w00.md)(2026-08-23,17/17 全采纳,取消默认率不适用,转 W01 0 项)。

## §1 i18n-check.py 实现规格(硬规格)

| # | 项 | 规格 |
|---|---|---|
| 1 | 技术栈 | 纯 python3 标准库(pathlib / hashlib / re),零第三方依赖,约 250 行,中文输出(与既有三脚本同栈同风格) |
| 2 | 输出 | 逐行违规 `[类别] 文件: 说明`(五类:缺镜像 / 孤儿 / 过期 / 缺标记 / 断链)+ 分类小计 + 末行汇总 + EXIT 0/1;白名单 / EN_NATIVE 合法存在打注记行(不算违规) |
| 3 | hash 口径 | zh 源文本 `\r\n → \n` 归一后 SHA-256 hexdigest **前 12 位**;en 的 zh-hash 字段同口径(防编辑器换行差异假报过期;代价 = 与原始字节不一致,注记于脚本 docstring) |
| 4 | --stamp 模式 | `python3 scripts/i18n-check.py --stamp en/<相对路径>` = 更新该 en 文件 zh-hash 为当前 zh 源 hash;**只单文件粒度,无批量**(过期标记是漂移证据,只能逐文件回译后显式消除);**前置校验**(grill-Q Q2 裁决 A,程序防御):en 文件 mtime 晚于 zh 源 mtime 才放行,否则拒绝(防「先盖戳后忘回译」消红;启发式可被 touch 绕过,最后防线仍是人审);check 默认模式零写入 |
| 5 | frontmatter 解析 | 手写行式 KV:正则提取 `lang:` / `en-source:` / `zh-hash:` 三行(限文件头 frontmatter 块内),不引 PyYAML;SKILL.md 型既有 frontmatter 追加三字段,其余文件新建 frontmatter |

## §2 首期五阶段拆分与 DoD

执行形态:**顺序不并行**(P1 先行;P3 内部三件 + CONTEXT 可乱序;P5 收尾)。提交粒度:内容阶段每 en 文件一提交,P1 机制允许多文件一提交。

### P1 机制阶段

- **内容**:① `en/` 目录 + `en/README.md` 骨架(切换入口 / canonical 声明 / License 双注 / 镜像树导航占位);② `scripts/i18n-check.py` 实现 + 最小自测;③ readme-revamp 留痕两处([L0-vision-readme-first-impression.md](../readme-revamp/L0-vision-readme-first-impression.md) 重访注记 + 根 CHANGELOG 条目);④ CLAUDE.md 工具命令节增「③ i18n 漂移检查」行。
- **退出判据**:空 en 树 → i18n-check 报全量「缺镜像」且 EXIT 1(机制就位证明);伪造样例分别触发孤儿 / 过期 / 断链 / 缺标记四类;三脚本(desensitize / skills-sync-check / i18n-check)对现状均可运行且后两者 0 违规。
- **依赖**:无(全部自包含)。

### P2 README 阶段

- **内容**:根 README 加切换行 + `en/README.md` 全文翻译(导航占位转实)+ 首批术语提名入 CONTEXT 对照节。
- **退出判据**:该文件 i18n-check 绿;人审记录(门面必审)。
- **依赖**:P1。

### P3 methodology + CONTEXT 阶段(最重:1,555 行)

- **内容**:methodology_v5(800 行)/ philosophy_v7(346)/ practical_v1(207)+ CONTEXT(202,含术语对照节英文呈现)翻译;术语表首批随翻随补。
- **退出判据**:四文件 i18n-check 绿;门面必审;术语表首批补齐;**翻译义务清单扩容**(TRANSLATABLE 加五件,代码注明出处)+ 复检绿(grill-Q Q3)。
- **依赖**:P1;P2 的首批术语(无则空启)。

### P4 SKILL.md 阶段

- **内容**:8 个 SKILL.md 翻译(frontmatter 的 name 保留原值、description 译英);引擎 / CHANGELOG / DESIGN 链接保持指中文原文(L1 §1.4)。**特例条款**(grill-Q Q6):grill-with-docs 的 SKILL.md 本已英文为主(约 8% 行含中文),其 en 镜像 = 仅译残留中文部分(模式节 / 相变节),其余原样,仍走三字段标记与 hash。
- **退出判据**:八文件 i18n-check 绿;AI 自查 + 人抽查;**翻译义务清单扩容**(TRANSLATABLE 加 skills/*/SKILL.md 模式)+ 复检绿(grill-Q Q3)。
- **依赖**:P1;术语表(术语优先复用)。

### P5 CHANGELOG 阶段 + 终验收

- **内容**:CHANGELOG 现条目全译(append-only 镜像);L0 验收七条终验(L1 §6.1 映射表逐条跑);收口三件(CHANGELOG「i18n 首期完成」条目 / STATUS-LOG 里程碑 / TODO i18n 块更新为「首期完成,扩面另立」)。
- **退出判据**:i18n-check 全绿(五类 0,无「已翻未入册」note)+ **翻译义务清单扩容**(TRANSLATABLE 加 CHANGELOG.md)+ L0 验收七条全过(grill-Q Q3)。
- **依赖**:P1–P4 全部。

## §3 翻译流程模板(逐文件七步,执行期照走)

1. 读 zh 源全文;
2. 新术语提名(**按文件批量**:整文件翻完出提名表,人审环节一次勾认,与步骤⑤合并——grill-Q Q7 粒度裁决;同一会话内确认,不留欠账);
   2.5. **发现 zh 源缺陷**(笔误/断链/表述缺陷)→ 停该文件翻译,报人修 zh(canonical 先行,英文永不回灌中文)→ hash 变 → 基于新版重算再翻(grill-Q Q5;zh 修复走既有修订路径,canonical 双件另有压测门);
3. 翻译(占位符 / 代码块 / 公式 / URL / 路径原样保持;**mermaid 图内文本标签译英、结构与节点 ID 不动**——L1 §3.4 硬约束,2026-08-23 dogfood 修订);
4. 写 en 文件(frontmatter 三字段:lang / en-source / zh-hash 占位);
5. 分级人审(门面必审:README / methodology 三件 / CONTEXT;非门面 AI 自查 + 人抽查);
6. `i18n-check --stamp` 落 hash;
7. 独立 git 提交(信息注 en 文件 + 人审状态,如 `Translated-By: claude; Reviewed-by: human`)。

**人审记录载体** = git 提交信息 + 阶段收口 STATUS-LOG 条目;不加 en 文件 frontmatter 审阅字段(审阅状态随 git 历史可溯)。

## §4 执行衔接

- **long-running 衔接**:实现期转 long-running-agent,从本层五阶段反推 feature_list(P1–P5 五 feature,P3 可按需细拆);passes=true 条件 = 各阶段 DoD 端到端过(检查器演示 + 人审记录在 git)。
- **提交门(执行期生效)**:涉 en/ 或可翻中文文件的提交,前置 i18n-check 0 违规(第四道手动门,ADR-0025 决策 5)。
- **首期后扩面**:白名单扩面(retro / OD 全量 / archive)走新 TODO 项,不并入首期;纳入 = 改白名单(代码注明出处)+ 同批交付翻译(L1 §2.3)。

## §5 已知风险注记(实现期防呆)

- **frontmatter 渲染代价**:GitHub 会把 en 文件 frontmatter 渲染为顶部表格(L1 §1.1 已知代价);若用户嫌干扰,等价细化载体 = 文件首行 HTML 注释,改前须用户确认一次。
- **CRLF**:hash 已按归一化口径(§1.3)防假过期;翻译工具若重排全文(非仅换行)仍会正确报「过期」——这是特性不是误报。
- **术语欠账回潮**:任何 en 文件翻译跳过步骤②(术语确认)= 流程违规,retro 候选。

## §6 dogfood 修订记录(2026-08-23,收尾面板裁决「先微闭环 dogfood」)

**闭环范围**:P1 机制(i18n-check.py 七项自测全绿 + en/README.md + 留痕两处 + CLAUDE.md 工具命令③)+ P2 单文件(README 翻译走完整七步流程)。四门实测:脱敏 0 / 双侧同步 0 / harness 布局 0 / i18n-check 仅 1 条待 stamp 的「过期」(PENDING-STAMP 占位,人审后消除)——**L0 验收 ①③④⑤⑥ 已实证,② 恒 0,⑦ 按 P2 进度**。

**发现的规格缺口与回修**(均已即时回修,人审可否决):

| # | 缺口 | 回修 |
|---|---|---|
| 1 | L1 §2.3「初始白名单 = L0 首期清单(一次性全量)」与 §4.2「0 违规才提交」在首期实施窗口冲突——P1–P4 期间未翻文件恒报「缺镜像」,第四道门无法全绿 | 白名单改为**随阶段扩容**(P2 起 README → P3 后加五件 → P4 后加 SKILL → P5 后加 CHANGELOG);语义不变(进白名单即负翻译义务);脚本内注释注明出处 |
| 2 | L1 §1.2 根 README 切换行原文 `**English** · [中文](./README.md)` 链接指向自身(笔误) | 按对称语义更正:`**中文** · [English](en/README.md)` / en 侧 `[中文](../README.md) · **English**` |
| 3 | 「mermaid 原样不译」(L0 #12 / L1 §3.4)两条理由复核:「防图漂移」不成立(图在文件内,文件级 zh-hash 已覆盖),仅语法风险真实且可控;README 协作图是承重件,英文读者在图处断线 | L1 §3.4 修订:**图内文本标签译英,结构与节点 ID 不动**,渲染验证人审兜底;en/README.md 协作图已重译;触发 = 人审质询,用户裁决「修订并译图」(2026-08-23) |

**流程观察**(不改规格,记档):① 七步流程可走通,步骤②(术语提名)与步骤⑤(人审)在人审环节自然合并为一次交互——流程成立;② ~~mermaid 中文标签保持原样后,英文读者从协作图获取的信息有限~~(已升级为缺口 #3 修订,图内标签译英);③ en/README.md frontmatter 在 GitHub 渲染为顶部表格——**已裁决维持 frontmatter 载体**(2026-08-23 grill-Q Q10:字段机器可查、语义标准,视觉代价可忍;换 HTML 注释需改解析器 + 全部 en 文件,不值)。
