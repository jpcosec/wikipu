---
identity:
  node_id: "doc:wiki/drafts/semantic_rules_in_current_implementation.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/runtime/data_management.md", relation_type: "documents"}
---

### JSON meaning

## Details

### JSON meaning

- Machine-readable state and parser output.
- Used for routing decisions, hashes, and downstream deterministic checks.

### Markdown meaning

- Human review/edit surface (`decision.md`) or human-facing generated content.
- Markdown is still the operator-facing review surface for `review_match`.

### Hash-based review lock (current behavior)

- `review_match` computes expected `source_state_hash` from `nodes/match/approved/state.json`.
- If a `decision.md` has no hash and no checked boxes, the node regenerates it.
- If boxes are checked but hash is missing, it fails closed.
- If the hash mismatches current match state, it fails closed.

Generated from `raw/docs_postulador_langgraph/docs/runtime/data_management.md`.