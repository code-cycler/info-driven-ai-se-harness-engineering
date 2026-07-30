# TODO

> 追踪文件。建仓:2026-07-28(建仓前经 grill-questionnaire 两波压测驱动筹建)。
> 当前状态:**methodology_v3 已发布(2026-07-29,long-running-agent 驱动,P0 经 grill-with-docs 压测定稿);仓库已首次推送至 GitHub**。
> 下一步主线:**grill-Q 压测 v3 成稿**(可选质量门);**OD-4 母本标注**(作者其他位置副本标「开发副本,以 v3 为准」,仓库外动作)。

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
> ✅ **已执行(2026-07-29)**:9 项修订全部落 [HLD_v2](docs/design/hld_v2.md) / [LLD_v2](docs/design/lld_v2.md);Q2+Q12 → [ADR-0005](docs/adr/0005-pillar-standard-wording.md);Q3 章节策略 → **彻底重排**,[ADR-0006](docs/adr/0006-v3-chapter-restructure.md)。归档问卷 [grill-methodology-v3-design-w01](docs/questionnaires/archive/grill-methodology-v3-design-w01.md)。
> ✅ **已落地(2026-07-29,long-running 会话 001)**:9 项随 v3 起草全部实现并 DoD 验证(grep 证据见 `.claude/claude-progress.txt`)。

- ✅ **HLD#11 标准措辞按 [ADR-0005](docs/adr/0005-pillar-standard-wording.md) 修订**:定义版(CONTEXT/README/CLAUDE)+ 完整版(v3§2.1),核心子串四处 grep 一致
- ✅ **HLD#9 三层立论模型表加因果方向**(Q1):v3 §2.1 表头「层(因果方向 ↓)」+ ↓导致/↓表现 行
- ✅ **HLD#1 章节策略**(Q3):**结论 = 彻底重排**(用户定夺,见 [ADR-0006](docs/adr/0006-v3-chapter-restructure.md));v3 章节按新立论重排,锚点全量重写
- ✅ **LLD 加 §2.1 改写回归 DoD**(Q4):LLD_v2 L4 已加;v3 grep 验证「有效上下文/120k/400k/双支柱」全在
- ✅ **LLD#7 v3 文件头写完整谱系**(Q5):v1 单支柱 → v2 双支柱 → v3 补机制层 + 推导链
- ✅ **LLD 补 §十一 失败模式表更新**(Q6):v3 §十一 #19–22(三层误读 / 双靶子失衡 / (a)(b) 混淆 / 标准句脱节)
- ✅ **LLD#12 DoD 脚本具体化**(Q7+Q8):核心子串 grep + 章节清单核对 + § 引用 Python 校验,均已在 v3 发布门执行
- ✅ **LLD#13 回归 DoD 措辞修正**(Q9):LLD_v2 已修;v3 按「内容不丢」执行关键概念 grep 全过
- ✅ **HLD#8 CONTEXT 术语清单扩展**(Q10+Q11):CONTEXT 新增「第一支柱术语分层(v3)」节,8 术语全部落盘标层级

### 🔴 methodology_v3 起草工作包(grill-Q W01 产出 · ADR-0004)

> 来源:grill-Q 压测 methodology_v2([W01](docs/questionnaires/archive/grill-methodology-v2-w01.md)),D7 核心发现——第一支柱立论实质偏离作者本意,「AI 幻觉式决策」机制层缺席。详见 [ADR-0004](docs/adr/0004-methodology-v3-hallucination-thesis.md)。
> ⚠️ **实现规格以 [LLD_v2](docs/design/lld_v2.md) 为准**(P0 章节设计 → P1–P4,5 阶段);本块为 ADR-0004 时期的初始拆分,章节策略已升级为彻底重排(ADR-0006)。

- ✅ **升 methodology_v3,补全第一支柱机制层**(ADR-0004 决策 1,2026-07-29 完成):
  - ✅ 两类信息断层(v3 §1.2:人与人 → AI 替代角色挂 §6.2;人与AI → 问答对齐挂第五章),返工框架保留为症状层
  - ✅ §2.1 正面因果立论:「背景缺失 → AI 在信息真空中的幻觉式自作主张决策 → 返工。问答逐步对齐需求,是对抗此机制的直接手段」(blockquote 独立引用形式,DoD Q8 核验通过)
  - ✅ §2.1/§7.6 过载对策链:design-Q 沉淀落盘 → /compact 压缩;点明「缺失 vs 过载两环节不矛盾」
  - ✅ §5.1 (a)(b) 盲区小节,grill 锚定 (b);§十二 加背景缺失自查项
  - ✅ 双靶子:vibe coding 主叙事限 §一 + 立论挂接点,传统 SDLC 原位保留为对照(grill-with-docs 压测定案)
- ✅ **CONTEXT.md 同步**(ADR-0004 决策 3,2026-07-29):第一支柱换 ADR-0005 定义版;8 术语分层清单落盘
- ✅ **README.md / 项目 CLAUDE.md 开篇同步**(2026-07-29):双支柱表述与 v3 一致;另修复 CLAUDE.md 两处——导航节 v2→v3 链接、脱敏映射真实名复述(脱敏门 2 命中 → 0)
- ⏳ **OD-4 母本同步**:v3 发布后,作者其他位置副本标注"开发副本,以 v3 为准"(仓库外动作,push 时执行)
- ✅ **v3 起草驱动方式抉择**(2026-07-29):design-Q 设计套 + long-running-agent 起草 + grill-with-docs 压测 P0 章节大纲,未裸写;**遗留可选质量门:grill-Q 压测 v3 成稿**

### 其他待办

- ⏳ **脱敏语义人审**(OD-1 ②):机械脱敏已 0 命中,但「项目A/B/C」占位在归档问卷里的通顺度、上下文是否仍可识别个人——需人逐行复审关键文件(`skills/*/docs/questionnaires/archive/`、各 `DESIGN.md`)
- ⏳ **design-questionnaire 正式设计**:vision → HLD → LLD。本批 [ADR](docs/adr/) / [OD](docs/OPEN-DECISIONS.md) 作输入
- ✅ **远程仓库建立 + push**(2026-07-29):[code-cycler/info-driven-ai-se-harness-engineering](https://github.com/code-cycler/info-driven-ai-se-harness-engineering),首次推送 2 个 commit(建仓全量 + long-running 工件);push 前 OD-1 三道门全绿(脚本 0 命中 / 语义人审已过 / 映射表外置)
- ⏳ **CONTRIBUTING + issue 模板**(OD-3):experimental 维护声明落地
- ⏳ **skill 内容审校**:复制的 7 skill 是否完整;引擎副本漂移(OD-8)是否需在 skill 区 README 说明
- ⏳ **可迁移性单点深钻**(可选):对 OD-2 逐 skill 盘 Claude Code 依赖,产出「理念 vs 执行依赖」清单(用 grill-with-docs)
