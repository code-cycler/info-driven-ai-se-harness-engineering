---
mode: feature
wave: 0
stage: confirm
created: 2026-08-03
status: archived
---
# 问卷 confirm W00 · 细节确认清单（AI 汇报理解，人核对）

> **本波是细节确认清单**（独立 wave 0）：把 AI 对本次行动细节的理解逐条列出，人只做「对/不对」核对。
>
> **作答规则**：
>
> - 勾 `[x]` = **理解正确**（按该理解执行）
> - 留空 `[ ]` = **理解有误或要改** → 该要点转正式题深究（或小波直接问）
> - 本波**不用 🤔**（对/不对二选一，无中间态）；「大体对但要改一两处」→ 留空，转正式题时在深究题里给正确值
>
> 来源标注于〔〕：**〔推断〕= AI 填的，重点核对**；〔用户原话 / 代码 / 文档〕= 有据。

## 细节确认清单

### 目标

- [X]  **1 行动定义**：本次「根据最近的更新，更新各个文档」= 执行 [TODO.md](TODO.md) 🟢 节已实证的 **「canonical 同步(7→8)」**——门槛已过（2026-07-31 action-Q 首案例），同步范围 grep 实证 6 文件 7 处，TODO 明载「同步执行另起行动」，本次即为该行动。〔文档：TODO.md 🟢 节「canonical 同步(7→8)」；用户本次请求〕
- [X]  **2 数量表述统一**：各 canonical 文档「7 个核心 skill」→「8 个核心 skill」，action-questionnaire 为第 8 个（skills/ 目录实测 8 个：action-Q / delegate / design-Q / grill / grill-Q / grill-with-docs / long-running / retro-Q）。OD-13「家族仍 7 个」是 2026-08-01 对 **shadow** 的裁决（shadow 不入家族），不构成 action-Q 不入家族的依据；OD-13 重访触发②「第 8 个 skill」与同步后数量冲突，处理见边界条目 12。〔代码：`ls skills/`；文档：TODO.md 🟢 节、OPEN-DECISIONS.md OD-13〕

### 输入

- [X]  **3 同步素材**：action-Q 的家族定位取 [skills/action-questionnaire/SKILL.md](skills/action-questionnaire/SKILL.md)「与家族的分工」表（确认式问卷 / 轻量前奏 / 非正式行动写操作前触发）+ DESIGN.md（15 题裁决）；不新造内容。〔文档：action-Q SKILL.md、DESIGN.md〕
- [X]  **4 命中清单（已 grep 核实）**：`7 个核心`表述分布在 —— CLAUDE.md:37（「7 个 skill 不是孤立的」）、README.md:47（表格标题）+ 65（仓库结构）、CONTEXT.md:40（skill 家族节）、ADR-0003:13（「7 个核心方法论 skill」）、v3:13（「7 个 Claude Code skill 是它的执行体」）+ §8.3 分类表（无 action-Q 行）、OPEN-DECISIONS.md:27（OD-2 依赖计数）。〔实测：`grep -rn "7 个核心|7 个 skill|7 个方法论"`〕

### 输出

- [X]  **5 README 三处**：① 核心 skill 表格加 `action-questionnaire` 行（用途：行动前细节确认/确认式问卷）；② 「## 7 个核心 skill」→ 8；③ 仓库结构 `skills/ 7 个核心方法论 skill` → 8。另有 mermaid 流程图（快速上手）补 action-Q 节点——该图加于 action-Q 入库前（commit dfe0491），图上只有 7 个 skill。〔代码：README.md:47,65 + mermaid 图；推断：mermaid 图补节点属同一「canonical 同步」目标，TODO 实证范围未单列〕
- [X]  **6 v3 三处**：① 开头「7 个 Claude Code skill 是它的执行体」→ 8；② 开头 mermaid 图（与 README 同源同改）补 action-Q 节点；③ §8.3 分类表加「**确认**」类行（`action-questionnaire` | 非正式行动前细节确认 | 触发词「对齐一下/确认细节/preflight」）。〔代码：methodology_v3.md:13、§8.3 表；TODO.md 🟢 实证「v3(§快速上手/§8.3)」〕
- [X]  **7 CONTEXT / CLAUDE.md / ADR-0003**：CONTEXT「skill 家族」节改 8 个并补 action-Q 一句话定义（确认式问卷，非正式行动写操作前对齐细节防幻觉）；CLAUDE.md:37 改 8 个；ADR-0003:13 改 8 个。〔代码：CONTEXT.md:40、CLAUDE.md:37、ADR-0003:13〕
- [X]  **8 OD-2 依赖计数更新**：OPEN-DECISIONS.md:27 现记「AskUserQuestion 9 处、subagent 6 处」（旧快照），重测 8 个 skill 的 SKILL.md：**AskUserQuestion 18 处、subagent 4 处**（2026-08-03 实测），同步时更新为实测值并注日期。〔实测：`grep -c` 逐 skill 统计，design=4/4、grill=4/0、grill-Q=3/1、with-docs=4/0、retro=2/0、action-Q=1/0、delegate=0/0、long-running=0/0〕

### 约束

- [X]  **9 脱敏门**：改完跑 `python3 scripts/desensitize.py .` 0 命中才能提交；编辑 .md 不引入真实项目名 / 路径 / 人名（映射表外置本地）。〔文档：CLAUDE.md「push 前三道门」、OD-1〕
- [X]  **10 提交方式**：全部改动单条 commit（如 `docs: canonical 同步(7→8) + 最近更新落盘`），**不 push**（push 为单向门，需另行显式要求）。〔推断：用户本次未提 push，本仓库 push 前需 OD-1 三道门全绿 + 用户确认〕

### 边界

- [X]  **11 CLAUDE.md「当前仓库状态」节刷新**：现文停在 7-29 叙事（「下一步主线：grill-Q 压测 v3 成稿 → 远程仓库建立 + push」），但远程仓库已建立并首次推送（commit d2252ae，2026-07-29/08-01）、脱敏语义人审已完成（909c030）、OD-4 母本标注已执行（b16328e）、action-Q 已入库（909c030）、OD-13/14 已新增（1f0fd12）。刷新到 8-03 现状（下一步主线指向 TODO 当前态）。〔代码：CLAUDE.md 状态节 vs git log 近 10 提交；推断：状态节过时属「根据最近更新更新文档」的自然范围，TODO 实证未单列〕
- [X]  **12 OD-13 触发②措辞连带修订**：OD-13 重访触发条件②「决定是否家族化（第 8 个 skill）或废弃」——若 action-Q 计入家族（8 个），shadow 家族化应为**第 9 个**；修订为「家族化（新增为家族成员）」或「第 9 个」。〔文档：OPEN-DECISIONS.md OD-13 重访触发②；推断：措辞修订〕
- [X]  **13 全局 `~/.claude/CLAUDE.md` 不在本次范围**：「Grill 类 skill 触发边界」表（design-Q / grill-Q / retro-Q 三行）缺 action-Q——但该表标题为「Grill 类」，action-Q 是确认式问卷非 Grill 决策引擎，且该文件在仓库外。**默认不动**，如需补行请勾掉本条并说明。〔推断：仓库外文件默认不越界修改〕
- [X]  **14 v3 正文不扩写**：本次只在实证范围（快速上手图 + §8.3 表）补 action-Q，**不**在 v3 正文（§4.2 环节详解 / §5.3 两族表）展开 action-Q 机制论述——action-Q 机制是否入方法论正文（如 §4.2 问答对齐节挂执行体）是超出本次实证范围的设计问题，如需顺带处理请说明。〔推断：按 TODO 实证范围执行，防范围蔓延〕

### 依赖

- [X]  **15 工具链可用**：`python3` + `scripts/desensitize.py` 可运行（脚本存在，python3 可用）。〔代码：scripts/desensitize.py 存在；python3 为本机已装〕

## 补充声明

（想补充的写这里，agent 处理时必读）
