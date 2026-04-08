---
identity:
  node_id: "doc:wiki/drafts/pantalla_9_load_previous_quotation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+--------------------------------------------------------------------+
| Cargar Cotizacion Previa                              [Cerrar]      |
|--------------------------------------------------------------------|
| Buscar por cliente/rut/folio: [____________________]               |
|                                                                    |
| Folio 1023 | Cliente A | Fecha | Estado              [Abrir]       |
| Folio 1024 | Cliente B | Fecha | Estado              [Abrir]       |
+--------------------------------------------------------------------+
```

- Estado: `LOAD_PREVIOUS`
- Objetivo: buscar y abrir cotizacion existente.
- Eventos:
  - `SEARCH_QUOTATION`
  - `OPEN_QUOTATION` -> `QUOTATION_EDITING`
  - `CLOSE` -> `HOME`
- Regla: `OPEN_QUOTATION` debe hidratar cliente, settings, basket y contexto antes de mostrar edicion.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.