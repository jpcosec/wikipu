---
identity:
  node_id: "doc:wiki/drafts/module_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/core/README.md", relation_type: "documents"}
---

```

## Details

```
src/core/
├── ai/                    # LLM configuration and tracing
├── application/          # Application workflows (autoapply)
├── graph/                # Graph state definitions
│   └── state.py          # GraphState dataclass
├── io/                   # I/O utilities (centralized, not fully migrated)
├── review/               # Review parsing and decision services
├── round_manager.py       # Round management for regeneration
├── scraping/             # Scraping facade and adapters
├── text/                 # Text processing (span resolver)
├── tools/                 # Tools (translation, rendering, review)
└── round_manager.py      # Round management
```

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/runtime/core/README.md`.