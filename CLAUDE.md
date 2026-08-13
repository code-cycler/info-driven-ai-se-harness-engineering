# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库定位

`info-driven-ai-se-harness-engineering` 是一套面向**个人开发者**的 **AI native 开发方法论 + 可直接运行的 Claude Code skill 执行体**。不是可构建的代码项目——**没有 build / test / lint 工具链**。仓库内容全部是 Markdown 文档 + skill 配置 + 一个 Python 脱敏脚本。

两大支柱(相乘,缺一为零,完整立论见 [methodology_v4.md](docs/methodology/methodology_v4.md)):
1. **以信息为核心** —— 信息流转;瓶颈在有效上下文的质与量 + 对抗 AI 在信息真空中的幻觉式自作主张决策。
2. **驾驭工程 = AI × 软件工程** —— AI 是加速器,工程纪律是骨架(v4 补机制层:「无护栏 → AI 产出悄悄劣化」)。

## 规范优先级

文档冲突时按此裁决(**唯一权威处**,不复制到其他文件;冲突必显式说明,不静默选择):

> **方法论主张(方法论 + 哲学文件,canonical)> ADR > CONTEXT 术语 > skill 规格(SKILL.md + DESIGN.md 同层)> 实操文件**

协调注:ADR 中的术语定义以 CONTEXT 为准——ADR 记决策(含历史措辞),CONTEXT 记活术语。

## 关键文档导航

- 方法论三块(ADR-0007):[methodology_v4.md](docs/methodology/methodology_v4.md)(怎么做,canonical)+ [philosophy_v5.md](docs/methodology/philosophy_v5.md)(为什么,canonical;v5 加安全科学第四学科视角「去 AI 黑盒」§八)+ [practical_v1.md](docs/methodology/practical_v1.md)(怎么用,非 canonical 轻量修订);[methodology_v3/v2](docs/methodology/archive/) 与 [philosophy_v4](docs/methodology/archive/philosophy_v4.md) 为历史母本。
- [docs/CONTEXT.md](docs/CONTEXT.md) —— 纯术语表(双支柱 / 第一支柱术语分层 / 术语治理 / **项目学科地图 + AI 黑盒(v5 第四学科视角锚点)** / Grill 家族 / skill 家族)。
- [docs/OPEN-DECISIONS.md](docs/OPEN-DECISIONS.md) —— 待决事项 + 重访触发。改"已决"事项前先查这里与 `harness/adr/`。
- [harness/adr/](harness/adr/) —— ADR-0001 source of truth / 0002 License / 0003 发布形态 / 0007 三块拆分 / 0008–0010 v4 落地 / 0011 硬编码 harness / 0012–0013 doctor-harness 分层 / **0014 学科挂接分层策略 / 0015 去黑盒第四学科视角独立锚点(v5)**。
- [harness/design/](harness/design/) 与 [harness/questionnaires/](harness/questionnaires/) —— **AI 流程产物**(设计文档套 / 归档问卷),与项目文件 docs/ 物理分离(三区模型)。
- 唯一工具命令:脱敏检查 `python3 scripts/desensitize.py .`(发布前 DoD 要求 0 命中;映射表本地 gitignored;push 前三道门 = 脚本 0 命中 + 语义人审 + 脱敏报告,见 [OD-1](docs/OPEN-DECISIONS.md);**不要在 .md 中复述映射表里的真实名**)。

## 双 License(编辑前必须知道分区)

| 区域 | License | 文件 |
|---|---|---|
| 方法论文字 | **CC-BY 4.0** | [docs/methodology/](docs/methodology/)、[docs/LICENSE](docs/LICENSE) |
| skill 配置 / 代码 | **MIT** | [skills/](skills/)、[scripts/](scripts/)、根 [LICENSE](LICENSE) |

改文章走署名转载语义;改 skill / 脚本是 MIT 自由复用。分区不要混(ADR-0002)。

## skill 家族协作

9 个 skill 构成 **5 环节闭环 + 横切**(衔接协议详见方法论 [§5.3](docs/methodology/methodology_v4.md#53-两族-grill) 与各 SKILL.md「主流程」末尾):

```
design-Q ──(收尾提议)──> grill-Q ──(收尾提议)──> long-running ──> retro
   │                         │                        │              │
   生成式设计                  对抗式压测(D1–D8)       跨会话实现       复盘
   │                         │                        │              │
   └────────── delegate(横切:任意环节下放纯执行决策)────────────────────┘

grill / grill-with-docs = 实现期单点深钻(一问一答),正交可任意插入
action-questionnaire = 非正式行动前的细节确认(confirm-list),轻量前奏可任意插入
doctor-harness = harness 演进治理(分层/迁移/校验/留痕),横切如 delegate
```

**落盘路径速查**(产物均落**宿主项目** `项目根/harness/`,硬编码不配置化——方案 R 已于 2026-08-07 放弃、回归硬编码,见 [ADR-0011](harness/adr/0011-abandon-plan-r-hardcode-harness.md)):

| skill | 产物落点 |
|---|---|
| action-Q | 确认结果 → 问卷归档 `harness/questionnaires/archive/`(只移不删);ADR 三条件 → `harness/adr/`;单向门/重大风险 → `docs/OPEN-DECISIONS.md`;术语冲突 → `CONTEXT.md` |
| design-Q | VISION / `harness/design/` HLD·LLD / `harness/adr/` / `docs/OPEN-DECISIONS.md` / `CONTEXT.md`;问卷 `harness/questionnaires/<stage>-w<NN>.md` → 归档 `archive/` |
| grill-Q | 发现 → `CONTEXT`/`adr`/`OPEN-DECISIONS`;**工件修订建议只进处理报告,绝不替改工件** |
| retro-Q | `docs/retro/<主题>_vN.md` + `TODO.md`;问卷 `harness/questionnaires/retro-<主题>-w<NN>.md` |
| long-running | `.claude/feature_list.json`(passes 只能端到端测试通过才 true)+ `.claude/claude-progress.txt`(写顶部) |
| delegate | `<项目根>/delegation.md`(白名单·禁区·开关)+ `delegation-log.md`(追加式,只增不改) |
| doctor-harness | 组织 harness/ 区(分层/迁移/校验/留痕);规则权威 `skills/doctor-harness/HARNESS-RULES.md`;校验 `scripts/harness-check.py` |

**引擎副本漂移(OD-8,编辑 skill 时必读)**:`QUESTIONNAIRE-FORMAT.md` / `PROCESSING-RULES.md` 在 design-Q / grill-Q / retro-Q / **action-Q** 各持一份副本(已漂移)——改一方考量**四方**,在对应 `DESIGN.md` 声明漂移关系;**禁止擅自统一 / 抽取共享文件**(已决项)。

## 编辑本仓库的铁律

这些是方法论自身反复强调、违反即产出劣化的纪律:

1. **AI 不替人决策** —— 出题 / 验证 / 落盘是 agent 的角色;选择永远是人做的。改 skill 或文档时同理,遇到决策点问人,不自行拍板。
2. **即时沉淀,不批处理** —— 处理完即刻写文件,不攒到末尾。
3. **原始信息不丢失** —— 已用问卷 `archive/`(只移不删);废弃文件归 `waste/` 不直接删除。
4. **先验证再写** —— 引用进文档 / 问卷的事实(尤其"代码 vs 文档"矛盾、外部依赖能否真正跑通)必须核实原文,不凭转述。
5. **文件版本命名** —— `_v1` / `_v2` 递增,禁 `final` / `new` / `copy`。
6. **不一致的设计文档比没有更危险** —— 实现与文档脱节时先更新文档。

## 仓库状态

**2026-08-05:repo 级设计完成,落地执行中**——design-Q 三阶段 + grill-Q 压测 12 项回灌(设计套 [harness/design/repo/](harness/design/repo/));方法论 + 哲学升 **v4**(受众收窄个人 / 第二支柱机制层对称化 / 哲学三学科化(人因/软工/运筹));harness 区物理分离(docs/design/ + docs/questionnaires/ 迁入);术语治理(8 术语全保留 + 新词三条件门槛)。落地执行 P1–P4 完成(P1 迁移 / P2 术语 / P3 v4 / P4 入口),**P5(P5 ADR-0008/0009/0010)与 P6(发布门 + dogfood)待执行**,见 [TODO.md](TODO.md)。

**2026-08-07:design-Q skill 规格整理(skill-spec-revamp)→ 撤销方案 R**:骨架增强(HLD/LLD 判别法则 + 反简化最小必含 + 坍缩分档,仅 design-Q)**保留并回灌**;落盘路径配置化(方案 R)**已放弃**([ADR-0011](harness/adr/0011-abandon-plan-r-hardcode-harness.md)),**回归硬编码 `项目根/harness/`**(design/ + questionnaires/ + adr/);两套 skill(skills/ 与 `~/.claude/skills/`)已重建一致(仅脱敏差),设计套 [harness/design/skill-spec-revamp/](harness/design/skill-spec-revamp/)。

**2026-08-08:doctor-for-harness 完成(第 9 个 skill)+ harness 治理落地**:分层规则权威化([HARNESS-RULES.md](skills/doctor-harness/HARNESS-RULES.md),ADR-0012/0013)+ 校验脚本 [scripts/harness-check.py](scripts/harness-check.py)(命名/ADR 编号/归档位置三检查);设计套压测 10 题全认定 + 7 项工件修订执行;格式反馈落地(单波次上限 10 / 小波阈值 3 四副本统一);**归档子目录化**(41 份按 feature/主题迁入 10 子目录 + [archive/README.md](harness/questionnaires/archive/README.md) 索引);MIGRATION-FLOW 迁移流程沉淀。

**2026-08-11:philosophy_v4 → v5 立论重构完成(安全科学第四学科视角 + 去 AI 黑盒锚点)**——经完整 write→review→implement 闭环:grill-Q philosophy-v4(W01/W02,18 处修订)→ discipline-mapping([ADR-0014](harness/adr/0014-discipline-mapping-strategy.md) 学科挂接分层)→ grill-with-docs(去黑盒 6 点结晶,落 [CONTEXT AI 黑盒节](docs/CONTEXT.md) + [OD-19](docs/OPEN-DECISIONS.md))→ design-Q philosophy-v5([VISION/HLD/LLD](harness/design/philosophy-v5/) + [ADR-0015](harness/adr/0015-deblackbox-anchor.md))→ 设计套压测(10 项修订)→ long-running 起草(P1-P5,commit 530d0f4);v4 归 archive,v5 为 current canonical。新增 [OD-18](docs/OPEN-DECISIONS.md)(学科挂接回顾)/ [OD-19](docs/OPEN-DECISIONS.md)(形式化 V&V 缺口);v5 §八「去 AI 黑盒」(三层次 + 正交第一支柱 + 三风险 + 统合对策 + 弹性边界)。

历史:2026-07-29 methodology_v3 完成(ADR-0004/5/6);2026-08-01 action-Q 入库(第 8 个 skill)+ 首次推送;2026-08-04 三块拆分(ADR-0007);2026-08-05 repo 级设计 + v4 + harness 迁移;2026-08-08 doctor-harness 完成(第 9 个 skill);2026-08-11 philosophy_v5(安全科学第四视角)。

下一步主线([TODO.md](TODO.md)):**philosophy_v5 F026 OD-4 母本同步(仓库外)+ push 前 OD-1 发布门**;三文件层级化治理(宪法→基本法→地方法,方法论 704 行臃肿审计 + 实操升版)单独立项;CONTRIBUTING + issue 模板(OD-3);git author 身份决策;术语全面审计(B 方案)。
