---
identity:
  node_id: "doc:wiki/drafts/current_flow_and_routing.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/graph_flow.md", relation_type: "documents"}
---

Linear path:

## Details

Linear path:

1. `scrape`
2. `translate_if_needed`
3. `extract_understand`
4. `match`
5. `review_match`
6. `generate_documents`
7. `render`
8. `package`

Review routing in `review_match`:

- `approve` -> `generate_documents` -> `render` -> `package`
- `request_regeneration` -> `match`
- `reject` -> stop

`package` is now a real terminal delivery step for the current prep flow: it validates `render` output refs and writes final markdown deliverables plus `final/manifest.json`.

Generated from `raw/docs_postulador_langgraph/docs/runtime/graph_flow.md`.