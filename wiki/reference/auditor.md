---
identity:
  node_id: "doc:wiki/reference/auditor.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/auditor.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:AuditReport"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:UndocumentedCodeCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:MissingDocstringsCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:UntypedIOCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:ComplianceViolationsCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:StaleEdgesCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:OrphanedPlansCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:MissingAbstractCheck"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/auditor.py:run_audit"
    relation_type: documents
---

Audit system for checking Knowledge Graph quality and compliance. Includes checks for missing docstrings, undocumented code, and stale edges.

## Signature or Schema

```python
def run_audit(graph: nx.DiGraph) -> AuditReport
```

The auditor uses a collection of internal check classes, each implementing a `run(graph)` method that returns a list of `AuditFinding` objects.

## Fields

- `AuditReport.findings`: List of `AuditFinding` discovered.
- `AuditFinding.check_name`: String identifier of the check.
- `AuditFinding.node_id`: ID of the failing node.
- `AuditFinding.detail`: Human-readable failure reason.

## Usage Examples

```python
from wiki_compiler.auditor import run_audit
import networkx as nx

graph = nx.DiGraph() # Loaded from knowledge_graph.json
report = run_audit(graph)
for check, count in report.summary.items():
    print(f"{check}: {count}")
```
