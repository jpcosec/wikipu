---
identity:
  node_id: "doc:wiki/drafts/node_registry.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md", relation_type: "documents"}
---

| Node | Source | Execution | Description |

## Details

| Node | Source | Execution | Description |
|------|--------|-----------|-------------|
| `scrape` | `src/nodes/scrape/logic.py` | NLLM-ND | Fetch job posting URL |
| `translate_if_needed` | `src/nodes/translate_if_needed/logic.py` | NLLM-ND | Conditionally normalize language |
| `extract_understand` | `src/nodes/extract_understand/logic.py` | LLM | Extract structured requirements |
| `match` | `src/nodes/match/logic.py` | LLM | Match requirements to CV evidence |
| `review_match` | `src/nodes/review_match/logic.py` | NLLM-D | Parse review decision, route flow |
| `generate_documents` | `src/nodes/generate_documents/logic.py` | LLM + D | Generate CV/letter/email drafts |
| `render` | `src/nodes/render/logic.py` | NLLM-D | Copy to render artifacts |
| `package` | `src/nodes/package/logic.py` | NLLM-D | Package final deliverables |

### Execution Class Legend

| Class | Meaning |
|-------|---------|
| `LLM` | Uses LLM for generation |
| `NLLM-D` | Non-LLM, deterministic |
| `NLLM-ND` | Non-LLM, bounded nondeterministic |

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/pipeline/README.md`.