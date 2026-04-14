# Enforce Structural Abstraction and Code-to-Doc Drift

As we scale down into highly granular nodes, we need dedicated heuristic penalties to enforce structural order, the use of descriptive abstractions, and alignment between implementation and documentation.

## Reference
- `src/wiki_compiler/energy.py`
- `wiki/concepts/energy.md`
- `wiki/standards/house_rules.md` (CS-9, OP-5)

## What to fix
1. **Descriptive Abstraction (Code as Natural Language):** Enforce the usage of small, highly descriptive functions and classes. Higher-order methods should read closer to natural language (and their documentation) than to low-level computational behavior. Long files ("giant code pills") must be heavily penalized to force division into smaller, structurally ordered files. This also extends to **test-level linting**, where test files must adhere to clarity and expressiveness standards, reflecting the natural language flow of the code they test.
2. **Structural Order:** Code must be organized into folders, sections, and packages that truly reflect and enforce its purpose.
3. **Documentation vs. Implementation Drift:** A deterministic measure must penalize drift between what the code's documentation (or `SemanticFacet.intent`) claims to do and what the AST actually does (e.g., verifying that the intent aligns with `ASTFacet.signatures` and dependencies).

## Depends on
- `plan_docs/issues/unimplemented/replace_node_count_heuristic.md`
