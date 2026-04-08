---
identity:
  node_id: "doc:wiki/drafts/pantalla_6_quotation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+------------------------------------------------------------------------------------------------+
| Cliente X | Fecha Inicio | Dias | Pax Global                             [Guardar] [Validar]  |
|------------------------------------------------------------------------------------------------|
| Catalogo (izquierda)                              | Basket por Dia (derecha)                    |
| Buscar categoria/item                              | Tabs: Dia 1 Dia 2 Dia 3                     |
| Categoria A -> Item 1 [Agregar]                   | Lineas del dia: item, pax, cant, hora, $     |
| Categoria B -> Item 2 [Agregar]                   | [editar override] [mover] [duplicar]         |
|                                                    | Subtotal / Total                              |
+------------------------------------------------------------------------------------------------+
```

- Estado: `QUOTATION_EDITING`
- Objetivo: construir la cotizacion por dias y entradas.
- Eventos:
  - `SET_SETTINGS`
  - `SHIP_ITEM`
  - `SET_ENTRY_OVERRIDE`, `CLEAR_OVERRIDE`, `RESET_OVERRIDES`
  - `MOVE_ENTRY`, `COPY_ENTRY`, `DUPLICATE_ENTRY`
  - `SELECT_DAY`
  - `SAVE_QUOTATION`
  - `GO_VALIDATE` -> `QUOTATION_VALIDATING`
- Guardas:
  - para editar/guardar/validar debe existir cliente seleccionado
  - `GO_VALIDATE` requiere al menos una entrada en basket

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.