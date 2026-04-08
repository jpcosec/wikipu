---
identity:
  node_id: "doc:wiki/drafts/estructura_propuesta_para_determinista.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

```

## Details

```
determinista/
├── pyproject.toml
├── src/
│   └── determinista/
│       ├── __init__.py
│       ├── io/                      # Copia de src/core/io/
│       │   ├── __init__.py
│       │   ├── workspace_manager.py
│       │   ├── artifact_reader.py
│       │   ├── artifact_writer.py
│       │   └── provenance_service.py
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── errors/
│       │   │   ├── __init__.py
│       │   │   └── types.py
│       │   └── translation/
│       │       ├── __init__.py
│       │       └── service.py
│       ├── contracts/
│       │   ├── __init__.py
│       │   └── render.py            # RenderStateEnvelope
│       ├── nodes/
│       │   ├── __init__.py
│       │   ├── translate_if_needed/
│       │   │   ├── __init__.py
│       │   │   └── logic.py
│       │   ├── render/
│       │   │   ├── __init__.py
│       │   │   ├── contract.py
│       │   │   └── logic.py
│       │   └── package/
│       │       ├── __init__.py
│       │       ├── contract.py
│       │       └── logic.py
│       └── compat/
│           └── __init__.py          # Adaptadores para PhD2
└── tests/
    ├── test_io/
    ├── test_translation/
    └── test_nodes/
```

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.