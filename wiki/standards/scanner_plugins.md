---
identity:
  node_id: "doc:wiki/standards/scanner_plugins.md"
  node_type: "doc_standard"
edges:
  - {target_id: "doc:wiki/reference/knowledge_node_facets.md", relation_type: "documents"}
  - {target_id: "file:src/wiki_compiler/protocols.py", relation_type: "documents"}
  - {target_id: "code:src/wiki_compiler/protocols.py:ScannerPlugin", relation_type: "documents"}
compliance:
  status: "implemented"
  failing_standards: []
---

Scanner plugins are the mechanism through which the Wikipu ecosystem extracts KnowledgeNodes from source code files of different languages. Each plugin is responsible for parsing a file and producing a list of normalized nodes.

## Rule Schema

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

## Fields

- `supported_extensions`: A set of string extensions (e.g., `['.py']`) that this plugin can process.
- `path`: The absolute or relative path to the file to be scanned.
- `project_root`: The root directory of the repository, used for resolving relative paths.

## Usage Examples

```python
from wiki_compiler.scanner import PythonScanner
from pathlib import Path

scanner = PythonScanner()
nodes = scanner.scan(Path("src/main.py"), Path("."))
print(f"Extracted {len(nodes)} nodes.")
```

## Built-in Scanners

### PythonScanner
The primary scanner for the Wikipu project itself. It uses the `ast` module to perform deep static analysis of Python files.

### TypeScriptScanner
A basic scanner for `.ts` and `.tsx` files. Currently provides file-level nodes.
