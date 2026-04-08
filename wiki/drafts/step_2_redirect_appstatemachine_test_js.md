---
identity:
  node_id: "doc:wiki/drafts/step_2_redirect_appstatemachine_test_js.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md", relation_type: "documents"}
---

File: `apps/quotation/state/appStateMachine.test.js`

## Details

File: `apps/quotation/state/appStateMachine.test.js`

Change the import line:
```js
// FROM:
import { createAppStateMachine } from './AppStateMachine.js';

// TO:
import { createAppState as createAppStateMachine } from '../../../packages/components/quotation/modals/AppState.js';
```

Run tests. This file's tests should now pass again.

---

Generated from `raw/docs_cotizador/plan/legacy/0-cleanup/agent_guideline.md`.