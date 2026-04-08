---
identity:
  node_id: "doc:wiki/drafts/the_decision_tree_memorize_this.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

```

## Details

```
Does the page have consistent HTML structure? → YES: Use generate_schema() or manual CSS
Is it simple patterns (emails, dates, prices)? → YES: Use RegexExtractionStrategy  
Do you need semantic understanding? → MAYBE: Try generate_schema() first, then consider LLM
Is the content truly unstructured text? → ONLY THEN: Consider LLM
```

**Cost Analysis**: 
- Non-LLM: ~$0.000001 per page
- LLM: ~$0.01-$0.10 per page (10,000x more expensive)

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.