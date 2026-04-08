---
identity:
  node_id: "doc:wiki/drafts/pantalla_5_new_client.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+----------------------------------------------------------------+
| Nuevo Cliente                                     [Cancelar]    |
|----------------------------------------------------------------|
| Empresa:   [____________________]                              |
| RUT:       [____________________]                              |
| Email:     [____________________]                              |
| Telefono:  [____________________]                              |
| Contacto:  [____________________]                              |
|                                                                |
| [ Guardar cliente ]                             [Volver]        |
+----------------------------------------------------------------+
```

- Estado: `CLIENT_CREATION`
- Objetivo: alta de cliente dentro del flujo.
- Eventos:
  - `SET_FIELD` (mismo estado)
  - `SUBMIT_NEW_CLIENT` -> `QUOTATION_EDITING` (cliente autoseleccionado)
  - `CANCEL` -> `CLIENT_SELECTION`
- Validacion minima sugerida: `empresa` y `rut` requeridos.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.