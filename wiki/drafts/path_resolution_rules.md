---
identity:
  node_id: "doc:wiki/drafts/path_resolution_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/canonical_path_registry.md", relation_type: "documents"}
---

### Rule 1: Single Source per Data Type

## Details

### Rule 1: Single Source per Data Type
Each data type has ONE canonical path. No exceptions.

### Rule 2: ReviewNodes vs Feedback
- **ReviewNodes** (generic, all stages) → `nodes/review/*.json`
- **Legacy feedback** (match-specific) → `feedback/` (DEPRECATED, avoid)

### Rule 3: Evidence Promotion
When a ReviewNode of type `AUGMENTATION` is validated:
1. Store in `nodes/review/<job_id>/augmentation_<id>.json`
2. Aggregator copies to `data/master/evidence/<evidence_id>.json`

### Rule 4: No Cross-Write
```
UI    → writes to → job folder (nodes/review/, nodes/drafting/)
CLI   → writes to → job folder (all)
API   → exposes → job folder (read/write bridge)
LangGraph → writes to → job folder (state.json, proposed/*.md)
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/canonical_path_registry.md`.