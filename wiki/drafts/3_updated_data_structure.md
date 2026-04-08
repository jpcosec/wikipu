---
identity:
  node_id: "doc:wiki/drafts/3_updated_data_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/07_evidence_tree_feedback_loop.md", relation_type: "documents"}
---

```

## Details

```
data/
├── master/                     # Global "Evidence Tree"
│   ├── profile.json            # Structured CV Profile
│   ├── evidence_bank/          # Links and HITL-validated proofs
│   │   └── *.json
│   └── templates/              # Base documents
│       ├── master_cv.md
│       ├── master_cover_letter.md
│       └── master_email.md
└── jobs/
    └── <source>/<job_id>/
        ├── raw/                # Original text and screenshots
        ├── nodes/              # Artifacts by stage
        │   ├── extract/
        │   ├── match/
        │   ├── strategy/
        │   └── drafting/
        └── review/             # ReviewNodes from this application
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/07_evidence_tree_feedback_loop.md`.