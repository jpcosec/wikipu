---
identity:
  node_id: "doc:wiki/standards/artifacts/task.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

A single, completable unit of work. Tasks live in `desk/tasks/`. They are ephemeral: once resolved, the file is deleted and the work lives only in git and changelog.

## Rule Schema

Tasks have no frontmatter. They are ephemeral operational artifacts (MA-3).

### Body sections

| Section | Required | Content |
|---|---|---|
| Title (H1) | yes | Imperative noun phrase: what needs to exist or be fixed |
| Explanation | yes | What is wrong or missing, and why it matters to the system |
| Reference | yes | Which nodes, rules, or files this affects |
| What to fix | yes | The concrete end state — what will be true when done |
| How to do it | optional | Suggested implementation steps; omit if the fix is obvious |
| Depends on | yes | Paths to blocking tasks, or the word `none` |

## Fields

- One task = one atomic unit of work. If "How to do it" has more than 3–4 steps that could fail independently, split into child tasks.
- "What to fix" describes outcome, not process. It must be verifiable: either the thing exists and passes tests, or it does not.
- "Depends on: none" must be written explicitly — omitting the field is not the same as having no dependencies.
- A task is done only when: tests pass, changelog updated, file deleted, removed from Board.

## Usage Examples

```markdown
# Fix query timeout

**Explanation:** Query timeouts after 30s for large result sets, blocking users.

**Reference:** `src/wiki_compiler/query_executor.py`, `wiki/selfDocs/HowAmI.md`

**What to fix:** Queries larger than 1000 results stream incrementally instead of loading all at once.

**How to do it:**
1. Add streaming mode to query executor
2. Add `--stream` flag to CLI
3. Update tests

**Depends on:** none
```
