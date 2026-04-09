---
identity:
  node_id: "doc:wiki/reference/cli/cleanse.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
compliance:
  status: "planned"
  failing_standards: []
---

This planned command will detect graph anomalies and propose structural corrections before any destructive or topology-changing cleanup is applied. It exists as a protocol placeholder so the graph can model the cleansing step before the runtime is fully implemented.

## Signature or Schema

Planned interface: `wiki-compiler cleanse --detect` to emit a cleansing report and `wiki-compiler cleanse --apply` to apply approved proposals.

## Fields

- `status: planned` means this command is documented as part of the system surface but the runtime is not implemented yet.
- `--detect` is expected to produce a machine-readable anomaly report.
- `--apply` is expected to require explicit approval for destructive operations.

## Usage Examples

- Planned usage: `wiki-compiler cleanse --detect`
- Planned usage: `wiki-compiler cleanse --apply report.json`
