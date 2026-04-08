---
identity:
  node_id: "doc:wiki/drafts/acceptance_criteria_for_drift_resolved.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md", relation_type: "documents"}
---

1. Every component has an actor-owned class as the primary API.

## Details

1. Every component has an actor-owned class as the primary API.
2. Factory helpers are optional adapters, not the architecture center.
3. Lifecycle operations (`start`, `subscribe`, `stop`) are owned and documented per class.
4. Docs, plans, and implementation all describe the same pattern.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md`.