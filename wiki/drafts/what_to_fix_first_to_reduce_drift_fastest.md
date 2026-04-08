---
identity:
  node_id: "doc:wiki/drafts/what_to_fix_first_to_reduce_drift_fastest.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md", relation_type: "documents"}
---

1. Convert `item` to actor-owned class while preserving `toDisplayObject()` and compatibility wrappers.

## Details

1. Convert `item` to actor-owned class while preserving `toDisplayObject()` and compatibility wrappers.
2. Introduce class APIs for `category`, `catalog`, `basket-day`, `basket` and keep current `createXActor()` functions as temporary adapters.
3. Re-classify `quotation/modals/AppState` to a flow-state base (not modal base).
4. Decide whether Step-04 runtime should be package-first (recommended) or remain app-runtime-first; align docs and ownership to that decision.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/mixins-style-drift-assessment.md`.