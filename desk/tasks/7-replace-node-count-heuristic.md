# Replace Raw Node Count with Redundancy Heuristic

**Explanation:** The current `wiki-compiler energy` calculation penalizes the system by adding 1.0 point per node and 0.2 points per edge. This discourages healthy, highly-atomic composition and multidimensional styling. Our core objective is maximum knowledge in minimal physical space without redundancy or contradiction.

**Reference:** 
- `src/wiki_compiler/energy.py`
- `wiki/concepts/energy.md`
- `wiki/standards/house_rules.md` (ID-2)

**What to fix:**
The heuristic must drop the absolute node/edge count penalty and replace it with a direct measurement of redundancy (e.g., Jaccard similarity across `SemanticFacet.intent` or AST structural hashing/clusters) and boilerplate-to-truth ratios. Orthogonal micro-files should not be artificially penalized if they successfully abstract a cross-cutting pattern.

**How to do it:**
1. Add Jaccard similarity calculation for `SemanticFacet.intent` across nodes
2. Add boilerplate detection (template repetition without new truth)
3. Add AST structural clustering to detect semantically similar code
4. Replace node/edge penalties with redundancy-based penalties
5. Test with current graph to verify lower energy for clean structure

**Depends on:** none
