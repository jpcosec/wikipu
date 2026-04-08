---
identity:
  node_id: "doc:wiki/drafts/6_error_handling_and_validation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

```python

## Details

```python
async def robust_extraction():
    """
    Implement fallback strategies for reliable extraction
    """
    strategies = [
        # Try fast regex first
        RegexExtractionStrategy(pattern=RegexExtractionStrategy.Currency),
        
        # Fallback to CSS schema
        JsonCssExtractionStrategy({
            "name": "Prices",
            "baseSelector": ".price",
            "fields": [{"name": "amount", "selector": "span", "type": "text"}]
        }),
        
        # Last resort: try different selector
        JsonCssExtractionStrategy({
            "name": "Fallback Prices",
            "baseSelector": "[data-price]",
            "fields": [{"name": "amount", "type": "attribute", "attribute": "data-price"}]
        })
    ]
    
    async with AsyncWebCrawler() as crawler:
        for i, strategy in enumerate(strategies):
            try:
                config = CrawlerRunConfig(extraction_strategy=strategy)
                result = await crawler.arun(url="https://example.com", config=config)
                
                if result.success and result.extracted_content:
                    data = json.loads(result.extracted_content)
                    if data:  # Validate non-empty results
                        print(f"✅ Success with strategy {i+1}: {strategy.__class__.__name__}")
                        return data
                        
            except Exception as e:
                print(f"❌ Strategy {i+1} failed: {e}")
                continue
    
    print("❌ All strategies failed")
    return None

# Validate extracted data
def validate_extraction(data, required_fields):
    """Validate that extraction contains expected fields"""
    if not data or not isinstance(data, list):
        return False
    
    for item in data:
        for field in required_fields:
            if field not in item or not item[field]:
                return False
    return True

# Usage
result = await robust_extraction()
if validate_extraction(result, ["amount"]):
    print("✅ Extraction validated")
else:
    print("❌ Validation failed")
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.