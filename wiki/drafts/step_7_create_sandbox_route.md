---
identity:
  node_id: "doc:wiki/drafts/step_7_create_sandbox_route.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md", relation_type: "documents"}
---

File: `apps/sandbox/routes/step-I3-category/index.html`

## Details

File: `apps/sandbox/routes/step-I3-category/index.html`

Standard sandbox page:
- Links global CSS
- Loads Alpine
- Imports and calls `mountCategoryStandalone(document.getElementById('app'))`

Update:
- `apps/sandbox/index.html` — add nav link to step-I3-category
- `tools/serve-sandbox.mjs` — add `'step-I3-category'` to route list

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md`.