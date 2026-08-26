---
name: grill-with-docs
description: Deep-dive engine for the 20% critical questions (80/20 judgment-cost principle): one-by-one grilling for dependency-chained, not-yet-formed decisions that need immediate feedback — the layer grill-questionnaire's batched 80% layer hands deep-water points to. Two modes: codebase-bound (default — challenges your plan against the existing domain model, sharpens terminology, updates CONTEXT.md/ADRs/OPEN-DECISIONS.md inline) and general mode (absorbs the retired grill's niche — no codebase exploration, zero auto-write, pure dialogue). When the user can't decide a question, de-risks it — defers or makes it reversible instead of forcing a choice. Use when user wants to stress-test a plan point-by-point against their project's language and documented decisions, or for general one-at-a-time deep-dives not tied to a codebase (general mode).
lang: en
en-source: skills/grill-with-docs/SKILL.md
zh-hash: 1b41c6cdc2cb
---

[中文](../../../skills/grill-with-docs/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original; English-dominant sections are carried over verbatim, with only the residual Chinese parts translated (i18n-support P4 special case, L2 §2). The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

## Modes: codebase-bound (default) / general (carrying grill's niche)

> Origin: grill's retirement preparation (retro skill-family W01 Q6 + the user's ruling "add the mode first + grill observation period"). This skill carries grill's "general-question single-point deep-dive" scenarios; grill entered its observation period.

This skill defaults to **codebase-bound mode** (challenge against codebase domain model + auto-write CONTEXT/ADR/OD). When the question is **general-type** (not bound to a specific codebase: non-project plans / pure logical reasoning / cross-project decisions), switch to **general mode**:

- **Determination (operable discrimination)**: does the answer depend on some concrete codebase's domain model / terminology / code facts? **No → general mode.** Typical scenarios: ① cross-project / no-project decisions (choosing a methodology, setting plans, evaluating an unbuilt-repo idea); ② pure logic / conceptual reasoning (weighing abstraction options, sorting out ideas that don't depend on existing code); ③ methodology meta-questions ("which skill should I use" — questions not aimed at concrete code). **Counter-boundary (must be codebase-bound)**: the answer depends on "how this project's code is currently written / how its terms are defined" — e.g. "should this field be nullable", "what is this module's responsibility".
- **General-mode behavior**: **no codebase exploration, no domain glossary building, no auto-writing CONTEXT/ADR/OD** — pure dialogue, zero trace; files are written only when the user explicitly asks (following `~/CLAUDE.md`: generated files go to `~/scratch/`, notes to `~/notes/`). The questioning methodology (one-by-one + recommendation + escape hatch + de-risk) is identical to codebase-bound mode.
- **Misjudgment fallbacks (both installed)**:
  1. **Entry confirmation**: after judging general / a trigger phrase hits ("general question / not codebase-bound / don't write files / pure logic"), confirm once with AskUserQuestion — "run general mode (zero trace)?" — the AI never switches on its own (general vs. codebase-bound affects whether traces are left; that is a human call); intercepts entry misjudgment.
  2. **Mid-course switch back**: under general mode, if it turns out codebase facts are actually needed, prompt to switch back to codebase-bound mode; intercepts mid-course misjudgment.
- **Zero-trace boundary (AI proposes + human decides)**: under general mode, when the output is a **reusable decision** (a conclusion worth keeping across sessions), the AI asks once with AskUserQuestion — "is this decision worth landing?" — and the human chooses whether to write it, preventing reusable decisions from being silently dropped by zero-trace while avoiding over-interruption; the user can also request a landing anytime.

## Mid-course phase change: discovering batchability → switch to a questionnaire

If a deep dive reveals the question at hand is really "**a batch of independent confirmation points answerable offline**" (shallow dependency chains, answer material already in the human's head, no instant feedback needed — the "known · answerable offline" state among the three cognitive states), propose switching to grill-questionnaire batch stress-testing with AskUserQuestion — **the AI proposes, the human decides**; never switch unilaterally; conclusions already crystallized follow the existing handoff (crystallize into an artifact → grill-Q re-stress-tests). The reverse phase change (grill-Q blocking escape hatch → switch to this skill's deep dive) is carried by the grill-Q spec and is not repeated here.

## How to ask questions

For EVERY question you ask during the grilling session, you MUST use the `AskUserQuestion` tool call. This gives the user an interactive UI with clickable options, making it much easier to respond.

### When the question has clear candidate answers

Provide 2-4 structured options in the `AskUserQuestion` call. Always include your recommended option first and mark it with "(Recommended)" when you have a strong preference. The system automatically provides an "Other" free-text option, so the user can always type a custom answer.

Example question types that work well with options:
- "Which approach should we use?" -> List the viable approaches as options
- "Is this X or Y?" -> Two options: X and Y
- "How should we handle edge case Z?" -> List the strategies as options
- "What's the scope of this feature?" -> List scope levels as options

### When the question is truly open-ended

Still use `AskUserQuestion` but with 2-3 "thinking direction" options that help the user structure their response, plus they can always type freely via "Other".

### Always include a "can't decide" escape hatch

A recommended answer is not enough: it hands the user a *conclusion* but doesn't resolve *why* they can't decide, and it doesn't make the decision *safe* to make. The user often genuinely cannot choose — they lack domain knowledge, lack the experience to predict consequences, or can't anticipate the situations that will arise. Give them an exit.

For EVERY question, make the last option an explicit escape hatch:

- **label**: "🤔 Can't decide — defer/de-risk" (Chinese: "🤔 我定不了 → 推迟/降风险")
- **description**: "I don't have the knowledge/experience to pick now — defer it or pick something reversible, don't force me to commit."

This must always be present, so the user never has to *remember* the exit exists — which matters precisely because they are already uncertain. Also treat free-text "Other" answers that signal uncertainty as the same trigger: "我不知道", "你决定", "不确定", "推迟", "不清楚", "看你", "难说" (and the English equivalents: "I don't know", "not sure", "you decide", "defer", "depends").

When the escape hatch fires, do NOT re-ask the same question. Switch into the de-risk protocol below.

### Format requirements

- Each question should have a clear, specific question in the `question` field
- Use `header` to tag the question topic (max 12 chars), e.g. "Data Model", "Edge Case", "Naming"
- Each option should have a concise `label` (1-5 words) and a `description` explaining the tradeoff
- Use `preview` field when showing code snippets, ASCII diagrams, or concrete examples helps the user compare options visually
- Set `multiSelect` to `true` only when multiple answers are genuinely valid simultaneously

### Workflow

Ask ONE question at a time using `AskUserQuestion`. Wait for the user's response before moving to the next question. After receiving the answer:
1. Process the response
2. Update CONTEXT.md or propose an ADR if a term/decision was resolved
3. Ask the next question

If a question can be answered by exploring the codebase, explore the codebase instead.

## When the user can't decide — the de-risk protocol

When the user signals they can't decide (escape hatch or uncertainty in free text), the default move is **not** to force a decision. It's to **convert the decision into a reversible one, or defer it** — preserve the user's right to decide later, when they have more knowledge, experience, or context. They should never have to cross a one-way door in the dark.

Work through these steps in order:

### 1. Assess reversibility first

Is this a **one-way door** (hard to reverse — database, public API shape, auth provider, deployment target) or a **two-way door** (cheap to reverse — a name, an internal structure, a config flag, a default value)?

- **Two-way door** → take the recommended option, **and still record it in `OPEN-DECISIONS.md` as provisional** (adopting the recommendation + two-way door + revisit trigger). It's reversible by definition — tell the user it's cheap to change — but adopting the recommendation also leaves a trace; no longer "Nothing to defer"; no information is lost (aligned with the questionnaire family's escape-hatch mechanism; step 4 already covers provisional → OD).
- **One-way door** → continue to step 2.

This single question dissolves most "I can't decide" moments: a lot of what people agonise over is actually a two-way door.

### 2. Try to defer or shrink the decision

Split the decision into "must settle now" vs "can settle later":

- Can it be **deferred entirely** until more is known? → defer it (step 4 records it).
- Can only a **minimal reversible slice** be settled now, leaving the irreversible part open? → settle the reversible slice; defer the rest.

Use the supporting tools to find the *most reversible placeholder*, not to force a final pick: explore the codebase and existing docs for how the rest of the system leans, search the web for how the problem is typically handled, and **explain the trade-offs in plain terms** (this also closes the user's knowledge gap). If the question is too big or abstract to answer, **decompose** it into concrete sub-questions — a smaller question is often answerable where the big one wasn't.

### 3. Last resort: must settle now AND irreversible

Only if the decision genuinely can't be deferred and is one-way: make a **recommendation with explicit reasoning** *and* a **reversibility assessment** — how costly to undo, and what future signal would force a change. The user's job drops from "decide which option is best" to "veto or accept" — a far lower bar. Record it as provisional with a revisit trigger (step 4).

### 4. Record it in OPEN-DECISIONS.md

Every deferred or provisional decision goes into `OPEN-DECISIONS.md` (create lazily on first use). A deferred decision is only safe if it stays visible and has an alarm clock — otherwise it silently fossilises into the design. Each entry captures: the question, *why* it's deferred (knowledge gap / experience gap / can't anticipate), the current reversible placeholder, the reversibility, and the **trigger condition** — the signal or information that should bring you back to settle it for real. See [OPEN-DECISIONS-FORMAT.md](../../../skills/grill-with-docs/OPEN-DECISIONS-FORMAT.md). Placement: `harness/` root in repos that have `harness/`, else `docs/` (HARNESS-RULES.md section 6).

</what-to-do>

<supporting-info>

## Domain awareness

During codebase exploration, also look for existing documentation:

### File structure

Most repos have a single context:

```
/
├── CONTEXT.md
├── docs/
│   ├── adr/
│   │   ├── 0001-event-sourced-orders.md
│   │   └── 0002-postgres-for-write-model.md
│   └── OPEN-DECISIONS.md      ← deferred/provisional decisions + revisit triggers
└── src/
```

If a `CONTEXT-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── CONTEXT.md
│   │   └── harness/adr/                 ← context-specific decisions
│   └── billing/
│       ├── CONTEXT.md
│       └── harness/adr/
```

Create files lazily — only when you have something to write. If no `CONTEXT.md` exists, create one when the first term is resolved. If no `harness/adr/` exists, create it when the first ADR is needed. If no `OPEN-DECISIONS.md` exists, create it when the first decision is deferred via the de-risk protocol.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `CONTEXT.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible — which is right?"

### Update CONTEXT.md inline

When a term is resolved, update `CONTEXT.md` right there. Don't batch these up — capture them as they happen. Use the format in [CONTEXT-FORMAT.md](../../../skills/grill-with-docs/CONTEXT-FORMAT.md).

`CONTEXT.md` should be totally devoid of implementation details. Do not treat `CONTEXT.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](../../../skills/grill-with-docs/ADR-FORMAT.md).

### Track open decisions

When a decision is deferred or made provisionally (because the user couldn't decide and you de-risked it instead of forcing it), record it in `OPEN-DECISIONS.md` **immediately** — don't batch. A deferred decision with no revisit trigger is just a forgotten decision wearing a disguise. When a later session finally resolves one, remove it from the list (and write the resolution as an ADR if it qualifies). Use the format in [OPEN-DECISIONS-FORMAT.md](../../../skills/grill-with-docs/OPEN-DECISIONS-FORMAT.md).

</supporting-info>
