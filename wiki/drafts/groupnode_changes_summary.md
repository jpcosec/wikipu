---
identity:
  node_id: "doc:wiki/drafts/groupnode_changes_summary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/D2_group_node_collapse.md", relation_type: "documents"}
---

**Before:**

## Details

**Before:**
- Dashed border container, label above, no header, no interaction

**After:**
- `NodeToolbar` at top-left with ▶/▼ toggle (always visible)
- Label + child count badge inside the toolbar
- Collapsed state: group node shrinks to a compact card (`style.height` set to fixed small value), children hidden, proxy edges injected
- Expanded state: group node restores original `style`, children unhidden, proxy edges removed

---

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/D2_group_node_collapse.md`.