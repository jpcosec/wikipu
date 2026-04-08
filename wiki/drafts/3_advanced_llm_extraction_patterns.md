---
identity:
  node_id: "doc:wiki/drafts/3_advanced_llm_extraction_patterns.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Block-Based Extraction (Unstructured Content)

## Details

### Block-Based Extraction (Unstructured Content)

```python
# When structure is too varied for schemas
block_strategy = LLMExtractionStrategy(
    llm_config=cheap_config,
    extraction_type="block",  # Extract free-form content blocks
    instruction="""
    Extract meaningful content blocks from this page.
    Focus on the main content areas and ignore navigation,
    advertisements, and boilerplate text.
    """,
    apply_chunking=True,
    chunk_token_threshold=1200,
    input_format="fit_markdown"  # Use cleaned content
)

async def extract_content_blocks():
    config = CrawlerRunConfig(
        extraction_strategy=block_strategy,
        word_count_threshold=50,  # Filter short content
        excluded_tags=['nav', 'footer', 'aside', 'advertisement']
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/article",
            config=config
        )
        
        if result.success:
            blocks = json.loads(result.extracted_content)
            for block in blocks:
                print(f"Block: {block['content'][:100]}...")
```

### Chunked Processing for Large Content

```python
# Handle large documents efficiently
large_content_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(
        provider="openai/gpt-4o-mini",
        api_token="env:OPENAI_API_KEY"
    ),
    schema=YourModel.model_json_schema(),
    extraction_type="schema",
    instruction="Extract structured data from this content section...",
    
    # Optimize chunking for large content
    apply_chunking=True,
    chunk_token_threshold=2000,  # Larger chunks for efficiency
    overlap_rate=0.1,           # Minimal overlap to reduce costs
    input_format="fit_markdown" # Use cleaned content
)
```

### Multi-Model Validation

```python
# Use multiple models for critical extractions
async def multi_model_extraction():
    """Use multiple LLMs for validation of critical data"""
    
    models = [
        LLMConfig(provider="openai/gpt-4o-mini", api_token="env:OPENAI_API_KEY"),
        LLMConfig(provider="anthropic/claude-3-5-sonnet", api_token="env:ANTHROPIC_API_KEY"),
        LLMConfig(provider="ollama/llama3.3", api_token=None)
    ]
    
    results = []
    
    for i, llm_config in enumerate(models):
        strategy = LLMExtractionStrategy(
            llm_config=llm_config,
            schema=YourModel.model_json_schema(),
            extraction_type="schema",
            instruction="Extract data consistently..."
        )
        
        config = CrawlerRunConfig(extraction_strategy=strategy)
        
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url="https://example.com", config=config)
            if result.success:
                data = json.loads(result.extracted_content)
                results.append(data)
                print(f"Model {i+1} extracted {len(data)} items")
    
    # Compare results for consistency
    if len(set(str(r) for r in results)) == 1:
        print("✅ All models agree")
        return results[0]
    else:
        print("⚠️ Models disagree - manual review needed")
        return results

# Use for critical business data only
critical_result = await multi_model_extraction()
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.