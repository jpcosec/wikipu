---
identity:
  node_id: "doc:wiki/standards/zones.md"
  node_type: "doc_standard"
edges:
  - target_id: "doc:wiki/concepts/WhereAmI.md"
    relation_type: "implements"
compliance:
  status: "implemented"
  failing_standards: []
---

Declarative contracts defining how each zone is sensed and measured by the perception system. Each zone has configurable tracking behavior and energy weights.

## Rule Schema

Each zone is defined as a YAML block with the following structure:

```yaml
zone: <zone_name>
path: <relative_path>
track_modified: <true|false>
track_untracked: <true|false>
energy_weight: <float>
response_action: <action>
```

## Fields

| Field | Type | Description |
|-------|------|-------------|
| `zone` | str | Unique zone identifier |
| `path` | str | Relative path from project root |
| `track_modified` | bool | Whether to detect file modifications |
| `track_untracked` | bool | Whether to detect new files |
| `energy_weight` | float | Multiplier for energy calculations (0.0-2.0) |
| `response_action` | str | Action: `scan`, `rebuild`, `ingest`, `review`, `ignore`, `audit` |

## Usage Examples

The perception system loads these contracts and applies them generically:

```python
from wiki_compiler.perception import build_status_report
from wiki_compiler.contracts import ZoneContract

contracts = load_zone_contracts()  # Loads from wiki topology
report = build_status_report(project_root, contracts)
```

To add a new zone, simply add a contract entry to the wiki topology. No code changes required.
