---
identity:
  node_id: "doc:wiki/drafts/view_1_graph_explorer.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md", relation_type: "documents"}
---

**Route**: `/jobs/:source/:jobId` + view-1 tab

## Details

**Route**: `/jobs/:source/:jobId` + view-1 tab
**Current component**: `ViewOneGraphExplorer.tsx`
**Sample reference**: `matching.html` (right panel) + `matching2.html`

### What exists today

- `GraphCanvas` renders match graph nodes + edges (requirement → evidence nodes)
- Edge labels show `MATCHED_BY` + score
- Match reasoning displayed as text rows below graph
- Data loaded via `getViewOnePayload()`

### Gaps vs. sample

| Gap | Description |
|---|---|
| Profile evidence bank panel | Sample has left sidebar listing all profile evidence entries (skills, projects, education) with status chips. Current implementation shows no evidence bank. |
| Match quality indicators | Sample shows color-coded quality (green/amber/red) per match edge. Current shows raw score only. |
| Requirement coverage bar | Sample shows a "coverage" progress indicator per requirement (e.g., "3/5 matched"). Not implemented. |
| Evidence source chips | Sample shows provenance chips per evidence node (e.g., "CV:project:Pub 3"). Not implemented. |
| Edge interactivity | Sample edges are clickable for detailed reasoning. Current edges are display-only. |
| Candidate profile summary | Sample has a compact profile card (photo, name, key stats) at top-left. Not implemented. |

---

Generated from `raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md`.