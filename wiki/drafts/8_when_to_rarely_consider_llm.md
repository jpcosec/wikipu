---
identity:
  node_id: "doc:wiki/drafts/8_when_to_rarely_consider_llm.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

**⚠️ WARNING: Before considering LLM, ask yourself:**

## Details

**⚠️ WARNING: Before considering LLM, ask yourself:**

1. "Can I identify repeating HTML patterns?" → Use CSS/XPath schema
2. "Am I extracting simple data types?" → Use Regex patterns  
3. "Can I provide a JSON example of what I want?" → Use generate_schema()
4. "Is this truly unstructured text requiring semantic understanding?" → Maybe LLM

**Only use LLM extraction for:**
- Unstructured prose that needs semantic analysis
- Content where structure varies dramatically across pages
- When you need AI reasoning about context/meaning

**Cost reminder**: LLM extraction costs 10,000x more than schema-based extraction.

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.