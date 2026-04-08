---
identity:
  node_id: "doc:wiki/drafts/1_design_philosophy_determinism_and_decoupling.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md", relation_type: "documents"}
---

The system is governed by absolute data transparency and interface independence.

## Details

The system is governed by absolute data transparency and interface independence.

### Progressive Interface Architecture (CLI > API > UI)

- All functionality must be born in Backend/CLI as a deterministic function.
- The API acts exclusively as a data bridge to the filesystem.
- The UI is a visualization and correction layer, never the primary business logic.

### Separation of Functions

- **Deterministic Functions**: File processing, I/O, PDF rendering, and provenance handling (`src/core/`).
- **AI-Based Functions**: LangGraph nodes that interact with LLMs (`src/nodes/`). Must be replaceable and isolated from persistence logic.
- **Anti-Hardcoding**: Strict use of Contracts (`contract.py`) in each node to define inputs and outputs, allowing the pipeline to be modular and scalable.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/product/03_methodology.md`.