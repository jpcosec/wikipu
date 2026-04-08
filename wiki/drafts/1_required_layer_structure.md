---
identity:
  node_id: "doc:wiki/drafts/1_required_layer_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

Every LangGraph module has this file layout:

## Details

Every LangGraph module has this file layout:

```
src/<module>/
  contracts.py     ← schema backbone: all input, output, review, persistence models
  prompt.py        ← prompt construction only: templates, serialization, variable building
  storage.py       ← persistence only: artifact paths, round management, JSON I/O
  graph.py         ← orchestration: state, nodes, edges, chain wiring, Studio factory
  __init__.py      ← public import surface
  main.py          ← CLI entry point
```

Each file owns exactly one concern. Graph nodes never write to disk directly — that belongs in `storage.py`. Prompt logic never lives in `graph.py`.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.