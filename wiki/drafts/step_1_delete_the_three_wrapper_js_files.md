---
identity:
  node_id: "doc:wiki/drafts/step_1_delete_the_three_wrapper_js_files.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

```bash

## Details

```bash
rm apps/quotation/state/AppStateMachine.js
rm apps/quotation/components/HomePage.js
rm apps/quotation/components/ClientSelector.js
```

These files contained only delegation code and no original logic.

Run tests. Expected: some tests will now fail (the three test files importing from these wrappers). That is expected — proceed to Step 2.

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.