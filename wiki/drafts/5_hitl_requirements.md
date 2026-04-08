---
identity:
  node_id: "doc:wiki/drafts/5_hitl_requirements.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_backend.md", relation_type: "documents"}
---

Does this feature require human intervention?

## Details

Does this feature require human intervention?

| Gate | Required | Schema | UI Component |
|------|----------|--------|--------------|
| yes/no | yes/no | ReviewNode / Decision | component_name |

### If HITL Required

```json
// Required ReviewNode schema
{
  "etapa": "<stage>",
  "tipo": "CORRECTION | AUGMENTATION | STYLE | REJECTION",
  "index": "...",
  "comentario": "...",
  "valor_anterior": null,
  "valor_nuevo": {}
}
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/planning_template_backend.md`.