---
name: grill-questionnaire
description: Batch-questionnaire stress-testing of existing plans / decisions / architecture proposals / ADR drafts / design documents. Converts grill's one-by-one stress-testing use into multi-wave Markdown questionnaires: eight fixed stress-test dimensions (unstated assumptions / one-way doors / alternatives / failure modes / blind spots / verifiability / contradictions with reality / terminology consistency) are fitted onto every key claim of the artifact; after the user answers offline, holes and blind spots go into the processing report, and sedimentable decisions / risks / terminology land in CONTEXT / ADR / OPEN-DECISIONS. Codebase-bound by default (specializes in contradictions between the artifact and existing code / decisions); degrades to pure-logic stress-testing with a review report when there is no project context. Produces findings only — never patches the artifact itself. Orthogonal to design-questionnaire (generative). Layer position (80/20 judgment-cost principle): the questionnaire-ized evolution of grill-with-docs — the 80% of predictable basic questions are stress-tested in batch (the human spends 20% of the time); the 20% of critical deep-water points (deep dependency chains, needing instant feedback) go to grill-with-docs one-by-one deep dives (the human spends 80% of the time). Triggers: stress-test the plan / review this ADR / pick holes in this design / find the holes / stress-test, "stress test", "review this", "pick holes", plus one proactive proposal after design-questionnaire produces a design draft at its close. Use when an existing plan/decision/architecture/ADR/design artifact should be stress-tested via a batched questionnaire instead of one-by-one Q&A.
lang: en
en-source: skills/grill-questionnaire/SKILL.md
zh-hash: a298a3fcc957
---

[中文](../../../skills/grill-questionnaire/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Replace "one-by-one grill stress-testing" with "multi-wave questionnaire stress-testing": read an existing artifact, generate a Markdown questionnaire from the fixed stress-test dimensions + artifact-driven concrete questions; after the user answers offline, parse item-by-item — holes go into the processing report, sedimentable items land immediately. One full stress-test pass as the norm, supplementary waves on demand, until there is nothing left to stress-test.

## Terms

- **Artifact**: the stress-test target. An existing document carrying decision content — a plan, decision record, architecture proposal, ADR draft, HLD/LLD draft, etc. It can be a file in the project or text the user pastes. The emphasis is "already exists, will be challenged" — distinct from the "draft" design-Q is still generating.

## Iron rules (inviolable)

1. **AI never decides for the human** — the questionnaire provides ★recommendations and pros/cons analysis; choosing is always the human's. The agent's role is posing questions, verifying, landing.
2. **Findings only — never patch the artifact** — artifact holes / blind spots found by stress-testing go only into the processing report (in conversation); **never directly patch the artifact file**. Artifact revision is human-initiated — the initiation mechanism is **proactively asking** at the close whether to execute (see step 5, mirroring grill-with-docs' proactive-decision style); landing happens only after the user authorizes it, and the asking itself is not patching. Benchmarks retro's "record only, never decide".
3. **The escape hatch is never re-asked** — if the user ticks 🤔 (or says "not sure / you decide" in a verbal quick-answer), run the de-risking protocol (see [PROCESSING-RULES.md](../../../skills/grill-questionnaire/PROCESSING-RULES.md)); never re-press the same question in different words. **Blocking-diversion is not re-asking**: step 4's "switch to a deep dive" is a mode-switch proposal the human rules on; it does not violate this rule.
4. **Sediment immediately, no batching** — after each wave is processed, sedimentable findings (decisions meeting the three ADR conditions, one-way-door risks, terminology conflicts) are written immediately into CONTEXT / ADR / OPEN-DECISIONS, never batched until the stress test ends.
5. **No raw information is lost** — the questionnaire file is the single source of truth; verbal quick-answers are transcribed verbatim into it; used questionnaires are archived (moved, never deleted).
6. **Verify before posing questions** (codebase mode) — for any "the artifact says X, but the code/CONTEXT/ADR says Y" contradiction to be cited into the questionnaire, the main agent must verify the original source; never pose from paraphrase.

## Main flow

### 0. Triggering and mode determination

- **Manual**: the user says "stress-test / review / pick holes / find the holes" + points at an artifact (file path or pasted text). If no artifact is given, ask for it first.
- **Proactive proposal**: when design-questionnaire closes by producing a design draft, propose once via AskUserQuestion — "stress-test the freshly produced design?". Execute only after the human confirms.
- **Mode determination**:
  - **Codebase-bound mode** (default): the artifact sits inside a project with CONTEXT/ADR/docs/code. Can check "artifact vs. reality" contradictions (D7) and terminology consistency (D8) — the most valuable part of stress-testing. **Greenfield submode** (project exists but has no code, e.g. pure design phase): still codebase-bound; D7's "reality" becomes the existing design documents/ADRs/constraints (artifact internal consistency + design vs. existing constraints), D1–D8 all open; the processing report notes "greenfield mode; D7 not checked against code".
  - **Pure-logic mode** (degraded): the artifact is free-floating text with no project context (e.g. a pasted plan). Run only the D1–D6 generic dimensions; touch no codebase; findings go into a review report in `~/notes/`, not into CONTEXT/ADR/OD. Explicitly tell the user "not checked against a codebase; recommend re-stress-testing once project context exists".
- **Inter-family self-check (batch vs. single-point)**: after mode determination, check the input shape once — this skill's stress-test target is a **formed artifact** (a document carrying decision content); if the input is actually a **single unformed question** (deep dependency chain, each next question depends on the previous one, needs instant feedback) → use AskUserQuestion to confirm switching to a grill-with-docs single-point deep dive; continue the questionnaire flow only if the human does not confirm. The criterion anchor = the three cognitive states: known · answerable offline → batch; direction known but unformed → single point; unknown unknowns → forced out by adversarial dimensions (term definitions in CONTEXT's "Grill family" section).

### 1. Reading and verification

- Read the artifact in full and extract the **key-claim list**. A key claim = a decision point / assumption / interface and constraint / acceptance criterion; background narrative and rhetoric are not mandatorily scrutinized (they serve as verifiable criteria for G6 termination — dogfood Q7).
- **Chunking oversized artifacts**: when the artifact is a multi-chapter mega-document (a whole HLD+LLD), chunk it by claim groups (e.g. HLD chapters); stress-test each chunk independently, and list cross-chunk contradictions as their own questions. Sub-wave question splitting (step 2) handles "too many questions"; artifact chunking handles "too large an artifact" — two separate dimensions (dogfood Q5).
- Codebase mode: the main agent speed-reads CLAUDE.md, CONTEXT, existing ADRs / OPEN-DECISIONS, and the code areas the artifact touches; reads `<project root>/TODO.md` (if present). Dispatch 1–3 Explore subagents as needed to verify "artifact claim vs. code / existing decision" contradictions; subagents return only structured fact lists (fact + source).
- The main agent verifies against the original source every contradiction to be cited into the questionnaire; no full re-review.
- Pure-logic mode: read only the artifact itself and run an internal-consistency check.

- **Hands-on testing and research prelude (standard flow)**: before producing the questionnaire, complete the "survey the current state → don't assume → test hands-on broadly → gather more information → save promptly" loop —
  1. **Survey the current state**: read CLAUDE.md / CONTEXT / ADR / OPEN-DECISIONS / TODO / the relevant code areas; never pose questions from memory;
  2. **Don't assume**: any fact to be cited into the questionnaire must be verified against the source or tested hands-on — never from paraphrase or memory;
  3. **Test hands-on broadly**: not just existence checks (`--version` / `brew list`) — actually run things through (compile+link / run / call-level); record the evidence (command + output + minimal program) into the question grounds;
  4. **Gather more information**: extra findings from hands-on testing (version differences, hidden dependencies, behavior details) are recorded as well;
  5. **Save information promptly**: evidence and findings are written **immediately** into the questionnaire's question grounds / processing file, not batched until after the questions are posed; what cannot be tested is explicitly marked "unverified assumption" and placed at the very front of the questionnaire (hooking into question-level ordering).

- **Lightweight mode**: when the stress-test target is small, claims are few, and no external-dependency hands-on testing is needed, you may propose the lightweight pipeline to the human — **the AI proposes, the human decides; the AI has no unilateral say** (AskUserQuestion: "judged a lightweight stress test — run lightweight?"). Lightweight pipeline = research reads only CLAUDE.md + the code areas the artifact directly touches (no full CONTEXT/ADR/OD/TODO sweep) + prefer small-wave direct asking (≤ 3 questions, no questionnaire file) + no archiving (processing summary goes into the conversation); **don't-assume / verify-first iron rules are not waived by lightness** (contradictions cited into the questionnaire are still verified against the source). **Preliminary conclusions first**: the AI does not wait for "bulletproof" before acting — put preliminary stress-test findings out for light human verification (tick / no / add a line), replacing "AI fully verifies" with "AI drafts + human lightly verifies" — isomorphic to [OD-13](../../docs/OPEN-DECISIONS.md)'s "human play-through acceptance before upgrading" / OD-19's "AI-written oracles must be human-reviewed", filling their gap at the lightweight-task layer.

- **Entry-calibration gate (lightweight mode exempt)**: before posing questions (step 2), present to the human the **artifact-understanding summary** (one paragraph) + the **key-claim list** + the **stress-test focus** (this wave's main dimensions / chunking); only generate the questionnaire after AskUserQuestion confirms/corrects the frame — intercepts "frame-level misreading" (the AI misjudges where the answer material sits cognitively, and the whole questionnaire is self-consistent inside the wrong frame). This is the in-system gate for CONTEXT's "AI same-origin questioning limitation". Lightweight mode is exempt (its "preliminary conclusions first + light human verification" is isomorphic); with chunked oversized artifacts, each chunk passes the gate once; gate confirmations/corrections are recorded into the processing report.

### 2. Generate the questionnaire

- Question sources = **fixed stress-test dimensions** ([GRILL-SKELETON.md](../../../skills/grill-questionnaire/GRILL-SKELETON.md) D1–D8, all open in codebase mode; pure-logic mode opens only D1–D6) + **artifact-driven concretization** (fit the dimensions onto the artifact's concrete claims; never copy dimension names verbatim) + **dynamic blind spots** (contradictions/undefined boundaries found during reading, new holes raised by the previous round's answers).
- Format strictly per [QUESTIONNAIRE-FORMAT.md](../../../skills/grill-questionnaire/QUESTIONNAIRE-FORMAT.md).
- Write to `harness/questionnaires/grill-<slug>-w<NN>.md` (slug = the artifact's short name, kebab-case; NN increments from 01), frontmatter `stage: grill`, status: pending. Directory lazily created. **Harness file layering: see HARNESS-RULES.md** (doctor-harness is the normative authority; not inlined here).
- Question volume: capped at 10 per wave; split into sub-waves beyond that (`grill-<slug>-w<NN>a.md`, `…b.md`).
- **Small-wave threshold**: if this wave has ≤ 3 questions, generate no questionnaire file; ask directly with AskUserQuestion instead (still with ★recommendations and the 🤔 escape hatch); questions, answers, and the processing summary are recorded verbatim into the processing report, appended to the tail of the most recent archived questionnaire.
- **Question-generation self-check (mandatory, against omissions)**: after generating the questionnaire you must grep-check "every question complete" — ① 🤔 escape-hatch count = question count; ② ❌ misframe-annotation count = question count (FORMAT rule 15, grill-Q-specific line); ③ ✍️ custom-line count = question count (every question's 🤔/❌ must be followed by a ✍️ custom line, FORMAT rule 4 — a dogfood lesson from two past omissions); ④ ★recommendations at most one per question. Count mismatch = incomplete questionnaire; complete it before handing it to the user. Commands: `grep -c '🤔 我定不了' <questionnaire>`, `grep -c '❌ 这题跑偏' <questionnaire>` and `grep -c '✍️ 自定义: ____' <questionnaire>` — the three must be equal and equal to the question count.

### 3. User answers

- Default: the user edits the questionnaire file directly (`[ ]` → `[x]`, filling ✍️ custom lines), then notifies the agent.
- Also accepted: verbal quick-answer; the agent transcribes it **verbatim** into the questionnaire file, then parses against the file.
- Do not parse until the user announces "done answering".

### 4. Process and land

- Parse item-by-item per [PROCESSING-RULES.md](../../../skills/grill-questionnaire/PROCESSING-RULES.md) (including anomalies: multiple ticks on single-choice, required items unanswered, conditional items mis-answered).
- Findings land in two classes (written the moment this wave's processing completes):
  - **Artifact holes / blind spots / one-way doors / missing alternatives** → **processing report** (in conversation), explicitly marked "artifact revision suggestions"; the human decides whether to revise the artifact. grill-Q does not touch artifact files. Among these, revision suggestions touching one-way doors / security / carrying new-wording discretion are marked **⚠** per step 5's "tiered authorization threshold".
  - **Sedimentable items** → hard-to-reverse + confusing-without-context + real-trade-off goes to `harness/adr/`; other one-way doors / major risks / questionable assumptions go to OPEN-DECISIONS.md (project-inherent files, paths untouched); terminology conflicts go to CONTEXT.md.
- Pure-logic mode: all findings go into a review report in `~/notes/` (following `~/CLAUDE.md` naming rules); nothing is written into the project's CONTEXT/ADR/OD.
- 🤔 escape hatch → de-risking protocol; never re-ask. **Blocking diversion**: if the item is a dependency prerequisite for later items (until it is settled, later items cannot be effectively processed), do not silently defer — AskUserQuestion has the human rule: ① defer into an OD (the current de-risking protocol); ② **switch on the spot to a grill-with-docs single-point deep dive** of that point, then return to this wave's processing once it crystallizes. Non-blocking items keep the standard protocol; the diversion choice and the dive's crystallization are recorded verbatim into the processing report.
- Output the **processing report** (in conversation; format per PROCESSING-RULES.md): each item's destination, new/updated files, anomaly handling, escape-hatch dispositions, next-wave candidates, coverage (8 dimensions + the artifact's key-claim review status), **quality signals** (❌ misframe rate / 🤔 escape-hatch rate / ✍️ custom rate + attribution of ❌-marked questions — wrong frame / dimension misuse / wrong fact; same-topic attribution cumulating ≥ 2 times → per [ADR-0023](../../../harness/adr/0023-skill-md-layered-slimming.md), promoted into this file's rule body; data-pipeline shape provisional, see OD-26).
- No user objection → questionnaire status: processed → archived, moved into `harness/questionnaires/archive/`, with the processing-report summary appended at the tail.

### 5. Loop and termination

- Criterion "**nothing left to stress-test**": all 8 dimensions covered (D1–D6 always; D7/D8 always in codebase mode) + every key claim of the artifact reviewed + dynamic blind spots cleared + all escape-hatch items entered into OPEN-DECISIONS.
  - Still some → wave+1 (supplementary wave), back to step 2.
  - None → present the coverage list (the review matrix of 8 dimensions × artifact key claims + landing summary), done.
- Close: output the stress-test completion list (classified summary of found holes + links to landed ADR/OD/CONTEXT files + the artifact-revision-suggestion list).
- **Proactively ask whether to execute the revisions** (mirroring grill-with-docs' proactive-decision style): after the completion list, **do not wait silently** — immediately use AskUserQuestion to ask the user "execute the revision decisions produced by the stress test?" — making "whether to land the revisions" an explicit decision point instead of a passive reminder the user must remember. Options: ① execute all revision suggestions immediately (**⚠ items excepted — confirmed one-by-one separately**) ② selective execution (the user picks which items) ③ hold off (the processing report + TODO already trace it; the user initiates manually later) ④ 🤔 unsure → de-risk (list the most reversible slices and do those first). After the user confirms execution, land the revisions per their choice — the revision is now user-authorized, not a violation of iron rule 2 (asking + authorization = human-initiated, not patching). Also remind: "if some hole is an uncertainty deep-water zone, run grill-with-docs on that point alone for a single-point deep dive".
- **Tiered authorization threshold**: batch authorization covers only "mechanical landing of confirmed findings" — items whose revision direction the user already ruled on item-by-item while answering. The following revision suggestions are marked **⚠** in the processing report, excluded from option ①, and require one-by-one confirmation: ① touching one-way doors / security; ② carrying new-wording discretion not pinned in the option description ("how to write" exceeds the "finding" scope confirmed by the answers — preventing discretion smuggling); ③ canonical-file revisions (which go through MC-04 cross-review instead). Basis = the judgment-type / pure-execution terminology boundary (CONTEXT's human-machine division of labor): what the answers ruled on are findings; what batch-delegation may land is only wording with no new discretion.
- **Optional: dogfood verification** — if the stress-test target is a product of this skill family (e.g. a design draft design-Q just produced, or this skill's own DESIGN.md), an optional step before the close: run the product through a full loop on a real small case, feeding format / flow gaps found straight back into the spec. The user may skip; both the skip and the result are recorded into DESIGN.md.

## Division of labor within the family

| | grill-questionnaire | grill / grill-with-docs | design-questionnaire | retro-questionnaire |
|---|---|---|---|---|
| scenario | stress-testing existing artifacts (adversarial) | implementation-phase single-point ambiguity, plan review (single-point deep dive) | project initialization, feature design (generative) | stage / project retrospective |
| interaction | multi-wave questionnaires, answered offline | one-by-one, waiting each round | multi-wave questionnaires, answered offline | multi-wave questionnaires, answered offline |
| skeleton | fixed stress-test dimensions D1–D8 (no content skeleton) | none | vision/hld/lld fixed skeleton | four sections + Action Items |
| landing | CONTEXT/ADR/OD + artifact revision suggestions (processing report) | CONTEXT/ADR/OD | VISION/HLD/LLD/ADR/OD/CONTEXT | retro document + TODO.md |
| artifact | findings only, never patches | — | generates artifacts | records only, never decides |

**Closed loop**: design-questionnaire produces the design draft → grill-questionnaire stress-tests → gaps feed back (OD/ADR/artifact revisions) → implementation. Both write→review steps are batched.

If stress-test processing reveals some single point is an uncertainty deep-water zone (one hole pulling out a tangle of sub-questions), suggest in the processing report that the user run grill-with-docs on that point alone, then return to the questionnaire flow.

</what-to-do>

<supporting-info>

- Stress-test dimension skeleton (this skill's template): [GRILL-SKELETON.md](../../../skills/grill-questionnaire/GRILL-SKELETON.md)
- Questionnaire format spec (engine copy; drift must be declared): [QUESTIONNAIRE-FORMAT.md](../../../skills/grill-questionnaire/QUESTIONNAIRE-FORMAT.md)
- Parsing and landing rules (engine copy; drift must be declared): [PROCESSING-RULES.md](../../../skills/grill-questionnaire/PROCESSING-RULES.md)
- This skill's design decision records (project side only): the project repository's skills/grill-questionnaire/DESIGN.md

</supporting-info>
