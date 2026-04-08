---
identity:
  node_id: "doc:wiki/drafts/pantalla_4_select_client.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+----------------------------------------------------------------+
| Seleccionar Cliente                               [Cerrar]      |
|----------------------------------------------------------------|
| Buscar: [____________________________]                         |
|                                                                |
| Cliente A  RUT  correo                        [Seleccionar]    |
| Cliente B  RUT  correo                        [Seleccionar]    |
|                                                                |
| [ Crear cliente nuevo ]                                        |
+----------------------------------------------------------------+
```

- Estado: `CLIENT_SELECTION`
- Objetivo: elegir cliente existente.
- Eventos:
  - `SEARCH_CLIENT` (mismo estado)
  - `SELECT_CLIENT` -> `QUOTATION_EDITING`
  - `GO_NEW_CLIENT` -> `CLIENT_CREATION`
  - `CLOSE` -> `HOME` (si no hay cliente) o `QUOTATION_EDITING` (si ya existe cliente activo)

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.