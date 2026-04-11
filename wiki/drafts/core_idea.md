---
identity:
  node_id: "doc:wiki/drafts/core_idea.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/board_gate_pattern.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/board_gate_pattern.md"
  source_hash: "5ddbb160292bc8387a9d70b4d3060c3c843651e5af5ef68e156bab47a0701c06"
  compiled_at: "2026-04-10T17:47:33.722139"
  compiled_from: "wiki-compiler"
---

Two distinct constructs govern how the system coordinates with humans:

## Details

Two distinct constructs govern how the system coordinates with humans:

1. **The Board** — a domain work tree: a structured index of pending items for one concern area, with phases, dependencies, and parallelization. Not a queue (FIFO) and not a flat list. A directed graph of items the system cannot advance without a decision.

2. **The Gate** — a single HITL checkpoint: one item the system cannot proceed past without explicit human input. Gates are embedded in or between Board items.

3. **desk/Gates.md** — the central gate monitor: a flat register of all open gates across all Boards. The single surface a human checks to know what the system is waiting on.

---

Generated from `raw/board_gate_pattern.md`.