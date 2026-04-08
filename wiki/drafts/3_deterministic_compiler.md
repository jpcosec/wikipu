---
identity:
  node_id: "doc:wiki/drafts/3_deterministic_compiler.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md", relation_type: "documents"}
---

### ContextRouter Class

## Details

### ContextRouter Class

```python
# src/tools/context_router.py

import json
import glob
from pathlib import Path
from typing import Optional

class ContextRouter:
    def __init__(self, matrix_path: str = "docs/index/routing_matrix.json"):
        self.matrix = self._load_matrix(matrix_path)
        self.base_path = Path(".")
        
    def _load_matrix(self, path: str) -> list[dict]:
        """Load the routing matrix."""
        with open(path) as f:
            return json.load(f).get("matrix", [])
    
    def _read_file(self, path: str) -> str:
        """Safe file reading."""
        try:
            full_path = self.base_path / path
            return full_path.read_text()
        except FileNotFoundError:
            return f"[FILE NOT FOUND: {path}]"
    
    def _resolve_glob(self, pattern: str) -> list[str]:
        """Resolve glob patterns to real files."""
        return glob.glob(pattern, recursive=True)
    
    def fetch_context(
        self,
        domain: Optional[str] = None,
        stage: Optional[str] = None,
        state: str = "runtime",
        include_code: bool = False,
        nature: Optional[str] = None
    ) -> str:
        """
        Deterministic tool to retrieve context.
        Acts as MCP endpoint for the AI Agent.
        """
        parts = [f"# CONTEXT | domain={domain or 'ALL'} | stage={stage or 'ALL'} | state={state}"]
        
        # 1. Filter by orthogonal coordinates
        entries = []
        for entry in self.matrix:
            if domain and entry.get("domain") != domain:
                continue
            if stage and entry.get("stage") != stage:
                continue
            if nature and entry.get("nature") != nature:
                continue
            doc_path = entry.get("doc_path", "")
            if state == "runtime" and doc_path.startswith("plan/"):
                continue
            if state == "plan" and not doc_path.startswith("plan/"):
                continue
            entries.append(entry)
        
        if not entries:
            return f"# EMPTY | No documents for domain={domain}, stage={stage}, state={state}"
        
        # 2. Assemble Documentation
        parts.append("\n## DOCUMENTATION\n")
        for entry in entries:
            doc_path = entry.get("doc_path")
            if doc_path:
                parts.append(f"\n### FILE: {doc_path}\n```markdown\n{self._read_file(doc_path)}\n```")
        
        # 3. Assemble Source Code
        if include_code:
            parts.append("\n## SOURCE CODE\n")
            for entry in entries:
                for pattern in entry.get("target_code", []):
                    for file_path in self._resolve_glob(pattern):
                        ext = file_path.split('.')[-1]
                        parts.append(f"\n### FILE: {file_path}\n```{ext}\n{self._read_file(file_path)}\n```")
        
        return "\n".join(parts)
```

---

Generated from `raw/docs_doc_methodology/doc-methodology-2.0/docs/seed/practices/12_context_router_protocol.md`.