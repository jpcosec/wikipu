---
identity:
  node_id: "doc:wiki/drafts/step_2_validate_csv_integration_via_seed_test_js.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md", relation_type: "documents"}
---

File: `packages/database/src/seed.test.js`

## Details

File: `packages/database/src/seed.test.js`

Tests load directly from `data/init/*.csv` using `loadSeedFromCsvDir()`. No hand-written seed fixture — the CSV files are the test data.

Tests must verify:
1. All 11 tables load without error
2. FK references resolve across tables (e.g., `ITEM_CATALOGO.ID_Categoria` → `CATEGORIAS`)
3. At least one item has `ID_Perfil_Precio_Override: null` (inherits from category)
4. At least one item has a non-null `ID_Perfil_Precio_Override` (explicit override)
5. `REGLAS_NEGOCIO` rows contain at least one `ERROR` and one `WARNING` rule with `Scope='ITEM'`

Run tests first to confirm failures if coverage is missing, then fix until all pass.

Commit: `feat: csv-based schema conformance and FK integrity tests`

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/agent_guideline.md`.