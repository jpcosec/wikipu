---
identity:
  node_id: "doc:wiki/drafts/node_editor_page.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md", relation_type: "documents"}
---

**Route**: `/jobs/:source/:jobId/node-editor`

## Details

**Route**: `/jobs/:source/:jobId/node-editor`
**Current component**: `JobNodeEditorPage.tsx`
**Sample reference**: No dedicated sample; this is an internal tool

### What exists today

- ReactFlow graph visualization of extract_understand and match state
- Click node → path selected in sidebar JSON editor
- Save edited JSON back to `state.json`
- Two stage tabs: Extract and Match
- JSON path navigation with dot-notation

### Gaps vs. sample

| Gap | Description |
|---|---|
| Visual node type differentiation | Sample nodes have type-specific colors (requirement, constraint, risk). Current uses generic styling. |
| Edge labels in graph | Sample shows relationship labels on edges. Partial — edge labels shown but no path labels. |
| Search/filter nodes | No search by text content. |
| Batch path update | Can only edit one path at a time. |
| Undo/redo | No history. The sandbox NodeEditor has this — reuse that interaction. |
| Keyboard shortcuts | No shortcuts for save, navigate, collapse. |

---

Generated from `raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md`.