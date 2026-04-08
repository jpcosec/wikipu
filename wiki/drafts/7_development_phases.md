---
identity:
  node_id: "doc:wiki/drafts/7_development_phases.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md", relation_type: "documents"}
---

Each phase delivers a working vertical slice (schema → engine → CLI → API → UI):

## Details

Each phase delivers a working vertical slice (schema → engine → CLI → API → UI):

| Phase | Engine | CLI | UI | Delivers |
|-------|--------|-----|-----|----------|
| **1** | Scanner + Graph Builder | `init`, `scan`, `lint`, `graph`, `serve` | Graph Explorer | See your project as a navigable network |
| **2** | Drift Detector | `drift`, `verify` | Drift Dashboard | Know what's broken or stale |
| **3** | Template Engine | `new`, `runbook` | Document Editor | Create and edit with templates |
| **4** | Packet Compiler | `packet` | Task Generator | Produce precise agent instructions |
| **5** | Correction Tracker | — | Correction View | Review and improve over time |
| **6** | MCP Protocol | — | — | Add MCP protocol to existing `serve` |

`doc-router serve` ships in Phase 1 (for the UI). Phase 6 adds MCP protocol support to the same server — no new command needed.

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/doc-router-design.md`.