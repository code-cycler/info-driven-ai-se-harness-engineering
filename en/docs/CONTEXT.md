---
lang: en
en-source: docs/CONTEXT.md
zh-hash: 20578677de6f
---
[中文](../../docs/CONTEXT.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../harness/adr/0025-english-mirror-drift-governance-integration.md)). The English Glossary at the end of this file is the single source of truth for translated terms.

# CONTEXT — Glossary

> A pure glossary: concept definitions only — no decisions (see [harness/adr/](../../harness/adr/)) and no implementation details.
> First created: 2026-07-28.
>
> **Normative navigation (2026-08-14, grill-Q methodology-improvement W01 Q10)**: the single authority for adjudicating document conflicts = [CLAUDE.md](../../CLAUDE.md) (methodology claims > ADR > CONTEXT terms > skill specs > practice file); it is not duplicated here. This table adds only the layer CLAUDE.md does not cover: **intra-suite layer adjudication — an HLD's contracts (interface contracts / global technology choices / module boundaries) take precedence over LLD detail; when an LLD conflicts, the HLD governs, and changing a contract must go through the [ADR-0021](../../harness/adr/0021-design-implementation-deviation-governance.md) governance-deviation path** (W01 Q1 ruling; the spec landed together with design-Q's digital-levels revamp — see the corresponding TODO entry).

## Dual pillars

The methodology's core ideas, multiplied together — either at zero makes the product zero (details in [methodology_v5 §1](methodology/methodology_v5.md)):

- **Pillar one · Information as the Core**: the essence of collaborating with AI is information flow; the bottlenecks are the quality and quantity of effective context, and countering AI's hallucinated self-directed decisions in an information vacuum.
- **Pillar two · Engineering Mastery = AI × Software Engineering**: AI is the accelerator; software engineering discipline (design-first / TDD / code review / ADRs / retrospectives) is the skeleton.

## Pillar-one terminology layering (v3)

The layer membership of pillar-one terms (details in the methodology file [§1.1 / §2.1](methodology/methodology_v5.md) and the philosophy file [§1.2](methodology/philosophy_v7.md)):

- **Information gap** = the root-cause framework of rework, in two types: the human-human gap (solved by AI-replacing roles) and the human-AI gap (solved by questionnaire alignment); rework is its visible symptom.
- **Information flow** = the process model: context enters the model, the model produces results, results sediment into new information.
- **Effective context** = the quality metric (metric layer): the amount of information hard to hallucinate from that precisely hits the current task; empirical values ≈ 120k for 200k models, ≈ 400k for 1m models.
- **Background absence** = the hallucination root cause (mechanism-layer trigger), in two classes (a)(b) (below).
- **Information vacuum** = the vivid alias of background absence: the vacuum zone where the AI acts on its own.
- **Mechanism layer / metric layer / symptom layer** = the three-layer thesis model (a causal chain, not peer categories): mechanism layer (AI's hallucinated self-directed decisions, root cause) → metric layer (effective context) → symptom layer (rework).
- **vibe coding** = coding without briefing background or setting constraints, AI improvising; the methodology's primary governance target.
- **(a)(b) blind spots** = the two classes of background absence: (a) known but unwritten → captured by preview / questionnaires; (b) not even known to yourself (implicit assumptions) → forced out by adversarial grilling.

## Human-machine division-of-labor terms

- **Judgment-type decision** = a decision requiring the choice of goals, options, priorities, or risk trade-offs, or confirming whether requirements / design / tests match intent; it changes or confirms "what to do, why, and whether the result is accepted" — it cannot be treated as pure execution merely because execution cost is low.
- **Pure-execution decision** = a decision that, within human-approved goals and specs, only selects execution details that change no intent, scope, or risk boundary; it answers "how, per established requirements", not "what should be done".
- **Their relationship** = "AI must not autonomously make judgment-type decisions" does not mean AI cannot perform actions with local choices; only choices explicitly confined to pure execution are within scope of the delegation discussion.

**Minimal discrimination table (v7, continuing W02)**:

| Discriminating question | Classification | Default handling | Example |
|---|---|---|---|
| Does it change goals, priorities, or the "why"? | Judgment-type decision | the human must choose and confirm | changing "build an export" into "build real-time sync" |
| Does it change risk boundaries, acceptance criteria, or irreversible state? | Judgment-type decision | the human must review; pause the action if needed | deleting data, releasing a version, changing acceptance gates |
| Does it only choose reversible execution details within approved goals, specs, and boundaries? | Pure-execution decision | delegable under whitelist, traceability, and emergency-off constraints | adjusting function names or file order within an approved field mapping |
| Cannot tell whether it changes any of the above? | Doubtful | treat as judgment-type; ask the human first | AI claims "just an optimization" but impact scope is unclear |

This table is a terminology discrimination contract, not delegate's complete whitelist or runtime implementation spec.

## Terminology governance (2026-08-05 audit)

Repo-level design P2 terminology compromise audit (2026-08-05): each word was adjudicated by direction (replace where a discipline-standard word exists with overlapping semantics; retain where no discipline counterpart exists or the discipline word's semantics drift) — **all 8 terms retained**: the core terms all carry author-specific semantic structure that standard discipline words cannot replace losslessly; the discipline-reference annotations:

| Term | Discipline reference | Verdict | Reason |
|---|---|---|---|
| 信息断层 (information gap) | Human factors: information-processing defects / information gaps | retained | the two-type distinction (human-human / human-AI) is author-specific structure; discipline words have no such distinction |
| 信息流转 (information flow) | Generic: information flow | retained | a process model; a generic concept |
| 有效上下文 (effective context) | Human factors: cognitive load / working memory (semantically related) | retained | no single standard word; **the two scales are non-convertible (2026-08-10 grill-Q W01 Q5): 120k/400k tokens = dilution of model attention ≠ human cognitive load (human decision fatigue) — related by analogy only** |
| 背景缺失 (background absence) | Human factors: loss of situation awareness | retained | the (a)(b) distinction is the author's core concept; **discipline precision (2026-08-10 grill-Q W01 Q4): background absence = the perception layer of situation awareness (Endsley); AI guess-completion = mental-model / schema-driven (Norman), not situation awareness itself** |
| 信息真空 (information vacuum) | no direct counterpart | retained | a vivid alias, a mechanism-layer key phrase; subordinate to background absence (already defined); not merged for now (merging would rewrite an ADR-0005 core substring) |
| 机制层/度量层/症状层 (mechanism/metric/symptom layers) | model-structure names | retained | a causal-chain model, not a coined-concept class |
| vibe coding | industry term | retained | not coined |
| (a)(b) 盲区 ((a)(b) blind spots) | none | retained | the author's core distinction |

**Three-condition gate for new words** (mandatory for future terms): ① no discipline-standard counterpart; ② necessary to the methodology (not expressible with existing words); ③ clearly defined (in this table or at first definition in the body).

## Project discipline map (2026-08-10, grill-Q discipline-mapping W01 output)

> The philosophy body anchors only the "thesis-core disciplines" (whose mechanisms directly support the methodology's theses); this section carries the **full discipline landscape** — disciplines with practice correspondence but no thesis contribution. Anchoring criteria and tiering strategy in [ADR-0014](../../harness/adr/0014-discipline-mapping-strategy.md).
>
> **Nature annotation (2026-08-18, grill-Q first-principles W01 Q4)**: this map is **expository decoration / inspiration provenance** — the thesis logic does not depend on this table (load test: delete all discipline footnotes and none of the four theses collapses); the table's value = retrieval entry and inspiration tracing, not argumentative grounds, generating no verification obligations.

### Thesis-core disciplines (enter the philosophy body)

| Discipline | Thesis mechanism it supports | Philosophy anchor |
|---|---|---|
| Human factors engineering | background absence → loss of situation awareness / guess-completion (mental models) | §1 |
| Software engineering | no guardrails → AI output quietly degrading | §2 |
| Operations research | judgment cost as a limited resource (80/20) | §3 |
| Safety science / reliability engineering / resilience engineering | system-level safety + failure anticipation + WAI/WAD | the v5 **fourth discipline perspective** anchor (clarified 2026-08-10 as non-pillar; originally "fifth discipline perspective", renamed 2026-08-13) |

> **Safety / reliability / resilience terminology boundary** (to prevent conflation in bridge-building research): **safety science** (Leveson STAMP; safety = system-level control) **≠ reliability engineering** (Reason / HRO; latent conditions + failure anticipation) **≠ resilience engineering** (Hollnagel Safety-II; **WAI = Work-As-Imagined / WAD = Work-As-Done**; the gap between them is the adaptation space). The philosophy uses "safety science" as the umbrella; details live in this map.

### Practice-corresponding disciplines (this map's layer; not in the philosophy body)

| Discipline | Project practice mapping | Roadmap layer |
|---|---|---|
| Systems engineering | five-stage loop / system-level constraints / three-zone model (docs·harness·skills) / harness engineering | L0 meta layer |
| Cognitive science | the base discipline of human factors (**human factors = applied cognitive science**); the underlayer of AI hallucination / cognitive failure | L0 meta layer |
| Configuration management (CM) | `_vN` versioning / `waste/` retirement / harness-check / SemVer + baselines + change control | L2 |
| Quality management (QMS) | the three desensitization gates / DoD / controlled documents / CAPA | L3 |
| Project management (PM) | VISION / HLD / LLD / retro / TODO / PMBOK initiate-plan-close | L4 |
| Knowledge management (KM) | ADR / CONTEXT / OPEN-DECISIONS / move-only archiving / SECI externalization / lessons learned | L5 |

### v7 governance-evolution mapping

When a discipline enters this project's governance, it must be translated from knowledge names into executable boundaries. The table below is the full-field current mapping; the philosophy body keeps only a reading summary. **Minimal evidence** is the lowest verifiable record this project can bear — not discipline empiricism or proof of downstream effect.

| Discipline knowledge | Governance mechanism | Minimal artifact | Minimal evidence | Trigger |
|---|---|---|---|---|
| **Systems engineering / requirements engineering** | requirements tracing, invariants, V&V, change-impact analysis | method invariants, verification cards, affected-reference lists | each invariant points to a single authority and one minimal verification record | when core claims propagate across files or skills |
| **Epistemology / measurement science** | distinguish claims, proxy indicators, independent evidence, causal conclusions; keep falsifiable boundaries | claim status, indicator definitions, evidence scope | what the indicator actually measures matches the claim boundary | when effect-wording like "effective / fast / quality improved" appears |
| **Configuration management / quality management** | baselines, single authority, non-conformances, corrective & preventive action (CAPA), controlled change | version records, conflict records, recovery actions, retro items | pre/post-change references, states, and recovery paths reconstructable | when canonical files or irreversible governance boundaries change |
| **Cognitive science / HCI** | counter automation bias, default effects, decision fatigue; calibrate human trust in AI | human-review tiering, default-cancel rate, fatigue / rework signals | human confirmation records comparable with later rework / misjudgment signals | when human-machine interface mechanisms change (pre-ticking, delegate, AI self-assessment…) |
| **Knowledge management / organizational learning** | make tacit judgment explicit; let retros enter the next round of norms; distinguish single- and double-loop learning | ADRs, CONTEXT, lessons learned, revisit conditions | recurring problems traceable from retro records to norm revisions or explicit non-fixes | when retros find rules failing or the same problem recurring |
| **Information security / threat modeling** | trust boundaries, least privilege, abuse scenarios, exfiltration and prompt-injection defenses | threat model, forbidden-zone list, desensitization and permission checks | every high-risk capability has forbidden zones, confirmation points, auditable records | when AI touches external systems, secrets, payment, release, or deletion capabilities |
| **Formal methods / assurance cases** | raise independent-verification strength via invariants, counterexamples, property tests, or evidence-argument graphs | counterexample sets, coverage matrices, argument graphs | counterexample coverage or argument chains reviewable independent of AI self-assessment | when AI-code ratio, risk level, or incident signals exceed OD-19 triggers |
| **Cybernetics / decision theory** | observability, feedback loops, reversibility, information value, escalation thresholds | monitoring indicators, escalation gates, shadow-comparison records | multi-round records show the basis of indicator change and escalation decisions | when multiple dogfoods have produced comparable data and upgrade cost is acceptable |

**Minimal entry/exit template for the first three rows (v7)**: entry = the trigger genuinely hit, and a single authority, minimal artifact, and minimal evidence determined; exit = minimal evidence recorded, failure signals and rollback / revisit conditions written, and the first retro found no unacknowledged boundary conflict. If any condition fails, stay "roadmap / unverified" or pause irreversible actions — do not promote to mandatory process. This template is the current governance target, not yet sufficiently validated by dogfood.

> **Introduction order**: a personal project first executes the minimal slice of the systems/requirements engineering, epistemology/measurement science, and configuration/quality management rows; information security, cognitive science/HCI, and knowledge management/organizational learning enter by practice scenario; formal methods and cybernetics/decision theory stay as risk- or data-triggered enhancement layers. This order is the default route, not a mandatory full adoption.

## The AI black box (v7 fourth-discipline thesis anchor · grill-with-docs deep-dive crystallization, 2026-08-10)

> Safety science as the fourth discipline perspective's thesis anchor; v7 inherits and extends the anchoring ([philosophy_v7 §4](methodology/philosophy_v7.md)). Dive source: the grill-with-docs "de-blackboxing" single-point dive (2026-08-10, 6 crystallized points).

- **AI black box** = three mutually independent, stackable dimensions of AI opacity (①②③ = philosophy §4.1's L1/L2/L3; 2026-08-14 grill-Q philosophy-v7 W01 Q5): ① **opaque decision process** (reasoning chain invisible); ② **untraceable decision basis** (why X not Y — no trace); ③ **output correctness not independently verifiable** (functional correctness has an objective oracle but it is usually AI-written — a nested black box; judgment-type outputs can only be human-reviewed, see [philosophy_v7 §4.1](methodology/philosophy_v7.md)). Evidence for any one dimension cannot substitute for the other two.
- **Orthogonal to pillar one**: pillar one governs "AI decides **wrong**" (information dimension; countermeasure = supply information); de-blackboxing governs "the AI's decision **process is invisible**" (audit dimension; countermeasures = traces / traceability). The two are independent — enough information can still leave a black box; full traces can still leave wrong decisions. Hence qualified as an independent fourth-discipline anchor.
- **Black-box risks (three bad outcomes)**: latent accumulation (reliability, Reason's latent conditions) + loss-of-control amplification (safety, STAMP system-level loss of control) + trust hijacking (human factors, black box → abandoned review → blind faith).
- **Countermeasure direction**: consolidate the project's audit instruments into the "against the black box" thesis — the black box is checked, not fully opened (no countermeasure for L1 reasoning chains; traces = the AI's self-reported reasons); instrument status is verified against the four-way "defined in spec / callable by the execution body / actually tested in this repository / adopters must wire", not the stateless "defined / available"; the formal-V&V gap (results independently verifiable) is left to [OD-19](OPEN-DECISIONS.md).
- **Degree (the elastic boundary)**: WAI sets the floor (critical / one-way-door / safety-class mandatory traces), WAD leaves room only in execution details; autonomous decisions already made must still be traced immediately; batch or after-the-fact recording is limited to non-autonomous decisions or pre-declared sampling — preventing de-blackboxing from degrading into documentation ritualism (a meta-principle failure mode).

> **"Process model" terminology conflict**: this table's "information flow = process model" (context → model → result → new information) is retained; STAMP's process model uses the full name "**safety-control process model**" (one of Leveson's three constructs: the controller's internal representation of the controlled system; an inaccurate model → control failure) — different notions, kept distinct.

## The five-stage loop

The development workflow's main path (details in [methodology_v5 §3](methodology/methodology_v5.md)): design-Q → grill-Q → dogfood → long-running → retro-Q; delegate cross-cuts. grill-Q / dogfood / retro / delegate are orthogonal methodologies insertable at any stage, not locked into linear phases.

## The Grill family

The decision engine, in two branches (details in [methodology_v5 §4.3](methodology/methodology_v5.md)):

- **Batch questionnaire family**: design-Q / grill-Q / retro-Q / action-Q (multi-wave questionnaires, answered offline; action-Q = the confirm-list confirm-style fork, its engine-family membership unchanged — added 2026-08-13, grill-Q philosophy-v5 W02 Q3, aligning with philosophy §3.1's membership; from v7 that section is §3.1).
- **Single-point deep-dive family**: grill-with-docs (one question one answer, waiting each round; codebase-bound mode default + general mode carrying the general scenarios — the original grill retired 2026-08-19, its niche carried by general mode, see [OD-12](OPEN-DECISIONS.md)).
- **80/20 judgment-cost principle** (the two branches' tiering criterion; grill-Q's original design principle, author's note 2026-07-31): the batch family handles foreseeable, offline-answerable basic questions; the single-point family handles critical questions with deep dependency chains, unformed decisions, or a need for instant feedback. 80/20 is a routing heuristic, not a time quota or statistical conclusion; the four routing criteria and handoffs are in [methodology_v5 §3.3.1](methodology/methodology_v5.md) / [§4.2](methodology/methodology_v5.md).
- **Three cognitive states** (2026-08-19, grill-with-docs "grill family boundary and mis-routing governance" dive crystallization) = the **cognitive-layer criterion** for routing the two branches, split by "where is the answer material right now", wired to methodology §4.1's (a)(b) blind-spot taxonomy: ① **know · offline-answerable** (the material is in the human's head, just unwritten — type (a)) → batch family; ② **know the direction · decision unformed** (answers must be generated round by round through the dependency chain, needing instant feedback) → single-point family; ③ **don't know what you don't know** (implicit assumptions — type (b)) → forced out by adversarial dimensions (grill-Q D1/D5/D7, or the dive's concrete-scenario boundary testing). **The criterion-layer definition of mis-routing** = the AI misjudges cognitive state when posing questions (treating ②③ as ① and asking in batch, or misunderstanding the artifact's frame so the whole questionnaire grills the wrong target); in-system gates = grill-Q's entry-calibration gate + item-level ❌ mis-routing marker (see grill-Q SKILL/FORMAT rule 15). **Three boundaries** (re-stressed grill-boundary-canonical-w01): this criterion is a **routing criterion, not a truth criterion** — wrong cognition (material present but wrong, "thinks they know but knows wrong") belongs to the verification layer (D7 contradictions with reality / verify-before-asking), not this criterion (Q2); cognitive state is **proposed by the AI, confirmed by the human** — the AI never determines it alone (Q3); the scenario where the human enlists AI precisely because they **lack the task knowledge** (learning / exploration) is out of scope — the material exists on neither side; follow methodology §0's task-level processes (Q3 custom). **Wiring status**: ✅ wired (2026-08-19, re-stress adopted and executed) — philosophy §3.1's "cognitive states" row added; methodology §4.1 wiring sentence / §4.3 priority sentence / §3.3.1 pointer note / §8 item 25 landed.

## The skill family

The methodology's executable carriers, 8 core skills: design-questionnaire / grill-questionnaire / grill-with-docs / retro-questionnaire / long-running-agent / delegate + **action-questionnaire** (the confirm-list questionnaire: a detail-confirmation list before informal write actions, a lightweight prelude, admitted 2026-08-01) + **doctor-harness** (harness evolution governance: layering/migration/validation/traces, cross-cutting like delegate, admitted 2026-08-08). **grill retired 2026-08-19** (to `waste/skills/grill/`; its general × single-point niche is carried by grill-with-docs general mode, see [OD-12](OPEN-DECISIONS.md)). This repository is its single source of truth ([ADR-0001](../../harness/adr/0001-source-of-truth.md)); the single entry routing, inputs / outputs / decision power / hard boundaries / handoff conditions are in [methodology_v5 §3.3.1](methodology/methodology_v5.md).

### Question dimensions quick reference (2026-08-19, retro skill-family W01 supplementary statement)

> Each skill's questioning/confirmation dimensions were scattered across the SKILL.md files, discoverable only by reading them one by one; they are aggregated here at the entry point for family discoverability. Dimension details are authoritative in each skill's skeleton files; this table is a guide only.
> **Sync pointer (2026-08-20, readme-revamp W01 Q2)**: when revising this table's dimension column, the README's "skill question/confirmation dimensions quick reference" table must sync (README is the guide copy; authority = this table).

| skill | Question / confirmation dimensions | Skeleton source |
|---|---|---|
| design-questionnaire | layered skeletons (L0-vision goal layer always + L1+/L2 on demand) + real-environment verification + unverified-assumption ledger | [STAGE-SKELETONS.md](../../skills/design-questionnaire/STAGE-SKELETONS.md) |
| grill-questionnaire | fixed 8 stress dimensions D1–D8 (unstated assumptions / one-way doors / alternatives / failure modes / blind spots / verifiability / contradictions with reality / terminology consistency) | [GRILL-SKELETON.md](../../skills/grill-questionnaire/GRILL-SKELETON.md) |
| action-questionnaire | implicit six-element skeleton (goal / input / output / constraints / boundaries / dependencies) + real-environment verification | each SKILL.md's "提取与核实" section |
| retro-questionnaire | methodology four sections (what went well / what went wrong and hypothesized causes / architectural drift / what was learned) + Action Items | [RETRO-SKELETONS.md](../../skills/retro-questionnaire/RETRO-SKELETONS.md) |
| grill-with-docs | no fixed skeleton (pure follow-up questioning, single-point dive); codebase-bound mode adds domain-vocabulary challenge / code cross-verification; general mode is zero-trace pure dialogue | [SKILL.md](../../skills/grill-with-docs/SKILL.md) |
| long-running / delegate / doctor-harness | non-questioning (constraint system / delegation governance / harness governance) | each SKILL.md |

## The methodology's three documents (ADR-0007)

methodology_v3's single file split into three independent files, each independently revisable (split finalized 2026-08-03/04; details in [ADR-0007](../../harness/adr/0007-methodology-three-way-split.md) and the [HLD](../../harness/design/hld-methodology-separation.md)):

- **The methodology file** = the complete exposition of "how" (processes / methods / disciplines; §0/§1–§5/§7/§8/§9 + appendices C/D); **canonical member**, retaining the "standalone / self-contained" claim.
- **The philosophy file** = the exposition of "why" (failure modes and information gaps / human-machine division of labor / meta-principles; v7 §1–§5); **canonical member** (belonging to "methodology claims").
- **The practice file** = the "how to use" operating guide (skill timing / tool conventions / context operation chains; quick start / §8 / appendices A·B / §7.4–7.6); **non-canonical**, revised via the lightweight process (small commits; exempt from OD-4 master-copy sync and the four-way lock checks).

After the split, "方法论" (methodology) is double-meaninged: the umbrella (the methodology system) vs one of the three documents (the methodology file) — the documents use "the methodology file" for the concrete file; "methodology" defaults to the umbrella.

- **Canonical review** (defined 2026-08-13, grill-Q philosophy-v5 W02 Q8 — previously the word appeared only in the philosophy header and OD-18, undefined) = the mandatory action before revising a canonical member (the methodology file + the philosophy file): grill-Q stress-testing (or line-by-line human review) + user approval; master-copy sync per [OD-4](OPEN-DECISIONS.md). The current canonical philosophy file is v7; dual-file cross-governance per [ADR-0018](../../harness/adr/0018-canonical-dual-challenge-governance.md).
- **Canonical version-bump criteria** (2026-08-18, grill-Q first-principles W02 T5): **structural change is what bumps the version** — renumbering / section add-remove / thesis change / normative-priority change; content syncs, annotation additions, and wording fixes all go through **in-version revision** (a revision-log line in the file header, no bump). Retroactive note: content revisions after v5 / v7 (including 2026-08-18 first-principles W01's ten items, W02's five) are all in-version revisions, not retroactively renumbered; at the next bump, do the compatibility mapping and repository-wide citation review per ADR-0017.

## Harness terminology boundary

> First defined: 2026-08-13, from grill-Q philosophy-v5 W04.

- **Methodology harness** = the process-execution body composed of methodology documents, skill execution bodies, and decision/process traces; this project's `harness/` directory carries its designs, ADRs, and questionnaire products.
- **Runtime harness** = a runnable system coordinating Agent, Context, Model, Capability, Result, persistence, and recovery.
- **This project's scope** = this project provides the methodology harness, not the runtime harness; the shared name does not make them one implementation or one body of evidence.

## Evidence status and scope (2026-08-13, grill-Q philosophy-v5 W04)

> **N=1 single-subject qualifier (2026-08-18, grill-Q first-principles W01 Q9)**: all evidence in this repository is produced by a **single author + AI**; the philosophy's "independent human review" clause is currently unsatisfiable (no second person in the system; dual-file cross-challenging prevents drift, not shared blind spots) — external issues / PRs / adoption feedback serve as the proxy evidence source. Every status word below inherits this qualifier automatically.

> **AI same-source questioning qualifier (2026-08-19, grill-with-docs grill-skills dive A)**: the Grill family's questioner (AI) and the stress-tested artifact (often AI-drafted) are same-source — **the human's adjudication independence is within questions, not beyond them**: question coverage is decided by the AI; a shared blind spot that never becomes a question never reaches the human's adjudication (philosophy §4.1's L3 nested black box, isomorphically replayed at the stress-testing layer). Countermeasure follows the N=1 precedent: external issues / PRs / adoption feedback as the proxy evidence source. Revisit trigger = an external report of "rework caused by a grill-uncovered blind spot".

> **Known-gap note (2026-08-18, grill-Q first-principles W02 T4)**: the acceptance side's (humans reviewing AI output) **load management has no dedicated mechanism** — current countermeasures = 80/20 tiering + L3 risk tiering (both unquantified); review fatigue → rubber-stamping = the known entry point of trust hijacking. Revisit trigger = an instance of "human review passed, production incident" (shared with [OD-19](OPEN-DECISIONS.md) trigger ②).

- **Normative requirement** = a boundary the methodology says should be followed; not equal to having been executed or verified.
- **Heuristic** = an empirical rule or analogy guiding judgment; not a statistical conclusion or discipline empiricism.
- **Pilot** = limited-scope exploration begun, results still to be re-checked against preset conditions; not a stable mechanism.
- **Provisional** = a design or interface written but explicitly marked pending; downstream must not rely on its long-term compatibility; differs from "pilot": a pilot is a process mechanism running, provisional is the artifact's content itself unsettled (introduced 2026-08-14, grill-Q methodology-improvement W01 Q10, following the peer-benchmark repo's provisional-design marker).
- **Verified** = a concrete assertion backed by explicit script, test-run, dogfood, or human-review evidence; must point to an evidence entry.
- **Unverified** = an assertion or device capability proposed but currently without sufficient evidence.
- **Known gap** = a part explicitly acknowledged to lack systematic countermeasures or independent evidence.
- **Audit-instrument status four-way split (v7 W01)** = "defined in spec / callable by the execution body / actually tested in this repository / adopters must wire"; the four answer, respectively, whether it should exist, whether it can be invoked, whether this repository has run it, and what adopting projects must add — none can impersonate another.

These status words apply only to core claims and the audit-instrument list. **This repository's evidence scope** is document/skill execution consistency and process governance — not proof of downstream development efficiency or quality causality; downstream effects must be dogfooded / retro-verified by the adopting projects themselves. Status governance and verification cards per [ADR-0016](../../harness/adr/0016-method-claim-assurance-contract.md).

**Unified claim-status template (v7)**: core claims and audit instruments are organized as "**claim → applicability → current status → minimal evidence → failure signal → revisit condition**". That order is the audit path, not a demand that every paragraph grow a table; the philosophy keeps the principles, and verification cards, test records, and concrete statuses live in the practice file or the `harness/` zone.

**Risk-triggered evidence-first (v7 W02)**: claims involving tool behavior, code behavior, external dependencies, or irreversible actions must carry the original source or reproducible command and output; unverifiable items are marked "unverified". Low-risk reversible actions may continue with status; high-risk or one-way-door actions pause and request human confirmation. Passing tests, a skill having run, or a document existing each cannot alone infer downstream effects or overall correctness.

## Claude Code (its position in this repository)

An attributive, naming the methodology's first practice carrier; not the repository's brand, not "exclusive". The methodology's ideas (dual pillars / five-stage loop / Grill) are tool-agnostic and portable; the skills' direct execution depends on Claude Code's AskUserQuestion / subagent / SKILL.md ([OD-2](OPEN-DECISIONS.md)).

## Desensitization

This repository's content has had the author's project names / paths / personal identifiers removed (release gate per [OD-1](OPEN-DECISIONS.md); check script [scripts/desensitize.py](../../scripts/desensitize.py)). The "项目A / 项目B …" (Project A / Project B …) in archived questionnaires are desensitization placeholders.

## English Glossary (2026-08-23, i18n-support L1 contract)

> The single source of truth for terms used in the English mirror (`en/`) ([ADR-0025](../../harness/adr/0025-english-mirror-drift-governance-integration.md)); new translations = drafted by the agent, confirmed by the human, then entered here — translations follow this table, **self-translating per file is forbidden**. The first batch of high-frequency terms was extracted per file during the first-phase translations and confirmed in review; the Chinese definitions remain authoritative at their "definition anchor" — this table only adds the translated names. Consistent with the philosophy document's precedent of bilingual term juxtaposition (WAI/WAD).

| 术语 (zh, canonical) | EN | Definition anchor |
|---|---|---|
| 镜像(发布镜像) | release mirror | [OD-10](OPEN-DECISIONS.md) — the skill release/distribution-copy sense; **not to be conflated** with "translation mirror" below (disambiguated 2026-08-23) |
| 英文镜像 | translation mirror | [ADR-0025](../../harness/adr/0025-english-mirror-drift-governance-integration.md) — this repository's `en/` translation-mirror tree (i18n-support feature); the Chinese source is the sole canonical, English is one-way derived |
| 翻译义务清单 | TRANSLATABLE | [i18n-check.py](../../scripts/i18n-check.py) — the commitment set for the en-mirror drift check ("entering the list incurs a translation obligation", growing per phase); formerly "翻译白名单". **Not the same as** delegate's "下放白名单" or sync-check's "EXCEPTIONS 例外白名单" — bare "whitelist" wording is deprecated (disambiguated 2026-08-23, grill-Q Q8) |
| 双支柱 | two pillars | this file's "Dual pillars" section |
| 以信息为核心 | Information as the Core | this file's "Dual pillars" section (pillar one) |
| 驾驭工程 = AI × 软件工程 | Engineering Mastery = AI × Software Engineering | this file's "Dual pillars" section (pillar two) |
| 信息流转 | information flow | this file's "Pillar-one terminology layering" section |
| 有效上下文 | effective context | this file's "Pillar-one terminology layering" section |
| 信息真空 | information vacuum | this file's "Pillar-one terminology layering" section |
| 幻觉式自作主张决策 | hallucinated self-directed decisions | this file's "Pillar-one terminology layering" section (background-absence entry) |
| 5 环节闭环 | five-stage loop | this file's "Five-stage loop" section |
| skill 家族 | skill family | this file's "Skill family" section |
| 横切 | cross-cutting | this file's "Five-stage loop" section |
| 对抗压测 | adversarial stress test | this file's "Grill family" section (grill-Q D1–D8) |
| 逃生舱 | escape hatch | each SKILL.md's answering rules (the 🤔 de-risking protocol) |
| 单点深钻 | single-point deep dive | this file's "Grill family" section (single-point deep-dive family) |
| 单向门 | one-way door | each questionnaire's "one-way-door items are never pre-ticked" rule |
| 三区模型 | three-zone model | README's "Repository structure (three-zone model)" section |
| 最小采用切片 | minimal adoption slice | README's "Minimal adoption slice" section |
| 生产车间 | production workshop | README's "Minimal adoption slice" section / CLAUDE.md's repository positioning |
| 复盘 | retrospective | this file's "Five-stage loop" section (retro-Q) |
| 脱敏 | desensitization | this file's "Desensitization" section |
| 信息断层 | information gap | this file's "Pillar-one terminology layering" section |
| 机制层 / 度量层 / 症状层 | mechanism layer / metric layer / symptom layer | this file's "Pillar-one terminology layering" section |
| 判断性决策 | judgment-type decision | this file's "Human-machine division-of-labor terms" section |
| 纯执行类决策 | pure-execution decision | this file's "Human-machine division-of-labor terms" section |
| 认知状态三态 | three cognitive states | this file's "Grill family" section |
| 双向门 | two-way door | the de-risking protocol's gate-type table (methodology §4.4) |
| 降风险协议 | de-risking protocol | methodology §4.4 |
| 层闸门 | layer gate | design-Q's layer-gate protocol |
| 环节 | stage (main-path) | methodology §3 |
| 正交(可插入) | orthogonal (insertable) | methodology §3.3 |
| 治理性偏差 | governance-level deviation | [ADR-0021](../../harness/adr/0021-design-implementation-deviation-governance.md) |
| 契约优先 | contract-first | methodology §5.3 sequencing discipline |
| 时序纪律 | sequencing discipline | methodology §5.3 |
| 未验证假设台账 | unverified-assumption ledger | design-Q STAGE-SKELETONS §1 |
| 证据前置 | evidence-first | methodology §3.3.2 |
| 爆炸半径 | blast radius | grill-Q D4 |
| 失败模式 | failure mode | methodology §8 / philosophy §5 |
| 批量问卷族 | batch questionnaire family | this file's "Grill family" section |
| 单点深钻族 | single-point deep-dive family | this file's "Grill family" section |
| 嵌套黑盒 | nested black box | this file's "AI black box" section (L3) |
| 信任劫持 | trust hijacking | this file's "AI black box" section |
| 潜伏沉积 | latent accumulation | philosophy §4.3 |
| 失控放大 | loss-of-control amplification | philosophy §4.3 |
| 元原则 | meta-principles | philosophy §5 |
| 情境意识 | situation awareness | philosophy §1 (Endsley) |
| 认知负荷 | cognitive load | philosophy §1 (non-convertible with effective context) |
| 潜伏条件 | latent conditions | philosophy §4.3 (Reason) |
| 验证卡 | verification card | [ADR-0016](../../harness/adr/0016-method-claim-assurance-contract.md) |
| 不可裁剪治理核心 | non-negotiable governance core | [ADR-0019](../../harness/adr/0019-methodology-nonnegotiable-guardrails.md) |
| 影子模式 | shadow mode | philosophy §3.2 ([OD-13](OPEN-DECISIONS.md)) |
| 决策分层 | decision tiering | methodology §4.5 |
| 铁律(不可违反) | iron rules (inviolable) | each SKILL.md's "Iron rules" section |
| 工件 | artifact | grill-Q SKILL.md "Terms" section |
| 主流程 | main flow | each SKILL.md's "Main flow" section |
| 处理报告 | processing report | each SKILL.md step 4 |
| 小波阈值 | small-wave threshold | design-Q / grill-Q / action-Q / retro-Q SKILL.md |
| 落盘 | land (write to disk) | high-frequency across all SKILL.md (paired with "sediment immediately") |
| 压测 | stress test | grill-Q SKILL.md (D1–D8) |
| 关键声明清单 | key-claim list | grill-Q SKILL.md step 1 |
| 绿地子模式 | greenfield submode | grill-Q SKILL.md step 0 |
| 代码库绑定模式 | codebase-bound mode | grill-Q / grill-with-docs SKILL.md |
| 纯逻辑模式 | pure-logic mode | grill-Q SKILL.md step 0 |
| 判断权 | judgment rights | delegate SKILL.md iron rule 1 |
| 全权模式 | full-authority mode (`mode: full`) | delegate SKILL.md "Full-authority mode" section / OD-13 |
| 排除集 | exclusion set | delegate SKILL.md "Full-authority mode" section |
| 建议升级(权) | escalation-proposal right | delegate SKILL.md iron rule 2 |
| 只增不改 | append-only, never edited | delegate SKILL.md iron rule 4 |
| 治理历史 | governance history | each SKILL.md's header index line / ADR-0024 |
| 有意分叉 | intentional fork | each SKILL.md's header index line / FORK-NOTES.md |
| 引擎副本 | engine copy | each SKILL.md's supporting-info (OD-8) |
| 旧三件 | legacy trio (VISION/HLD/LLD) | design-Q / long-running SKILL.md |
| 层文件(LN 制) | layer files (LN naming) | design-Q / long-running SKILL.md |
| 五源读取 | five-source reading | retro-Q SKILL.md step 1 |
| 架构偏离 | architectural deviation | retro-Q SKILL.md (one of the four sections) |
| 一次一个功能 | one feature at a time | long-running SKILL.md §6 |
| 单次收尾面板 | single closing panel | design-Q SKILL.md step 5 |
| 收尾停点 | closing stop point | design-Q / long-running SKILL.md |
| 入口校准闸门 | entry-calibration gate | design-Q / grill-Q SKILL.md |
| 环境现实验证 | environment reality verification | design-Q / action-Q SKILL.md |

> Second batch, 31 entries (from the methodology/philosophy/practical/OPEN-DECISIONS/CONTEXT translations): proposed per file batch and **confirmed by human review (2026-08-25)**; landed in the zh table above (single source) and mirrored here. Third batch, 28 entries (from the 8 SKILL.md translations): **confirmed by human review (2026-08-26, spot-check waived)**; cumulative 80 entries.
