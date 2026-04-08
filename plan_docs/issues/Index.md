┄ Wikipu Issues Index

This file is the entrypoint for subagents deployed to solve issues in this repository.

┄┄ Working rule for every issue

Once an issue is solved:
 1. Check whether any existing test is no longer valid.
 2. Add new tests where necessary.
 3. Run the relevant tests.
 4. Update `changelog.md`.
 5. Delete the solved issue from both this index and the corresponding file in `plan_docs/issues/`.
 6. Make a commit that clearly states what was fixed.

┄┄ Current state

Foundation, interface, and generation layers are functional (Tasks 0–5 complete). The immediate goals are: fix the ingest test regression, close documentation debt, and implement the cleansing protocol.

┄┄ Priority roadmap

┄┄┄ Phase 1 — Fix regression (blocks clean test suite)

 1. plan_docs/issues/gaps/ingest-test-regression.md
    • Node IDs from ingest include temp dir prefix; fix path relativization in ingest.py.

┄┄┄ Phase 2 — Documentation debt (parallelizable)

 2. plan_docs/issues/unimplemented/code-documentation-coverage.md
    • Link existing code nodes to wiki nodes using `documents` edges.
 3. plan_docs/issues/unimplemented/docstring-coverage.md
    • Add missing docstrings to constructs flagged by audit.
 4. plan_docs/issues/unimplemented/wiki-template-compliance.md
    • Update wiki nodes to include mandatory abstract and required sections.

┄┄┄ Phase 3 — Structural gaps (parallelizable)

 5. plan_docs/issues/gaps/duplicate-docs-cleanup.md
    • Create missing wiki/standards/00_house_rules.md (referenced by ADR 002 and librarian protocol but doesn't exist).

┄┄┄ Phase 4 — Runtime and protocol

 6. plan_docs/issues/unimplemented/query-server-runtime.md
    • Build the query server and tool runtime for the Librarian agent.
    • Depends on: none (graph already includes code nodes).
 7. plan_docs/issues/unimplemented/cleansing-protocol.md
    • Implement cleanser.py with anomaly detectors and CleansingProposal.
    • Depends on: none (independent of query server).
 8. plan_docs/issues/unimplemented/draft-curation-pipeline.md
    • Add source-mirrored subdirectories to wiki/drafts/, per-source INDEX.md, and
      a `wiki-compiler curate` command with --score and --promote modes.
    • Depends on: gaps/ingest-test-regression.md (path relativization fix).

┄┄ Dependency summary

Phase 1 → Phase 2+3 (regression fix unblocks accurate audit results)
Phase 1 → Phase 4[8] (ingest path fix required before subdirectory logic)
Phase 3+4 are otherwise independent of each other.

┄┄ Parallelization map

Phase 1 [1]
Phase 2 [2][3][4] — parallel
Phase 3 [5] — parallel with Phase 4
Phase 4 [6][7][8] — 6 and 7 parallel; 8 depends on Phase 1
