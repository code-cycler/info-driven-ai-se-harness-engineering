---
name: retro-questionnaire
description: Batch-questionnaire retrospective for projects / stages. Generates a Markdown retrospective questionnaire per the methodology's four sections (what went well / problems and cause hypotheses / architecture deviations / lessons learned) + Action Items; after the user answers offline, results land in the host project's docs/retro/<topic>_vN.md and TODO.md, and used questionnaires are archived. Proactively proposed after a stage's DoD verification; can also be manually triggered anytime (record promptly, like memory). Triggers: stage retrospective, project retrospective, "retro this", "do a retro", retro, DoD verification passed. Use when a development stage or project is done and a structured retrospective questionnaire should be generated, answered, and sedimented.
lang: en
en-source: skills/retro-questionnaire/SKILL.md
zh-hash: e4d461ed280c
---

[中文](../../../skills/retro-questionnaire/SKILL.md) · **English**

> **Translation notice** — This is a translation of the Chinese original. The Chinese text is canonical; in case of conflict, the Chinese version governs ([ADR-0025](../../../harness/adr/0025-english-mirror-drift-governance-integration.md)). Terms follow the English Glossary in [CONTEXT](../../docs/CONTEXT.md).

> Governance history: see this skill directory's CHANGELOG.md in the project repository (project side only); intentional forks: see FORK-NOTES.md in this directory (no such file = no rule-body-level fork).

<what-to-do>

Turn retrospectives from "relying on self-discipline" into "triggered, structured, sedimented": five-source reading → generate the retro questionnaire → user answers → land the retro document and TODO.md → archive. The questionnaire engine is the copy in this directory (copied from design-questionnaire; forks are declared in FORK-NOTES.md).

**The acting target is the host project** (the project being retroed): question grounds are read from the host project; the retro document, TODO.md, and questionnaire archive all land in the host project, never in this skill's directory.

## Iron rules

1. **A retrospective records only, never decides** — architecture deviations are only recorded in the retro document; follow-up actions (updating design documents / new ADRs) are initiated by the human.
2. **AI never decides for the human** — reflection-question options are a "list of common cause hypotheses"; the real cause is whatever the user's ✍️ custom answer says.
3. **Sediment immediately** — retro document, TODO.md, archive: written the moment processing completes.
4. **No raw information is lost** — the questionnaire file is the single source of truth; verbal quick-answers are transcribed verbatim into it; used questionnaires are archived only, never deleted.
5. All engine iron rules are inherited (see PROCESSING-RULES.md and QUESTIONNAIRE-FORMAT.md).

## Triggering

- **Proactive proposal**: on detecting that a stage of the host project passed its DoD verification → propose a retrospective with AskUserQuestion; execute after the human confirms.
- **Manual**: the user says "retro this" / "do a retro" etc. — triggered anytime, recorded promptly (like memory).

## Main flow

1. **Five-source reading** (interface contract, no deviation allowed):
   1. The stage's design documents (HLD / LLD / DoD)
   2. `git log` (this stage's commits) — **non-git projects**: skip this source and note in the retro document's "five-source reading" section "this project is not a git repository; the git-log source was skipped"; never fabricate, never fill in from memory
   3. `TODO.md` unfinished items
   4. The previous retro's Action Items (→ an "Action Items review" section opens the new retro document)
   5. Valuable content from exchanges with the user (feedback, decisions, insights)
- **Research-and-verify prelude (standard flow)**: before generating the retrospective questionnaire, complete the "survey the current state → don't assume / verify → gather more information → save promptly" loop —
  1. **Survey the current state**: beyond the five-source reading (above), read the project's current state (progress / feature_list / recent commits), never from memory;
  2. **Don't assume / verify**: factual claims in the retrospective questionnaire (e.g. "X is done", "some step went smoothly") must be verified (git log / documents / code) rather than taken from memory;
  3. **Gather more information**: extra facts found while reading (unrecorded problems, deviations, leftovers) go into the questionnaire's question grounds as well;
  4. **Save information promptly**: evidence and findings are written into the questionnaire / retro document immediately, not batched until processing time.

2. **Generate the retro questionnaire**: pose questions per [RETRO-SKELETONS.md](../../../skills/retro-questionnaire/RETRO-SKELETONS.md), format per [QUESTIONNAIRE-FORMAT.md](../../../skills/retro-questionnaire/QUESTIONNAIRE-FORMAT.md), written to the host project's `harness/questionnaires/retro-<topic>-w<NN>.md`. When this wave has ≤ 3 questions, generate no file; ask directly with AskUserQuestion (small-wave threshold). **Harness file layering: see HARNESS-RULES.md** (doctor-harness is the normative authority; not inlined here).
3. **User answers**: file editing as the primary path; verbal quick-answers are transcribed verbatim into the questionnaire file. Do not parse until the user announces "done answering".
4. **Process and land** (per [PROCESSING-RULES.md](../../../skills/retro-questionnaire/PROCESSING-RULES.md)):
   - Retro document: host project `docs/retro/<topic>_vN.md` (_vN increments; final/new/copy forbidden), structure = four sections + Action Items
   - Action items → host project `TODO.md` (problem → action → verification timing)
   - Processing report (in conversation)
   - Questionnaire archived to `harness/questionnaires/archive/`, with the processing-report summary appended at the tail
5. **Termination**: one retro usually completes in a single wave; for new questions raised by the answers, judge "no more information to interrogate" to decide whether a supplementary wave is needed.

</what-to-do>

<supporting-info>

- Retro skeleton template (four sections + Action Items): [RETRO-SKELETONS.md](../../../skills/retro-questionnaire/RETRO-SKELETONS.md)
- Engine copies (drift must be declared): [QUESTIONNAIRE-FORMAT.md](../../../skills/retro-questionnaire/QUESTIONNAIRE-FORMAT.md), [PROCESSING-RULES.md](../../../skills/retro-questionnaire/PROCESSING-RULES.md)
- This skill's design documents (project side only): the project repository's skills/retro-questionnaire/docs/ (VISION / hld_v1), decision index DESIGN.md

</supporting-info>
