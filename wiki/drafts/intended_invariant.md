---
identity:
  node_id: "doc:wiki/drafts/intended_invariant.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md", relation_type: "documents"}
---

Expected shape for each component:

## Details

Expected shape for each component:

1. Component class owns its XState actor internally.
2. Public methods delegate to actor events (not direct synchronous mutation pipelines).
3. Lifecycle ownership is local to the class (`start`, `stop`, subscriptions, cleanup).
4. Parent containers compose child classes through their actor-owned APIs.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md`.