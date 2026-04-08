---
identity:
  node_id: "doc:wiki/drafts/2_contract_schema_document_delta_json.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/08_document_delta.md", relation_type: "documents"}
---

File generated at the end of Stage 5.1, input for final drafting.

## Details

File generated at the end of Stage 5.1, input for final drafting.

```json
{
  "documento_id": "string",        // Reference to Master Doc (e.g., master_cv_v2, standard_letter_en)
  "motivaciones_clave": [          // Narrative hooks for this specific application
    "string"
  ],
  "modificaciones": [
    {
      "selector": "string",        // Section/paragraph ID (e.g., experience:company_a, letter:intro)
      "accion": "REPLACE | HIGHLIGHT | OMIT | APPEND",
      "evidencia_ref": "string",   // Evidence tree ID
      "instrucciones_estilo": "string"  // Tone preferences from historical ReviewNodes
    }
  ]
}
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/08_document_delta.md`.