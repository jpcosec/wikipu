---
identity:
  node_id: "doc:wiki/drafts/step_3_redirect_home_test_js.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

File: `apps/quotation/components/home.test.js`

## Details

File: `apps/quotation/components/home.test.js`

Change the import line:
```js
// FROM:
import { createHomePageController } from './HomePage.js';

// TO:
import { createHomePage as createHomePageController } from '../../../packages/components/quotation/modals/HomePage.js';
```

The test calls `getActions()`, `clickAction()`, `on()`, `off()` — all exist on `HomePage`. The `isVisible()` wrapper always returned `true`, same as `HomePage.isVisible()`. No other changes needed.

Run tests. This file's tests should now pass.

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.