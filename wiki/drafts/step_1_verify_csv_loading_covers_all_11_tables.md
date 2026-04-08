---
identity:
  node_id: "doc:wiki/drafts/step_1_verify_csv_loading_covers_all_11_tables.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md", relation_type: "documents"}
---

**Data source:** `data/init/*.csv` is the only source of truth. Do not maintain a separate hand-written seed fixture for the playground or integration tests.

## Details

**Data source:** `data/init/*.csv` is the only source of truth. Do not maintain a separate hand-written seed fixture for the playground or integration tests.

Load data via:
- `loadSeedFromCsvUrl(baseUrl)` — browser (fetches from `/data/init`)
- `loadSeedFromCsvDir(dirPath)` — Node.js tests (reads from `data/init/`)

Verify that all 11 tables load without error and that `BROWSER_TABLES` in `databaseMachine.js` lists all of them:

```
Block 1 — Reference:   CLIENTES, PERFILES_PRECIO, CATEGORIAS, ITEM_CATALOGO, COMPOSICION_KIT, REGLAS_NEGOCIO
Block 2 — Transactional: COTIZACIONES, LINEA_DETALLE, AJUSTES_COTIZACION, CACHE_COTIZACION, HISTORIAL_COTIZACION
```

Tables with header-only CSVs (no data rows yet) should still load without error.

Export format (single named export):
```js
export const SEED_DATA = [
  { table: 'PERFILES_PRECIO', records: [...] },
  { table: 'CATEGORIAS', records: [...] },
  { table: 'ITEM_CATALOGO', records: [...] },
  { table: 'REGLAS_NEGOCIO', records: [...] }
];
```

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md`.