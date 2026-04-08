---
identity:
  node_id: "doc:wiki/drafts/async_readiness_phase_4.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md", relation_type: "documents"}
---

When GAS is wired in, `COMMIT_EDIT` and `COMMIT_ADD` gain a `saving` intermediate state. The machine absorbs this without Alpine changes — Alpine just sees a `isSaving: true` flag in context and disables the commit button.

## Details

When GAS is wired in, `COMMIT_EDIT` and `COMMIT_ADD` gain a `saving` intermediate state. The machine absorbs this without Alpine changes — Alpine just sees a `isSaving: true` flag in context and disables the commit button.

```
editing → COMMIT_EDIT [valid] → saving → (on done) → browsing
                                        → (on error) → editing (sets error)
```

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md`.