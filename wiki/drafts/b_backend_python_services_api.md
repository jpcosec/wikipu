---
identity:
  node_id: "doc:wiki/drafts/b_backend_python_services_api.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/02_system_architecture.md", relation_type: "documents"}
---

- **LangGraph Orchestrator**: The engine that executes stages. Agnostic to whether called via CLI or API.

## Details

- **LangGraph Orchestrator**: The engine that executes stages. Agnostic to whether called via CLI or API.
- **FastAPI Server**: Acts as a bridge (Data Bridge). Its function is not to manage a DB, but to read/write to the local filesystem and expose it to the UI.
- **Provenance Service**: Responsible for tracking where each piece of data comes from (link between original text and extraction).

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/02_system_architecture.md`.