# Replace Raw Node Count with Redundancy Heuristic

**Status:** ✓ CLOSED (implemented in energy.py)

**Explanation:** The current `wiki-compiler energy` calculation penalizes the system by adding 1.0 point per node and 0.2 points per edge. This discourages healthy, highly-atomic composition and multidimensional styling. Our core objective is maximum knowledge in minimal physical space without redundancy or contradiction.

**Reference:** 
- `src/wiki_compiler/energy.py`
- `wiki/concepts/energy.md`
- `wiki/standards/house_rules.md` (ID-2)

**Implementation (2026-04-16):**
- Added `detect_redundant_nodes()` - Jaccard similarity for SemanticFacet.intent
- Added `detect_long_files_and_functions()` - file complexity detection
- Added `detect_code_doc_drift()` - AST vs documentation comparison
- Replaced node/edge penalties with redundancy-based penalties

**Depends on:** none
