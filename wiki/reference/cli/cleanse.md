---
identity:
  node_id: "doc:wiki/reference/cli/cleanse.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/cleanser.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/cleanser.py:detect_cleansing_candidates", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Detects graph anomalies and proposes structural corrections before any destructive or topology-changing cleanup is applied. The current implementation covers `--detect`; `--apply` remains a follow-up.

## Signature or Schema

`wiki-compiler cleanse --detect` emits a machine-readable `CleansingReport` covering the implemented detection heuristics. `wiki-compiler cleanse --apply` is planned but not implemented yet.

## Fields

- `--detect` produces a machine-readable anomaly report.
- `--apply` is reserved for the follow-up application layer and currently raises a not-implemented error.

## Usage Examples

```bash
wiki-compiler cleanse --detect
```

- Planned follow-up: `wiki-compiler cleanse --apply report.json`
