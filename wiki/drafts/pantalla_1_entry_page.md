---
identity:
  node_id: "doc:wiki/drafts/pantalla_1_entry_page.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+------------------------------------------------------+
| Cotizador Lodge                                      |
|------------------------------------------------------|
| [ Nueva cotizacion ]                                 |
| [ Cargar cotizacion previa ]                         |
| [ Database Browser ]                                 |
+------------------------------------------------------+
```

- Estado: `HOME`
- Objetivo: entrada unica a los tres caminos funcionales.
- Entrada: boot o reset.
- Salida:
  - `CLICK_DATABASE_BROWSER` -> `DB_BROWSING`
  - `CLICK_NEW_QUOTATION` -> `NEW_QUOTATION_INIT`
  - `CLICK_LOAD_PREVIOUS` -> `LOAD_PREVIOUS`

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.