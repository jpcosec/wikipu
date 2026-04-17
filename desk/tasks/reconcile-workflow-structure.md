---
status: open
priority: p1
depends_on: []
created: 2026-04-17
assigned_to: self
---

# Reconcile workflow/ with Wikipu Structure

## Problem

Two parallel workflow representations exist:

1. **Generic `workflow/`** — portable template with AGENTS.md, STANDARDS.md, instructions/
2. **Wikipu `wiki/standards/house_rules.md`** — OP-1 through OP-10, WK rules, NAV rules

They overlap but use different vocabularies:
- workflow/: Supervisor, Executor, Pill, Atomization, Board
- wikipu/: self, wiki-compiler, desk, topology, energy

## Analysis

### What workflow/ does well:
- Clear role definitions (Supervisor/Executor)
- Explicit rituals with steps
- Context pills for rationale
- One task = one commit traceability

### What wikipu/standards/ does well:
- Layered rule organization (ID, MA, NAV, OP, WK, CS)
- Rule IDs for machine reference (ID-1, OP-6, WK-3)
- Integration with the 4-zone model
- Energy-based health measurement

### What both need:
- Task tracking → use wikipu's desk/ (already exists)
- Context pills → use wikipu's structure
- Agent protocols → model in OWL ontology
- Commit triggers → already defined

## Proposed Reconciliation

### 1. Deprecate workflow/AGENTS.md and workflow/STANDARDS.md

Move relevant concepts into wikipu's ontology:

| workflow/ Concept | Wikipu Concept |
|------------------|----------------|
| Supervisor role | OWL class `workflow:Supervisor` |
| Executor role | OWL class `workflow:Executor` |
| Pill | OWL annotation on Task |
| Board | SPARQL query result |
| Atomization | Ritual class |
| Initialization Ritual | `workflow:InitRitual` individual |
| Execution Ritual | `workflow:ExecRitual` individual |

### 2. Keep workflow/instructions/ as derived

Move detailed instructions to wiki/ reference:

```
workflow/instructions/          →  wiki/reference/workflows/
supervisor-instructions.md     →  wiki/reference/workflows/supervisor.md
executor-instructions.md       →  wiki/reference/workflows/executor.md
pill-audit-instructions.md     →  wiki/reference/workflows/pill-audit.md
context_compiler-instructions.md →  wiki/reference/workflows/context-compiler.md
```

### 3. Use desk/ for tasks (already correct)

No change needed — desk/tasks/ and desk/tasks/Board.md are wikipu's task surface.

### 4. Model rituals in OWL

Per ADR-004, model rituals as OWL individuals with steps as properties.

### 5. Keep init_instructions.md as reference

The `init_instructions.md` is useful for bootstrapping NEW projects, not wikipu itself.

## Migration Steps

1. Create `wiki/reference/workflows/` directory
2. Move instructions to wiki/
3. Create `wiki/concepts/workflow.md` as the OWL ontology anchor
4. Deprecate `workflow/AGENTS.md` and `workflow/STANDARDS.md` (mark as "superseded by wiki/ontology")
5. Update gitignore to exclude derived workflow instructions
6. Update AGENTS.md to point to wiki/ontology

## Verification

```bash
# After migration:
ls wiki/reference/workflows/  # Should contain supervisor.md, executor.md, etc.
cat workflow/AGENTS.md  # Should say "DEPRECATED - see wiki/concepts/workflow.md"
```

## Related

- `wiki/adrs/004_workflow_as_ontology.md`
- `wiki/standards/house_rules.md`
- `wiki/concepts/workflow.md` (to be created)
