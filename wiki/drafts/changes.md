---
identity:
  node_id: "doc:wiki/drafts/changes.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md", relation_type: "documents"}
---

- Add validation to run_logic

## Details

- Add validation to run_logic
- Update architecture docs
```

`tests/fixtures/sample_project/docs/plans/test-feature/review_test-feature_0.md`:

```markdown
---
id: review-test-feature-0
domain: pipeline
stage: extract
nature: development
type: review
group: test-feature
version: 0
parent: plan-test-feature-0
status: active
touches:
  - path: src/nodes/extract/logic.py
    symbol: run_logic
  - path: docs/architecture.md
file_tags:
  - file: src/nodes/extract/logic.py
    lines: [10, 15]
    comment: needs error handling
graph_changes:
  - action: add_touch
    target: src/core/io/writer.py
    comment: also needs update
---

# Test Feature Plan (reviewed)

This is the reviewed version with inline edits.
```

- [ ] **Step 2: Write the failing tests**

Create `tests/test_plans.py`:

```python
"""Tests for plan discovery and iteration chain."""

from __future__ import annotations

from pathlib import Path

import pytest

from doc_router.plans import (
    discover_plan_groups,
    get_plan_chain,
    read_plan_file,
    save_review,
    PlanMetadata,
)


@pytest.fixture
def plans_dir(sample_project_dir: Path) -> Path:
    return sample_project_dir / "docs" / "plans"


def test_discover_plan_groups(plans_dir: Path) -> None:
    """Should find all plan groups as subdirectories."""
    groups = discover_plan_groups(plans_dir)
    assert len(groups) >= 1
    assert any(g["group"] == "test-feature" for g in groups)
    tf = next(g for g in groups if g["group"] == "test-feature")
    assert tf["status"] == "active"
    assert tf["domain"] == "pipeline"


def test_get_plan_chain(plans_dir: Path) -> None:
    """Should return ordered iteration chain for a group."""
    chain = get_plan_chain(plans_dir, "test-feature")
    assert chain["group"] == "test-feature"
    assert len(chain["chain"]) == 2
    assert chain["chain"][0]["type"] == "plan"
    assert chain["chain"][0]["version"] == 0
    assert chain["chain"][1]["type"] == "review"
    assert chain["chain"][1]["version"] == 0


def test_get_plan_chain_not_found(plans_dir: Path) -> None:
    """Should raise FileNotFoundError for unknown group."""
    with pytest.raises(FileNotFoundError):
        get_plan_chain(plans_dir, "nonexistent")


def test_read_plan_file(plans_dir: Path) -> None:
    """Should return metadata and content of a plan file."""
    result = read_plan_file(plans_dir, "test-feature", "plan", 0)
    assert result["metadata"]["id"] == "plan-test-feature-0"
    assert result["metadata"]["type"] == "plan"
    assert result["metadata"]["group"] == "test-feature"
    assert "# Test Feature Plan" in result["content"]


def test_read_plan_file_not_found(plans_dir: Path) -> None:
    """Should raise FileNotFoundError for missing file."""
    with pytest.raises(FileNotFoundError):
        read_plan_file(plans_dir, "test-feature", "plan", 99)


def test_read_review_file_with_tags(plans_dir: Path) -> None:
    """Should parse file_tags and graph_changes from review frontmatter."""
    result = read_plan_file(plans_dir, "test-feature", "review", 0)
    meta = result["metadata"]
    assert meta["type"] == "review"
    assert meta["parent"] == "plan-test-feature-0"
    assert len(meta.get("file_tags", [])) == 1
    assert meta["file_tags"][0]["file"] == "src/nodes/extract/logic.py"
    assert len(meta.get("graph_changes", [])) == 1
    assert meta["graph_changes"][0]["action"] == "add_touch"


def test_save_review(tmp_path: Path) -> None:
    """Should write a review file and supersede the source plan."""
    # Setup: create a plan group with one plan
    group_dir = tmp_path / "test-save"
    group_dir.mkdir(parents=True)
    plan_file = group_dir / "plan_test-save_0.md"
    plan_file.write_text(
        "---\nid: plan-test-save-0\ntype: plan\ngroup: test-save\n"
        "version: 0\nstatus: active\ndomain: core\nstage: global\n"
        "nature: development\ntouches: []\n---\n\n# Original plan\n"
    )

    # Save review
    save_review(
        plans_dir=tmp_path,
        group="test-save",
        version=0,
        content="# Reviewed plan with edits",
        file_tags=[{"file": "src/foo.py", "lines": [1, 5], "comment": "fix this"}],
        graph_changes=[{"action": "add_touch", "target": "src/bar.py", "comment": "needed"}],
        touches=[{"path": "src/foo.py"}, {"path": "src/bar.py"}],
    )

    # Review file should exist
    review_file = group_dir / "review_test-save_0.md"
    assert review_file.exists()

    # Read it back and verify
    result = read_plan_file(tmp_path, "test-save", "review", 0)
    assert result["metadata"]["type"] == "review"
    assert result["metadata"]["parent"] == "plan-test-save-0"
    assert result["metadata"]["status"] == "active"
    assert "# Reviewed plan with edits" in result["content"]
    assert len(result["metadata"]["file_tags"]) == 1
    assert len(result["metadata"]["graph_changes"]) == 1

    # Source plan should be superseded
    source = read_plan_file(tmp_path, "test-save", "plan", 0)
    assert source["metadata"]["status"] == "superseded"
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `python -m pytest tests/test_plans.py -v`
Expected: FAIL — `doc_router.plans` does not exist

- [ ] **Step 4: Implement plans.py**

Create `src/doc_router/plans.py`:

```python
"""Plan discovery, iteration chain logic, and read/write operations."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


# Pattern: plan_{group}_{version}.md or review_{group}_{version}.md
_FILENAME_RE = re.compile(r"^(plan|review)_(.+)_(\d+)\.md$")


def _parse_plan_file(path: Path) -> dict[str, Any]:
    """Parse a plan/review markdown file into metadata + content."""
    text = path.read_text(encoding="utf-8")
    stripped = text.strip()
    if not stripped.startswith("---"):
        return {"metadata": {}, "content": text}

    end = stripped.find("---", 3)
    if end == -1:
        return {"metadata": {}, "content": text}

    raw_fm = stripped[3:end].strip()
    body = stripped[end + 3:].strip()

    try:
        metadata = yaml.safe_load(raw_fm)
        if not isinstance(metadata, dict):
            metadata = {}
    except yaml.YAMLError:
        metadata = {}

    return {"metadata": metadata, "content": body}


def _write_plan_file(path: Path, metadata: dict[str, Any], content: str) -> None:
    """Write a plan/review file with YAML frontmatter + markdown body."""
    fm = yaml.dump(metadata, default_flow_style=False, sort_keys=False, allow_unicode=True)
    path.write_text(f"---\n{fm}---\n\n{content}\n", encoding="utf-8")


def discover_plan_groups(plans_dir: Path) -> list[dict[str, Any]]:
    """Find all plan groups and return summary for each.

    Args:
        plans_dir: Root directory containing plan group subdirectories.

    Returns:
        List of dicts with keys: group, latest_type, latest_version, status, domain.
    """
    if not plans_dir.is_dir():
        return []

    groups = []
    for group_dir in sorted(plans_dir.iterdir()):
        if not group_dir.is_dir():
            continue

        latest = _find_latest_in_group(group_dir)
        if latest is None:
            continue

        groups.append(latest)

    return groups


def _find_latest_in_group(group_dir: Path) -> dict[str, Any] | None:
    """Find the latest plan/review in a group directory."""
    entries = []
    for f in group_dir.iterdir():
        m = _FILENAME_RE.match(f.name)
        if m:
            entries.append({
                "file": f,
                "type": m.group(1),
                "group": m.group(2),
                "version": int(m.group(3)),
            })

    if not entries:
        return None

    # Sort: highest version first, then review before plan (review is later in chain)
    entries.sort(key=lambda e: (e["version"], e["type"] == "review"), reverse=True)
    latest_entry = entries[0]
    parsed = _parse_plan_file(latest_entry["file"])
    meta = parsed["metadata"]

    return {
        "group": latest_entry["group"],
        "latest_type": latest_entry["type"],
        "latest_version": latest_entry["version"],
        "status": meta.get("status", "draft"),
        "domain": meta.get("domain", ""),
    }


def get_plan_chain(plans_dir: Path, group: str) -> dict[str, Any]:
    """Get the full iteration chain for a plan group.

    Args:
        plans_dir: Root plans directory.
        group: Plan group name.

    Returns:
        Dict with keys: group, chain (list of {type, version, status, id}).

    Raises:
        FileNotFoundError: If group directory does not exist.
    """
    group_dir = plans_dir / group
    if not group_dir.is_dir():
        raise FileNotFoundError(f"Plan group not found: {group}")

    chain = []
    for f in sorted(group_dir.iterdir()):
        m = _FILENAME_RE.match(f.name)
        if not m:
            continue

        parsed = _parse_plan_file(f)
        meta = parsed["metadata"]
        chain.append({
            "type": m.group(1),
            "version": int(m.group(3)),
            "status": meta.get("status", "draft"),
            "id": meta.get("id", ""),
        })

    # Sort by version, then type (plan before review within same version)
    chain.sort(key=lambda e: (e["version"], e["type"] == "review"))

    return {"group": group, "chain": chain}


def read_plan_file(
    plans_dir: Path, group: str, type_: str, version: int
) -> dict[str, Any]:
    """Read a single plan or review file.

    Args:
        plans_dir: Root plans directory.
        group: Plan group name.
        type_: "plan" or "review".
        version: Version number.

    Returns:
        Dict with keys: metadata (dict), content (str).

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    filename = f"{type_}_{group}_{version}.md"
    file_path = plans_dir / group / filename
    if not file_path.exists():
        raise FileNotFoundError(f"Plan file not found: {filename}")

    return _parse_plan_file(file_path)


def save_review(
    plans_dir: Path,
    group: str,
    version: int,
    content: str,
    file_tags: list[dict[str, Any]] | None = None,
    graph_changes: list[dict[str, Any]] | None = None,
    touches: list[dict[str, str]] | None = None,
) -> Path:
    """Save a review file and supersede the source plan.

    Args:
        plans_dir: Root plans directory.
        group: Plan group name.
        version: Version number (matches the source plan version).
        content: Markdown body of the review.
        file_tags: List of file tag annotations.
        graph_changes: List of graph edit comments.
        touches: Updated list of touched files.

    Returns:
        Path to the created review file.

    Raises:
        FileNotFoundError: If the source plan does not exist.
    """
    # Read source plan to get base metadata
    source = read_plan_file(plans_dir, group, "plan", version)
    source_meta = source["metadata"]

    # Build review metadata
    review_meta = {
        "id": f"review-{group}-{version}",
        "domain": source_meta.get("domain", ""),
        "stage": source_meta.get("stage", "global"),
        "nature": source_meta.get("nature", "development"),
        "type": "review",
        "group": group,
        "version": version,
        "parent": source_meta.get("id", f"plan-{group}-{version}"),
        "status": "active",
        "touches": touches or source_meta.get("touches", []),
    }
    if file_tags:
        review_meta["file_tags"] = file_tags
    if graph_changes:
        review_meta["graph_changes"] = graph_changes

    # Write review file
    review_path = plans_dir / group / f"review_{group}_{version}.md"
    _write_plan_file(review_path, review_meta, content)

    # Supersede source plan
    source_meta["status"] = "superseded"
    source_path = plans_dir / group / f"plan_{group}_{version}.md"
    _write_plan_file(source_path, source_meta, source["content"])

    return review_path
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python -m pytest tests/test_plans.py -v`
Expected: ALL PASS

- [ ] **Step 6: Commit**

```bash
git add src/doc_router/plans.py tests/test_plans.py tests/fixtures/sample_project/docs/plans/
git commit -m "feat(doc-router): add plans module with discovery, chain, and read/write"
```

---

### Task 3: File tree module — directory listing, content, sandboxing

**Files:**
- Create: `src/doc_router/filetree.py`
- Create: `tests/test_filetree.py`

- [ ] **Step 1: Write the failing tests**

Create `tests/test_filetree.py`:

```python
"""Tests for file tree listing, content reading, and security."""

from __future__ import annotations

from pathlib import Path

import pytest

from doc_router.filetree import list_directory, read_file_content, validate_path


def test_list_directory_root(sample_project_dir: Path) -> None:
    """Should list top-level entries with metadata."""
    entries = list_directory(sample_project_dir, sample_project_dir)
    names = {e["name"] for e in entries}
    assert "docs" in names
    assert "src" in names
    docs = next(e for e in entries if e["name"] == "docs")
    assert docs["is_dir"] is True
    assert docs["path"] == "docs"


def test_list_directory_subdir(sample_project_dir: Path) -> None:
    """Should list entries in a subdirectory."""
    entries = list_directory(sample_project_dir, sample_project_dir, "docs")
    names = {e["name"] for e in entries}
    assert "design.md" in names
    assert "architecture.md" in names
    design = next(e for e in entries if e["name"] == "design.md")
    assert design["is_dir"] is False
    assert design["extension"] == ".md"
    assert design["path"] == "docs/design.md"


def test_list_directory_not_found(sample_project_dir: Path) -> None:
    """Should raise FileNotFoundError for missing directory."""
    with pytest.raises(FileNotFoundError):
        list_directory(sample_project_dir, sample_project_dir, "nonexistent")


def test_read_file_content(sample_project_dir: Path) -> None:
    """Should return file content and detected language."""
    result = read_file_content(sample_project_dir, "docs/design.md")
    assert result["path"] == "docs/design.md"
    assert "# Match Stage Design" in result["content"]
    assert result["language"] == "markdown"


def test_read_file_content_python(sample_project_dir: Path) -> None:
    """Should detect Python language."""
    result = read_file_content(sample_project_dir, "src/module.py")
    assert result["language"] == "python"


def test_read_file_content_not_found(sample_project_dir: Path) -> None:
    """Should raise FileNotFoundError for missing file."""
    with pytest.raises(FileNotFoundError):
        read_file_content(sample_project_dir, "nonexistent.txt")


def test_validate_path_traversal(sample_project_dir: Path) -> None:
    """Should reject path traversal attempts."""
    with pytest.raises(PermissionError):
        validate_path(sample_project_dir, "../../etc/passwd")


def test_validate_path_ok(sample_project_dir: Path) -> None:
    """Should accept valid paths within project root."""
    result = validate_path(sample_project_dir, "docs/design.md")
    assert result.is_file()


def test_read_file_content_size_limit(tmp_path: Path) -> None:
    """Should raise ValueError for files exceeding 1MB."""
    big_file = tmp_path / "big.txt"
    big_file.write_text("x" * (1024 * 1024 + 1))
    with pytest.raises(ValueError, match="exceeds"):
        read_file_content(tmp_path, "big.txt")
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_filetree.py -v`
Expected: FAIL — `doc_router.filetree` does not exist

- [ ] **Step 3: Implement filetree.py**

Create `src/doc_router/filetree.py`:

```python
"""Directory listing, file content reading, and path sandboxing."""

from __future__ import annotations

from pathlib import Path
from typing import Any

_MAX_FILE_SIZE = 1024 * 1024  # 1MB

_LANG_MAP = {
    ".py": "python",
    ".md": "markdown",
    ".json": "json",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".js": "javascript",
    ".jsx": "javascript",
    ".html": "html",
    ".css": "css",
    ".toml": "toml",
    ".txt": "text",
    ".sh": "shell",
    ".bash": "shell",
}


def validate_path(project_root: Path, rel_path: str) -> Path:
    """Validate and resolve a relative path within the project root.

    Args:
        project_root: The project root directory (sandbox boundary).
        rel_path: Relative path to validate.

    Returns:
        Resolved absolute path.

    Raises:
        PermissionError: If the resolved path is outside project root.
    """
    resolved = (project_root / rel_path).resolve()
    root_resolved = project_root.resolve()

    if not str(resolved).startswith(str(root_resolved)):
        raise PermissionError(f"Path traversal denied: {rel_path}")

    return resolved


def list_directory(
    project_root: Path,
    root_for_rel: Path,
    rel_path: str = "",
) -> list[dict[str, Any]]:
    """List entries in a directory.

    Args:
        project_root: The project root (sandbox boundary).
        root_for_rel: Root for computing relative paths (usually same as project_root).
        rel_path: Relative path of directory to list. Empty string = root.

    Returns:
        List of dicts with keys: name, path, is_dir, extension, child_count.

    Raises:
        FileNotFoundError: If directory does not exist.
    """
    if rel_path:
        target = validate_path(project_root, rel_path)
    else:
        target = project_root

    if not target.is_dir():
        raise FileNotFoundError(f"Directory not found: {rel_path}")

    entries = []
    for child in sorted(target.iterdir()):
        # Skip hidden files and __pycache__
        if child.name.startswith(".") or child.name == "__pycache__":
            continue

        child_rel = str(child.relative_to(root_for_rel))
        entry: dict[str, Any] = {
            "name": child.name,
            "path": child_rel,
            "is_dir": child.is_dir(),
            "extension": child.suffix if child.is_file() else None,
        }
        if child.is_dir():
            try:
                entry["child_count"] = sum(
                    1 for c in child.iterdir()
                    if not c.name.startswith(".") and c.name != "__pycache__"
                )
            except PermissionError:
                entry["child_count"] = 0
        else:
            entry["child_count"] = None

        entries.append(entry)

    return entries


def read_file_content(project_root: Path, rel_path: str) -> dict[str, Any]:
    """Read file content with language detection.

    Args:
        project_root: The project root (sandbox boundary).
        rel_path: Relative path of the file to read.

    Returns:
        Dict with keys: path, content, language.

    Raises:
        FileNotFoundError: If file does not exist.
        ValueError: If file exceeds size limit.
    """
    resolved = validate_path(project_root, rel_path)

    if not resolved.is_file():
        raise FileNotFoundError(f"File not found: {rel_path}")

    size = resolved.stat().st_size
    if size > _MAX_FILE_SIZE:
        raise ValueError(f"File exceeds {_MAX_FILE_SIZE} byte limit: {rel_path}")

    content = resolved.read_text(encoding="utf-8", errors="replace")
    language = _LANG_MAP.get(resolved.suffix.lower(), "text")

    return {"path": rel_path, "content": content, "language": language}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_filetree.py -v`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add src/doc_router/filetree.py tests/test_filetree.py
git commit -m "feat(doc-router): add filetree module with listing, content, and sandboxing"
```

---

### Task 4: Add plan and file API routes to server

**Files:**
- Modify: `src/doc_router/server.py`
- Modify: `tests/test_server.py`

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_server.py`:

```python
@pytest.mark.asyncio
async def test_get_plans_list(client) -> None:
    """Should return list of plan groups."""
    resp = await client.get("/api/plans")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert any(g["group"] == "test-feature" for g in data)


@pytest.mark.asyncio
async def test_get_plan_chain(client) -> None:
    """Should return iteration chain for a group."""
    resp = await client.get("/api/plans/test-feature")
    assert resp.status_code == 200
    data = resp.json()
    assert data["group"] == "test-feature"
    assert len(data["chain"]) >= 2


@pytest.mark.asyncio
async def test_get_plan_chain_not_found(client) -> None:
    """Should return 404 for unknown group."""
    resp = await client.get("/api/plans/nonexistent")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_get_plan_content(client) -> None:
    """Should return metadata and content of a plan file."""
    resp = await client.get("/api/plans/test-feature/plan_0")
    assert resp.status_code == 200
    data = resp.json()
    assert data["metadata"]["type"] == "plan"
    assert "# Test Feature Plan" in data["content"]


@pytest.mark.asyncio
async def test_get_plan_content_not_found(client) -> None:
    """Should return 404 for missing plan file."""
    resp = await client.get("/api/plans/test-feature/plan_99")
    assert resp.status_code == 404


@pytest.mark.asyncio
async def test_save_review(client, sample_project_dir: Path) -> None:
    """Should save a review file via PUT."""
    resp = await client.put(
        "/api/plans/test-feature/review_0",
        json={
            "content": "# Reviewed by test",
            "file_tags": [{"file": "src/foo.py", "lines": [1, 5], "comment": "test tag"}],
            "graph_changes": [],
            "touches": [{"path": "src/foo.py"}],
        },
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"

    # Verify review was saved
    review_file = sample_project_dir / "docs/plans/test-feature/review_test-feature_0.md"
    assert review_file.exists()


@pytest.mark.asyncio
async def test_save_review_forbidden_plan_type(client) -> None:
    """Should return 403 when trying to overwrite a plan (not review)."""
    resp = await client.put(
        "/api/plans/test-feature/plan_0",
        json={"content": "hijack", "file_tags": [], "graph_changes": [], "touches": []},
    )
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_get_files_root(client) -> None:
    """Should list project root directory."""
    resp = await client.get("/api/files")
    assert resp.status_code == 200
    data = resp.json()
    names = {e["name"] for e in data}
    assert "docs" in names
    assert "src" in names


@pytest.mark.asyncio
async def test_get_files_subdir(client) -> None:
    """Should list subdirectory contents."""
    resp = await client.get("/api/files", params={"path": "docs"})
    assert resp.status_code == 200
    data = resp.json()
    names = {e["name"] for e in data}
    assert "design.md" in names


@pytest.mark.asyncio
async def test_get_file_content(client) -> None:
    """Should return file content with language."""
    resp = await client.get("/api/files/content", params={"path": "docs/design.md"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["language"] == "markdown"
    assert "# Match Stage Design" in data["content"]


@pytest.mark.asyncio
async def test_get_file_content_traversal(client) -> None:
    """Should return 403 for path traversal."""
    resp = await client.get("/api/files/content", params={"path": "../../etc/passwd"})
    assert resp.status_code == 403


@pytest.mark.asyncio
async def test_get_files_touched(client) -> None:
    """Should return touched files for a plan group."""
    resp = await client.get("/api/files/touched", params={"group": "test-feature", "version": "0"})
    assert resp.status_code == 200
    data = resp.json()
    paths = {t["path"] for t in data}
    assert "src/nodes/extract/logic.py" in paths
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_server.py -v -k "plan or file or review or touched"`
Expected: FAIL — routes don't exist yet

- [ ] **Step 3: Implement new routes in server.py**

Add to `server.py` inside `create_app()`, after existing routes and before static mount:

```python
    from doc_router.plans import discover_plan_groups, get_plan_chain, read_plan_file, save_review
    from doc_router.filetree import list_directory, read_file_content, validate_path

    # Resolve plans directory
    plan_dir_rel = config.plan_paths.get("plans", "docs/plans/") if hasattr(config, "plan_paths") else "docs/plans/"
    plans_dir = root / plan_dir_rel

    # --- Plans routes ---

    @app.get("/api/plans")
    def list_plans():
        """List all plan groups."""
        return discover_plan_groups(plans_dir)

    @app.get("/api/plans/{group}")
    def plan_chain(group: str):
        """Get iteration chain for a plan group."""
        try:
            return get_plan_chain(plans_dir, group)
        except FileNotFoundError:
            raise HTTPException(404, f"Plan group not found: {group}")

    @app.get("/api/plans/{group}/{type_ver}")
    def plan_content(group: str, type_ver: str):
        """Get content of a specific plan/review file.

        type_ver format: plan_0, review_0, plan_1, etc.
        """
        parts = type_ver.rsplit("_", 1)
        if len(parts) != 2:
            raise HTTPException(400, f"Invalid format: {type_ver}. Expected: plan_N or review_N")
        type_, ver_str = parts
        try:
            ver = int(ver_str)
        except ValueError:
            raise HTTPException(400, f"Invalid version: {ver_str}")

        try:
            return read_plan_file(plans_dir, group, type_, ver)
        except FileNotFoundError:
            raise HTTPException(404, f"Plan file not found: {group}/{type_ver}")

    @app.put("/api/plans/{group}/{type_ver}")
    def put_review(group: str, type_ver: str, body: dict):
        """Save a review file."""
        parts = type_ver.rsplit("_", 1)
        if len(parts) != 2:
            raise HTTPException(400, f"Invalid format: {type_ver}")
        type_, ver_str = parts

        if type_ != "review":
            raise HTTPException(403, "Can only save review files, not plans")

        try:
            ver = int(ver_str)
        except ValueError:
            raise HTTPException(400, f"Invalid version: {ver_str}")

        try:
            save_review(
                plans_dir=plans_dir,
                group=group,
                version=ver,
                content=body.get("content", ""),
                file_tags=body.get("file_tags"),
                graph_changes=body.get("graph_changes"),
                touches=body.get("touches"),
            )
        except FileNotFoundError:
            raise HTTPException(409, f"Source plan not found for {group} v{ver}")

        return {"status": "ok"}

    # --- File tree routes ---

    @app.get("/api/files")
    def list_files(path: str = ""):
        """List directory contents."""
        try:
            return list_directory(root, root, path)
        except FileNotFoundError:
            raise HTTPException(404, f"Directory not found: {path}")
        except PermissionError:
            raise HTTPException(403, f"Access denied: {path}")

    @app.get("/api/files/content")
    def file_content(path: str):
        """Read file content."""
        try:
            return read_file_content(root, path)
        except FileNotFoundError:
            raise HTTPException(404, f"File not found: {path}")
        except PermissionError:
            raise HTTPException(403, f"Access denied: {path}")
        except ValueError as e:
            raise HTTPException(413, str(e))

    @app.get("/api/files/touched")
    def files_touched(group: str, version: int = 0):
        """Get files touched by a plan group."""
        try:
            result = read_plan_file(plans_dir, group, "plan", version)
        except FileNotFoundError:
            raise HTTPException(404, f"Plan not found: {group} v{version}")

        touches = result["metadata"].get("touches", [])
        return touches
```

- [ ] **Step 4: Run all server tests to verify they pass**

Run: `python -m pytest tests/test_server.py -v`
Expected: ALL PASS (old + new)

- [ ] **Step 5: Run full test suite**

Run: `python -m pytest tests/ -v`
Expected: ALL PASS

- [ ] **Step 6: Commit**

```bash
git add src/doc_router/server.py tests/test_server.py
git commit -m "feat(doc-router): add plan and file tree API routes"
```

---

### Task 5: Copy shared components from review-workbench

**Files:**
- Create: `ui/src/components/organisms/IntelligentEditor.tsx` (copy)
- Create: `ui/src/components/molecules/SplitPane.tsx` (copy)
- Create: `ui/src/features/file-explorer/components/FileTree.tsx` (copy)
- Create: `ui/src/features/file-explorer/components/BreadcrumbNav.tsx` (copy)
- Create: `ui/src/features/file-explorer/components/FilePreview.tsx` (copy)
- Create: `ui/src/features/file-explorer/components/JsonPreview.tsx` (copy)
- Create: `ui/src/features/file-explorer/components/MarkdownPreview.tsx` (copy)
- Create: `ui/src/features/file-explorer/components/ImagePreview.tsx` (copy)

The source directory is: `/home/jp/phd-workspaces/dev/.worktrees/ui-redesign/apps/review-workbench/src/`

- [ ] **Step 1: Create target directories**

```bash
mkdir -p ui/src/components/organisms
mkdir -p ui/src/features/file-explorer/components
```

- [ ] **Step 2: Copy components**

Copy each file from review-workbench. Adjust import paths as needed — the atoms (Badge, Button, Icon, etc.) are already at `components/atoms/` in doc-router's UI. The key adjustments:
- Change `../../atoms/` imports to match doc-router's path structure
- Change `../../molecules/` imports similarly
- Remove any references to review-workbench-specific types (e.g., `ExplorerEntry` — adapt to use doc-router's own types)
- Verify each file compiles by running `npx tsc --noEmit` after all copies

Source paths to copy from:
- `components/molecules/SplitPane.tsx`
- `features/explorer/components/ExplorerTree.tsx` → adapt as `FileTree.tsx`
- `features/explorer/components/BreadcrumbNav.tsx`
- `features/explorer/components/FilePreview.tsx`
- `features/explorer/components/JsonPreview.tsx`
- `features/explorer/components/MarkdownPreview.tsx`
- `features/explorer/components/ImagePreview.tsx`

For IntelligentEditor: check if it exists at `components/organisms/IntelligentEditor.tsx` in the review-workbench. If it needs CodeMirror dependencies, add them to `ui/package.json`:

```bash
cd ui && npm install @codemirror/lang-markdown @codemirror/lang-json @codemirror/state @codemirror/view codemirror
```

- [ ] **Step 3: Verify compilation**

Run: `cd ui && npx tsc --noEmit`
Expected: No errors (or only pre-existing errors)

- [ ] **Step 4: Commit**

```bash
git add ui/src/components/organisms/ ui/src/features/file-explorer/components/ ui/package.json ui/package-lock.json
git commit -m "feat(doc-router): copy shared components from review-workbench"
```

---

### Task 6: Frontend types and API client extensions

**Files:**
- Modify: `ui/src/types/graph.types.ts`
- Modify: `ui/src/api/client.ts`

- [ ] **Step 1: Add plan and file types**

Add to `ui/src/types/graph.types.ts`:

```typescript
// --- Plan types ---

export interface TouchEntry {
  path: string;
  symbol?: string;
  [key: string]: unknown;
}

export interface FileTag {
  file: string;
  lines: [number, number];
  comment: string;
  [key: string]: unknown;
}

export interface GraphChange {
  action: "add_touch" | "remove_touch" | "add_dependency";
  target: string;
  comment: string;
  [key: string]: unknown;
}

export interface PlanGroupSummary {
  group: string;
  latest_type: string;
  latest_version: number;
  status: string;
  domain: string;
  [key: string]: unknown;
}

export interface PlanChainEntry {
  type: string;
  version: number;
  status: string;
  id: string;
  [key: string]: unknown;
}

export interface PlanChain {
  group: string;
  chain: PlanChainEntry[];
  [key: string]: unknown;
}

export interface PlanContent {
  metadata: {
    id: string;
    type: string;
    group: string;
    version: number;
    status: string;
    parent: string | null;
    domain: string;
    stage: string;
    nature: string;
    touches: TouchEntry[];
    file_tags?: FileTag[];
    graph_changes?: GraphChange[];
    [key: string]: unknown;
  };
  content: string;
  [key: string]: unknown;
}

export interface SaveReviewBody {
  content: string;
  file_tags: FileTag[];
  graph_changes: GraphChange[];
  touches: TouchEntry[];
}

// --- File tree types ---

export interface FileEntry {
  name: string;
  path: string;
  is_dir: boolean;
  extension: string | null;
  child_count: number | null;
  [key: string]: unknown;
}

export interface FileContent {
  path: string;
  content: string;
  language: string;
  [key: string]: unknown;
}
```

- [ ] **Step 2: Extend API client**

Add to `ui/src/api/client.ts`:

```typescript
import type {
  PlanGroupSummary,
  PlanChain,
  PlanContent,
  SaveReviewBody,
  FileEntry,
  FileContent,
  TouchEntry,
} from "../types/graph.types";

// ... existing api object, add these methods:

  // Plans
  getPlans: () => get<PlanGroupSummary[]>("/api/plans"),

  getPlanChain: (group: string) =>
    get<PlanChain>(`/api/plans/${group}`),

  getPlanContent: (group: string, type: string, version: number) =>
    get<PlanContent>(`/api/plans/${group}/${type}_${version}`),

  saveReview: async (group: string, version: number, body: SaveReviewBody) => {
    const resp = await fetch(`/api/plans/${group}/review_${version}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    if (!resp.ok) throw new Error(`Save failed: ${resp.status}`);
    return resp.json();
  },

  // Files
  getFiles: (path = "") =>
    get<FileEntry[]>(`/api/files${path ? `?path=${encodeURIComponent(path)}` : ""}`),

  getFileContent: (path: string) =>
    get<FileContent>(`/api/files/content?path=${encodeURIComponent(path)}`),

  getFilesTouched: (group: string, version = 0) =>
    get<TouchEntry[]>(`/api/files/touched?group=${encodeURIComponent(group)}&version=${version}`),
```

- [ ] **Step 3: Commit**

```bash
git add ui/src/types/graph.types.ts ui/src/api/client.ts
git commit -m "feat(doc-router): add plan and file types + API client methods"
```

---

### Task 7: Frontend hooks for plans and files

**Files:**
- Create: `ui/src/features/plan-review/hooks/usePlans.ts`
- Create: `ui/src/features/file-explorer/hooks/useFiles.ts`

- [ ] **Step 1: Create plan hooks**

Create `ui/src/features/plan-review/hooks/usePlans.ts`:

```typescript
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { api } from "../../../api/client";
import type { SaveReviewBody } from "../../../types/graph.types";

export function usePlanGroups() {
  return useQuery({
    queryKey: ["plans"],
    queryFn: () => api.getPlans(),
    staleTime: 10_000,
  });
}

export function usePlanChain(group: string | null) {
  return useQuery({
    queryKey: ["plan-chain", group],
    queryFn: () => api.getPlanChain(group!),
    enabled: !!group,
    staleTime: 10_000,
  });
}

export function usePlanContent(
  group: string | null,
  type: string | null,
  version: number | null
) {
  return useQuery({
    queryKey: ["plan-content", group, type, version],
    queryFn: () => api.getPlanContent(group!, type!, version!),
    enabled: !!group && !!type && version !== null,
    staleTime: 10_000,
  });
}

export function useSaveReview() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: ({
      group,
      version,
      body,
    }: {
      group: string;
      version: number;
      body: SaveReviewBody;
    }) => api.saveReview(group, version, body),
    onSuccess: (_, vars) => {
      qc.invalidateQueries({ queryKey: ["plan-chain", vars.group] });
      qc.invalidateQueries({ queryKey: ["plans"] });
    },
  });
}
```

- [ ] **Step 2: Create file hooks**

Create `ui/src/features/file-explorer/hooks/useFiles.ts`:

```typescript
import { useQuery } from "@tanstack/react-query";
import { api } from "../../../api/client";

export function useFileTree(path: string) {
  return useQuery({
    queryKey: ["file-tree", path],
    queryFn: () => api.getFiles(path),
    staleTime: 30_000,
  });
}

export function useFileContent(path: string | null) {
  return useQuery({
    queryKey: ["file-content", path],
    queryFn: () => api.getFileContent(path!),
    enabled: !!path,
    staleTime: 30_000,
  });
}

export function useFilesTouched(group: string | null, version = 0) {
  return useQuery({
    queryKey: ["files-touched", group, version],
    queryFn: () => api.getFilesTouched(group!, version),
    enabled: !!group,
    staleTime: 10_000,
  });
}
```

- [ ] **Step 3: Commit**

```bash
git add ui/src/features/plan-review/hooks/ ui/src/features/file-explorer/hooks/
git commit -m "feat(doc-router): add React Query hooks for plans and files"
```

---

### Task 8: TabNav component and App routing

**Files:**
- Create: `ui/src/components/molecules/TabNav.tsx`
- Modify: `ui/src/App.tsx`

- [ ] **Step 1: Create TabNav**

Create `ui/src/components/molecules/TabNav.tsx`:

```typescript
import { cn } from "../../utils/cn";

export type TabId = "graph" | "plans" | "files";

interface TabNavProps {
  active: TabId;
  onChange: (tab: TabId) => void;
}

const TABS: { id: TabId; label: string }[] = [
  { id: "graph", label: "Graph" },
  { id: "plans", label: "Plans" },
  { id: "files", label: "Files" },
];

export function TabNav({ active, onChange }: TabNavProps) {
  return (
    <nav className="flex gap-1">
      {TABS.map((tab) => (
        <button
          key={tab.id}
          onClick={() => onChange(tab.id)}
          className={cn(
            "px-3 py-1.5 text-xs font-headline tracking-widest uppercase transition-colors",
            active === tab.id
              ? "text-[var(--color-primary)] border-b-2 border-[var(--color-primary)]"
              : "text-[var(--color-on-muted)] hover:text-[var(--color-on-surface)]"
          )}
        >
          {tab.label}
        </button>
      ))}
    </nav>
  );
}
```

- [ ] **Step 2: Update App.tsx to use TabNav**

Replace `ui/src/App.tsx`:

```typescript
import { useState } from "react";
import { TabNav, type TabId } from "./components/molecules/TabNav";
import { RouteGraphCanvas } from "./features/graph-explorer/components/RouteGraphCanvas";

export default function App() {
  const [activeTab, setActiveTab] = useState<TabId>("graph");

  return (
    <div className="h-screen flex flex-col bg-[var(--color-background)] text-[var(--color-on-surface)]">
      <header className="flex items-center gap-6 px-4 py-2 border-b border-[var(--color-outline)]/30 bg-[var(--color-surface)]">
        <h1 className="font-headline text-sm tracking-widest uppercase text-[var(--color-primary)]">
          Doc-Router
        </h1>
        <TabNav active={activeTab} onChange={setActiveTab} />
      </header>
      <main className="flex-1 min-h-0">
        {activeTab === "graph" && <RouteGraphCanvas />}
        {activeTab === "plans" && (
          <div className="flex items-center justify-center h-full text-[var(--color-on-muted)]">
            Plans view — coming next
          </div>
        )}
        {activeTab === "files" && (
          <div className="flex items-center justify-center h-full text-[var(--color-on-muted)]">
            Files view — coming next
          </div>
        )}
      </main>
    </div>
  );
}
```

- [ ] **Step 3: Verify UI compiles**

Run: `cd ui && npx vite build 2>&1 | tail -5`
Expected: Build succeeds

- [ ] **Step 4: Commit**

```bash
git add ui/src/components/molecules/TabNav.tsx ui/src/App.tsx
git commit -m "feat(doc-router): add TabNav and tabbed layout to App"
```

---

### Task 9: PlanList component

**Files:**
- Create: `ui/src/features/plan-review/components/PlanList.tsx`

- [ ] **Step 1: Create PlanList**

```typescript
import { usePlanGroups } from "../hooks/usePlans";
import { Badge } from "../../../components/atoms/Badge";
import { Spinner } from "../../../components/atoms/Spinner";
import { cn } from "../../../utils/cn";
import type { PlanGroupSummary } from "../../../types/graph.types";

interface PlanListProps {
  selectedGroup: string | null;
  onSelect: (group: string) => void;
}

const STATUS_VARIANT: Record<string, "primary" | "secondary" | "success" | "danger" | "muted"> = {
  draft: "muted",
  active: "primary",
  approved: "success",
  superseded: "secondary",
};

export function PlanList({ selectedGroup, onSelect }: PlanListProps) {
  const { data: groups, isLoading, error } = usePlanGroups();

  if (isLoading) return <div className="p-4 flex justify-center"><Spinner /></div>;
  if (error) return <div className="p-4 text-[var(--color-error)]">Failed to load plans</div>;
  if (!groups?.length) return <div className="p-4 text-[var(--color-on-muted)]">No plans found</div>;

  return (
    <div className="flex flex-col gap-1 p-2">
      {groups.map((g: PlanGroupSummary) => (
        <button
          key={g.group}
          onClick={() => onSelect(g.group)}
          className={cn(
            "flex items-center justify-between px-3 py-2 rounded text-left transition-colors",
            "hover:bg-[var(--color-primary)]/5",
            selectedGroup === g.group
              ? "bg-[var(--color-primary)]/10 border-r-2 border-[var(--color-primary)]"
              : "border-r-2 border-transparent"
          )}
        >
          <div>
            <div className="text-sm font-mono">{g.group}</div>
            <div className="text-[10px] text-[var(--color-on-muted)]">
              {g.domain} · v{g.latest_version} ({g.latest_type})
            </div>
          </div>
          <Badge variant={STATUS_VARIANT[g.status] || "muted"}>{g.status}</Badge>
        </button>
      ))}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add ui/src/features/plan-review/components/PlanList.tsx
git commit -m "feat(doc-router): add PlanList component"
```

---

### Task 10: IterationTimeline component

**Files:**
- Create: `ui/src/features/plan-review/components/IterationTimeline.tsx`

- [ ] **Step 1: Create IterationTimeline**

```typescript
import { usePlanChain } from "../hooks/usePlans";
import { Spinner } from "../../../components/atoms/Spinner";
import { cn } from "../../../utils/cn";
import type { PlanChainEntry } from "../../../types/graph.types";

interface IterationTimelineProps {
  group: string;
  selectedId: string | null;
  onSelect: (type: string, version: number) => void;
}

export function IterationTimeline({ group, selectedId, onSelect }: IterationTimelineProps) {
  const { data, isLoading } = usePlanChain(group);

  if (isLoading) return <div className="p-2 flex justify-center"><Spinner size="sm" /></div>;
  if (!data?.chain?.length) return null;

  return (
    <div className="flex items-center gap-1 px-3 py-2 overflow-x-auto border-b border-[var(--color-outline)]/20">
      {data.chain.map((entry: PlanChainEntry, i: number) => (
        <div key={entry.id} className="flex items-center gap-1">
          {i > 0 && (
            <span className="text-[var(--color-on-muted)] text-xs">→</span>
          )}
          <button
            onClick={() => onSelect(entry.type, entry.version)}
            className={cn(
              "px-2 py-1 rounded text-[10px] font-mono transition-colors",
              entry.type === "plan"
                ? "bg-[var(--color-primary)]/10 text-[var(--color-primary)]"
                : "bg-[var(--color-secondary)]/10 text-[var(--color-secondary)]",
              selectedId === entry.id && "ring-1 ring-[var(--color-primary)]",
              entry.status === "superseded" && "opacity-50"
            )}
          >
            {entry.type}_{entry.version}
          </button>
        </div>
      ))}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add ui/src/features/plan-review/components/IterationTimeline.tsx
git commit -m "feat(doc-router): add IterationTimeline component"
```

---

### Task 11: PlanEditor, TouchChips, and CommentDialog

**Files:**
- Create: `ui/src/features/plan-review/components/PlanEditor.tsx`
- Create: `ui/src/features/plan-review/components/TouchChips.tsx`
- Create: `ui/src/features/plan-review/components/CommentDialog.tsx`

- [ ] **Step 1: Create CommentDialog**

```typescript
import { useState } from "react";
import { Button } from "../../../components/atoms/Button";

interface CommentDialogProps {
  title: string;
  description: string;
  onSubmit: (comment: string) => void;
  onCancel: () => void;
}

export function CommentDialog({ title, description, onSubmit, onCancel }: CommentDialogProps) {
  const [comment, setComment] = useState("");

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
      <div className="bg-[var(--color-surface)] border border-[var(--color-outline)]/30 rounded-lg p-4 w-96 max-w-[90vw]">
        <h3 className="font-headline text-sm tracking-widest uppercase mb-1">{title}</h3>
        <p className="text-xs text-[var(--color-on-muted)] mb-3">{description}</p>
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Why this change?"
          className="w-full h-24 bg-[var(--color-background)] border border-[var(--color-outline)]/30 rounded px-3 py-2 text-sm font-mono text-[var(--color-on-surface)] resize-none focus:outline-none focus:border-[var(--color-primary)]"
          autoFocus
        />
        <div className="flex justify-end gap-2 mt-3">
          <Button variant="ghost" size="sm" onClick={onCancel}>Cancel</Button>
          <Button variant="primary" size="sm" onClick={() => onSubmit(comment)} disabled={!comment.trim()}>
            Save
          </Button>
        </div>
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Create TouchChips**

```typescript
import { cn } from "../../../utils/cn";
import type { TouchEntry } from "../../../types/graph.types";

interface TouchChipsProps {
  touches: TouchEntry[];
  onClickTouch: (touch: TouchEntry) => void;
}

export function TouchChips({ touches, onClickTouch }: TouchChipsProps) {
  if (!touches.length) return null;

  return (
    <div className="flex flex-wrap gap-1.5 px-3 py-2 border-b border-[var(--color-outline)]/20">
      <span className="text-[10px] text-[var(--color-on-muted)] uppercase tracking-wider self-center mr-1">
        Touches
      </span>
      {touches.map((t, i) => (
        <button
          key={`${t.path}-${i}`}
          onClick={() => onClickTouch(t)}
          className={cn(
            "inline-flex items-center gap-1 px-2 py-0.5 rounded",
            "text-[10px] font-mono",
            "border border-[var(--color-primary)]/30",
            "text-[var(--color-primary)] hover:bg-[var(--color-primary)]/10",
            "transition-colors cursor-pointer"
          )}
        >
          {t.path}
          {t.symbol && <span className="text-[var(--color-secondary)]">::{t.symbol}</span>}
        </button>
      ))}
    </div>
  );
}
```

- [ ] **Step 3: Create PlanEditor**

```typescript
import { useState, useCallback } from "react";
import { usePlanContent, useSaveReview } from "../hooks/usePlans";
import { Button } from "../../../components/atoms/Button";
import { Spinner } from "../../../components/atoms/Spinner";
import { TouchChips } from "./TouchChips";
import type { TouchEntry, FileTag, GraphChange } from "../../../types/graph.types";

interface PlanEditorProps {
  group: string;
  type: string;
  version: number;
  onNavigateToFile: (touch: TouchEntry) => void;
}

export function PlanEditor({ group, type, version, onNavigateToFile }: PlanEditorProps) {
  const { data, isLoading, error } = usePlanContent(group, type, version);
  const saveReview = useSaveReview();

  const [editedContent, setEditedContent] = useState<string | null>(null);
  const [fileTags, setFileTags] = useState<FileTag[]>([]);
  const [graphChanges, setGraphChanges] = useState<GraphChange[]>([]);
  const [dirty, setDirty] = useState(false);

  // Sync initial content when data loads
  const content = editedContent ?? data?.content ?? "";
  const touches = data?.metadata?.touches ?? [];

  const handleContentChange = useCallback((value: string) => {
    setEditedContent(value);
    setDirty(true);
  }, []);

  const handleSave = useCallback(() => {
    if (!data) return;
    saveReview.mutate({
      group,
      version,
      body: {
        content: editedContent ?? data.content,
        file_tags: fileTags,
        graph_changes: graphChanges,
        touches: data.metadata.touches ?? [],
      },
    });
    setDirty(false);
  }, [data, editedContent, fileTags, graphChanges, group, version, saveReview]);

  if (isLoading) return <div className="flex-1 flex items-center justify-center"><Spinner /></div>;
  if (error) return <div className="p-4 text-[var(--color-error)]">Failed to load plan</div>;
  if (!data) return null;

  return (
    <div className="flex flex-col h-full">
      <TouchChips touches={touches} onClickTouch={onNavigateToFile} />
      <div className="flex-1 min-h-0 overflow-auto p-4">
        <textarea
          value={content}
          onChange={(e) => handleContentChange(e.target.value)}
          className="w-full h-full bg-transparent font-mono text-sm text-[var(--color-on-surface)] resize-none focus:outline-none"
          spellCheck={false}
        />
      </div>
      <div className="flex items-center justify-between px-4 py-2 border-t border-[var(--color-outline)]/30 bg-[var(--color-surface)]">
        <div className="text-[10px] text-[var(--color-on-muted)]">
          {data.metadata.type} · v{data.metadata.version}
          {dirty && <span className="ml-2 text-[var(--color-secondary)]">● Modified</span>}
        </div>
        <Button
          variant="primary"
          size="sm"
          onClick={handleSave}
          disabled={!dirty || saveReview.isPending}
        >
          {saveReview.isPending ? "Saving..." : "Save Review"}
        </Button>
      </div>
    </div>
  );
}
```

Note: This uses a plain `<textarea>` for now. In Task 5 we copy IntelligentEditor — once that's integrated, PlanEditor should be updated to use it instead for CodeMirror-based editing with syntax highlighting. This is a follow-up refinement, not a blocker.

- [ ] **Step 4: Commit**

```bash
git add ui/src/features/plan-review/components/
git commit -m "feat(doc-router): add PlanEditor, TouchChips, CommentDialog components"
```

---

### Task 12: Plans tab — wire PlanList + Timeline + Editor

**Files:**
- Create: `ui/src/features/plan-review/components/PlansView.tsx`
- Modify: `ui/src/App.tsx`

- [ ] **Step 1: Create PlansView**

```typescript
import { useState, useCallback } from "react";
import { PlanList } from "./PlanList";
import { IterationTimeline } from "./IterationTimeline";
import { PlanEditor } from "./PlanEditor";
import type { TouchEntry } from "../../../types/graph.types";

interface PlansViewProps {
  onNavigateToFile: (touch: TouchEntry) => void;
}

export function PlansView({ onNavigateToFile }: PlansViewProps) {
  const [selectedGroup, setSelectedGroup] = useState<string | null>(null);
  const [selectedType, setSelectedType] = useState<string | null>(null);
  const [selectedVersion, setSelectedVersion] = useState<number | null>(null);
  const [selectedId, setSelectedId] = useState<string | null>(null);

  const handleSelectIteration = useCallback((type: string, version: number) => {
    setSelectedType(type);
    setSelectedVersion(version);
    setSelectedId(`${type}-${selectedGroup}-${version}`);
  }, [selectedGroup]);

  const handleSelectGroup = useCallback((group: string) => {
    setSelectedGroup(group);
    setSelectedType(null);
    setSelectedVersion(null);
    setSelectedId(null);
  }, []);

  return (
    <div className="flex h-full">
      {/* Left: plan list */}
      <div className="w-64 border-r border-[var(--color-outline)]/20 overflow-y-auto">
        <PlanList selectedGroup={selectedGroup} onSelect={handleSelectGroup} />
      </div>

      {/* Right: timeline + editor */}
      <div className="flex-1 flex flex-col min-w-0">
        {selectedGroup ? (
          <>
            <IterationTimeline
              group={selectedGroup}
              selectedId={selectedId}
              onSelect={handleSelectIteration}
            />
            {selectedType !== null && selectedVersion !== null ? (
              <PlanEditor
                group={selectedGroup}
                type={selectedType}
                version={selectedVersion}
                onNavigateToFile={onNavigateToFile}
              />
            ) : (
              <div className="flex-1 flex items-center justify-center text-[var(--color-on-muted)]">
                Select an iteration to view
              </div>
            )}
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-[var(--color-on-muted)]">
            Select a plan group
          </div>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Update App.tsx**

Replace the plans placeholder in App.tsx:

```typescript
import { useState, useCallback } from "react";
import { TabNav, type TabId } from "./components/molecules/TabNav";
import { RouteGraphCanvas } from "./features/graph-explorer/components/RouteGraphCanvas";
import { PlansView } from "./features/plan-review/components/PlansView";
import type { TouchEntry } from "./types/graph.types";

export default function App() {
  const [activeTab, setActiveTab] = useState<TabId>("graph");

  const handleNavigateToFile = useCallback((touch: TouchEntry) => {
    setActiveTab("files");
    // TODO: pass touch.path to Files view for auto-selection
  }, []);

  return (
    <div className="h-screen flex flex-col bg-[var(--color-background)] text-[var(--color-on-surface)]">
      <header className="flex items-center gap-6 px-4 py-2 border-b border-[var(--color-outline)]/30 bg-[var(--color-surface)]">
        <h1 className="font-headline text-sm tracking-widest uppercase text-[var(--color-primary)]">
          Doc-Router
        </h1>
        <TabNav active={activeTab} onChange={setActiveTab} />
      </header>
      <main className="flex-1 min-h-0">
        {activeTab === "graph" && <RouteGraphCanvas />}
        {activeTab === "plans" && <PlansView onNavigateToFile={handleNavigateToFile} />}
        {activeTab === "files" && (
          <div className="flex items-center justify-center h-full text-[var(--color-on-muted)]">
            Files view — coming next
          </div>
        )}
      </main>
    </div>
  );
}
```

- [ ] **Step 3: Verify build**

Run: `cd ui && npx vite build 2>&1 | tail -5`
Expected: Build succeeds

- [ ] **Step 4: Commit**

```bash
git add ui/src/features/plan-review/components/PlansView.tsx ui/src/App.tsx
git commit -m "feat(doc-router): wire Plans tab with list, timeline, and editor"
```

---

### Task 13: Files tab — FileExplorer with tree, preview, and TagBar

**Files:**
- Create: `ui/src/features/file-explorer/components/FileExplorer.tsx`
- Create: `ui/src/features/file-explorer/components/TagBar.tsx`
- Modify: `ui/src/App.tsx`

- [ ] **Step 1: Create TagBar**

```typescript
import { Button } from "../../../components/atoms/Button";
import type { FileTag } from "../../../types/graph.types";

interface TagBarProps {
  tags: FileTag[];
  onSave: () => void;
  onRemoveTag: (index: number) => void;
  dirty: boolean;
  saving: boolean;
}

export function TagBar({ tags, onSave, onRemoveTag, dirty, saving }: TagBarProps) {
  return (
    <div className="border-t border-[var(--color-outline)]/30 bg-[var(--color-surface)] px-4 py-2">
      <div className="flex items-center justify-between mb-1">
        <span className="text-[10px] text-[var(--color-on-muted)] uppercase tracking-wider">
          Tags ({tags.length})
        </span>
        <Button variant="primary" size="sm" onClick={onSave} disabled={!dirty || saving}>
          {saving ? "Saving..." : "Save Tags"}
        </Button>
      </div>
      {tags.length > 0 && (
        <div className="flex flex-col gap-1 max-h-24 overflow-y-auto">
          {tags.map((tag, i) => (
            <div key={i} className="flex items-center gap-2 text-xs font-mono">
              <span className="text-[var(--color-secondary)]">L{tag.lines[0]}-{tag.lines[1]}</span>
              <span className="text-[var(--color-on-surface)] flex-1 truncate">{tag.comment}</span>
              <button
                onClick={() => onRemoveTag(i)}
                className="text-[var(--color-on-muted)] hover:text-[var(--color-error)] transition-colors"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
```

- [ ] **Step 2: Create FileExplorer**

```typescript
import { useState, useCallback } from "react";
import { useFileTree, useFileContent } from "../hooks/useFiles";
import { Spinner } from "../../../components/atoms/Spinner";
import { TagBar } from "./TagBar";
import type { FileEntry, FileTag, TouchEntry } from "../../../types/graph.types";

interface FileExplorerProps {
  touchedPaths?: Set<string>;
  initialPath?: string;
}

export function FileExplorer({ touchedPaths, initialPath }: FileExplorerProps) {
  const [currentPath, setCurrentPath] = useState(initialPath ?? "");
  const [selectedFile, setSelectedFile] = useState<string | null>(null);
  const [tags, setTags] = useState<FileTag[]>([]);
  const [tagsDirty, setTagsDirty] = useState(false);

  const { data: entries, isLoading: treeLoading } = useFileTree(currentPath);
  const { data: fileContent, isLoading: contentLoading } = useFileContent(selectedFile);

  const handleEntryClick = useCallback((entry: FileEntry) => {
    if (entry.is_dir) {
      setCurrentPath(entry.path);
      setSelectedFile(null);
    } else {
      setSelectedFile(entry.path);
    }
  }, []);

  const handleBreadcrumb = useCallback((path: string) => {
    setCurrentPath(path);
    setSelectedFile(null);
  }, []);

  // Build breadcrumb parts
  const pathParts = currentPath ? currentPath.split("/") : [];
  const breadcrumbs = pathParts.map((part, i) => ({
    label: part,
    path: pathParts.slice(0, i + 1).join("/"),
  }));

  return (
    <div className="flex h-full">
      {/* Left: file tree */}
      <div className="w-72 border-r border-[var(--color-outline)]/20 flex flex-col">
        {/* Breadcrumb */}
        <div className="px-3 py-2 border-b border-[var(--color-outline)]/20 text-xs font-mono">
          <button
            onClick={() => handleBreadcrumb("")}
            className="text-[var(--color-primary)]/70 hover:text-[var(--color-primary)]"
          >
            ROOT
          </button>
          {breadcrumbs.map((bc) => (
            <span key={bc.path}>
              <span className="text-[var(--color-on-muted)] mx-1">/</span>
              <button
                onClick={() => handleBreadcrumb(bc.path)}
                className="text-[var(--color-primary)]/70 hover:text-[var(--color-primary)]"
              >
                {bc.label}
              </button>
            </span>
          ))}
        </div>

        {/* Entry list */}
        <div className="flex-1 overflow-y-auto">
          {treeLoading ? (
            <div className="p-4 flex justify-center"><Spinner /></div>
          ) : (
            entries?.map((entry: FileEntry) => (
              <button
                key={entry.path}
                onClick={() => handleEntryClick(entry)}
                className={`flex items-center gap-2 w-full px-3 py-1.5 text-left text-sm hover:bg-[var(--color-primary)]/5 transition-colors ${
                  selectedFile === entry.path ? "bg-[var(--color-primary)]/10 border-r-2 border-[var(--color-primary)]" : ""
                }`}
              >
                <span className="text-[var(--color-on-muted)] text-xs">
                  {entry.is_dir ? "📁" : "📄"}
                </span>
                <span className="flex-1 truncate font-mono text-xs">{entry.name}</span>
                {touchedPaths?.has(entry.path) && (
                  <span className="w-2 h-2 rounded-full bg-[var(--color-primary)]" />
                )}
              </button>
            ))
          )}
        </div>
      </div>

      {/* Right: file preview + tag bar */}
      <div className="flex-1 flex flex-col min-w-0">
        {selectedFile ? (
          <>
            <div className="px-4 py-2 border-b border-[var(--color-outline)]/20 text-xs font-mono text-[var(--color-on-muted)]">
              {selectedFile}
              {fileContent && (
                <span className="ml-2 text-[var(--color-primary)]">({fileContent.language})</span>
              )}
            </div>
            <div className="flex-1 overflow-auto p-4">
              {contentLoading ? (
                <div className="flex justify-center"><Spinner /></div>
              ) : fileContent ? (
                <pre className="font-mono text-sm text-[var(--color-on-surface)] whitespace-pre-wrap">
                  {fileContent.content}
                </pre>
              ) : null}
            </div>
            <TagBar
              tags={tags.filter((t) => t.file === selectedFile)}
              onSave={() => { setTagsDirty(false); /* TODO: save to review */ }}
              onRemoveTag={(i) => {
                setTags((prev) => prev.filter((_, idx) => idx !== i));
                setTagsDirty(true);
              }}
              dirty={tagsDirty}
              saving={false}
            />
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-[var(--color-on-muted)]">
            Select a file to preview
          </div>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 3: Update App.tsx — wire Files tab**

Replace the files placeholder with:

```typescript
import { FileExplorer } from "./features/file-explorer/components/FileExplorer";

// In the render:
{activeTab === "files" && <FileExplorer />}
```

- [ ] **Step 4: Verify build**

Run: `cd ui && npx vite build 2>&1 | tail -5`
Expected: Build succeeds

- [ ] **Step 5: Commit**

```bash
git add ui/src/features/file-explorer/components/ ui/src/App.tsx
git commit -m "feat(doc-router): add Files tab with FileExplorer, tree, preview, and TagBar"
```

---

### Task 14: GraphEditPanel — mini graph for editing touches

**Files:**
- Create: `ui/src/features/plan-review/components/GraphEditPanel.tsx`

- [ ] **Step 1: Create GraphEditPanel**

```typescript
import { useState, useCallback, useMemo } from "react";
import {
  ReactFlow,
  Background,
  Controls,
  type Node,
  type Edge,
} from "@xyflow/react";
import "@xyflow/react/dist/style.css";
import { CommentDialog } from "./CommentDialog";
import { Button } from "../../../components/atoms/Button";
import type { TouchEntry, GraphChange } from "../../../types/graph.types";

interface GraphEditPanelProps {
  touches: TouchEntry[];
  graphChanges: GraphChange[];
  onAddTouch: (change: GraphChange) => void;
  onRemoveTouch: (change: GraphChange) => void;
}

export function GraphEditPanel({
  touches,
  graphChanges,
  onAddTouch,
  onRemoveTouch,
}: GraphEditPanelProps) {
  const [commentDialog, setCommentDialog] = useState<{
    action: "add_touch" | "remove_touch";
    target: string;
  } | null>(null);
  const [newTouchPath, setNewTouchPath] = useState("");

  // Build nodes from touches
  const nodes: Node[] = useMemo(
    () =>
      touches.map((t, i) => ({
        id: t.path,
        position: { x: 20, y: i * 60 + 20 },
        data: { label: `${t.path}${t.symbol ? `::${t.symbol}` : ""}` },
        style: {
          background: "var(--color-surface)",
          border: "1px solid var(--color-primary)",
          color: "var(--color-on-surface)",
          fontSize: "10px",
          fontFamily: "JetBrains Mono, monospace",
          padding: "4px 8px",
          borderRadius: "4px",
        },
      })),
    [touches]
  );

  const handleRemove = useCallback(
    (path: string) => {
      setCommentDialog({ action: "remove_touch", target: path });
    },
    []
  );

  const handleAdd = useCallback(() => {
    if (!newTouchPath.trim()) return;
    setCommentDialog({ action: "add_touch", target: newTouchPath.trim() });
  }, [newTouchPath]);

  const handleCommentSubmit = useCallback(
    (comment: string) => {
      if (!commentDialog) return;
      const change: GraphChange = {
        action: commentDialog.action,
        target: commentDialog.target,
        comment,
      };
      if (commentDialog.action === "add_touch") {
        onAddTouch(change);
      } else {
        onRemoveTouch(change);
      }
      setCommentDialog(null);
      setNewTouchPath("");
    },
    [commentDialog, onAddTouch, onRemoveTouch]
  );

  return (
    <div className="border-t border-[var(--color-outline)]/20">
      <div className="px-3 py-2 flex items-center gap-2">
        <span className="text-[10px] text-[var(--color-on-muted)] uppercase tracking-wider">
          Touch Graph
        </span>
        <input
          value={newTouchPath}
          onChange={(e) => setNewTouchPath(e.target.value)}
          placeholder="src/path/to/file.py"
          className="flex-1 bg-[var(--color-background)] border border-[var(--color-outline)]/30 rounded px-2 py-1 text-xs font-mono text-[var(--color-on-surface)] focus:outline-none focus:border-[var(--color-primary)]"
        />
        <Button variant="ghost" size="sm" onClick={handleAdd} disabled={!newTouchPath.trim()}>
          + Add
        </Button>
      </div>

      <div className="h-48">
        <ReactFlow nodes={nodes} edges={[]} fitView>
          <Background />
        </ReactFlow>
      </div>

      {/* Changes log */}
      {graphChanges.length > 0 && (
        <div className="px-3 py-2 border-t border-[var(--color-outline)]/10">
          <span className="text-[10px] text-[var(--color-on-muted)] uppercase">Changes ({graphChanges.length})</span>
          {graphChanges.map((gc, i) => (
            <div key={i} className="text-xs font-mono mt-1">
              <span className={gc.action === "add_touch" ? "text-green-400" : "text-red-400"}>
                {gc.action}
              </span>
              {" "}{gc.target}
              <span className="text-[var(--color-on-muted)]"> — {gc.comment}</span>
            </div>
          ))}
        </div>
      )}

      {commentDialog && (
        <CommentDialog
          title={commentDialog.action === "add_touch" ? "Add Touch" : "Remove Touch"}
          description={`${commentDialog.action === "add_touch" ? "Adding" : "Removing"}: ${commentDialog.target}`}
          onSubmit={handleCommentSubmit}
          onCancel={() => setCommentDialog(null)}
        />
      )}
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add ui/src/features/plan-review/components/GraphEditPanel.tsx
git commit -m "feat(doc-router): add GraphEditPanel with touch editing and comment prompts"
```

---

### Task 15: E2E test — create sample plan, verify full cycle

**Files:**
- Create: test plan fixture for live testing

- [ ] **Step 1: Create a sample plan in the project**

Create `docs/plans/doc-router-phase2/plan_doc-router-phase2_0.md`:

```markdown
---
id: plan-doc-router-phase2-0
domain: practices
stage: global
nature: development
type: plan
group: doc-router-phase2
version: 0
parent: null
status: active
touches:
  - path: src/doc_router/plans.py
  - path: src/doc_router/filetree.py
  - path: src/doc_router/server.py
  - path: ui/src/App.tsx
---

# Doc-Router Phase 2 Plan

Extend Doc-Router with plan review workspace, file tree browser, and interactive editor.

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/superpowers/plans/2026-03-23-doc-router-phase2.md`.