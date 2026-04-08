---
identity:
  node_id: "doc:wiki/drafts/field_guide.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_backend.md", relation_type: "documents"}
---

| Field | Required | Description |

## Details

| Field | Required | Description |
|-------|----------|-------------|
| Type | Yes | backend (LangGraph), api (FastAPI), pipeline (edges), core (deterministic) |
| Domain | Yes | Which technical domain this belongs to |
| Stage | Yes | Pipeline stage or "cross-cutting" |
| State Contract | Yes | How state.json changes |
| Core Functions | If applicable | Which deterministic functions are affected |
| Node Implementation | If applicable | LangGraph node details |
| HITL | No | Whether this requires human review gate |
| API Endpoints | If applicable | FastAPI router changes |
| File Changes | Yes | Complete list of files to create/modify |
| Dependencies | Yes | What blocks this |
| Testing | Yes | How to verify |
| Rollback | Yes | How to undo |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_backend.md`.