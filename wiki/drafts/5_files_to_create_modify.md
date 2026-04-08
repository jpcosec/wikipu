---
identity:
  node_id: "doc:wiki/drafts/5_files_to_create_modify.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/specs/C1_cv_graph_editor.md", relation_type: "documents"}
---

```

## Details

```
src/features/base-cv/
  lib/
    mastery-scale.ts          COPY verbatim from dev sandbox/lib/mastery-scale.ts
  components/
    GroupNode.tsx             NEW: collapsible category container node
    SkillBallNode.tsx         NEW: mastery-colored skill ball (replaces SkillNode.tsx)
    ProxyEdge.tsx             COPY verbatim from dev sandbox/components/cv-graph/ProxyEdge.tsx
    EntryNode.tsx             EXTEND: add inline expand panel, description bullets
    NodeInspector.tsx         EXTEND: add skill mastery editor + group reorder section
    SkillPalette.tsx          NEW: right sidebar — related/unrelated split + add skill
    CvGraphCanvas.tsx         REWRITE: GroupNode-based layout, proxy edges, drag handlers
    types.ts                  NEW: EntryNodeData, SkillNodeData, GroupNodeData (from dev)
src/pages/global/
  BaseCvEditor.tsx            EXTEND: 5 new state fields + 8 new handlers
```

---

Generated from `raw/docs_postulador_langgraph/plan/01_ui/specs/C1_cv_graph_editor.md`.