---
identity:
  node_id: "doc:wiki/drafts/consolidated_library_decisions.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

| ID | Decision | Recommendation | Switch Trigger |

## Details

| ID | Decision | Recommendation | Switch Trigger |
|---|---|---|---|
| LIB-STATE-01 | State management | zustand | N/A — committed |
| LIB-LAYOUT-01 | Layout engine | elkjs | N/A — committed, replaces dagre |
| LIB-DOCK-01 | Dockable panels | FlexLayout-react | CSS impossible to align with MD3 |
| LIB-FORMS-01 | Schema-driven forms | RJSF (@rjsf/core) | Custom widget API too limited |
| LIB-TREE-01 | Explorer tree | react-arborist | Sync contract impossible |
| LIB-NEO4J-01 | Graph database driver | neo4j-driver | N/A — official driver |
| LIB-TEST-01 | Unit/component testing | Vitest + @testing-library/react | N/A — committed |
| LIB-E2E-01 | Integration testing | Playwright | N/A — already in use |
| LIB-RICHTEXT-01 | Markdown editor | TBD (matrix in 03b) | — |
| LIB-CODE-01 | Code editor | CodeMirror 6 (recommended) | IDE-grade features justify Monaco |
| LIB-JSON-01 | JSON/YAML inspector | TBD (matrix in 03c) | — |
| LIB-TABLE-01 | Table editor | TanStack Table (recommended) | Spreadsheet-grade features justify AG Grid |
| LIB-IMAGE-01 | Image annotation | TBD (matrix in 03f) | — |

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.