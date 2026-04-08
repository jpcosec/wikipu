---
identity:
  node_id: "doc:wiki/drafts/architecture_plan.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-04-quotation-internal-rebuild-plan.md", relation_type: "documents"}
---

1. Build a quotation runtime coordinator in `apps/quotation/state/` that composes:

## Details

1. Build a quotation runtime coordinator in `apps/quotation/state/` that composes:
   - `createCatalogActor` (catalog orchestration),
   - `createBasketActor` (day-wide basket orchestration).
2. Keep UI as projection-only:
   - one snapshot contract (`toDisplayObject`) for Alpine,
   - no pricing/rules/business logic in template handlers.
3. Keep identity boundary strict:
   - item definition identity by `itemId`,
   - entry mutation identity by `entryId`.

Generated from `raw/docs_cotizador/docs/plans/2026-03-04-quotation-internal-rebuild-plan.md`.