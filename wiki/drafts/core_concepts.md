---
identity:
  node_id: "doc:wiki/drafts/core_concepts.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md", relation_type: "documents"}
---

The schema answers five questions for any document:

## Details

The schema answers five questions for any document:

| Question | Schema key | Graph effect |
|----------|-----------|--------------|
| What kind of document is this? | `document` block | Page title, domain selector label |
| What is a node? | `render_as: "node"` | Rendered as a standalone ReactFlow node |
| What is a subflow (group of nodes)? | `render_as: "group"` | Rendered as a ReactFlow group node with children inside (subflow) |
| What is an attribute? | `render_as: "attribute"` | Shown as a property row in the node inspector, not as a separate node |
| What connects to what? | `edge_types` | Rendered as ReactFlow edges with labels |
| What does colour mean? | `color_token` + `visual_encoding` | Node border/bg color, edge stroke color |

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/D1_schema_explorer.md`.