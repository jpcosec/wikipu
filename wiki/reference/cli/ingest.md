---
identity:
  node_id: "doc:wiki/reference/cli/ingest.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/ingest.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/ingest.py:ingest_raw_sources", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Converts raw source files in a staging directory into draft wiki nodes with well-formed frontmatter, writing them to a destination directory. It is the first stage of the ore-to-node pipeline: unstructured knowledge enters `raw/` and exits as structured Markdown stubs ready for editing and promotion.

## Signature or Schema

`wiki-compiler ingest` walks the source directory, reads each raw file, generates a draft Markdown node with a minimal frontmatter block, and writes it under the destination directory. Existing files are skipped unless `--overwrite` is passed. The command prints a JSON array of the written file paths. A `.wikiignore` file at the project root controls which source files are excluded.

## Fields

```
wiki-compiler ingest [OPTIONS]
```

| Flag | Default | Description |
|---|---|---|
| `--source` | `raw` | Directory containing raw source files to ingest |
| `--dest` | `wiki/drafts` | Directory where draft wiki nodes are written |
| `--project-root` | `.` | Project root used for `.wikiignore` lookup |
| `--overwrite` | `false` | When set, overwrites existing draft files |
| `--model` | _(none)_ | Reserved for future LLM-backed extraction |

**Output:** JSON array of posix paths for every file written.

## Usage Examples

```bash
# Ingest all raw files into the default drafts directory
wiki-compiler ingest

# Ingest from a custom source with overwrite enabled
wiki-compiler ingest --source raw/phase2 --dest wiki/drafts --overwrite

# Ingest with an explicit project root (for .wikiignore resolution)
wiki-compiler ingest --source raw --project-root /home/user/myproject
```
