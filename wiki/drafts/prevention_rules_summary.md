---
identity:
  node_id: "doc:wiki/drafts/prevention_rules_summary.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

| Mode | Can write to code? | Can write to docs/runtime? | Can write to plan/? | Use Tool | Docs required? |

## Details

| Mode | Can write to code? | Can write to docs/runtime? | Can write to plan/? | Use Tool | Docs required? |
|------|-------------------|---------------------------|-------------------|----------|----------------|
| sync | NO | YES (overwrite) | NO | `sync_code_to_docs()` | YES |
| implement | YES | YES (promote) | NO (auto-delete) | `implement_plan()` | YES |
| design | NO | NO | YES (create) | `draft_plan()` | N/A |
| hotfix | YES | YES (update) | NO | `hotfix()` | **YES** (use `skip_docs` only in emergencies) |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.