---
identity:
  node_id: "doc:wiki/concepts/energy.md"
  node_type: "concept"
edges: []
compliance:
  status: "implemented"
  failing_standards: []
---

Energy in Wikipu is the conceptual and structural cost of creating or modifying elements within the system. Minimizing this energy (Rule ID-2) ensures the Knowledge Graph remains lean, orthogonal, and maintainable.

## Definition

The Minimal Energy principle states that when resolving an issue or responding to a perturbation, the system (or agent) should choose the path that incurs the lowest systemic cost. 

Systemic Energy can be deterministically calculated or estimated using the following factors:

1. **Orthogonality Cost:** Does the proposed change overlap in intent with an existing node? If an intent overlaps by >80% (as scored by query context routing), creating a new node is a high-energy error. Updating the existing node is a low-energy extension.
2. **Structural Complexity:** The number of new files, `KnowledgeNode` definitions, and graph edges introduced. Each new node adds maintenance overhead.
3. **Execution Cost:** The volume of LLM tokens required to generate and validate the change, or the number of independent autopoietic cycles required to stabilize the topology.
4. **State Uncertainty:** The likelihood that a change will introduce compliance violations (e.g., missing fields, broken links) requiring subsequent cleanup passes.

**Energy Score Heuristic:**
`Energy = (New Nodes * 10) + (New Edges * 2) + (Orthogonality Violations * 100)`

A score > 50 for a single functional change suggests the proposal should be rejected or refactored into smaller, extension-based increments.

## Examples

- **Low Energy (Preferred):** Adding a new field to an existing Pydantic model in `contracts.py` and updating its corresponding `doc_standard` node.
- **High Energy (Rejected):** Creating a parallel `contracts_v2.py` module because the original model was deemed too complex to safely modify, creating massive orthogonality violations.

## Related Concepts

- `[[topology]]`
- `[[facet]]`