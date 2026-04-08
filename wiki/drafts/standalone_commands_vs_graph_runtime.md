---
identity:
  node_id: "doc:wiki/drafts/standalone_commands_vs_graph_runtime.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/runtime/data_management.md", relation_type: "documents"}
---

### Top-level graph

## Details

### Top-level graph

- reads through the data manager when loading disk artifacts
- works on in-memory primitive payloads and validated models
- persists canonical outputs back through the data manager

### Standalone CLI

Follows a strict three-step flow:

1. `DataManager.read_*_artifact(...)`
2. pass primitive payload into the domain adapter/core
3. `DataManager.write_*_artifact(...)`

This keeps disk IO out of business logic while preserving debuggable standalone
commands.

Generated from `raw/docs_postulador_refactor/docs/runtime/data_management.md`.