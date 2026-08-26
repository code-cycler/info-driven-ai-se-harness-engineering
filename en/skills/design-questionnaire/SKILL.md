---
name: design-questionnaire
description: Batch-questionnaire grill for project initialization and major feature design. Generates multi-wave Markdown questionnaires (option checkboxes + escape hatch + custom answers); after the user answers offline, results land by type into harness/design/ layered design files (LN naming: the L0-vision goal layer always present, L1+/L2 added dynamically on demand; legacy VISION/HLD/LLD accepted as aliases) / ADR / OPEN-DECISIONS / CONTEXT; used questionnaires archived. In-layer loops until no more information to interrogate; crossing layers requires a human gate; the close always stops to ask about multi-threaded start. Coexists with, and divides labor from, the one-by-one grill / grill-with-docs (they handle implementation-phase single-point deep dives). Triggers: new-project initialization, new feature design, help me design, produce a questionnaire, initialize the project design, conceive / global design / phased / layered design stages. Use when starting a project or feature where the layered design (L0-vision first, more levels on demand) should be completed via batched questionnaires instead of one-by-one Q&A.
lang: en
en-source: skills/design-questionnaire/SKILL.md
zh-hash: 6b3d0ff72371
---

[中文](../../../skills/design-questionnaire/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Replace "one-by-one grill" with "multi-wave questionnaire grill": each wave generates one Markdown questionnaire file; the user answers offline (editing the file or verbal quick-answers); after answering, parse item-by-item and land; loop within the layer until no more information to interrogate.

## Iron rules (inviolable)

1. **AI never decides for the human** — the questionnaire provides ★recommendations and pros/cons analysis; choosing is always the human's. The agent's role is posing questions, verifying, landing.
2. **The escape hatch is never re-asked** — if the user ticks 🤔 (or says "not sure / you decide" in a verbal quick-answer), run the de-risking protocol (see [PROCESSING-RULES.md](../../../skills/design-questionnaire/PROCESSING-RULES.md)); never re-press the same question in different words.
3. **Sediment immediately, no batching** — after each wave's questionnaire is processed, write into the corresponding documents immediately (stage documents / ADR / OPEN-DECISIONS / CONTEXT); never batch until the stage ends.
4. **No raw information is lost** — the questionnaire file is the single source of truth; verbal quick-answers must be transcribed verbatim into it; used questionnaires are archived (moved, never deleted).
5. **Verify before posing questions** — for facts an Explore subagent surfaces, the main agent must verify the original source for anything to be cited into the questionnaire; never pose from paraphrase.
6. **Stage gates must pass the human** — within-stage termination is judged by the agent with a coverage list presented; across stages, explicit user confirmation is mandatory.

## Main flow

### 0. Triggering and mode determination

- Determine mode:
  - `init` — new project / from scratch;
  - `feature` — new-feature design in an existing project: the skeleton is adjusted per [STAGE-SKELETONS.md](../../../skills/design-questionnaire/STAGE-SKELETONS.md)'s feature-trimming section; exploring the existing codebase is a mandatory prelude.
- If the user gave no initial description, first ask for "a one-sentence idea + motivation". That is the user's homework; the agent never ghost-writes the concept.
- **Term mapping (LN naming)**: this file's historical wording vision / hld / lld maps respectively to **L0-vision (goal layer, always present) / L1-contract (contract layer) / L2-build (build layer)**; the questionnaire frontmatter's `stage` takes the **layer name** (e.g. `L0-vision`, `L1-contract`, `L2-build`, or a self-declared layer name); artifact files follow LN naming (`L<N>-<feature>.md`, see STAGE-SKELETONS general rules). The legacy trio naming (VISION/HLD/LLD) is legacy-exempt only (layout side: HARNESS-RULES section 7; migration map: its section 8).
- **Layer count and shape determination** (confirmed with the user via AskUserQuestion, replacing the old three-tier collapse):
  - **Initial layer count = minimum 1**: L0 is always generated; whether to add L1/L2 follows the **L0 self-check's five signals** as a recommendation + the human's ruling (single-layer delivery is legal for small projects / small features / small actions);
  - Medium-to-large defaults to the L0/L1/L2 three layers; multi-subsystem projects add L3+ as needed (the inter-layer insertion protocol can insert mid-course);
  - **Shape**: multi-file (one file per layer, each layer an independent W00) or single-file multi-section (small projects, the whole file one W00) — chosen at mode determination.
- **Legacy-set migration**: migrating an existing VISION/HLD/LLD design suite to LN naming goes through doctor-harness (migration map), never edited in passing by this skill.

### 1. Exploration and verification

- The main agent speed-reads the document map: CLAUDE.md (auto-loaded), docs/ index, existing VISION / CONTEXT / ADR / OPEN-DECISIONS.
- Read `<project root>/TODO.md` (if present): unfinished action items enter the questioning context.
- Dispatch 1–3 Explore subagents as needed (adaptive division of labor): existing documents, codebase, external research. Greenfield projects with no code skip the code subagent.
- Subagents return only structured fact lists (fact + source), no analytical prose.
- The main agent verifies against the original source every key fact to be cited into the questionnaire (existing decisions, term definitions, interface contracts, contradictions with code); no full re-review.
- **Environment reality verification**: for any selection/path/version of an **external dependency** (graphics/GUI/network/database libraries, toolchains, local resource paths, versions) the questionnaire will involve, test hands-on before posing questions — not just `--version` / `brew list` (library exists ≠ usable); **test the compile+link for real**: write a minimal program (e.g. a one-liner `gcc + library`), run through `init`/linking/basic invocation. Record the evidence (command, output, minimal program) into the question grounds; assumptions that cannot be tested hands-on are explicitly marked "unverified assumption" in the question stem. Never build the plan on "assume it works once installed" (项目B dogfood evidence: a certain graphics library turned out to be a compatibility shim / a companion font library was missing / the build script lacked the library link — three assumptions all wrong, exposed only at implementation time).

- **Hands-on testing and research prelude (standard flow)**: before producing the questionnaire, complete the "survey the current state → don't assume → test hands-on broadly → gather more information → save promptly" loop —
  1. **Survey the current state**: read CLAUDE.md / CONTEXT / ADR / OPEN-DECISIONS / TODO / the relevant code areas; never pose questions from memory;
  2. **Don't assume**: any fact to be cited into the questionnaire must be verified against the source or tested hands-on — never from paraphrase or memory;
  3. **Test hands-on broadly**: not just existence checks (`--version` / `brew list`) — actually run things through (compile+link / run / call-level); record the evidence (command + output + minimal program) into the question grounds;
  4. **Gather more information**: extra findings from hands-on testing (version differences, hidden dependencies, behavior details) are recorded as well;
  5. **Save information promptly**: evidence and findings are written **immediately** into the questionnaire's question grounds / processing file, not batched until after the questions are posed; what cannot be tested is explicitly marked "unverified assumption" and placed at the very front of the questionnaire (hooking into question-level ordering).

- **Lightweight mode**: when the feature is small, delivery is single-layer (L0 always present), and no external-dependency hands-on testing is needed, you may propose the lightweight pipeline to the human — **the AI proposes, the human decides; the AI has no unilateral say** (AskUserQuestion: "judged a lightweight design — run lightweight?"). Lightweight pipeline = research reads only CLAUDE.md + the directly involved code areas (no full document map) + L0 single-layer delivery + prefer small-wave direct asking + no archiving (processing summary goes into the conversation); **verify-before-posing (iron rule 5) / environment reality verification are not waived by lightness** (external dependencies are still tested hands-on). **Preliminary conclusions first**: the AI does not wait for "bulletproof" before acting — put a preliminary design draft out for light human verification (tick / no / add a line), replacing "AI fully verifies" with "AI drafts + human lightly verifies" — isomorphic to [OD-13](../../docs/OPEN-DECISIONS.md)'s "human play-through acceptance before upgrading" / OD-19's "AI-written oracles must be human-reviewed", filling their gap at the lightweight-task layer.

- **Unverified-assumption lifecycle management**: the verification disciplines (iron rule 5 / environment reality verification / hands-on prelude) anchor "at question time", but concepts / requirements evolve with the questionnaire, and early untested information may become planning support in a later stage. Add the three-piece kit:
  ① **Ledger maintenance**: at each wave's processing, fold "unverified assumptions marked in the question grounds + new information raised by user answers + last wave's leftover unverified items" into the ledger, tracked continuously across waves, never dropped with the wave. Ledger records: assumption + source (questionnaire + question number) + stage involved + status (pending / verified / stale); landing spot = each wave's processing report gains an "unverified-assumption ledger" section (preserved with the archived questionnaire's tail, single-file traceability). Track only information "that will affect later planning" — no exhaustive pursuit (anti-formalism).
  ② **Re-verify before reuse**: when a piece of information is about to become the **planning basis of the next stage's document**, re-verify before drafting (hands-on test / check the source); if unverifiable → explicitly mark "unverified + will serve as the planning basis of X", submit for user confirmation or run the de-risking protocol — never silently enter the VISION / HLD / LLD document.

### 2. Generate the questionnaire

- **Entry-calibration gate (lightweight mode exempt)**: before each layer's W00, present via AskUserQuestion the **project-understanding summary** (one paragraph: the AI's frame-level understanding of the project/feature, e.g. "CLI tool or library", "single process or multi-subsystem") + **this layer's design focus** (the decision domain this layer will interrogate) — only generate W00 after the human confirms/corrects the frame. Intercepts "frame-level misreading of the project": with the direction misread, all W00 points are self-consistent inside the wrong frame, and item-by-item yes/no can only correct after the fact, offloading cognitive burden onto the human; this is the in-system gate for CONTEXT's "AI same-origin questioning limitation", symmetric with grill-Q's entry-calibration gate. Confirmations/corrections are recorded into the processing report; with chunked oversized artifacts, each chunk passes the gate once.
- **preview (mandatory per layer, independent wave 0)**: each layer first generates an independent **W00 preview questionnaire** (`<layer-name>-w00.md`, layer names like `L0-vision` / `feature-<slug>-L1-contract`), **never co-released with W01**. **Sequencing**: W00 delivered → user answers → processing produces the cancellation list → **only then** generate W01; with a large cancellation list, split into sub-waves at the 10-per-wave cap — bloat stays controllable. preview = a list of decision defaults, one point per line = the decision point this layer will interrogate + the AI's default lean + source; whether each item is **pre-ticked is decided by the opt-in switch** (opt-in off by default: only if the user explicitly says "pre-tick" at skill start are items pre-ticked `[x]`, tick = adopt the default and land on it; when not enabled, all `[ ]`, answered item-by-item by the human); **unticked (blank) = not adopted** (that point moves into W01 for separate interrogation); **one-way-door points are never pre-ticked** (release/deletion/spending/desensitization — forced explicit tick). W00 **uses no 🤔** (a binary yes/no, no middle state; truly undecidable = untick and move to W01); the "supplementary declarations" field at the bottom is kept. **Single-file multi-section exception**: the whole file is one W00 (all layers' decision defaults merged, listed per-layer by section), preventing W00 fragmentation for small projects. W01 formal questions = deeper probing of W00's unticked (unadopted) points + mandatory open-ended skeleton items unsuited to yes/no (multi-choice / direction questions). Format per [QUESTIONNAIRE-FORMAT.md](../../../skills/design-questionnaire/QUESTIONNAIRE-FORMAT.md) "file structure (§ W00 preview questionnaire template)"; parsing per [PROCESSING-RULES.md](../../../skills/design-questionnaire/PROCESSING-RULES.md). Later waves (W02+) are gap-driven; no more previews.
- **delegate whitelist interface**: trigger = feature mode + a `delegation.md` at the project root with the master switch on + **the human explicitly says "enable the whitelist" in the current session** (three conditions AND-ed; prevents a stale whitelist silently taking effect in an old project). Once triggered, the questioning shape: decisions **inside the whitelist get no independent questions**; they merge into a single question, **"wholesale whitelist confirmation"** — listing the in-whitelist decision points + the values the AI will adopt + the whitelist entry source; the human can confirm the whole package (= all decisions auto-taken at those values) or pick items out one-by-one (picked items become formal questions for probing) — keeping human visibility while lowering only the interaction granularity. Dual trace: the processing report's "whitelist auto-decision list" (decision point / value adopted / whitelist entry source) + **per-case appends to `delegation-log.md`** (in the delegate skill's existing log format). The never-delegate list (security / merge-release / layer-file revisions etc.) is questioned as usual, doubly stacked with one-way doors never pre-ticked. Whitelist governance / revocation mechanics belong to the delegate skill; the questionnaire-side interface belongs to this skill. init mode or no delegation.md → status quo (ask the human for everything).
- Question sources = **stage skeleton** ([STAGE-SKELETONS.md](../../../skills/design-questionnaire/STAGE-SKELETONS.md)'s uncovered must-ask items for the current stage, prioritized) + **dynamic blind spots** (contradictions/conflicts/undefined boundaries found in exploration, new questions raised by previous answers).
- Format strictly per [QUESTIONNAIRE-FORMAT.md](../../../skills/design-questionnaire/QUESTIONNAIRE-FORMAT.md).
- Write to `harness/questionnaires/<stage>-w<NN>.md` (feature mode: `feature-<slug>-<stage>-w<NN>.md`), status: pending. Directory lazily created. **Harness file layering: see HARNESS-RULES.md** (doctor-harness is the normative authority; not inlined here).
- Question volume: capped at 10 per wave; split into sub-waves beyond that (`<stage>-w<NN>a.md`, `<stage>-w<NN>b.md`).
- **Small-wave threshold**: if this wave has ≤ 3 questions, generate no questionnaire file; ask directly with AskUserQuestion instead (still with ★recommendations and the 🤔 escape hatch); questions, answers, and processing results are recorded verbatim into the processing report, with the summary appended to the tail of the most recent archived questionnaire.

### 3. User answers

- Default: the user edits the questionnaire file directly (opt-in on: untick pre-ticked items / tick unticked ones; opt-in off: tick item-by-item; fill ✍️ custom lines), then notifies the agent.
- Also accepted: verbal quick-answer (e.g. "Q1: A; Q2: custom……"); the agent transcribes it **verbatim** into the questionnaire file, then parses against the file.
- Do not parse until the user announces "done answering".

### 4. Process and land

- Parse item-by-item per [PROCESSING-RULES.md](../../../skills/design-questionnaire/PROCESSING-RULES.md) (including anomalies: multiple ticks on single-choice, required items unanswered, conditional items mis-answered).
- Land item-by-item: layer documents (LN naming `L<N>-<feature>.md`; legacy VISION/HLD/LLD legacy-exempt only) → `harness/design/`; ADR → `harness/adr/NNNN-<slug>.md`; **CONTEXT.md / OPEN-DECISIONS.md / TODO.md are project-inherent files, paths untouched** (already fixed per project), **written the moment this wave's processing completes**. Action items (processing-report / retrospective outputs) go into `<project root>/TODO.md` (format: problem → action → verification timing).
- Before generating a new questionnaire, the stage gate, DoD verification, or a new-session recovery: read TODO.md first.
- 🤔 escape hatch → de-risking protocol; never re-ask.
- Output the **processing report** (in conversation; format per PROCESSING-RULES.md): each item's destination, new/updated files, anomaly handling, escape-hatch dispositions, next-wave candidates, this stage's coverage.
- Each stage's W00 processing report must contain preview statistics (ticked-adopted count, unticked-unadopted count, moved-to-W01 formal-question count) + the untick-default rate (when the opt-in switch is on; see PROCESSING-RULES.md "pre-tick safeguard"); the stage coverage checklist must check W00 existence — a stage without W00 counts as a process gap.
- No user objection → questionnaire status: processed → archived, moved into `harness/questionnaires/archive/`.

### 5. Loop and termination (LN naming: layer gates)

- Judge whether the current **layer** still has **information to interrogate**; criteria: the layer's minimum-must-contains (STAGE-SKELETONS part 2) fully covered + dynamic blind spots cleared + all escape-hatch items entered into OPEN-DECISIONS.
  - Still some → wave+1, back to step 2.
  - None → present the coverage list, then pass the **layer gate**: use AskUserQuestion to confirm once, separately — "anything to add to this layer?".
    - Additions → generate a supplementary wave.
    - None → **the L0 gate simultaneously passes the L0 self-check** (five-signal recommendation + human ruling on adding layers or not; single-layer delivery is legal); enter the next layer (or close, if the final layer is done).
  - **Layer-reopen rule**: when an already-gated layer needs reopening due to the inter-layer insertion / rollback protocol (an upper-layer contract change or an invalidated upstream premise), **only the affected layers re-pass** (not the whole chain re-run); items are labeled void / still-valid; archived questionnaires stay untouched; the reopening fact goes into the processing report.
  - **Gate reporting**: when presenting the coverage list, also present the "unverified information the next layer will depend on" list (source: the ledger; see §1 "unverified-assumption lifecycle management").
- **delegate handoff (if the project enables decision delegation)**: the init draft may start at the beginning of the engineering effort; **activation is uniformly at the L0 layer gate** — at gate confirmation the human also reviews and finalizes delegation.md; before that, run as "ask the human for everything". Mechanism and whitelist governance: see the delegate skill; preview and questionnaire flow belong to this skill, delegate only references them.
- Close: output the design-completion list (each layer's LN files / ADR / OPEN-DECISIONS links summarized), reminding the user to enter the implementation phase per the methodology (TDD, small-step commits; for implementation-phase ambiguity switch to grill-with-docs single-point deep dives).
- **Optional: dogfood verification** — see "single closing panel" question 2 below.
- **Optional: propose stress-testing (grill-questionnaire handoff)** — see "single closing panel" question 3 below (not narrowed by project size; small projects get the proposal too).
- **🛑 Closing stop point: single closing panel (mandatory stop)** — after the design chain ends, you **must** complete the four handoff questions with **one multi-question AskUserQuestion panel** — no skipping, no silence (interruptions drop from 4 to 1; each question's ruling semantics unchanged):
  1. **Multi-threaded start inquiry (panel's first question, keeping its mandatory-stop ruling status)**: "implementation phase multi-threaded (worktree) in parallel?" Single-threaded → go straight to the handoff proposal; multi-threaded → prompt switching to long-running-agent **preparation mode** (plan parallel threads + task packages; the human reviews and confirms before work starts). The anti-"AI silently opens worktrees" one-way-door semantics unchanged.
  2. **dogfood verification (optional)**: if the design product is a self-usable tool / process / template (a skill, methodology, the questionnaire itself), propose running the product through a full loop on a real small case; format / flow gaps found by dogfood are fed straight back into the spec. The user may skip; both the skip and the result are recorded into the project repository DESIGN.md's "dogfood revisions" section (project side only).
  3. **Propose stress-testing (grill-questionnaire handoff, optional)**: propose "stress-test the freshly produced design with grill-questionnaire?", hooking up the write→review loop. The user may refuse; refusal = skip.
  4. **Propose long-running-agent handoff (optional)**: if stress-testing was **refused**, immediately propose "enter long-running implementation (long-running-agent)?"; if stress-testing was **accepted**, propose again after the stress test completes. The user may refuse; refusal = skip, with manual invocation anytime afterwards. On handoff, long-running-agent reverse-derives the feature_list from this skill's **layer files (LN)** (rule: the lowest build-semantics layer; absent a build layer, from the L0 acceptance criteria — see the long-running SKILL.md), independent of session context. Design→implementation is a cross-stage handoff; entering it is the human's decision.

## Division of labor with grill / grill-with-docs

| | design-questionnaire | grill / grill-with-docs |
|---|---|---|
| scenario | initialization, feature design (batch decisions) | implementation-phase single-point ambiguity, plan review (single-point deep dive) |
| interaction | multi-wave questionnaires, answered offline by the user | one-by-one, waiting each round |
| landing | VISION / HLD / LLD / ADR / OD / CONTEXT | CONTEXT / ADR / OD |
| termination | no more information to interrogate (coverage list + gate) | shared understanding reached |

If questionnaire processing reveals some single point is an uncertainty deep-water zone (the answer pulls out a tangle of sub-questions), suggest in the processing report that the user run grill-with-docs on that point alone, then return to the questionnaire flow.

</what-to-do>

<supporting-info>

- Questionnaire format spec (engine, reusable by retro-questionnaire etc.): [QUESTIONNAIRE-FORMAT.md](../../../skills/design-questionnaire/QUESTIONNAIRE-FORMAT.md)
- Parsing and landing rules (engine, reusable by retro-questionnaire etc.): [PROCESSING-RULES.md](../../../skills/design-questionnaire/PROCESSING-RULES.md)
- Layer skeletons (LN naming; this skill's templates): [STAGE-SKELETONS.md](../../../skills/design-questionnaire/STAGE-SKELETONS.md)
- This skill's design decision records (project side only): the project repository's skills/design-questionnaire/DESIGN.md

</supporting-info>
