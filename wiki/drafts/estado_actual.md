---
identity:
  node_id: "doc:wiki/drafts/estado_actual.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

### Dependencias de cada nodo

## Details

### Dependencias de cada nodo

| Nodo | Dependencias src/core/ | Dependencias externas |
|------|------------------------|----------------------|
| `translate_if_needed` | `core/tools/translation/service.py` | `deep-translator` |
| `render` | `core/io/` (5 clases) | Ninguna |
| `package` | `core/io/` (5 clases) + `nodes/render/contract.py` | Ninguna |

### Infraestructura compartida requerida

1. **IO Layer** (`src/core/io/`):
   - `WorkspaceManager` — path validation y construcción
   - `ArtifactReader` — lectura de archivos y JSON
   - `ArtifactWriter` — escritura atómica con fsync
   - `ProvenanceService` — hashing SHA256
   - `ObservabilityService` — snapshots de ejecución

2. **Translation Service** (`src/tools/translation/`):
   - `translate_text()` — traducción con chunking y retry
   - `translate_fields()` — traducción de campos específicos

3. **Error Types** (`src/tools/errors/`):
   - `ToolFailureError`
   - `ToolDependencyError`

4. **Contracts**:
   - `nodes/render/contract.py` → `RenderStateEnvelope` (usado por `package`)

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.