---
identity:
  node_id: "doc:wiki/drafts/design_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/phases/02_persistence_port.md", relation_type: "documents"}
---

- Runtime and UI know only `PersistencePort`.

## Details

- Runtime and UI know only `PersistencePort`.
- Adapter owns physical storage specifics.
- Interface must support both local simulation and GAS without changes to runtime.

Generated from `raw/docs_cotizador/plan/U-1-save/phases/02_persistence_port.md`.