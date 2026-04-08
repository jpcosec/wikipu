---
identity:
  node_id: "doc:wiki/drafts/events.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-3-category/machine_blueprint.md", relation_type: "documents"}
---

| Event | Payload |

## Details

| Event | Payload |
|-------|---------|
| SELECT_CATEGORY | `{ categoryId }` |
| ADD_ITEM | `{ itemId }` |
| REMOVE_ITEM | `{ itemId }` |
| SET_CONTEXT | `{ patch: { paxGlobal?, dia?, hora? } }` |

---

Generated from `raw/docs_cotizador/plan/legacy/I-3-category/machine_blueprint.md`.