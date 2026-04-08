---
identity:
  node_id: "doc:wiki/drafts/7_cli_entry_points.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/basic.md", relation_type: "documents"}
---

Every module that can be run standalone has a `main.py` with a `_build_parser()` function. Arguments are defined there — not duplicated in READMEs.

## Details

Every module that can be run standalone has a `main.py` with a `_build_parser()` function. Arguments are defined there — not duplicated in READMEs.

`main()` accepts an optional `argv: list[str] | None = None` parameter for testability. Returns an integer exit code.

```python
def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    ...
    return 0
```

Generated from `raw/docs_postulador_refactor/docs/standards/code/basic.md`.