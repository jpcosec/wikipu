---
identity:
  node_id: "doc:wiki/standards/artifacts/adr.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/standards/artifacts/wiki_node.md", relation_type: "extends"}
compliance:
  status: "implemented"
  failing_standards: []
---

An Architectural Decision Record captures a design decision that shaped the system — the context that forced it, what was decided, and what consequences followed. ADRs are permanent: once accepted, they are never deleted, only superseded. They live in `wiki/adrs/` and are part of the graph.

## Rule Schema

### Frontmatter

```yaml
identity:
  node_id: str      # required — "doc:wiki/adrs/<NNN>_<slug>.md"
  node_type: "adr"  # required — always "adr"
adr:
  decision_id: str  # required — zero-padded integer matching filename prefix, e.g. "003"
  status: str       # required — proposed | accepted | deprecated | superseded
  superseded_by: str  # conditional — "doc:wiki/adrs/<NNN>_<slug>.md"; required when status = superseded
edges:              # required — at least one edge pointing to the node(s) this decision affectsrelation_type: documents
compliance:
  status: "implemented"   # ADRs are always implemented; they document past decisions
  failing_standards: []
```

### Body sections

| Section | Required | Content |
|---|---|---|
| Abstract | yes | 1–3 sentences: what was decided and why it matters |
| Context | yes | What situation or problem forced this decision |
| Decision | yes | What was decided, stated precisely |
| Rationale | yes | Why this option over discarded alternatives |
| Consequences | yes | What changes, what becomes easier, what becomes harder |

## Fields

- Filename must be `<NNN>_<slug>.md` where `NNN` matches `adr.decision_id`.
- A superseded ADR must keep its body intact and add `superseded_by`.
- ADRs are never deleted — only marked `deprecated` or `superseded`.
- At least one `documents` edge is required; an ADR with no edges is an orphan decision.

## Usage Examples

_See `wiki/adrs/002_documentation_consolidation.md` for a complete ADR example._
