# Add Code-Documentation Drift Detection

**Status:** ✓ CLOSED (implemented in energy.py)

**Explanation:** A deterministic measure must penalize drift between what the code's documentation (or `SemanticFacet.intent`) claims to do and what the AST actually does.

**Reference:**
- `src/wiki_compiler/energy.py`
- `wiki/standards/house_rules.md` (OP-5)

**What to fix:**
Verify that the intent aligns with `ASTFacet.signatures` and dependencies. Flag when docstrings and actual implementation diverge.

**How to do it:**
1. Extract expected behavior from SemanticFacet.intent
2. Compare against actual AST signatures
3. Add penalty for drift between documented and actual behavior

**Depends on:** 7 (replace node count heuristic)
