---
identity:
  node_id: "doc:wiki/drafts/4_error_contracts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_quality_checklist.md", relation_type: "documents"}
---

- [ ] Domain-specific custom exceptions are defined at the top of the file (no reliance on bare `Exception`).

## Details

- [ ] Domain-specific custom exceptions are defined at the top of the file (no reliance on bare `Exception`).
- [ ] No errors are swallowed silently — every caught exception is either logged or re-raised with `from e`.
- [ ] Caught errors are logged with `LogTag.WARN` or `LogTag.FAIL` before any recovery is attempted.
- [ ] ABCs expose operational limits (chunk sizes, retry delays, etc.) as `@property` attributes.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_quality_checklist.md`.