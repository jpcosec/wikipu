---
identity:
  node_id: "doc:wiki/standards/issues_lifecycle.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
  - {target_id: "doc:wiki/standards/artifacts/issue.md", relation_type: "extends"}
compliance:
  status: "implemented"
  failing_standards: []
---

The issue lifecycle standard defines how active work is represented, tracked, and retired in Wikipu. It is the canonical source for issue file structure, atomization, contradiction checks, dependency mapping, and resolution rules.

## Rule Schema

### Stage 1 - Mapping

Produce one Markdown issue per concern under `desk/issues/`:

- No subdirectories (gaps/unimplemented) — all issues live flat in `desk/issues/`
- Filename format: `<number>-<slug>.md` (e.g., `1-ingest-raw.md`)

Each issue file must include these sections:

```text
# <Title>

**Explanation:** What is wrong or missing, and why it matters.
**Reference:** File(s) in src/, wiki/, or desk/ where the issue lives.
**What to fix:** The concrete end state.
**How to do it:** Suggested implementation path.
**Depends on:** Other issue file path(s) this must wait for, or `none`.
```

### Stage 2 - Board Update

Before assigning work, run these operations in order:

1. `Legacy audit` - delete obsolete content instead of fixing it when that is the correct outcome; encode durable rationale in an ADR if needed.
2. `Atomization` - split issues whose implementation has more than 3-4 independently failing steps.
3. `Contradiction check` - detect overlap, incompatible end states, and circular dependencies.
4. `Dependency graph` - map every `Depends on:` edge and identify roots, blockers, and parallelizable groups.
5. Update `desk/issues/Board.md` with the issue and its dependencies.

### Lifecycle

Once an issue is solved:

1. Delete the issue file.
2. Remove it from `desk/issues/Board.md`.
3. Update `changelog.md`.
4. Record lasting design decisions in `wiki/adrs/` if the resolution changed architecture.
5. Do not archive resolved issues; history belongs in git and ADRs.

### Default enforcement

- Non-trivial runtime or test work must be linked to at least one issue file under `desk/issues/`.
- Non-trivial documentation work should also use an issue unless it is an explicitly structural docs-only change.
- Resolved issue deletion should happen together with `desk/issues/Board.md` update.
- `wiki-compiler check-workflow` is the operational guard for these rules.

## Fields

- `Atomization` means one issue can be completed and verified by one agent in one session.
- `Contradiction check` includes overlap, conflict, and circular dependency review.
- `Structural docs-only change` means a repo-organization or documentation-topology change that does not modify runtime code or tests.

## Usage Examples

- A stale doc that should simply be deleted is handled in the legacy audit stage, not kept alive as fake implementation work.
- A multi-language scanner refactor that requires independent protocol, plugin, and runtime changes should be split into child issues.
- A resolved issue disappears from `desk/issues/` and from `desk/issues/Board.md` in the same logical change.
- Before committing, run `wiki-compiler check-workflow` to catch missing issue links or missing `changelog.md` updates.
