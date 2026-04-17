---
status: completed
priority: p2
depends_on: [owl-phase2-quadstore-primary]
created: 2026-04-17
completed: 2026-04-17
assigned_to: self
---

# Phase 3: Reasoning Integration

## Objective

Add `sync_reasoner()` to energy/audit cycle. Replace manual drift detection with HermiT/Pellet consistency checking.

## Tasks

- [ ] Integrate `sync_reasoner()` into `wiki-compiler energy` command
  - [ ] Run HermiT reasoner on quadstore
  - [ ] Store inferred relationships in separate inference ontology
  - [ ] Display inferred class memberships in energy report
- [ ] Add consistency checking to `wiki-compiler audit`
  - [ ] Detect contradictory knowledge via HermiT
  - [ ] Report inconsistent classes as violations
- [ ] Activate SHACL validation as gatekeeper
  - [ ] Block invalid triples at insertion time
  - [ ] Use `owlready2.observe` for real-time validation
- [ ] Extract rule IDs and "Enforced by" clauses as OWL annotations

## Verification

```bash
wiki-compiler energy  # Should run sync_reasoner() and report inferred relationships
wiki-compiler audit  # Should detect inconsistencies via HermiT
```

## Related

- `wiki/adrs/003_owl_integration.md` (Reasoning section)
- `wiki/standards/house_rules.md`
- `desk/tasks/owl-phase2-quadstore-primary.md`
