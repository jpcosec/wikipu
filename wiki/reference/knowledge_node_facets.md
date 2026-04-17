---
identity:
  node_id: "doc:wiki/reference/knowledge_node_facets.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/contracts/__init__.py", relation_type: "documents"}
  - {target_id: "doc:wiki/concepts/how_wikipu_works.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

This reference defines the node and facet vocabulary used throughout the Wikipu knowledge graph. Use it when you need to look up what a node type, edge, or facet field means rather than when you need an explanation of why the graph exists.

## Signature or Schema

### Core node identity

| Element | Meaning |
|---|---|
| `node_id` | Unique graph identifier such as `dir:src`, `file:src/main.py`, `code:src/main.py:run`, or `doc:wiki/Index.md` |
| `node_type` | Artifact category such as `directory`, `file`, `code_construct`, `concept`, `how_to`, `doc_standard`, `reference`, `faq`, `index`, or `adr` |

### Edge relation types

| Relation | Meaning |
|---|---|
| `contains` | Parent-child structure or domain containment |
| `depends_on` | Code or semantic dependency |
| `reads_from` | Data intake relation |
| `writes_to` | Data output relation |
| `documents` | Documentation page describes a code or doc node |
| `transcludes` | Markdown inclusion via `![[...]]` |
| `extends` | Specialization or schema inheritance |
| `implements` | A node realizes a standard or requirement |

### Facets

| Facet | Primary question | Important fields |
|---|---|---|
| `SemanticFacet` | What does this node do? | `intent`, `raw_docstring` |
| `ASTFacet` | How is this node structured? | `construct_type`, `signatures`, `dependencies` |
| `IOFacet` | What data crosses this boundary? | `medium`, `schema_ref`, `path_template` |
| `ComplianceFacet` | How complete and rule-compliant is this node? | `status`, `failing_standards`, `exemption_reason` |
| `TestMapFacet` | How is this node tested? | `test_type`, `coverage_percent` |
| `ADRFacet` | What decision shaped this node? | `decision_id`, `status`, `context_summary` |
| `GitFacet` | What git-backed state is known about this file? | `blob_sha`, `created_at_commit`, `last_modified_commit`, `last_modified_author`, `status` |

### Compliance status values

| Status | Meaning |
|---|---|
| `planned` | Designed or queued, not implemented |
| `scaffolding` | Structural shell exists |
| `mocked` | Logic exists but still uses fake dependencies |
| `implemented` | Real implementation exists |
| `tested` | Automated tests cover the behavior |
| `exempt` | Explicitly excluded from normal compliance tracking |

## Fields

- `node_id` identifies a concrete graph node and includes its namespace prefix.
- `node_type` classifies the artifact represented by the node.
- `Relation` describes the semantic meaning of an edge between two nodes.
- `Facet` names a dimension of metadata that can be attached independently to a node.
- `Compliance status` tracks implementation maturity and standards conformance.

## Usage Examples

- Inspect the concrete schema in `src/wiki_compiler/contracts/__init__.py`.
- Rebuild the graph with `wiki-compiler build` after changing node structure or docs.
- Query nodes with `wiki-compiler query --type get_node --node-id <node_id>`.
- Use `wiki-compiler context --nodes "<node_id>"` to render focused graph context.

```text
doc:wiki/reference/knowledge_node_facets.md
file:src/wiki_compiler/contracts/__init__.py
code:src/wiki_compiler/scanner.py:scan_python_sources
```

```bash
wiki-compiler query --type get_node --node-id file:src/wiki_compiler/contracts/__init__.py
```
