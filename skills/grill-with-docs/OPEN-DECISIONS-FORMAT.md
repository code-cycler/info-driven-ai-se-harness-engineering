# OPEN-DECISIONS.md Format

A living list of decisions that were **deferred or made provisionally** during a grilling session — because the user couldn't settle them confidently (knowledge gap, experience gap, or can't-anticipate-the-future) and the choice was **de-risked** instead of forced. These are *open*: they still need a real answer someday.

This file is the alarm clock that makes deferring safe instead of negligent. Without it, "we'll decide later" silently becomes "we never decided, and now it's baked in."

## Structure

```md
# Open Decisions

Decisions deferred during grilling because they couldn't be settled confidently yet. Each has a reversible placeholder and a trigger that should bring us back to settle it for real.

---

## {Topic} — {the question, phrased sharply}

**Status:** deferred | provisional
**Why deferred:** knowledge gap | experience gap | can't anticipate
**Current placeholder:** {the most-reversible option picked for now, and what it lets us do today}
**Reversibility:** {how costly to undo — minutes / hours / a sprint / a quarter}
**Trigger — revisit when:** {the concrete signal or information that means we should come back and settle this for real}

---

## {Next topic} — ...
```

## Rules

- **One question per entry.** If a deferral bundles several questions, split them into separate entries.
- **The placeholder must be reversible.** If you couldn't find a reversible option, the decision wasn't actually deferrable — promote it to a provisional ADR with a stated risk instead, and mark `Status: provisional`.
- **The trigger is mandatory.** A deferred decision without a revisit trigger is just a forgotten decision. Make the trigger *concrete*: "when we add a second region", "when monthly volume exceeds 1M", "when a customer asks for partial refunds", "when we hire a security engineer" — not "eventually" or "when we have time".
- **State *why* it's deferred.** This tells future-you what kind of help is needed to resolve it: *learn the domain* (knowledge gap), *gain operational experience* (experience gap), or *wait for the situation to arise* (can't anticipate).
- **Resolve and remove.** When an entry is settled, delete it from this file. If the resolution qualifies as an ADR (hard to reverse + surprising + real trade-off — see [ADR-FORMAT.md](./ADR-FORMAT.md)), record it there. This list should contain *only* genuinely open items.
- **Keep it a flat list, newest at the bottom.** No nesting — this is a queue, not a spec or a scratch pad.

## Where it lives

`docs/OPEN-DECISIONS.md`:

- **Single context (most repos):** one file at `docs/OPEN-DECISIONS.md` at the repo root.
- **Multiple contexts:** alongside each context's own `CONTEXT.md` (e.g. `src/ordering/docs/OPEN-DECISIONS.md`), following the `CONTEXT-MAP.md`.

Created lazily — only when the first decision is deferred via the de-risk protocol.

## How it relates to the other docs

| Doc | Holds | Settled? |
|-----|-------|----------|
| `CONTEXT.md` | the glossary — what terms *mean* | n/a (definitions) |
| `harness/adr/` | decisions that are *made* and worth remembering | yes — closed |
| `docs/OPEN-DECISIONS.md` | decisions that are *not yet made* | **no — open** |

A row migrates from `OPEN-DECISIONS.md` to `harness/adr/` when it's finally settled. `CONTEXT.md` is orthogonal: it never holds decisions, only language.
