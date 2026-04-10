---
identity:
  node_id: "doc:wiki/standards/artifacts/proposal.md"
  node_type: "doc_standard"
compliance:
  status: "implemented"
  failing_standards: []
---

A change proposal submitted for review before any action is taken. Proposals are operational artifacts — they live in `desk/proposals/`, are deleted when applied or rejected, and leave a trace only in the changelog and (when a design decision was involved) in an ADR.

## Rule Schema

### Frontmatter

```yaml
proposal_id: str          # required — "<type>-<YYYYMMDD>-<slug>", e.g. "topology-20260409-add-cleanser"
proposal_type: str        # required — topology | cleansing | editorial
requires_human_approval: bool  # required — true if the change crosses the topology boundary (ID-5)
status: str               # required — draft | submitted | approved | rejected | applied
opened: str               # required — YYYY-MM-DD
resolved: str             # conditional — YYYY-MM-DD; required when status = approved | rejected | applied
```

### Body sections

| Section | Required | Content |
|---|---|---|
| Abstract | yes | 1–3 sentences: what this proposes and why |
| Changes | yes | Numbered list of specific, reversible actions |
| Rationale | yes | Why this change is necessary now |
| Risk and Reversal | yes | What could go wrong; exact `git revert` or rollback procedure |
| Resolution | conditional | Required when status ≠ draft — who approved/rejected, what was applied |

## Fields

- `requires_human_approval: true` is mandatory for any change that cannot be fully reversed by `git revert` or that propagates outside `wiki/`, `desk/`, or `src/`.
- `Changes` must be a numbered list, not prose — each item must be independently verifiable.
- A proposal at `status: applied` must be deleted from `desk/proposals/` and its outcome recorded in the changelog.
- If the proposal involved a design decision, create an ADR before deleting the proposal.

## Usage Examples

_To be added._
