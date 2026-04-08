---
identity:
  node_id: "doc:wiki/drafts/definition_of_recovered_state.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-04-legacy-functionality-recovery-mapping.md", relation_type: "documents"}
---

Legacy functionality is considered recovered when:

## Details

Legacy functionality is considered recovered when:

- every interaction in the legacy UI has a mapped command in the rebuild route,
- no pricing/rules logic is duplicated in UI handlers,
- entry identity (`entryId`) remains the mutation boundary,
- parity flows (catalog -> basket -> validation -> completion) pass manual and automated checks.

Generated from `raw/docs_cotizador/docs/plans/2026-03-04-legacy-functionality-recovery-mapping.md`.