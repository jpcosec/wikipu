---
identity:
  node_id: "doc:wiki/standards/artifacts/backlog_item.md"
  node_type: "doc_standard"
compliance:
  status: "implemented"
  failing_standards: []
---

A deferred idea not yet ready to become a task. Backlog items live in `drawers/` and are low-churn — reviewed periodically but not acted on. When the trigger condition is met, a backlog item is promoted to a task and deleted from `drawers/`.

## Rule Schema

Backlog items have no frontmatter.

### Body sections

| Section | Required | Content |
|---|---|---|
| Title (H1) | yes | Short noun phrase naming the idea |
| Added | yes | `**Added:** YYYY-MM-DD` — use absolute date, never relative |
| Description | yes | What the idea is, stated precisely |
| Why deferred | yes | What is blocking promotion, or why this is not urgent now |
| Trigger | yes | The specific condition that would promote this to a task |

## Fields

- A backlog item with no Trigger is a dead item — it will never be promoted. Either define the trigger or delete the item.
- Items older than 6 months with no trigger change are reviewed for deletion in OP-6 (Autopoietic Cycle).
- Promotion means: create a task file in `desk/tasks/`, delete the backlog file, add the task to the Board.
- Backlog items never reference `desk/` — they are ideas, not active work.

## Usage Examples

```markdown
---
identity:
  node_id: "doc:drawers/my_idea.md"
  node_type: "backlog_item"
---

# My Idea

**Added:** 2026-04-15

## Description
A new feature that would improve query performance by caching results.

## Why Deferred
Not urgent — current query speed is acceptable for now.

## Trigger
When query latency exceeds 500ms, promote to task.
```
