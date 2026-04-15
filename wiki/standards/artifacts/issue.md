---
identity:
  node_id: "doc:wiki/standards/artifacts/issue.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

A single, completable unit of work. Issues live in `desk/issues/`. They are ephemeral: once resolved, the file is deleted and the work lives only in git and changelog.

## Rule Schema

Issues have no frontmatter. They are ephemeral operational artifacts (MA-3).

### Body sections

| Section | Required | Content |
|---|---|---|
| Title (H1) | yes | Imperative noun phrase: what needs to exist or be fixed |
| Explanation | yes | What is wrong or missing, and why it matters to the system |
| Reference | yes | Which nodes, rules, or files this affects |
| What to fix | yes | The concrete end state — what will be true when done |
| How to do it | optional | Suggested implementation steps; omit if the fix is obvious |
| Depends on | yes | Paths to blocking issues, or the word `none` |

## Fields

- One issue = one atomic unit of work. If "How to do it" has more than 3–4 steps that could fail independently, split into child issues.
- "What to fix" describes outcome, not process. It must be verifiable: either the thing exists and passes tests, or it does not.
- "Depends on: none" must be written explicitly — omitting the field is not the same as having no dependencies.
- An issue is done only when: tests pass, changelog updated, file deleted, removed from Board.
