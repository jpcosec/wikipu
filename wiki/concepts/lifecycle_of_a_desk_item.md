---
identity:
  node_id: doc:wiki/concepts/lifecycle_of_a_desk_item.md
  node_type: concept
edges:
- target_id: raw:raw/desk_zone.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/desk_zone.md
  source_hash: 8719d650771e57b8cb2c6dda66c04511f3223100d4954abb4fa2c1d02fcb9213
  compiled_at: '2026-04-14T16:50:28.658526'
  compiled_from: wiki-compiler
---

```

## Definition

The concept of lifecycle of a desk item within the Wikipu framework.

## Examples

- Implementation of this concept within the Wikipu workflow.
- Application of these principles in current documentation.

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

```
idea or detected problem
    ↓
raw/ seed (if conceptual) OR direct to desk/ (if actionable)
    ↓
desk/<domain>/Board.md — item added to the appropriate phase
    ↓
desk/<domain>/items/<slug>.md — full item file created
    ↓
if HITL required: desk/Gates.md — gate entry added
    ↓
human resolves gate (approves, decides, answers)
    ↓
agent or human executes resolution
    ↓
desk/<domain>/items/<slug>.md — DELETED
    ↓
desk/<domain>/Board.md — item removed
    ↓
desk/Gates.md — gate line removed (if applicable)
    ↓
changelog.md — one entry recording what was resolved
```

History lives in git log and changelog. The desk is clean.

---

Generated from `raw/desk_zone.md`.
