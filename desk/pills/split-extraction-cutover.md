---
pill_type: warning
scope: domain
language: en
nature: implementation
bound_to: 132-135
created: 2026-04-24
lifecycle: current
---

# Extraction Cutover Warnings

## Cutover order

1. Scaffold sibling `kgdb` repo.
2. Externalize `kgdb` dependency and remove in-repo `src/kgdb/`.
3. Scaffold sibling `ontology` repo.
4. Externalize `ontology` dependency and remove in-repo `src/ontology/`.

## Why the order matters

- `ontology` depends conceptually and operationally on the final `kgdb` public surface.
- Cutting over both packages at once makes failures ambiguous.
- External repo scaffolding and dependency cutover are different risk classes and should not be merged.

## Do not do this

- Do not remove in-repo package trees before local editable dependencies are wired.
- Do not cut over `ontology` before `kgdb` is already externalized and green.
- Do not treat repo scaffolding as proof that dependency cutover works.

## Exit criteria

- This repo imports the sibling packages through local editable dependencies.
- In-repo package copies are gone.
- Test baseline and import audits still hold.

## Reference

- `desk/tasks/132-scaffold-sibling-kgdb-repo.md`
- `desk/tasks/133-externalize-kgdb-dependency.md`
- `desk/tasks/134-scaffold-sibling-ontology-repo.md`
- `desk/tasks/135-externalize-ontology-dependency.md`
