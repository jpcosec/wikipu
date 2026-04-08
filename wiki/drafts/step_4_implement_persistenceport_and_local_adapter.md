---
identity:
  node_id: "doc:wiki/drafts/step_4_implement_persistenceport_and_local_adapter.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/agent_guideline.md", relation_type: "documents"}
---

Create/adjust:

## Details

Create/adjust:

- `PersistencePort` interface,
- `LocalPersistenceAdapter` implementation.

Rules:

- runtime never sees physical database details,
- adapter normalizes output to the port contract,
- save and load are both covered by tests.

---

Generated from `raw/docs_cotizador/plan/U-1-save/agent_guideline.md`.