# Plan: Extracción de nodos deterministas a library "determinista"

## Objetivo

Crear una library Python independiente `determinista` que contenga los nodos `translate_if_needed`, `render` y `package`, junto con la infraestructura necesaria para funcionar como una library reutilizable en proyectos externos.

## Estado actual

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

## Estructura propuesta para `determinista/`

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

## Pasos de implementación

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

## Decisiones de diseño

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

## Compatibilidad con PhD2

PhD2 puede seguir usando `src/core/io/` internamente. La library `determinista` es para consumo externo. Opcionalmente, podemos migrar PhD2 a usar `determinista` internamente para evitar duplicación.

### Estrategia de migración gradual

1. **Fase inicial**: `determinista` existe pero PhD2 sigue usando `src/core/`
2. **Fase intermedia**: PhD2 importa desde `determinista` via layer de compatibilidad
3. **Fase final**: `src/core/` se convierte en re-export de `determinista`

## Verificación

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

## Timeline estimado

- Fase 1-3: 30 minutos
- Fase 4-5: 45 minutos
- Fase 6-7: 30 minutos
- Fase 8: 15 minutos
- **Total: ~2 horas**

## Alternativas consideras

1. **No extraer, solo documentar**: Mantener todo en PhD2, documentar que son reutilizables
   - *Rechazado*: El usuario específicamente pidió crear una library separada

2. **Git worktree**: Crear un git worktree del repo
   - *Rechazado*: No tiene sentido para una library Python; los git worktrees son para trabajo paralelo en el mismo repo

3. **Monorepo style**: Crear workspace con PhD2 y determinista como packages separados
   - *Considerar*: Más complejo pero podría ser valioso a largo plazo
   - *Decisión*: Mantener como packages independientes por ahora

## Notas adicionales

- La library no debe modificar `core/` durante ejecución (constraint de Pulpo)
- `package` depende de `render.contract.RenderStateEnvelope` — debe mantenerse sincronizado
- `translate_if_needed` usa `deep-translator` que debe ser dependency opcional o lazy-imported
