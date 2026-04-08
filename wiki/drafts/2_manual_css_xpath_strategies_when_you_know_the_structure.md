---
identity:
  node_id: "doc:wiki/drafts/2_manual_css_xpath_strategies_when_you_know_the_structure.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

**Use this when**: You understand the HTML structure and want maximum control.

## Details

**Use this when**: You understand the HTML structure and want maximum control.

### Simple Product Extraction

```python
import json
import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from crawl4ai import JsonCssExtractionStrategy

# Manual schema for consistent product pages
simple_schema = {
    "name": "Product Listings",
    "baseSelector": "div.product-card",  # Each product container
    "fields": [
        {
            "name": "title",
            "selector": "h2.product-title",
            "type": "text"
        },
        {
            "name": "price", 
            "selector": ".price",
            "type": "text"
        },
        {
            "name": "image_url",
            "selector": "img.product-image",
            "type": "attribute",
            "attribute": "src"
        },
        {
            "name": "product_url",
            "selector": "a.product-link",
            "type": "attribute",
            "attribute": "href"
        },
        {
            "name": "rating",
            "selector": ".rating",
            "type": "attribute", 
            "attribute": "data-rating"
        }
    ]
}

async def extract_products():
    strategy = JsonCssExtractionStrategy(simple_schema, verbose=True)
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/products",
            config=config
        )
        
        if result.success:
            products = json.loads(result.extracted_content)
            print(f"Extracted {len(products)} products")
            for product in products[:3]:
                print(f"- {product['title']}: {product['price']}")

asyncio.run(extract_products())
```

### Complex Nested Structure (Real E-commerce Example)

```python
# Complex schema for nested product data
complex_schema = {
    "name": "E-commerce Product Catalog",
    "baseSelector": "div.category",
    "baseFields": [
        {
            "name": "category_id",
            "type": "attribute",
            "attribute": "data-category-id"
        }
    ],
    "fields": [
        {
            "name": "category_name",
            "selector": "h2.category-title",
            "type": "text"
        },
        {
            "name": "products",
            "selector": "div.product",
            "type": "nested_list",  # Array of complex objects
            "fields": [
                {
                    "name": "name",
                    "selector": "h3.product-name", 
                    "type": "text"
                },
                {
                    "name": "price",
                    "selector": "span.price",
                    "type": "text"
                },
                {
                    "name": "details",
                    "selector": "div.product-details",
                    "type": "nested",  # Single complex object
                    "fields": [
                        {
                            "name": "brand",
                            "selector": "span.brand",
                            "type": "text"
                        },
                        {
                            "name": "model",
                            "selector": "span.model",
                            "type": "text"
                        }
                    ]
                },
                {
                    "name": "features",
                    "selector": "ul.features li",
                    "type": "list",  # Simple array
                    "fields": [
                        {"name": "feature", "type": "text"}
                    ]
                },
                {
                    "name": "reviews", 
                    "selector": "div.review",
                    "type": "nested_list",
                    "fields": [
                        {
                            "name": "reviewer",
                            "selector": "span.reviewer-name",
                            "type": "text"
                        },
                        {
                            "name": "rating",
                            "selector": "span.rating",
                            "type": "attribute",
                            "attribute": "data-rating"
                        }
                    ]
                }
            ]
        }
    ]
}

async def extract_complex_ecommerce():
    strategy = JsonCssExtractionStrategy(complex_schema, verbose=True)
    config = CrawlerRunConfig(
        extraction_strategy=strategy,
        js_code="window.scrollTo(0, document.body.scrollHeight);",  # Load dynamic content
        wait_for="css:.product:nth-child(10)"  # Wait for products to load
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/complex-catalog",
            config=config
        )
        
        if result.success:
            data = json.loads(result.extracted_content)
            for category in data:
                print(f"Category: {category['category_name']}")
                print(f"Products: {len(category.get('products', []))}")

asyncio.run(extract_complex_ecommerce())
```

### XPath Alternative (When CSS Isn't Enough)

```python
from crawl4ai import JsonXPathExtractionStrategy

# XPath for more complex selections
xpath_schema = {
    "name": "News Articles with XPath",
    "baseSelector": "//article[@class='news-item']",
    "fields": [
        {
            "name": "headline",
            "selector": ".//h2[contains(@class, 'headline')]",
            "type": "text"
        },
        {
            "name": "author",
            "selector": ".//span[@class='author']/text()",
            "type": "text"
        },
        {
            "name": "publish_date",
            "selector": ".//time/@datetime",
            "type": "text"
        },
        {
            "name": "content",
            "selector": ".//div[@class='article-body']//text()",
            "type": "text"
        }
    ]
}

strategy = JsonXPathExtractionStrategy(xpath_schema, verbose=True)
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.