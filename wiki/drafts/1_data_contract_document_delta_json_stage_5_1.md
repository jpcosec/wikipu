---
identity:
  node_id: "doc:wiki/drafts/1_data_contract_document_delta_json_stage_5_1.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/09_autopostulation_deployment.md", relation_type: "documents"}
---

The "Delta" is a set of instructions telling the drafting engine how to adapt Base Documents (Master Docs) for the specific job posting.

## Details

The "Delta" is a set of instructions telling the drafting engine how to adapt Base Documents (Master Docs) for the specific job posting.

```json
{
  "master_doc_id": "string",       // Reference to original document (e.g., cv_academico_v2.md)
  "puntos_narrativos": [           // "Hooks" or motivations entered in UI
    "string"
  ],
  "transformaciones": [
    {
      "target": "string",          // Component to change (e.g., summary, experience_01, cover_letter_body)
      "op": "REPLACE | ENHANCE | HIDE",
      "evidencia_ref": ["string"], // Evidence Bank IDs
      "estilo_override": "string"  // Tone instructions from historical ReviewNodes
    }
  ]
}
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/09_autopostulation_deployment.md`.