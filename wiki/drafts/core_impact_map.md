---
identity:
  node_id: "doc:wiki/drafts/core_impact_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/05_validation_and_test_impact_map.md", relation_type: "documents"}
---

### Editing `NodeEditorSandboxPage.tsx`

## Details

### Editing `NodeEditorSandboxPage.tsx`

Likely impacts:

- sandbox interaction behavior
- local history
- layout actions
- keyboard shortcuts

Usually does not directly impact:

- backend persistence
- CV graph payloads

### Editing `CvGraphEditorPage.tsx`

Likely impacts:

- saved CV graph shape
- container/group behavior
- proxy edges
- API roundtrip correctness

### Editing `RichTextPane.tsx`

Likely impacts:

- annotation creation/editing
- text anchor identity
- doc-to-graph link behavior

### Editing API payloads / models

Likely impacts:

- frontend fetch/save
- persistence compatibility
- existing saved data

Generated from `raw/docs_postulador_ui/plan/future/05_validation_and_test_impact_map.md`.