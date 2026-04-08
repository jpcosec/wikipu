---
identity:
  node_id: "doc:wiki/drafts/testing.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/PACKAGES/components.md", relation_type: "documents"}
---

Run package-level and integration tests from repo root:

## Details

Run package-level and integration tests from repo root:

```bash
npm test
```

Run selected suites:

```bash
npx vitest run packages/components/item/tests/Item.test.js
npx vitest run packages/components/basket/tests/basketMachine.test.js
npx vitest run packages/components/catalog/tests/catalogMachine.test.js
```

Last update: 2026-03-11

Generated from `raw/docs_cotizador/docs/PACKAGES/components.md`.