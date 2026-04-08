---
identity:
  node_id: "doc:wiki/drafts/7_how_to_extend_the_codebase_safely.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md", relation_type: "documents"}
---

When adding a new step/node:

## Details

When adding a new step/node:

1. Create a node package under `src/nodes/<node_name>/` with:
   - `contract.py` (schemas/contracts)
   - `logic.py` (node behavior)
   - prompt files if LLM-driven
2. Keep deterministic parsing/validation fail-closed (no silent success fallbacks).
3. Add or update tests under `tests/nodes/<node_name>/`.
4. Wire the node into graph topology in `src/graph.py`:
   - register handler in node registry
   - add linear edge(s)
   - add review transitions if it is a review gate
5. Keep resume semantics stable:
   - same `thread_id` convention
   - decisions parsed from artifacts, not injected ad hoc
6. Update docs to reflect runtime truth:
   - `docs/runtime/graph_flow.md`
   - `docs/operations/tool_interaction_and_known_issues.md`
   - `README.md` if user-facing behavior changed

Generated from `raw/docs_postulador_langgraph/docs/operations/agent_entrypoint.md`.