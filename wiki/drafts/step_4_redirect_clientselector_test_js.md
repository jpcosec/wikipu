---
identity:
  node_id: "doc:wiki/drafts/step_4_redirect_clientselector_test_js.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

File: `apps/quotation/components/clientSelector.test.js`

## Details

File: `apps/quotation/components/clientSelector.test.js`

Change the import line:
```js
// FROM:
import { createClientSelectorController } from './ClientSelector.js';

// TO:
import { createClientSelector as createClientSelectorController } from '../../../packages/components/quotation/modals/ClientSelector.js';
```

Then **delete the `getAllClients` test** — it tested wrapper-only logic that doesn't exist in the package:
```js
// DELETE the entire block:
it('should get all original clients', () => { ... });
```

Run tests. All remaining tests in this file should pass.

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.