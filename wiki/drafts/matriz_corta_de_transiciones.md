---
identity:
  node_id: "doc:wiki/drafts/matriz_corta_de_transiciones.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md", relation_type: "documents"}
---

| Desde | Evento | Hacia |

## Details

| Desde | Evento | Hacia |
|---|---|---|
| `HOME` | `CLICK_DATABASE_BROWSER` | `DB_BROWSING` |
| `HOME` | `CLICK_NEW_QUOTATION` | `NEW_QUOTATION_INIT` |
| `HOME` | `CLICK_LOAD_PREVIOUS` | `LOAD_PREVIOUS` |
| `NEW_QUOTATION_INIT` | `GO_SELECT_CLIENT` | `CLIENT_SELECTION` |
| `NEW_QUOTATION_INIT` | `GO_NEW_CLIENT` | `CLIENT_CREATION` |
| `CLIENT_SELECTION` | `SELECT_CLIENT` | `QUOTATION_EDITING` |
| `CLIENT_SELECTION` | `GO_NEW_CLIENT` | `CLIENT_CREATION` |
| `CLIENT_CREATION` | `SUBMIT_NEW_CLIENT` | `QUOTATION_EDITING` |
| `LOAD_PREVIOUS` | `OPEN_QUOTATION` | `QUOTATION_EDITING` |
| `QUOTATION_EDITING` | `GO_VALIDATE` | `QUOTATION_VALIDATING` |
| `QUOTATION_VALIDATING` | `BACK_TO_QUOTATION` | `QUOTATION_EDITING` |
| `QUOTATION_VALIDATING` | `PRINT_QUOTATION` | `PRINT_PREVIEW` |
| `PRINT_PREVIEW` | `SAVE_AFTER_PRINT` | `SAVE_EXECUTED` |

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-screen-by-screen-spec.md`.