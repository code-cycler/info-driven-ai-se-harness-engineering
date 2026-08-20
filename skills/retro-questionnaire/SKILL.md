---
name: retro-questionnaire
description: 项目/阶段复盘的批量问卷式回顾。按方法论四节(进展顺利/出问题与原因假设/架构偏离/学到什么)+ Action Items 生成 Markdown 复盘问卷,用户离线作答后落盘宿主项目 docs/retro/<主题>_vN.md 与 TODO.md,已用问卷归档。阶段 DoD 核验后主动提议,也可随时手动触发(及时记录,类似 memory)。触发:阶段复盘、项目复盘、"复盘一下"、"做个 retro"、retro、DoD 核验通过。Use when a development stage or project is done and a structured retrospective questionnaire should be generated, answered, and sedimented.
---

> 治理历史见本目录 CHANGELOG.md;有意分叉见 FORK-NOTES.md。

<what-to-do>

把复盘从「靠自觉」变为「有触发、有结构、有落盘」:五源读取 → 生成 retro 问卷 → 用户作答 → 落盘 retro 文档与 TODO.md → 归档。问卷引擎为本目录内的副本(复制自 design-questionnaire,漂移需声明,见 [DESIGN.md](./DESIGN.md))。

**作用对象是宿主项目**(被复盘的项目):出题依据从宿主项目读取,retro 文档、TODO.md、问卷归档全部落盘在宿主项目,不落本 skill 目录。

## 铁律

1. **复盘只记录,不决策** — 架构偏离只记录在 retro 文档;后续动作(更新设计文档 / 新 ADR)由人发起。
2. **AI 不替人决策** — 反思题的选项是「常见原因假设清单」,真实原因以用户的 ✍️ 自定义为准。
3. **即时沉淀** — retro 文档、TODO.md、归档,处理完即刻写。
4. **原始信息不丢失** — 问卷文件是唯一事实源;对话速答逐字转写;已用问卷只归档不删除。
5. 引擎铁律全部继承(见 PROCESSING-RULES.md 与 QUESTIONNAIRE-FORMAT.md)。

## 触发

- **主动提议**:检测到宿主项目某阶段 DoD 核验通过 → 用 AskUserQuestion 提议复盘,人确认后执行。
- **手动**:用户说「复盘一下」「做个 retro」等,随时触发,及时记录(类似 memory)。

## 主流程

1. **五源读取**(接口契约,不得偏离):
   1. 阶段设计文档(HLD / LLD / DoD)
   2. `git log`(本阶段提交)——**非 git 项目**:此源跳过,在 retro 文档「五源读取」节注明「本项目非 git 仓库,git log 源跳过」;不伪造、不凭记忆补
   3. `TODO.md` 未完成项
   4. 上一份 retro 的 Action Items(→ 新 retro 文档开头设「Action Items 回顾」节)
   5. 与用户交流中的有价值内容(反馈、决定、洞察)
- **调研与核实前置(标准流程)**:生成复盘问卷前,完成「调研现状 → 不假设 / 核实 → 多获取信息 → 及时保存」闭环——
  1. **调研现状**:五源读取(上)之外,读项目现状(progress / feature_list / 最近提交),不凭记忆;
  2. **不假设 / 核实**:复盘问卷中的事实声明(如「X 已完成」「某环节顺利」)需核实(git log / 文档 / 代码)而非凭记忆;
  3. **多获取信息**:读取中发现的额外事实(未记录的问题、偏离、遗留)一并记入问卷出题依据;
  4. **及时保存信息**:证据与发现立即写入问卷 / retro 文档,不攒到处理时。

2. **生成 retro 问卷**:按 [RETRO-SKELETONS.md](./RETRO-SKELETONS.md) 出题,格式按 [QUESTIONNAIRE-FORMAT.md](./QUESTIONNAIRE-FORMAT.md),写到宿主项目 `harness/questionnaires/retro-<主题>-w<NN>.md`。本波问题数 ≤ 3 时不生成文件,直接 AskUserQuestion 提问(小波阈值)。**harness 文件分层见 HARNESS-RULES.md**(doctor-harness 规范权威,不内联复制)。
3. **用户作答**:文件编辑为主;对话速答逐字转写进问卷文件。用户宣布「答完了」之前不解析。
4. **处理落盘**(按 [PROCESSING-RULES.md](./PROCESSING-RULES.md)):
   - retro 文档:宿主项目 `docs/retro/<主题>_vN.md`(_vN 递增,禁 final/new/copy),结构 = 四节 + Action Items
   - 行动项 → 宿主项目 `TODO.md`(问题 → 行动 → 核验时机)
   - 处理报告(对话内)
   - 问卷归档 `harness/questionnaires/archive/`,尾部附处理报告摘要
5. **终止**:一份 retro 通常一波完成;答案引出的新问题按「再无可盘问的信息」判断是否出补充波。

</what-to-do>

<supporting-info>

- retro 骨架模板(四节 + Action Items):[RETRO-SKELETONS.md](./RETRO-SKELETONS.md)
- 引擎副本(漂移需声明):[QUESTIONNAIRE-FORMAT.md](./QUESTIONNAIRE-FORMAT.md)、[PROCESSING-RULES.md](./PROCESSING-RULES.md)
- 本 skill 设计文档:[docs/VISION.md](./docs/VISION.md)、[docs/design/hld_v1.md](./docs/design/hld_v1.md)、决策索引 [DESIGN.md](./DESIGN.md)

</supporting-info>
