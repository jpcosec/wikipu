---
identity:
  node_id: "doc:wiki/drafts/usage.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/creating-a-component.md", relation_type: "documents"}
---

\`\`\`javascript

## Details

\`\`\`javascript
import { createMyComponent } from './logic/createMyComponent.js';

const component = await createMyComponent(
  { initial: 0, min: -10, max: 100 },
  'container-id'
);

component.setValue(50);
component.increment();

const state = component.getState();
console.log(state.value);  // 51
\`\`\`

Generated from `raw/docs_cotizador/docs/GUIDES/creating-a-component.md`.