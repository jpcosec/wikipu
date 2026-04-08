---
identity:
  node_id: "doc:wiki/drafts/what_is_a_component_for_this_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-11-vistas-design-map.md", relation_type: "documents"}
---

Use these planning tags to avoid ambiguity.

## Details

Use these planning tags to avoid ambiguity.

- `COMPONENT`: reusable runtime unit (own state/machine/API), e.g. `item`, `catalog`, `basket-day`, `basket`.
- `SCREEN`: app-level composition of components (home, quotation editor, validation).
- `WORKFLOW`: state/navigation orchestration (AppFlow stage machine).
- `SERVICE`: persistence/export adapters (save/load/PDF/Excel).
- `TOOL`: admin/editor tooling (DB browser, rule builder, category/price builders).

Rule of thumb:

- If it can be mounted and reused in multiple screens with a stable API, treat it as `COMPONENT`.
- If it mostly routes, coordinates, or persists, it is not a component (`SCREEN`, `WORKFLOW`, `SERVICE`, `TOOL`).

Generated from `raw/docs_cotizador/docs/plans/2026-03-11-vistas-design-map.md`.