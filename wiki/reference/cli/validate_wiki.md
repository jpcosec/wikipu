---
identity:
  node_id: "doc:wiki/reference/cli/validate_wiki.md"
  node_type: "reference"
edges:
  - {target_id: "file:src/wiki_compiler/main.py", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/artifact_validation.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:validate_wiki_artifact", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Validates one authored wiki artifact against the implemented frontmatter, abstract, template, and ADR-local rules. This command is the foundation layer for turning the artifact standards into executable checks.

## Signature or Schema

`wiki-compiler validate-wiki --path <path>` loads one markdown artifact, validates it against the implemented wiki-node rules, and emits a JSON report with rule-level findings.

## Fields

| Flag | Default | Description |
|---|---|---|
| `--path` | none | Path to the authored wiki artifact markdown file |

## Usage Examples

```bash
wiki-compiler validate-wiki --path wiki/concepts/how_wikipu_works.md
wiki-compiler validate-wiki --path wiki/adrs/002_documentation_consolidation.md
```
