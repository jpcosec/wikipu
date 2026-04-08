---
identity:
  node_id: "doc:wiki/drafts/decision_options.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md", relation_type: "documents"}
---

### Option A - Normalize docs to current split/factory reality

## Details

### Option A - Normalize docs to current split/factory reality

- Pros: minimal refactor, lower short-term risk.
- Cons: accepts architecture divergence from the intended invariant.

### Option B - Converge code to actor-owned classes (recommended if invariant is firm)

- Pros: consistent lifecycle model and component API across layers.
- Cons: requires staged refactor and compatibility wrappers during transition.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md`.