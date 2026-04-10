---
identity:
  node_id: "doc:wiki/standards/artifacts/board.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

The operational entry point for a `desk/` domain. A Board tracks the active work tree for one domain: what is being done, in what order, with what dependencies. It is mutable and updated continuously as work progresses. Resolved items are deleted from it, not archived.

## Rule Schema

Boards have no frontmatter. They are operational artifacts, not graph nodes.

### Body sections

| Section | Required | Content |
|---|---|---|
| Title (H1) | yes | `# <Domain> Board` |
| Current State | yes | 1–3 sentences: where the domain stands right now |
| Priority Roadmap | yes | Numbered items grouped into named phases; each item links to its issue file |
| Dependency Summary | yes | Bullet list of cross-item blocking relationships |
| Parallelization Map | yes | Which items within each phase can run concurrently |

### Priority Roadmap item format

```
<N>. <path/to/issue.md>
   • <one-line description>
   • Depends on: <path/to/other.md> | none
```

### Parallelization Map format

```
Phase N  [item][item]  — all parallel
Phase N  [item] then [item]  — sequential
```

## Fields

- One Board per `desk/` domain — no domain has two Boards.
- Items are identified by their issue file path, not by title, to prevent drift.
- An item stays on the Board until its issue file is deleted. Deletion = resolution.
- All four sections are mandatory. A Board missing any section is malformed.

## Usage Examples

_To be added._
