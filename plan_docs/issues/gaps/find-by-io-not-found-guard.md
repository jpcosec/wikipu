# validate-wiki Missing-File Guard

**Explanation:** `wiki-compiler validate-wiki --path <path>` reports `rule_id: "artifact/frontmatter"` when the file does not exist, because the bare `except Exception` in `validate_wiki_artifact` absorbs the OS `FileNotFoundError` and surfaces it as a frontmatter error. This is misleading — the artifact is not malformed, it simply does not exist. Any automated traversal that calls `validate-wiki` on graph-referenced but disk-absent paths (e.g. `wiki/adrs/Index.md`) will produce false `is_valid: false` with a confusing message.

**Reference:** `src/wiki_compiler/artifact_validation.py` (`validate_wiki_artifact`)

**What to fix:** Add a path-existence check before `parse_markdown_node` that returns a dedicated `rule_id: "artifact/not_found"` finding immediately, without falling through to the frontmatter parser.

**How to do it:**
1. At the top of `validate_wiki_artifact`, add: `if not path.exists(): return ArtifactValidationReport(path=..., is_valid=False, findings=[ArtifactValidationFinding(rule_id="artifact/not_found", message=f"File not found: {path}")])`.
2. Add a unit test: `validate_wiki_artifact(Path("nonexistent.md"))` returns `is_valid=False` with `rule_id="artifact/not_found"`, not `"artifact/frontmatter"`.

**Depends on:** `none`
