---
name: proj-overview
description: Human-readable project-mastery view generator (cross-cutting tool type, 9th in the skill family). Scans the project's structural/governance/functional file surfaces and generates a single read-only derived view at the repo root (PROJECT-OVERVIEW.md) — the first-reading entry: where a human's context reload begins (audience = any developer): eight sections (positioning / reading guide / structural panorama / governance-file summary / decision threads / status snapshot / DFS deep chains / lookup index) + a governance-file summary (every ADR/OD entry on one line) + mermaid relationship graphs (all vertical; BFS hierarchical decomposition + DFS functional logic chains). Adds no new source of authority; the source files govern. Triggers: "project map", "project overview", "regenerate project view", "regain mastery", "re-orient", "I'm lost".
lang: en
en-source: skills/proj-overview/SKILL.md
zh-hash: 4dfa724d5a94
---

[中文](../../../skills/proj-overview/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Generate a project-mastery view **for humans** — the first-reading entry: where a human's context reload begins. Harness files target AI context rebuilding (rigorous and detailed); this artifact targets humans (cognition-friendly) — read-only derivation; line count grows linearly with the source-file surface; no improvisation at generation time.

## Positioning and boundaries

- Cross-cutting tool type: not part of the five-stage loop's main path; pure generation, no questionnaire, no AskUserQuestion.
- Artifact = a single read-only derived view: adds no source of authority, does not participate in norm-priority adjudication, **the source files govern**; the three entry points each have an emphasis and may overlap (CLAUDE.md leans AI sessions / README leans external adoption / this file leans human full mastery).
- Governance-file summary = read-only derived paraphrase: **does not take over the source files' living duties** (action tracking / change records / status history remain with TODO/CHANGELOG/STATUS-LOG); once a source file changes, the summary is stale.
- Does not take over the five existing files' duties; never make one-way-door decisions from a stale view or stale summary (before release/deletion/spending/desensitization, always verify against the source files).

## Main flow, four steps

1. **Scan (graded reading; full-repo deep reads forbidden)**: structural class, full read (README / CLAUDE.md / directory tree); governance class = CONTEXT section titles / design-suite indexes **header read** + **full entry read of every ADR/OD** (each entry's title + status/decision-section first paragraph, to support a one-line summary); key-N selective read (files carrying the current mainline, back-derived from the status-tracking file and recent changes).
2. **Extract**: two node classes (function/structure nodes, information/artifact nodes); three edge classes (containment, dependency, flow·trigger). The current-status snapshot = the project's status-tracking file header (when following this methodology = TODO.md header), **quoted and paraphrased directly; the AI adds no judgment of its own**; in projects without this convention, use recent git activity as the source and label the data source; if the header clearly disagrees with recent git activity → prompt the human to update first; the AI never ghost-writes the snapshot.
3. **Organize: eight sections in fixed order** ① positioning (one sentence + three-entry emphasis) → ② reading guide (three reading tiers) → ③ structural panorama (BFS master graph + block index table) → ④ governance-file summary → ⑤ decision threads (key-decision timeline) → ⑥ current-status snapshot → ⑦ DFS deep-chain views → ⑧ lookup index ("I want to find X → go to Y", organized by question).
4. **Render**: md + mermaid code blocks; short names/labels inside graphs, links unified in the index table beside each graph (markdown relative links, file-level primarily, key chains to "file#section" anchors).

## Output specification (hard constraints)

- Target the **repo root** `PROJECT-OVERVIEW.md` (alongside README/CLAUDE/TODO — first-reading-entry discoverability first; moved out of harness/ by user adjudication 2026-09-26; AI-process artifacts stay in harness/); manually triggered, overwrite-style regeneration (git history is the versioning).
- File-header trio: timestamp + information-source list (source files listed per summary section; path + one-line summary per file) + "the source files govern; this is a derived view; the first-reading entry" declaration.
- **Reading-guide section, 3–5 lines, one line per tier pointing to section numbers**: 3-minute recovery (①⑥⑤) / 15-minute framework (first four sections + summary-table skim) / lookup (⑧⑦ + tables beside graphs).
- **Summary-section specification** (top warning line: "the source files govern; never make one-way-door decisions from a stale summary"): ADR table, 3 columns (number·with source link / title / one-sentence decision summary — sourcing = direct quote or tight paraphrase of the first sentence of the ADR's decision section, **no cross-section synthesis**; at generation, sample 3 entries for quick human review); OD table, 3 columns (number·with source link / topic / status — **read directly from the OD status field; AI classification forbidden**; in projects without that field, quote the title's gate-type annotation directly); TODO/STATUS-LOG/CHANGELOG headers as narrative + bullets; **each table's row count = the source's actual entry count**.
- **Graph specification**: all graphs `flowchart TD` (vertical); `direction LR` **forbidden** inside subgraphs; one BFS hierarchical-decomposition graph (≤ 30 nodes; over the limit, aggregate by layer); DFS dynamic selection = 1 mainline chain (whatever carries the current mainline at generation time; self-reference legal at depth 1) + 1–2 high-risk/backlog chains + optionally 1 just-closed chain, 3–5 total, ≤ 30 nodes per graph; graph count ≥ 2 and ≤ 12.
- **No hard line-count cap** (the derived nature is the constraint); **typed self-check**: fact sections (summary/snapshot/threads) traced to source files per section; structural sections (positioning/guide/index) checked against the section spec; target ≤ 15 lines per narrative section.
- Loose drift governance: not covered by check scripts, no mandatory sync duty; freshness relies on the file-header trio's self-declaration.

## Human-factors design principles

- Information layering: disclosure order = overview → how to read → structure → governance assets → evolution → status → chains → lookup (newcomer read-through progression; the amnesia fast path is carried by the reading guide).
- Progressive disclosure, three tiers: overview section no links → structure section index tables → chain section "file#section" anchors.
- Graph size ≤ 30 nodes/graph; linear cognitive order (eight sections in fixed order, never reordered).
- Discipline anchors: cognitive load, situation awareness (cite CONTEXT's existing definitions; coin no new terms).

## Style specification

- Prohibitions: metaphorical epithets ("anchor-of-stability" style), literary rhetoric, emotional adjectives.
- Terminology (common systems-engineering intersection; cites no single standard): module / interface / dependency / baseline / traceability / verification / configuration item / responsibility / boundary / constraint / entry / flow / status / snapshot / layer / coverage / deviation / adjudication / trigger / delivery.

## Triggers and self-check

- Trigger phrases in the frontmatter; every trigger = full regeneration (overwrite-style).
- Post-generation self-check (one-off; no resident script): eight section titles grep-complete; `direction LR` 0 hits; summary-table row count = the source directory's actual count (measured N annotated at generation); every summary line contains a relative link; typed self-check and ADR-summary sampling traces left (DESIGN.md); **per-graph render verification** — embed each graph in a temporary HTML (mermaid CDN), verify rendering in a browser, then delete the temporary file.
- The amnesia test is executed by the human (not built into the skill): after ≥ 3 days, read only the view and, within ≤ 15 minutes, answer three questions (current mainline / which file holds the key decision / next step); all three = pass (the 3-minute reading tier should cover the three questions).

</what-to-do>
