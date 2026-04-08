---
identity:
  node_id: "doc:wiki/drafts/pantalla_3_new_quotation_launcher.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+------------------------------------------------------+
| Nueva Cotizacion                                     |
|------------------------------------------------------|
| [ Seleccionar cliente existente ]                    |
| [ Crear cliente nuevo ]                              |
| [ Volver ]                                           |
+------------------------------------------------------+
```

- Estado: `NEW_QUOTATION_INIT`
- Objetivo: decidir origen de cliente antes de editar la cotizacion.
- Eventos:
  - `GO_SELECT_CLIENT` -> `CLIENT_SELECTION`
  - `GO_NEW_CLIENT` -> `CLIENT_CREATION`
  - `CANCEL_TO_HOME` -> `HOME`
- Regla: no pasar a `QUOTATION_EDITING` sin cliente.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.