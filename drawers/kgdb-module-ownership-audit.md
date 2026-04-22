---
status: open
priority: p1
depends_on:
  - drawers/kgdb-storage-boundary.md
created: 2026-04-22
assigned_to: self
---

# kgdb Module Ownership Audit

This audit classifies current `src/wiki_compiler/` modules by where they should live after the split.

## Bucket meanings

- `kgdb`: relation + semantic storage or graph-native behavior
- `wikipu`: curation/workspace/orchestration behavior
- `split`: mixed module; keep a curator-facing adapter in `wikipu`, move the relation-oriented core toward `kgdb`

## Audit

| Module | Target | Why |
|---|---|---|
| `contracts.py` | split | mixes graph contracts/facets with workspace-facing node schema |
| `graph_utils.py` | kgdb | graph persistence and node/edge storage |
| `query_language.py` | kgdb | graph query surface |
| `query_executor.py` | kgdb | graph traversal/execution |
| `owl_reasoner.py` | kgdb | semantic inference layer |
| `auditor_owl.py` | kgdb | reasoning-oriented validation |
| `energy.py` | split | graph energy belongs in `kgdb`; workspace drift belongs in `wikipu` |
| `context.py` | split | graph neighborhood logic belongs in `kgdb`; task/checklist hydration belongs in `wikipu` |
| `cleanser.py` | kgdb | graph-structure optimization proposals |
| `registry.py` | split | facet registry can move; workflow registry concerns stay local if any |
| `facet_validator.py` | split | graph facet validation core vs CLI/workflow handling |
| `facet_injectors.py` | split | injectors tied to graph enrichment move; repo-specific discovery stays curated |
| `scanner.py` | split | code/entity extraction may feed `kgdb`, but project scanning policy is curator-owned |
| `builder.py` | split | graph assembly core moves; source selection and zone orchestration stay in `wikipu` |
| `coordinator.py` | wikipu | coordinates repo workflow rather than pure graph storage |
| `perception.py` | wikipu | zone contracts and git-backed workspace perception are curator concerns |
| `auditor.py` | wikipu | compliance reporting across the workspace, not just graph storage |
| `main.py` | wikipu | CLI composition |
| `query_server.py` | wikipu | serving/query entrypoint layer |
| `scaffolder.py` | wikipu | project bootstrapping and structure creation |
| `curate.py` | wikipu | explicit curation workflow |
| `ingest.py` | wikipu | raw-to-curated ingestion policy |
| `manifest.py` | wikipu | raw/source manifest management |
| `drafts.py` | wikipu | draft lifecycle |
| `trails.py` | wikipu | trail artifacts |
| `gates.py` | wikipu | human approval surface |
| `session_storage.py` | wikipu | session state |
| `workflow_guard.py` | wikipu | workflow enforcement |
| `sync_gate.py` | wikipu | operational synchronization control |
| `preflight.py` | wikipu | repo/process checks before commands |
| `artifact_validation.py` | wikipu | authored artifact validation in workspace surfaces |
| `validator.py` | wikipu | topology proposal validation is a curation/governance concern |
| `node_templates.py` | wikipu | current wiki authoring templates; likely future bridge to `sldb` |
| `protocols.py` | split | interface definitions should follow whichever boundary they describe |
| `__init__.py` | split | package surface changes after split |

## First extraction candidates

These are the cleanest starting points for `kgdb`:

- `graph_utils.py`
- `query_language.py`
- `query_executor.py`
- `owl_reasoner.py`
- `auditor_owl.py`
- `cleanser.py`

## Modules that must be split carefully

- `contracts.py`
- `energy.py`
- `context.py`
- `builder.py`
- `scanner.py`
- `facet_injectors.py`
- `registry.py`
- `facet_validator.py`

## Suggested next implementation artifact

After this audit, the next step is a migration document that turns these ownership calls into:

- package boundaries
- adapter entrypoints
- import-direction rules
- test migration rules
