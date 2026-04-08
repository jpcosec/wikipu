---
identity:
  node_id: "doc:wiki/drafts/workflow_rules.md"
  node_type: "doc_standard"
edges:
  - {target_id: "raw:raw/docs_postulador_ui/plan/01_ui/README.md", relation_type: "documents"}
---

### Per-Spec Completion Checklist

## Details

### Per-Spec Completion Checklist

1. **Implementar** según spec en `specs/`
2. **Verificar** Definition of Done
3. **Ejecutar E2E** tests (TestSprite)
4. **Commit** con mensaje requerido (ver abajo)
5. **Changelog** — agregar entrada en `changelog.md`
6. **Checklist** — marcar `[x]` en `index_checklist.md`

### Commit Message Format

```bash
feat(ui): implement <view name> (<spec-id>)

- <component 1>
- <component 2>
...
- Connected to <hook names>
```

### Changelog Entry Format

```markdown

Generated from `raw/docs_postulador_ui/plan/01_ui/README.md`.