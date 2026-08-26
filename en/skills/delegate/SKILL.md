---
name: delegate
description: Project-level governance of decision-class delegation. Manages the per-project delegation governance file (project-root delegation.md: the delegable decision-class whitelist + never-delegate list + per-entry revocation conditions + master switch); the AI autonomously executes only decision classes inside the list and logs every case (delegation-log.md, an auditable queue); anything outside the list always goes to the human — the AI has only an escalation-proposal right, no self-classification right; judgment rights (product / engineering / security / merge) are never delegated; end-of-task / retro summarizes and reviews; preview-grade documents have migrated to design-questionnaire (single source), and this skill handles only the whitelist / log / revocation. Triggers: initializing the delegation list for a new project / new engineering effort, "delegate", "delegate decisions", "delegate", "delegation", enabling / adjusting / revoking delegation, viewing the AI autonomous-decision log, decision-delegation dogfood pilot.
lang: en
en-source: skills/delegate/SKILL.md
zh-hash: d023b615851f
---

[中文](../../../skills/delegate/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

# delegate · decision-class delegation

> Makes "delegate simple decisions to the AI, keep the human focused on judgment" a governable, traceable, revocable mechanism.
> Origin: the host project's "decision delegation" OD entry (produced by a grill-questionnaire stress test; timeline in the CHANGELOG). Currently a dogfood pilot; feedback returns to that OD entry.

## Iron rules (inviolable)

1. **Judgment rights are never delegated** — the four judgment classes (product, engineering, security, merge) always stay with the human; this skill handles only execution-layer "decision classes".
2. **The AI has no self-classification right** — a decision point not in the whitelist → always ask the human; the AI can only "propose escalation" (propose adding a class to the whitelist; the human decides).
3. **Forbidden zones take precedence** — when a decision seems to fall both in the whitelist and the never-delegate list, treat it as forbidden.
4. **Log every case, no batching** — every autonomous decision is written to delegation-log.md immediately; raw information is not lost; append-only, never edited.
5. **List changes are human-initiated only** — the AI may propose, the human approves; every change must be recorded in delegation.md's Changelog.
6. **Revocation takes precedence** — the moment a per-entry revocation condition hits, stop (that decision class → suspended); no arguing, no carrying on; with the master switch `enabled: false`, everything goes to the human.

## File conventions

| file | role | nature |
|---|---|---|
| `<project root>/delegation.md` | governance file: whitelist, forbidden zones, revocation conditions, master switch, Changelog | single source of truth; changes must be human-initiated |
| `<project root>/delegation-log.md` | auditable queue: one entry per AI autonomous decision | append-only log; entries added, never edited |

Both files are version-controlled. Templates in [templates/](../../../skills/delegate/templates/).

## Main flow

### 1. init (at the start of a project / engineering effort, or on first enablement)

1. Read the project conventions (CLAUDE.md / AGENTS.md / existing agreements) and draft this project's delegation.md per `templates/delegation-template.md`: whitelist candidates listed class-by-class, each class spelling out its scope / constraints and revocation triggers.
2. **The human reviews class-by-class**: delete, modify, confirm; the forbidden-zone list is walked item-by-item.
3. On finalization, record the first Changelog entry (initial enumeration, initiator = human), and **create an empty delegation-log.md (with header) at the same time** — the log file must exist from init on, never back-filled afterwards.
4. Until the whitelist is finalized, everything runs as "ask the human for everything".

### 2. Daily execution (on hitting a decision point)

1. Determine which decision class the point belongs to:
   - **In the whitelist and active** → execute autonomously, and immediately write delegation-log.md (decision class, decision, grounds, reversibility).
   - **Touches a forbidden zone** → never autonomous; route to the human per the project's existing process.
   - **Neither** → ask the human as usual; if the class recurs, you may "propose escalation": propose a new decision class to the human (with: class name, scope, revocation conditions, occurrence count so far); once the human approves, it goes through list change.
2. Before any decision in a session, first confirm delegation.md exists and `enabled: true`; a missing file or a closed switch = ask the human for everything.

### 3. Revocation

- **Per entry**: a decision class's revocation trigger hits (e.g. "the naming caused ambiguity once") → that class's state becomes `suspended`, record in the Changelog, write the log, inform the human explicitly; restoration requires explicit human action.
- **Wholesale**: the human sets `enabled` to `false` (or verbally announces revocation) → immediately ask the human for everything; record in the Changelog.

### 4. Review (task end / retro)

- **Log existence check (mandatory)**: first confirm delegation-log.md exists. A missing file = a process gap (logging went unexecuted); it must be explicitly flagged in the review report and the file re-created (recoverable entries back-filled, marked "restored after the fact"); never continue silently.
- Summarize this period's delegation-log.md: total entries, distribution across decision classes, escalation-to-human count, misjudgment / revocation events. **Zero entries** must be explicitly explained as "no AI autonomous decisions this period" (zero entries is itself a fact that must be explained, not a default success).
- After the human's review, decide: keep, adjust the list (via change), or revoke.
- Dogfood pilot projects: bring the summary data (escalation-to-human rate, post-hoc veto / rollback rate, misjudgment count, subjective fatigue before/after) back to the host project's "decision delegation" OD entry.

### 5. preview-grade stage documents (migrated to design-questionnaire)

preview has been migrated into design-questionnaire as a **mandatory stage step** (now an independent W00 wave; the single-source spec is design-Q's QUESTIONNAIRE-FORMAT.md); delegate no longer maintains its own preview flow. Non-design-Q scenarios needing a preview should follow the design-Q spec manually. Migration reasons and process: see the CHANGELOG.

## List-change governance

- Adding / adjusting / deleting a decision class = an explicit revision of delegation.md: human-initiated, recorded in the Changelog (date, change, initiator, reason).
- AI proposals only go to "propose escalation"; they never touch the file directly.
- Creeping-erosion defense: every "but this one's simple too" must go through the same change flow, no exceptions.

## Full-authority mode (mode: full)

Produced by the grill-Q stress test (OD-13): a loose mode for the "AI full autonomy" dual-track comparison (shadow / champion-challenger).

- **Switch**: delegation.md frontmatter `mode: full` (`strict` is the default); switching is human-initiated only, recorded in the Changelog.
- **Semantics**: with `mode: full` on, whitelist semantics invert into an **exclusion set** — "anything not in the forbidden zones (the never-delegate list) is executable by default"; under `strict` the original whitelist semantics hold.
- **The floor is unchanged**: the forbidden-zone list, **release / payment / external publication / data deletion — four classes never auto-executed**, and judgment rights (product / engineering / security / merge) never delegated — all three remain in force under `full`.
- **Traceability is unchanged**: every autonomous decision still goes to delegation-log.md (append-only).
- **Hands-on-test clause (new discipline)**: "The AI may autonomously run hands-on tests first (read-only: tools / scripts / bash commands); the post-test decision classification still goes to the human, or into the `full`-mode exclusion set" — resolves the tension between "the AI tests first, then classifies" and "the AI has no self-classification right". Autonomous hands-on testing is **read-only only**; write operations stay within the whitelist / exclusion-set framework.
- **Revocation first**: applies under `full` as well — the moment a revocation condition hits, stop; no arguing.

## Relation to family skills

- Orthogonal to design-questionnaire / grill-questionnaire: they govern "how the human makes batch decisions"; delegate governs "which execution-layer decisions stop being asked of the human".
- The questionnaire engine's 🤔 escape hatch (de-risking protocol) is a one-off, temporary transfer of a single decision; delegate is the standing delegation of enumerated decision classes; the two do not substitute for each other.
