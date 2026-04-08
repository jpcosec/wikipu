---
identity:
  node_id: "doc:wiki/drafts/pantalla_2_database_browser.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+----------------------------------------------------------------------------------+
| Database Browser                                              [Back to Home]     |
|----------------------------------------------------------------------------------|
| Table Selector                  | Table Grid                                    |
|---------------------------------|-----------------------------------------------|
| CLIENTES                        | rows... cols...                                |
| ITEM_CATALOGO                   |                                                |
| CATEGORIAS                      | [Add Row] [Edit Cell] [Save] [Cancel]         |
| REGLAS                          |                                                |
+----------------------------------------------------------------------------------+
```

- Estado: `DB_BROWSING`
- Objetivo: exploracion y edicion de tablas.
- Subpantalla interna: `table_selector`.
- Eventos:
  - `SELECT_TABLE` (no cambia estado global)
  - `EDIT_CELL`, `ADD_ROW`, `SAVE_ROW`, `CANCEL_EDIT`
  - `BACK_HOME` -> `HOME`
- Regla: no persistir si validacion de fila falla.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.