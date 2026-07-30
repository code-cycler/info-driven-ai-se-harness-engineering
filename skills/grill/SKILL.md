---
name: grill
description: Lightweight grilling session for GENERAL questions — relentlessly interviews the user one question at a time, walking the design tree, with a recommended answer and a "can't decide → de-risk" escape hatch on every question. Pure dialogue by default; writes a file ONLY when the user explicitly asks (placed per ~/CLAUDE.md). Use to stress-test plans/decisions NOT tied to a specific codebase. For codebase-domain work with CONTEXT.md/ADR, use /grill-with-docs instead.
---

<what-to-do>

Interview me relentlessly about every aspect of this plan/question until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

This skill is for **general** questions — decisions, plans, choices not bound to one specific codebase's domain model. Do NOT build a domain glossary or dig into a project's code structure; that is `/grill-with-docs`'s job. If the user's question is really about a specific codebase's terminology/architecture, suggest `/grill-with-docs` instead.

## How to ask questions

For EVERY question you ask, you MUST use the `AskUserQuestion` tool call (interactive UI, far easier to respond to).

### When the question has clear candidate answers
Provide 2-4 structured options. Put your recommended option first and mark it "(Recommended)" / "(推荐)" when you have a strong preference. The system auto-adds an "Other" free-text option.

### When the question is truly open-ended
Still use `AskUserQuestion`, with 2-3 "thinking direction" options; the user can always type freely via "Other".

### Always include a "can't decide" escape hatch
For EVERY question, make the last option an explicit escape hatch:
- **label**: "🤔 我定不了 → 推迟/降风险" (EN: "🤔 Can't decide — defer/de-risk")
- **description**: "我现在没把握拍板——推迟它或选个可逆的,别逼我现在定。"

Treat free-text uncertainty as the same trigger: "我不知道"/"你决定"/"不确定"/"推迟"/"不清楚"/"看你"/"难说", or "I don't know"/"not sure"/"you decide"/"defer"/"depends". When it fires, do NOT re-ask the same question — switch to the de-risk protocol below.

### Format requirements
- Clear, specific `question`.
- `header` tag (≤12 chars), e.g. "命名", "边界", "取舍".
- Each option: concise `label` (1-5 words) + `description` of the tradeoff.
- Use `preview` for code/ASCII/concrete comparisons that help the user decide.
- `multiSelect: true` only when multiple answers are valid simultaneously.

## Workflow

Ask ONE question at a time via `AskUserQuestion`. Wait for the response, process it, then ask the next. If a question can be answered by checking something (a file, a config, the filesystem) instead of asking, check it first — don't make the user answer what you can look up.

If invoked with no args, first ask (one `AskUserQuestion`) what plan/question to grill.

## Files: write ONLY on explicit request

- By default `/grill` is **pure dialogue — write nothing**.
- Generate a specific file **only when the user explicitly asks** ("把结论写成文件"/"保存"/"生成个 X"/"write this up").
- When you do write, obey `~/CLAUDE.md`:
  - Generated/temp files default to `~/scratch/`; into a project folder only if the user names one.
  - Notes/reports → `~/notes/`; never dump loose files at `~/` root.
  - Follow global naming/versioning (`_v1`/`_v2`…, no `final`/`new`/`copy`).
- NEVER auto-write `CONTEXT.md`, `ADR`, `OPEN-DECISIONS.md`, or any decision-tracking file. `/grill` does not maintain those.

## When the user can't decide — de-risk (in-chat, no files)

The default move when the user can't decide is NOT to force a choice. It's to convert the decision into a reversible one, or defer it — preserve the user's right to decide later.

### 1. Assess reversibility first
- **Two-way door** (cheap to reverse — a name, a default, a config, an internal structure) → take the recommended option, **and still note it in the in-chat「🔓 待定」list as provisional**(采用推荐项 + 双向门 + revisit trigger)。Tell the user it's cheap to change. 机制与 grill-with-docs / questionnaire 家族对齐(采用推荐项也留痕,不再「move on」了事);介质保持对话内、不写文件(2026-07-24,用户选「保持纯对话不持久化」)。
- **One-way door** (hard to reverse) → continue to step 2.

This single step dissolves most "I can't decide" moments.

### 2. Defer or shrink
- Defer entirely until more is known → say so, keep going.
- Settle only a minimal reversible slice now; leave the irreversible part open.
- Explain the trade-offs in plain terms (this closes the user's knowledge gap). If a question is too big or abstract, decompose it into concrete sub-questions.

### 3. Last resort: must settle now AND irreversible
Make a recommendation with explicit reasoning + a reversibility assessment (cost to undo, what future signal would force a change). The user's job drops to "veto or accept."

### 4. Tracking — in chat only, no file
A deferred decision stays in the conversation (e.g. a running "🔓 待定" list in your reply). Do NOT write it to any file. If the user later wants it persisted, they'll ask — then save it to `~/notes/` or `~/scratch/` per `~/CLAUDE.md`.

## End of session

When shared understanding is reached, give a concise in-chat summary of the decisions made. Only write a file if the user asks.

</what-to-do>

<supporting-info>

## /grill vs /grill-with-docs

| | `/grill` | `/grill-with-docs` |
|---|---|---|
| 问题类型 | 通用型(不绑代码库) | 绑定具体代码库领域模型 |
| 探索代码库 | 否 | 是 |
| 写文件 | 仅用户明确要求,入 `~/scratch/`/`~/notes/` | 自动写 `CONTEXT.md`/`ADR`/`OPEN-DECISIONS.md` |
| 提问方法论 | 完整(逐个问+推荐+逃生口+de-risk+设计树) | 完整(同) |

If unsure which to use: a general decision/plan → `/grill`; "stress-test this against my codebase's domain language and record decisions" → `/grill-with-docs`.

## ~/CLAUDE.md compliance

`/grill` runs often in `~/`. Any file it creates there obeys `~/CLAUDE.md`: `~/` root = project folders only; `~/notes/` = notes/reports; `~/scratch/` = generated/temp; no stray junk (`package-lock.json`, `*.log`, `*.tmp`) at root; violating files are quarantined to `~/scratch/`, never auto-deleted.

</supporting-info>
