---
identity:
  node_id: doc:wiki/concepts/autopoiesis.md
  node_type: concept
edges:
  - target_id: doc:wiki/concepts/core_philosophy.md
    relation_type: implements
compliance:
  status: implemented
  failing_standards: []
---

Autopoiesis in Wikipu refers to the system's ability to self-define, self-maintain, and regenerate its own knowledge structures through a closed loop of perception, classification, and execution.

## Definition

Autopoiesis in Wikipu refers to the system's ability to self-define, self-maintain, and regenerate its own knowledge structures through a closed loop of perception, classification, and execution.

## Examples

- **Perturbation:** An external change (e.g., a new raw file, a code edit).
- **Compensation:** The autopoietic loop (via the Bibliotecario) compensates for the perturbation by updating the graph, resolving the gap, and restoring the baseline.

## Related Concepts

- [[core philosophy]]
- [[core_philosophy]]

## The Triadic Process Model
Following the cybernetic model of Limone & Bastias (2006), the Wikipu autopoietic loop operates through three coupled fundamental processes:

### 1. The Primary Process (Energy Regeneration)
In biological systems, this regenerates the components. In Wikipu, this is the **`wiki-compiler build`** and **Audit** process. It regenerates the `knowledge_graph.json` and the compliance baseline—the "energy" required for agents to navigate and validate the system.

### 2. The Structuring Process (Operational Framework)
This process produces the operational and decision-making structure. In Wikipu, this is the **Hausordnung** (House Rules) and the **Contracts** (`contracts.py`). These define the "law" and the "schemas" that every agent must respect to maintain systemic integrity.

### 3. The Decision-Making Process (Conversational Regulation)
This is a "closed network of conversations" that activates and coordinates the system. In Wikipu, this refers to the **LLM Sessions** and the **Coordinator Cycles**. Every gate resolution, issue atomization, and socratic interrogation is part of this regulatory conversation.

## Operational Closure
Wikipu achieves "Operational Closure" because its own processes (the CLI, the Agent protocols, and the House Rules) are nodes within the Knowledge Graph they govern. A system that cannot model itself cannot maintain itself.

- **Perturbation:** An external change (e.g., a new raw file, a code edit).
- **Compensation:** The autopoietic loop (via the Bibliotecario) compensates for the perturbation by updating the graph, resolving the gap, and restoring the baseline.

## Why it Matters
Without autopoiesis, a repository suffers from **Entropy**: documentation drifts from code, rules are forgotten, and context is lost. Autopoiesis ensures that the "Learning" of the system is distilled into permanent, compiled knowledge that regenerates with every cycle.

Generated from the Limone & Bastias (2006) cybernetic research paper.
