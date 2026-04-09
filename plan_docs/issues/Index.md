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

  10. plan_docs/issues/unimplemented/cleansing-apply-and-advanced-detectors.md
      • Add cleanse proposal application and the remaining anomaly detector families.
      • Depends on: none.
  12. plan_docs/issues/unimplemented/operational-artifact-validation.md
      • Add validators for issue, board, backlog, and gate artifacts using the new wiki artifact validation foundation.
      • Depends on: none.
  13. plan_docs/issues/unimplemented/artifact-validation-rollup.md
      • Add repo-wide artifact validation traversal and workflow integration.
      • Depends on: operational-artifact-validation.
  14. plan_docs/issues/unimplemented/scanner-plugin-interface.md
      • ScannerPlugin protocol + PythonScanner refactor + TypeScriptScanner; language-agnostic graph extraction.
      • Depends on: artifact-validation-rollup.

┄┄┄ Phase 4 — Autopoietic loop (depends on Phase 3)

15. plan_docs/issues/unimplemented/perception-gates-and-classification.md
    • Add perturbation classification and gate-aware status reporting on top of the perception foundation.
    • Depends on: none.
16. plan_docs/issues/unimplemented/cross-session-memory.md
    • SessionLog + TrailArtifact models, session log writes, wiki-compiler history.
    • Depends on: unimplemented/autopoiesis-loop-coordinator.md.
17. plan_docs/issues/unimplemented/autopoiesis-loop-coordinator.md
    • wiki-compiler run: the full cycle orchestrator with minimal energy enforcement.
    • Depends on: perception-gates-and-classification, cleansing-apply-and-advanced-detectors.
18. plan_docs/issues/unimplemented/context-routing.md
    • Add wiki-compiler context command: graph-driven context bundle for any task in one CLI call.
    • Depends on: query-server-runtime, how-to-wiki-section, verification-checklists.

┄┄ Dependency summary

Phase 3[10] → Phase 4[17]      (coordinator depends on the full cleanser, not just detection)
Phase 3[12] → Phase 3[13]      (rollup builds on operational artifact validators)
Phase 3[13] → Phase 3[14]      (scanner plugin targets the stabilized validation surface)
Phase 3[13] → Phase 4[18]      (context routing still depends on the broader validation/runtime foundation)
Phase 4[17] → Phase 4[16]      (coordinator triggers session open/close for memory)

┄┄ Parallelization map

Phase 3  [10][12] then [13] then [14]     — 10 and 12 parallel, then 13, then 14
Phase 4  [15] then [17] then [16]; [18] after [13]
