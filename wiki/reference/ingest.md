---
identity:
  node_id: "doc:wiki/reference/ingest.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/ingest.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/ingest.py:ingest_raw_sources"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/ingest.py:decompose_source"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/ingest.py:render_draft"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/ingest.py:summarize_source"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/ingest.py:draft_node_path"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/ingest.py:slugify"
    relation_type: documents
---

Handles the ingestion of raw source files and their transformation into Knowledge Graph draft nodes. It supports atomic decomposition of sources into multiple nodes and generates initial markdown documentation with appropriate frontmatter.

## Signature or Schema

```python
def ingest_raw_sources(
    source_dir: Path,
    dest_dir: Path,
    project_root: Path | None = None,
    overwrite: bool = False,
) -> list[Path]: ...

def decompose_source(source_path: Path) -> list[tuple[str, str, str]]: ...

def render_draft(
    source_path: Path,
    rel_source: str,
    dest_dir: Path,
    draft_slug: str,
    title: str,
    content: str,
    node_type: str = "concept",
) -> str: ...

def summarize_source(source_path: Path) -> tuple[str, str]: ...

def draft_node_path(dest_dir: Path, stem: str) -> str: ...

def slugify(value: str) -> str: ...
```

## Fields

This module provides functions and does not define public classes or fields.

## Usage Examples

```python
from pathlib import Path
from wiki_compiler.ingest import ingest_raw_sources

source_dir = Path("raw")
dest_dir = Path("wiki/drafts")
ingested_files = ingest_raw_sources(source_dir, dest_dir, overwrite=True)
```
