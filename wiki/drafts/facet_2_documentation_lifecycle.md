---
identity:
  node_id: "doc:wiki/drafts/facet_2_documentation_lifecycle.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/methodology_synthesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/methodology_synthesis.md"
  source_hash: "509baf32ca0ea70f59fdc2382e05095dde9fba07ad7092c46d49ecdca431bc34"
  compiled_at: "2026-04-10T17:47:33.731960"
  compiled_from: "wiki-compiler"
---

**Question:** How does an idea move from thought to plan to code to history?

## Details

**Question:** How does an idea move from thought to plan to code to history?

**Consistent pattern (postulador_refactor, postulador_v2, doc_methodology):**

```
idea / known problem
  → future_docs/<topic>.md     (deferred: why, proposed direction, linked TODO)
  → plan_docs/<plan>.md        (active: when prioritized, future_docs entry deleted)
  → deleted + changelog.md     (complete: plan deleted, inline TODO removed)
```

**Additional rule from doc_methodology:**
- `docs/runtime/` = current truth. Never contaminated by plan references.
- `plan/` can reference `docs/runtime/`. `docs/runtime/` cannot reference `plan/`.
- Temporal unidirectionality: the current state of the world does not point forward to an uncommitted future.

**Key invariant:** Plans are ephemeral by design. A plan that survives its completion is documentation drift. The healthy state is: plan gone, code changed, changelog updated.

**Debt decay rule (postulador_refactor):** future_docs/ entries not touched in 6 months are stale — promote, delete, or re-date. No graveyard accumulation.

---

Generated from `raw/methodology_synthesis.md`.