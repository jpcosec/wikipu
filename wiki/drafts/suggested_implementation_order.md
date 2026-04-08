---
identity:
  node_id: "doc:wiki/drafts/suggested_implementation_order.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md", relation_type: "documents"}
---

1. Copy `mastery-scale.ts` → `features/base-cv/lib/`

## Details

1. Copy `mastery-scale.ts` → `features/base-cv/lib/`
2. Add `GroupNode.tsx` with collapsible logic
3. Upgrade `SkillNode.tsx` → mastery-colored ball with `SkillBallNode` shape
4. Add `ProxyEdge.tsx`
5. Upgrade `CvGraphCanvas.tsx` — group-based layout + proxy edges + drag reorder + `onConnect`
6. Upgrade `EntryNode.tsx` — inline expand panel with descriptions
7. Add `SkillPalette.tsx` — sidebar skill panel when entry focused
8. Extend `NodeInspector.tsx` — skill mastery editor + group reorder panel
9. Extend `BaseCvEditor.tsx` — add all new state + handlers
10. Wire "Add entry" / "Add skill" / "Add description" through group/entry node buttons

Generated from `raw/docs_postulador_langgraph/plan/01_ui/cv_graph_feature_merge.md`.