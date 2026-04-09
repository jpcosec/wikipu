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

Foundation, interface, and generation layers are functional. The immediate goals are: close documentation debt and implement the cleansing protocol.

┄┄ Priority roadmap

┄┄┄ Phase 3 — Runtime and protocol

  10. plan_docs/issues/unimplemented/cleansing-protocol.md
      • Implement cleanser.py with anomaly detectors and CleansingProposal.
      • Depends on: none.
  12. plan_docs/issues/unimplemented/artifact-schema-validation.md
      • Pydantic models and wiki-compiler validate command for all artifact schemas (markdown/YAML only).
      • Depends on: query-server-runtime.
  13. plan_docs/issues/unimplemented/scanner-plugin-interface.md
     • ScannerPlugin protocol + PythonScanner refactor + TypeScriptScanner; language-agnostic graph extraction.
     • Depends on: artifact-schema-validation.

┄┄┄ Phase 4 — Autopoietic loop (depends on Phase 3)

15. plan_docs/issues/unimplemented/perception-layer.md
    • Implement GitFacet and wiki-compiler status command for drift detection.
    • Depends on: none.
16. plan_docs/issues/unimplemented/cross-session-memory.md
    • SessionLog + TrailArtifact models, session log writes, wiki-compiler history.
    • Depends on: unimplemented/autopoiesis-loop-coordinator.md.
17. plan_docs/issues/unimplemented/autopoiesis-loop-coordinator.md
    • wiki-compiler run: the full cycle orchestrator with minimal energy enforcement.
    • Depends on: perception-layer, cleansing-protocol, query-server-runtime.
18. plan_docs/issues/unimplemented/context-routing.md
    • Add wiki-compiler context command: graph-driven context bundle for any task in one CLI call.
    • Depends on: query-server-runtime, how-to-wiki-section, verification-checklists.

┄┄ Dependency summary

Phase 3[10] → Phase 4[17]      (coordinator depends on cleanser alongside resolved curation/query foundations)
Phase 3[12] → Phase 3[13]      (scanner plugin targets stable KnowledgeNode schema)
Phase 3[12] → Phase 4[18]      (context routing still depends on the query runtime foundation carried by artifact validation)
Phase 4[17] → Phase 4[16]      (coordinator triggers session open/close for memory)

┄┄ Parallelization map

Phase 3  [10] then [12] then [13]         — 10 first, then 12, then 13
Phase 4  [15] then [17] then [16]; [18] after [12]
