---
identity:
  node_id: "doc:wiki/drafts/4_local_persistence_and_state_management.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md", relation_type: "documents"}
---

The "Database" is the filesystem (Local-First).

## Details

The "Database" is the filesystem (Local-First).

### Persistent DB in Files

- All application data resides in `data/jobs/<source>/<job_id>/`. This ensures portability and easy debugging.

### State Synchronization

- Pipeline state (`state.json`) is managed by LangGraph.
- Any manual edit in the UI (JSON or Markdown) overwrites the file in `data/`, triggering a state update in the backend for the next execution.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md`.