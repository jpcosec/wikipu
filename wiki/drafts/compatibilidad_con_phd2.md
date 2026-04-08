---
identity:
  node_id: "doc:wiki/drafts/compatibilidad_con_phd2.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_langgraph/plan/determinista_library.md", relation_type: "documents"}
---

PhD2 puede seguir usando `src/core/io/` internamente. La library `determinista` es para consumo externo. Opcionalmente, podemos migrar PhD2 a usar `determinista` internamente para evitar duplicación.

## Details

PhD2 puede seguir usando `src/core/io/` internamente. La library `determinista` es para consumo externo. Opcionalmente, podemos migrar PhD2 a usar `determinista` internamente para evitar duplicación.

### Estrategia de migración gradual

1. **Fase inicial**: `determinista` existe pero PhD2 sigue usando `src/core/`
2. **Fase intermedia**: PhD2 importa desde `determinista` via layer de compatibilidad
3. **Fase final**: `src/core/` se convierte en re-export de `determinista`

Generated from `raw/docs_postulador_langgraph/plan/determinista_library.md`.