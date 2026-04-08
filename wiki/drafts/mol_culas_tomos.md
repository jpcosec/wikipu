---
identity:
  node_id: "doc:wiki/drafts/mol_culas_tomos.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_component_map.md", relation_type: "documents"}
---

| Molécula | Átomos que consume | Rol de cada átomo |

## Details

| Molécula | Átomos que consume | Rol de cada átomo |
|----------|--------------------|-------------------|
| `<IntelligentEditor>` | `<Tag>` `<Badge>` `<Icon>` | `<Tag>` resalta spans en el texto. `<Badge>` aparece en el hover card. |
| `<GraphCanvas>` | `<Badge>` `<Icon>` | `<Badge>` muestra scores en los edges. `<Icon>` en los nodos. |
| `<PortfolioTable>` | `<Badge>` `<Icon>` | `<Badge status="verified\|pending">` para estado del job. |
| `<HitlCtaBanner>` | `<Button>` `<Icon>` | Botón gigante `variant="primary"` para ir al review. |
| `<RequirementList>` | `<Badge>` `<Button>` `<Icon>` | `<Badge>` para prioridad (must/nice). `<Button variant="ghost">` para borrar. |
| `<EvidenceBankSidebar>` | `<Badge>` `<Icon>` | `<Badge>` para categoría (skill/project). `<Icon name="drag_indicator">`. |
| `<FileTree>` | `<Icon>` | `<Icon>` dinámico según extensión (`.json`, `.md`, carpeta). |
| `<ControlPanel>` (todos) | `<Button>` `<Spinner>` `<Kbd>` | `<Button>` para commit/guardar. `<Spinner>` mientras guarda. `<Kbd>` para atajos. |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_component_map.md`.