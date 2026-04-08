---
identity:
  node_id: "doc:wiki/drafts/what_subclasses_must_implement.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md", relation_type: "documents"}
---

Three methods throw at runtime if not overridden:

## Details

Three methods throw at runtime if not overridden:

| Method | Required by | Error timing |
|--------|-------------|--------------|
| `toDisplayObject()` | `Alpineable` | When Alpine tries to render |
| `toStorageObject()` | `Storable` | When persistence is attempted |
| `validate()` | `Formable` | When form submission is attempted |

One method has a default implementation that subclasses *should* override:

| Method | Provided by | Default behavior |
|--------|-------------|-----------------|
| `_buildRuleContext()` | `Rulable` | Returns `{ ...this._inheritedContext }` |

Subclasses override `_buildRuleContext()` to enrich the evaluation context with their own state fields (e.g., the item's `_profile`, its own IDs, current quantities). The richer the context, the more conditional the rules can be.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixin-arch/02_design_strategy.md`.