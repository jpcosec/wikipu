---
identity:
  node_id: "doc:wiki/drafts/6_performance_optimization_for_llm_extraction.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Batch Processing

## Details

### Batch Processing

```python
async def batch_llm_extraction():
    """Process multiple pages efficiently"""
    
    # Collect content first (fast)
    urls = ["https://example.com/page1", "https://example.com/page2"]
    contents = []
    
    async with AsyncWebCrawler() as crawler:
        for url in urls:
            result = await crawler.arun(url=url)
            if result.success:
                contents.append({
                    "url": url,
                    "content": result.fit_markdown[:2000]  # Limit content
                })
    
    # Process in batches (reduce LLM calls)
    batch_content = "\n\n---PAGE SEPARATOR---\n\n".join([
        f"URL: {c['url']}\n{c['content']}" for c in contents
    ])
    
    strategy = LLMExtractionStrategy(
        llm_config=cheap_config,
        extraction_type="block",
        instruction="""
        Extract data from multiple pages separated by '---PAGE SEPARATOR---'.
        Return results for each page in order.
        """,
        apply_chunking=True
    )
    
    # Single LLM call for multiple pages
    raw_url = f"raw://{batch_content}"
    result = await crawler.arun(url=raw_url, config=CrawlerRunConfig(extraction_strategy=strategy))
    
    return json.loads(result.extracted_content)

# Batch processing reduces LLM calls
batch_results = await batch_llm_extraction()
```

### Caching LLM Results

```python
import hashlib
from pathlib import Path

class LLMResultCache:
    def __init__(self, cache_dir="./llm_cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
    
    def get_cache_key(self, url, instruction, schema):
        """Generate cache key from extraction parameters"""
        content = f"{url}:{instruction}:{str(schema)}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def get_cached_result(self, cache_key):
        """Get cached result if available"""
        cache_file = self.cache_dir / f"{cache_key}.json"
        if cache_file.exists():
            return json.load(cache_file.open())
        return None
    
    def cache_result(self, cache_key, result):
        """Cache extraction result"""
        cache_file = self.cache_dir / f"{cache_key}.json"
        json.dump(result, cache_file.open("w"), indent=2)

cache = LLMResultCache()

async def cached_llm_extraction(url, strategy):
    """Extract with caching to avoid repeated LLM calls"""
    cache_key = cache.get_cache_key(
        url, 
        strategy.instruction,
        str(strategy.schema)
    )
    
    # Check cache first
    cached_result = cache.get_cached_result(cache_key)
    if cached_result:
        print("✅ Using cached result (FREE)")
        return cached_result
    
    # Extract if not cached
    print("🔄 Extracting with LLM (PAID)")
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url, config=config)
        
        if result.success:
            data = json.loads(result.extracted_content)
            cache.cache_result(cache_key, data)
            return data

# Cached extraction avoids repeated costs
result = await cached_llm_extraction(url, strategy)
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.