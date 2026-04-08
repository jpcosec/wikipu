---
identity:
  node_id: "doc:wiki/drafts/recommended_migration_strategy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md", relation_type: "documents"}
---

1. **Do not rewrite everything at once.** Build class-first APIs while preserving wrappers.

## Details

1. **Do not rewrite everything at once.** Build class-first APIs while preserving wrappers.
2. **Stabilize Item first.** It is the foundational leaf for all container components.
3. **Migrate containers in dependency order:** `category -> catalog -> basket-day -> basket`.
4. **Extract `AppFlow` last,** once component contracts are stable.
5. **Gate each phase with tests** before removing adapters.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/05_ideal_mixin_migration_idea.md`.