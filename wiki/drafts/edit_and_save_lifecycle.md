---
identity:
  node_id: "doc:wiki/drafts/edit_and_save_lifecycle.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

- Any node/relation field update marks the workspace as `dirty`.

## Details

- Any node/relation field update marks the workspace as `dirty`.
- Save is explicit (user-triggered), not implicit.
- Save persists:
  - node properties and extensible attributes
  - relation type and relation attributes
  - relation endpoints after reconnect operations
  - graph layout positions for free nodes
  - expanded/collapsed composition state
  - active mapping configuration and visibility controls for the workspace
- Cancel in edit mode closes the editor panel and keeps changes only if already saved.
- Discard reverts unsaved edits for the active node/relation and clears `dirty` if no other unsaved changes exist.
- Validation errors must block save and show the failing fields.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.