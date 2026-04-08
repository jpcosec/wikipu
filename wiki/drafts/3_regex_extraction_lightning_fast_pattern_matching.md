---
identity:
  node_id: "doc:wiki/drafts/3_regex_extraction_lightning_fast_pattern_matching.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

**Use this for**: Simple data types like emails, phones, URLs, prices, dates.

## Details

**Use this for**: Simple data types like emails, phones, URLs, prices, dates.

### Built-in Patterns (Fastest Option)

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai import RegexExtractionStrategy

async def extract_common_patterns():
    # Use built-in patterns for common data types
    strategy = RegexExtractionStrategy(
        pattern=(
            RegexExtractionStrategy.Email |
            RegexExtractionStrategy.PhoneUS |
            RegexExtractionStrategy.Url |
            RegexExtractionStrategy.Currency |
            RegexExtractionStrategy.DateIso
        )
    )
    
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/contact",
            config=config
        )
        
        if result.success:
            matches = json.loads(result.extracted_content)
            
            # Group by pattern type
            by_type = {}
            for match in matches:
                label = match['label']
                if label not in by_type:
                    by_type[label] = []
                by_type[label].append(match['value'])
            
            for pattern_type, values in by_type.items():
                print(f"{pattern_type}: {len(values)} matches")
                for value in values[:3]:
                    print(f"  {value}")

asyncio.run(extract_common_patterns())
```

### Available Built-in Patterns

```python
# Individual patterns
RegexExtractionStrategy.Email          # Email addresses
RegexExtractionStrategy.PhoneUS        # US phone numbers 
RegexExtractionStrategy.PhoneIntl      # International phones
RegexExtractionStrategy.Url            # HTTP/HTTPS URLs
RegexExtractionStrategy.Currency       # Currency values ($99.99)
RegexExtractionStrategy.Percentage     # Percentage values (25%)
RegexExtractionStrategy.DateIso        # ISO dates (2024-01-01)
RegexExtractionStrategy.DateUS         # US dates (01/01/2024)
RegexExtractionStrategy.IPv4           # IP addresses
RegexExtractionStrategy.CreditCard     # Credit card numbers
RegexExtractionStrategy.TwitterHandle  # @username
RegexExtractionStrategy.Hashtag        # #hashtag

# Use all patterns
RegexExtractionStrategy.All
```

### Custom Patterns

```python
# Custom patterns for specific data types
async def extract_custom_patterns():
    custom_patterns = {
        "product_sku": r"SKU[-:]?\s*([A-Z0-9]{4,12})",
        "discount": r"(\d{1,2})%\s*off",
        "model_number": r"Model\s*#?\s*([A-Z0-9-]+)",
        "isbn": r"ISBN[-:]?\s*(\d{10}|\d{13})",
        "stock_ticker": r"\$([A-Z]{2,5})",
        "version": r"v(\d+\.\d+(?:\.\d+)?)"
    }
    
    strategy = RegexExtractionStrategy(custom=custom_patterns)
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            config=config
        )
        
        if result.success:
            data = json.loads(result.extracted_content)
            for item in data:
                print(f"{item['label']}: {item['value']}")

asyncio.run(extract_custom_patterns())
```

### LLM-Generated Patterns (One-Time Cost)

```python
async def generate_optimized_regex():
    """
    Use LLM ONCE to generate optimized regex patterns
    Then use them unlimited times with zero LLM calls
    """
    cache_file = Path("./patterns/price_patterns.json")
    
    if cache_file.exists():
        # Load cached patterns - NO LLM CALLS
        patterns = json.load(cache_file.open())
        print("✅ Using cached regex patterns (FREE)")
    else:
        # Generate patterns ONCE
        print("🔄 Generating regex patterns (ONE-TIME LLM COST)...")
        
        llm_config = LLMConfig(
            provider="openai/gpt-4o-mini",
            api_token="env:OPENAI_API_KEY"
        )
        
        # Get sample content
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun("https://example.com/pricing")
            sample_html = result.cleaned_html
        
        # Generate optimized patterns
        patterns = RegexExtractionStrategy.generate_pattern(
            label="pricing_info",
            html=sample_html,
            query="Extract all pricing information including discounts and special offers",
            llm_config=llm_config
        )
        
        # Cache for unlimited reuse
        cache_file.parent.mkdir(exist_ok=True)
        json.dump(patterns, cache_file.open("w"), indent=2)
        print("✅ Patterns generated and cached")
    
    # Use cached patterns (NO MORE LLM CALLS)
    strategy = RegexExtractionStrategy(custom=patterns)
    return strategy

# Use generated patterns for unlimited extractions
strategy = await generate_optimized_regex()
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.