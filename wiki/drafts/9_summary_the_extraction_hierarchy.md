---
identity:
  node_id: "doc:wiki/drafts/9_summary_the_extraction_hierarchy.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

1. **🥇 FIRST CHOICE**: `generate_schema()` - AI generates pattern once, use unlimited times

## Details

1. **🥇 FIRST CHOICE**: `generate_schema()` - AI generates pattern once, use unlimited times
2. **🥈 SECOND CHOICE**: Manual CSS/XPath - Full control, maximum speed
3. **🥉 THIRD CHOICE**: Regex patterns - Simple data types, lightning fast
4. **🏴 LAST RESORT**: LLM extraction - Only for semantic reasoning

**Remember**: 99% of web data is structured. You almost never need LLM for extraction. Save LLM for analysis, not extraction.

**Performance**: Non-LLM strategies are 100-1000x faster and 10,000x cheaper than LLM extraction.

---

**📖 Next**: If you absolutely must use LLM extraction, see [extraction-llm.md](./extraction-llm.md) for guidance on the rare cases where it's justified.

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.