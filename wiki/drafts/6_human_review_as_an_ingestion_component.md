---
identity:
  node_id: "doc:wiki/drafts/6_human_review_as_an_ingestion_component.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md", relation_type: "documents"}
---

The review UI (`src/review_ui/`) is an ingestion component. It receives uncontrolled human input (button clicks, text fields, free-form notes) and produces a typed `ReviewPayload`.

## Details

The review UI (`src/review_ui/`) is an ingestion component. It receives uncontrolled human input (button clicks, text fields, free-form notes) and produces a typed `ReviewPayload`.

Rules that apply:
- The same validation-at-boundary rule applies: validate `ReviewPayload` shape before passing it to the graph.
- Hash-check the source artifact the reviewer acted on — if the artifact changed since the UI loaded, reject the payload.
- A review submission with missing or invalid fields is a `IngestionValidationError`, not a graph error.

The graph should never receive a `ReviewPayload` it has to partially trust. Either it's valid and hash-checked, or it's rejected at the boundary.

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/ingestion_layer.md`.