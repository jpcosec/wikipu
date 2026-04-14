---
identity:
  node_id: "doc:wiki/concepts/the_gate.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/board_gate_pattern.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
source:
  source_path: "raw/board_gate_pattern.md"
  source_hash: "5ddbb160292bc8387a9d70b4d3060c3c843651e5af5ef68e156bab47a0701c06"
  compiled_at: "2026-04-14T16:50:28.657175"
  compiled_from: "wiki-compiler"
---

A gate is any item that:

## Details

A gate is any item that:
- Cannot be resolved by the system alone
- Blocks the system from proceeding
- Requires explicit human input (approval, decision, or answer)

Gates exist in several forms:
- An issue item waiting to be picked up (implementation decision)
- A CleansingProposal with `requires_human_approval: true`
- A TopologyProposal awaiting approval before scaffolding
- A Socratic question awaiting a design decision
- A trail collect artifact awaiting integration

### Gate Properties

| Property | Description |
|---|---|
| `source_board` | Which Board this gate belongs to |
| `item_id` | The specific item within that Board |
| `gate_type` | `approval`, `decision`, `answer`, `review` |
| `blocking` | What cannot proceed until this gate resolves |
| `opened_at` | When the gate was created |

---

Generated from `raw/board_gate_pattern.md`.