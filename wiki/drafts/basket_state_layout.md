---
identity:
  node_id: "doc:wiki/drafts/basket_state_layout.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-04-legacy-quotation-ui-blueprint.md", relation_type: "documents"}
---

```text

## Details

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ RIGHT AREA HEADER (Config Panel)                                            │
│ [Cargar] [Guardar] [Copiar Día] [PDF] [Datos]                               │
│ Inicio [date]   Duración [n]   Pax Global [n]                               │
├──────────────────────────────────────────────────────────────────────────────┤
│ Day Tabs:  [Día 1] [Día 2] [Día 3] ...                                      │
├──────────────────────────────────────────────────────────────────────────────┤
│ Timeline (accordion list of basket lines for selected day)                  │
│  [Hora] Item Name  $Total • pax                           [expand/collapse] │
│   - Pax [n], Unidades [n], Duración [n]                                     │
│   - Comentario [textarea]                                                    │
│   - [Eliminar] [Copiar al siguiente día] [Duplicar]                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Bottom Summary Bar: Neto $...   Total $...                                  │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────── LEFT SIDEBAR ──────────────────────────────────┐
│ SF Lodge / Cotizador                                                         │
│ Cliente: [Seleccionar/Crear] or selected client + [Cambiar]                 │
│ Buscar item [text]                                                           │
│ Category accordion list                                                      │
│   - Mini card per item (name + base price + add icon)                       │
└───────────────────────────────────────────────────────────────────────────────┘
```

Generated from `raw/docs_cotizador/docs/plans/2026-03-04-legacy-quotation-ui-blueprint.md`.