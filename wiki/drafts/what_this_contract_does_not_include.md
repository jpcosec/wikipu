---
identity:
  node_id: "doc:wiki/drafts/what_this_contract_does_not_include.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md", relation_type: "documents"}
---

- Transactional data (COTIZACIONES, LINEA_DETALLE) — resolved at quotation level, not item level

## Details

- Transactional data (COTIZACIONES, LINEA_DETALLE) — resolved at quotation level, not item level
- COMPOSICION_KIT children — resolved by a separate `resolveKitDefinition()` (future)
- Computed pricing totals — calculated at runtime by the Item domain, never stored here
- `Updated_At` timestamps — stripped; not needed downstream

Generated from `raw/docs_cotizador/plan/legacy/III-1-resolver/field_contracts.md`.