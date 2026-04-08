---
identity:
  node_id: "doc:wiki/drafts/pipeline_stages.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/implementation_status.md", relation_type: "documents"}
---

| Stage | Status | Notes |

## Details

| Stage | Status | Notes |
|-------|--------|-------|
| 1. Scrape | `implemented` | |
| 2. Translate | `implemented` | |
| 3. Extract | `partial` | Returns spans but doesn't pause for HITL gate |
| 4. Match | `implemented` | Full HITL gate via RoundManager |
| 5.1 Strategy | `blocked` | Nodes exist but bypassed (`PREP_MATCH_LINEAR_EDGES`) |
| 5.2 Drafting | `partial` | Generates `.md` but jumps to render without review |
| 6. Render | `implemented` | |
| 7. Package | `implemented` | |
| 8. Feedback Loop | `planned` | Aggregator not built; UI uses workaround |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/implementation_status.md`.