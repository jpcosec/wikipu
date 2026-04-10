from __future__ import annotations
from pathlib import Path
import pytest
from wiki_compiler.scanner import scan_codebase, PythonScanner, TypeScriptScanner

def test_scan_codebase_multiple_languages(tmp_path: Path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    
    # Python file
    py_file = src_dir / "app.py"
    py_file.write_text('"""App module."""\ndef main(): pass', encoding="utf-8")
    
    # TS file
    ts_file = src_dir / "utils.ts"
    ts_file.write_text('// TS module', encoding="utf-8")
    
    # Generic text file (should be skipped)
    txt_file = src_dir / "readme.txt"
    txt_file.write_text("hello", encoding="utf-8")
    
    nodes = scan_codebase(project_root=tmp_path, source_roots=[src_dir])
    
    # Should have nodes for app.py (and its main function) and utils.ts
    node_ids = [n.identity.node_id for n in nodes]
    assert "file:src/app.py" in node_ids
    assert "code:src/app.py:main" in node_ids
    assert "file:src/utils.ts" in node_ids
    assert "file:src/readme.txt" not in node_ids

def test_scan_codebase_with_custom_plugin(tmp_path: Path):
    from wiki_compiler.contracts import KnowledgeNode, SystemIdentity
    from wiki_compiler.protocols import ScannerPlugin
    
    class GoScanner:
        @property
        def supported_extensions(self) -> set[str]:
            return {".go"}
        def scan(self, path: Path, project_root: Path) -> list[KnowledgeNode]:
            return [KnowledgeNode(identity=SystemIdentity(node_id=f"file:{path.relative_to(project_root).as_posix()}", node_type="file"))]
            
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    go_file = src_dir / "main.go"
    go_file.write_text("package main", encoding="utf-8")
    
    # Default plugins won't see .go
    nodes_default = scan_codebase(project_root=tmp_path, source_roots=[src_dir])
    assert not any("main.go" in n.identity.node_id for n in nodes_default)
    
    # Custom plugin should see .go
    nodes_custom = scan_codebase(project_root=tmp_path, source_roots=[src_dir], plugins=[GoScanner(), PythonScanner()])
    assert any("main.go" in n.identity.node_id for n in nodes_custom)
