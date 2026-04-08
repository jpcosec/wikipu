---
identity:
  node_id: "doc:wiki/knowledge_node_facets.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/contracts.py"
    relation_type: "documents"
  - target_id: "doc:wiki/how_it_works.md"
    relation_type: "documents"
---

# Knowledge Node Facets

A `KnowledgeNode` is the universal building block of the graph. Its core is fixed (`SystemIdentity` + `edges`), but its meaning comes from **facets** — optional, independently injectable dimensions of knowledge.

Each facet answers a different question about the node.

---

## Immutable Base

### `SystemIdentity`
*Who is this node?*

| Field | Type | Description |
|---|---|---|
| `node_id` | `str` | Unique absolute identifier. Prefix convention: `dir:`, `file:`, `code:`, `doc:` |
| `node_type` | enum | `directory`, `file`, `code_construct`, `doc_standard`, `concept` |

### `Edge`
*How does this node relate to others?*

| `relation_type` | Meaning |
|---|---|
| `contains` | Hierarchy — parent owns child (e.g. `dir:src` → `file:src/main.py`) |
| `depends_on` | Code import dependency |
| `reads_from` | Consumes data from another node |
| `writes_to` | Produces data into another node |
| `documents` | A doc node that describes a code node |
| `transcludes` | Atomic embedding — DRY wiki inclusion (`![[node]]`) |

---

## Configurable Facets

### `SemanticFacet`
*What does this node do?*

Extracted from module docstrings or `README.md` files. Answers the "why" question.

| Field | Source |
|---|---|
| `intent` | First non-empty line of module/class docstring, or README heading |
| `raw_docstring` | Full docstring as written in code |

---

### `ASTFacet`
*How is this node structured?*

Extracted by static analysis of Python source files.

| Field | Description |
|---|---|
| `construct_type` | `function`, `class`, or `script` |
| `signatures` | Method/function signatures as strings |
| `dependencies` | Internal imports detected (e.g. `from .contracts import KnowledgeNode`) |

---

### `IOFacet`
*What data does this node consume or produce?*

A node can have multiple `io_ports`. Each port describes one data channel.

| Field | Description |
|---|---|
| `medium` | `memory` (in-process), `disk` (file system), `network` (HTTP/socket) |
| `schema_ref` | Name of the Pydantic model that governs this data, if any |
| `path_template` | File path pattern, if `medium` is `disk` (e.g. `output/{source}/data.json`) |

Detected from: docstring `input:`/`output:` annotations and AST inference of `open()` / `Path(...).read_text()` calls.

---

### `ComplianceFacet`
*How complete and rule-compliant is this node?*

Tracks adherence to `wiki/standards/00_house_rules.md`. The lifecycle progresses linearly:

| Status | Meaning |
|---|---|
| `planned` | Mentioned in `future_docs/` or `plan_docs/`, no code yet |
| `scaffolding` | Required files exist (`contracts.py`, `__init__.py`, `README.md`) |
| `mocked` | Logic runs against fakes/stubs, no real dependencies |
| `implemented` | Connected to real dependencies, production-ready |
| `tested` | Automated tests cover the node's behaviour |
| `exempt` | Excluded via `.wikiignore` or `@wiki_exempt` decorator |

Additional fields:

| Field | Description |
|---|---|
| `failing_standards` | List of `wiki/standards/` rules currently not met |
| `exemption_reason` | Required when `status` is `exempt` |

---

### `TestMapFacet`
*How is this node tested?*

| Field | Description |
|---|---|
| `test_type` | `unit`, `integration`, `e2e`, or `manual_review` |
| `coverage_percent` | Float 0–100, if measured. `null` if not tracked. |

---

### `ADRFacet`
*What design decisions shaped this node?*

Links a node to an Architectural Decision Record in `wiki/adrs/`.

| Field | Description |
|---|---|
| `decision_id` | Unique ADR identifier (e.g. `001`) |
| `status` | `proposed`, `accepted`, `deprecated`, `superseded` |
| `context_summary` | Why this decision was made, including discarded alternatives |

---

## Which Nodes Get Which Facets?

| Node type | Typical facets |
|---|---|
| `directory` | `semantics`, `compliance` |
| `file` (Python) | `semantics`, `ast`, `io_ports`, `compliance`, `test_map` |
| `code_construct` | `semantics`, `ast`, `io_ports`, `compliance`, `test_map` |
| `doc_standard` | `semantics`, `adr` |
| `concept` | `semantics`, `adr` |

All facets are optional. The scanner injects what it can detect; the rest can be declared manually via YAML frontmatter in wiki nodes.
