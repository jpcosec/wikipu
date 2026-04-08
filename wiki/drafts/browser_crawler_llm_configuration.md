---
identity:
  node_id: "doc:wiki/drafts/browser_crawler_llm_configuration.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

Core configuration classes for controlling browser behavior, crawl operations, LLM providers, and understanding crawl results.

## Details

Core configuration classes for controlling browser behavior, crawl operations, LLM providers, and understanding crawl results.

### BrowserConfig - Browser Environment Setup

```python
from crawl4ai import BrowserConfig, AsyncWebCrawler

# Basic browser configuration
browser_config = BrowserConfig(
    browser_type="chromium",  # "chromium", "firefox", "webkit"
    headless=True,           # False for visible browser (debugging)
    viewport_width=1280,
    viewport_height=720,
    verbose=True
)

# Advanced browser setup with proxy and persistence
browser_config = BrowserConfig(
    headless=False,
    proxy="http://user:pass@proxy:8080",
    use_persistent_context=True,
    user_data_dir="./browser_data",
    cookies=[
        {"name": "session", "value": "abc123", "domain": "example.com"}
    ],
    headers={"Accept-Language": "en-US,en;q=0.9"},
    user_agent="Mozilla/5.0 (X11; Linux x86_64) Chrome/116.0.0.0 Safari/537.36",
    text_mode=True,  # Disable images for faster crawling
    extra_args=["--disable-extensions", "--no-sandbox"]
)

async with AsyncWebCrawler(config=browser_config) as crawler:
    result = await crawler.arun("https://example.com")
```

### CrawlerRunConfig - Crawl Operation Control

```python
from crawl4ai import CrawlerRunConfig, CacheMode
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

# Basic crawl configuration
run_config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,
    word_count_threshold=10,
    excluded_tags=["nav", "footer", "script"],
    exclude_external_links=True,
    screenshot=True,
    pdf=True
)

# Advanced content processing
md_generator = DefaultMarkdownGenerator(
    content_filter=PruningContentFilter(threshold=0.6),
    options={"citations": True, "ignore_links": False}
)

run_config = CrawlerRunConfig(
    # Content processing
    markdown_generator=md_generator,
    css_selector="main.content",  # Focus on specific content
    target_elements=[".article", ".post"],  # Multiple target selectors
    process_iframes=True,
    remove_overlay_elements=True,
    
    # Page interaction
    js_code=[
        "window.scrollTo(0, document.body.scrollHeight);",
        "document.querySelector('.load-more')?.click();"
    ],
    wait_for="css:.content-loaded",
    wait_for_timeout=10000,
    scan_full_page=True,
    
    # Session management
    session_id="persistent_session",
    
    # Media handling
    screenshot=True,
    pdf=True,
    capture_mhtml=True,
    image_score_threshold=5,
    
    # Advanced options
    simulate_user=True,
    magic=True,  # Auto-handle popups
    verbose=True
)
```

### CrawlerRunConfig Parameters by Category

```python
# Content Processing
config = CrawlerRunConfig(
    word_count_threshold=10,              # Min words per content block
    css_selector="main.article",          # Focus on specific content
    target_elements=[".post", ".content"], # Multiple target selectors
    excluded_tags=["nav", "footer"],       # Remove these tags
    excluded_selector="#ads, .tracker",   # Remove by selector
    only_text=True,                       # Text-only extraction
    keep_data_attributes=True,            # Preserve data-* attributes
    remove_forms=True,                    # Remove all forms
    process_iframes=True                  # Include iframe content
)

# Page Navigation & Timing
config = CrawlerRunConfig(
    wait_until="networkidle",             # Wait condition
    page_timeout=60000,                   # 60 second timeout
    wait_for="css:.loaded",               # Wait for specific element
    wait_for_images=True,                 # Wait for images to load
    delay_before_return_html=0.5,         # Final delay before capture
    semaphore_count=10                    # Max concurrent operations
)

# Page Interaction
config = CrawlerRunConfig(
    js_code="document.querySelector('button').click();",
    scan_full_page=True,                  # Auto-scroll page
    scroll_delay=0.3,                     # Delay between scrolls
    remove_overlay_elements=True,         # Remove popups/modals
    simulate_user=True,                   # Simulate human behavior
    override_navigator=True,              # Override navigator properties
    magic=True                           # Auto-handle common patterns
)

# Caching & Session
config = CrawlerRunConfig(
    cache_mode=CacheMode.BYPASS,          # Cache behavior
    session_id="my_session",              # Persistent session
    shared_data={"context": "value"}      # Share data between hooks
)

# Media & Output
config = CrawlerRunConfig(
    screenshot=True,                      # Capture screenshot
    pdf=True,                            # Generate PDF
    capture_mhtml=True,                  # Capture MHTML archive
    image_score_threshold=3,             # Filter low-quality images
    exclude_external_images=True         # Remove external images
)

# Link & Domain Filtering
config = CrawlerRunConfig(
    exclude_external_links=True,         # Remove external links
    exclude_social_media_links=True,     # Remove social media links
    exclude_domains=["ads.com", "tracker.io"],  # Custom domain filter
    exclude_internal_links=False         # Keep internal links
)
```

### LLMConfig - Language Model Setup

```python
from crawl4ai import LLMConfig

# OpenAI configuration
llm_config = LLMConfig(
    provider="openai/gpt-4o-mini",
    api_token=os.getenv("OPENAI_API_KEY"),  # or "env:OPENAI_API_KEY"
    temperature=0.1,
    max_tokens=2000
)

# Local model with Ollama
llm_config = LLMConfig(
    provider="ollama/llama3.3",
    api_token=None,  # Not needed for Ollama
    base_url="http://localhost:11434"  # Custom endpoint
)

# Anthropic Claude
llm_config = LLMConfig(
    provider="anthropic/claude-3-5-sonnet-20240620",
    api_token="env:ANTHROPIC_API_KEY",
    max_tokens=4000
)

# Google Gemini
llm_config = LLMConfig(
    provider="gemini/gemini-1.5-pro",
    api_token="env:GEMINI_API_KEY"
)

# Groq (fast inference)
llm_config = LLMConfig(
    provider="groq/llama3-70b-8192",
    api_token="env:GROQ_API_KEY"
)
```

### CrawlResult - Understanding Output

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com", config=run_config)
    
    # Basic status information
    print(f"Success: {result.success}")
    print(f"Status: {result.status_code}")
    print(f"URL: {result.url}")
    
    if not result.success:
        print(f"Error: {result.error_message}")
        return
    
    # HTML content variants
    print(f"Original HTML: {len(result.html)} chars")
    print(f"Cleaned HTML: {len(result.cleaned_html or '')} chars")
    
    # Markdown output (MarkdownGenerationResult)
    if result.markdown:
        print(f"Raw markdown: {len(result.markdown.raw_markdown)} chars")
        print(f"With citations: {len(result.markdown.markdown_with_citations)} chars")
        
        # Filtered content (if content filter was used)
        if result.markdown.fit_markdown:
            print(f"Fit markdown: {len(result.markdown.fit_markdown)} chars")
            print(f"Fit HTML: {len(result.markdown.fit_html)} chars")
    
    # Extracted structured data
    if result.extracted_content:
        import json
        data = json.loads(result.extracted_content)
        print(f"Extracted {len(data)} items")
    
    # Media and links
    images = result.media.get("images", [])
    print(f"Found {len(images)} images")
    for img in images[:3]:  # First 3 images
        print(f"  {img.get('src')} (score: {img.get('score', 0)})")
    
    internal_links = result.links.get("internal", [])
    external_links = result.links.get("external", [])
    print(f"Links: {len(internal_links)} internal, {len(external_links)} external")
    
    # Generated files
    if result.screenshot:
        print(f"Screenshot captured: {len(result.screenshot)} chars (base64)")
        # Save screenshot
        import base64
        with open("page.png", "wb") as f:
            f.write(base64.b64decode(result.screenshot))
    
    if result.pdf:
        print(f"PDF generated: {len(result.pdf)} bytes")
        with open("page.pdf", "wb") as f:
            f.write(result.pdf)
    
    if result.mhtml:
        print(f"MHTML captured: {len(result.mhtml)} chars")
        with open("page.mhtml", "w", encoding="utf-8") as f:
            f.write(result.mhtml)
    
    # SSL certificate information
    if result.ssl_certificate:
        print(f"SSL Issuer: {result.ssl_certificate.issuer}")
        print(f"Valid until: {result.ssl_certificate.valid_until}")
    
    # Network and console data (if captured)
    if result.network_requests:
        requests = [r for r in result.network_requests if r.get("event_type") == "request"]
        print(f"Network requests captured: {len(requests)}")
    
    if result.console_messages:
        errors = [m for m in result.console_messages if m.get("type") == "error"]
        print(f"Console messages: {len(result.console_messages)} ({len(errors)} errors)")
    
    # Session and metadata
    if result.session_id:
        print(f"Session ID: {result.session_id}")
    
    if result.metadata:
        print(f"Metadata: {result.metadata.get('title', 'No title')}")
```

### Configuration Helpers and Best Practices

```python
# Clone configurations for variations
base_config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    word_count_threshold=200,
    verbose=True
)

# Create streaming version
stream_config = base_config.clone(
    stream=True,
    cache_mode=CacheMode.BYPASS
)

# Create debug version
debug_config = base_config.clone(
    headless=False,
    page_timeout=120000,
    verbose=True
)

# Serialize/deserialize configurations
config_dict = base_config.dump()  # Convert to dict
restored_config = CrawlerRunConfig.load(config_dict)  # Restore from dict

# Browser configuration management
browser_config = BrowserConfig(headless=True, text_mode=True)
browser_dict = browser_config.to_dict()
cloned_browser = browser_config.clone(headless=False, verbose=True)
```

### Common Configuration Patterns

```python
# Fast text-only crawling
fast_config = CrawlerRunConfig(
    cache_mode=CacheMode.ENABLED,
    text_mode=True,
    exclude_external_links=True,
    exclude_external_images=True,
    word_count_threshold=50
)

# Comprehensive data extraction
comprehensive_config = CrawlerRunConfig(
    process_iframes=True,
    scan_full_page=True,
    wait_for_images=True,
    screenshot=True,
    capture_network_requests=True,
    capture_console_messages=True,
    magic=True
)

# Stealth crawling
stealth_config = CrawlerRunConfig(
    simulate_user=True,
    override_navigator=True,
    mean_delay=2.0,
    max_range=1.0,
    user_agent_mode="random"
)
```

### Advanced Configuration Features

#### User Agent Management & Bot Detection Avoidance

```python
from crawl4ai import CrawlerRunConfig

# Random user agent generation
config = CrawlerRunConfig(
    user_agent_mode="random",
    user_agent_generator_config={
        "platform": "windows",  # "windows", "macos", "linux", "android", "ios"
        "browser": "chrome",    # "chrome", "firefox", "safari", "edge"
        "device_type": "desktop"  # "desktop", "mobile", "tablet"
    }
)

# Custom user agent with stealth features
config = CrawlerRunConfig(
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    simulate_user=True,      # Simulate human mouse movements
    override_navigator=True,  # Override navigator properties
    mean_delay=1.5,          # Random delays between actions
    max_range=2.0
)

# Combined anti-detection approach
stealth_config = CrawlerRunConfig(
    user_agent_mode="random",
    simulate_user=True,
    override_navigator=True,
    magic=True,  # Auto-handle common bot detection patterns
    delay_before_return_html=2.0
)
```

#### Proxy Configuration with ProxyConfig

```python
from crawl4ai import CrawlerRunConfig, ProxyConfig, ProxyRotationStrategy

# Single proxy configuration
proxy_config = ProxyConfig(
    server="http://proxy.example.com:8080",
    username="proxy_user",
    password="proxy_pass"
)

# From proxy string format
proxy_config = ProxyConfig.from_string("192.168.1.100:8080:username:password")

# Multiple proxies with rotation
proxies = [
    ProxyConfig(server="http://proxy1.com:8080", username="user1", password="pass1"),
    ProxyConfig(server="http://proxy2.com:8080", username="user2", password="pass2"),
    ProxyConfig(server="http://proxy3.com:8080", username="user3", password="pass3")
]

rotation_strategy = ProxyRotationStrategy(
    proxies=proxies,
    rotation_method="round_robin"  # or "random", "least_used"
)

config = CrawlerRunConfig(
    proxy_config=proxy_config,
    proxy_rotation_strategy=rotation_strategy
)

# Load proxies from environment variable
proxies_from_env = ProxyConfig.from_env("MY_PROXIES")  # comma-separated proxy strings
```

#### Content Selection: css_selector vs target_elements

```python
from crawl4ai import CrawlerRunConfig

# css_selector: Extracts HTML at top level, affects entire processing
config = CrawlerRunConfig(
    css_selector="main.article, .content-area",  # Can be list of selectors
    # Everything else (markdown, extraction, links) works only on this HTML subset
)

# target_elements: Focuses extraction within already processed HTML
config = CrawlerRunConfig(
    css_selector="body",  # First extract entire body
    target_elements=[     # Then focus extraction on these elements
        ".article-content",
        ".post-body", 
        ".main-text"
    ],
    # Links, media from entire body, but markdown/extraction only from target_elements
)

# Hierarchical content selection
config = CrawlerRunConfig(
    css_selector=["#main-content", ".article-wrapper"],  # Top-level extraction
    target_elements=[                                     # Subset for processing
        ".article-title",
        ".article-body", 
        ".article-metadata"
    ],
    excluded_selector="#sidebar, .ads, .comments"  # Remove these from selection
)
```

#### Advanced wait_for Conditions

```python
from crawl4ai import CrawlerRunConfig

# CSS selector waiting
config = CrawlerRunConfig(
    wait_for="css:.content-loaded",  # Wait for element to appear
    wait_for_timeout=15000
)

# JavaScript boolean expression waiting
config = CrawlerRunConfig(
    wait_for="js:() => window.dataLoaded === true",  # Custom JS condition
    wait_for_timeout=20000
)

# Complex JavaScript conditions
config = CrawlerRunConfig(
    wait_for="js:() => document.querySelectorAll('.item').length >= 10",
    js_code=[
        "document.querySelector('.load-more')?.click();",
        "window.scrollTo(0, document.body.scrollHeight);"
    ]
)

# Multiple conditions with JavaScript
config = CrawlerRunConfig(
    wait_for="js:() => !document.querySelector('.loading') && document.querySelector('.results')",
    page_timeout=30000
)
```

#### Session Management for Multi-Step Crawling

```python
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

# Persistent session across multiple arun() calls
async def multi_step_crawling():
    async with AsyncWebCrawler() as crawler:
        # Step 1: Login page
        login_config = CrawlerRunConfig(
            session_id="user_session",  # Create persistent session
            js_code="document.querySelector('#username').value = 'user'; document.querySelector('#password').value = 'pass'; document.querySelector('#login').click();",
            wait_for="css:.dashboard",
            cache_mode=CacheMode.BYPASS
        )
        
        result1 = await crawler.arun("https://example.com/login", config=login_config)
        
        # Step 2: Navigate to protected area (reuses same browser page)
        nav_config = CrawlerRunConfig(
            session_id="user_session",  # Same session = same browser page
            js_only=True,  # No page reload, just JS navigation
            js_code="window.location.href = '/dashboard/data';",
            wait_for="css:.data-table"
        )
        
        result2 = await crawler.arun("https://example.com/dashboard/data", config=nav_config)
        
        # Step 3: Extract data from multiple pages
        for page in range(1, 6):
            page_config = CrawlerRunConfig(
                session_id="user_session",
                js_only=True,
                js_code=f"document.querySelector('.page-{page}').click();",
                wait_for=f"js:() => document.querySelector('.page-{page}').classList.contains('active')"
            )
            
            result = await crawler.arun(f"https://example.com/data/page/{page}", config=page_config)
            print(f"Page {page} data extracted: {len(result.extracted_content)}")
        
        # Important: Kill session when done
        await crawler.kill_session("user_session")

# Session with shared data between steps
async def session_with_shared_data():
    shared_context = {"user_id": "12345", "preferences": {"theme": "dark"}}
    
    config = CrawlerRunConfig(
        session_id="persistent_session",
        shared_data=shared_context,  # Available across all session calls
        js_code="console.log('User ID:', window.sharedData.user_id);"
    )
```

#### Identity-Based Crawling Parameters

```python
from crawl4ai import CrawlerRunConfig, GeolocationConfig

# Locale and timezone simulation
config = CrawlerRunConfig(
    locale="en-US",                    # Browser language preference
    timezone_id="America/New_York",    # Timezone setting
    user_agent_mode="random",
    user_agent_generator_config={
        "platform": "windows",
        "locale": "en-US"
    }
)

# Geolocation simulation
geo_config = GeolocationConfig(
    latitude=40.7128,   # New York coordinates
    longitude=-74.0060,
    accuracy=100.0
)

config = CrawlerRunConfig(
    geolocation=geo_config,
    locale="en-US",
    timezone_id="America/New_York"
)

# Complete identity simulation
identity_config = CrawlerRunConfig(
    # Location identity
    locale="fr-FR",
    timezone_id="Europe/Paris", 
    geolocation=GeolocationConfig(latitude=48.8566, longitude=2.3522),
    
    # Browser identity
    user_agent_mode="random",
    user_agent_generator_config={
        "platform": "windows",
        "locale": "fr-FR",
        "browser": "chrome"
    },
    
    # Behavioral identity
    simulate_user=True,
    override_navigator=True,
    mean_delay=2.0,
    max_range=1.5
)
```

#### Simplified Import Pattern

```python
# Almost everything from crawl4ai main package
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig, 
    CrawlerRunConfig,
    LLMConfig,
    CacheMode,
    ProxyConfig,
    GeolocationConfig
)

# Specialized strategies (still from crawl4ai)
from crawl4ai import (
    JsonCssExtractionStrategy,
    LLMExtractionStrategy,
    DefaultMarkdownGenerator,
    PruningContentFilter,
    RegexChunking
)

# Complete example with simplified imports
async def example_crawl():
    browser_config = BrowserConfig(headless=True)
    
    run_config = CrawlerRunConfig(
        user_agent_mode="random",
        proxy_config=ProxyConfig.from_string("192.168.1.1:8080:user:pass"),
        css_selector="main.content",
        target_elements=[".article", ".post"],
        wait_for="js:() => document.querySelector('.loaded')",
        session_id="my_session",
        simulate_user=True
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun("https://example.com", config=run_config)
        return result
```

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.