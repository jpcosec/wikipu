---
identity:
  node_id: "doc:wiki/drafts/how_to_run_in_parallel.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_cotizador/docs/plans/2026-03-11-vistas-parallel-design-graph.md", relation_type: "documents"}
---

1. Start `Path 0` and `Path 4` immediately (low coupling, high unblock value).

## Details

1. Start `Path 0` and `Path 4` immediately (low coupling, high unblock value).
2. Start `Path 1` design baseline (`B1`) while `Path 0` closes Gate A.
3. Start `Path 2` as soon as Gate A is closed (kit/group is the main blocker for pack parity).
4. Start `Path 3` after Gate B, so validation/export contracts include pack semantics from day one.

Generated from `raw/docs_cotizador/docs/plans/2026-03-11-vistas-parallel-design-graph.md`.