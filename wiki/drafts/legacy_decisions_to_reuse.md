---
identity:
  node_id: "doc:wiki/drafts/legacy_decisions_to_reuse.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-3-gas/objectives.md", relation_type: "documents"}
---

- Router functions exposed to client (`guardarCotizacion`, `cargarCotizacion`) via `google.script.run`.

## Details

- Router functions exposed to client (`guardarCotizacion`, `cargarCotizacion`) via `google.script.run`.
- Service orchestration separated from model/store access.
- Sheet persistence through a dedicated abstraction (`SheetDB` in legacy).

References:

- `claps_codelab/Codigo.js`
- `claps_codelab/Controller_Cotizacion.js`
- `claps_codelab/Models.js`
- `claps_codelab/SheetDB.js`

---

Generated from `raw/docs_cotizador/plan/U-3-gas/objectives.md`.