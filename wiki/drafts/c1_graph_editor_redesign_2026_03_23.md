---
identity:
  node_id: "doc:wiki/drafts/c1_graph_editor_redesign_2026_03_23.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md", relation_type: "documents"}
---

### C1-A: KnowledgeGraph Terran Theme Fix + Sub-flows + Document Template

## Details

### C1-A: KnowledgeGraph Terran Theme Fix + Sub-flows + Document Template
- Replaced light pastel CATEGORY_COLORS with Terran dark border+bg pairs
- Fixed 5 hardcoded white/light `.ne-*` CSS classes + ReactFlow node background override
- Added `GroupNode` (resizable titled frame, dashed border, category colors)
- Added `SubFlowEdge` (resolves absolute positions from ReactFlow store)
- Added `document`, `section`, `entry` to CATEGORY_OPTIONS and NODE_TEMPLATES
- Document template creates 3-level Document→Section(×2)→Entry nested structure on canvas drop
- Added `meta?: unknown` passthrough to `SimpleNodeData` for round-trip preservation
- Added `initialNodes`, `initialEdges`, `onSave`, `onChange` props to `KnowledgeGraph`

### C1-B: CV Editor → KnowledgeGraph
- Created `features/base-cv/lib/cvToGraph.ts` adapter (cvProfileToGraph / graphToCvProfile)
- `BaseCvEditor` replaced with thin wrapper using KnowledgeGraph + adapter

### C1-C: Match View → KnowledgeGraph
- Added `category?: string` to `GraphNode` in api.types.ts
- Updated match fixtures to include category on all nodes
- Created `features/job-pipeline/lib/matchToGraph.ts` (matchPayloadToGraph / graphToMatchEdits / MatchEdits)
- Created `UnmappedSkillsPanel` — collapsible list of unconnected profile nodes
- `Match.tsx` replaced with KnowledgeGraph in 2-column grouped layout + UnmappedSkillsPanel + MatchDecisionModal
```

- [ ] **Step 4: Final commit**

```bash
git add plan/index_checklist.md changelog.md
git commit -m "docs: update changelog and checklist for C1 graph editor redesign"
```

Generated from `raw/docs_postulador_ui/plan/01_ui/plans/2026-03-23-c1-graph-editor-redesign.md`.