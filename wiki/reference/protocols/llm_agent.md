---
identity:
  node_id: "doc:wiki/reference/protocols/llm_agent.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/00_house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

This protocol summarizes the expectations for LLM agents operating inside Wikipu. It is a lookup-oriented companion to the house rules and librarian protocol, not a replacement for them.

## Rule Schema

- Navigate graph-first: use the knowledge graph and focused context before broad Markdown wandering.
- Treat `wiki/` as current truth and `raw/` as read-only seed material.
- Do not create new modules or topology changes without the proposal and orthogonality workflow.
- Use canonical standards and how-to pages instead of relying on stale root-level notes.
- Preserve reversibility and update durable documentation when significant behavior changes.

## Fields

- `Graph-first` means start with `wiki-compiler build`, `query`, or `context` when the question is structural.
- `Current truth` means docs in `wiki/` should match code reality or be explicitly marked otherwise.
- `Proposal workflow` means `TopologyProposal` plus validation before new topology is introduced.

## Usage Examples

- Before implementing a new module, inspect the graph and standards, then run the proposal flow.
- When a rule and a workflow doc disagree, treat the standards doc as canonical and update the workflow doc.
