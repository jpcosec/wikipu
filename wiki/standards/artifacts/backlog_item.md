---
identity:
  node_id: "doc:wiki/standards/artifacts/backlog_item.md"
  node_type: "doc_standard"
compliance:
  status: "implemented"
  failing_standards: []
---

A deferred idea that is not yet ready to become an issue. Backlog items live in `drawers/` and are low-churn — they are reviewed periodically but not acted on. When the trigger condition is met, a backlog item is promoted to an issue and deleted from `drawers/`.

## Rule Schema

Backlog items have no frontmatter.

### Body sections

| Section | Required | Content |
|---|---|---|
| Title (H1) | yes | Short noun phrase naming the idea |
| Added | yes | `**Added:** YYYY-MM-DD` — use absolute date, never relative |
| Description | yes | What the idea is, stated precisely |
| Why deferred | yes | What is blocking promotion, or why this is not urgent now |
| Trigger | yes | The specific condition that would promote this to an issue |

## Fields

- A backlog item with no Trigger is a dead item — it will never be promoted. Either define the trigger or delete the item.
- Items older than 6 months with no trigger change are reviewed for deletion in OP-6 (Autopoietic Cycle).
- Promotion means: create an issue file in `desk/issues/`, delete the backlog file, add the issue to the Board.
- Backlog items never reference `desk/` — they are ideas, not active work.
