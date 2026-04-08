---
identity:
  node_id: "doc:wiki/drafts/overview_the_4_flows.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

| Flow | Direction | Use Case | Modifies |

## Details

| Flow | Direction | Use Case | Modifies |
|------|-----------|----------|----------|
| **Sync** | Code → Docs | Docs became stale after code changes | docs/ only |
| **Implement** | Plan → Code → Docs | Execute an existing design | code + docs |
| **Design** | Runtime → Plan | Propose new architecture | plan/ only |
| **Hotfix** | Code → Code | Fix bug, respect contracts | code + docs |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.