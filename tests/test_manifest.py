from __future__ import annotations
import csv
from pathlib import Path
import pytest
from wiki_compiler.manifest import add_to_manifest, load_manifest, compute_content_hash

def test_manifest_adds_and_persists_entry(tmp_path: Path):
    source = tmp_path / "raw/source.txt"
    source.parent.mkdir(parents=True)
    source.write_text("hello manifest", encoding="utf-8")
    
    manifest_path = tmp_path / "manifests/raw_sources.csv"
    
    entry = add_to_manifest(
        project_root=tmp_path,
        manifest_path=manifest_path,
        source_path=source,
        notes="First test"
    )
    
    assert entry.filename == "source.txt"
    assert entry.path == "raw/source.txt"
    assert entry.file_kind == "txt"
    assert entry.content_hash == compute_content_hash(source)
    assert entry.status == "new"
    assert entry.notes == "First test"
    
    # Verify CSV persistence
    assert manifest_path.exists()
    with open(manifest_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert len(rows) == 1
        assert rows[0]["path"] == "raw/source.txt"
        assert rows[0]["content_hash"] == entry.content_hash

def test_manifest_updates_existing_entry(tmp_path: Path):
    source = tmp_path / "raw/source.txt"
    source.parent.mkdir(parents=True)
    source.write_text("initial", encoding="utf-8")
    
    manifest_path = tmp_path / "manifests/raw_sources.csv"
    
    add_to_manifest(tmp_path, manifest_path, source)
    
    # Change content
    source.write_text("updated", encoding="utf-8")
    new_hash = compute_content_hash(source)
    
    updated_entry = add_to_manifest(tmp_path, manifest_path, source, notes="Updated note")
    
    assert updated_entry.content_hash == new_hash
    assert updated_entry.notes == "Updated note"
    
    entries = load_manifest(manifest_path)
    assert len(entries) == 1
    assert entries[0].content_hash == new_hash
