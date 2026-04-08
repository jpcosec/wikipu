---
identity:
  node_id: "doc:wiki/drafts/impact.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md", relation_type: "documents"}
---

1. Architectural mismatch: docs describe actor-owned classes while code often uses class+machine split or machine-only factories.

## Details

1. Architectural mismatch: docs describe actor-owned classes while code often uses class+machine split or machine-only factories.
2. Lifecycle ambiguity: actor ownership is distributed, making cleanup contracts less uniform.
3. API inconsistency: some modules are class-first, others actor-factory-first.
4. Onboarding friction: engineers cannot infer one canonical component construction pattern.

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/actor-ownership-drift-diagnostics.md`.