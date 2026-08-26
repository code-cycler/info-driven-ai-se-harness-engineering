---
lang: en
en-source: CHANGELOG.md
zh-hash: f0493fe41f5f
---

[中文](../CHANGELOG.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](docs/CONTEXT.md). Incremental protocol: each new zh entry ships with its en counterpart (append-only mirror).

# Changelog

> The single record of repository-level, externally visible changes (migrated from the README's "release notes" section, 2026-08-20).

> **Recording rules**: this file is the single record of repository-level, externally visible changes — every change **perceivable to adopters** (skill behavior / artifact structure / methodology content) must be recorded; purely internal repository governance (questionnaire archiving, link repairs, etc.) is not. Reverse-chronological. Skills carry no independent version numbers; this file is the only window for perceiving `skills/` changes.

## i18n first phase complete: full English-mirror chain delivered (2026-08-26, ADR-0025)

- **First-phase translation surface closed**: the top-level `en/` mirror tree, 15 files all green (README + the methodology trio + CONTEXT + OPEN-DECISIONS + 8 SKILL.md files + this CHANGELOG; docs/LICENSE is an en-native notice file, not counted); the `en/skills/` link policy = engine / governance-history files point to the Chinese originals (L1 §1.4); grill-with-docs runs under the special-case clause (English body verbatim, only residual Chinese translated).
- **Changes perceivable to adopters**: the repository is now readable as a complete English tree (Chinese remains the single authoritative source; on conflict, Chinese governs); `scripts/i18n-check.py`'s TRANSLATABLE obligation list closed out via stage-by-stage expansion (README → the five docs files → skills/*/SKILL.md → CHANGELOG.md); the English-side incremental protocol = each new CHANGELOG entry ships with its en counterpart (append-only; this entry is the first dual landing).
- **Terminology**: the CONTEXT "English Glossary" section totals 80 entries (first batch 18 / second 31 / third 28); translations follow that table — per-file self-translation is forbidden.

## i18n kickoff: English mirror started (2026-08-23, ADR-0025)

- **This entry = a revisit trace**: readme-revamp (2026-08-20) had decided "no English README (listed as a future option, to be revisited when external demand appears)" — this user-initiated i18n kickoff (feature-i18n-support) met the trigger condition, and that decision was formally overturned (see the [readme-revamp design-doc note](../harness/design/readme-revamp/L0-vision-readme-first-impression.md) and [ADR-0025](../harness/adr/0025-english-mirror-drift-governance-integration.md)).
- **Changes perceivable to adopters**: the repository gains a top-level `en/` English-mirror directory (Chinese is the single authoritative source; English is a one-way derivative); a language-switch line at the top of the root README; and a new `scripts/i18n-check.py` (English-mirror drift check: missing mirror / orphan / stale / missing markers / broken link, five classes; the fourth manual pre-commit gate). Translation proceeds in phases: the first phase covered README, with the methodology trio / CONTEXT / OPEN-DECISIONS / the 8 SKILL.md files / CHANGELOG following in batches; historical versions (archive/) and internal-governance products are not translated.

## skill evolution (2026-08-20, governance-history split + dual-side shape division, ADR-0024)

- **Each skill gains a `CHANGELOG.md` (governance history, held only by this repository)**: all dated ruling-provenance annotations moved out of SKILL.md, which now keeps only current rule values + a one-line header index — **SKILL.md resident-context density improved** (pillar one landing on the repository's own shape); the three questionnaire skills also gain `FORK-NOTES.md` (intentional-fork declarations, identical on both sides). Design decisions remain in each `DESIGN.md` (converged into a pure decision table).
- **Dual-side standing shape division (install-shape change)**: `~/.claude/skills/` (user-global) becomes the **distribution-clean shape** — only SKILL.md + engine/template files + FORK-NOTES, no longer DESIGN.md / CHANGELOG.md (works out of the box, no evolution noise); this repository's `skills/` = the workshop-complete shape. For already-installed users: the global side's DESIGN.md/CHANGELOG.md were removed with the upgrade; all history remains in this repository (zero information loss; doctor-harness hands-on details are held privately in the global side's `DOGFOOD-LOG.md`).
- **Supporting mechanisms**: `skills-sync-check.py` upgraded with class rules (history-layer files existing project-side only = legal; DESIGN/CHANGELOG are history layer); the project CLAUDE.md's iron rule 8 semantics updated accordingly; `harness/STATUS-LOG.md` created to carry the repository's internal state history (CLAUDE.md's status section slimmed to a 3-line snapshot).

## README revamp + release notes moved out (2026-08-20)

- **README upgraded to the external first-impression shape**: "the 8 core skills" went from a one-line table to card form (per skill: positioning / triggers / outputs / core dimensions or mechanisms); a new "skill questioning/confirmation dimensions quick reference" table (authority = CONTEXT's "questioning dimensions quick reference" section; the README is a navigation copy); the minimal adoption slice promoted to its own heading; section order reorganized + lightweight badges.
- **Release notes moved to this file**: all historical entries of the README's "release notes" section migrated to the repository-root CHANGELOG.md (GitHub recognizes it automatically); the README's original spot keeps only a one-line link. Recording rules unchanged.
- **Accompanying drift fixes**: three grill-retirement leftovers in practice §8.3 + the sync pointer at the CONTEXT quick-reference section head (F035).

## skill evolution (2026-08-19, grill-family governance day: retirement + spec revisions + boundary mechanisms)

- **grill retired, family 9 → 8**: `/grill` removed (into `waste/skills/grill/`, recoverable); its "general × single-point deep-dive" niche is carried by grill-with-docs' new **general mode** (not codebase-bound + zero trace; entry confirmation + mid-course switch-back double fallback). Adopters with grill installed: uninstall it; use grill-with-docs directly for general questions.
- **Lightweight mode (action-Q / grill-Q / design-Q)**: for light tasks the AI proposes and the human decides, walking a slimmed pipeline (tiered research / small-wave direct asking / no archiving) with "preliminary conclusions first + light human verification"; the don't-assume / verify-first iron rules are not waived by lightness.
- **grill-Q anti-misframe mechanisms**: entry-calibration gate (before questioning, confirm with the human the "artifact-understanding summary + key-claim list + stress-test focus") + a per-question ❌ misframe annotation (≥ 2 questions marked in the same wave → stop the wave and re-calibrate the frame) + blocking escape hatches can divert to a grill-with-docs single-point deep dive + a processing-report quality-signals section.
- **SKILL.md layering principle established** ([ADR-0023](../harness/adr/0023-skill-md-layered-slimming.md)): rules stay in SKILL, lessons move to DESIGN; only the same mistake recurring ≥ 2 times earns a permanent promotion; progressive enforcement.
- **In-version canonical revisions** (no version bump): philosophy §3.1's routing table gains a "cognitive states" row (the two-family routing anchor); methodology §4.1/§4.3 wiring (three cognitive states + conflict-of-criteria priority + when in doubt, the stricter reading). Re-stress-tested via grill-boundary-canonical-w01 (9 questions, [archived questionnaire](../harness/questionnaires/archive/_misc/grill-boundary-canonical-w01.md)).

## skill evolution (2026-08-19, dual-side sync institutionalized)

- **Skill dual-side sync check online**: new [scripts/skills-sync-check.py](../scripts/skills-sync-check.py) — after changing either `skills/` (this repository) or `~/.claude/skills/` (user-global), run the check before committing, **0 violations or no commit**; the script is check-only and picks no side — which side is right is a semantic judgment, always the human's (ruling-exception whitelist built in). Background: the 2026-08-18 bidirectional merge (9-skill reconciliation + 8/14 revisions back-ported) exposed a "fixed in-project, missed in-global" gap; institutionalized closure.

## skill evolution (2026-08-16/17, design-Q layered LN revamp)

- **design-Q artifact structure upgraded to LN naming**: the VISION/HLD/LLD trio → **LN layered design** — L0-vision (the goal layer) always present, L1+/L2 added dynamically on demand, the legacy trio demoted to alias compatibility; the skeleton enhancements (HLD/LLD discrimination rules + anti-simplification minimum-contents + collapse tiers) retained, see [ADR-0022](../harness/adr/0022-design-questionnaire-digital-levels.md).
- **doctor-harness takes over layered governance**: HARNESS-RULES gains section 7 (LN layout / guide block / legacy exemption) and section 8 (legacy-structure restructuring flow + old-set migration map); this repository's existing design suites (the repo/ trio) git-mv'd through an LN-migration drill.
- **Full-loop closure**: F027–F034 all green (end-to-end tests passed); DOGFOOD case 1 user-verified; the first retro document produced (retro-questionnaire's first run).

## methodology_v5 (2026-08-14, methodology section-continuity and contract-first)

- **Methodology file upgraded to v5**: continuous numbering §0 through §9 across the body (the v4 mapping table at the file top) + repository-wide reference review; §4.3 (old §5.3) two-family table adds action-Q; §5.3 (old §7.3) adds "sequencing discipline" — contract-layer changes must **update the canonical design first, then continue irreversible actions** (ADR-0021 generalized).
- **Accompanying items**: CONTEXT gains normative navigation and the "provisional" status word; the same round kicked off the design-Q digital-levels revamp, dogfood definition disambiguation, and the 704-line methodology audit (see [TODO.md](../TODO.md)).
- **Version disposition**: v4 kept in [`docs/methodology/archive/`](../docs/methodology/archive/) as the historical master.

## v7 (2026-08-14, philosophy as an independent article and dual-file governance)

- **Philosophy file upgraded to v7**: the body unified into continuous sections §1–§5, an independent reading entry added, with the v3 old-section mapping, compatibility aliases / redirection notes, and historical questionnaire/ADR traceback retained; the terminology boundary between the methodology harness and the runtime harness added.
- **Honest governance boundaries**: the current known-gap status, the first three disciplines' minimal entry/exit templates, and the rework / de-blackboxing proxy indicators explicitly marked as reflection prompts rather than effect verification or automatic acceptance gates.
- **Version disposition**: v6 kept in [`docs/methodology/archive/`](../docs/methodology/archive/) as the historical master, v7 becoming current canonical; philosophy and methodology (upgraded to v5 the same day) are governed as peer canonical dual files under [ADR-0018](../harness/adr/0018-canonical-dual-challenge-governance.md).

## v6 (2026-08-13, philosophy governance evolution)

- **Philosophy file upgraded to v6**: on top of v5's safety-science fourth-discipline view and "de-blackboxing AI", a full-text reading route and section transitions; §8.6 clarified as "the methodology's own governance loop", with a unified claim-status template and a discipline governance roadmap.
- **Governance evolution path**: systems/requirements engineering, epistemology and measurement science, configuration management/QMS, cognitive science/HCI, knowledge management/organizational learning, information security/threat modeling, formal methods, cybernetics/decision theory mapped onto governance mechanisms, minimal artifacts, and entry conditions — without turning them into mandatory process for a personal project.
- **Version disposition**: v5 kept in archive as the historical master; v6 was current canonical, now succeeded (and archived together) by v7.

## v5 (2026-08-11, philosophy thesis restructure)

- **Philosophy file upgraded to v5**: added **§8 the safety-science view: de-blackboxing AI** (the fourth-discipline view; the black-box three-level definition + orthogonal to pillar one + three risks + consolidating existing auditable-instrument countermeasures + the WAI/WAD elastic boundary); the top-of-file discipline mounts expanded to four (human factors / software engineering / operations research / safety science); the meta-principles failure-mode table gains "black-box trust hijacking". v4 to archive.
- **Discipline-mount layering** ([ADR-0014](../harness/adr/0014-discipline-mapping-strategy.md)): the philosophy body mounts only "thesis-core disciplines"; CONTEXT's "project discipline map" carries the panorama (systems engineering / CM / QMS / PM / KM / cognitive science + the security / reliability / resilience terminology trichotomy).
- **A complete write→review→implement loop**: grill-Q philosophy-v4 (W01/W02, 18 revisions) → discipline-mapping → grill-with-docs (6 de-blackboxing crystallizations) → design-Q (VISION/HLD/LLD + [ADR-0015](../harness/adr/0015-deblackbox-anchor.md)) → design-suite stress test (10 revisions) → long-running drafting (commit 530d0f4).

## skill evolution (2026-08-08, doctor-harness the 9th skill)

- **Harness evolution-governance skill online**: organizes the harness zone (layering / migration / validation / record-keeping); rules authority [HARNESS-RULES.md](../skills/doctor-harness/HARNESS-RULES.md) (ADR-0012/0013); validation script [scripts/harness-check.py](../scripts/harness-check.py) (three checks: naming regex / ADR number continuity / archive location).
- **Archive subdirectories**: 41 archived questionnaires migrated by feature/topic into 10 subdirectories under `harness/questionnaires/archive/`, with a [README index](../harness/questionnaires/archive/README.md).
- **Format feedback landed**: single-wave questionnaire cap 10, small-wave (direct Q&A) threshold 3, unified across the four copies (design-Q / grill-Q / retro-Q / action-Q); new [MIGRATION-FLOW](../skills/doctor-harness/MIGRATION-FLOW.md) migration-process doc.

## skill evolution (2026-08-07, design-Q spec cleanup)

- **Landing paths back to the hardcoded `harness/`** (2026-08-07, Plan R withdrawn; see [ADR-0011](../harness/adr/0011-abandon-plan-r-hardcode-harness.md)): questionnaire/ADR landing paths for design-Q + grill-Q/retro-Q/action-Q + long-running are **all hardcoded to `<project root>/harness/`** (design/ + questionnaires/ + adr/); CONTEXT/OPEN-DECISIONS/TODO are project-inherent files, paths untouched.
- **design-Q skeleton enhancements**: HLD/LLD discrimination rules (phase-invariant vs incremental + the two-sentence discriminators) + anti-simplification minimum-contents (H1–H5/L1–L5, 10 items, constraining content not just structure) + collapse tiers. design-Q skeleton only; not spread to grill/retro/action.

## v4 (2026-08-05)

- **Methodology + philosophy upgraded to v4**: audience narrowed to the **individual developer**; pillar two gains the mechanism-layer thesis ("no guardrails → AI output quietly degrades"); the philosophy file disciplined (human-factors engineering / software engineering / operations research — three views).
- **Terminology version note**: all 8 terms **retained** (no rewording), with discipline-reference annotations + the three-condition gate for new terms added (see the [CONTEXT terminology-governance section](docs/CONTEXT.md)); old skill copies need no term migration, but landing paths (harness/) and normative priority follow this repository.
- **Repository structure**: harness/ (design docs + archived questionnaires) and docs/ (project files) physically separated; AGENTS.md added (Codex entry routing).
- **Normative priority**: methodology claims (canonical) > ADR > CONTEXT terms > skill specs > practice (see [CLAUDE.md](../CLAUDE.md)); v3 kept as the historical master.
