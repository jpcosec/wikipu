---
identity:
  node_id: "doc:wiki/drafts/table_extraction.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

Extract structured data from HTML tables with automatic detection and scoring.

## Details

Extract structured data from HTML tables with automatic detection and scoring.

### Basic Table Extraction

```python
import asyncio
import pandas as pd
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

async def extract_tables():
    async with AsyncWebCrawler() as crawler:
        config = CrawlerRunConfig(
            table_score_threshold=7,  # Higher = stricter detection
            cache_mode=CacheMode.BYPASS
        )
        
        result = await crawler.arun("https://example.com/tables", config=config)
        
        if result.success and result.tables:
            # New tables field (v0.6+)
            for i, table in enumerate(result.tables):
                print(f"Table {i+1}:")
                print(f"Headers: {table['headers']}")
                print(f"Rows: {len(table['rows'])}")
                print(f"Caption: {table.get('caption', 'No caption')}")
                
                # Convert to DataFrame
                df = pd.DataFrame(table['rows'], columns=table['headers'])
                print(df.head())

asyncio.run(extract_tables())
```

### Advanced Table Processing

```python
from crawl4ai import LXMLWebScrapingStrategy

async def process_financial_tables():
    config = CrawlerRunConfig(
        table_score_threshold=8,  # Strict detection for data tables
        scraping_strategy=LXMLWebScrapingStrategy(),
        keep_data_attributes=True,
        scan_full_page=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://coinmarketcap.com", config=config)
        
        if result.tables:
            # Get the main data table (usually first/largest)
            main_table = result.tables[0]
            
            # Create DataFrame
            df = pd.DataFrame(
                main_table['rows'],
                columns=main_table['headers']
            )
            
            # Clean and process data
            df = clean_financial_data(df)
            
            # Save for analysis
            df.to_csv("market_data.csv", index=False)
            return df

def clean_financial_data(df):
    """Clean currency symbols, percentages, and large numbers"""
    for col in df.columns:
        if 'price' in col.lower():
            # Remove currency symbols
            df[col] = df[col].str.replace(r'[^\d.]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        elif '%' in str(df[col].iloc[0]):
            # Convert percentages
            df[col] = df[col].str.replace('%', '').astype(float) / 100
        
        elif any(suffix in str(df[col].iloc[0]) for suffix in ['B', 'M', 'K']):
            # Handle large numbers (Billions, Millions, etc.)
            df[col] = df[col].apply(convert_large_numbers)
    
    return df

def convert_large_numbers(value):
    """Convert 1.5B -> 1500000000"""
    if pd.isna(value):
        return float('nan')
    
    value = str(value)
    multiplier = 1
    if 'B' in value:
        multiplier = 1e9
    elif 'M' in value:
        multiplier = 1e6
    elif 'K' in value:
        multiplier = 1e3
    
    number = float(re.sub(r'[^\d.]', '', value))
    return number * multiplier
```

### Table Detection Configuration

```python
# Strict table detection (data-heavy pages)
strict_config = CrawlerRunConfig(
    table_score_threshold=9,  # Only high-quality tables
    word_count_threshold=5,   # Ignore sparse content
    excluded_tags=['nav', 'footer']  # Skip navigation tables
)

# Lenient detection (mixed content pages)
lenient_config = CrawlerRunConfig(
    table_score_threshold=5,  # Include layout tables
    process_iframes=True,     # Check embedded tables
    scan_full_page=True      # Scroll to load dynamic tables
)

# Financial/data site optimization
financial_config = CrawlerRunConfig(
    table_score_threshold=8,
    scraping_strategy=LXMLWebScrapingStrategy(),
    wait_for="css:table",     # Wait for tables to load
    scan_full_page=True,
    scroll_delay=0.2
)
```

### Multi-Table Processing

```python
async def extract_all_tables():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/data", config=config)
        
        tables_data = {}
        
        for i, table in enumerate(result.tables):
            # Create meaningful names based on content
            table_name = (
                table.get('caption') or 
                f"table_{i+1}_{table['headers'][0]}"
            ).replace(' ', '_').lower()
            
            df = pd.DataFrame(table['rows'], columns=table['headers'])
            
            # Store with metadata
            tables_data[table_name] = {
                'dataframe': df,
                'headers': table['headers'],
                'row_count': len(table['rows']),
                'caption': table.get('caption'),
                'summary': table.get('summary')
            }
        
        return tables_data

# Usage
tables = await extract_all_tables()
for name, data in tables.items():
    print(f"{name}: {data['row_count']} rows")
    data['dataframe'].to_csv(f"{name}.csv")
```

### Backward Compatibility

```python
# Support both new and old table formats
def get_tables(result):
    # New format (v0.6+)
    if hasattr(result, 'tables') and result.tables:
        return result.tables
    
    # Fallback to media.tables (older versions)
    return result.media.get('tables', [])

# Usage in existing code
result = await crawler.arun(url, config=config)
tables = get_tables(result)

for table in tables:
    df = pd.DataFrame(table['rows'], columns=table['headers'])
    # Process table data...
```

### Table Quality Scoring

```python
# Understanding table_score_threshold values:
# 10: Only perfect data tables (headers + data rows)
# 8-9: High-quality tables (recommended for financial/data sites)
# 6-7: Mixed content tables (news sites, wikis)
# 4-5: Layout tables included (broader detection)
# 1-3: All table-like structures (very permissive)

config = CrawlerRunConfig(
    table_score_threshold=8,  # Balanced detection
    verbose=True  # See scoring details in logs
)
```


**📖 Learn more:** [CrawlResult API Reference](https://docs.crawl4ai.com/api/crawl-result/), [Browser & Crawler Configuration](https://docs.crawl4ai.com/core/browser-crawler-config/), [Cache Modes](https://docs.crawl4ai.com/core/cache-modes/)

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.