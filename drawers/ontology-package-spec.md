---
status: open
priority: p1
depends_on:
  - drawers/kgdb-storage-boundary.md
  - drawers/kgdb-module-ownership-audit.md
  - drawers/kgdb-migration-plan.md
created: 2026-04-23
assigned_to: self
---

# ontology Package Specification

This document defines the `ontology` package: its scope, structure, own `main`, import rules, and extraction order.

## Role

`ontology` is the domain knowledge layer above `kgdb`.

It uses `kgdb` as its storage and traversal substrate. It adds the interpretation layer: what do nodes and edges mean, are they semantically consistent, how much entropy does the current graph state carry, which structural patterns should be cleaned up?

`ontology` has no knowledge of wiki workflows, user sessions, gates, zones, or the CLI.

## Package Boundary

```
ontology/
├── contracts/      ← domain contracts (facets, energy, wiki_nodes, proposals)
├── facets/         ← facet registry, injection, and validation
├── reasoning/      ← OWL backend, reasoner, and consistency checking
├── energy/         ← systemic energy audit logic
├── cleansing/      ← domain-aware structural cleansing rules
├── wiki_nodes/     ← document type taxonomy and node schema
└── main.py         ← ontology CLI entrypoint
```

## ontology main commands

The ontology CLI operates on a graph loaded from `kgdb`, applying domain knowledge:

- `ontology reason --graph <path>` — run OWL reasoner (HermiT) and return inferred relationships
- `ontology check --graph <path>` — OWL consistency check; exit 1 if inconsistent
- `ontology energy --graph <path> --project-root <path>` — run systemic energy audit
- `ontology cleanse detect --graph <path>` — detect domain-level cleansing candidates
- `ontology cleanse apply --report <path> --graph <path>` — apply an approved cleansing report
- `ontology inject-facets --graph <path> --source <dir>` — inject domain facets into graph nodes
- `ontology propose-facet --proposal <file> --graph <path>` — validate a new facet for orthogonality
- `ontology audit-owl --graph <path>` — check for conflicts between Markdown edges and OWL triples

## Module Mapping

### Modules moving to `ontology` (clean, no workspace assumptions)

| Source module | Target in ontology |
|---|---|
| `owl_reasoner.py` | `ontology/reasoning/reasoner.py` |
| `owl_backend/` | `ontology/reasoning/owl_backend/` |
| `auditor_owl.py` | `ontology/reasoning/auditor.py` |
| `energy.py` | `ontology/energy/audit.py` |
| `facet_injectors.py` | `ontology/facets/injectors.py` |
| `facet_validator.py` | `ontology/facets/validator.py` |
| `registry.py` | `ontology/facets/registry.py` |
| `contracts/facets.py` | `ontology/contracts/facets.py` |
| `contracts/energy.py` | `ontology/contracts/energy.py` |
| `contracts/wiki_nodes.py` | `ontology/contracts/wiki_nodes.py` |
| `contracts/proposals.py` | `ontology/contracts/proposals.py` |

### Modules that must be split before extraction

| Source module | ontology portion | wikipu portion |
|---|---|---|
| `builder.py` | `ontology/facets/builder.py` (edge building, facet enrichment, compliance scoring) | `wikipu` (wiki compilation, source selection, zone orchestration) |
| `scanner.py` | `ontology/facets/scanner.py` (code entity extraction) | `wikipu` (project scanning policy, exclusion rules) |
| `cleanser.py` | `ontology/cleansing/rules.py` (domain rules); `ontology/cleansing/apply.py` (execution) | `wikipu` adapter executes filesystem ops using cleansing results |

Note on `cleanser.py`: the detection rules (`_stale_edge_proposals`, `_orphaned_test_proposals`, etc.) belong in `ontology` because they encode domain knowledge about tests, plans, and config files. The `apply_cleansing_proposal` function executes filesystem operations — the execution policy belongs in a `wikipu` adapter that calls the `ontology` detection and then acts on the result.

## Import Rules for `ontology`

```
ontology →  kgdb  (storage and traversal only)
ontology →  sldb artifacts (stable document inputs for relation building)
```

Forbidden from inside `ontology`:
- `from wikipu import ...` — never
- direct imports of `wiki_compiler.coordinator`, `wiki_compiler.gates`, `wiki_compiler.session_storage`, or any workspace/curation surface

## Adapter Entry Points to Create Inside `wikipu`

Before extraction, create these adapter modules:

- `wikipu.adapters.ontology_reason` — wraps `ontology.reasoning`
- `wikipu.adapters.ontology_energy` — wraps `ontology.energy`
- `wikipu.adapters.ontology_cleanse` — wraps detection + applies via filesystem
- `wikipu.adapters.ontology_facets` — wraps injection and validation

## Extraction Order

### Step 1: verify clean ontology candidates

Run grep checks to confirm none of the clean candidates import from `coordinator`, `gates`, `session_storage`, `perception`, or other workspace modules.

### Step 2: move clean candidates

Move `owl_reasoner.py`, `owl_backend/`, `auditor_owl.py`, `energy.py`, `registry.py`, `facet_injectors.py`, `facet_validator.py`, and the four contract files.

Each move:
- adjust import paths to use `kgdb` for storage primitives
- verify no `wiki_compiler.` workspace imports remain
- add the moved module to the `ontology` package surface

### Step 3: split mixed modules

Split `builder.py`, `scanner.py`, and `cleanser.py` (see split table above).

For each:
- move the domain-knowledge core to `ontology`
- leave a thin adapter in `wikipu` that calls the `ontology` function and handles workspace context
- update `main.py` and commands to use the adapter

### Step 4: create the `ontology` package physically

- create sibling repo/package `ontology` with `pyproject.toml`
- add `ontology = "ontology.main:main"` to `[project.scripts]`
- move all extracted modules there
- update `wikipu` adapters to import the external package

## Dependencies for `ontology`

```toml
dependencies = [
    "pydantic>=2.0.0",
    "networkx>=3.0",
    "owlready2>=0.46",
    "rdflib>=7.0",
    "kgdb",        # storage and traversal substrate
]
```

## Test Migration Rules

Tests that verify domain semantics move to `ontology`:
- `test_cleanser.py` → `ontology`
- `test_cleansing_extended.py` → `ontology`
- `test_facet_injectors.py` → `ontology`
- `test_facet_proposal.py` → `ontology`
- `test_scanner_io.py` (entity extraction portions) → `ontology`
- `test_scanner_plugin.py` (entity extraction portions) → `ontology`
- `test_registry_and_query.py` (registry and facet portions) → `ontology`
- `test_auditor.py` (OWL check portions) → `ontology`

Tests that verify workspace and CLI behavior stay in `wikipu`.

## Done Criteria

The ontology extraction is successful when:

- `ontology` has no imports from `wikipu`
- `ontology` can run the reasoner, energy audit, and cleansing detection given only a graph path and a project root
- `kgdb` has no imports from `ontology`
- `wikipu` accesses `ontology` only through its adapter layer
- the `ontology` CLI (`ontology reason`, `ontology energy`, `ontology cleanse detect`) works end-to-end independently
