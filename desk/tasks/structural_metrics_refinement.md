---
identity:
  node_id: "doc:wiki/desk/tasks/structural_metrics_refinement.md"
  node_type: "doc_task"
compliance:
  status: "pending"
  failing_standards: []
---

**Added:** 2026-04-18

**Description:**

Refinar y mejorar la métrica de estructura determinista `FFT(Markov(Structure(Code)))` desarrollada en `src/structural_abstraction/`.

**Why deferred:**

- La implementación actual funciona pero necesita más validación
- Hay warnings de numpy en algunos casos edge
- Falta integrar al sistema de energía

**Trigger:**

Cuando se necesite evaluar calidad de código o detectar código que necesita reordenamiento.

## Tasks

- [ ] Validar con más ejemplos de clean vs spaghetti code
- [ ] Manejar archivos con pocas estructuras (evitar warnings)
- [ ] Integrar en `src/wiki_compiler/energy.py`
- [ ] Crear CLI command para análisis rápido
- [ ] Probar para detectar archivos que necesitan reordenamiento
- [ ] Documentar en `deterministic_structure_measuring.md`

## Notes

Pipeline actual:
```
Code → AST → Structural symbols → N-gram → NLL → FFT → Spectrum comparison
```

Archivos relacionados:
- `src/structural_abstraction/__init__.py`
- `src/markov_entropy/__init__.py`  
- `src/wiki_compiler/face/__init__.py`
- `deterministic_structure_measuring.md`