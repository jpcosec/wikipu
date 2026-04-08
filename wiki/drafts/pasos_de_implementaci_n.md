---
identity:
  node_id: "doc:wiki/drafts/pasos_de_implementaci_n.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

### Fase 1: Crear estructura base

## Details

### Fase 1: Crear estructura base

1. Crear directorio `determinista/` en raíz
2. Crear `pyproject.toml` con:
   - Nombre: `determinista`
   - Dependencias: `pydantic`, `deep-translator>=1.9.1`
   - Dependencias opcionales: `pathlib` (stdlib, siempre disponible)
3. Estructurar paquetes `src/determinista/*`

### Fase 2: Extraer IO Layer

4. Copiar `src/core/io/` → `determinista/src/determinista/io/`
5. Actualizar imports internos (`src.core.io` → relative imports)
6. Crear `__init__.py` con exports públicos

### Fase 3: Extraer Translation Service

7. Copiar `src/tools/translation/service.py` → `determinista/src/determinista/tools/translation/`
8. Copiar `src/tools/errors/types.py` → `determinista/src/determinista/tools/errors/`
9. Actualizar imports

### Fase 4: Extraer Contracts

10. Copiar `nodes/render/contract.py` → `determinista/src/determinista/contracts/render.py`
11. Incluir `RenderStateEnvelope`, `RenderedDocumentRef`, `RenderInputState`

### Fase 5: Extraer Nodes

12. Copiar `nodes/translate_if_needed/logic.py` → `determinista/`
13. Copiar `nodes/render/logic.py` → `determinista/`
14. Copiar `nodes/package/logic.py` → `determinista/`
15. Actualizar todos los imports a usar la library local

### Fase 6: Capa de compatibilidad con PhD2

16. Crear `determinista/compat/__init__.py` con adaptadores:
    ```python
    # Para que PhD2 pueda usar determinista sin cambios
    from determinista.io import WorkspaceManager, ArtifactReader, ArtifactWriter
    from determinista.tools.translation import translate_text
    # etc.
    ```

17. En `src/nodes/translate_if_needed/logic.py` de PhD2:
    - Agregar fallback: intentar imports de `determinista` primero, luego `src.core`
    - O mantener como está y solo usar `determinista` en proyectos externos

### Fase 7: Tests

18. Crear tests unitarios para cada módulo:
    - `tests/test_io/test_workspace_manager.py`
    - `tests/test_io/test_provenance.py`
    - `tests/test_translation/test_service.py`
    - `tests/test_nodes/test_render.py`
    - `tests/test_nodes/test_package.py`

19. Tests de integración verificando que los nodes funcionan como library

### Fase 8: Documentación

20. Crear `README.md` para `determinista/`:
    - Uso básico
    - API reference
    - Ejemplos de integración
    - Dependencias externas requeridas

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.