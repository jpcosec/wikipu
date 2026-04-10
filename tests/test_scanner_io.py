from __future__ import annotations
import ast
import pytest
from wiki_compiler.scanner import infer_io_from_ast
from wiki_compiler.contracts import IOFacet

def test_infer_io_pathlib_read_write():
    code = """
from pathlib import Path
p = Path("data.txt")
content = Path("input.txt").read_text()
Path("output.txt").write_text("hello")
Path("binary.dat").read_bytes()
Path("out.dat").write_bytes(b"data")
"""
    tree = ast.parse(code)
    ports = infer_io_from_ast(tree)
    
    # We expect 4 ports from the direct Path("...").method() calls.
    # p = Path("data.txt") is a call but not a read/write call.
    assert len(ports) == 4
    
    # Path("input.txt").read_text()
    assert any(p.path_template == "input.txt" and p.direction == "input" and p.medium == "disk" for p in ports)
    # Path("output.txt").write_text("hello")
    assert any(p.path_template == "output.txt" and p.direction == "output" and p.medium == "disk" for p in ports)
    # Path("binary.dat").read_bytes()
    assert any(p.path_template == "binary.dat" and p.direction == "input" and p.medium == "disk" for p in ports)
    # Path("out.dat").write_bytes(b"data")
    assert any(p.path_template == "out.dat" and p.direction == "output" and p.medium == "disk" for p in ports)

def test_infer_io_json_load_dump():
    code = """
import json
with open("data.json", "r") as f:
    data = json.load(f)

with open("out.json", "w") as f:
    json.dump(data, f)
"""
    tree = ast.parse(code)
    ports = infer_io_from_ast(tree)
    
    # 2 from open(), 2 from json.load/dump = 4
    assert len(ports) == 4
    
    # json.load(f)
    assert any(p.direction == "input" and p.medium == "disk" and p.path_template is None for p in ports)
    # json.dump(data, f)
    assert any(p.direction == "output" and p.medium == "disk" and p.path_template is None for p in ports)
    
    # open() calls
    assert any(p.path_template == "data.json" and p.direction == "input" for p in ports)
    assert any(p.path_template == "out.json" and p.direction == "output" for p in ports)

def test_infer_io_open_modes():
    code = """
open("read.txt")
open("write.txt", "w")
open("append.txt", "a")
open("exclusive.txt", "x")
open("rb.txt", "rb")
"""
    tree = ast.parse(code)
    ports = infer_io_from_ast(tree)
    assert len(ports) == 5
    
    assert any(p.path_template == "read.txt" and p.direction == "input" for p in ports)
    assert any(p.path_template == "write.txt" and p.direction == "output" for p in ports)
    assert any(p.path_template == "append.txt" and p.direction == "output" for p in ports)
    assert any(p.path_template == "exclusive.txt" and p.direction == "output" for p in ports)
    assert any(p.path_template == "rb.txt" and p.direction == "input" for p in ports)
