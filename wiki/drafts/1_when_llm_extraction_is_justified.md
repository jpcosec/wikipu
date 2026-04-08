---
identity:
  node_id: "doc:wiki/drafts/1_when_llm_extraction_is_justified.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Scenario 1: Truly Unstructured Content Analysis

## Details

### Scenario 1: Truly Unstructured Content Analysis

```python
# Example: Analyzing customer feedback for sentiment and themes
import asyncio
import json
from pydantic import BaseModel, Field
from typing import List
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, LLMConfig
from crawl4ai import LLMExtractionStrategy

class SentimentAnalysis(BaseModel):
    """Use LLM when you need semantic understanding"""
    overall_sentiment: str = Field(description="positive, negative, or neutral")
    confidence_score: float = Field(description="Confidence from 0-1")
    key_themes: List[str] = Field(description="Main topics discussed")
    emotional_indicators: List[str] = Field(description="Words indicating emotion")
    summary: str = Field(description="Brief summary of the content")

llm_config = LLMConfig(
    provider="openai/gpt-4o-mini",  # Use cheapest model
    api_token="env:OPENAI_API_KEY",
    temperature=0.1,  # Low temperature for consistency
    max_tokens=1000
)

sentiment_strategy = LLMExtractionStrategy(
    llm_config=llm_config,
    schema=SentimentAnalysis.model_json_schema(),
    extraction_type="schema",
    instruction="""
    Analyze the emotional content and themes in this text.
    Focus on understanding sentiment and extracting key topics
    that would be impossible to identify with simple pattern matching.
    """,
    apply_chunking=True,
    chunk_token_threshold=1500
)

async def analyze_sentiment():
    config = CrawlerRunConfig(
        extraction_strategy=sentiment_strategy,
        cache_mode=CacheMode.BYPASS
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://example.com/customer-reviews",
            config=config
        )
        
        if result.success:
            analysis = json.loads(result.extracted_content)
            print(f"Sentiment: {analysis['overall_sentiment']}")
            print(f"Themes: {analysis['key_themes']}")

asyncio.run(analyze_sentiment())
```

### Scenario 2: Complex Knowledge Extraction

```python
# Example: Building knowledge graphs from unstructured content
class Entity(BaseModel):
    name: str = Field(description="Entity name")
    type: str = Field(description="person, organization, location, concept")
    description: str = Field(description="Brief description")

class Relationship(BaseModel):
    source: str = Field(description="Source entity")
    target: str = Field(description="Target entity") 
    relationship: str = Field(description="Type of relationship")
    confidence: float = Field(description="Confidence score 0-1")

class KnowledgeGraph(BaseModel):
    entities: List[Entity] = Field(description="All entities found")
    relationships: List[Relationship] = Field(description="Relationships between entities")
    main_topic: str = Field(description="Primary topic of the content")

knowledge_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(
        provider="anthropic/claude-3-5-sonnet-20240620",  # Better for complex reasoning
        api_token="env:ANTHROPIC_API_KEY",
        max_tokens=4000
    ),
    schema=KnowledgeGraph.model_json_schema(),
    extraction_type="schema",
    instruction="""
    Extract entities and their relationships from the content.
    Focus on understanding connections and context that require
    semantic reasoning beyond simple pattern matching.
    """,
    input_format="html",  # Preserve structure
    apply_chunking=True
)
```

### Scenario 3: Content Summarization and Insights

```python
# Example: Research paper analysis
class ResearchInsights(BaseModel):
    title: str = Field(description="Paper title")
    abstract_summary: str = Field(description="Summary of abstract")
    key_findings: List[str] = Field(description="Main research findings")
    methodology: str = Field(description="Research methodology used")
    limitations: List[str] = Field(description="Study limitations")
    practical_applications: List[str] = Field(description="Real-world applications")
    citations_count: int = Field(description="Number of citations", default=0)

research_strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(
        provider="openai/gpt-4o",  # Use powerful model for complex analysis
        api_token="env:OPENAI_API_KEY",
        temperature=0.2,
        max_tokens=2000
    ),
    schema=ResearchInsights.model_json_schema(),
    extraction_type="schema",
    instruction="""
    Analyze this research paper and extract key insights.
    Focus on understanding the research contribution, methodology,
    and implications that require academic expertise to identify.
    """,
    apply_chunking=True,
    chunk_token_threshold=2000,
    overlap_rate=0.15  # More overlap for academic content
)
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.