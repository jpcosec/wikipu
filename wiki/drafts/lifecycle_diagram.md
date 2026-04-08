---
identity:
  node_id: "doc:wiki/drafts/lifecycle_diagram.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/entrypoint.md", relation_type: "documents"}
---

```

## Details

```
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 1: PLANNING                           │
│  planning_template*.md → plan/[domain]/feature.md              │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 2: EXECUTION                          │
│  Implement via agent or manually → Code in src/                 │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 3: TESTING                            │
│  Local verification → TestSprite E2E tests                     │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 4: DOCUMENTATION                      │
│  Promote plan → docs/runtime → Delete plan → Changelog          │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 5: GIT                                │
│  Standardized commit message                                    │
└─────────────────────────┬───────────────────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     PHASE 6: META-REVIEW                        │
│  Audit session → Fix friction → Update meta-docs               │
└─────────────────────────────────────────────────────────────────┘
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/entrypoint.md`.