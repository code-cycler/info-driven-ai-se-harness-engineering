---
name: long-running-agent
description: "Constraint system for long-running, multi-session complex projects. Incremental work, the feature_list.json feature list, claude-progress.txt progress records, end-to-end test verification (a feature is marked passes:true only after passing tests), clean Git state, conventional commits. Single agent working one feature at a time by default; extension capability: preparation mode (planning parallel threads + task packages, human review and confirmation) and execution mode (multi-worktree parallelism, preferring Claude Code's native multi-agent inter-communication: the main session spawns background agents each resident in a worktree + SendMessage communication). Triggers: multi-session / long-horizon projects, feature_list tracking needed, long engineering tasks, work spanning context windows, design-questionnaire layered-design (LN) close stop-point handing off into the implementation phase, preparation mode, execution mode, multi-worktree parallelism. Use when a project enters long-running implementation spanning multiple sessions / context windows, or after design-questionnaire hands off (single or multi-worktree modes)."
lang: en
en-source: skills/long-running-agent/SKILL.md
zh-hash: ab01c35af597
---

[中文](../../../skills/long-running-agent/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

# long-running-agent (long-running agent constraint system)

> Based on Anthropic's official article "Effective harnesses for long-running-agents"
> **Original link**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
>
> This skill is a **general-purpose development tool**, not bound to any specific project. Terminology uses the Claude Code context: "compressing context" in this file refers to Claude Code's `/compact`, not to any product-level Compression concept.

## 1. What problem it solves

Across complex tasks spanning multiple context windows, AI agents tend to:

1. **Do too much at once** → piles of half-finished work
2. **Declare completion prematurely** → treating a partially finished feature as project completion
3. **Mark done without testing** → features marked `passes:true` without running end-to-end tests
4. **Amnesia between sessions** → a new session has no memory of the previous one (this skill fights amnesia with **files on disk**, not session context)

### Core ideas

- **Incremental work**: one feature at a time
- **Clear artifacts**: leave clear progress records for the next session (written into files, not context)
- **Clean state**: code is always in a mergeable-to-main state
- **End-to-end verification**: a feature is marked complete only after passing full tests

## 2. Project files

A long-running project should contain these core files:

```
project/
├── .claude/
│   ├── feature_list.json      # feature requirements list
│   └── claude-progress.txt    # progress record file
├── src/                       # source code
├── tests/                     # test files
└── .git/                      # Git repository
```

| file | purpose |
|------|------|
| `feature_list.json` | all feature requirements and their status; created in the first session, statuses updated in later sessions |
| `claude-progress.txt` | per-session work records; updated at session end |

> **Initialization scripts are no longer used** (init.sh / init.bat). Environment startup is handled by the project's existing toolchain (README / Makefile / package.json / build scripts etc.); this skill creates no startup scripts.

## 3. Feature-list spec (feature_list.json)

### JSON format

```json
{
  "project_name": "project name",
  "created_at": "2026-03-03T10:00:00Z",
  "features": [
    {
      "id": "F001",
      "category": "functional",
      "priority": "high",
      "description": "feature description",
      "steps": ["test step 1", "test step 2", "test step 3"],
      "passes": false,
      "last_tested": null,
      "notes": ""
    }
  ]
}
```

### Field descriptions

| field | type | description |
|------|------|------|
| `id` | string | unique feature identifier (e.g. F001) |
| `category` | string | category: `functional` / `ui` / `api` / `performance` / `security` |
| `priority` | string | priority: `high` / `medium` / `low` |
| `description` | string | a clear description of the feature |
| `steps` | array | test steps verifying this feature |
| `passes` | boolean | whether the feature passed end-to-end tests |
| `last_tested` | string | last test time (ISO 8601) |
| `notes` | string | notes or known issues |

> If the project was designed via design-questionnaire, `features` is reverse-derived preferentially from the LLD's **phase split** and DoD, not enumerated from thin air — see §5.3.

## 4. Progress-file spec (claude-progress.txt)

### Format

```
================================================================================
SESSION: <session number>
Time: <ISO 8601 timestamp>
================================================================================

## Completed tasks
- <task description>

## Modified files
- <file path>: <brief note>

## Git commits
- <commit hash>: <commit message>

## Problems encountered
- <problem description and solution>

## Next-step plan
- <next feature ID to handle>

================================================================================
```

New sessions are written at the **top** of the file (newest on top); historical sessions stack downward.

## 5. Session-start check (single flow)

> No longer distinguishes an "initialization agent" from a "coding agent". The first session and later sessions share one startup checklist; the only difference is whether feature_list.json already exists.

### 5.1 Startup checklist

```
1. Confirm the working directory
   [ ] pwd to confirm the working directory; edit files only inside it

2. Rebuild context (from files on disk, not session context)
   [ ] Read claude-progress.txt for recent work
   [ ] git log --oneline -10 for recent commits
   [ ] Read feature_list.json for feature status
   [ ] (If present) read design-Q's VISION / HLD / LLD and archived questionnaires

3. Verify the base environment
   [ ] Start the environment with the project's existing toolchain (README / Makefile / build scripts)
   [ ] Run basic tests to confirm the environment is healthy; fix problems first

4. Pick the next feature
   [ ] From feature_list.json, pick the highest-priority unfinished (passes:false) feature
   [ ] One feature at a time

5. Implement the feature
   [ ] Write code
   [ ] Write tests
   [ ] Run end-to-end tests

6. Update status
   [ ] Set passes:true only after all tests pass
   [ ] Update claude-progress.txt (at the top)
   [ ] Git commit (following the project's existing commit conventions)

7. Session-end check
   [ ] Code in a clean state
   [ ] All tests passing
   [ ] Progress file updated
```

### 5.2 First-session extra steps

When feature_list.json does not exist, create it first:

```
[ ] Analyze requirements, extract all feature points
[ ] Write feature_list.json with all features passes:false, each with detailed test steps
[ ] Create claude-progress.txt recording initial setup complete
[ ] git init (if not initialized) + initial commit
```

### 5.3 Rebuild context from files on disk (the key mechanism)

**Session context may be compacted (Claude Code `/compact`) and lose design-phase decision detail**. This skill does not rebuild project understanding from session context, but from files on disk:

- **With design-Q products (LN naming)**: read the layer files (`L0-vision-*` always + all layers) + `harness/questionnaires/archive/` archived questionnaires. **Feature reverse-derivation rule**: from the **lowest build-semantics layer**'s phase split (L2-build or a self-declared build/phase-content layer); with no build layer (single-layer delivery) → reverse-derive item-by-item from the L0 acceptance criteria (the L0 writing constraint "acceptance written as independently verifiable items" exists for this). The legacy trio VISION/HLD/LLD = aliases of L0/L1/L2, same rule. **Harness file layering: see HARNESS-RULES.md** (doctor-harness is the normative authority; not inlined here).
- **Without design-Q products**: read claude-progress.txt + feature_list.json + git log; rebuild from historical sessions and the code's current state.

The mechanism is self-consistent: whether or not context is compacted, the files on disk are the source of truth.

### 5.4 Handoff with design-questionnaire

design-Q, after its final-layer close and the grill-questionnaire stress test, triggers this skill (into the implementation phase) via the **multi-threaded stop-point inquiry**. The stop point has two branches:

- Single-threaded branch → straight into implementation (this file's default path); multi-threaded branch → enter **preparation mode** (see §5.5).
- The layer files (LN) design-Q produced are the feature_list's source of truth.
- The user may refuse the handoff and manually invoke this skill anytime later (see §7 trigger contract).
- Manual invocation is immune to context compaction — rebuilt from files on disk (§5.3).

### 5.5 Preparation mode and execution mode (multi-thread extension capability)

> Positioning: **default = single agent** (this skill's main path, one feature at a time); multi-worktree multi-agent = an **extension capability**, optionally enabled; the implementation prefers **Claude Code's native multi-agent inter-communication** — the main session acts as coordinator (spawns background agents each resident in a worktree; SendMessage dispatches task packages and inter-thread communication; task-notification receives completion signals); the human opening multiple independent sessions is a legal fallback. **Mode switches are confirmed by the human; the AI never starts on its own.**

**Preparation mode** (touches no code): rebuild the feature_list from the layer files → plan parallel threads (one feature branch + task package per worktree) → **stop; the human reviews and confirms which threads start**. Task-package schema (five fields per package): thread name/branch, scope (L0 acceptance anchors), DoD, dependencies and boundaries vs. other threads, forbidden-overreach items.

**Execution mode** (multi-worktree): after the human confirms, the main session spawns background agents each resident in a worktree to implement per task packages; the main session only aggregates progress and manages **merge order**. **Three lines of defense against code-level merge conflicts**: ① preparation-mode task packages cut threads along module boundaries wherever possible (reducing same-file crossings at the source); ② merge order is serialized along the dependency chain (upstream threads merge first); ③ a true conflict (git merge conflict) stops that thread until the human rules — no preset file ownership, no zero-conflict promise.

**Thread-failure rollback**: rolling back one worktree does not affect other threads; its task package is marked "failed / rolled back" into the processing report, and the corresponding feature_list item goes back to false.

## 6. Incremental-work principles

### One feature at a time (qualified form, provisional)

**Within a single-worktree session**, one feature at a time; multi-worktree parallelism exists only inside execution mode + human-confirmed task-package boundaries (§5.5). **Must be strictly obeyed**:

```
[OK] correct
1. Pick one feature → implement fully → write and run tests → on pass, update status → commit → next

[X] wrong
1. Starting multiple features at once
2. Leaving multiple half-finished products
3. Marking done without testing
```

### Clean code state

At each session's end, the code should be:

- Free of major bugs, existing features working
- Orderly, understandable code
- All tests passing
- Mergeable to the main branch

### Git commit conventions

**Follow the project's existing conventions first** (the project's AGENTS.md / CLAUDE.md / contributing guide). If the project has none, default to conventional commits:

```
<type>(<scope>): <description>
```

type: `feat` / `fix` / `refactor` / `test` / `docs` / `chore`.

Examples: `feat(student): add ID validation` / `fix(course): fix student-count error`.

> This skill does not rewrite the project's commit rules — project-level conventions take precedence; the skill only supplies a default in their absence.

## 7. Trigger contract

- design-Q's LLD close, after grill-Q, gets **one proposal**, refusable.
- If grill-Q is refused, propose immediately after; if grill-Q is accepted, propose after the stress test completes.
- After refusal, no more automatic proposals during implementation; the user can manually invoke anytime (`/skill` or natural language "start long-running-agent").
- Manual invocation is immune to context compaction — rebuilt from files on disk (§5.3).

## 8. Testing and verification requirements

### End-to-end principle

**Core principle**: only after passing end-to-end tests may a feature be marked `passes: true`.

```
1. Implement the feature code
2. Write test cases
3. Run unit + integration tests
4. Manual verification (where applicable)
5. All pass → passes:true
6. Any failure → keep passes:false and keep fixing
```

### Feature-marking rules

```json
// [OK] all tests passed
{ "passes": true, "last_tested": "2026-03-03T15:00:00+08:00", "notes": "all tests passed" }

// [X] marking true without testing — forbidden
{ "passes": true, "last_tested": null }

// [OK] tests failed, stays false
{ "passes": false, "last_tested": "2026-03-03T15:30:00+08:00", "notes": "case 3 fails; fix the boundary condition" }
```

### Forbidden behaviors

| forbidden | why |
|------|------|
| Deleting or modifying test steps | may cause missing features or bugs |
| Marking passes:true without testing | produces unreliable feature status |
| Skipping failing tests | hides latent problems |
| Deleting feature items to reduce workload | features are lost forever |
| Handling multiple features at once within a single-worktree session (multi-worktree parallelism must be inside execution mode + human-confirmed task-package boundaries, §5.5) | easily produces half-finished code |

## 9. Failure modes and recovery

### Problem → countermeasure

| problem | countermeasure |
|------|------|
| Prematurely declaring the project done | at session start read feature_list and continue an unfinished feature |
| Leaving buggy or unrecorded code | at session start read progress + git log + run basic tests; at session end commit to Git and update progress |
| Marking a feature complete prematurely | feature_list defines detailed test steps; passes:true only after end-to-end pass |
| Trying to do too much at once | one feature at a time; move on only after completing it |

### Recovery strategy

When the code is in a bad state:

```
1. Identify the problem
   [ ] Run tests to confirm which features fail
   [ ] git log to find the last stable version
   [ ] Read progress for recent changes

2. Restore a stable state
   [ ] git revert the problematic commits
   [ ] Or git reset --hard <commit> back to a stable version (use with care)
   [ ] Re-run tests to confirm recovery

3. Start over
   [ ] Update progress to record the recovery
   [ ] Re-pick a feature, this time in smaller, safer steps
```

## 10. Quick reference

### Session-start checklist

```
[ ] 1. pwd to confirm the working directory
[ ] 2. Read claude-progress.txt (recent work)
[ ] 3. Read feature_list.json (feature status)
[ ] 4. (If present) read VISION/HLD/LLD (design-Q products)
[ ] 5. git log --oneline -10 (recent commits)
[ ] 6. Start the environment with the project's existing toolchain + basic tests
[ ] 7. Pick the next feature
```

### Session-end checklist

```
[ ] 1. All tests passing
[ ] 2. Clean code state
[ ] 3. Update feature_list.json (if any feature completed)
[ ] 4. Update claude-progress.txt (at the top)
[ ] 5. Git commit (the project's existing conventions)
[ ] 6. Report to the user
```

### Mandatory enforcement

**These are the core rules of long-running projects and must be strictly obeyed:**

- Never skip the session-startup flow
- Never handle multiple features at once within a single-worktree session (multi-worktree parallelism = execution mode + human-confirmed task-package boundaries, provisional: re-check the wording on the multi-worktree setup's first real use)
- Never mark done without testing
- Never leave the code in an unclean state
- Always leave clear artifacts for the next session
