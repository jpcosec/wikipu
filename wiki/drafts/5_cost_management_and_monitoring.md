---
identity:
  node_id: "doc:wiki/drafts/5_cost_management_and_monitoring.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Token Usage Tracking

## Details

### Token Usage Tracking

```python
class ExtractionCostTracker:
    def __init__(self):
        self.total_cost = 0.0
        self.total_tokens = 0
        self.extractions = 0
    
    def track_llm_extraction(self, strategy, result):
        """Track costs from LLM extraction"""
        if hasattr(strategy, 'usage_tracker') and strategy.usage_tracker:
            usage = strategy.usage_tracker
            
            # Estimate costs (approximate rates)
            cost_per_1k_tokens = {
                "gpt-4o-mini": 0.0015,
                "gpt-4o": 0.03,
                "claude-3-5-sonnet": 0.015,
                "ollama": 0.0  # Self-hosted
            }
            
            provider = strategy.llm_config.provider.split('/')[1]
            rate = cost_per_1k_tokens.get(provider, 0.01)
            
            tokens = usage.total_tokens
            cost = (tokens / 1000) * rate
            
            self.total_cost += cost
            self.total_tokens += tokens
            self.extractions += 1
            
            print(f"💰 Extraction cost: ${cost:.4f} ({tokens} tokens)")
            print(f"📊 Total cost: ${self.total_cost:.4f} ({self.extractions} extractions)")
    
    def get_summary(self):
        avg_cost = self.total_cost / max(self.extractions, 1)
        return {
            "total_cost": self.total_cost,
            "total_tokens": self.total_tokens,
            "extractions": self.extractions,
            "avg_cost_per_extraction": avg_cost
        }

# Usage
tracker = ExtractionCostTracker()

async def cost_aware_extraction():
    strategy = LLMExtractionStrategy(
        llm_config=cheap_config,
        schema=YourModel.model_json_schema(),
        extraction_type="schema",
        instruction="Extract data...",
        verbose=True  # Enable usage tracking
    )
    
    config = CrawlerRunConfig(extraction_strategy=strategy)
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://example.com", config=config)
        
        # Track costs
        tracker.track_llm_extraction(strategy, result)
        
        return result

# Monitor costs across multiple extractions
for url in urls:
    await cost_aware_extraction()

print(f"Final summary: {tracker.get_summary()}")
```

### Budget Controls

```python
class BudgetController:
    def __init__(self, daily_budget=10.0):
        self.daily_budget = daily_budget
        self.current_spend = 0.0
        self.extraction_count = 0
    
    def can_extract(self, estimated_cost=0.01):
        """Check if extraction is within budget"""
        if self.current_spend + estimated_cost > self.daily_budget:
            print(f"❌ Budget exceeded: ${self.current_spend:.2f} + ${estimated_cost:.2f} > ${self.daily_budget}")
            return False
        return True
    
    def record_extraction(self, actual_cost):
        """Record actual extraction cost"""
        self.current_spend += actual_cost
        self.extraction_count += 1
        
        remaining = self.daily_budget - self.current_spend
        print(f"💰 Budget remaining: ${remaining:.2f}")

budget = BudgetController(daily_budget=5.0)  # $5 daily limit

async def budget_controlled_extraction(url):
    if not budget.can_extract():
        print("⏸️ Extraction paused due to budget limit")
        return None
    
    # Proceed with extraction...
    strategy = LLMExtractionStrategy(llm_config=cheap_config, ...)
    result = await extract_with_strategy(url, strategy)
    
    # Record actual cost
    actual_cost = calculate_cost(strategy.usage_tracker)
    budget.record_extraction(actual_cost)
    
    return result

# Safe extraction with budget controls
results = []
for url in urls:
    result = await budget_controlled_extraction(url)
    if result:
        results.append(result)
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.