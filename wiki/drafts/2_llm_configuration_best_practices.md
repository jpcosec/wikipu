---
identity:
  node_id: "doc:wiki/drafts/2_llm_configuration_best_practices.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

### Cost Optimization

## Details

### Cost Optimization

```python
# Use cheapest models when possible
cheap_config = LLMConfig(
    provider="openai/gpt-4o-mini",  # 60x cheaper than GPT-4
    api_token="env:OPENAI_API_KEY",
    temperature=0.0,  # Deterministic output
    max_tokens=800    # Limit output length
)

# Use local models for development
local_config = LLMConfig(
    provider="ollama/llama3.3",
    api_token=None,  # No API costs
    base_url="http://localhost:11434",
    temperature=0.1
)

# Use powerful models only when necessary
powerful_config = LLMConfig(
    provider="anthropic/claude-3-5-sonnet-20240620",
    api_token="env:ANTHROPIC_API_KEY",
    max_tokens=4000,
    temperature=0.1
)
```

### Provider Selection Guide

```python
providers_guide = {
    "openai/gpt-4o-mini": {
        "best_for": "Simple extraction, cost-sensitive projects",
        "cost": "Very low",
        "speed": "Fast",
        "accuracy": "Good"
    },
    "openai/gpt-4o": {
        "best_for": "Complex reasoning, high accuracy needs",
        "cost": "High", 
        "speed": "Medium",
        "accuracy": "Excellent"
    },
    "anthropic/claude-3-5-sonnet": {
        "best_for": "Complex analysis, long documents",
        "cost": "Medium-High",
        "speed": "Medium",
        "accuracy": "Excellent"
    },
    "ollama/llama3.3": {
        "best_for": "Development, no API costs",
        "cost": "Free (self-hosted)",
        "speed": "Variable",
        "accuracy": "Good"
    },
    "groq/llama3-70b-8192": {
        "best_for": "Fast inference, open source",
        "cost": "Low",
        "speed": "Very fast",
        "accuracy": "Good"
    }
}

def choose_provider(complexity, budget, speed_requirement):
    """Choose optimal provider based on requirements"""
    if budget == "minimal":
        return "ollama/llama3.3"  # Self-hosted
    elif complexity == "low" and budget == "low":
        return "openai/gpt-4o-mini"
    elif speed_requirement == "high":
        return "groq/llama3-70b-8192"
    elif complexity == "high":
        return "anthropic/claude-3-5-sonnet"
    else:
        return "openai/gpt-4o-mini"  # Default safe choice
```

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.