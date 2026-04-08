---
identity:
  node_id: "doc:wiki/drafts/race_condition_warning.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/canonical_path_registry.md", relation_type: "documents"}
---

**PROBLEM**: Multiple processes write to same files:

## Details

**PROBLEM**: Multiple processes write to same files:
- LangGraph (background)
- UI (via PUT requests)
- CLI (manual operations)

**RULE**: Before any write:
1. Check if another process holds lock (`.<file>.lock`)
2. If locked, wait or abort with error
3. Acquire lock before writing
4. Release lock after write

**IMPLEMENTATION REQUIRED**:
```bash
# Lock file pattern
.<original_file>.lock

# Atomic write pattern
mv /tmp/<file>.<uuid> <destination>
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/canonical_path_registry.md`.