---
identity:
  node_id: "doc:wiki/standards/artifacts/wiki_node.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "extends"}
  - {target_id: "doc:wiki/standards/house_rules.md", relation_type: "implements"}
compliance:
  status: "implemented"
  failing_standards: []
---

The fundamental knowledge unit. Every file in `wiki/` is a wiki node. Its frontmatter is the machine-readable identity and graph contract; its body is the human-readable content. Together they make the node independently traversable by both agents and humans.

## Rule Schema

### Frontmatter

```yaml
identity:
  node_id: str        # required — "doc:<path_from_repo_root>"; must match the file's actual path
  node_type: str      # required — one of: concept | how_to | doc_standard | adr | reference | faq | index
edges:                # optional — omit if the node has no known relations yet
  - target_id: str    # "doc:<path>" | "file:<path>" | "code:<path>"
    relation_type: str  # contains | depends_on | reads_from | writes_to | documents | transcludes | extends | implements
compliance:
  status: str         # required — planned | scaffolding | implemented | deprecated
  failing_standards: []  # list of rule_ids not yet met; empty means compliant
```

### Body sections by `node_type`

| `node_type` | Required sections (in order) |
|---|---|
| `concept` | Abstract → Definition → Examples → Related Concepts |
| `how_to` | Abstract → Prerequisites → Steps → Verification |
| `doc_standard` | Abstract → Schema → Fields → Usage Examples |
| `adr` | Abstract → Context → Decision → Rationale → Consequences |
| `reference` | Abstract → Overview → Commands / API → Examples |
| `faq` | Abstract → Q&A pairs (`**Q:** ... **A:** ...`) |
| `index` | Abstract → Entry table (artifact or domain listing) |

**Abstract rule (applies to all types):** The first content after the frontmatter must be a 1–3 sentence plain-text paragraph stating the node's intent. No heading before it. It must stand alone as a summary.

## Fields

- `node_id` must match `"doc:" + relative_path_from_repo_root`.
- `node_type` must be one of the enum values above.
- `compliance.status` must be `implemented` only when the described thing actually exists and is current.
- A node with no edges is valid but flagged by audit as a candidate orphan.
- The abstract paragraph is mandatory. A file that starts with a heading has a missing abstract.

## Usage Examples

_See any file in `wiki/` for a concrete wiki node example._
