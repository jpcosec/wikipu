---
identity:
  node_id: "doc:wiki/drafts/clasificacion_de_nodos_actuales.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/ARCHITECTURE/app-flow-state-screen-foundation.md", relation_type: "documents"}
---

| Nodo | Tipo principal | Nota |

## Details

| Nodo | Tipo principal | Nota |
|---|---|---|
| `Entry page` | Pantalla | Inicio del flujo |
| `database_browser` | Pantalla | Modulo de navegacion de tablas |
| `table_selector` | Subpantalla/componente UI | Parte interna de `database_browser` |
| `New_quotation` | Evento/accion | Dispara inicio de nueva cotizacion |
| `load_previous_quotation` | Evento/accion | Carga cotizacion previa (puede abrir selector) |
| `select_client` | Pantalla/modal | Seleccion de cliente existente |
| `new_client` | Pantalla/modal | Alta de cliente nuevo |
| `quotation` | Pantalla | Edicion principal |
| `validate` | Pantalla | Revision previa a salida/finalizacion |
| `print` | Accion (o pantalla opcional) | Puede ser `PrintPreview` si se vuelve vista explicita |
| `save` | Accion | Persistencia de cotizacion |

---

Generated from `raw/docs_cotizador/docs/ARCHITECTURE/app-flow-state-screen-foundation.md`.