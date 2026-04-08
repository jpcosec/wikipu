---
identity:
  node_id: "doc:wiki/drafts/mapeo_de_nodos_pantalla_vs_estado_vs_evento.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

| Nodo | Clasificacion principal | Estado sugerido |

## Details

| Nodo | Clasificacion principal | Estado sugerido |
|---|---|---|
| `Entry page` | Pantalla | `HOME` |
| `database_browser` | Pantalla | `DB_BROWSING` |
| `table_selector` | Subpantalla/componente de UI | interno de `DB_BROWSING` |
| `New_quotation` | Evento de navegacion | `HOME -> NEW_QUOTATION_INIT` |
| `load_previous_quotation` | Evento de navegacion | `HOME -> LOAD_PREVIOUS` |
| `select_client` | Pantalla/modal | `CLIENT_SELECTION` |
| `new_client` | Pantalla/modal | `CLIENT_CREATION` |
| `quotation` | Pantalla | `QUOTATION_EDITING` |
| `validate` | Pantalla | `QUOTATION_VALIDATING` |
| `print` | Accion (o pantalla opcional) | `PRINT_PREVIEW` (opcional) |
| `save` | Accion/efecto | `SAVE_EXECUTED` (logico/transitorio) |

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.