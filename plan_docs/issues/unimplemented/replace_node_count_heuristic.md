# Replace Raw Node Count with Redundancy Heuristic

The current `wiki-compiler energy` calculation penalizes the system by adding 1.0 point per node and 0.2 points per edge. This discourages healthy, highly-atomic composition and multidimensional styling. Our core objective is maximum knowledge in minimal physical space without redundancy or contradiction.

## Reference
- `src/wiki_compiler/energy.py`
- `wiki/concepts/energy.md`
- `wiki/standards/house_rules.md` (ID-2)

## What to fix
The heuristic must drop the absolute node/edge count penalty and replace it with a direct measurement of redundancy (e.g., Jaccard similarity across `SemanticFacet.intent` or AST signatures) and boilerplate-to-truth ratios. Orthogonal micro-files should not be artificially penalized if they successfully abstract a cross-cutting pattern.

## Depends on
none
