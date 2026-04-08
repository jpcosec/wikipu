# Audit and Proposal Gates

**Explanation:** The "closed loop" of the project's design is not yet operational. The compiler doesn't have an audit command to check for quality or compliance, and it doesn't have a mechanism to validate new facets against existing ones (orthogonality). This is Task 3-4 of the Three-Phase plan.

**Reference:** `plan_docs/2026-04-08-three-phase-graph.md` (Task 3, 4)

**What to fix:** 
1. Implement `wiki-compiler audit` CLI with `AuditCheck` plugins (Task 3).
2. Implement `FacetProposal` orthogonality gate (Task 4) and its validation logic in `facet_validator.py`.
3. Wire the `propose-facet` subcommand into `main.py`.

**How to do it:** 
Follow the detailed steps and code in Task 3 and 4 of the `plan_docs/2026-04-08-three-phase-graph.md` document. This involves creating `auditor.py` and `facet_validator.py`.

**Depends on:** `plan_docs/issues/unimplemented/facet-system-foundation.md`
