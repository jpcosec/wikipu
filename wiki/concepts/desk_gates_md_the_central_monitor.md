---
identity:
  node_id: doc:wiki/concepts/desk_gates_md_the_central_monitor.md
  node_type: concept
edges:
- target_id: raw:raw/board_gate_pattern.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/board_gate_pattern.md
  source_hash: 5ddbb160292bc8387a9d70b4d3060c3c843651e5af5ef68e156bab47a0701c06
  compiled_at: '2026-04-14T16:50:28.657221'
  compiled_from: wiki-compiler
---

A flat register of all currently open gates across all Boards. One line per gate. The human's daily check.

## Definition

A flat register of all currently open gates across all Boards.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

A flat register of all currently open gates across all Boards. One line per gate. The human's daily check.

Format:
```
[gate_type] <source_board>/<item_id> — <one-line description of what is needed> → blocks: <what is blocked>
```

Example:
```
[approval]  proposals/topology_cleanser_module — approve new cleanser.py topology → blocks: implementation start
[decision]  socratic/query_server_design — resolve: CLI-only vs Python API? → blocks: query-server-runtime
[review]    autopoiesis/drift_report_2026_04_09 — 3 stale nodes flagged, approve repairs → blocks: next build
```

When a gate is resolved, its line is removed from Gates.md. The resolution is recorded in changelog.md.

---

Generated from `raw/board_gate_pattern.md`.
