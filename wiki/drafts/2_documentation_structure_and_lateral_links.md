---
identity:
  node_id: "doc:wiki/drafts/2_documentation_structure_and_lateral_links.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md", relation_type: "documents"}
---

Documentation is organized as a graph where context flows in a controlled manner.

## Details

Documentation is organized as a graph where context flows in a controlled manner.

### Folder Hierarchy

- `docs/runtime/`: Current technical truth. What the code does today.
- `plan/`: Target state design. References `docs/` to propose changes.

### Link Rules

- **Temporal Unidirectionality**: `plan/` → references to `docs/` (allowed). `docs/` → references to `plan/` (prohibited, to avoid contaminating current truth).
- **Lateral Context**: Encouraged links between domains (e.g., a UI doc in `docs/ui/` can link to DB spec in `docs/architecture/`) to give complete context to developers.

### "Hard" vs. "Soft" Documentation

- Detailed technical documentation lives close to code in local `README.md` files.
- Conceptual maps and `canonical_map.md` live at `docs/` root as hierarchical entry points.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md`.