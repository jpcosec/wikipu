---
identity:
  node_id: "doc:wiki/drafts/status.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/architecture/core_io_and_provenance_manager_spec.md", relation_type: "documents"}
---

This is an official mixed-status spec.

## Details

This is an official mixed-status spec.

### Implemented today

- `src/core/io/` exists.
- `WorkspaceManager`, `ArtifactReader`, `ArtifactWriter`, and `ProvenanceService` exist in code.
- Adoption is partial; some runtime slices still use inline path I/O.

### Future / target-state

- All runtime nodes should converge on the shared I/O layer.
- Provenance and artifact-writing behavior should become uniform across nodes.

Generated from `raw/docs_postulador_langgraph/docs/architecture/core_io_and_provenance_manager_spec.md`.