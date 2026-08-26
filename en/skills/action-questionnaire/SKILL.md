---
name: action-questionnaire
description: Batch detail-confirmation before informal actions — extracts the AI's understanding of an action's details into a "detail-confirmation list (confirm-list)" questionnaire; the user checks it offline, then it is parsed and archived, aligning information to ward off the AI's hallucinated self-directed decisions in an information vacuum. Reuses the design-questionnaire engine (preview re-purposed to confirm-list semantics; small-wave threshold ≤ 3), with the preview list as the default and formal question waves as backstop. Division of labor with design-phase skills: this skill handles generic informal actions unrelated to design; when an action escalates to feature level (worth a feature record, changes direction, multi-file structural change), it reminds you to switch to the dedicated skill — design-Q / grill-Q / long-running etc. Triggers: "align before we start", "confirm the details", "preflight", before starting an informal write operation that is multi-file / multi-decision / touches external dependencies. Use when about to take an informal (non-design) action whose details should be aligned with the user first to prevent hallucination-driven rework.
lang: en
en-source: skills/action-questionnaire/SKILL.md
zh-hash: f3ac1863a088
---

[中文](../../../skills/action-questionnaire/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Replace "confirming a few things by feel before starting" with "multi-wave questionnaire detail confirmation": before an action, write the AI's extracted action details and understanding into a **detail-confirmation list (confirm-list)** questionnaire; the user checks it offline (tick = understood correctly; blank = misunderstood or needs changing); blank items turn into formal questions for deeper probing or are asked directly under the small-wave threshold; confirmation results land and leave a trace immediately. **This is a confirmation questionnaire, not a generative design questionnaire** — the AI reports its understanding and the human checks it; it is not the AI proposing a plan for the human to adopt.

## Iron rules (inviolable)

1. **AI never decides for the human** — the list provides the AI's understanding and ★recommendations; confirming and choosing are always the human's. The agent's role is extracting, verifying, questioning, landing.
2. **Verify before listing (reality verification)** — whenever a list/question item involves **code facts or external dependencies** (libraries, toolchains, paths, versions, existing implementation behavior), verify against the source or test hands-on before listing it; write the evidence into the question grounds; anything unverifiable is explicitly marked "unverified assumption" in the item. **User confirmation can only align the background in the user's head; if the AI itself misread reality, the user cannot see it** — confirming "the AI's misreading + the user's rubber stamp" equals endorsing a hallucination.
3. **Write operations are confirmed by default** — before an informal action's write operation, this confirmation runs by default; **unless the project explicitly declares that operation to inherit a delegate whitelist entry** (then exempt per delegation.md). Confirmation takes precedence over delegation: a delegate whitelist does not automatically exempt this skill; exemption must be explicitly declared.
   - **Lightweight floor**: this confirmation covers only informal write operations that are **multi-file / multi-decision / touch external dependencies** (aligned with the description's trigger scope); a purely-execution change hitting all four criteria is exempt from the confirm-list — **single file + git-revertible + no network/payment/deletion + no new decisions** (exempt only when the AI has zero discretion and everything is objective; if any criterion fails, confirmation still runs).
4. **The escape hatch is never re-asked** — if the user ticks 🤔 (or says "not sure / you decide" in a verbal quick-answer), run the de-risking protocol (see [PROCESSING-RULES.md](../../../skills/action-questionnaire/PROCESSING-RULES.md)); never re-press the same question in different words.
5. **Sediment immediately, no batching** — after each wave is processed, confirmation results are archived immediately; a decision meeting the three ADR conditions (hard to reverse + confusing without context + a real trade-off) is promoted to `harness/adr/` immediately, one-way doors / major risks are promoted to `OPEN-DECISIONS.md` (placement per HARNESS-RULES.md section 6), terminology conflicts to `CONTEXT.md` — never batched until the action ends.
6. **No raw information is lost** — the questionnaire file is the single source of truth; verbal quick-answers are transcribed verbatim into it; used questionnaires are archived (moved, never deleted).
7. **No overstepping into design** — if confirmation reveals the action is really feature-level (worth a feature record, changes direction, multi-file structural change), do not go on to unfold the design inside this skill — remind the user to switch to the dedicated skill (see step 5); this skill keeps only the confirmation record.

## Main flow

### 0. Triggering and scoping

- **Trigger**: fires by default before an informal action's write operation (iron rule 3); explicit user trigger ("align a bit", "confirm the details", "preflight") also works.
- **Scoping (do this first, to prevent misuse)**: determine whether the action is feature-level — worth a feature record, changes direction, multi-file structural change, needs design first. Yes → do not start this skill; remind to switch to design-Q (needs design) / grill-Q (has an artifact to stress-test) / long-running (cross-session implementation). No → continue.
- **delegate exemption check**: read `<project root>/delegation.md` (if it exists); if the user or project **explicitly declares** this operation inherits a whitelist entry → skip confirmation, execute directly and log to delegation-log; with no explicit declaration → confirm by default.

### 1. Extraction and verification

- Extract the **action details list**: per the implicit skeleton's six elements — **goal / inputs / outputs / constraints / boundaries / dependencies** — list the AI's understanding of this action item-by-item. Each item = detail point + the AI's understanding + source (user's words / code / docs / inference). Inferred sources must be marked — "inference" is the legal entry point for hallucinations; the user must see which items are facts and which the AI filled in.
- **Verify (iron rule 2)**: for items involving code facts ("this function currently returns X") and external dependencies ("version Y is installed in the environment"), verify against the source or test hands-on before listing; write evidence into the item's grounds; what cannot be verified is marked "unverified assumption".
- **Dynamic blind spots**: contradictions found during extraction (what the user said vs. what the code does), undefined boundaries — these go straight onto the list or become formal-question candidates.

- **Hands-on testing and research prelude (standard flow)**: before producing the questionnaire, complete the "survey the current state → don't assume → test hands-on broadly → gather more information → save promptly" loop —
  1. **Survey the current state**: read CLAUDE.md / CONTEXT / ADR / OPEN-DECISIONS / TODO / the relevant code areas; never pose questions from memory;
  2. **Don't assume**: any fact to be cited into the questionnaire must be verified against the source or tested hands-on — never from paraphrase or memory;
  3. **Test hands-on broadly**: not just existence checks (`--version` / `brew list`) — actually run things through (compile+link / run / call-level); record the evidence (command + output + minimal program) into the question grounds;
  4. **Gather more information**: extra findings from hands-on testing (version differences, hidden dependencies, behavior details) are recorded as well;
  5. **Save information promptly**: evidence and findings are written **immediately** into the questionnaire's question grounds / processing file, not batched until after the questions are posed; what cannot be tested is explicitly marked "unverified assumption" and placed at the very front of the questionnaire (hooking into question-level ordering).

- **Lightweight mode**: when the action is small, has few points (confirm-list expected ≤ 5 items), and needs no external-dependency hands-on testing, you may propose the lightweight pipeline to the human — **the AI proposes, the human decides; the AI has no unilateral say** (AskUserQuestion: "judged a lightweight confirmation — run lightweight?"; complementary to iron rule 3's lightweight floor — the floor judges "exempt from confirmation", this clause judges "confirm, but through the light pipeline"). Lightweight pipeline = research reads only CLAUDE.md + the directly involved files (no full document sweep) + confirm-list direct output + no archiving (confirmation summary goes into the conversation); **iron rule 2's verify-first is not waived by lightness** (items touching code facts / external dependencies are still verified against source or tested). **Preliminary conclusions first**: the AI does not wait for "bulletproof" before acting — put a preliminary understanding list out for light human verification (tick / no / add a line), replacing "AI fully verifies" with "AI drafts + human lightly verifies" — isomorphic to [OD-13](../../docs/OPEN-DECISIONS.md)'s "human play-through acceptance before upgrading" / OD-19's "AI-written oracles must be human-reviewed", filling their gap at the lightweight-task layer.

- **Re-verify before reuse**: if the confirm-list cites information that was **confirmed before but never actually tested** (assumptions confirmed by a previous confirm-list, or the user's prior conclusions), re-verify before listing (hands-on test / check the source); if unverifiable → explicitly mark "unverified + will serve as the basis for X", never silently carried over. Hooks into the supplementary-declaration's fourth class (user prior conclusion → assumption pending verification): moving "explicitly test during analysis" forward to "re-verify before listing".

### 2. Generate the questionnaire

- **confirm-list (default first wave, independent wave 0)**: generate `confirm-<slug>-w00.md` — a detail-confirmation list, one point per line = detail point + the AI's understanding + source. Each item `[ ]`: **tick `[x]` = understood correctly** (execute on that understanding), **blank = misunderstood or needs changing** (turns into a formal question for probing, or asked directly under the small-wave threshold). W00 **uses no 🤔** (a binary correct/incorrect, no middle state); the "supplementary declarations" field at the bottom is kept. Format per [QUESTIONNAIRE-FORMAT.md](../../../skills/action-questionnaire/QUESTIONNAIRE-FORMAT.md).
- **Formal question waves (W01+, backstop)**: **preview as primary with formal question waves as backstop is this skill's intended shape** — most confirmation flows = W00 list + small-wave direct asking; W01 questionnaire files rarely appear; never force questions out just to "use the questionnaire file" (anti-formalism). W01 = deeper probing of blank W00 points + open-ended confirmation items unsuited to yes/no.
- **Small-wave threshold**: if the formal questions number ≤ 3, generate no questionnaire file; ask directly with AskUserQuestion instead (still with ★recommendations and the 🤔 escape hatch); questions, answers, and the processing summary are recorded verbatim into the processing report, appended to the tail of the most recent archived questionnaire.
- Question volume: formal waves capped at 10 per wave, split into sub-waves beyond that; the confirm-list is not bound by this cap (point count suggested 5–20 — the action is lightweight, so keep it simple).

### 3. User answers

- Default: the user edits the questionnaire file directly (`[ ]` → `[x]`, filling ✍️ custom lines), then notifies the agent.
- Also accepted: verbal quick-answer; the agent transcribes it **verbatim** into the questionnaire file, then parses against the file.
- Do not parse until the user announces "done answering".

### 4. Process and land

- Parse item-by-item per [PROCESSING-RULES.md](../../../skills/action-questionnaire/PROCESSING-RULES.md) (including anomalies: multiple ticks on single-choice, required items unanswered, conditional items mis-answered).
- Landing (written the moment this wave's processing completes):
  - **Confirmation results** → the archived questionnaire as the sole regular trace (`harness/questionnaires/archive/`, moved never deleted); later sessions can reload it. **Harness file layering: see HARNESS-RULES.md** (doctor-harness is the normative authority; not inlined here).
  - **Decisions meeting the three ADR conditions** → `harness/adr/` (decisions dug out during confirmation are recorded as usual — "informal action" is no exemption).
  - **One-way doors / major risks / questionable assumptions** → `OPEN-DECISIONS.md` (placement per HARNESS-RULES.md section 6) (revisit-trigger conditions mandatory).
  - **Terminology conflicts** → `CONTEXT.md`.
- 🤔 escape hatch → de-risking protocol; never re-ask.
- Output the **processing report** (in conversation; format per PROCESSING-RULES.md): each item's destination, new/updated files, anomaly handling, escape-hatch dispositions, confirm-list statistics (confirmed correct X / blank-corrected Y), coverage (confirmation status of the implicit skeleton's six elements).

### 5. Loop and termination

- Criterion "**no more details left to confirm**": all six implicit-skeleton elements (goal/inputs/outputs/constraints/boundaries/dependencies) confirmed + dynamic blind spots cleared + all escape-hatch items entered into OPEN-DECISIONS.
  - Still some → wave+1, back to step 2.
  - None → present the coverage list (six elements × confirmation status), **and only then start the action**.
- **Escalation handoff**: if during confirmation (or after it, before starting) the action turns out to be feature-level → immediately remind the user to switch to the dedicated skill (design-Q / grill-Q / long-running); this skill's confirmation record stays on file as input, not as a replacement for the design flow.
- Close: confirmation done → execute the action on the confirmed understanding; after the action completes, append the processing-report summary to the tail of the archived questionnaire (single-file traceability).

## Division of labor within the family

| | action-questionnaire | design-questionnaire | grill-questionnaire | grill / grill-with-docs | delegate |
|---|---|---|---|---|---|
| scenario | detail confirmation **before informal actions** (align to prevent hallucination) | project initialization, feature design (generative) | adversarial stress-testing of existing artifacts | implementation-phase single-point ambiguity (one-by-one) | pure-execution decision delegation (cross-cutting) |
| interaction | confirm-list primary + small-wave direct asking (threshold ≤ 3), formal waves as backstop | multi-wave questionnaires (preview + formal questions) | multi-wave questionnaires (D1–D8) | one-by-one, waiting each round | no human asking inside the whitelist |
| landing | archived questionnaires + three-condition promotion to ADR/OD/CONTEXT | VISION/HLD/LLD/ADR/OD/CONTEXT | processing report + ADR/OD/CONTEXT | CONTEXT/ADR/OD | delegation.md + log |
| boundary | action escalates to feature level → remind to switch to the dedicated skill | feature-level design | has an artifact to challenge | single-point deep dive | **only explicit inheritance of a whitelist entry exempts this confirmation** |

**Handoff**: this skill is a "lightweight prelude", not a replacement for the design flow. Before a design-Q-closed design enters implementation, this skill can align implementation-action details; before action items from grill-Q / retro-Q land, this skill can confirm them too. Feature-level actions discovered → hand off (step 5).

## Known limitations

- **Only aligns half of class-(a) hallucinations**: user confirmation aligns "the background in the user's head"; the half where the AI misread reality is covered by iron rule 2 (verify before listing), but verification depth is limited — for actions involving complex code behavior, keep verifying in small steps even after confirmation.
- **No replacement for design and stress-testing**: this skill has no content skeleton and no adversarial dimensions; the problems it finds are shallower than grill-Q's; feature-level actions must be handed off.

</what-to-do>

<supporting-info>

- Questionnaire format spec (engine copy; design-Q is canonical; this skill forks intentionally: confirm-list semantics + point-count suggestion 5–20): [QUESTIONNAIRE-FORMAT.md](../../../skills/action-questionnaire/QUESTIONNAIRE-FORMAT.md)
- Parsing and landing rules (engine copy, intentionally forked: small-wave threshold ≤ 3): [PROCESSING-RULES.md](../../../skills/action-questionnaire/PROCESSING-RULES.md)
- This skill's design decision records (15 stress-test rulings + rejected options; project side only): the project repository's skills/action-questionnaire/DESIGN.md

</supporting-info>
