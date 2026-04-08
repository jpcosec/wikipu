---
identity:
  node_id: "doc:wiki/drafts/unreleased.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/plans/2026-03-29-pipeline-graph-unification.md", relation_type: "documents"}
---

### Refactored

## Details

### Refactored
- Pipeline graph: `match_skill` is now a native LangGraph compiled subgraph — inner topology (load_match_inputs → run_match_llm → persist_match_round → human_review_node → apply_review_decision → …) is fully visible in LangGraph Studio.
- Match skill graph: replaced `Command`-based routing in `apply_review_decision` with `add_conditional_edges` — all routing paths are now statically declared and visible in Studio.
- `GraphState` carries `requirements` and `profile_evidence` populated by `extract_bridge`, enabling clean subgraph state passing without wrapper nodes.
- Removed `src/graph/nodes/match_skill.py` opaque wrapper node.
```

- [ ] **Step 4.4: Run full test suite one final time**

Run: `pytest tests/ -q`
Expected: all pass

- [ ] **Step 4.5: Final commit**

```bash
git add src/core/ai/match_skill/graph.py future_docs/issues/pipeline_graph_unification.md changelog.md
git commit -m "chore: remove resolved TODOs and update changelog for graph unification"
```

Generated from `raw/docs_postulador_refactor/docs/superpowers/plans/2026-03-29-pipeline-graph-unification.md`.