---
identity:
  node_id: "doc:wiki/drafts/known_gaps_workarounds_in_place.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/implementation_status.md", relation_type: "documents"}
---

| Gap | Workaround | Risk |

## Details

| Gap | Workaround | Risk |
|-----|------------|------|
| No Strategy gate | UI saves to `nodes/strategy/delta.json` manually | Data may be overwritten by future backend activation |
| No Drafting gate | UI overwrites `nodes/drafting/*.md` before render | Race condition if LangGraph runs simultaneously |
| No global Feedback Loop | UI writes `nodes/review/` for future aggregator | No immediate learning benefit |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/implementation_status.md`.