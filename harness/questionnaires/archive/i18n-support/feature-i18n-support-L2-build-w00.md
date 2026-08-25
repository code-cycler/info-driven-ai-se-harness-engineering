---
mode: feature
wave: 0
stage: L2-build
created: 2026-08-23
status: archived
---
# 问卷 feature-i18n-support L2-build W00 · Preview(决策默认值 yes/no 速答)

> **本波是 preview 预答层**(独立 wave 0):把 AI 有明确默认倾向的构建决策逐条列出,人只做 yes/no 速答。
>
> **作答规则**:
>
> - **预勾选 = opt-in 开关**(默认关):全部 `[ ]`,人逐条作答;勾 `[x]` = 采纳默认按默认落盘
> - **取消勾选(留空)= 不采纳** → 该要点转入 W01 单独拷问
> - **单向门要点永不预勾**;本波无 🤔(真定不了 → 取消勾选转 W01)
> - 若"大体同意但要改一两处" → 取消勾选,转 W01 时给自定义值
>
> 默认来源标注于〔〕。硬约束条目(继承 L1)不重出,本波只定 L2 构建层决策。

> **出题依据摘要**(2026-08-23,一手核实):
>
> - **L0+L1 已决全采纳**([L0](../../design/i18n-support/L0-vision-i18n-support.md) 23 条 / [L1](../../design/i18n-support/L1-contract-en-mirror-governance.md) 21 条 + [ADR-0025](../../adr/0025-english-mirror-drift-governance-integration.md)):六模块契约与五类检查为硬约束,本层不重议,只定实现规格 / 阶段拆分 / 流程模板 / 执行衔接。
> - **既有脚本风格实测**:三脚本(desensitize 89 行 / harness-check 192 行 / skills-sync-check 127 行)均为纯标准库 + 中文输出 + 逐行违规列表 + EXIT 0/1;i18n-check 同风格延续。〔scripts/ 源码〕
> - **frontmatter 现状**:8 个 SKILL.md 有 YAML frontmatter;README / CHANGELOG / docs 根无 frontmatter——en 镜像统一新建 frontmatter 承载三字段(L1 §1.1 已决,含 GitHub 渲染表格代价注记);仓库无 PyYAML 依赖 → 解析须手写行式 KV。〔skills/ 与 docs/ 实测 + python3 环境无 yaml 包风险注记(标准库外零依赖原则)〕
> - **long-running 衔接既有规则**:阶段拆分是 feature_list 反推源;passes 只能端到端测试通过才 true。〔CLAUDE.md 落盘路径表 + long-running SKILL.md〕
> - **无未验证假设**(SHA-256 / pathlib 均标准库;--stamp 为写操作但属本层新定接口)。

## 决策默认值清单

### 一、i18n-check.py 实现规格

- [X]  **1 技术栈与体量**:纯 python3 标准库(pathlib / hashlib / re,零第三方依赖),预计约 250 行,与既有三脚本同栈同风格(中文输出)。〔scripts/ 三脚本实测风格〕
- [X]  **2 输出格式**:仿 skills-sync-check——逐行违规 `[类别] 文件: 说明`(五类:缺镜像/孤儿/过期/缺标记/断链)+ 分类小计 + 末行汇总 + EXIT 0/1;白名单 / EN_NATIVE 合法存在打注记行(不算违规)。〔L1 §2.2 + sync-check 输出实测〕
- [X]  **3 hash 细节 = 换行规范化后内容**:zh 源 hash 对象 = 文本 `\r\n → \n` 归一后的 SHA-256 hex 前 12 位(防编辑器换行差异假报过期);en 文件 zh-hash 字段记录同一规范化口径。备选:原始字节(更简单,但一次 CRLF 转换即全线假过期)——默认归一化。〔跨编辑器稳健;代价 = 与原始字节不一致,注记于脚本 docstring〕
- [X]  **4 --stamp 写入模式(单文件粒度)**:`python3 scripts/i18n-check.py --stamp en/<相对路径>` = 把该 en 文件 zh-hash 更新为当前 zh 源 hash;**只提供单文件粒度,不提供批量 --stamp-all**(防一键盖掉未回译文件的过期标记——过期标记是漂移证据,只能逐文件在回译完成后显式消除);check 默认模式仍零写入。〔L1 §2.2 check-only + 回译协议 §4.2〕
- [X]  **5 frontmatter 解析 = 手写行式 KV**:正则提取 `lang:` / `en-source:` / `zh-hash:` 三行(限文件头 frontmatter 块内),不引 PyYAML(仓库零第三方依赖原则);SKILL.md 型既有 frontmatter 追加三字段,其余文件新建 frontmatter。〔仓库无 yaml 包 + L1 §1.1〕

### 二、首期五阶段拆分与 DoD

- [X]  **6 P1 机制阶段 DoD**:① `en/` 目录 + `en/README.md` 骨架(切换入口 / canonical 声明 / License 双注 / 镜像树导航占位);② `scripts/i18n-check.py` 实现并通过最小自测(空 en 树 → 全部「缺镜像」且 EXIT 1;伪造样例分别触发孤儿 / 过期 / 断链 / 缺标记);③ readme-revamp 留痕两处(设计文档重访注记 + 根 CHANGELOG 条目);④ CLAUDE.md 工具命令节增「③ i18n 漂移检查」行。**退出判据 = 空树检查报全量缺镜像(EXIT 1)证明机制就位 + 三脚本(含 i18n-check)对现状可运行**。〔L1 §6.4 执行序 + L0 #22〕
- [X]  **7 P2 README 阶段 DoD**:根 README 加切换行 + en/README.md 全文翻译(导航转实)+ 首批术语提名入 CONTEXT 对照节;**退出 = 该文件 i18n-check 绿 + 人审记录(门面必审)**。〔L1 §1.2/§1.3 + §4.1〕
- [X]  **8 P3 methodology + CONTEXT 阶段 DoD**:三件(methodology_v5 800 行 / philosophy_v7 346 / practical_v1 207)+ CONTEXT(含术语对照节英文呈现)翻译;**退出 = 四文件绿 + 人审(门面必审)+ 术语表首批补齐**。〔L1 §6.4 + 行数实测〕
- [X]  **9 P4 SKILL.md 阶段 DoD**:8 个 SKILL.md 翻译(frontmatter 的 name/description 字段保留原 name、description 译英);引擎 / CHANGELOG / DESIGN 链接保持指中文原文;**退出 = 八文件绿 + AI 自查 + 人抽查**。〔L1 §1.4 + §4.1 分级〕
- [X]  **10 P5 CHANGELOG 阶段 + 终验收 DoD**:CHANGELOG 现条目全译(append-only 镜像);**退出 = i18n-check 全绿(五类 0)+ L0 验收七条全过(L1 §6.1 映射表逐条跑)+ 收口三件(CHANGELOG 条目 / STATUS-LOG / TODO 块更新)**。〔L0 #19 + L1 §6.1〕
- [X]  **11 阶段执行形态 = 顺序不并行**:P1 先行,P2–P4 顺序推进(P3 内部三件 + CONTEXT 可乱序),P5 收尾终验收;不并行开多线程(个人开发者单线程,翻译人审是串行瓶颈)。〔long-running 默认单 agent 一次一功能 + 人审串行现实〕

### 三、翻译流程模板

- [X]  **12 逐文件七步标准流程**(记 L2 文档,执行期照走):① 读 zh 源全文 → ② 新术语提名(人当次确认入 CONTEXT 对照节)→ ③ 翻译(占位符 / 代码块 / mermaid / 公式 / URL / 路径原样保持)→ ④ 写 en 文件(frontmatter 三字段)→ ⑤ 分级人审(门面必审 / 非门面抽查)→ ⑥ `i18n-check --stamp` 落 hash → ⑦ 独立 git 提交(信息注 en 文件 + 人审状态)。〔L1 §3/§4 契约的操作化〕
- [X]  **13 人审记录载体 = git 提交信息 + STATUS-LOG**:人审事实记提交信息(如 `Translated-By: claude; Reviewed-by: human` 注记)+ 阶段收口 STATUS-LOG 条目;**不加 en 文件 frontmatter 审阅字段**(减字段膨胀,审阅状态随 git 历史可溯)。备选:frontmatter `reviewed:` 字段(机器可查但字段膨胀)——默认弃。〔git 可溯性 + frontmatter 最小化〕
- [X]  **14 术语提名不过夜**:逐文件翻译时即提名即确认,不留「待定术语」跨会话(防术语欠账与各文件自译回潮);会话内人不在场时该文件暂停于步骤②。〔L1 §3.2 单点事实源 + 即时沉淀铁律〕

### 四、执行衔接

- [X]  **15 long-running 衔接**:实现期转 long-running-agent,从本层五阶段反推 feature_list(P1–P5 五 feature,或 P3 拆三件 + CONTEXT);passes=true 条件 = 各阶段 DoD 端到端过(检查器演示 + 人审记录在 git)。〔long-running SKILL.md 规则 + L1 §6.4〕
- [X]  **16 提交粒度**:内容阶段每 en 文件一提交(细粒度,回译定位与 review 友好);P1 机制阶段允许多文件一提交(机制是一个整体)。〔git 可溯性 + 分期 DoD〕
- [X]  **17 首期收口动作**:P5 退出后——根 CHANGELOG 记「i18n 首期完成」条目 + STATUS-LOG 记里程碑 + TODO i18n 块更新为「首期完成,后续扩面(白名单迭代)另立」;后续白名单扩面(retro / OD 全量 / archive)走新 TODO 项不并入首期。〔L1 §2.3 白名单迭代协议〕

## 补充声明

<任何想补充的话……没有就留空。agent 处理时必读>

---

## 处理报告摘要(2026-08-23,W00 处理)

**作答解析**:17/17 答毕,无异常。无 🤔 逃生舱。

**preview 统计**:勾选采纳 **17** · 取消勾选 **0** · 转 W01 正式题 **0**。opt-in 未启用,取消默认率不适用。补充声明为空。

**每题去向**:17 条全按默认落盘 [L2-build-i18n-phases-dod.md](../../design/i18n-support/L2-build-i18n-phases-dod.md)(§1 实现规格表 / §2 五阶段 DoD / §3 七步翻译流程 / §4 执行衔接 / §5 实现期防呆注记)。i18n-support 设计套三层齐:L0 + L1 + ADR-0025 + CONTEXT 术语节 + L2。

**三层全链小结**:L0 23/23 + L1 21/21 + L2 17/17 = 61 条决策全采纳、零取消、零逃生舱、零补充声明;W01 全链未触发(每层 W00 全采纳即覆盖骨架必含,无开放必答项遗留)。

**下一波候选**:无——L2 为末层,设计链收口。后续动作 = 层闸门 → 收尾面板(多线程开工 / dogfood / grill-Q 压测 / long-running 衔接四问)。

**未验证假设台账**:全链关闭。实现期首个重验点 = P1 自测(i18n-check 对空树全量报缺镜像);frontmatter 渲染代价已在 L1 §1.1 / L2 §5 注记,留用户视觉确认触发等价细化。

**状态**:pending → processed(2026-08-23)→ archived(同日,目录 i18n-support/)。
