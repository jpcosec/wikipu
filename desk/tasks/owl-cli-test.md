---
status: open
priority: p2
depends_on: []
created: 2026-04-17
assigned_to: self
---

# OWL CLI Build Test

## Task

Test and verify OWL CLI integration works correctly.

## Test Commands

### 1. Build with OWL Export
```bash
wiki-compiler build --owl
```
**Expected:**
- `wikipu.owl` created (gitignored)
- At least 500 triples extracted

### 2. SPARQL Query
```bash
wiki-compiler query --owl "SELECT (COUNT(*) as ?c) WHERE { ?s ?p ?o }"
```
**Expected:**
- Returns count > 500

### 3. Energy with Reasoning
```bash
wiki-compiler energy --reasoning
```
**Expected:**
- Shows "Consistency: CONSISTENT"
- Shows "Reasoner: HermiT reasoner completed"

### 4. Audit Sync Check
```bash
wiki-compiler audit --sync-check
```
**Expected:**
- Reports owl_conflict findings

## Validation

All commands should complete without errors.

## References

- `wiki/reference/owl_integration.md`
- `src/wiki_compiler/owl_backend/`
- `src/wiki_compiler/owl_reasoner.py`