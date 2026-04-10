# Define Energy and Calculation Method

**Explanation:** The "Minimal Energy" rule (ID-2) is a core system constraint, but "Energy" is not formally defined. A human comment suggests defining Energy as its own concept and creating a deterministic way to calculate it, incorporating orthogonality violations as a form of energy consumption.
**Reference:** `wiki/standards/house_rules.md` (ID-2).
**What to fix:** 
1. Create `wiki/concepts/energy.md` to define the concept of systemic energy.
2. Formulate a deterministic scoring mechanism or rubric for evaluating the "energy cost" of a proposed change (factoring in LLM tokens, structural graph additions, and orthogonality overlap).
3. Update rule ID-2 in `house_rules.md` to reference this formal definition and remove the human comment.
**How to do it:** 
1. Author the `wiki/concepts/energy.md` node.
2. Update the description of ID-2 in `wiki/standards/house_rules.md` to explicitly link to `[[energy]]`.
3. (Optional but recommended) Outline how the coordinator or validation layer might calculate this score in the future.
**Depends on:** none.
