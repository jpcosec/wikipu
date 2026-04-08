---
identity:
  node_id: "doc:wiki/drafts/what_is_configurable_vs_hardcoded.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_customization_and_architecture.md", relation_type: "documents"}
---

### Frontend node editor sandbox

## Details

### Frontend node editor sandbox

Currently hardcoded in `NodeEditorSandboxPage.tsx`:

- Category palette and colors: `CATEGORY_OPTIONS`, `CATEGORY_COLORS`
- Drag templates and defaults: `NODE_TEMPLATES`
- Initial mock graph: `buildInitialGraph`
- Attribute type options in modal forms: `ATTRIBUTE_TYPES`

Configurable at runtime (already supported in UI behavior):

- Relation visibility toggles per active relation type
- Node filtering by name + property key/value
- Focus isolation toggle (`Hide non-neighbors`)
- Deterministic layout commands (`Layout all`, `Layout focus`, `Layout custom`)

### Backend CV graph categories

- Categories are mostly data-driven from profile content and normalized by builder logic (for example `_normalize_skill_category` in `read_models.py`).
- There is no dedicated external config file for category taxonomy yet; behavior is encoded in profile data + normalization code.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_customization_and_architecture.md`.