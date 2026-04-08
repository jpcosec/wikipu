---
identity:
  node_id: "doc:wiki/drafts/technology_stack.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

| Concern | Library | Status |

## Details

| Concern | Library | Status |
|---|---|---|
| Graph canvas | @xyflow/react (React Flow) | In use |
| Layout engine | elkjs | Committed, replaces dagre |
| State management | zustand | Committed |
| Dockable panels | flexlayout-react | Committed |
| Schema-driven forms | @rjsf/core + @rjsf/utils + custom theme | Committed |
| Extension registry | Custom (~300 lines) | To build |
| Explorer tree | react-arborist | Committed |
| Icons | Material Symbols Outlined | In mockups |
| CSS framework | Tailwind CSS + MD3 tokens as CSS vars | In use |
| Typography | Manrope (headlines) + Inter (body) | In mockups |
| Graph database | neo4j + neo4j-driver | Committed |
| Unit testing | Vitest | Committed |
| Component testing | @testing-library/react | Committed |
| Integration testing | Playwright | In use (partially) |
| Markdown editor | TBD (decision matrix in 03b) | Deferred |
| Code editor | CodeMirror 6 (recommended, matrix in 03e) | Deferred |
| JSON/YAML inspector | TBD (decision matrix in 03c) | Deferred |
| Table editor | TanStack Table (recommended, matrix in 03d) | Deferred |
| Image annotation | TBD (decision matrix in 03f) | Deferred |

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.