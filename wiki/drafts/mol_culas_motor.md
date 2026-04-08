---
identity:
  node_id: "doc:wiki/drafts/mol_culas_motor.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/00_stack.md", relation_type: "documents"}
---

| Molécula | Átomos | Librería motor | Por qué |

## Details

| Molécula | Átomos | Librería motor | Por qué |
|----------|--------|---------------|---------|
| `<SplitPane>` | — | `react-resizable-panels` | Del equipo core de React. Maneja divisores arrastrables, snap y collapse con Tailwind sin escribir cálculos de mouse. |
| `<IntelligentEditor>` | `<Tag>` `<Badge>` | `@uiw/react-codemirror` | Wrapper limpio de CodeMirror 6. Trae folding de JSON/MD, temas oscuros y sistema de decoraciones (tags) listo para usar. Reemplaza Slate.js. |
| `<GraphCanvas>` | `<Badge>` `<Icon>` | `@xyflow/react` + `dagre` | Ya en el proyecto. `dagre` calcula el layout jerárquico automático — los nodos no nacen amontonados. |
| `<EvidenceBankSidebar>` | `<Badge>` `<Icon>` | `@dnd-kit/core` | Estándar moderno para D&D en React. Permite arrastrar tarjetas del sidebar al canvas del grafo sin pelear con la API nativa de HTML5. |
| `<PortfolioTable>` | `<Badge>` `<Icon>` | `@tanstack/react-table` (opcional) | Si la tabla crece, maneja ordenamiento, filtros y estados sin programar la lógica de arrays a mano. |
| `<FileTree>` | `<Icon>` | Nativo o `react-folder-tree` | Un componente recursivo en React suele bastar. Librería solo si la complejidad lo justifica. |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/00_stack.md`.