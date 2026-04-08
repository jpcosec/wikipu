---
identity:
  node_id: "doc:wiki/drafts/pantalla_8_print_opcional_como_pantalla.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+----------------------------------------------------------------------------------+
| Print Preview                                              [Imprimir] [Cerrar]   |
|----------------------------------------------------------------------------------|
| Documento imprimible (cliente, items, totales)                                  |
+----------------------------------------------------------------------------------+
```

- Estado: `PRINT_PREVIEW` (opcional)
- Objetivo: confirmar salida de impresion/PDF.
- Eventos:
  - `CONFIRM_PRINT` (accion)
  - `SAVE_AFTER_PRINT` -> `SAVE_EXECUTED`
  - `CLOSE_PRINT` -> `QUOTATION_VALIDATING`

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.