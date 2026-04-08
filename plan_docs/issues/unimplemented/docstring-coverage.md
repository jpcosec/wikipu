# Docstring Coverage

**Explanation:** The audit tool (`wiki-compiler audit`) can now detect code constructs missing docstrings via the `SemanticFacet`. The scanner populates `raw_docstring` from source. Any construct where `raw_docstring` is null is undocumented. These gaps need to be filled across the codebase.

**Reference:** `src/wiki_compiler/auditor.py`, `src/wiki_compiler/scanner.py`

**What to fix:** Add docstrings to all public functions, methods, and classes in `src/wiki_compiler/` that the audit flags as missing.

**How to do it:**
1. Run `wiki-compiler audit` to get the current list of constructs with null `raw_docstring`.
2. Add docstrings to each flagged construct — one sentence describing what it does.
3. Re-run `wiki-compiler audit` and confirm the count drops to zero.

**Depends on:** none
