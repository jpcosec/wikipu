---
identity:
  node_id: doc:wiki/concepts/q6_how_is_git_used.md
  node_type: concept
edges:
- target_id: raw:raw/methodology_synthesis_extended.md
  relation_type: documents
compliance:
  status: implemented
  failing_standards: []
source:
  source_path: raw/methodology_synthesis_extended.md
  source_hash: 0eaf49dde8b77f6999c8e390207549968bc290d82d4774999f7136fecc61fb30
  compiled_at: '2026-04-14T16:50:28.663725'
  compiled_from: wiki-compiler
---

**Commit message format (doc_methodology / PhD 2.0):**

## Definition

**Commit message format (doc_methodology / PhD 2.

## Examples

- <component 1>
- <component 2>
- TestSprite: Passed | ID-123
- <component 1>
- <component 2>

## Related Concepts

- [[Index]]
- [[core_philosophy]]

## Details

**Commit message format (doc_methodology / PhD 2.0):**
```
<type>(<domain>): <description> (<spec-id>)

- <component 1>
- <component 2>
- TestSprite: Passed | ID-123
```

`<type>`: feat, fix, docs, refactor, chore
`<domain>`: ui, pipeline, core, api, data, policy
`<spec-id>`: mandatory — traces the commit back to the plan that authorized it

**Commit format (postulador UI):**
```
feat(ui): implement <view name> (<spec-id>)

- <component 1>
- <component 2>
- Connected to <hook names>
```
Plus a changelog entry and a checklist mark in `index_checklist.md`.

**Enforcement (doc_methodology):**
- `commit-msg` hook: blocks commit without valid format or TestSprite evidence
- `pre-push` hook: blocks push if `pytest`, `npm run typecheck`, or `npm run lint` fail
- GitHub branch protection: requires 1+ approval, CI must pass, no bypass even for admins

**postulador (lighter):** `pytest` as the mandatory verification baseline. No commit-msg hook, but changelog update is mandatory for major changes.

**Tracking docs are updated in the same commit as implementation changes** (postulador_langgraph refactor governance rule). No split "update docs later" commits.

**Branch conventions:** Not explicitly documented in any project. Implied: feature branches, PR-based workflow, no direct pushes to main.

**Git as audit trail:** The drift diagnostics doc (cotizador) uses exact commit hashes and dates to reconstruct the timeline of when and why architecture diverged. Git is the source of truth for historical decisions, not a separate changelog tool (though changelog.md is maintained for human-readable summaries).

**Finding:** Git is used as both an enforcement mechanism (hooks) and an audit trail (commit history documents what changed and why, commit messages reference the spec that authorized the change). The `(spec-id)` in commit messages is the link between git history and the planning system.

---

Generated from `raw/methodology_synthesis_extended.md`.
