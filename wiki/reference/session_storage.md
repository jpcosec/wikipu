---
identity:
  node_id: "doc:wiki/reference/session_storage.md"
  node_type: "doc_standard"
edges:
  - {target_id: "file:src/wiki_compiler/session_storage.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/session_storage.py:get_session_dir", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/session_storage.py:save_session_log", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/session_storage.py:load_session_log", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/session_storage.py:list_sessions", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/session_storage.py:get_latest_session", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Storage policy and discovery helpers for session logs. Manages the persistence of `SessionLog` objects to the canonical `desk/autopoiesis/sessions/` directory.

## Rule Schema

```python
def save_session_log(project_root: Path, log: SessionLog) -> Path
def load_session_log(project_root: Path, session_id: str) -> SessionLog
def get_latest_session(project_root: Path) -> SessionLog | None
```

## Fields

- `project_root`: The root directory of the repository.
- `log`: A `SessionLog` Pydantic model instance.
- `session_id`: Unique identifier for the session (e.g., `cycle-20260410...`).

## Usage Examples

```python
from wiki_compiler.session_storage import get_latest_session
from pathlib import Path

latest = get_latest_session(Path("."))
if latest:
    print(f"Resuming from {latest.session_id} on branch {latest.branch}")
```
