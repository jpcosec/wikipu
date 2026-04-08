---
identity:
  node_id: "doc:wiki/drafts/priority_rules_conflict_resolution.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md", relation_type: "documents"}
---

When multiple controls are active, apply precedence in this order:

## Details

When multiple controls are active, apply precedence in this order:

1. Edit mode constraints
2. Focus mode constraints
3. Relation type visibility filters
4. Node field filters
5. Hover visibility

This order avoids ambiguity when a node is both filtered and focused.

Additional guarantee:

- An actively edited node or relation stays visible and interactive regardless of active filters until the edit session ends.

Cross-cutting UI requirements:

- Provide a dedicated `View Options` section in sidebar for focus opacity and line style behavior tuning.
- Provide a visible mode badge on canvas (e.g., `Mode: Browse`, `Mode: Focus`, `Mode: Edit`) that also supports returning to browse.

Generated from `raw/docs_postulador_langgraph/docs/ui/node_editor_behavior_spec.md`.