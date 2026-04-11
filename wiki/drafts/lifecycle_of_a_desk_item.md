---
identity:
  node_id: "doc:wiki/drafts/lifecycle_of_a_desk_item.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/desk_zone.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/desk_zone.md"
  source_hash: "6ee387eded8902a4b171c92ba6c94d8721f2b7bfdd481c0a5299951da3127390"
  compiled_at: "2026-04-10T17:47:33.730228"
  compiled_from: "wiki-compiler"
---

```

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