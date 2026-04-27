# Tasks Board

> **Single entry point for all active work.** Read this before starting any task.

## Current State Summary

- Branch: `kgdb-ontology-split`
- Objective: keep `wikipu` on external sibling `kgdb` + `ontology` packages after the in-repo split
- Baseline: extraction work has been atomized into `desk/tasks/` and the split is now in follow-up cleanup mode
- Current phase: complete — boundary cleanup done, all split-package imports routed through adapters

## Priority Roadmap

### Phase 1 - Create kgdb in-repo package
- `desk/tasks/101-scaffold-kgdb-package.md`
- `desk/tasks/102-move-kgdb-base-contracts.md`
- `desk/tasks/103-move-graph-utils-to-kgdb.md`
- `desk/tasks/104-move-query-modules-to-kgdb.md`
- `desk/tasks/105-add-kgdb-cli-entrypoint.md`

### Phase 2 - Create ontology in-repo package
- `desk/tasks/106-scaffold-ontology-package.md`
- `desk/tasks/107-move-ontology-domain-contracts.md`
- `desk/tasks/108-move-owl-reasoner-to-ontology.md`
- `desk/tasks/109-move-owl-backend-to-ontology.md`
- `desk/tasks/110-move-owl-auditor-to-ontology.md`
- `desk/tasks/111-move-energy-audit-to-ontology.md`
- `desk/tasks/112-split-cleanser-detection-into-ontology.md`
- `desk/tasks/113-move-facet-registry-to-ontology.md`
- `desk/tasks/114-move-facet-injectors-to-ontology.md`
- `desk/tasks/115-move-facet-validator-to-ontology.md`
- `desk/tasks/116-add-ontology-cli-entrypoint.md`

### Phase 3 - Split mixed modules
- `desk/tasks/117-split-context-between-kgdb-and-wiki-compiler.md`
- `desk/tasks/118-split-scanner-between-ontology-and-wiki-compiler.md`
- `desk/tasks/119-split-builder-between-ontology-and-wiki-compiler.md`

### Phase 4 - Route all boundaries through adapters
- `desk/tasks/120-create-kgdb-store-adapter.md`
- `desk/tasks/121-create-kgdb-query-adapter.md`
- `desk/tasks/122-create-ontology-energy-adapter.md`
- `desk/tasks/123-create-ontology-cleanse-adapter.md`
- `desk/tasks/124-create-ontology-reasoning-adapter.md`
- `desk/tasks/125-create-ontology-facets-adapter.md`
- `desk/tasks/126-route-energy-and-cleanse-commands-through-adapters.md`
- `desk/tasks/127-route-build-command-through-adapters.md`
- `desk/tasks/128-route-main-through-adapters.md`
- `desk/tasks/129-remove-kgdb-shims.md`
- `desk/tasks/130-remove-ontology-contract-and-facet-shims.md`
- `desk/tasks/131-remove-ontology-reasoning-and-energy-shims.md`

### Phase 5 - Extract sibling repos after in-repo split is green
- complete

## Dependency Summary

- Root tasks: none
- `kgdb` path: extracted to sibling repo, all imports through adapters
- `ontology` path: extracted to sibling repo, all imports through adapters
- Energy re-owned in `wiki_compiler`, adapter layer is the sole boundary surface

## Parallelization Map

- All lanes complete

## Active (status=open|in_progress)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| - | - | none | - | - |

## Blocked (status=blocked)

| ID | Domain | Task | Priority | Depends On |
|----|--------|------|----------|------------|
| - | - | none | - | - |

---

**Working rules for every task:**

1. Check whether any existing test is no longer valid and delete it if needed.
2. Add new tests where necessary.
3. Run the relevant tests.
4. Update `changelog.md`.
5. Delete the solved task file from `desk/tasks/`.
6. Update this Board.
7. Make a commit that clearly states what was fixed, making sure all required files are staged.
