# Scanner Plugin Interface

**Explanation:** The wiki-compiler currently has one scanner: a Python AST scanner (`src/wiki_compiler/`). It extracts code nodes (ASTFacet, SemanticFacet, IOFacet) from `.py` files and produces `KnowledgeNode` instances. When the project includes TypeScript, Go, or any other language, there is no path to extract code nodes from those files — the graph simply has no representation of non-Python code. This breaks ID-6 (Traceable Causality) and ID-7 (Self-Inclusion) for any multi-language codebase.

**The architecture:** Validation and extraction are separated by design. The wiki-compiler (Python) always runs validation against the normalized `KnowledgeNode` format regardless of source language. Each language has a scanner that transforms source code into `KnowledgeNode` instances. The wiki-compiler orchestrates the scanners; the language toolchains (ruff, tsc, ESLint) enforce style separately and are not replaced by this system.

```
source code (any language)
    → language scanner plugin → KnowledgeNode (contracts.py)
    → wiki-compiler graph build + validate → pass/fail

per-language style toolchain (ruff / tsc / eslint / ...)
    → separate CI step
```

**Reference:** `wiki/reference/knowledge_node_facets.md`, `wiki/standards/artifacts/wiki_node.md`, `wiki/standards/languages/`

**What to fix:** Define and implement a scanner plugin interface so that any language can contribute nodes to the graph.

**How to do it:**
1. Define `ScannerPlugin` protocol in `contracts.py`: `scan(path: Path) -> list[KnowledgeNode]`. Plugins are discovered by file extension or explicit configuration in `.wiki-compiler.yml`.
2. Refactor the existing Python AST scanner into a `PythonScanner` that implements `ScannerPlugin`.
3. Implement `TypeScriptScanner` as the first non-Python plugin — uses `ts-morph` or TypeScript compiler API via subprocess; outputs ASTFacet, SemanticFacet, IOFacet nodes in the same format as the Python scanner.
4. Add scanner registration to `wiki-compiler build` — auto-detects installed scanner plugins.
5. Document the plugin contract in `wiki/standards/artifacts/` or `wiki/how_to/` so that adding a new language scanner is a self-contained, documented operation.

**Depends on:** `unimplemented/artifact-schema-validation.md` (KnowledgeNode schema must be stable before scanners target it)
