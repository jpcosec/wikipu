---
identity:
  node_id: "doc:wiki/drafts/what_already_exists.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/objectives.md", relation_type: "documents"}
---

| Artifact | Status | Location |

## Details

| Artifact | Status | Location |
|---|---|---|
| Transactional schema (`COTIZACIONES`, `LINEA_DETALLE`) | ✅ | `packages/database/src/Config_Schema.js` |
| In-memory store and model factory | ✅ | `packages/database/src/stores/InMemoryStore.js`, `packages/database/src/createDatabase.js` |
| Runtime snapshot/projection | ✅ | `apps/quotation/state/createQuotationInternalRuntime.js` |
| Legacy save/load behavior | ✅ reference | `claps_codelab/Controller_Cotizacion.js` |
| Legacy UI calls (`google.script.run`) | ✅ reference | `claps_codelab/Stores_App.html` |

Generated from `raw/docs_cotizador/plan/U-1-save/objectives.md`.