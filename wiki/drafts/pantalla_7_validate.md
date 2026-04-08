---
identity:
  node_id: "doc:wiki/drafts/pantalla_7_validate.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

```text

## Details

```text
+----------------------------------------------------------------------------------+
| Validacion Cotizacion                               [Volver a Cotizacion]        |
|----------------------------------------------------------------------------------|
| Cliente | Fecha | Pax                                                         |
| Tabla resumen por dia/item                                                    |
| Subtotal | IVA | Total                                                        |
|----------------------------------------------------------------------------------|
| [Imprimir]                                                    [Guardar]         |
+----------------------------------------------------------------------------------+
```

- Estado: `QUOTATION_VALIDATING`
- Objetivo: revision final previa a impresion y guardado.
- Eventos:
  - `BACK_TO_QUOTATION` -> `QUOTATION_EDITING`
  - `PRINT_QUOTATION` -> `PRINT_PREVIEW` (si existe como estado)
  - `SAVE_QUOTATION` -> `SAVE_EXECUTED`
- Regla: no recalcular negocio aqui; solo proyeccion final.

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.