---
identity:
  node_id: "doc:wiki/standards/artifacts/Index.md"
  node_type: "index"
compliance:
  status: "implemented"
  failing_standards: []
---

Canonical structure definitions for every artifact type in the Wikipu ecosystem. Each document defines the frontmatter schema and required body sections for one artifact. These definitions are the ground truth for authoring, validation, and automated checking.

| Artifact | File | Zone | Frontmatter |
|---|---|---|---|
| Wiki Node | `wiki_node.md` | `wiki/` | yes |
| ADR | `adr.md` | `wiki/adrs/` | yes |
| Proposal | `proposal.md` | `desk/proposals/` | yes |
| Board | `board.md` | `desk/` | no |
| Task | `task.md` | `desk/tasks/` | no |
| Gate | `gate.md` | `desk/Gates.md` | row format |
| Backlog Item | `backlog_item.md` | `drawers/` | no |
