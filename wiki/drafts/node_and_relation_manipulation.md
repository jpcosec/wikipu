---
identity:
  node_id: "doc:wiki/drafts/node_and_relation_manipulation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

- Free (non-contained) nodes are draggable for manual arrangement.

## Details

- Free (non-contained) nodes are draggable for manual arrangement.
- Nodes expose handles for connecting relations.
- Unrelated nodes can be connected by dragging from sidebar sections into the canvas and linking.
- Relation creation/editing must support both:
  - simple un-attributed relations
  - attributed relations editable from edge selection
- Relation lifecycle actions:
  - create relation (drag handle)
  - inspect relation (click edge)
  - edit relation type and attributes
  - reconnect relation endpoint(s)
  - delete relation
- Node lifecycle actions:
  - create node
  - edit node
  - reposition free node
  - delete node (with explicit confirmation and relation impact warning)

Handle and edge UX baseline for this phase:

- handles are revealed on hover/selection to reduce visual clutter
- handles support multiple anchor zones (top/right/bottom/left)
- loose connection mode is acceptable for conceptual mapping phase
- edge anchoring should prefer shortest-angle geometry between nodes (floating-edge style behavior)

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.