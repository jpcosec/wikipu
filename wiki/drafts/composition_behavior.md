---
identity:
  node_id: "doc:wiki/drafts/composition_behavior.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

- A node can contain nodes of same or different categories.

## Details

- A node can contain nodes of same or different categories.
- Container nodes (for example CV sections like Education) start collapsed and show summary info.
- Internal composition can be inspected in two ways:
  - hover preview
  - explicit expand/collapse
- Expanded view must keep child items clearly linked to the parent container.
- Collapsed children are not directly editable until expanded or opened through container navigation.
- Relations to collapsed children are hidden by default and shown when the container is expanded.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.