---
identity:
  node_id: "doc:wiki/drafts/alpine_connection.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md", relation_type: "documents"}
---

Alpine is display-only. It sends events up to the actor and renders whatever is in `snapshot.context`.

## Details

Alpine is display-only. It sends events up to the actor and renders whatever is in `snapshot.context`.

```
init()
  actor.subscribe(snap => Object.assign(this, snap.context))

Table tab click      → actor.send({ type: 'SELECT_TABLE', tableId })
Column header click  → actor.send({ type: 'SORT', column })
Tag chip click       → actor.send({ type: 'TOGGLE_FILTER', tag })
Cell double-click    → actor.send({ type: 'DOUBLE_CLICK_CELL', rowId, field, value })
Input keydown Enter  → actor.send({ type: 'COMMIT_EDIT' })
Input keydown Escape → actor.send({ type: 'CANCEL_EDIT' })
Input @input         → actor.send({ type: 'UPDATE_BUFFER', value: $el.value })
Add row button       → actor.send({ type: 'ADD_ROW' })
Save new row         → actor.send({ type: 'COMMIT_ADD' })
Cancel new row       → actor.send({ type: 'CANCEL_ADD' })
Delete button        → actor.send({ type: 'DELETE_ROW', rowId })
```

### UI state derivations (Alpine computes from context, no extra state)

| UI element | Derived from |
|-----------|--------------|
| Active table tab highlight | `activeTable` |
| Row count pill | `rows[activeTable].length` |
| Filtered rows | `rows[activeTable]` filtered by `tagFilters` + sorted by `sort` |
| Inline edit input visible | `editTarget !== null && editTarget.rowId === row.id && editTarget.field === field` |
| Cell error outline | `editTarget.error !== null` (in editing state) |
| Pending row visible | `pendingRow !== null` (green-left-border accent) |

---

Generated from `raw/docs_cotizador/plan/legacy/I-1-database/machine_blueprint.md`.