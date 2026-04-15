---
identity:
  node_id: "doc:wiki/standards/tasks_lifecycle.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
  - {target_id: "doc:wiki/standards/artifacts/task.md", relation_type: "extends"}
compliance:
  status: "implemented"
  failing_standards: []
---

The task lifecycle standard defines how active work is represented, tracked, and retired in Wikipu. It is the canonical source for task file structure, atomization, contradiction checks, dependency mapping, and resolution rules.

## Rule Schema

### Stage 1 - Mapping

Produce one Markdown task per concern under `desk/tasks/`:

- No subdirectories — all tasks live flat in `desk/tasks/`
- Filename format: `<number>-<slug>.md` (e.g., `1-ingest-raw.md`)

Each task file must include these sections:

```text
# <Title>

**Explanation:** What is wrong or missing, and why it matters.
**Reference:** File(s) in src/, wiki/, or desk/ where the task lives.
**What to fix:** The concrete end state.
**How to do it:** Suggested implementation path.
**Depends on:** Other task file path(s) this must wait for, or `none`.
```

### Stage 2 - Board Update

Before assigning work, run these operations in order:

1. `Legacy audit` - delete obsolete content instead of fixing it when that is the correct outcome; encode durable rationale in an ADR if needed.
2. `Atomization` - split tasks whose implementation has more than 3-4 independently failing steps.
3. `Contradiction check` - detect overlap, incompatible end states, and circular dependencies.
4. `Dependency graph` - map every `Depends on:` edge and identify roots, blockers, and parallelizable groups.
5. Update `desk/tasks/Board.md` with the task and its dependencies.

### Lifecycle

Once a task is solved:

1. Delete the task file.
2. Remove it from `desk/tasks/Board.md`.
3. Update `changelog.md`.
4. Record lasting design decisions in `wiki/adrs/` if the resolution changed architecture.
5. Do not archive resolved tasks; history belongs in git and ADRs.

### Default enforcement

- Non-trivial runtime or test work must be linked to at least one task file under `desk/tasks/`.
- Non-trivial documentation work should also use a task unless it is an explicitly structural docs-only change.
- Resolved task deletion should happen together with `desk/tasks/Board.md` update.
- `wiki-compiler check-workflow` is the operational guard for these rules.

## Fields

- `Atomization` means one task can be completed and verified by one agent in one session.
- `Contradiction check` includes overlap, conflict, and circular dependency review.
- `Structural docs-only change` means a repo-organization or documentation-topology change that does not modify runtime code or tests.

## Usage Examples

- A stale doc that should simply be deleted is handled in the legacy audit stage, not kept alive as fake implementation work.
- A multi-language scanner refactor that requires independent protocol, plugin, and runtime changes should be split into child tasks.
- A resolved task disappears from `desk/tasks/` and from `desk/tasks/Board.md` in the same logical change.
- Before committing, run `wiki-compiler check-workflow` to catch missing task links or missing `changelog.md` updates.
