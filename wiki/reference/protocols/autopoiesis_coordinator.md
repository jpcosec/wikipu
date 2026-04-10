---
identity:
  node_id: "doc:wiki/reference/protocols/autopoiesis_coordinator.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/how_to/use_autopoiesis.md", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
---

This protocol placeholder reserves a graph node for the autopoiesis coordinator that will eventually orchestrate the system's self-maintenance cycle. It links the conceptual cycle to a future operational coordinator surface.

## Rule Schema

- Re-seed the system with its own current state.
- Trigger ingest, build, and rule revision in the correct order.
- Remain planned until the coordinator runtime exists.

## Fields

- `planned` indicates the protocol has conceptual definition but no finished coordinator implementation yet.

## Usage Examples

- See `wiki/how_to/use_autopoiesis.md` for the current manual cycle.
