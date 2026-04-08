---
identity:
  node_id: "doc:wiki/drafts/2_why_the_demo_chain_exists.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md", relation_type: "documents"}
---

The demo chain is not a mock — it is a structural enabler.

## Details

The demo chain is not a mock — it is a structural enabler.

Without it:
- Studio cannot render the graph if the model node raises on missing credentials
- Development and debugging require live API calls
- Tests that cover graph topology need real credentials

With it:
- Studio always loads and shows the full topology
- Graph lifecycle (pause → resume → route) can be validated without a model
- Tests use the demo chain by default; integration tests opt into the real chain

The demo chain must produce output that passes schema validation. A chain that returns garbage is not useful. Make it deterministic and structurally correct.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md`.