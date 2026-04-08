---
identity:
  node_id: "doc:wiki/drafts/verificaci_n.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

```bash

## Details

```bash
# Instalar como editable
pip install -e determinista/

# Importar desde cualquier proyecto
from determinista import translate_text
from determinista.nodes.render import run_logic as render
from determinista.nodes.package import run_logic as package

# Correr tests
pytest determinista/tests/ -v
```

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.