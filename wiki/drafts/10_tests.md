---
identity:
  node_id: "doc:wiki/drafts/10_tests.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

- **Unit tests** with `AsyncMock` Playwright page: verify `_validate_selectors` raises on missing mandatory selectors, warns on missing optional ones.

## Details

- **Unit tests** with `AsyncMock` Playwright page: verify `_validate_selectors` raises on missing mandatory selectors, warns on missing optional ones.
- **Integration tests** against saved HTML snapshots of real apply forms (not live portals). These are the primary regression guard against DOM changes.
- Snapshot fixtures are stored under `tests/fixtures/apply/` and refreshed manually when portals update their UI.
- The `error_state.png` mechanism makes live debugging tractable without test infrastructure on CI.

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.