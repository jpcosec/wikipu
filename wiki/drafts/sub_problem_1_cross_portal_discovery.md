---
identity:
  node_id: "doc:wiki/drafts/sub_problem_1_cross_portal_discovery.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/new_feature/stage2_cross_portal_and_autoapply.md", relation_type: "documents"}
---

### Problem

## Details

### Problem

The `application_url` field captured during scrape-time points to a company ATS (Workday, Greenhouse, Lever, SAP SuccessFactors, Taleo, etc.) or a company career sub-domain. We are not currently following these links to discover additional open positions at that company.

### Crawl4AI capabilities available

- `AdaptiveCrawler` with `digest()` — intelligently follows links on a careers page using information foraging: evaluates coverage, consistency, and saturation to stop automatically when all relevant job URLs have been found. Cheaper and faster than blind BFS for this use case.
- `DomainFilter(allowed_domains=[company_domain])` — scopes discovery to the company's ATS domain
- `URLPatternFilter` — filters to job-like URL patterns (`*/jobs/*`, `*/careers/*`, `*/stellenangebote/*`)
- `AsyncUrlSeeder(source="sitemap")` — if the company careers page exposes a sitemap, bulk-discovers all open positions instantly without crawling

### Proposed architecture

```
JobPosting.application_url
    ↓
CompanyPortalAdapter.discover(url)
    ↓  AdaptiveCrawler.digest(
    ↓      start_url=application_url,
    ↓      query="open job position requirements responsibilities"
    ↓  )  + URLPatternFilter(patterns=["*/jobs/*", "*/careers/*", "*/apply/*"])
    ↓
[list of job page URLs on company portal]
    ↓
SmartScraperAdapter (or new CompanyPortalAdapter)
    ↓
canonical ingest under data/jobs/<company_domain>/<job_id>/
```

`AdaptiveCrawler` stops automatically when saturation is high (no new job-like pages are being found), avoiding over-crawling. `AsyncUrlSeeder` is the preferred path when the target domain exposes a sitemap — faster and zero token cost.

A new `source` value (e.g. `"company:siemens.com"`) would distinguish company-portal-discovered jobs from aggregator-discovered ones.

### ATS detection and anti-bot strategy

Most major ATS platforms have recognizable URL patterns. A small lookup table maps domain patterns to known ATS types, which informs both the extraction schema and the bot-evasion config to use:

| ATS | URL pattern | Rendering | Bot protection |
|-----|-------------|-----------|---------------|
| Workday | `*.wd*.myworkdayjobs.com` | Heavy SPA | Cloudflare |
| Greenhouse | `boards.greenhouse.io/*` | Mostly static | Low |
| Lever | `jobs.lever.co/*` | Clean JSON-LD | Low |
| SAP SuccessFactors | `*.successfactors.com/*` | Complex SPA | Medium |
| Taleo | `*.taleo.net/*` | Legacy iframes | Low |

For portals with active bot protection (Workday, SAP), apply stealth mode:

```python
from crawl4ai import UndetectedAdapter, BrowserConfig

browser_config = BrowserConfig(
    enable_stealth=True,
    headless=False,  # required to defeat some DataDome checks
)
```

`enable_stealth=True` patches browser fingerprints. `headless=False` is sometimes required for Cloudflare/DataDome challenges that inspect rendering behavior. Use only when the portal is known to block headless crawlers — it is slower and more resource-intensive.

---

Generated from `raw/docs_postulador_refactor/future_docs/new_feature/stage2_cross_portal_and_autoapply.md`.