---
pill_type: guardrail
scope: global
language: en
nature: context
bound_to: owl-phase1-parallel-run, owl-phase2-quadstore-primary, owl-phase3-reasoning, owl-phase4-full-migration
created: 2026-04-17
lifecycle: current
---

# OWL Integration Global Constraints

## Hard Constraints (Must Never Violate)

### 1. Java Runtime Required
```
HermiT/Pellet reasoners require JVM.
Before sync_reasoner(), verify:
  import subprocess
  result = subprocess.run(["java", "-version"], capture_output=True)
  if result.returncode != 0:
      raise RuntimeError("Java not found")
```

### 2. Quadstore is Derivative (Phase 1-3)
OWL quadstore is **derived** from Markdown files, not source of truth.
Markdown → OWL export is one-way until Phase 4.

### 3. SyncGate Cannot Be Bypassed
All Pydantic ↔ OWL sync must go through `SyncGate` class.
No direct `default_world.add()` in application code.

### 4. SHACL Gate on All Writes
Every triple added to quadstore must pass SHACL validation.
Exception: triples added by `sync_reasoner()` (reasoner output).

### 5. Immutable Ontology IRI
Base IRI `http://wikipu.org/ontology/` is fixed.
Changing it invalidates all existing individuals.

## Soft Constraints (Should Avoid)

### 6. No Large Ontology Loads in Hot Path
Loading Gene Ontology (~170MB) must be async/deferred.
Do not load on every `wiki-compiler` command.

### 7. SQLite Exclusive Mode by Default
`exclusive=True` for faster performance.
Only use `exclusive=False` if multiple processes need access.

### 8. Commit After Every Build
Per OP-9: Build output (quadstore) must be committed.
Do not leave quadstore drifted from git state.

## Phase-Specific Constraints

| Phase | Constraint |
|-------|-----------|
| 1 | OWL read-only, Markdown is source |
| 2 | Bidirectional sync via SyncGate |
| 3 | SHACL gates all writes |
| 4 | OWL is source, Markdown is export |

## Reference

- `wiki/adrs/003_owl_integration.md` (Consequences section)
- `wiki/standards/house_rules.md` (OP-9: Build Synchronization)
