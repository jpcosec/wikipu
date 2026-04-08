---
identity:
  node_id: "doc:wiki/drafts/1_orthogonal_dimensions_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md", relation_type: "documents"}
---

The repository is treated as a **3D Matrix** where information lives at exact coordinates. The agent only requests coordinates, the system assembles files.

## Details

The repository is treated as a **3D Matrix** where information lives at exact coordinates. The agent only requests coordinates, the system assembles files.

### Axes

| Axis | Name | Values |
|------|------|--------|
| **X** | Technical Domain | `ui`, `api`, `pipeline`, `core`, `data`, `policy` |
| **Y** | Pipeline Stage | `scrape`, `translate`, `extract`, `match`, `strategy`, `drafting`, `render`, `package` |
| **Z** | Resolution Layer | `docs`, `code` |
| **W** | Temporal State | `runtime` (current docs), `plan` (future designs) |

### Domain (Axis X)

| Domain | Description |
|--------|-------------|
| `ui` | React frontend, components, view specifications, graph editing |
| `api` | FastAPI endpoints, network contracts, Pydantic models |
| `pipeline` | LangGraph logic, node flows, semantic gates, transitions |
| `core` | Deterministic functions, local I/O, parsing, PDF rendering |
| `data` | Local-first structure, JSON schemas, Evidence Tree |
| `policy` | Business rules, ethics, usage limits |

### Stage (Axis Y)

```
scrape → translate → extract → match → strategy → drafting → render → package
```

### Content Nature (Sub-axis)

| Nature | Description |
|--------|-------------|
| `philosophy` | Why it exists, intention, design |
| `implementation` | How it's technically implemented |
| `development` | Guides for developing/extending |
| `testing` | Tests, verifications, contracts |
| `expected_behavior` | Observable behavior, edge cases |

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md`.