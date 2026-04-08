---
identity:
  node_id: "doc:wiki/drafts/component_map_changes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md", relation_type: "documents"}
---

| File | Change |

## Details

| File | Change |
|------|--------|
| `styles.css` | Fix 5 hardcoded light `.ne-*` values + `.react-flow__node` override |
| `KnowledgeGraph.tsx` | New `CATEGORY_COLORS`, add `GroupNode`, `SubFlowEdge`, Document template, `onSave` prop |
| `features/base-cv/lib/cvToGraph.ts` | New — adapter functions |
| `pages/global/BaseCvEditor.tsx` | Replaced — thin wrapper |
| `types/api.types.ts` | Add `category?: string` to `GraphNode` |
| `mock/fixtures/artifacts_match_*.json` | Add `category` to requirement/profile nodes |
| `features/job-pipeline/lib/matchToGraph.ts` | New — adapter + `MatchEdits` type |
| `pages/job/Match.tsx` | Use KnowledgeGraph + `UnmappedSkillsPanel` + keep `MatchDecisionModal` |

Generated from `raw/docs_postulador_ui/plan/01_ui/specs/C1_graph_editor_redesign.md`.