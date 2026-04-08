---
identity:
  node_id: "doc:wiki/drafts/shared_constraints.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/phases/README.md", relation_type: "documents"}
---

- Legacy behavior must be reviewed first (`Codigo.js`, `Controller_Cotizacion.js`, `Models.js`, `SheetDB.js`, `Stores_App.html`).

## Details

- Legacy behavior must be reviewed first (`Codigo.js`, `Controller_Cotizacion.js`, `Models.js`, `SheetDB.js`, `Stores_App.html`).
- Mapper is pure (no I/O).
- Runtime depends only on `PersistencePort`.
- Adapter owns physical persistence details.
- Field names in persisted payload match `Config_Schema.js`.

Generated from `raw/docs_cotizador/plan/U-1-save/phases/README.md`.