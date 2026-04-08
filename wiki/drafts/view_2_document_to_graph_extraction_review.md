---
identity:
  node_id: "doc:wiki/drafts/view_2_document_to_graph_extraction_review.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md", relation_type: "documents"}
---

**Route**: `/jobs/:source/:jobId` + view-2 tab

## Details

**Route**: `/jobs/:source/:jobId` + view-2 tab
**Current component**: `ViewTwoDocToGraph.tsx`
**Sample reference**: `extraction.html` + `matching.html` (left panel)

### What exists today

- Source markdown rendered as line-by-line buttons
- Highlighted lines for selected requirement's spans
- Line-level click selects linked requirement
- Requirement panel shows ID, priority, text, spans
- GraphCanvas shows source → requirements topology

### Gaps vs. sample

| Gap | Description |
|---|---|
| Difficulty rating | Sample shows a difficulty indicator (color dot) per requirement extracted from job text. |
| Requirement metadata | Sample shows `type` chip (skill/experience/certification) per requirement. Current shows only ID. |
| Confidence score | Sample shows per-requirement confidence (e.g., 0.87). Current has no confidence display. |
| Evidence linking | Sample's matching panel (right) shows requirement → evidence mapping with score. This is essentially View 1's domain. |
| Edit extraction inline | User cannot edit requirement text from this view — must go to node editor. Sample implies inline edit capability. |
| Batch approve/reject | Sample has bulk selection checkboxes for requirements. Not implemented. |
| Exact quote highlight | Sample highlights the exact character span in the source text, not just line-level. Current uses line-level spans. |

---

Generated from `raw/docs_postulador_langgraph/docs/ui/ui_view_spec.md`.