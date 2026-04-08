---
identity:
  node_id: "doc:wiki/drafts/1_implementation_sequence.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md", relation_type: "documents"}
---

Build in this order. Each step produces something verifiable before the next begins.

## Details

Build in this order. Each step produces something verifiable before the next begins.

1. **Define contracts** (`contracts.py`) — input models, LLM output model, review model, persistence model. Nothing else exists yet.
2. **Build storage** (`storage.py`) — artifact paths, round management, JSON I/O. Test in isolation with toy data.
3. **Build prompt** (`prompt.py`) — template, serialization, variable construction. Verify the rendered prompt manually before wiring to the model.
4. **Build graph** (`graph.py`) — state, nodes, edges. Wire to a demo chain first so the graph topology can be validated without model credentials.
5. **Add CLI** (`main.py`) — run/resume flow. Test with the demo chain before adding real model credentials.
6. **Expose to Studio** — add `create_studio_graph()` and `langgraph.json` entry. Verify topology in Studio before live runs.
7. **Validate with real model** — add credentials, run end-to-end, inspect artifacts.
8. **Harden** — expand tests, handle edge cases discovered during real usage.

The key invariant: the graph must be exercisable at every step, even before credentials exist. The demo chain enables this.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md`.