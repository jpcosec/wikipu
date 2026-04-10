---
identity:
  node_id: "doc:wiki/how_to/design.md"
  node_type: "how_to"
compliance:
  status: "implemented"
  failing_standards: []
---

Designing a new module or topology change in Wikipu means authoring a `TopologyProposal` before writing any code. The proposal is the formal blueprint that the `wiki-compiler` evaluates for orthogonality against the existing knowledge graph. This process enforces ID-1 (Orthogonality) and ID-6 (Traceable Causality).

# How to Design

Designing a new module or topology change in Wikipu means authoring a `TopologyProposal` before writing any code. The proposal is the formal blueprint that the `wiki-compiler` evaluates for orthogonality against the existing knowledge graph. This process enforces ID-1 (Orthogonality) and ID-6 (Traceable Causality): every new element must prove it does not duplicate existing functionality and must trace to a deliberate, reviewed decision.

## Prerequisites

- Read `wiki/standards/artifacts/proposal.md` to understand the proposal schema: required frontmatter fields (`proposal_id`, `proposal_type`, `requires_human_approval`, `status`, `opened`) and mandatory body sections (Abstract, Changes, Rationale, Risk and Reversal).
- Familiarity with the knowledge graph — run `wiki-compiler build` and review `knowledge_graph.json` to understand what already exists.
- A resolved Socratic session (`desk/socratic/`) if the design involves significant unknowns. Open questions must be answered before a proposal is submitted.

## Steps

1. Query the knowledge graph for existing nodes with overlapping intent: `wiki-compiler query --type find_by_io` or review `wiki/Index.md` to identify the relevant domain entrypoints.
2. Draft a `TopologyProposal` file in `desk/proposals/` using the schema from `wiki/standards/artifacts/proposal.md`. Assign a `proposal_id` in the format `topology-<YYYYMMDD>-<slug>`.
3. Define the module's name, intent, I/O ports (medium, schema_ref, path_template), and any new glossary terms required.
4. Fill in the Changes section as a numbered list of specific, independently reversible actions.
5. Fill in the Rationale and Risk and Reversal sections — document exactly what `git revert` commands would undo the proposal.
6. Set `requires_human_approval: true` if the change crosses the topology boundary (touches external codebases, services, or published artifacts — see ID-5).
7. Submit the proposal. If `wiki-compiler` returns a `CollisionReport`, revise the proposal to eliminate overlaps. You have a maximum of 3 attempts before human escalation is required.
8. Once approved, scaffold the module: `wiki-compiler scaffold --module src/<name> --intent "<intent>"`. This creates `contracts.py`, `__init__.py`, and `README.md`.
9. Define Pydantic input/output models in `contracts.py` with `Field(description=...)` on every field.
10. Implement the module logic, following CS-1 through CS-9 in `wiki/standards/house_rules.md`.
11. Update the module's `README.md` (`KnowledgeNode`) with correct `edges`, `io_ports`, and `compliance.status`.
12. Run `wiki-compiler build` to update `knowledge_graph.json` and `.compliance_baseline.json`.
13. Delete the proposal file from `desk/proposals/` and record the outcome in `changelog.md`. If the design involved a decision, write an ADR in `wiki/adrs/`.

## Verification

- [ ] The proposal file was created with all required frontmatter fields and body sections before any code was written.
- [ ] The collision check returned no colliding nodes, or all collisions were resolved through proposal revision.
- [ ] `wiki-compiler scaffold` was used — the module directory was not created by hand.
- [ ] `contracts.py` contains typed Pydantic models with `Field(description=...)` on every field.
- [ ] The module's `README.md` has correct `edges` linking to dependencies, data sources, and related docs.
- [ ] `wiki-compiler build` completes without compliance errors for the new module.
- [ ] The proposal file is deleted from `desk/proposals/` and `changelog.md` is updated.
