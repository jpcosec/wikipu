---
identity:
  node_id: "doc:wiki/drafts/1_module_layout.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md", relation_type: "documents"}
---

```

## Details

```
src/apply/
  __init__.py
  main.py              # CLI entry point and provider registry
  smart_adapter.py     # ApplyAdapter ABC and shared execution logic
  models.py            # FormSelectors, ApplicationRecord, ApplyMeta
  providers/
    xing/adapter.py
    stepstone/adapter.py
  README.md
```

---

Generated from `raw/docs_postulador_refactor/docs/superpowers/specs/2026-03-30-apply-module-design.md`.