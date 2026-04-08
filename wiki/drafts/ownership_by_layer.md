---
identity:
  node_id: "doc:wiki/drafts/ownership_by_layer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/data_management.md", relation_type: "documents"}
---

### LangGraph state

## Details

### LangGraph state

Owns:

- routing
- UI-facing lightweight summaries
- refs and status flags

Must not own:

- full generated documents
- large source markdown
- repeated JSON payload copies for every step

### Data manager

Owns:

- job root resolution
- node/stage artifact placement
- primitive artifact reads and writes
- lifecycle metadata in `meta.json`

Enforcement rule:

- runtime code under `src/graph/`, `src/core/ai/`, and `src/core/tools/` must not bypass `DataManager` for filesystem operations
- direct `Path.read_text()`, `read_bytes()`, `write_text()`, `write_bytes()`, and `mkdir()` calls are only allowed inside `src/core/data_manager.py`

Must not own:

- domain validation
- business logic
- LangGraph state

### Nodes and adapters

Own:

- validating primitive data into Pydantic models
- business transforms
- deciding what the canonical outputs of the step are

---

Generated from `raw/docs_postulador_refactor/docs/runtime/data_management.md`.