---
identity:
  node_id: "doc:wiki/drafts/7_studio_exposure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

Every LangGraph module exposes a `create_studio_graph()` factory and an entry in `langgraph.json`.

## Details

Every LangGraph module exposes a `create_studio_graph()` factory and an entry in `langgraph.json`.

```python
def create_studio_graph():
    """Create a Studio-friendly compiled graph.
    Loads even without model credentials — uses demo chain if API key absent.
    """
    return build_graph(
        chain=_build_studio_chain(),
        checkpointer=InMemorySaver(),
    )

def _build_studio_chain():
    if os.getenv("GOOGLE_API_KEY"):
        return build_default_chain()
    return _DemoChain()
```

The demo chain must produce structurally valid output (pass `with_structured_output` validation) so the full graph lifecycle can be exercised without credentials. It should be clearly identifiable in artifacts (`summary_notes` or similar field).

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.