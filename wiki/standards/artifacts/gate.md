---
identity:
  node_id: "doc:wiki/standards/artifacts/gate.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

A human approval checkpoint that blocks execution until explicitly resolved. Gates are not separate files — they are rows in `desk/Gates.md`, the central monitor. A gate exists because a proposal requires human approval before it can be applied (ID-5). Each gate row points to the proposal that created it.

## Rule Schema

`desk/Gates.md` is a markdown table. Each row is one open gate.

### Table format

```markdown
| gate_id | proposal | opened | description | status |
|---|---|---|---|---|
| gate-001 | desk/proposals/topology-20260409-add-cleanser.md | 2026-04-09 | Add cleanser module to src/ topology | open |
```

### Field definitions

| Field | Type | Required | Description |
|---|---|---|---|
| `gate_id` | str | yes | Sequential identifier: `gate-<NNN>` |
| `proposal` | path | yes | Relative path to the proposal file in `desk/proposals/` |
| `opened` | date | yes | YYYY-MM-DD when the gate was created |
| `description` | str | yes | One-line summary of what needs approval |
| `status` | str | yes | `open` \| `approved` \| `rejected` |

## Fields

- A gate row is removed from `Gates.md` only after: the human has explicitly approved or rejected AND the proposal has been applied or discarded AND the changelog has been updated.
- Status `approved` or `rejected` is set by the human — never by an agent.
- If a proposal is split into sub-proposals after a gate is opened, the original gate stays open and each sub-proposal gets its own gate row.
- `Gates.md` with no open rows means no human decisions are pending. This is the desired state.

## Usage Examples

_To be added._
