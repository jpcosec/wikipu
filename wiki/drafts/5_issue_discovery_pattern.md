---
identity:
  node_id: "doc:wiki/drafts/5_issue_discovery_pattern.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md", relation_type: "documents"}
---

Real usage against Studio reveals issues that tests miss. The most common class:

## Details

Real usage against Studio reveals issues that tests miss. The most common class:

**Implicit assumptions about resume state.** Tests inject state directly. Studio users click buttons. These produce different state shapes.

When Studio reveals a crash:
1. Reproduce with a targeted test using `InMemorySaver` and the demo chain.
2. Fix the node to handle the missing/unexpected state safely.
3. Add the test case to the minimum coverage contract above.

The bare-Continue case (resuming with no `review_payload`) was discovered this way. It is now a required test case because of that.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_methodology.md`.