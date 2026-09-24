---
name: proj-overview
description: Human-readable project-mastery view generator (cross-cutting tool type, 9th in the skill family). Scans the project's structural/governance/functional file surfaces and generates a single read-only derived view harness/PROJECT-OVERVIEW.md: five linear sections + mermaid relationship graphs (one BFS hierarchical decomposition pass + one DFS functional logic-chain pass), helping the project's owner quickly regain mastery of the whole project when entering from different points in time and space. Adds no new source of authority; the source files govern. Triggers: "project map", "project overview", "regenerate project view", "regain mastery", "re-orient", "I'm lost".
lang: en
en-source: skills/proj-overview/SKILL.md
zh-hash: a5e0ac901992
---

[中文](../../../skills/proj-overview/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Generate a one-page project-mastery view **for humans**. Harness files target AI context rebuilding (rigorous and detailed); this artifact targets humans (cognition-friendly) — read-only derivation, design orientation "reduced load > added load".

## Positioning and boundaries

- Cross-cutting tool type: not part of the five-stage loop's main path; pure generation, no questionnaire, no AskUserQuestion.
- Artifact = a single read-only derived view: adds no source of authority, does not participate in norm-priority adjudication, **the source files govern**.
- Does not take over the five existing files' duties: AI session entry (CLAUDE.md) / external publicity (README) / change record (CHANGELOG) / action tracking (TODO) / status history (STATUS-LOG).
- Never make one-way-door decisions from a stale view (before release/deletion/spending/desensitization, always verify against the source files).

## Main flow, four steps

1. **Scan (three-tier graded reading; full-repo deep reads forbidden)**: structural class, full read (README / CLAUDE.md / directory tree); governance class, header read (CONTEXT section titles / OD entry heads / ADR title lines / design-suite indexes); key-N selective read (files carrying the current mainline, back-derived from the status-tracking file and recent changes).
2. **Extract**: two node classes (function/structure nodes, information/artifact nodes); three edge classes (containment, dependency, flow·trigger). The current-status snapshot = the project's status-tracking file header (when following this methodology = TODO.md header), **quoted and paraphrased directly; the AI adds no judgment of its own**; in projects without this convention, use recent git activity as the source and label the data source in the snapshot section; if the header clearly disagrees with recent git activity → prompt the human to update first, then generate; the AI never ghost-writes the snapshot.
3. **Organize**: five sections in fixed order ① one-sentence project positioning → ② structural panorama (BFS master graph + block index table) → ③ decision threads (key-decision timeline) → ④ current-status snapshot → ⑤ DFS deep-chain views.
4. **Render**: md + mermaid code blocks; short names/labels inside graphs, links unified in the index table beside each graph (markdown relative links, file-level primarily, key chains to "file#section" anchors).

## Output specification (hard constraints)

- Target `harness/PROJECT-OVERVIEW.md`; manually triggered, overwrite-style regeneration (git history is the versioning; no `_vN` increments).
- File-header trio: generation timestamp + information-source list (path + one-line summary per file) + "the source files govern; this is a derived view" declaration.
- Total length ≤ 250 lines (over the limit → trim: detail grading / link externalization); target ≤ 15 lines per section.
- **BFS: one hierarchical-decomposition graph**: project root → layers → functions under each layer, expanded layer by layer down to function granularity (below functions, hand off to DFS and the index table); ≤ 30 nodes; over the limit, aggregate by layer (aggregation prefers keeping each layer's functions complete); note the layering rationale in the "structural panorama" section.
- **DFS: one logic chain per function**: function → internal logic/sub-functions → dependencies → landing artifacts; key functions (carrying the current mainline/high risk) get full chains, other functions get a one-line short chain + index table; ≤ 30 nodes per graph; graph count ≥ 2 and ≤ 12.
- Loose drift governance: not covered by check scripts, no mandatory sync duty; freshness relies on the file-header trio's self-declaration.

## Human-factors design principles

- Information layering: disclosure order = overview → structure → chains → status (panorama before detail).
- Progressive disclosure, three tiers: overview section no links → structure section index tables → chain section "file#section" anchors.
- Graph size ≤ 30 nodes/graph; linear cognitive order (five sections in fixed order, never reordered).
- Discipline anchors: cognitive load, situation awareness (cite CONTEXT's existing definitions; coin no new terms).

## Style specification

- Prohibitions: metaphorical epithets ("anchor-of-stability" style), literary rhetoric, emotional adjectives.
- Terminology (common systems-engineering intersection; cites no single standard): module / interface / dependency / baseline / traceability / verification / configuration item / responsibility / boundary / constraint / entry / flow / status / snapshot / layer / coverage / deviation / adjudication / trigger / delivery.

## Triggers and self-check

- Trigger phrases in the frontmatter; every trigger = full regeneration (overwrite-style).
- Post-generation self-check (one-off commands; no resident script): `wc -l` ≤ 250; five section titles grep-complete; header trio grep-complete; mermaid block count ≥ 2 and ≤ 12; node self-count per graph ≤ 30; **per-graph render verification** — embed each graph in a temporary HTML (mermaid CDN), verify rendering in a browser, then delete the temporary file.
- The amnesia test is executed by the human (not built into the skill): after ≥ 3 days, read only the view and, within ≤ 15 minutes, answer three questions (current mainline / which file holds the key decision / next step); all three = pass.

</what-to-do>
