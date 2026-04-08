---
identity:
  node_id: "doc:wiki/drafts/step_2_write_failing_tests.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md", relation_type: "documents"}
---

File: `packages/components/category/tests/Category.test.js`

## Details

File: `packages/components/category/tests/Category.test.js`

Create the directory first:
```bash
mkdir -p packages/components/category/tests
```

Write tests that cover all completion criteria from `objectives.md`. Import `Category` from `../Category.js` (which does not exist yet). Import `Item` and `resolveItemDefinition` and seed from the established paths.

Run to confirm all fail (module not found).

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/agent_guideline.md`.