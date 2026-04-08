---
identity:
  node_id: "doc:wiki/drafts/8_migration_from_llm_to_non_llm.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Pattern Analysis for Schema Generation

## Details

### Pattern Analysis for Schema Generation

```python
async def analyze_llm_results_for_schema():
    """
    Analyze LLM extraction results to create non-LLM schemas
    Use this to transition from expensive LLM to cheap schema extraction
    """
    
    # Step 1: Use LLM on sample pages to understand structure
    llm_strategy = LLMExtractionStrategy(
        llm_config=cheap_config,
        extraction_type="block",
        instruction="Extract all structured data from this page"
    )
    
    sample_urls = ["https://example.com/page1", "https://example.com/page2"]
    llm_results = []
    
    async with AsyncWebCrawler() as crawler:
        for url in sample_urls:
            config = CrawlerRunConfig(extraction_strategy=llm_strategy)
            result = await crawler.arun(url=url, config=config)
            
            if result.success:
                llm_results.append({
                    "url": url,
                    "html": result.cleaned_html,
                    "extracted": json.loads(result.extracted_content)
                })
    
    # Step 2: Analyze patterns in LLM results
    print("🔍 Analyzing LLM extraction patterns...")
    
    # Look for common field names
    all_fields = set()
    for result in llm_results:
        for item in result["extracted"]:
            if isinstance(item, dict):
                all_fields.update(item.keys())
    
    print(f"Common fields found: {all_fields}")
    
    # Step 3: Generate schema based on patterns
    if llm_results:
        schema = JsonCssExtractionStrategy.generate_schema(
            html=llm_results[0]["html"],
            target_json_example=json.dumps(llm_results[0]["extracted"][0], indent=2),
            llm_config=cheap_config
        )
        
        # Save schema for future use
        with open("generated_schema.json", "w") as f:
            json.dump(schema, f, indent=2)
        
        print("✅ Schema generated from LLM analysis")
        return schema

# Generate schema from LLM patterns, then use schema for all future extractions
schema = await analyze_llm_results_for_schema()
fast_strategy = JsonCssExtractionStrategy(schema)
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.