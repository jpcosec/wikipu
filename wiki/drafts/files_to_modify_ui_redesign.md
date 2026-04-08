---
identity:
  node_id: "doc:wiki/drafts/files_to_modify_ui_redesign.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/01_ui/match_node_editor_merge.md", relation_type: "documents"}
---

| File | Change |

## Details

| File | Change |
|---|---|
| `pages/job/Match.tsx` | Add `manualEdgesHistory`, search state, focusedNodeId, extended keyDown handler, shortcuts modal trigger |
| `features/job-pipeline/components/MatchControlPanel.tsx` | Replace raw JSON dump with structured field editor for selected node |
| `features/job-pipeline/components/MatchGraphCanvas.tsx` | Accept `searchQuery` + `focusedNodeId` props → pass as node data for highlight styling |
| `features/job-pipeline/components/ProfileNode.tsx` | Accept `dimmed` / `highlighted` props |
| `features/job-pipeline/components/RequirementNode.tsx` | Accept `dimmed` / `highlighted` + editable `priority` / `text` |

Generated from `raw/docs_postulador_langgraph/plan/01_ui/match_node_editor_merge.md`.