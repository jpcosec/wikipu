---
identity:
  node_id: "doc:wiki/drafts/step_5_build_the_playground_mount_function.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md", relation_type: "documents"}
---

File: `packages/components/category/logic/createCategoryStandaloneComponent.js`

## Details

File: `packages/components/category/logic/createCategoryStandaloneComponent.js`

The mount function sets up an Alpine component that:
1. Maintains the `externalContext` (paxGlobal, dia, hora) — the External State Panel controls
2. Maintains the selected category definition
3. Maintains the `Category` instance and its items list
4. Re-calls `category.receiveContext()` and `item.calculate()` whenever context changes
5. Exposes `state = category.toDisplayObject()` for the template to bind to

See `minimal_js_pseudo_code.md` for the Alpine component data structure.

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md`.