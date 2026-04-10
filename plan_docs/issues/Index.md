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

┄┄┄ Gap issues (no dependencies — fix before starting phase work)

  32. [DONE] plan_docs/issues/unimplemented/documentation-debt-resolution.md
      • Resolve 147 undocumented nodes and the scanner_plugins.md compliance violation.
      • Depends on: none.

┄┄┄ Phase 3 — Runtime and protocol

  10. [DONE] plan_docs/issues/unimplemented/cleansing-apply-and-advanced-detectors.md
      • Add cleanse proposal application and the remaining anomaly detector families.
      • Depends on: none.
  12. [DONE] plan_docs/issues/unimplemented/operational-artifact-validation.md
      • Add validators for issue, board, backlog, and gate artifacts using the new wiki artifact validation foundation.
      • Depends on: none.
  13. [DONE] plan_docs/issues/unimplemented/artifact-validation-rollup.md
      • Add repo-wide artifact validation traversal and workflow integration.
      • Depends on: operational-artifact-validation.
  14. [DONE] plan_docs/issues/unimplemented/scanner-plugin-interface.md
      • ScannerPlugin protocol + PythonScanner refactor + TypeScriptScanner; language-agnostic graph extraction.
      • Depends on: artifact-validation-rollup.
  15. [DONE] plan_docs/issues/unimplemented/gate-table-runtime.md
      • Add read/write helpers and state handling for `desk/Gates.md`.
      • Depends on: none.
  21. [DONE] plan_docs/issues/unimplemented/perception-gates-and-classification.md
      • Add perturbation classification and gate-aware status reporting on top of the perception foundation.
      • Depends on: none.
  16. [DONE] plan_docs/issues/unimplemented/run-skeleton.md
      • Add a safe first version of `wiki-compiler run`.
      • Depends on: perception-gates-and-classification.
  17. [DONE] plan_docs/issues/unimplemented/coordinator-gate-resume-flow.md
      • Add gate pause/resume/apply flow to the coordinator.
      • Depends on: gate-table-runtime, run-skeleton, cleansing-apply-and-advanced-detectors.
  18. [DONE] plan_docs/issues/unimplemented/coordinator-identity-preflight.md
      • Add identity-rule and minimal-energy preflight before coordinator actions execute.
      • Depends on: run-skeleton.
  19. [DONE] plan_docs/issues/unimplemented/cycle-record-persistence.md
      • Persist a minimal cycle record for each coordinator run.
      • Depends on: run-skeleton.
  20. [DONE] plan_docs/issues/unimplemented/trail-collect-closeout.md
      • Add trail collect as the coordinator closeout step.
      • Depends on: coordinator-gate-resume-flow, cycle-record-persistence.

┄┄┄ Phase 4 — Autopoietic loop (depends on Phase 3)

22. [DONE] plan_docs/issues/unimplemented/context-router-contract.md
    • Define the stable CLI contract and bundle schema for context routing.
    • Depends on: none.
23. [DONE] plan_docs/issues/unimplemented/context-graph-aware-routing.md
    • Upgrade context matching into graph-aware routing with ranking reasons.
    • Depends on: context-router-contract.
24. [DONE] plan_docs/issues/unimplemented/context-prose-bundles.md
    • Render LLM-ready context bundles with prose snippets and ranked explanations.
    • Depends on: context-router-contract, context-graph-aware-routing, context-checklists-and-rules, context-active-work-intersection.
25. [DONE] plan_docs/issues/unimplemented/context-active-work-intersection.md
    • Add active-issue intersection to context bundles.
    • Depends on: context-router-contract, context-graph-aware-routing.
26. [DONE] plan_docs/issues/unimplemented/context-checklists-and-rules.md
    • Attach operation-aware checklists and governing rules to context bundles.
    • Depends on: context-router-contract.
27. [DONE] plan_docs/issues/unimplemented/session-log-schema.md
    • Define `SessionLog` and `TrailArtifact` and reconcile the standards language.
    • Depends on: none.
28. [DONE] plan_docs/issues/unimplemented/session-log-storage.md
    • Add session-log storage helpers and canonical paths under `desk/autopoiesis/`.
    • Depends on: session-log-schema.
29. [DONE] plan_docs/issues/unimplemented/history-command.md
    • Add `wiki-compiler history` as a read-only session-log aggregator.
    • Depends on: session-log-schema, session-log-storage.
30. [DONE] plan_docs/issues/unimplemented/trail-collect-session-log.md
    • Write session logs from the trail collect closeout path.
    • Depends on: session-log-schema, session-log-storage, trail-collect-closeout.
31. [DONE] plan_docs/issues/unimplemented/session-resume-from-log.md
    • Restore coordinator context from the latest session log.
    • Depends on: session-log-schema, session-log-storage, trail-collect-session-log, run-skeleton.

┄┄┄ Phase 5 — Conceptual Maturation & Protocol Deepening

33. [DONE] plan_docs/issues/unimplemented/define-topology-and-facet.md
    • Define Topology and Facet concepts in the wiki to clarify structural language and remove human comments.
    • Depends on: none.
34. [DONE] plan_docs/issues/unimplemented/define-energy-and-calculation.md
    • Define systemic Energy and a deterministic calculation method for orthogonality/cost, resolving human comments.
    • Depends on: none.
35. [DONE] plan_docs/issues/unimplemented/deepen-socratic-protocol.md
    • Expand the Socratic protocol from a stub to a fully defined operational schema.
    • Depends on: none.

┄┄ Dependency summary

Phase 3[10] → Phase 3[17]      (gate resume depends on cleanser apply)
Phase 3[12] → Phase 3[13]      (rollup builds on operational artifact validators)
Phase 3[13] → Phase 3[14]      (scanner plugin targets the stabilized validation surface)
Phase 3[15] → Phase 3[17]      (gate resume depends on gate runtime)
Phase 3[16] → Phase 3[17,18,19] (run skeleton is the base for coordinator follow-ups)
Phase 3[19] → Phase 3[20]      (trail collect closeout follows persisted cycles)
Phase 3[21] → Phase 3[16]      (run skeleton depends on perception classification)
Phase 4[22] → Phase 4[23,24]   (context feature work starts from the contract)
Phase 4[23] → Phase 4[25,26]   (routing is required before work intersection and prose bundles)
Phase 4[24] → Phase 4[26]      (prose bundles attach operation rules/checklists)
Phase 4[27] → Phase 4[28,29,30,31] (session schema is the base for all memory work)
Phase 4[28] → Phase 4[29,30,31] (storage helpers are required before history, writes, and resume)
Phase 3[20] → Phase 4[30]      (session-log writing follows trail collect closeout)
Phase 3[16] → Phase 4[31]      (session resume depends on coordinator startup)

┄┄ Parallelization map

Phase 3  [10][12][15] then [13][21] then [14][16] then [17][18][19] then [20]
Phase 4  [22][27] then [23][24][28] then [25][29] then [26][30][31]
