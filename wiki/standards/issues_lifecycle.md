---
identity:
  node_id: "doc:wiki/standards/issues_lifecycle.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
  - {target_id: "doc:wiki/standards/artifacts/issue.md", relation_type: "extends"}
  - {target_id: "doc:wiki/standards/issues_index_seed.md", relation_type: "extends"}
compliance:
  status: "implemented"
  failing_standards: []
---

The issue lifecycle standard defines how active work is represented, indexed, split, and retired in Wikipu. It is the canonical source for issue file structure, atomization, contradiction checks, dependency mapping, and resolution rules.

## Rule Schema

### Stage 1 - Mapping

Produce one Markdown issue per concern under one of these paths:

- `plan_docs/issues/gaps/` for things that exist but are wrong, inconsistent, or incomplete.
- `plan_docs/issues/unimplemented/` for things explicitly designed but not yet built.

Each issue file must include these sections:

```text
# <Title>

**Explanation:** What is wrong or missing, and why it matters.
**Reference:** File(s) in src/, wiki/, agents/, or plan_docs/ where the issue lives.
**What to fix:** The concrete end state.
**How to do it:** Suggested implementation path.
**Depends on:** Other issue file path(s) this must wait for, or `none`.
```

### Stage 2 - Indexing

Before assigning work, run these operations in order:

1. `Legacy audit` - delete obsolete content instead of fixing it when that is the correct outcome; encode durable rationale in an ADR if needed.
2. `Atomization` - split issues whose implementation has more than 3-4 independently failing steps.
3. `Contradiction check` - detect overlap, incompatible end states, and circular dependencies.
4. `Dependency graph` - map every `Depends on:` edge and identify roots, blockers, and parallelizable groups.
5. `Index generation` - regenerate `plan_docs/issues/Index.md` from `wiki/standards/issues_index_seed.md`.

### Lifecycle

Once an issue is solved:

1. Delete the issue file.
2. Remove it from `plan_docs/issues/Index.md`.
3. Update `changelog.md`.
4. Record lasting design decisions in `wiki/adrs/` if the resolution changed architecture.
5. Do not archive resolved issues; history belongs in git and ADRs.

### Default enforcement

- Non-trivial runtime or test work must be linked to at least one issue file under `plan_docs/issues/`.
- Non-trivial documentation work should also use an issue unless it is an explicitly structural docs-only change.
- Resolved issue deletion should happen together with `plan_docs/issues/Index.md` update.
- `wiki-compiler check-workflow` is the operational guard for these rules.

## Fields

- `gap` means the system already has the thing, but it is wrong or incomplete.
- `unimplemented` means the system has already committed to the design, but the implementation does not exist yet.
- `Atomization` means one issue can be completed and verified by one agent in one session.
- `Contradiction check` includes overlap, conflict, and circular dependency review.
- `Index generation` means `plan_docs/issues/Index.md` is treated as a generated operational entrypoint, not an ad hoc note.
- `Structural docs-only change` means a repo-organization or documentation-topology change that does not modify runtime code or tests.

## Usage Examples

- A stale doc that should simply be deleted is handled in the legacy audit stage, not kept alive as fake implementation work.
- A multi-language scanner refactor that requires independent protocol, plugin, and runtime changes should be split into child issues.
- A resolved issue disappears from `plan_docs/issues/` and from `plan_docs/issues/Index.md` in the same logical change.
- Before committing, run `wiki-compiler check-workflow` to catch missing issue links or missing `changelog.md` updates.
