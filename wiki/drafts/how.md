---
identity:
  node_id: "doc:wiki/drafts/how.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/phases/01_category_loader.md", relation_type: "documents"}
---

Build a category playground route that:

## Details

Build a category playground route that:

1. Loads DB seed once.
2. Maps seed using shared adapter `seedToResolverDb(seed)`.
3. Lets the user select one category.
4. Resolves all active category items through `resolveItemDefinition`.
5. Creates one item actor per runtime entry.
6. Broadcasts context (`paxGlobal`, `dia`, `hora`) to every child actor via `SET_CONTEXT`.
7. Aggregates snapshot collections into category display state.

Presentation constraint for this step:

- Use the shared item catalog HTML (`catalogRuntimeHtml`) instead of duplicating card markup in category templates.

Identity rule for this and all next steps:

- `itemId`: definition identity from DB.
- `entryId`: runtime identity for each instance in the container.

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/phases/01_category_loader.md`.