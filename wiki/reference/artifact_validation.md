---
identity:
  node_id: "doc:wiki/reference/artifact_validation.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/artifact_validation.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:validate_wiki_artifact", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:validate_all_artifacts", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_validate_issue", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_validate_gates", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_validate_backlog_item", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_validate_board", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_validate_adr", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_repo_style_path", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/artifact_validation.py:_validate_identity_path", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Validation helpers for authored wiki and operational artifacts. Ensures files like Issues, Boards, Gates, and Wiki nodes conform to their expected internal structures and frontmatter schemas.

## Rule Schema

```python
def validate_wiki_artifact(path: Path) -> ArtifactValidationReport
def validate_all_artifacts(project_root: Path) -> list[ArtifactValidationReport]
```

## Fields

- `path`: The path to the markdown artifact to validate.
- `project_root`: The root directory of the repository for full traversal.

## Usage Examples

```python
from wiki_compiler.artifact_validation import validate_wiki_artifact
from pathlib import Path

report = validate_wiki_artifact(Path("desk/Gates.md"))
if not report.is_valid:
    for finding in report.findings:
        print(finding.message)
```
