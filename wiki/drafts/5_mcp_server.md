---
identity:
  node_id: "doc:wiki/drafts/5_mcp_server.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

`doc-router serve` exposes the backend as MCP tools:

## Details

`doc-router serve` exposes the backend as MCP tools:

| Tool | Description |
|------|-------------|
| `query_route` | Find docs/code by domain, stage, nature |
| `check_drift` | Run drift detection, return report |
| `get_context` | Given a file/symbol, return its full context graph |
| `generate_packet` | Compile a task packet from description |
| `get_runbook` | Generate runbook for a domain/stage |
| `list_templates` | Available doc/code templates |
| `scaffold` | Create new doc/code from template |

MCP resources expose the graph itself — clients can browse nodes and edges directly.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.