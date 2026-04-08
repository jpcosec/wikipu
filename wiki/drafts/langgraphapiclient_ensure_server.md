---
identity:
  node_id: "doc:wiki/drafts/langgraphapiclient_ensure_server.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md", relation_type: "documents"}
---

The `api_client.py` already has `ensure_server()` which can auto-start `langgraph dev` if not running. The CLI commands could call this instead of the current ping-then-fallback pattern, making the API server a transparent prerequisite rather than an optional dependency.

## Details

The `api_client.py` already has `ensure_server()` which can auto-start `langgraph dev` if not running. The CLI commands could call this instead of the current ping-then-fallback pattern, making the API server a transparent prerequisite rather than an optional dependency.

Generated from `raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md`.