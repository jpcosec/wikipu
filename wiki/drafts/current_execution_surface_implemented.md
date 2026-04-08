---
identity:
  node_id: "doc:wiki/drafts/current_execution_surface_implemented.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

The executable graph helper in daily use is the prep-match flow:

## Details

The executable graph helper in daily use is the prep-match flow:

1. `scrape`
2. `translate_if_needed`
3. `extract_understand`
4. `match`
5. `review_match`
6. `generate_documents`
7. `render`
8. `package`

Implemented by:

- `src/graph.py` via `build_prep_match_node_registry()`, `create_prep_match_app()`, `run_prep_match()`
- `src/cli/run_prep_match.py` for operator execution and resume

Current review routing:

- `approve` -> `generate_documents`
- `request_regeneration` -> `match`
- `reject` -> end

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.