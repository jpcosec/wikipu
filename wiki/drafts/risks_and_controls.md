---
identity:
  node_id: "doc:wiki/drafts/risks_and_controls.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

Main risks:

## Details

Main risks:

- hidden behavior changes during class/factory migration
- dual-path confusion while wrappers coexist
- flow regressions in step-04 runtime

Controls:

- compatibility wrappers with explicit deprecation window
- contract tests for lifecycle, actor wiring, and `toDisplayObject()` shape
- scenario/flow tests for stage transitions and context propagation

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.