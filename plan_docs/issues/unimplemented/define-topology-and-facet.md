# Define Topology and Facet Concepts

**Explanation:** The foundational concepts of "Topology" and "Facet" are heavily used in the system's rules (especially ID-1 and ID-5) but lack rigorous definitions in the `wiki/concepts/` domain. A human comment in `house_rules.md` explicitly calls out this lack of clarity.
**Reference:** `wiki/standards/house_rules.md` (ID-1), `wiki/concepts/`.
**What to fix:** 
1. Create `wiki/concepts/topology.md` to define what constitutes the system's boundary and internal structure.
2. Create `wiki/concepts/facet.md` to define what a facet is within the Knowledge Graph (a typed data dimension attached to a node).
3. Remove the human comment from `wiki/standards/house_rules.md` (ID-1).
**How to do it:** 
1. Scaffold the two concept nodes using the standard `concept` template (Abstract, Definition, Examples, Related Concepts).
2. Ensure both nodes are transcluded or linked from `wiki/concepts/Index.md`.
3. Update `house_rules.md` to link to these new definitions.
**Depends on:** none.
