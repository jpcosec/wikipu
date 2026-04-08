# Self-Documentation Enforcement (Graph includes Code)

**Explanation:** The knowledge graph currently only indexes files in `wiki/`. It does not yet effectively "compile" the source code (`src/wiki_compiler/`) into nodes. This makes the graph "blind" to the system's own implementation, preventing the Librarian agent from navigating the codebase.

**Reference:** `plan_docs/issues.md` (Librarian Perspective)

**What to fix:** 
Ensure the `build` process includes `src/` modules as nodes with their own `semantics` and `ast` facets. The graph should allow an agent to query what `src/wiki_compiler/builder.py` does directly.

**How to do it:** 
1. Update `scanner.py` or `builder.py` to ensure every Python file in the `code_roots` is added to the graph.
2. Ensure that code nodes are enriched with docstring-derived semantics.
3. Validate that these nodes appear when running `wiki-compiler build`.

**Depends on:** `plan_docs/issues/unimplemented/facet-system-foundation.md`
