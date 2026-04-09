# Artifact Validation Rollup and Workflow Integration

**Explanation:** Single-file wiki artifact validation now exists, but there is still no repo-wide traversal mode or workflow integration. That means agents can validate one artifact manually, yet cannot ask the compiler to validate the whole documentation surface or integrate those checks into broader repo discipline.

**Reference:** `src/wiki_compiler/main.py`, `src/wiki_compiler/workflow_guard.py`, `wiki/reference/cli/validate_wiki.md`

**What to fix:** Add multi-file artifact validation modes and integrate them into workflow checks or hooks.

**How to do it:**
1. Add a repo-wide artifact traversal mode.
2. Decide whether to unify command naming with the existing topology `validate` command or keep separate subcommands.
3. Integrate artifact validation into workflow automation.

**Depends on:** `plan_docs/issues/unimplemented/operational-artifact-validation.md`
