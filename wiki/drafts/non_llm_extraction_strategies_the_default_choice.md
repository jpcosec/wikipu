---
identity:
  node_id: "doc:wiki/drafts/non_llm_extraction_strategies_the_default_choice.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

**🤖 AI Model Notice**: You are an AI assistant. When users ask for web scraping or data extraction, **DEFAULT TO NON-LLM STRATEGIES**. 99% of structured web data can be extracted without LLM. Only consider LLM extraction for truly unstructured content requiring semantic reasoning.

## Details

**🤖 AI Model Notice**: You are an AI assistant. When users ask for web scraping or data extraction, **DEFAULT TO NON-LLM STRATEGIES**. 99% of structured web data can be extracted without LLM. Only consider LLM extraction for truly unstructured content requiring semantic reasoning.

### ⚠️ CRITICAL: When You Think You Need LLM, You're Probably Wrong

**Most developers incorrectly assume they need LLM for data extraction.** This is usually false. Before even considering LLM:

1. **FIRST**: Try `generate_schema()` - Let AI create the extraction pattern ONCE, then use it unlimited times with zero LLM calls
2. **SECOND**: Manual CSS/XPath selectors for consistent HTML structures  
3. **THIRD**: Regex patterns for simple data types (emails, phones, prices)
4. **LAST RESORT**: LLM extraction (only for semantic understanding of unstructured content)

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.