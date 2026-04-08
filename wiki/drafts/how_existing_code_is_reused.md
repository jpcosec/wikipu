---
identity:
  node_id: "doc:wiki/drafts/how_existing_code_is_reused.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

Most reusable pieces already exist:

## Details

Most reusable pieces already exist:

- mixins in `packages/components/common/mixins/`
- role base classes in `packages/components/common/base/`
- container actor orchestration patterns in `category`, `catalog`, `basket-day`, `basket`
- quotation flow stages already modeled in runtime logic

Migration focuses on:

1. adding `ComponentBase` and flow/scenario bases,
2. re-pointing existing base compositions to inherit from `ComponentBase`,
3. moving component entry points to class-first APIs,
4. keeping compatibility wrappers during transition.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.