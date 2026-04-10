# Trail Collect

## Core Idea

Every agent conversation produces artifacts that currently evaporate: design decisions resolved, gap discoveries, corrections to wrong assumptions, Q&A that clarified ambiguity, things the agent got wrong and had to fix. These are precisely the high-value signals — they represent friction that was encountered and resolved. Without a collection step, every session's insights are lost, and the same questions recur in future sessions.

Trail collect is the mechanism that operationalizes Phase 6 (meta-review). It is a structured post-session extraction step that distills durable facts from conversation artifacts and routes them to the right place in the system.

---

## What Gets Collected

Not everything is worth keeping. Trail collect is not a transcript archive — it is a distillation. The artifacts worth preserving:

| Artifact Type | Destination |
|---|---|
| Design decision resolved | Encode in the relevant doc, issue, or hausordnung |
| Gap discovered | Create an issue in `desk/issues/` |
| Ambiguity resolved (Q&A) | Encode inline in the relevant doc or `desk/socratic/` resolution |
| Correction (agent was wrong) | Update the source of the wrong assumption |
| Rule that caused friction | Rewrite the rule in the hausordnung |
| New concept identified | Write to `raw/` as a seed |

Raw session logs stay in the assistant's memory system. Trail collect extracts only the durable facts — the delta between "what the system knew before the session" and "what it knows now."

---

## The Collection Step

At natural breakpoints or session end:

1. **Scan** the session for the artifact types above.
2. **Classify** each artifact: decision / gap / correction / new concept / rule patch.
3. **Route** each classified artifact to its destination (doc update, new issue, raw seed, hausordnung patch).
4. **Record** a one-line entry in the changelog: what was collected and where it went.

This step should be lightweight. If it takes more than a few minutes, it is doing too much — the valuable artifacts should be obvious.

---

## Relation to Phase 6 (Meta-Review)

Phase 6 from the methodology synthesis:

> "At the end of every development session, the human operator reviews what the agent did, identifies friction — hallucinations, stuck states, routing failures, ambiguous rules — and immediately patches the meta-documentation that caused the friction."

Trail collect is the agent-side complement. Phase 6 is the human reviewing what the agent did. Trail collect is the agent extracting what it learned and encoding it before the session closes. Together they close the loop: nothing the session discovered should be lost.

---

## What Trail Collect Is Not

It is not a memory dump. It is not a session summary. It is not a log of everything that happened. It is a targeted extraction of the facts that should change the system's behavior in future sessions — the minimal set of updates that makes the next session better than this one.

---

## Failure Mode Without Trail Collect

The same design question gets asked in three different sessions. Each time, the answer is derived from scratch. Each time, a slightly different answer emerges. The system accumulates inconsistencies that no one can trace because the context that produced each answer is gone.

Trail collect prevents this by making session discoveries first-class citizens of the system's knowledge base.
