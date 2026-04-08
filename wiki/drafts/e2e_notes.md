---
identity:
  node_id: "doc:wiki/drafts/e2e_notes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/GUIDES/testing-components.md", relation_type: "documents"}
---

- Playwright specs live in `tests/e2e/**`.

## Details

- Playwright specs live in `tests/e2e/**`.
- Keep unit assertions out of E2E tests; focus on user flows and integration behavior.
- Prefer stable selectors (roles, labels, text contracts) over brittle CSS chains.

Generated from `raw/docs_cotizador/docs/GUIDES/testing-components.md`.