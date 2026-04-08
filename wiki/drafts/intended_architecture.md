---
identity:
  node_id: "doc:wiki/drafts/intended_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md", relation_type: "documents"}
---

The LangGraph API server is the single source of truth for all graph state. The CLI is a thin HTTP client. There is no local execution path.

## Details

The LangGraph API server is the single source of truth for all graph state. The CLI is a thin HTTP client. There is no local execution path.

- If the API is unreachable → fail fast with a clear error message.
- `data/jobs/checkpoints.db` is no longer written or read by the CLI.
- `build_match_skill_graph` is only called by the API server (via `langgraph.json`), not by the CLI.

Generated from `raw/docs_postulador_refactor/future_docs/issues/api_only_execution.md`.