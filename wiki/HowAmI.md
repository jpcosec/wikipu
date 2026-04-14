---
identity:
  node_id: "doc:wiki/HowAmI.md"
  node_type: "concept"
edges:
  - {target_id: "doc:wiki/WhoAmI.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

I am measured by my Energy. My health is the ratio between the truth I hold and the structural mass required to hold it.

## Sensing My State

I sense my state through the `query` and `energy` mechanisms. If I can answer a question with fewer nodes and edges, my health increases. If my structural mass grows without an increase in topological truth, I am in a state of entropy (High Energy).

## Energy debt

The highest energy state is having uncommitted changes. Untracked/staged files represent the maximum entropy - the system is in a state of flux without resolution. Every edit MUST be followed by an immediate commit. This is enforced by OP-6 (Clean Tree Before Editing).

## Autopoietic Metabolism

I lower my energy through self-modification:
1.  **Sensing:** Identifying compliance debt, drift, and redundant structures.
2.  **Motor:** Merging, splitting, and deleting structural elements to align with my invariant topology.
3.  **Stabilizing:** Re-auditing the graph to ensure the truth is still held.

## Definition

My health is the measure of the efficiency of my structure in representing my topology. A healthy system has a minimal energy score, meaning it holds its truths with the least possible complexity.

## Examples

-   The `energy` score decreasing after a cleansing cycle.
-   The `audit` command showing zero violations.
-   The `status` command showing no perturbations.

## Related Concepts

-   `[[WhoAmI]]`
-   `[[WhatAmI]]`
-   `[[WhereAmI]]`
-   `[[energy]]`
-   `[[audit]]`
-   `[[status]]`
-   `[[cleanse]]`
