---
identity:
  node_id: "doc:wiki/how_to/use_socratic_methodology.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

The Socratic method in Wikipu is the pre-design gap finder — the structured interrogation of a plan or proposal before implementation begins. It produces typed questions that expose hidden assumptions, missing constraints, and contradictions with existing nodes, which must be resolved before a plan moves to execution.

# How to Use the Socratic Methodology

The Socratic method in Wikipu is the pre-design gap finder — the structured interrogation of a plan or proposal before implementation begins. It does not produce answers; it produces typed questions that expose hidden assumptions, missing constraints, contradictions with existing nodes, and undefined edge cases. These questions must be resolved before a plan moves to `desk/tasks/` for execution. Without this step, plans that feel complete often contain contradictions or ownership gaps that only surface as failures mid-implementation.

## Prerequisites

- A plan file, a node draft, or a proposed design to interrogate — the input to the Socratic process.
- Access to the knowledge graph (`knowledge_graph.json` current) to detect contradictions against existing nodes.
- A `desk/socratic/Board.md` to track open questions as board items.
- Understanding of the six question types: missing constraint, unstated assumption, contradiction, undefined edge case, scope creep signal, ownership gap (see `raw/socratic_protocol.md`).

## Steps

1. Identify the input artifact: the plan, proposal, or node design to be interrogated.
2. Read the artifact and generate questions by type for each claim or section. For each question, record: the question type, the specific claim or section that prompted it, and what resolution would look like.
3. Create a structured Q&A artifact in `desk/socratic/` with one board item per open question.
4. Add each question to `desk/socratic/Board.md`. Each item is unresolved until a human or authorized agent provides an explicit answer.
5. For each question: if it reveals a **missing constraint**, encode the answer in the relevant wiki node or `house_rules.md`. If it reveals a **contradiction**, revise the plan or the conflicting node before proceeding. If it reveals **scope creep**, split the plan at the boundary.
6. When a question is answered, record the resolution inline in the board item, apply the encoding (doc update, rule update, or new issue), and delete the item from the board.
7. Once all questions for the artifact are resolved, delete the `desk/socratic/` artifact and promote the plan to `desk/tasks/` for implementation.

## Verification

- [ ] Every open question is a board item in `desk/socratic/Board.md` with an explicit type label.
- [ ] No plan file moves to `desk/tasks/` while it has unresolved Socratic questions.
- [ ] Every resolved question has its answer encoded — either in a wiki node, a rule update, or a new issue — before the board item is deleted.
- [ ] The `desk/socratic/` artifact is deleted after all its questions are resolved; history is preserved only in git and the changelog.
- [ ] Contradictions discovered during interrogation are reflected as revisions to the plan or the conflicting node, not left as comments.
