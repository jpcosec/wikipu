# Socratic Protocol

## Core Idea

The Socratic method is a form of cooperative argumentative dialogue that surfaces hidden assumptions through structured questioning. It does not seek to provide answers — it seeks to find what you did not know you were assuming.

Applied to software design: before a plan is implemented, a Socratic agent (or process) interrogates the plan's assumptions, identifies gaps, contradictions with existing nodes, and undefined edge cases. The output is not a critique — it is a set of open questions that must be resolved before implementation begins.

This is the pre-flight check. Phase 6 (meta-review) is the post-flight debrief. Together they close the friction loop.

---

## Where It Fits

```
raw/          →  [ingest]  →  wiki/
                                 ↓
                         Socratic Protocol    ←— runs here, before any plan is created
                                 ↓
                         desk/socratic/Board.md   (open questions, pending human resolution)
                                 ↓
                         desk/issues/ or proposals/   (resolved → actionable)
```

Socratic runs before `desk/issues/` — it is the step that validates a design before it becomes a plan.

---

## Question Types

A Socratic interrogation of a plan or node produces questions of these types:

| Type | Description |
|---|---|
| **Missing constraint** | What is explicitly not allowed? What are the bounds? |
| **Unstated assumption** | What must be true for this to work that hasn't been written down? |
| **Contradiction** | Does this conflict with an existing node, rule, or decision? |
| **Undefined edge case** | What happens at the boundary? What inputs break this? |
| **Scope creep signal** | Is this one thing or two things masquerading as one? |
| **Ownership gap** | Who is responsible for this? What layer does it belong to? |

---

## The Protocol

1. **Input**: a plan file, a node, or a proposed design.
2. **Interrogation**: generate questions by type, each linked to the specific claim or section that prompted it.
3. **Output**: a structured Q&A artifact stored in `desk/socratic/`. Each question is an item on the Board. It is unresolved until a human (or agent with authority) provides an answer.
4. **Resolution**: when a question is answered, the answer is encoded — either in the relevant doc, in the hausordnung, or as a new issue. The item is deleted from the Board.
5. **Promotion**: once all questions for a given plan are resolved, the plan moves to `desk/issues/` for implementation.

---

## Relation to the Q&A Pattern

The Q&A sessions in this project (e.g., the design inputs for query-server-runtime and cleansing-protocol) are informal instances of this protocol. The Socratic Protocol formalizes that practice: the questions are typed, stored, tracked, and their resolutions are encoded — not lost when the conversation ends.

---

## What It Is Not

Socratic is not code review (that's post-implementation). It is not the cleansing protocol (that's post-build graph analysis). It is not trail collect (that's post-session artifact recovery). It is the pre-design gap finder — the step that transforms vague intentions into plans that can actually be implemented.
