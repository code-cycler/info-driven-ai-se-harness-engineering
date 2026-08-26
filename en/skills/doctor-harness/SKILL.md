---
name: doctor-harness
description: harness evolution-governance skill — handles the authoritatizing of organization rules, migration tooling/flows, layout compliance validation, and evolution record-keeping for the project's "project-root/harness/" zone (design/ + questionnaires/ + adr/). Harness files go strictly under the `harness/` parent plus subfolder layering within it, never polluting the project root; layering rules live in HARNESS-RULES.md (the single authoritative source). Triggers: harness layering / reorganization, harness file migration, validating the harness layout, "how should harness files be laid out", "where does this file go", harness organization chaos needing governance, layer reform / migration (LN-naming legacy-set migration), legacy normalization (restructuring a project without harness files into the standard layout). Use when harness file organization, migration, or layout validation is needed.
lang: en
en-source: skills/doctor-harness/SKILL.md
zh-hash: 41ca5410a4d3
---

[中文](../../../skills/doctor-harness/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Handle the **evolution governance** of the harness zone (`<project root>/harness/`): authoritatizing organization rules + migration + validation + record-keeping. Harness files go strictly under the `harness/` parent, layered internally into feature/topic subfolders, **never polluting the project's directory structure**.

## Iron rules (inviolable)

1. **AI never decides for the human** — rule revisions and whether to execute a migration are decided by the human; the agent provides proposals and validation results.
2. **Organize only, never rewrite uninvited** — stress tests / validation produce findings and suggestions; they never directly rearrange directories the user has not authorized. A migration is its own action item with a DoD, initiated by the human.
3. **No raw information is lost** — migrations only move, never delete, and file names stay unchanged; archiving never rearranges existing stock.
4. **Rules are authoritative in one place** — HARNESS-RULES.md is the single authoritative source; each skill's SKILL.md only references it ("layering: see HARNESS-RULES.md"), never inlines a copy.
5. **ADR-0011 is not overturned** — layering is an **internal** organization form of harness/; it does not go back on the hardcoded landing root; the hardcoded `harness/` stays.

## Main flow

### 0. Triggering and mode determination

- **Manual trigger**: "layer this", "validate the harness", "how should harness files be placed"; or when harness organization is in chaos (design/ mixed usage, naming drift, archive bloat).
- **Determination**: which of these this run is — ① organization rules (landing in HARNESS-RULES.md) ② migration execution (restructuring directories) ③ validation (running the script) ④ record-keeping (recording changes) ⑤ layer reform (legacy trio → LN-naming migration, per HARNESS-RULES sections 7/8) ⑥ legacy normalization (project without harness files → standard structure, per section 8's five-step flow) ⑦ **governance-history layout** (establishing and migrating the history carriers CHANGELOG/FORK-NOTES/DOGFOOD-LOG/STATUS-LOG; stripping history annotations out of rule files; the five increment-recording triggers — per section 9 / ADR-0024) — singly or in combination.

### 1. Rule authority (organization rules)

- Read [HARNESS-RULES.md](../../../skills/doctor-harness/HARNESS-RULES.md) (the single authoritative source) and confirm whether it covers the current scenario:
  - **Layering definitions**: the design/<feature>/ predicate (feature-level = will be independently referenced / conflicts with other features → subdirectory; global or single-file designs sit at the top level);
  - **Ownership criteria**: a submodule with its own CLAUDE.md/git/release boundary → its own harness; otherwise it belongs to the main root;
  - **Naming conventions**: per-mode regexes (init/feature/grill/retro/confirm) + exemption list;
  - **Archive rules**: new archives get feature/topic subdirectories; existing stock is not moved; README index;
  - **Layered-design-document rules (LN naming)**: `L<N>-<feature>.md` naming / feature-directory or single-file multi-section layouts / header guide block / legacy-trio exemption for existing stock (section 7);
  - **Legacy-structure restructuring flow**: inventory → create the zone → semantic mapping (migration map) → mark gaps as to-be-filled instead of ghost-writing them → human confirms to seal; DoD = sealed once fully marked (section 8);
  - **Governance-history layout (section 9, ADR-0024)**: carrier naming and granularity (skill CHANGELOG project-side only / FORK-NOTES identical on both sides / DOGFOOD-LOG global-side only / STATUS-LOG); the one-side-only rule for the history layer (a sync-check class rule); index-pointer requirements; the five increment-recording triggers + the anchor-update obligation when a section title is renamed.
- If the rules have a gap (a new scenario not covered) → draft a revision proposal; after the human confirms, update HARNESS-RULES.md + leave a CHANGELOG trace.

### 2. Migration flow (restructuring + broken-link regression)

When there is a directory-restructuring need (e.g. this layering landing), execute the 7-step flow of [MIGRATION-FLOW.md](../../../skills/doctor-harness/MIGRATION-FLOW.md):

1. **Design the new layout** (check ownership item-by-item against the predicates) → 2. **Move files** (git mv, move-only-never-delete) → 3. **Recompute relative links** (archived-questionnaire depth) → 4. **Broken-link regression** (0 introduced this time) → 5. **Run validation** (harness-check.py, 0 violations) → 6. **Spec sync** (SKILL.md references) → 7. **Leave a trace** (CHANGELOG).

### 3. Layout compliance validation

- **Script**: `python3 scripts/harness-check.py [harness_root]` — three checks (questionnaire naming regex / ADR number continuity / archive location); zero output when 0 violations (the false-positive gate).
- **Trigger**: mandatory as a migration's DoD; afterwards manual / pre-release optional; never wired into any skill's every-run flow.
- Violation list → the human decides whether to fix (the agent offers a fix direction, never fixes unilaterally).

### 4. Evolution record-keeping

- Every migration / rule revision appends one entry (date + change + reason) to the project repository's skills/doctor-harness/CHANGELOG.md (project side only), so "why the harness looks like this" stays traceable.

## Division of labor within the family

| skill | scenario | relation to doctor-harness |
|---|---|---|
| design-Q / grill-Q / retro-Q / action-Q | generate questionnaires / stress tests / retrospectives / action confirmation | landing paths layered per HARNESS-RULES.md (reference, not copy) |
| long-running | cross-session implementation | rebuilds context from harness/questionnaires/archive/, follows layered archiving |
| delegate | decision delegation | cross-cutting; harness-organization decisions are not delegated by default (rule authority stays with the human) |

**Handoff**: doctor-harness is a cross-cutting governance skill, not locked into a linear stage; whenever any skill's landing hits a "where does this go" ambiguity, adjudicate per HARNESS-RULES.md.

</what-to-do>

<supporting-info>

- Authoritative harness organization rules (single source): [HARNESS-RULES.md](../../../skills/doctor-harness/HARNESS-RULES.md)
- Directory-migration execution flow: [MIGRATION-FLOW.md](../../../skills/doctor-harness/MIGRATION-FLOW.md)
- Evolution change log (project side only): the project repository's skills/doctor-harness/CHANGELOG.md; global-side hands-on details in DOGFOOD-LOG.md (private)
- Validation script: `python3 scripts/harness-check.py [harness_root]` (the canonical copy lives in the engine repository's `scripts/`, alongside desensitize.py; **do not copy the script into** the validated repo if it is git-tracked — when validating across repos, pass the target repo's harness root path)
- This skill's design decision records (project side only): the project repository's skills/doctor-harness/DESIGN.md + the design suite `harness/design/doctor-harness/` (VISION/HLD/LLD)
- Decision basis: [ADR-0012](../../../harness/adr/0012-harness-layering-rule.md) (layering rules) + [ADR-0013](../../../harness/adr/0013-harness-layering-migration.md) (migration execution) + [ADR-0011](../../../harness/adr/0011-abandon-plan-r-hardcode-harness.md) (hardcoded harness/)

</supporting-info>
