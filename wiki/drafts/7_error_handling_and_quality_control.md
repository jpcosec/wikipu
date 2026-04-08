---
identity:
  node_id: "doc:wiki/drafts/7_error_handling_and_quality_control.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Validation and Retry Logic

## Details

### Validation and Retry Logic

```python
async def robust_llm_extraction():
    """Implement validation and retry for LLM extraction"""
    
    max_retries = 3
    strategies = [
        # Try cheap model first
        LLMExtractionStrategy(
            llm_config=LLMConfig(provider="openai/gpt-4o-mini", api_token="env:OPENAI_API_KEY"),
            schema=YourModel.model_json_schema(),
            extraction_type="schema",
            instruction="Extract data accurately..."
        ),
        # Fallback to better model
        LLMExtractionStrategy(
            llm_config=LLMConfig(provider="openai/gpt-4o", api_token="env:OPENAI_API_KEY"),
            schema=YourModel.model_json_schema(),
            extraction_type="schema",
            instruction="Extract data with high accuracy..."
        )
    ]
    
    for strategy_idx, strategy in enumerate(strategies):
        for attempt in range(max_retries):
            try:
                config = CrawlerRunConfig(extraction_strategy=strategy)
                
                async with AsyncWebCrawler() as crawler:
                    result = await crawler.arun(url="https://example.com", config=config)
                    
                    if result.success and result.extracted_content:
                        data = json.loads(result.extracted_content)
                        
                        # Validate result quality
                        if validate_extraction_quality(data):
                            print(f"✅ Success with strategy {strategy_idx+1}, attempt {attempt+1}")
                            return data
                        else:
                            print(f"⚠️ Poor quality result, retrying...")
                            continue
                    
            except Exception as e:
                print(f"❌ Attempt {attempt+1} failed: {e}")
                if attempt == max_retries - 1:
                    print(f"❌ Strategy {strategy_idx+1} failed completely")
    
    print("❌ All strategies and retries failed")
    return None

def validate_extraction_quality(data):
    """Validate that LLM extraction meets quality standards"""
    if not data or not isinstance(data, (list, dict)):
        return False
    
    # Check for common LLM extraction issues
    if isinstance(data, list):
        if len(data) == 0:
            return False
        
        # Check if all items have required fields
        for item in data:
            if not isinstance(item, dict) or len(item) < 2:
                return False
    
    return True

# Robust extraction with validation
result = await robust_llm_extraction()
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.