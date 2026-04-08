---
identity:
  node_id: "doc:wiki/drafts/relationship_between_category_machine_and_item_display.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/machine_blueprint.md", relation_type: "documents"}
---

Category's playground renders each item using the **existing Item component template** — it does not re-implement item rendering. Each `item` in `state.items` is the output of `Item.toDisplayObject()`, so the same HTML partial used in the I-2 playground can be reused here.

## Details

Category's playground renders each item using the **existing Item component template** — it does not re-implement item rendering. Each `item` in `state.items` is the output of `Item.toDisplayObject()`, so the same HTML partial used in the I-2 playground can be reused here.

The Category machine does **not** spawn child Item machines. Items are plain domain objects managed by the closure `Category` instance. This keeps the machine simple and avoids inter-actor communication overhead at this stage.

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/machine_blueprint.md`.