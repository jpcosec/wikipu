---
identity:
  node_id: "doc:wiki/drafts/test_levels.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/testing-components.md", relation_type: "documents"}
---

1. **Domain unit tests**

## Details

1. **Domain unit tests**
   - Pure functions (pricing, quantity, formatting, rules helpers).
   - Fast and deterministic.
2. **Runtime integration tests**
   - Component + machine + projection contracts.
   - Examples: `basketMachine`, `catalogMachine`, `categoryMachine`.
3. **E2E flow tests**
   - Browser behavior against sandbox or GAS preview routes.

Generated from `raw/docs_cotizador/docs/GUIDES/testing-components.md`.