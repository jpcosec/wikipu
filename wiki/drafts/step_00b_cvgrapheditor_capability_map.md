---
identity:
  node_id: "doc:wiki/drafts/step_00b_cvgrapheditor_capability_map.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md", relation_type: "documents"}
---

### 1. Architecture Logic

## Details

### 1. Architecture Logic

Before building: map every CvGraphEditor feature to where it lives in the new architecture. This is the migration contract — nothing gets lost, nothing gets ported blindly.

| CvGraphEditor Feature | Step | How It Maps |
|---|---|---|
| Group nodes (per-category containers) | 01b | Container node type with container_config. Categories are metadata, not hardcoded groups. |
| Entry nodes (category, essential, descriptions) | 01b | Structured entry node type in registry. Payload carries category, essential flag, description array. |
| Skill ball nodes (mastery, shape, color) | 01b | Skill node type in registry. Mastery scale in payload. Visual style derived from mastery + category via schema. |
| Expand/collapse containers | 02 | Container collapse/expand with summary + child count. Generic, not CV-specific. |
| Proxy edges when collapsed | 02 | Proxy edge rendering as container behavior. Dashed style, deduplication. |
| Drag reorder within group | 02 | Container child reorder via order array. Semantic action, undoable. |
| Drag across groups | 02 | Cross-container move. Semantic action, undoable. |
| Drag connect entry→skill | 01 | Standard edge creation. "demonstrates" is a relation type. |
| Entry expand panel (right slide-in) | 01b | edit_in_context renderer mode for entry node type. |
| Skill palette sidebar | 02a / 00e | Sidebar panel extension showing available nodes of a type. |
| Mastery scale (5-level) | 01b | Payload metadata. Rendering via schema visual config + CSS theme. |
| API persistence (GET/PUT) | 01 | Pluggable persistence API. CV profile graph is one adapter. |
| Dagre layout | 01a | Replaced by elkjs. |
| Dynamic container height | 01a | elkjs compound layout computes bounds from children. |
| Dirty detection + save/discard | 01c | Action-count dirty detection. Save/discard in toolbar. |

### 2. Objectives

1. Every CvGraphEditor feature has a named home in the new architecture
2. No feature is lost — this table is the verification checklist
3. When the NodeEditor can reproduce all rows, CvGraphEditor is deleted

### 3. Don'ts

- **Don't port CvGraphEditor code directly.** Features are requirements, not implementations.
- **Don't keep CvGraphEditor alive after migration.** Once all rows pass, delete it.
- **Don't add CV-specific logic to the generic editor.** Entry, skill, mastery are node types and payload shapes. The editor is type-agnostic.

### 4. Known Gaps & Open Questions

None — this step is purely a mapping document.

### 5. Library Decision Matrix

N/A — no libraries needed for this step.

### 6. Test Plan

N/A — this step produces a document, not code.

### 7. Review Checklist

- [ ] Every CvGraphEditor feature is listed with a target step
- [ ] No feature is marked "not needed" without explicit justification
- [ ] The mapping table is referenced by all downstream steps

---

Generated from `raw/docs_postulador_ui/plan/future/2026-03-20-ui-plan-review-design.md`.