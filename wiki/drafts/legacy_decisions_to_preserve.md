---
identity:
  node_id: "doc:wiki/drafts/legacy_decisions_to_preserve.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/objectives.md", relation_type: "documents"}
---

From `claps_codelab`:

## Details

From `claps_codelab`:

1. Save/Load/PDF are routed via GAS-facing functions (`guardarCotizacion`, `cargarCotizacion`, `generarPDF`).
2. Save-first flow is mandatory before PDF generation.
3. Business flow is layered: router -> controller/service -> model/store.
4. Client + quotation + detail rows are persisted together as one business operation.

References:

- `claps_codelab/Codigo.js`
- `claps_codelab/Controller_Cotizacion.js`
- `claps_codelab/Models.js`
- `claps_codelab/Stores_App.html`

---

Generated from `raw/docs_cotizador/plan/U-1-save/objectives.md`.