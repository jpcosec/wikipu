---
identity:
  node_id: "doc:wiki/drafts/completion_criteria.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/plan/U-1-save/objectives.md", relation_type: "documents"}
---

### Contract

## Details

### Contract

- [ ] `SavePayload.md` includes two mappings:
  - legacy semantic mapping (`claps_codelab` fields and responses),
  - rebuild schema mapping (`COTIZACIONES`, `LINEA_DETALLE` in `Config_Schema.js`).
- [ ] ID strategy is configurable via boundary (no hard-coded format in runtime).

### Serializer

- [ ] `serializeQuotation(...)` is pure and deterministic.
- [ ] All required transactional columns are populated.
- [ ] Overrides are mapped (`pax`, `cantidad`, `duracionMin`, `hora`, `comentarios`).

### Boundary

- [ ] Runtime depends only on `PersistencePort`.
- [ ] Local adapter implements `save/load` with no UI dependency.
- [ ] Response contract normalizes legacy shape and rebuild shape.

### Runtime/UI

- [ ] `confirmSave()` transitions `validation -> completed` on success.
- [ ] Save flow passes through a real intermediate `saving` state.
- [ ] `quotationId` is visible after save.
- [ ] `loadQuotation(id)` path exists and returns normalized payload.
- [ ] Load flow passes through a real intermediate `loadingQuotation` state.

---

Generated from `raw/docs_cotizador/plan/U-1-save/objectives.md`.