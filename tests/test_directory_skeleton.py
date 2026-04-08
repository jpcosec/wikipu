from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.builder import build_directory_skeleton


def write(path: Path, content: str = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_skeleton_creates_directory_nodes_with_contains_edges(tmp_path: Path) -> None:
    write(tmp_path / "src/module/__init__.py")
    write(tmp_path / "src/module/main.py")

    nodes = build_directory_skeleton(root=tmp_path / "src", project_root=tmp_path)
    node_map = {n.identity.node_id: n for n in nodes}

    assert "dir:src" in node_map
    assert "dir:src/module" in node_map

    src_targets = {e.target_id for e in node_map["dir:src"].edges}
    assert "dir:src/module" in src_targets

    module_targets = {e.target_id for e in node_map["dir:src/module"].edges}
    assert "file:src/module/__init__.py" in module_targets
    assert "file:src/module/main.py" in module_targets


def test_skeleton_node_type_is_directory(tmp_path: Path) -> None:
    write(tmp_path / "src/a.py")
    nodes = build_directory_skeleton(root=tmp_path / "src", project_root=tmp_path)
    dir_node = next(n for n in nodes if n.identity.node_id == "dir:src")
    assert dir_node.identity.node_type == "directory"


def test_skeleton_empty_directory(tmp_path: Path) -> None:
    (tmp_path / "src").mkdir()
    nodes = build_directory_skeleton(root=tmp_path / "src", project_root=tmp_path)
    assert any(n.identity.node_id == "dir:src" for n in nodes)
