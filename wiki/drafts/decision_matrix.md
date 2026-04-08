---
identity:
  node_id: "doc:wiki/drafts/decision_matrix.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md", relation_type: "documents"}
---

```

## Details

```
Is there a bug to fix?
├─ YES → hotfix (Template 4)
│        └─ Call hotfix(domain, stage, fixed_code, updated_docs)
│            → or hotfix(domain, stage, fixed_code, {}, skip_docs=True) for emergency
└─ NO
  ├─ Is there a design document in plan/?
  │   ├─ YES → implement (Template 2)
  │   │        └─ Call implement_plan(domain, stage, plan_doc, generated_code, generated_docs)
  │   └─ NO
  │       ├─ Do you want to propose something new?
  │       │   ├─ YES → design (Template 3)
  │       │   │        └─ Call draft_plan(domain, stage, filename, content)
  │       │   └─ NO
  │       │       └─ Did code change without updating docs?
  │       │           ├─ YES → sync (Template 1)
  │       │           │        └─ Call sync_code_to_docs(domain, stage, generated_docs)
  │       │           └─ NO → STOP (nothing to do)
```

### Debt Resolution

After `skip_docs=True` hotfix, you MUST call within 24 hours:
```
sync_code_to_docs(domain='<same>', stage='<same>', generated_docs={...})
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/13_agent_intervention_templates.md`.