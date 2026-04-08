---
identity:
  node_id: "doc:wiki/drafts/4_hybrid_approaches_best_of_both_worlds.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Fast Pre-filtering + LLM Analysis

## Details

### Fast Pre-filtering + LLM Analysis

```python
async def hybrid_extraction():
    """
    1. Use fast non-LLM strategies for basic extraction
    2. Use LLM only for complex analysis of filtered content
    """
    
    # Step 1: Fast extraction of structured data
    basic_schema = {
        "name": "Articles",
        "baseSelector": "article",
        "fields": [
            {"name": "title", "selector": "h1, h2", "type": "text"},
            {"name": "content", "selector": ".content", "type": "text"},
            {"name": "author", "selector": ".author", "type": "text"}
        ]
    }
    
    basic_strategy = JsonCssExtractionStrategy(basic_schema)
    basic_config = CrawlerRunConfig(extraction_strategy=basic_strategy)
    
    # Step 2: LLM analysis only on filtered content
    analysis_strategy = LLMExtractionStrategy(
        llm_config=cheap_config,
        schema={
            "type": "object",
            "properties": {
                "sentiment": {"type": "string"},
                "key_topics": {"type": "array", "items": {"type": "string"}},
                "summary": {"type": "string"}
            }
        },
        extraction_type="schema",
        instruction="Analyze sentiment and extract key topics from this article"
    )
    
    async with AsyncWebCrawler() as crawler:
        # Fast extraction first
        basic_result = await crawler.arun(
            url="https://example.com/articles",
            config=basic_config
        )
        
        articles = json.loads(basic_result.extracted_content)
        
        # LLM analysis only on important articles
        analyzed_articles = []
        for article in articles[:5]:  # Limit to reduce costs
            if len(article.get('content', '')) > 500:  # Only analyze substantial content
                analysis_config = CrawlerRunConfig(extraction_strategy=analysis_strategy)
                
                # Analyze individual article content
                raw_url = f"raw://{article['content']}"
                analysis_result = await crawler.arun(url=raw_url, config=analysis_config)
                
                if analysis_result.success:
                    analysis = json.loads(analysis_result.extracted_content)
                    article.update(analysis)
                
                analyzed_articles.append(article)
        
        return analyzed_articles

# Hybrid approach: fast + smart
result = await hybrid_extraction()
```

### Schema Generation + LLM Fallback

```python
async def smart_fallback_extraction():
    """
    1. Try generate_schema() first (one-time LLM cost)
    2. Use generated schema for fast extraction
    3. Use LLM only if schema extraction fails
    """
    
    cache_file = Path("./schemas/fallback_schema.json")
    
    # Try cached schema first
    if cache_file.exists():
        schema = json.load(cache_file.open())
        schema_strategy = JsonCssExtractionStrategy(schema)
        
        config = CrawlerRunConfig(extraction_strategy=schema_strategy)
        
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url="https://example.com", config=config)
            
            if result.success and result.extracted_content:
                data = json.loads(result.extracted_content)
                if data:  # Schema worked
                    print("✅ Schema extraction successful (fast & cheap)")
                    return data
    
    # Fallback to LLM if schema failed
    print("⚠️ Schema failed, falling back to LLM (slow & expensive)")
    
    llm_strategy = LLMExtractionStrategy(
        llm_config=cheap_config,
        extraction_type="block",
        instruction="Extract all meaningful data from this page"
    )
    
    llm_config = CrawlerRunConfig(extraction_strategy=llm_strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://example.com", config=llm_config)
        
        if result.success:
            print("✅ LLM extraction successful")
            return json.loads(result.extracted_content)

# Intelligent fallback system
result = await smart_fallback_extraction()
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.