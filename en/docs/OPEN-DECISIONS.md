---
lang: en
en-source: docs/OPEN-DECISIONS.md
zh-hash: 0d76542fbb8e
---
[中文](../../docs/OPEN-DECISIONS.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../harness/adr/0025-english-mirror-drift-governance-integration.md)). OD numbers and statuses are stable identifiers; dates and decision records are translated faithfully.

# OPEN-DECISIONS — Pending decisions

> Deferred decisions + revisit triggers. Each entry must state: problem / deferral reason / current placeholder / reversibility / **revisit trigger** (a concrete signal — "later" is forbidden).
> First created: 2026-07-28, output of the pre-repository grill-questionnaire stress test.

---

## OD-1 Desensitization release gate (one-way door · requires line-by-line human review)

- **Problem**: once open-sourced, content forked / cached cannot truly be withdrawn; incomplete desensitization = permanent leakage. How to guarantee "desensitized clean"?
- **Deferral reason**: a script can be written, but "semantic leakage" (identifiable without project names) can only be human-reviewed — it cannot be fully automated up front.
- **Current placeholder**: push only when all three DoD items are green —
  1. the desensitization script ([scripts/desensitize.py](../../scripts/desensitize.py)) reports **0 hits** repository-wide;
  2. **line-by-line human re-review** of the semantic information the script cannot scan (**including git commit messages** — the script scans only .md; commit messages are a blind spot; 2026-08-01 incident: an OD-4 copy-annotation commit's message restated a real project name, intercepted and fixed before push);
  3. a **desensitization report** (what changed).
- **Current status**: mechanical desensitization done (39 hits in skills + 3 in methodology, script at 0 hits); **semantic human review pending** — see the repository-creation desensitization report. (2026-08-13: incremental push of 2 commits (4cc7c4b / f93cc8b) passed all three — script 0 hits + the semantic-review material seen by the user, who directed the push + desensitization report: 0 items needing mechanical desensitization in that batch)
- **Reversibility**: fully reversible before push; a one-way door after push.
- **Revisit trigger**: re-run the script + redo the human review before every release / major update; the sensitive-word list grows as discoveries are made.

---

## OD-2 "The methodology ports to general tools" is an unverified assumption

- **Problem**: the claim "skills were practiced on Claude Code, but the methodology ports". Yet the skills depend heavily on Claude Code mechanisms (AskUserQuestion / subagent / SKILL.md loading) and have never actually been verified on other tools.
- **Deferral reason**: experience gap — never trial-run on Cursor / Cline / other LLM CLIs.
- **Current placeholder**: the README states "the methodology's ideas are tool-agnostic and portable; the skills' direct execution depends on three Claude Code mechanisms — AskUserQuestion, subagent, SKILL.md; porting to other tools requires adapting these".
- **Dependency boundary inventoried**: across the 8 core skills' SKILL.md files, AskUserQuestion appears 18 times, subagent 4 (re-measured 2026-08-03, including action-questionnaire) — those two + SKILL.md frontmatter triggering are the main dependencies. (2026-08-08 note: doctor-harness, the 9th skill's SKILL.md, has no AskUserQuestion / subagent dependency — pure script + document validation; does not affect the counts above)
- **Reversibility**: two-way door (README wording).
- **Revisit trigger**: ① a user reports success / failure adapting to another tool; ② someone attempts a port; ③ a "can't install" issue appears.

---

## OD-3 Maintenance-commitment hedge (one-way door)

- **Problem**: open-sourcing = a public maintenance commitment. The skills still iterate (delegate pilot, just bumped to v2); unanswered issues / PRs → the repository becomes a graveyard.
- **Deferral reason**: maintenance energy cannot be predicted.
- **Current placeholder**: README labeled `experimental / maintained by one person / no guarantee of response` + CONTRIBUTING + issue templates; if energy runs short, fall back to "articles only".
- **Reversibility**: publishing is a one-way door; the commitment wording is a two-way door.
- **Revisit trigger**: issue backlog exceeds capacity; raise the commitment when the methodology stabilizes out of pilot; consider archival labeling after > 3 consecutive months without updates.

---

## OD-4 Master-copy sync of the methodology articles

- **Problem**: before this repository, the methodology articles had copies in several of the author's locations; this repository introduces the master. Leaving the source undecided invites drift.
- **Deferral reason**: historical copies are scattered.
- **Current placeholder**: **this repository's methodology_v5 + philosophy_v7 are canonical** (2026-08-14, methodology v4→v5 upgrade completed — continuous sections + contract-first adjudication + action-Q joining the family (grill-Q methodology-improvement W01); philosophy v7 the current canonical, with continuous sections, historical-number compatibility, and dual-file cross-governance — copies elsewhere are annotated per the corresponding canonical version). **The practice file is non-canonical**, revised via the lightweight process (small commits, exempt from master-copy sync).
- **Historical ruling (2026-08-03, ADR-0007)**: methodology_v3 three-way split — canonical membership extended to **the methodology file + the philosophy file** (under docs/methodology/, where the methodology claims live); the practice file non-canonical; the pre-split historical master-copy narrative is retained but is not current guidance.
- **Reversibility**: the master-copy convention is a two-way door; once published, a one-way door.
- **Revisit trigger**: any canonical member bumps version / master-copy content changes / canonical membership or sync strategy is adjusted again, or an explicit "maintain only this repository's version".

---

## OD-5 (completed) ADR / OD landing

- This batch of ADR-0001 / 0002 / 0003 + this OD file landed in this repository with its creation (2026-07-28). The original "migration" pending item is closed.

---

## OD-6 Differentiation claim awaits market validation

- **Problem**: the differentiation = "methodology + ready-to-run skill executables" in one — a claim, not yet verified.
- **Deferral reason**: needs post-release feedback.
- **Current placeholder**: stated up front in the README.
- **Reversibility**: two-way door.
- **Revisit trigger**: after release, watch stars / issues / clones; if cold, re-examine positioning.

---

## OD-7 Exposure surface of the early non-desensitized copy (already occurred)

- **Problem**: skills / archived questionnaires that once appeared in another public project of the author's contained project names — public and irreversible.
- **Deferral reason**: the other project has its own review process.
- **Current placeholder**: that copy stays untouched; this repository's README notes "the author has an earlier, non-desensitized copy".
- **Reversibility**: already-public is a one-way door; whether to go back and clean is a two-way door.
- **Revisit trigger**: a decision to clean the other project too; or privacy concerns arise.

---

## OD-8 Open-source presentation of the skill engine copies (decided)

- **Problem**: QUESTIONNAIRE-FORMAT / PROCESSING-RULES are held one copy each by the three questionnaire skills (design-Q / grill-Q / retro-Q), each self-labeled "design-Q engine reuse"; diff confirmed the design-Q and grill-Q engine files **have drifted** — a living specimen of methodology item 17, "engine drift".
- **Decision**: keep the copies as-is + declare the drift relationships in DESIGN.md. No unifying, no extracting a shared file.
- **Rationale**: faithfully present the status quo; unifying / extracting would change the skills' internal organization — cost off the value main line. Copyright is the author's original work; MIT-izing is unobstructed.
- **Reversibility**: two-way door — no ADR (insufficient irreversibility).
- **Revisit trigger**: the drift causes confusion / issues; or after a design-Q engine upgrade, evaluate syncing the other copies.
- **2026-08-03 revisit trigger ① hit**: design-Q engine upgrade (pre-tick switch + unified option ordering, OD-14 revision); evaluated per the revisit condition and **synced all four copies** (QUESTIONNAIRE-FORMAT / PROCESSING-RULES unified across design-Q / grill-Q / retro-Q / action-Q; SKILL.md needed syncing only in design-Q); drift records updated to each DESIGN.md's "engine sync record (2026-08-03)" section.
- **2026-08-19 scope extension (grill-Q skill-family W01 Q2-C)**: the "questioning methodology" of grill and grill-with-docs (how to ask / escape hatch / de-risking protocol, ~60 lines) is a **5th implicit copy** beyond the four questionnaire engines (one copy each in the two skills, nearly verbatim isomorphic) — brought under this entry's drift governance: when revising either skill's questioning methodology, cross-check the other; drift declarations go in each DESIGN.md. The same stress round rejected the "grill absorbed into grill-with-docs as a mode" merge proposal; OD-12 stands.
- **2026-08-20 carrier-migration note ([ADR-0024](../../harness/adr/0024-governance-history-split-dual-form.md), execution pending P1)**: each skill's drift/fork declaration moves out of DESIGN.md into an independent **FORK-NOTES.md (byte-identical both sides)**; global-side visibility improves from "invisible (DESIGN.md doesn't ship to the global side)" to "visible"; the historical part of the drift records migrates to each skill's CHANGELOG.md (project side only).

---

## OD-9 (decided) Repository name

- **Decision**: the repository name = `info-driven-ai-se-harness-engineering`, expressing the dual pillars (information-driven × AI + software engineering = Engineering Mastery).
- **Reversibility**: two-way door (GitHub rename redirects).
- **Revisit trigger**: if branding changes.

---

## OD-10 Skill family "distribution-clean" vs keeping during dogfood

- **Problem**: under skills/, each skill's SKILL.md / DESIGN.md carry dogfood records, historical process statements, and other non-essential information; an ideal distribution copy would be clean (noise removed for distribution), but we are in the dogfood stage and need to keep them.
- **Deferral reason**: dogfood unfinished — cleaning time not ripe; and the v3 thesis rebuild explicitly left skills untouched (W00 #6 adopted).
- **Current placeholder**: during dogfood, keep all historical / dogfood statements (the skills are living, iterating bodies).
- **Target state**: when a skill is ready for formal distribution, clean the non-essential statements (historical info, dogfood process records), keeping only the distribution-essential spec.
- **Reversibility**: two-way door (cleaning is revertible via Git history).
- **Revisit trigger**: ① some skill's dogfood closes; ② a skill is ready for formal distribution / packaging; ③ done together with the pre-distribution desensitization check (OD-1).
- **2026-08-20 design ruling ([ADR-0024](../../harness/adr/0024-governance-history-split-dual-form.md), execution pending P0–P4)**: dual-side steady-state division of form — the global side (`~/.claude/skills/`) becomes the **distribution-clean form** (out-of-the-box: SKILL.md + engine/templates + FORK-NOTES; no DESIGN.md / no CHANGELOG); the distribution-clean target state is **reached early** on the global side; the project side keeps the full evolution history. Revisit trigger ①'s "dogfood closes" is re-worded to "after migration P4 (global-side reorganization) completes, evaluate together".

---

## OD-11 (decided) Fork governance of the 4th questionnaire-engine copy

- **Problem**: the new "detail confirmation before actions" skill (naming pending, leaning `action-questionnaire`) reuses the design-Q engine = a 4th copy; it carries two **intentional** forks (small-wave threshold ≤2→4; preview renamed/re-purposed as the "detail-confirmation list / confirm-list"). Does this trigger an OD-8 re-debate?
- **Decision** (2026-07-30, grill-Q W01 Q6=A): **no re-debate**. The 4th copy copies the design-Q **canonical** engine (including the W00 preview section — the grill-Q / retro-Q copies lack it, diff-verified); the copy header self-labels "design-Q engine reuse"; the new skill's DESIGN.md declares the intentional-fork list.
- **Rationale**: fits OD-8's governance frame (keep as-is + declare drift); intentional forks with stated provenance are more controllable than the accidental drift of the existing three.
- **Reversibility**: two-way door (the copy can change before distribution; the fork parameters are just numbers/wording).
- **Revisit trigger**: ① a design-Q engine upgrade evaluates **four** copies (not three) together; ② the forks confuse users / generate issues.

---

## OD-12 (decided) Disposition of grill (general, zero-trace)

- **Problem**: after the "merge the single-point deep-dive family" frame was dropped (grill-merge-grill-family-w01, user ruling 2026-07-31), grill's keep / retire / archive was suspended.
- **Decision** (2026-08-19, grill-with-docs grill-skills dive E, after revisit trigger ① hit, re-estimated and executed via this stress round): **keep**. Reasons: ① in the 2×2 niche matrix (general/bound × single-point/batch), grill uniquely occupies the "general × single-point" cell (dives not bound to a codebase, with deep chains, needing instant feedback — e.g. non-project plans / pure logical reasoning) — the other three cells are covered by grill-Q pure-logic mode / grill-Q default mode / grill-with-docs; retiring = an empty cell; ② near-zero maintenance cost (shares the questioning methodology with grill-with-docs); ③ zero-trace is a design feature ruled by the user on 2026-07-24, not a defect.
- **Structural note**: the original trigger ② "3 consecutive months of zero use" is **unverifiable** at the system level — grill is zero-trace = no usage records; the trigger can never be falsified from inside the system; usage monitoring downgrades to **author self-reflection**; the system sets no unverifiable fake triggers (ritualism devices).
- **Reversibility**: two-way door (files recoverable; trigger-word habit impact = the author alone).
- **Revisit triggers** (narrowed): ① another instance of grill / grill-Q trigger-word confusion; ② the author proactively re-estimates (after self-reflecting on usage).
- **2026-08-19 revisit trigger ② hit → flipped to "retirement preparation / observation period"**: the author that day proactively re-estimated "I can't see the point of grill's existence" (retro skill-family W01 Q6 ticked "grill trigger words confuse easily, can retire" + follow-up made explicit), overturning the ruling's niche reason ① — the "general × single-point" cell is now carried by **grill-with-docs' new "general mode"** (unbound + zero-trace, behaviorally equivalent; landed 2026-08-19). **Disposition = observation period, not immediate deletion**: grill gets a "observation period / pending retirement" banner directing triggers elsewhere; once with-docs general mode is validated by real use to carry the load, grill retires (moved to `waste/`, honoring zero information loss). Relation to the same day's W01 Q2-C (which rejected "with-docs adds a general mode" for simplification): that rejection was to simplify the family while grill's niche still seemed valuable; this addition is the carrying precondition for retiring grill — different purposes, no contradiction; in essence the "cell value" is downgraded from "a standalone skill" to "a mode of with-docs".
- **Observation-period revisit triggers** (2026-08-19): ① with-docs general mode validated by ≥ 1 real general-purpose use as able to carry (human confirms equivalent experience) → grill retires; ② general mode proves insufficient (misses general scenarios / worse than standalone grill) → roll back, grill restored to formal status; ③ observation period exceeds 60 days with no general-purpose use instance → adjudicate "low-frequency but valuable vs mechanism ineffective" (grill is zero-trace = no records; author self-reflection applies; no unverifiable fake triggers).
- **Reversibility**: two-way door (grill undeleted during observation; general mode is an added switch; rollback = remove banner + delete the mode section).
- **First real use in the observation period (2026-08-19, general-mode spec dive)**: the user used grill-with-docs general mode to dive into "general-mode applicable scenarios + missing-information fallback" — itself a meta-question of general mode's carrying capacity (unbound, single-point, instant feedback). Three spec precisions fed back: ① operable discrimination (three applicable scenarios + counter-boundaries); ② both misjudgment fallbacks (entry confirmation + mid-course switch back); ③ zero-trace boundary (AI proposes + human decides, replacing the original grill's passive "write only on explicit request"). This use proves general mode can carry "methodology meta-question" scenarios; but the sample = 1 and a meta-question — **whether it covers all of grill's original general scenarios (cross-project decisions / pure logical reasoning) awaits more instances** — observation trigger ①'s "≥ 1 real validation" partially hit; not alone sufficient to retire grill.
- **✅ Observation period terminated → formal retirement (same day 2026-08-19, explicit user ruling)**: the user ruled "remove grill — this skill was derived from mattpocock's grill-with-docs (https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs), with few applicable scenarios". **Execution**: grill archived to `waste/skills/grill/` (both sides; zero information loss; recoverable) + logged in waste.log; the niche (general × single-point) formally carried by grill-with-docs general mode; all living documents synced (CLAUDE.md / README / CONTEXT / methodology §3.3.1 · §4.3 / philosophy §3.1 · §5 in-version revisions); historical narratives and archives unchanged; the family shrinks from 9 to 8. **Same-origin supporting evidence**: diff confirms grill and grill-with-docs questioning methodologies are highly isomorphic (wording-level differences, structural identity) — the derivation holds. Note: retirement did not go through the full "observation ≥ 1 cross-project / pure-logic validation" trigger — the user ruled directly on "derived same-origin + few scenarios", an early termination via the author's proactive re-estimation right (extension of trigger ②), recorded for reference; if general mode later proves insufficient, restore from `waste/skills/grill/`.

---

## OD-13 (decided) AI dual-track comparison pilot (shadow + champion-challenger)

- **Problem**: "90% of AI suggestions are right, but only 10% are important decisions — human productivity not fully freed; granting AI all decision power risks the solution space missing the right answer" — should a "full AI autonomy" skill be added, running dual branches at suitable decision nodes (full AI vs human-led) and comparing in retro? Maps to the systems-engineering/OR models: shadow mode + champion-challenger.
- **Decision** (2026-08-01, grill-Q ai-autonomy W01 stress; **W02 corrected**): **approve the pilot, but keep it out of the skill family for now** (the family stays at 7; the CLAUDE.md "7 core skills" wording unchanged — 2026-08-03 revision: the family has since updated to 8 with action-Q's admission, canonical synced — "unchanged" means not changed for shadow; this "shadow does not join the family" ruling stands), dogfood first. Key points:
  - Execution form: **shadow first, then real** (W02 Q1); **shadow = automated dogfood, run routinely, no N cap** (W02 Q1 custom — shadow runs on every task, accumulating comparison data); real execution upgrades on demand, judged by shadow data; subagent judgment applies only to shadow / champion-challenger dual-track mode; normal mode keeps human decision power
  - Permission floor: keep delegate's forbidden zones + **release / payment / external publication / data deletion — four classes never auto-executed**; **delegate multi-mode decided** (W02 Q3): delegation.md adds a `mode: full` switch; when on, whitelist semantics invert to "anything not listed as forbidden is executable by default"; floor and traceability (delegation-log) unchanged
  - **delegate new-discipline clause candidate** (W02 Q4 adopted): "the AI may autonomously probe (read-only) first; post-probe decision classification still goes to the human, or into the full-power mode's exclusion set" — resolving the tension between "AI probes first then classifies" and "AI has no self-classification right"; clause landing awaits revision authorization
  - Acceptance: DoD / end-to-end tests set in advance (reusing long-running's passes mechanism) + **N ≥ 3 trial runs (real-execution phase)** + human arbitration of differences; "it went wrong" is never adjudicated by AI self-assessment
  - Process information: reduced to "decision-point-level traces" (like delegation-log, append-only); logs land in the host project's `.claude/` or `~/scratch/`, **never in the public repository**; desensitization hides absolute paths
  - Pilot site: `~/code/DOGFOOD/`
- **First-round dogfood data (2026-08-03 user feedback, carrier = DOGFOOD sandbox shapez-game-test)**:
  - Ran through: delegation.md `mode: full` + 23 autonomous-decision traces + shadow audit zone + dogfood report v1 + difference report v1;
  - Key evidence: **"AI self-assessed playable (27 tests green + Playwright clear) ≠ actually playable by a human"** — difference report #7's "level-solvability tests constructed by the level author itself (self-certification)" risk was evidenced; user experience = "unsatisfying, unplayable";
  - Cause judgment (capability-difference items): the AI branch lacked information and visual capability, could not monitor in real time;
  - **Value repositioning**: "rapid design templates and demo generation" as the main output value (expected output downgraded from "a playable game" to "template / demo-grade artifacts + fast trial-and-error");
  - **Upgrade arbitration (2026-08-03 user ruling): upgrading to real execution is conditional** — only after a human actually plays through; never unconditionally granted;
  - Desensitization: in this repository's records, absolute paths hidden as `~`; relative-path references allowed (the DOGFOOD sandbox subproject name may be written).
- **Reversibility**: two-way door (not in the family; pilot revocable; naming undecided (Q14 chose C))
- **Revisit triggers**: ① shadow auto-dogfood data keeps accumulating — round 1 out (2026-08-03), value repositioned; next node = the real-execution decision after human play-through acceptance, or 30 days without new value; ② decide family-ization (adding as a family member; currently 8) or abandonment; ③ after delegate `mode: full`'s first real execution, review per delegation-log summary.

---

## OD-14 (decided) design-Q questionnaire default-tick pilot (pre-authorization mechanism)

- **Problem**: does default-ticking the recommended option violate the iron rule "AI never decides for the human"? A direction for solving "low decision efficiency".
- **Decision** (2026-08-01, grill-Q ai-autonomy W01 stress): characterized as a **pre-authorization mechanism** (same semantics as delegate's whitelist — a recommendation remains a recommendation; the human keeps veto), with four guardrails:
  1. **One-way-door items (release / delete / spend / desensitize) are never default-ticked — mandatory answers**;
  2. **Option ordering counteracts the default effect**: non-recommended first → escape hatch second-to-last → recommended last (exploiting linear reading; the user's custom scheme);
  3. **Guardrail metrics**: processing reports must carry the "user default-cancel rate" + an explicit confirmation point before writing to disk + a warning and default rollback after N consecutive waves with zero cancels (N = 3 provisional; a two-way-door parameter);
  4. **Only design-Q canonical pilots**; syncing the four copies (grill-Q / retro-Q / action-Q) is evaluated at OD-8's revisit (stress-type questionnaires' default ticking weakens adversarials — different, unchanged);
  5. **Question-level ordering** (W02 Q2, user ruling, rejecting "put last"): questions "lacking information / untestable" go **first** in the questionnaire — exposing information gaps earliest, handled with the user's best attention. "Untestable" criteria (user-defined): ① agent-capability probing (tools / scripts / bash) yields no results; ② probing yields no valid conclusion.
- **2026-08-03 revision (pre-tick switch-ized; user ruling; action-Q confirm-list confirm-pregou-switch-w00 fully confirmed)**:
  1. **Pre-tick = opt-in switch, default off** — only when the user explicitly says "pre-tick" at skill start are recommended options pre-ticked; otherwise all `[ ]`; guardrail ① retained (one-way-door items still not pre-ticked when on);
  2. Option ordering (guardrail ②) = **default behavior, independent of the switch**;
  3. Guardrails (③) = **apply when the switch is on** ("pre-tick guard" section: cancel rate / pre-write confirmation point / 3-wave zero-cancel warning);
  4. Guardrail ④ revised: **four copies synced** — QUESTIONNAIRE-FORMAT / PROCESSING-RULES unified across design-Q / grill-Q / retro-Q / action-Q (OD-8 revisit trigger ① hit; declared in each DESIGN.md; SKILL.md contains pre-tick description only in design-Q, synced);
  5. Question-level ordering (⑤) kept only in design-Q, not synced across the four (user confirmed);
  6. The first round's "taken-for-granted" risk (recorded 2026-08-03) is tightened by this switch-ization (more thorough than the proposed "no pre-tick on high-risk items").
- **First-round dogfood data (2026-08-03 user feedback, carrier = DOGFOOD sandbox shapez-game-human-decision's hld / lld W00)**:
  - **Reduced judgment burden ✓** (user confirmed);
  - **"Taken-for-granted" risk signal appeared**: follow-up questions and fixes suspected related to pre-ticked-all-adopted without reading the recommendation reasons — the textbook guardrail scenario = "default-cancel rate = 0 + later rework", docking directly with the guardrail metrics (cancel-rate indicator / 3-wave zero-cancel warning);
  - The user provided no concrete instance (confirm-list item 8 ticked = not digging further); the risk recorded as a signal;
  - The vision W00 predates the pre-tick change (2026-08-01) — not pilot data.
- **Reversibility**: two-way door (pilot revertible; ordering/parameters are editable numbers and wording).
- **Revisit triggers**: ① pilot comparison data lands (processing time / default-cancel rate / write-then-rework rate / subjective fatigue) — round 1 out (2026-08-03), decide keep or revert; if the "taken-for-granted" signal recurs (cancel rate = 0 with rework) → tighten (add "no pre-tick on high-risk items" beyond the one-way-door exemption); ② evaluate four-copy sync at OD-8's revisit.

---

## OD-15 (completed) doctor-for-harness skill — harness evolution governance

- **Problem**: the harness file-management spec (ADR-0011 hardcoding + each SKILL.md's write paths) was a **static flat** design (design/ + questionnaires/ + adr/; filename prefixes), not covering:
  - **Hierarchization**: design/ had no feature-aggregation directories (the status quo mixed repo/, skill-spec-revamp/ subdirectories with bare VISION.md / hld_v2.md; the spec undefined when to create directories);
  - **Sub-project boundaries**: no criterion for harness ownership in multi-subproject repositories;
  - **Evolution governance**: directory structure / naming / archive organization evolve with project lifecycle; no dedicated mechanism for "migration + normalization + validation".
  - Stress source: [grill-harness-file-mgmt-w01](../../harness/questionnaires/archive/harness-file-mgmt/grill-harness-file-mgmt-w01.md) (2026-08-08, 14 items accepted/delegated).
- **Landed (2026-08-08)**: doctor-for-harness design (design-Q suite + ADR-0012/0013) + implementation (F017–F020, commits c6293fc/5a0221a/7fe5bc0) + admitted as the 9th family member; HARNESS-RULES made authoritative + the harness-check.py validation script + archive sub-directoryization (41 files). The original "deferral reason" and "expected responsibilities" are both fulfilled.
- **Reversibility**: two-way door (changeable before the skill ships).
- **Revisit triggers**: ① when harness migrates again, validation rules go first; ② evaluate together with OD-10 (skill distribution-clean); ③ see OD-17 (usage verification).

---

## OD-16 Harness tiering optional tracks (questionnaires/adr) revisit trigger

- **Problem**: ADR-0013's optional tracks (questionnaires/ new archives into subdirectories + adr/ tiering) marked TBD with no revisit trigger — to what degree of flat-archive bloat (questionnaires/archive already 30+ files) do we act? Without a quantified signal, it's permanent suspension or random deciding.
- **Source**: [grill-doctor-harness-w01](../../harness/questionnaires/archive/doctor-harness/grill-doctor-harness-w01.md) Q5 (2026-08-08, all accepted).
- **Current placeholder** (updated 2026-08-08): **the questionnaires optional track is executed** — archive sub-directoryization landed: 41 legacy files migrated into 10 subdirectories by feature/topic + the [archive/README.md](../../harness/questionnaires/archive/README.md) index (commit c825e75; HARNESS-RULES §4 "legacy stays" → "wholesale migration allowed"). **adr/ tiering still TBD** (currently 13 files; not yet needed).
- **Reversibility**: two-way door (archive organization can evolve).
- **Revisit triggers**: ① files under `harness/questionnaires/archive/` > 50; ② some feature's archived questionnaires > 10; ③ actual retrieval difficulty in the archive (user feedback); ④ adr/ files > 15. Any one → re-evaluate deeper tiering (e.g. adr/ tiers).

---

## OD-17 doctor-harness's "evolution is the norm" assumption — usage verification

- **Problem**: VISION Q1's motivation "evolution is the norm → establish a governance skill". But this repository (the methodology repo) evolves its harness at low frequency (4 feature-level designs: repo / v4 / skill-spec-revamp / doctor-harness, across weeks). If cross-project use is also absent, doctor-harness may degenerate into "a one-off migration tool + static docs" — in tension with its "standing governance-skill" positioning.
- **Source**: [grill-doctor-harness-w01](../../harness/questionnaires/archive/doctor-harness/grill-doctor-harness-w01.md) Q9 (2026-08-08, the doubtful assumption acknowledged).
- **Current placeholder**: doctor-harness is in the family (9th, F020), positioned as a governance skill; minimal-usable constraint (only four duties: rules / migration / validation / traces).
- **Reversibility**: two-way door (can revert to "migration tool + static docs" positioning).
- **Revisit triggers**: ① doctor-harness unused for 3 consecutive months (cf. the OD-12 grill "usage marginalization" precedent); ② used only by this repository, no cross-project feedback; ③ harness organization long stable, no evolution. Any one → re-evaluate positioning (downgrade to tool or archive).

---

## OD-18 Discipline-anchoring completeness review trigger (two-way door)

- **Problem**: the philosophy canonical's discipline anchoring is a thesis claim, but "is it complete?" had no proactive review mechanism — this round ([grill-discipline-mapping-w01](../../harness/questionnaires/archive/methodology/grill-discipline-mapping-w01.md), 2026-08-10) only found the omissions (safety science + a whole swath: CM/QMS/PM/KM/systems engineering/cognitive science) because the user asked. No completeness review = long-lived anonymous omissions.
- **Deferral reason**: anchoring completeness must be checked against practice evolution (e.g. discipline mappings newly found in bridge-building research); cannot be fixed once.
- **Current placeholder**: tiering strategy + mechanism criteria set ([ADR-0014](../../harness/adr/0014-discipline-mapping-strategy.md)) — the philosophy anchors thesis-core disciplines; CONTEXT's "project discipline map" section carries the panorama; safety science entered the philosophy in v5; v7 inherits v6's governance-evolution roadmap and adds the first-three-disciplines minimal entry/exit template.
- **Reversibility**: two-way door (adding/removing disciplines goes through canonical review + OD-4 master-copy sync).
- **Revisit triggers**: ① ~~re-check anchoring completeness at every methodology version bump (v5+)~~ **de-ritualized (2026-08-18, grill-Q first-principles W01 Q4: discipline anchoring is expository decoration, not load-bearing for the thesis logic; bump-time review no longer mandatory)** → "review when the user initiates"; ② review when a newly introduced practice (e.g. bridge-building-research-style deep research) reveals a strong discipline mapping; ③ review for ritualism when the philosophy body's discipline count > 6 (ADR-0014 soft boundary); ④ when the philosophy's discipline count changes. Any one → review anchoring completeness.

---

## OD-19 The formal-V&V gap — the black box's "results independently verifiable" countermeasure is missing (two-way door)

- **Problem**: among the de-blackboxing layers ([CONTEXT AI black box](CONTEXT.md)), "results independently verifiable" (confirming output correct independent of AI self-assessment) lacks a systematic countermeasure — the project relies on human review + dogfood (manual V&V), lacking formal methods (coverage matrices / measurable assurance / model checking). [OD-13](OPEN-DECISIONS.md) already evidenced "AI self-assessed playable ≠ human-usable".
- **Deferral reason**: formal V&V may overload an individual-developer methodology (bridge-building research #3 also noted formal methods as too heavy for individuals); timing depends on the AI-code ratio and risk profile.
- **Current placeholder**: consolidate the existing auditable instruments (delegation-log / ADRs / code-review humans / dogfood) into the de-blackboxing thesis; "results independently verifiable" leans on human review + dogfood as backstop; the gap explicitly acknowledged (non-formal, non-systematic coverage).
- **W02 interim direction (2026-08-14)**: adopt risk-tiered minimum assurance — ordinary reversible code uses objective tests with scope stated; AI-written oracles must be human-reviewed; user-playable artifacts and one-way-door operations require human play-through / confirmation; escalate to coverage matrices, formal methods, or stronger independent verification on high risk or counterexample signals. This direction feeds verification cards and dogfood first; OD-19 is not considered resolved.
- **Reversibility**: two-way door (adding formal V&V is additive; can be introduced gradually).
- **Revisit triggers**: ① the AI-generated-code share of project code rises markedly (e.g. > 50%); ② an instance of "human review passed but production incident" (manual-V&V failure signal); ③ formal toolchains become friendly to individual developers (low-cost, usable). Any one → evaluate adding formal V&V (coverage matrices / assurance metrics / model checking).

## OD-20 Core-document tiering depth — full Level 1/2/3 or the minimal governance slice (two-way door)

- **Problem**: in grill-Q philosophy-v5 W04, Q1 chose "copy Level 1/2/3 wholesale"; Q10 chose "the minimal slice of A+B+D, not copying the full Level 1/2/3". The two represent structural rebuild vs cost-controlled minimal governance — they cannot be silently merged into one conclusion.
- **Source**: [grill-philosophy-v5-w04](../../harness/questionnaires/archive/philosophy-v5/grill-philosophy-v5-w04.md) Q1/Q10 (2026-08-13).
- **Current placeholder**: do not move or rename the existing three files; first establish the core claims' minimal verification/change contract per [ADR-0016](../../harness/adr/0016-method-claim-assurance-contract.md); whether full Level 1/2/3 holds awaits a separate ruling.
- **Audit evidence (2026-08-14, grill-Q methodology-improvement W01 Q4-B)**: the three-file content audit is complete ([methodology-audit_v1](../../harness/design/methodology-audit_v1.md)) — semantic conflicts are rare (1, fixed); the bulk is "duplicated but consistently worded"; but **sync drift is evidenced** (15+ link texts unsynced after the v5/v7 renumbering); the pain point characterized as "one fact written in many places → sync drift". Revisit trigger ① ("living-document conflicts") not hit literally; whether the dual-write cost evidence suffices to upgrade to tiered restructuring is left to design-Q (same source as feature-designq-digital-levels' inter-layer adjudication). If the minimal slice is kept: B3 (§6 verbatim dual-written with the global CLAUDE.md) / C5 (deviation governance in five places) / C7 (evidence-first in four places) converge first. **Audit-method increment (2026-08-18, grill-Q first-principles W01 Q7)**: the next audit's DoD adds a **reverse-reference scan** — check back-references from CONTEXT / CLAUDE.md / README to canonical section numbers (audit_v1 and the bump script were forward audits only; found misses: CONTEXT's stale "§四" numbering, CLAUDE.md's collaboration diagram missing the dogfood node, and one more).
- **Reversibility**: two-way door. The minimal slice first does not prevent adding norm/evidence layers later; a wholesale rebuild carries high migration and sync costs.
- **Revisit triggers**: ① after the three-file audit, the same core rule still conflicts in two or more living documents; ② after the first 6–10 method invariants / verification cards trial-run, readers still cannot tell the single authority; ③ the number of files needing sync for new core-claim changes keeps exceeding the maintainable range. Any one → re-compare full tiering vs the minimal slice.

## OD-21 (decided · two-way door) Dual-file governance focus of philosophy / methodology — does the practice file exit structural evolution

- **Problem**: W01's supplementary statement noted the three files' structure is bloated and proposed "narrow to philosophy and methodology, letting the two evolve separately yet challenge each other". That wording could mean narrowing the canonical governance focus, or physical merging / removing the practice file — migration costs and boundaries completely different; cannot be silently merged.
- **Source**: [grill-philosophy-v6-w01](../../harness/questionnaires/archive/philosophy-v6/grill-philosophy-v6-w01.md) supplementary statement (2026-08-14).
- **Deferral reason**: whether "narrowing" changes governance scope or file structure was undefined; nor how the two canonical files challenge each other, who carries the practice content, how versioning and release gates change.
- **User ruling (2026-08-14, W02 Q10)**: adopt "philosophy + methodology" as canonical peer dual files; each evolves its own version independently; every canonical revision of either requires cross-review or a grill-Q consistency check by the other. `practical_v1.md` stays as the non-canonical guide — not deleted or physically merged by this ruling.
- **Current placeholder**: execute the dual-file governance focus per [ADR-0018](../../harness/adr/0018-canonical-dual-challenge-governance.md); the minimal cross-review fields are in ADR-0018 and the [governance minimal slice](../../harness/design/methodology-governance/LLD.md); first-round real-case evidence and trigger-gate calibration await dogfood / retro.
- **Reversibility**: two-way door. Narrowing only the canonical review scope is revertible; physical merging / removing the practice file changes references, maintenance boundaries, and historical interpretation — higher migration cost.
- **Revisit triggers**: ① after W02 fixes the dual-file governance contract; ② the three-file audit finds practice/methodology responsibility duplication; ③ the practice file's lightweight non-canonical revisions keep back-polluting the two canonical files; ④ the user explicitly demands physical merging, removal, or re-tiering.

## OD-22 Skill niche and naming routing table (two-way door)

- **Problem**: the nine skills' responsibilities are locally divided, but `grill`, `grill-with-docs`, `grill-questionnaire`, and the two questionnaire entry types can still be mis-triggered by name alone; there is no single authoritative routing table of inputs, outputs, decision power, hard boundaries, and handoff conditions.
- **Source**: [grill-philosophy-v7-w02](../../harness/questionnaires/archive/philosophy-v7/grill-philosophy-v7-w02.md) Q1/Q3. Q3 took the escape hatch; the recommendation was adopted provisionally per the de-risking protocol.
- **Deferral reason**: no repeated mis-triggers or real handoff-failure samples yet; immediate renaming would break historical trigger words, references, and usage habits — migration cost above the evidence-supported benefit.
- **Current placeholder**: keep the current names; the single authoritative routing table and the nine skills' minimal niche cards are in [methodology_v5 §3.3.1](methodology/methodology_v5.md), covering inputs, outputs, decision power, hard boundaries, and handoff conditions. Real-case validation and repeated mis-trigger evidence still accumulate; no renaming before then.
- **Reversibility**: two-way door. The routing table is a reversible compensating layer; renaming stays in reserve.
- **Revisit triggers**: two independent mis-triggers within three months; one mis-trigger causing wrong artifacts or irreversible actions; the routing table showing an unresolved dual authority for the same responsibility; or a real dogfood proving the niche cards cannot produce traceable handoffs.

## OD-23 delegate pilot and controllability verification (two-way door)

- **Problem**: this repository has no project-level `delegation.md` / `delegation-log.md` instance; low usage cannot distinguish "low-frequency but valuable" from "mechanism ineffective"; the post-enable revocation and log loop are also untested.
- **Source**: [grill-philosophy-v7-w02](../../harness/questionnaires/archive/philosophy-v7/grill-philosophy-v7-w02.md) Q5/Q6.
- **Deferral reason**: lacking real usage, human-correction, revocation, and log-completeness evidence; forced enabling would create ritualistic usage and widen the permission surface.
- **Current placeholder**: delegate defaults off, explicitly enabled; pilot with 1–2 low-risk, reversible, countable execution-decision classes. Record per-class usage, revocations, human corrections, and log completeness; keep per-class revocation conditions, the global kill switch, and the append-only per-case log; complete one failure-injection / revocation drill. No scope or default-path expansion before the pilot and retro complete.
- **Reversibility**: two-way door. Closing the pilot or revoking a class is immediate; expansion needs re-evaluation.
- **Revisit triggers**: the first three runs or the 30-day window expires; missing logs, ineffective revocation, wrong classification, or concentrated human corrections appear; 30 consecutive days unused; or expansion beyond low-risk classes is needed. Any one → retro decides keep, adjust, or revoke.
- **Related**: [ADR-0019](../../harness/adr/0019-methodology-nonnegotiable-guardrails.md) (the non-negotiable core), OD-13.

## OD-24 Skill dual-copy experimentation strategy — global experiments / project backup / DOGFOOD field-testing (two-way door)

- **Problem**: structural skill rebuilds such as the design-Q digital-levels revamp (grill-Q methodology-improvement W01 Q3-A) should not directly modify this project's stable version; the user ruled the experiment-site strategy as "this project's skills/ as backup, the global `~/.claude/skills/` as the experiment, dogfood field-testing under the peer DOGFOOD project" (W01 supplementary statement, 2026-08-14). The strategy turns the dual copies from "rebuilt-identical (2026-08-07, desensitization diff only)" into an **intentional fork** — the drift risk needs explicit governance.
- **Deferral reason**: during the fork, both copies' responsibilities and feed-back timing evolve with the experiment; merge-back conditions depend on DOGFOOD evidence.
- **Current placeholder**: global = experimental version (structural changes land there first); this project's skills/ = backup stable baseline (the distribution surface); the DOGFOOD project = field-test site (same domain as OD-13's pilot site). Experiment validated → feed back into the project version and restore identity; experiment failed → roll the global side back to the project version.
- **Stress-test revision (2026-08-14, grill-designq-digital-levels-design W01 Q2-C/Q6-A)**: ① field-testing revealed **bidirectional drift** (the long-running project version led; the doctor HARNESS-RULES global version led by 3 additions of 2026-08-14; the design-Q FORMAT global version led by 1) — the one-way assumption "global = experiment / project = stable backup" is corrected to "**bidirectional drift: whichever side leads, sync first, then experiment**": before a rebuild, first sync global ⇄ project to a common starting point; ② **three experiment-window constraints**: within the window avoid initiating formal runs of the three skills in other projects (informal use at your own risk); bugs found during the window are fixed first, not rolled back (unless destructive); DOGFOOD completion means feed-back and closure, window target ≤ 2 weeks.
- **Reversibility**: two-way door (experiment branches can roll back and merge).
- **Revisit triggers**: ① DOGFOOD field-testing passes → feed-back and merge; ② during the window the dual-copy drift causes actual confusion / misuse (user feedback); ③ the rebuild is abandoned → global restored to project identity; ④ the fork persists > 60 days without feed-back (long-term fork = a no-master signal); ⑤ the window exceeds 2 weeks without closure. Any one → re-evaluate the strategy or execute the merge.
- **✅ This round closed (2026-08-17, commit a9086be)**: the levels revamp fed back and merged (F027–F034 all green; DOGFOOD case 1 + legacy-suite migration drill accepted; case 2 skipped by user ruling, recorded); window took 3 days (within the ≤ 2-week target); the bidirectional-drift evidence merged into the practice (sync first, then experiment). **The strategy is retained for reuse in later structural skill rebuilds**; the triggers stay valid for the next round.
- **2026-08-20 semantic extension ([ADR-0024](../../harness/adr/0024-governance-history-split-dual-form.md); design ruling 2026-08-20; execution pending P0–P4)**: the "intentional fork" is elevated from an **experiment-window temporary state** to a **steady-state division of form** — global side = distribution-clean form (out-of-the-box, no evolution history); project side = the workshop's complete form; the sync semantics change from "byte-identical both sides" to "rule body (SKILL.md/engines/FORK-NOTES) identical + history layer (CHANGELOG) project-side only" (sync-check class rules; EXCEPTIONS emptied). This entry's "sync first, then experiment" principle still applies under the steady-state division (experiments still start from a common point).
- **Related**: OD-8 (engine-copy drift precedent), OD-13 (DOGFOOD site), TODO's "design-Q digital levels" block, [HLD §6](../../harness/design/designq-digital-levels/HLD.md).

## OD-25 This repository's governance-file layout vs HARNESS-RULES §6 (two-way door)

- **Problem**: HARNESS-RULES §6 (ruled 2026-08-14) states "for projects with a `harness/`: OPEN-DECISIONS.md / TODO.md / CONTEXT.md belong at the `harness/` root"; this repository itself keeps OPEN-DECISIONS / CONTEXT under `docs/` and TODO at the repository root — the methodology's own production workshop conflicts with its own authoritative rule. Root cause is chronology: ADR-0011 (2026-08-07) "CONTEXT/OPEN-DECISIONS/TODO are project-inherent files; paths unchanged" predates the §6 ruling (2026-08-14), which made no disposition for this repository's legacy layout.
- **Deferral reason**: migration means repository-wide reference-repair (README/CLAUDE.md/ADR/archived-questionnaire living references) — a full MIGRATION-FLOW round; not appropriate to do in passing during a README stress round; and whether this repository, as rule-maker, should "self-migrate as demonstration" or claim a "production-workshop exemption" is a positioning judgment needing its own ruling.
- **Current placeholder**: keep the current layout (the README's "repository structure" section describes it truthfully); rule §6 takes effect as usual for new host projects.
- **Reversibility**: two-way door (pure file moves + reference repair; re-migrable).
- **Revisit triggers**: ① the next large harness governance / migration round executes MIGRATION-FLOW together; ② an external adopter is confused by this repository's layout conflicting with §6; ③ the doctor-harness validation script adds §6 to its checks, flagging this repository. Any one → rule "self-migrate as demonstration vs exemption note" and execute.
- **Related**: [HARNESS-RULES §6](../../skills/doctor-harness/HARNESS-RULES.md), [ADR-0011](../../harness/adr/0011-abandon-plan-r-hardcode-harness.md) (the original "paths unchanged" ruling), [MIGRATION-FLOW](../../skills/doctor-harness/MIGRATION-FLOW.md).

## OD-26 grill-Q questionnaire quality data-pipeline form — embedded in processing reports vs an independent ledger (two-way door · provisional)

- **Problem**: the aggregation form for grill-Q item-level quality signals (❌ mis-routing rate / 🤔 escape-hatch rate / ✍️ custom rate + mis-routed-item attribution): a "quality signals" section embedded in processing reports, or an independent quality ledger under harness/?
- **Source**: 2026-08-19 grill-with-docs "grill family boundary and mis-routing governance" dive Branch D (user triggered the escape hatch → de-risking protocol step 1 judged a two-way door → adopted the recommended minimal slice + provisional trace).
- **Deferral reason**: the benefit difference between the two forms depends on real cross-wave aggregation frequency; this repository has no instance data; an independent ledger is in tension with the rulings "no ex-ante gates" (grill-skill-family W01 Q6-B) and "no global criteria" (W01 Q9-C) — needs instances to justify.
- **Current placeholder (provisional)**: processing reports embed a "quality signals" section + archived-questionnaire tail traces + retro cross-wave aggregation + same-cause attribution ≥ 2 goes through the [ADR-0023](../../harness/adr/0023-skill-md-layered-slimming.md) promotion; **no independent ledger**.
- **Reversibility**: two-way door (all document/format-level changes, git-revertible; a ledger is pure addition, addable anytime).
- **Revisit triggers**: ① ≥ 1 instance of "attributions scattered, hard to aggregate" during retro aggregation; ② same-cause mis-routing ≥ 2 times but retro misses it (loop-failure signal); ③ grill-Q wave frequency rises to where manual aggregation is infeasible. Any one → re-evaluate the independent-ledger form.

## OD-27 design-Q questionnaire granularity vs methodology §4.5 decision tiering — residual tension in init / no-whitelist scenarios (two-way door)

- **Problem**: methodology v5 §4.5 (canonical) states explicitly "🟢 low-stakes two-way door → take the recommendation directly, spend no energy; ⚪ pure execution → delegable to AI"; design-Q's W00, with opt-in off (default), asks the human item-by-item for every decision point "with a clear AI lean" (mostly 🟢/⚪ tier) — the tension with canonical sits on paper. After the 2026-08-20 grill-design-q-w01 Q5 ruling C (delegate whitelist interface), the tension narrows to: **init mode and projects without delegation.md still ask the human for everything** — that boundary is unwritten in canonical; option B's claim that "§4.5's table intends implementation-phase tiering, not design-phase" is advocacy, not conclusion.
- **Source**: [grill-design-q-w01](../../harness/questionnaires/archive/_misc/grill-design-q-w01.md) Q5 (user chose C; neither the split-section scheme A nor "keep + CONTEXT disambiguation" B).
- **Deferral reason**: whether to give design-phase decisions their own tiering semantics (every design decision, however small, is eyeballed vs aligning with §4.5 to save energy) depends on the user's value trade-off on their own design-phase judgment energy — an experience gap; and the delegate interface's (Q5-C) actual whitelist coverage is unknown — judge the residual surface after seeing the interface's real effect.
- **Current placeholder**: keep W00 full item-by-item asking + Q5-C's delegate whitelist interface (in feature mode with delegation.md, whitelisted decisions auto-adopt with traces, not entering W00; interface details are a design-Q spec revision, awaiting authorized execution).
- **Reversibility**: two-way door (questionnaire-structure-level change, git-revertible).
- **Revisit triggers**: ① after the delegate interface lands and runs through 1 real feature project, re-evaluate whether init / no-whitelist scenarios still need full asking; ② the user experiences "W00 fatigue rubber-stamping" in a real project (linked with Q4-A quality signals); ③ the methodology's next revision touching §4.5 writes the "design-phase vs implementation-phase" tiering boundary en passant. Any one → adjudicate A (sectioning) / B (CONTEXT disambiguation) / keep.
- **Related**: [methodology_v5 §4.5](../../docs/methodology/methodology_v5.md), OD-23 (delegate pilot), design-Q DESIGN.md (a decision row when the interface lands).

## OD-28 design-Q spec-revision self-check list — await a second spec-contradiction instance before promoting (two-way door · watch item)

- **Problem**: after revising design-Q's engine specs (QUESTIONNAIRE-FORMAT / PROCESSING-RULES / STAGE-SKELETONS / SKILL.md), there is no spec-level self-consistency regression: the existing grep self-check anchors "at question-posing time" (against questionnaire incompleteness), not "at revision time" (against cross-rule contradictions). Precedent: the ordering contradiction between FORMAT rule 4 (✍️ position) and rules 13/14 (option ordering) existed from introduction and was only caught in real use on 2026-08-18 by first-principles W01.
- **Source**: [grill-design-q-w01](../../harness/questionnaires/archive/_misc/grill-design-q-w01.md) Q10 (user chose A, adding the "form × protocol" cross table; B's "revision self-check list" enters OD as a watch item per the ★recommendation's rationale — not adopted for immediate creation).
- **Deferral reason**: aligning with [ADR-0023](../../harness/adr/0023-skill-md-layered-slimming.md)'s promotion mechanism "a lesson repeats ≥ 2 times before becoming standing" — cross-rule contradictions have 1 confirmed instance so far; a self-check list adds a procedure to every revision; creating it before the contradiction frequency is confirmed risks ritualism.
- **Current placeholder**: no list; when revising skill specs, manually mind cross-rule references; the "form × protocol" cross table (Q10-A), once landed, itself eliminates a class of combinatorial contradiction sources.
- **Reversibility**: two-way door (a list is pure addition, addable anytime).
- **Revisit trigger**: a second spec-level cross-rule contradiction caught in real use (any skill's FORMAT/PROCESSING/SKILL rules conflicting). Triggered → create a "revision self-check list" in the corresponding DESIGN.md's maintenance section.
- **Related**: [ADR-0023](../../harness/adr/0023-skill-md-layered-slimming.md) (promotion mechanism), OD-8 (engine four-way sync — an existing constraint at revision time).
