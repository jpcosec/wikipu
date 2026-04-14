---
identity:
  node_id: "doc:wiki/standards/facet_injectors.md"
  node_type: "doc_standard"
edges:
  - target_id: "file:src/wiki_compiler/facet_injectors.py"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_injectors.py:ADRInjector"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_injectors.py:TestMapInjector"
    relation_type: documents
  - target_id: "code:src/wiki_compiler/facet_injectors.py:_module_to_node_id"
    relation_type: documents
---

Enriches Knowledge Graph nodes with additional facets by scanning architectural decisions and test files. This module contains injectors that populate ADR and Test Map information into nodes during the build process.

## Rule Schema

```python
class ADRInjector:
    def inject(self, node: KnowledgeNode, context: InjectionContext) -> KnowledgeNode: ...

class TestMapInjector:
    def inject(self, node: KnowledgeNode, context: InjectionContext) -> KnowledgeNode: ...
```

## Fields

- `ADRInjector.spec`: `FacetSpec` for the `adr` facet.
- `TestMapInjector.spec`: `FacetSpec` for the `test_map` facet.

## Usage Examples

```python
from wiki_compiler.facet_injectors import ADRInjector, TestMapInjector
from wiki_compiler.registry import InjectionContext

ctx = InjectionContext(project_root=".", adr_dir="wiki/adrs", tests_dir="tests")
adr_injector = ADRInjector()
# node is a KnowledgeNode instance
enriched_node = adr_injector.inject(node, ctx)
```
