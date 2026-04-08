---
identity:
  node_id: "doc:wiki/drafts/current_component_packages.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/PACKAGES/components.md", relation_type: "documents"}
---

- `item/` - core item runtime (`catalog` and `basket` modes), pricing/quantity/rules projections.

## Details

- `item/` - core item runtime (`catalog` and `basket` modes), pricing/quantity/rules projections.
- `category/` - category-level runtime over item actors.
- `catalog/` - multi-category orchestration runtime.
- `basket-day/` - single-day basket runtime with entry-level operations.
- `basket/` - multi-day basket orchestration runtime.
- `quotation/` - modal/view classes used in quotation app composition.
- `common/` - shared base classes, mixins, and style tokens.

Legacy demo packages retained for historical reference:

- `counter-basic/`
- `counter-composed/`

Generated from `raw/docs_cotizador/docs/PACKAGES/components.md`.