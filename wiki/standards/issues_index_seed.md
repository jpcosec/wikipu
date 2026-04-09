---
identity:
  node_id: "doc:wiki/standards/issues_index_seed.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/issues_lifecycle.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

This seed defines the canonical starting shape for `plan_docs/issues/Index.md`. Use it when regenerating the issue index so subagents always receive the same operational structure and completion checklist.

## Rule Schema

`plan_docs/issues/Index.md` should preserve these sections in order: entrypoint note, working rule for every issue, current state, priority roadmap, dependency summary, and parallelization map.

## Fields

- `[Project Name]` is replaced by the real repository name.
- Phase names should reflect the current work program, not archival history.
- Each issue entry should use the file path as the durable identifier.

## Usage Examples

- Regenerate the live issue index after splitting, adding, or resolving issues.
- Keep the operational checklist at the top so subagents see completion rules first.

┄ [Project Name] Issues Index

This file is the entrypoint for subagents deployed to solve issues in this repository.

All issue-fixing work must stay aligned with the rest of `plan_docs/` and `wiki/`, with special care for `wiki/standards/` so implementation, tests, and documentation remain consistent with the project's rules.

┄┄ Working rule for every issue

Once an issue is solved, the next step is always:

 1. Check whether any existing test is no longer valid and delete it if needed.
 2. Add new tests where necessary.
 3. Run the relevant tests.
 4. Update `changelog.md`.
 5. Delete the solved issue from both this index and the corresponding file in `plan_docs/issues/`.
 6. Make a commit that clearly states what was fixed, making sure all required files are staged.

┄┄ Priority roadmap

┄┄┄ Phase 1 — [Phase name]

 1. plan_docs/issues/[gaps|unimplemented]/issue-name.md
 2. plan_docs/issues/[gaps|unimplemented]/issue-name.md

    • [Parallelization note if applicable]

┄┄┄ Phase 2 — [Phase name]

 3. plan_docs/issues/[gaps|unimplemented]/issue-name.md
    • depends on plan_docs/issues/.../issue-name.md

    • [Parallelization note if applicable]

┄┄ Dependency summary

• plan_docs/issues/.../downstream.md  ->  plan_docs/issues/.../upstream.md

┄┄ Parallelization map

Phase 1  [1][2]          ← [note]
Phase 2     [3]          ← [note]
