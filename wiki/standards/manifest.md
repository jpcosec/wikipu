---
identity:
  node_id: "doc:wiki/standards/manifest.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/manifest.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/manifest.py:compute_content_hash", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/manifest.py:load_manifest", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/manifest.py:save_manifest", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/manifest.py:add_to_manifest", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Manages the raw source manifest system for tracking file provenance. Handles computing file hashes and persisting entries to a CSV manifest to support delta-compilation and stale node detection.

## Rule Schema

```python
def compute_content_hash(path: Path) -> str
def load_manifest(manifest_path: Path) -> list[RawSourceEntry]
def save_manifest(manifest_path: Path, entries: list[RawSourceEntry]) -> None
def add_to_manifest(
    project_root: Path,
    manifest_path: Path,
    source_path: Path,
    notes: str = ""
) -> RawSourceEntry
```

## Fields

- `manifest_path`: Path to the CSV manifest file.
- `source_path`: Path to the raw source file being tracked.
- `entries`: A list of `RawSourceEntry` models.

## Usage Examples

```python
from wiki_compiler.manifest import compute_content_hash
from pathlib import Path

hash_val = compute_content_hash(Path("raw/notes.md"))
print(f"SHA-256: {hash_val}")
```
