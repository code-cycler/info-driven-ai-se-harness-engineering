# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 这是什么仓库

`info-driven-ai-se-harness-engineering` 是一套面向 1–5 人小团队的 **AI native 开发方法论 + 可直接运行的 Claude Code skill 执行体**。不是可构建的代码项目——**没有 build / test / lint 工具链**。仓库内容全部是 Markdown 文档 + skill 配置 + 一个 Python 脱敏脚本。

两大支柱（详见 [docs/methodology/methodology_v3.md](docs/methodology/methodology_v3.md)）：
1. **以信息为核心** —— 与 AI 协作的本质是信息流转；瓶颈在有效上下文的质与量，以及对抗 AI 在信息真空中的幻觉式自作主张决策。
2. **驾驭工程 = AI × 软件工程** —— AI 是加速器，工程纪律（设计先行 / TDD / ADR / 复盘）是骨架。

## 双 License（编辑前必须知道分区）

| 区域 | License | 文件 |
|---|---|---|
| 方法论文字 | **CC-BY 4.0** | [docs/methodology/](docs/methodology/)、[docs/LICENSE](docs/LICENSE) |
| skill 配置 / 代码 | **MIT** | [skills/](skills/)、[scripts/](scripts/)、根 [LICENSE](LICENSE) |

改文章走署名转载语义；改 skill / 脚本是 MIT 自由复用。分区不要混（ADR-0002）。

## 唯一的工具命令:脱敏检查

仓库内容已脱敏（ADR-0001 + OD-1）。`scripts/desensitize.py` 是发布门槛脚本:

```bash
python3 scripts/desensitize.py .                  # check 全仓库(发布前 DoD 要求 0 命中)
python3 scripts/desensitize.py skills docs --apply # 按映射表执行替换
python3 scripts/desensitize.py . --exclude docs/methodology
```

- 映射表(真实项目名 → 「项目A/B/C…」、真实用户路径 → `~`)在**本地文件** `scripts/desensitize_map.local.json`(gitignored 不入库;2026-07-29 起外置,防映射本身随仓库泄漏)。仓库内脚本默认空映射,公开克隆者运行为无害空转。**这些「项目A/B/C」是脱敏占位,不是真实项目名**——编辑时不要当真名对待,也不要无意中引入真实项目名 / 路径 / 人名;**也不要在 .md 文档中复述映射表里的真实名**(脚本只扫 .md,复述即泄漏)。
- **push 前三道门全绿**(OD-1):① 脚本 0 命中;② 人逐行复审语义信息;③ 脱敏报告。push 后内容被 fork / 缓存不可真正撤回——这是单向门。

## skill 家族协作架构（核心 big picture）

7 个 skill 不是孤立的,构成 **5 环节闭环 + 横切**。理解它们的衔接协议才能正确编辑任一 skill:

```
design-Q ──(收尾提议)──> grill-Q ──(收尾提议)──> long-running ──> retro
   │                         │                        │              │
   生成式设计                  对抗式压测(D1–D8)         跨会话实现       复盘
   │                         │                        │              │
   └────────── delegate(横切:任意环节下放纯执行决策)────────────────────┘

grill / grill-with-docs = 实现期单点深钻(一问一答),正交可任意插入
```

**三族 skill 的交互模式**(方法论 §5.3,改动一族的机制要对齐另一族):

| 族 | skill | 交互 | 落盘 |
|---|---|---|---|
| 批量问卷族 | design-Q / grill-Q / retro-Q | 多波次 Markdown 问卷,离线作答 | 阶段文档 / ADR / OD / CONTEXT |
| 单点深钻族 | grill / grill-with-docs | 一问一答,逐轮 `AskUserQuestion` | grill 纯对话默认不写文件;with-docs 写 CONTEXT/ADR/OD |
| 约束系统 | long-running-agent | 落盘文件驱动(feature_list + progress) | `.claude/feature_list.json` 等 |

**衔接协议**(在各 SKILL.md 的"主流程"末尾,改一个 skill 的衔接点要同步另一端):
- design-Q 收尾 → 提议 grill-Q 压测;grill-Q 收尾 → 提议 long-running。
- 问卷处理中发现"单点深水区"→ 建议用户对该点单独跑 grill-with-docs。

## skill 内部结构与"引擎漂移"（编辑 skill 时必读）

每个 skill 目录结构:`SKILL.md`(带 `<what-to-do>` / `<supporting-info>` 区块 + YAML frontmatter) + 骨架文件(`*-SKELETONS.md`) + `DESIGN.md`(设计决策 + dogfood 记录) + 可选 `docs/`(retro 有完整 VISION/HLD/归档问卷)。

**引擎副本漂移(OD-8,方法论「常见误区 #17」的活体证据)**:`QUESTIONNAIRE-FORMAT.md` 与 `PROCESSING-RULES.md` 在 design-Q / grill-Q / retro-Q 三个 skill **各持一份副本**(均自标「design-Q 引擎复用件」),diff 证实已漂移。
- **改一方要考量三方**,在对应 `DESIGN.md` 声明漂移关系。
- **禁止擅自统一 / 抽取共享文件**——这是已决项(保留现状,统一不在价值主线)。

## 落盘路径速查（skill 产物落在哪）

| skill | 产物落点(均落**宿主项目**,非本仓库) |
|---|---|
| design-Q | VISION / `docs/design/` HLD·LLD / `docs/adr/` / `docs/OPEN-DECISIONS.md` / `CONTEXT.md`;问卷 `docs/questionnaires/<stage>-w<NN>.md` → 处理后归档 `archive/` |
| grill-Q | 发现 → `CONTEXT`/`adr`/`OPEN-DECISIONS`;**工件修订建议只进处理报告,绝不替改工件** |
| retro-Q | `docs/retro/<主题>_vN.md` + `TODO.md`;问卷 `docs/questionnaires/retro-<主题>-w<NN>.md` |
| long-running | `.claude/feature_list.json`(passes 只能端到端测试通过才 true)+ `.claude/claude-progress.txt`(写顶部) |
| delegate | `<项目根>/delegation.md`(白名单·禁区·开关)+ `delegation-log.md`(追加式,只增不改) |

## 编辑本仓库的铁律（与全家族 skill 对齐）

这些是方法论自身反复强调、违反即产出劣化的纪律:

1. **AI 不替人决策** —— 出题 / 验证 / 落盘是 agent 的角色;选择永远是人做的。改 skill 或文档时同理,遇到决策点问人,不自行拍板。
2. **即时沉淀,不批处理** —— 处理完即刻写文件,不攒到末尾。
3. **原始信息不丢失** —— 已用问卷 `archive/`(只移不删);废弃文件归 `waste/` 不直接删除。
4. **先验证再写** —— 引用进文档 / 问卷的事实(尤其"代码 vs 文档"矛盾、外部依赖能否真正跑通)必须核实原文,不凭转述。
5. **文件版本命名** —— `_v1` / `_v2` 递增,禁 `final` / `new` / `copy`(全局 `~/.claude/CLAUDE.md` 已规定,本仓库同样适用)。
6. **不一致的设计文档比没有更危险** —— 实现与文档脱节时先更新文档。

## 当前仓库状态（递归:方法论要用于自身设计）

仓库 2026-07-28 建仓;**2026-07-29 methodology_v3 完成**:design-Q 设计套([VISION](docs/design/VISION.md) / [HLD_v2](docs/design/hld_v2.md) / [LLD_v2](docs/design/lld_v2.md))+ grill-Q 两轮压测(ADR-0004/5/6)→ grill-with-docs 压测 P0 章节大纲 → long-running-agent 起草 [methodology_v3](docs/methodology/methodology_v3.md) 并全仓库同步(CONTEXT / README / CLAUDE 定义版措辞、v2 标历史、脱敏门 0 命中)。工件:[.claude/feature_list.json](.claude/feature_list.json) 全绿。

**下一步主线([TODO.md](TODO.md))**:grill-Q 压测 v3 成稿(可选质量门)→ 远程仓库建立 + push(单向门:push 前 OD-1 三道门全绿 + OD-4 母本标注)。注意:本仓库**自身**的 repo 级 design-Q(对仓库定位 / skill 家族的设计)仍未跑——design-Q / grill-Q / retro-Q 各自目录内的 `docs/` 是 dogfood 产物,不构成本仓库自身的设计文档。

待办关键项:脱敏语义人审(OD-1 ②)、OD-4 母本标注、远程仓库建立、CONTRIBUTING + issue 模板(OD-3)。

## 关键文档导航

- [docs/methodology/methodology_v3.md](docs/methodology/methodology_v3.md) —— 方法论完整阐述(自包含,不依赖 skill 规格;[v2](docs/methodology/methodology_v2.md) 保留作历史版本)。**任何关于方法论主张的修改以此为 canonical(OD-4)。**
- [docs/CONTEXT.md](docs/CONTEXT.md) —— 纯术语表(双支柱 + 第一支柱术语分层(v3) / 5 环节 / Grill 家族 / skill 家族 / Claude Code 定位)。
- [docs/OPEN-DECISIONS.md](docs/OPEN-DECISIONS.md) —— 9 条待决事项 + 重访触发条件。改任何"已决"事项前先查这里与 `docs/adr/`。
- [docs/adr/](docs/adr/) —— ADR-0001 source of truth / 0002 License / 0003 发布形态。
