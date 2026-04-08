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

┄┄ Design commentary (Post-Foundation)

The Foundation, Interface, and Generation layers are now functional. The graph correctly indexes the source code, extract docstrings, and validates wiki templates. The immediate goal is now to **Resolve Documentation Debt** revealed by the `audit` tool.

┄┄ Priority roadmap

┄┄┄ Phase 1 — Resolving Documentation Debt

 1. plan_docs/issues/unimplemented/code-documentation-coverage.md
    • Link existing code nodes to wiki nodes using `documents` edges.
 2. plan_docs/issues/unimplemented/docstring-coverage.md
    • Add missing docstrings to the 98 constructs identified by the audit.
 3. plan_docs/issues/unimplemented/wiki-template-compliance.md
    • Update existing wiki nodes to include mandatory `abstract` and required sections.

┄┄ Dependency summary
None - these can be parallelized.

┄┄ Parallelization map
Phase 1 [1][2][3]
