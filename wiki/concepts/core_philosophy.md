---
identity:
  node_id: "doc:wiki/concepts/core_philosophy.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/concepts/autopoiesis.md", relation_type: "contains"}
compliance:
  status: "implemented"
  failing_standards: []
---

Wikipu is built on the philosophy that **Documentation is Code** and **Knowledge is a Graph**. 

## The Core Axioms

1.  **Truth is Topological:** The facts themselves matter less than how they connect.
2.  **Structural Plasticity:** Files and directories can change, but the topological truth must be preserved.
3.  **Minimal Energy:** The system should always move toward the leanest structure that can still hold its truth.

## Definition

The philosophy of this system is centered on autopoiesis—self-creation. It rejects static, drifting documentation in favor of a dynamic, compiled knowledge graph that reflects the repository's ground truth.

## Examples

-   An ADR documenting a design decision and its impact on the graph.
-   The use of Pydantic contracts to enforce data integrity across processes.

## Related Concepts

-   `[[WhoAmI]]`
-   `[[autopoiesis]]`
-   `[[topology]]`
-   `[[energy]]`
