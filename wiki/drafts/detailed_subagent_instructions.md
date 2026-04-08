---
identity:
  node_id: "doc:wiki/drafts/detailed_subagent_instructions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/phases/01_category_loader.md", relation_type: "documents"}
---

### Subagent A - Contract and dependency audit (explore)

## Details

### Subagent A - Contract and dependency audit (explore)

Read and summarize integration boundaries from:

- `packages/database/src/resolveItemDefinition.js`
- `packages/components/item/Item.js`
- `packages/components/item/machine/itemMachine.js`
- `packages/components/category/STATE_CONTRACT.md`

Return:

- Required child snapshot fields for aggregation.
- API assumptions that must not change.
- Mismatches to fix before implementation.

### Subagent B - Category runtime and tests (general)

Implement and test a minimal category runtime manager.

Required runtime capabilities:

- initialize from `{ categoryId, db, context }`
- create/destroy child entries
- broadcast context patches to all children
- compute category display snapshot from child snapshots

Write tests first for:

- load all active items in selected category
- aggregate totals and rule flags
- cleanup correctness (no stale updates after destroy)

### Subagent C - Minimal playground route (general)

Create a basic route with:

- category selector
- context controls (`paxGlobal`, `dia`, `hora`)
- simple list of child item summaries
- category aggregate panel

Do not implement timeline interactions in this step.

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/phases/01_category_loader.md`.