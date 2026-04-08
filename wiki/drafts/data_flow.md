---
identity:
  node_id: "doc:wiki/drafts/data_flow.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/architecture.md", relation_type: "documents"}
---

```

## Details

```
API (real or mock)
  └── React Query hook (features/*/api/)
        └── Page (reads params, calls hook)
              └── Feature component (receives data via props)
                    └── Organism / Molecule / Atom (pure UI)
```

- Lower layers **never** import from upper layers
- `atoms/` and `molecules/` know nothing about the backend
- `features/` don't import each other (maximum via `types/`)

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/ui/architecture.md`.