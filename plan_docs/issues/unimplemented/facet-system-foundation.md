# Facet System Foundation

**Explanation:** The knowledge graph compiler currently only handles basic identity and edges. It lacks a structured way to register and inject additional information (facets) like ADR associations, test mapping, and structured queries. This is the foundational Task 0-2 of the Three-Phase plan.

**Reference:** `plan_docs/2026-04-08-three-phase-graph.md` (Task 0, 1, 2)

**What to fix:** 
1. Implement `registry.py` with `FacetSpec` and `FacetRegistry`.
2. Implement `protocols.py` with `FacetInjector` and `AuditCheck` protocols.
3. Implement `query_language.py` and `query_executor.py` for structured graph queries.
4. Implement `build_directory_skeleton` in `builder.py` (Task 1).
5. Implement `ADRInjector` and `TestMapInjector` in `facet_injectors.py` (Task 2).

**How to do it:** 
Follow the detailed steps and code in Task 0, 1, and 2 of the `plan_docs/2026-04-08-three-phase-graph.md` document. This involves creating new modules and updating `builder.py`.

**Depends on:** none
