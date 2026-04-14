---
identity:
  node_id: "doc:wiki/standards/llm_agent.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
  - {target_id: "file:AGENTS.md", relation_type: "documents"}
  - {target_id: "file:CLAUDE.md", relation_type: "documents"}
  - {target_id: "file:GEMINI.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

**Abstract:** LLM agents operating inside Wikipu use this protocol for initialization and routing via the unified preamble system.

This protocol summarizes the expectations and initialization routing for LLM agents operating inside Wikipu. It explicitly documents the unified preamble system used to bootstrap new agent sessions.

## Agent Initialization Routing

To ensure all agents receive the exact same invariant rules and guardrails, the repository uses a unified entrypoint strategy:
- **`AGENTS.md`**: The single, authoritative initialization preamble for all AI agents.
- **`CLAUDE.md`**: A symlink routing to `AGENTS.md`.
- **`GEMINI.md`**: A symlink routing to `AGENTS.md`.

This symlink topology guarantees that any updates to the agent preamble apply universally across different LLM platforms without duplication.

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
