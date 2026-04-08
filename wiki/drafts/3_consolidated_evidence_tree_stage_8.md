---
identity:
  node_id: "doc:wiki/drafts/3_consolidated_evidence_tree_stage_8.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/08_document_delta.md", relation_type: "documents"}
---

Stage 8 takes all corrections and organizes them into the Global Evidence Arrangement:

## Details

Stage 8 takes all corrections and organizes them into the Global Evidence Arrangement:

| Type | Source | Description |
|------|--------|-------------|
| **Static Evidence** | `profile.json` | Titles, past jobs (base data) |
| **Dynamic Evidence (HITL)** | ReviewNodes AUGMENTATION | Links and achievements manually added in Stage 4 |
| **Exclusion Filters** | ReviewNodes REJECTION | Skills/experiences marked as undesirable for certain roles |

### Consolidation Flow

```
data/jobs/<source>/<job_id>/review/*.json
                ↓
    [Stage 8: Aggregator]
                ↓
    data/master/evidence_bank/
    data/master/filters/
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/08_document_delta.md`.