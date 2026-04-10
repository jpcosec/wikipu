---
identity:
  node_id: "doc:wiki/reference/scanner_plugins.md"
  node_type: "reference"
edges:
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

# Scanner Plugins

Scanner plugins are the mechanism through which the Wikipu ecosystem extracts KnowledgeNodes from source code files of different languages. Each plugin is responsible for parsing a file and producing a list of normalized nodes.

## The ScannerPlugin Protocol

Any class implementing the `ScannerPlugin` protocol (defined in `src/wiki_compiler/protocols.py`) can be used to scan the codebase.

```python
class ScannerPlugin(Protocol):
    @property
    def supported_extensions(self) -> set[str]:
        """Returns the set of file extensions this scanner handles (e.g. {'.py'})."""
        ...

    def scan(self, path: Path, project_root: Path) -> list[KnowledgeNode]:
        """Scans a file and returns extracted knowledge nodes."""
        ...
```

## Built-in Scanners

### PythonScanner
The primary scanner for the Wikipu project itself. It uses the `ast` module to perform deep static analysis of Python files, extracting:
- **ASTFacet**: Signatures, base classes, and internal structure.
- **SemanticFacet**: Docstring-based intent extraction.
- **IOFacet**: Static inference of file and network I/O.

### TypeScriptScanner
A basic scanner for `.ts` and `.tsx` files. Currently provides file-level nodes; deep extraction of interfaces and functions is planned for future iterations.

## Adding a New Scanner

To add support for a new language:
1. Implement the `ScannerPlugin` protocol in a new class.
2. Register the plugin in `src/wiki_compiler/scanner.py` or provide it to `scan_codebase` via configuration.
3. Ensure the plugin maps its native AST structures to the unified `KnowledgeNode` format.
