---
identity:
  node_id: doc:wiki/concepts/energy.md
  node_type: concept
edges: []
compliance:
  status: implemented
  failing_standards: []
---

Energy in Wikipu is the conceptual and structural cost of creating or modifying elements within the system. Minimizing this energy (Rule ID-2) ensures the Knowledge Graph remains lean, orthogonal, and maintainable.

## Definition

Energy in Wikipu is the conceptual and structural cost of creating or modifying elements within the system.

## Examples

- Energy Score Heuristic:

## Related Concepts

- [[facet]]
- [[topology]]

Systemic Energy can be deterministically calculated or estimated using the following factors:

1. **Orthogonality Cost:** Does the proposed change overlap in intent with an existing node? If an intent overlaps by >80% (as scored by query context routing), creating a new node is a high-energy error. Updating the existing node is a low-energy extension.
2. **Structural Complexity:** The number of new files, `KnowledgeNode` definitions, and graph edges introduced. Each new node adds maintenance overhead.
3. **Execution Cost:** The volume of LLM tokens required to generate and validate the change, or the number of independent autopoietic cycles required to stabilize the topology.
4. **State Uncertainty:** The likelihood that a change will introduce compliance violations (e.g., missing fields, broken links) requiring subsequent cleanup passes.

**Energy Score Heuristic:**
`Energy = (New Nodes * 10) + (New Edges * 2) + (Orthogonality Violations * 100)`

A score > 50 for a single functional change suggests the proposal should be rejected or refactored into smaller, extension-based increments.

## The Energy-Based Model (EBM) Macro-Architecture

Wikipu operates mathematically as a macro-scale **Energy-Based Model (EBM)**. While deep learning EBMs use neural networks to assign scalar energy scores to continuous tensors, Wikipu uses the `wiki-compiler energy` heuristic to assign a scalar energy score to a discrete configuration (the entire Git repository and knowledge graph).

| Concept | Deep Learning EBM | Wikipu Autopoiesis |
|---|---|---|
| **The Configuration ($x$)** | A tensor (e.g., text sequence) | The Git repository (Markdown + Graph + Code) |
| **The Energy Function $E(x)$** | A neural network outputting a scalar | The `wiki-compiler energy` heuristic |
| **The Goal** | Low energy = compatible with real data | Low energy = orthogonal, debt-free, compliant topology |
| **Inference (System 2 Thinking)** | Continuous gradient descent to minimize $E(x)$ | Discrete structural modifications via the autopoietic cycle |
| **Temperature ($T$)** | Controls exploration vs exploitation | $T=0$ (deterministic invariant enforcement) in `wiki/` |

Instead of generating files greedily left-to-right like an autoregressive LLM, Wikipu evaluates the *global energy* of its repository state (Structural Mass + Compliance Debt + Operational Drift + Uncommitted Changes). The system's "inference time optimization" consists of discrete operations—Socratic interrogations, graph cleanses, node merges, and immediate Git commits—that deterministically step the system down into its lowest possible energy state.
