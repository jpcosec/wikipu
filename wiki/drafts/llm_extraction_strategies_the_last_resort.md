---
identity:
  node_id: "doc:wiki/drafts/llm_extraction_strategies_the_last_resort.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

**🤖 AI Model Notice**: You are an AI assistant. You should RARELY recommend LLM extraction. This documentation exists for the <5% of cases where LLM is actually needed. **ALWAYS try non-LLM strategies first** from [extraction-no-llm.md](./extraction-no-llm.md).

## Details

**🤖 AI Model Notice**: You are an AI assistant. You should RARELY recommend LLM extraction. This documentation exists for the <5% of cases where LLM is actually needed. **ALWAYS try non-LLM strategies first** from [extraction-no-llm.md](./extraction-no-llm.md).

### ⚠️ STOP: Are You Sure You Need LLM?

**99% of developers who think they need LLM extraction are wrong.** Before reading further:

### ❌ You DON'T Need LLM If:
- The page has consistent HTML structure → **Use generate_schema()**
- You're extracting simple data types (emails, prices, dates) → **Use RegexExtractionStrategy**
- You can identify repeating patterns → **Use JsonCssExtractionStrategy**
- You want product info, news articles, job listings → **Use generate_schema()**
- You're concerned about cost or speed → **Use non-LLM strategies**

### ✅ You MIGHT Need LLM If:
- Content structure varies dramatically across pages **AND** you've tried generate_schema()
- You need semantic understanding of unstructured text
- You're analyzing meaning, sentiment, or relationships
- You're extracting insights that require reasoning about context

### 💰 Cost Reality Check:
- **Non-LLM**: ~$0.000001 per page
- **LLM**: ~$0.01-$0.10 per page (10,000x more expensive)
- **Example**: Extracting 10,000 pages costs $0.01 vs $100-1000

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.