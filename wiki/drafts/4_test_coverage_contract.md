---
identity:
  node_id: "doc:wiki/drafts/4_test_coverage_contract.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md", relation_type: "documents"}
---

Minimum automated test coverage for any LangGraph module:

## Details

Minimum automated test coverage for any LangGraph module:

- **Approve flow**: graph runs, persists, pauses, resumes with approval, completes.
- **Regeneration flow**: review requests regeneration, context is prepared, second round runs.
- **Rejection flow**: review rejects, graph ends cleanly.
- **Stale hash rejection**: resume with a hash that doesn't match current proposal is rejected.
- **Bare-Continue safety**: resume with no payload returns to pending state without crashing.

Tests use `InMemorySaver` and injected fake chains — never the real model. CLI tests patch `build_graph` to inject the fake app.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md`.