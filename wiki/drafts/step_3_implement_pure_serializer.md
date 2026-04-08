---
identity:
  node_id: "doc:wiki/drafts/step_3_implement_pure_serializer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/agent_guideline.md", relation_type: "documents"}
---

Create serializer from runtime snapshot to transactional payload.

## Details

Create serializer from runtime snapshot to transactional payload.

Rules:

- pure function,
- no store calls,
- deterministic mapping.

Add tests for:

- multi-day entries,
- overrides,
- empty/edge cases,
- ID policy injection.

---

Generated from `raw/docs_cotizador/plan/U-1-save/agent_guideline.md`.