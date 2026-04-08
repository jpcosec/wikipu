---
identity:
  node_id: "doc:wiki/drafts/2_node_taxonomy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

Every node in a LangGraph module fits one of these types. Name them accordingly:

## Details

Every node in a LangGraph module fits one of these types. Name them accordingly:

| Type | Responsibility | Rules |
|---|---|---|
| **Input validation** (`load_*`) | Validate and normalize state inputs, merge prior artifacts | Fail fast — raise if required inputs are missing |
| **LLM boundary** (`run_*_llm`) | Build prompt variables, invoke chain, validate output | Only place that calls the model. No disk I/O. |
| **Persistence** (`persist_*`) | Write artifacts, compute hashes, return refs into state | No business logic. Delegate entirely to `storage.py`. |
| **Breakpoint anchor** (`*_review_node`) | Pause the graph for human input | Intentionally thin — exists only as an interrupt target |
| **Review/routing** (`apply_*`) | Validate review payload, hash-check, route via `Command` | Hash validation mandatory. Safe-return if payload absent. |
| **Context prep** (`prepare_*`) | Merge patch evidence, compute regeneration scope, clear stale inputs | Must confirm routing condition before executing |

For this repository's LangGraph runtime, graph nodes are expected to be synchronous by default.

Rules:
- Prefer `def node(state) -> dict` over `async def` for graph nodes.
- Keep blocking file I/O, persistence, rendering, and other deterministic work in sync helpers instead of mixing sync operations into async nodes.
- Only introduce async nodes when the node's core work is truly async end-to-end and cannot reasonably be handled behind a sync boundary.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.