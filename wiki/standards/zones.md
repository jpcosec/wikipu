---
identity:
  node_id: "doc:wiki/standards/zones.md"
  node_type: "doc_standard"
edges:
  - target_id: "doc:wiki/WhereAmI.md"
    relation_type: "implements"
compliance:
  status: "implemented"
  failing_standards: []
---

# Zone Contracts

Declarative contracts defining how each zone is sensed and measured.

## The Six Zones

| Zone | Path | Track Modified | Track Untracked | Energy Weight | Response |
|------|------|----------------|-----------------|---------------|----------|
| raw | `raw/` | false | true | 1.0 | ingest |
| exclusion | `exclusion/` | false | false | 0.0 | ignore |
| wiki | `wiki/` | true | false | 1.0 | rebuild |
| desk | `desk/` | true | true | 2.0 | scan |
| drawers | `drawers/` | true | true | 0.5 | review |
| src | `src/` | true | false | 1.5 | audit |

## Zone Definitions

### raw/ (Inviolable)

The seed/ore zone. Files here are inputs to the system. We track untracked files to trigger ingestion, but never track modifications (as raw is immutable).

```yaml
zone: raw
path: raw/
track_modified: false
track_untracked: true
energy_weight: 1.0
response_action: ingest
```

### exclusion/ (Inviolable)

Hidden infrastructure. No tracking.

```yaml
zone: exclusion
path: exclusion/
track_modified: false
track_untracked: false
energy_weight: 0.0
response_action: ignore
```

### wiki/

The curated truth. Track modifications to detect drift and trigger rebuilds.

```yaml
zone: wiki
path: wiki/
track_modified: true
track_untracked: false
energy_weight: 1.0
response_action: rebuild
```

### desk/

Active work surface. High energy weight because active work indicates perturbations.

```yaml
zone: desk
path: desk/
track_modified: true
track_untracked: true
energy_weight: 2.0
response_action: scan
```

### drawers/

Deferred work. Lower energy weight since deferred items are expected to be stale.

```yaml
zone: drawers
path: drawers/
track_modified: true
track_untracked: true
energy_weight: 0.5
response_action: review
```

### src/

Motor and sensory organs. Track modified files and apply high weight.

```yaml
zone: src
path: src/
track_modified: true
track_untracked: false
energy_weight: 1.5
response_action: audit
```

## Usage

The perception system loads these contracts and applies them generically:

```python
from wiki_compiler.perception import build_status_report
from wiki_compiler.contracts import ZoneContract

contracts = load_zone_contracts()  # Loads from wiki topology
report = build_status_report(project_root, contracts)
```

## Adding New Zones

To add a new zone, simply add a contract entry to the wiki topology. No code changes required.
