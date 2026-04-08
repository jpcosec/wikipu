---
identity:
  node_id: "doc:wiki/drafts/9_summary_when_llm_is_actually_needed.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### ✅ Valid LLM Use Cases (Rare):

## Details

### ✅ Valid LLM Use Cases (Rare):
1. **Sentiment analysis** and emotional understanding
2. **Knowledge graph extraction** requiring semantic reasoning
3. **Content summarization** and insight generation
4. **Unstructured text analysis** where patterns vary dramatically
5. **Research paper analysis** requiring domain expertise
6. **Complex relationship extraction** between entities

### ❌ Invalid LLM Use Cases (Common Mistakes):
1. **Structured data extraction** from consistent HTML
2. **Simple pattern matching** (emails, prices, dates)
3. **Product information** from e-commerce sites
4. **News article extraction** with consistent structure
5. **Contact information** and basic entity extraction
6. **Table data** and form information

### 💡 Decision Framework:
```python
def should_use_llm(extraction_task):
    # Ask these questions in order:
    questions = [
        "Can I identify repeating HTML patterns?",  # No → Consider LLM
        "Am I extracting simple data types?",      # Yes → Use Regex
        "Does the structure vary dramatically?",   # No → Use CSS/XPath
        "Do I need semantic understanding?",       # Yes → Maybe LLM
        "Have I tried generate_schema()?"          # No → Try that first
    ]
    
    # Only use LLM if:
    return (
        task_requires_semantic_reasoning(extraction_task) and
        structure_varies_dramatically(extraction_task) and
        generate_schema_failed(extraction_task)
    )
```

### 🎯 Best Practice Summary:
1. **Always start** with [extraction-no-llm.md](./extraction-no-llm.md) strategies
2. **Try generate_schema()** before manual schema creation
3. **Use LLM sparingly** and only for semantic understanding
4. **Monitor costs** and implement budget controls
5. **Cache results** to avoid repeated LLM calls
6. **Validate quality** of LLM extractions
7. **Plan migration** from LLM to schema-based extraction

Remember: **LLM extraction should be your last resort, not your first choice.**

---

**📖 Recommended Reading Order:**
1. [extraction-no-llm.md](./extraction-no-llm.md) - Start here for 99% of use cases
2. This document - Only when non-LLM strategies are insufficient

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.