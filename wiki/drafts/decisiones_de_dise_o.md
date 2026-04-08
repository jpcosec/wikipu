---
identity:
  node_id: "doc:wiki/drafts/decisiones_de_dise_o.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

### Opción A: Dependency Inversion (Recomendada)

## Details

### Opción A: Dependency Inversion (Recomendada)

Los nodes aceptan dependencias via constructor o parámetros:

```python
# En lugar de importar directamente:
from determinista.io import WorkspaceManager

# El nodo recibe las dependencias:
def run_logic(
    state: Mapping[str, Any],
    workspace: WorkspaceManager | None = None,
    translator_factory: TranslatorFactory | None = None,
) -> dict[str, Any]:
    workspace = workspace or WorkspaceManager()
    # ...
```

**Ventajas**: Testeable, flexible, separable
**Desventajas**: Más código en cada llamada

### Opción B: Direct Import

Los nodes importan directamente desde `determinista.io` como cualquier library.

**Ventajas**: Menos código, API más limpia
**Desventajas**: Menos flexible para testing

### Recomendación

Usar **Opción A** para `translate_if_needed` (donde ya existe `translator_factory` como parámetro) y **Opción B** para `render` y `package` (que solo usan I/O básico).

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.