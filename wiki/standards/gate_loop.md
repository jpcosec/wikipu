---
identity:
  node_id: "doc:wiki/standards/gate_loop.md"
  node_type: "doc_standard"
compliance:
  status: "planned"
  failing_standards: []
---

This protocol placeholder reserves a graph node for the gate monitoring loop that tracks open human-approval requirements. It exists so the graph can represent that control point before the desk runtime is fully encoded.

## Rule Schema

- Surface open gates that block work crossing the topology boundary.
- Require explicit approval or rejection before destructive or external actions proceed.

## Fields

- `planned` means the protocol is recognized but still waiting for its mature operational implementation.

## Usage Examples

- Future protocol details will describe how `desk/Gates.md` is monitored and advanced.
