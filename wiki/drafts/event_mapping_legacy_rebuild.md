---
identity:
  node_id: "doc:wiki/drafts/event_mapping_legacy_rebuild.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-04-legacy-functionality-recovery-mapping.md", relation_type: "documents"}
---

- `agregarItem(item)` -> `basket.send({ type: 'SHIP_ITEM_TO_DAY', dayIndex, itemId })`

## Details

- `agregarItem(item)` -> `basket.send({ type: 'SHIP_ITEM_TO_DAY', dayIndex, itemId })`
- `actualizarCantidad/Unidades/Duracion/Hora/Comentario` -> `SET_ENTRY_OVERRIDE` per key
- clear field -> `CLEAR_ENTRY_OVERRIDE`
- reset line -> `RESET_ENTRY_OVERRIDES`
- `eliminarItem` -> `REMOVE_ENTRY`
- day tab click -> `SELECT_DAY`
- global pax/hour/duration changes -> `SET_CONTEXT`
- move entry day -> `MOVE_ENTRY_TO_DAY`

Generated from `raw/docs_cotizador/docs/plans/2026-03-04-legacy-functionality-recovery-mapping.md`.