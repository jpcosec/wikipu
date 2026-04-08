---
identity:
  node_id: "doc:wiki/drafts/lifecycle.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/future_docs_guide.md", relation_type: "documents"}
---

```

## Details

```
idea / known problem
       ↓
  future_docs/<topic>.md  ←  linked from inline # TODO(future)
       ↓  (when prioritized)
  plan_docs/<plan>.md     ←  full execution plan written, future_docs entry deleted
       ↓  (when complete)
  plan_docs deleted, changelog.md updated, inline TODO removed
```

- Promote to `plan_docs/` when the item enters active execution.
- Delete the `future_docs/` entry at that point — do not keep both.
- Remove the inline `# TODO(future)` comment once the work is done.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/future_docs_guide.md`.