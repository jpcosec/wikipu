---
identity:
  node_id: "doc:wiki/drafts/3_how_to_write_code_documentation.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md", relation_type: "documents"}
---

### Module docstrings

## Details

### Module docstrings

Every Python file opens with a module docstring — an executive summary of what the module does and its role in the system.

### Class and method docstrings

Every public class, method, and function has a structured docstring with purpose, args, and return value. For ABCs, the class docstring explicitly lists all abstract methods as the developer contract.

### Pydantic field descriptions

`Field(description=...)` is dual-purpose: it's read by humans and consumed by LLMs. Write it accordingly — semantic, specific, with examples for fields that carry ambiguous values. For multilingual fields, include examples in both languages.

```python
# ✅
responsibilities: list[str] = Field(
    description="Job responsibilities ('Deine Aufgaben', 'Your Impact'). Extract as a list of short action phrases."
)
```

Mark MANDATORY vs. OPTIONAL fields in class-level comments so the boundary is visible without reading validation logic.

### Error contracts

Define domain-specific exceptions at the top of the file. Never rely on bare `Exception` for flow control.

```python
class ToolDependencyError(Exception): pass
class ToolFailureError(Exception): pass
```

Never swallow errors silently. If you catch a broad exception to trigger a fallback, log it with `[⚠️]` first and re-raise with `from e` to preserve the stack trace.

Expose operational limits (chunk sizes, retry budgets, rate limits) as `@property` on ABCs — not buried in loops or config dicts.

### Observability log tags

Logs are real-time execution documentation. **Never write emoji tag strings by hand** — import `LogTag` from `src/shared/log_tags.py`. This prevents typos and enforces the shared vocabulary.

```python
from src.shared.log_tags import LogTag

logger.info(f"{LogTag.LLM} Generating match proposal for {job_id}")
logger.warning(f"{LogTag.WARN} Rate limit hit, retrying in {delay}s")
logger.error(f"{LogTag.FAIL} Schema validation failed: {err}")
```

| `LogTag` | Tag | Meaning |
|---|---|---|
| `LogTag.SKIP` | `[⏭️]` | Skipped — already processed (idempotency) |
| `LogTag.CACHE` | `[📦]` | Cache hit / loaded existing artifact |
| `LogTag.LLM` | `[🧠]` | LLM reasoning or dynamic generation — **not for deterministic paths** |
| `LogTag.FAST` | `[⚡]` | Fast / deterministic path — no LLM involved |
| `LogTag.FALLBACK` | `[🤖]` | Fallback mechanism active |
| `LogTag.OK` | `[✅]` | Success / validation passed |
| `LogTag.WARN` | `[⚠️]` | Expected / handled error |
| `LogTag.FAIL` | `[❌]` | Hard failure — pipeline breaks |

Note: the enum enforces the tag vocabulary, not semantic correctness. Using `LogTag.LLM` on a deterministic path is still wrong — that's a code review concern.

---

Generated from `raw/docs_postulador_refactor/docs/standards/docs/documentation_and_planning_guide.md`.