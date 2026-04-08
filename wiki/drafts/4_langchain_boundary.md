---
identity:
  node_id: "doc:wiki/drafts/4_langchain_boundary.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md", relation_type: "documents"}
---

The model invocation boundary is narrow and typed:

## Details

The model invocation boundary is narrow and typed:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = ChatPromptTemplate.from_messages([...])
chain = prompt | model.with_structured_output(OutputContract)
result = chain.invoke(prompt_variables)
```

Rules:
- `with_structured_output` against a Pydantic model defined in `contracts.py` — never raw string parsing
- Prompt serialization lives in `prompt.py`, not in the node
- The LLM boundary node validates the returned model before storing it in state

---

Generated from `raw/docs_postulador_refactor/docs/standards/code/llm_langgraph_components.md`.