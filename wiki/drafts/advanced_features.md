---
identity:
  node_id: "doc:wiki/drafts/advanced_features.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

Comprehensive guide to advanced crawling capabilities including file handling, authentication, dynamic content, monitoring, and session management.

## Details

Comprehensive guide to advanced crawling capabilities including file handling, authentication, dynamic content, monitoring, and session management.

### File Download Handling

```python
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
import os

# Enable downloads with custom path
downloads_path = os.path.join(os.getcwd(), "my_downloads")
os.makedirs(downloads_path, exist_ok=True)

browser_config = BrowserConfig(
    accept_downloads=True,
    downloads_path=downloads_path
)

# Trigger downloads with JavaScript
async def download_files():
    async with AsyncWebCrawler(config=browser_config) as crawler:
        config = CrawlerRunConfig(
            js_code="""
                // Click download links
                const downloadLinks = document.querySelectorAll('a[href$=".pdf"]');
                for (const link of downloadLinks) {
                    link.click();
                    await new Promise(r => setTimeout(r, 2000));  // Delay between downloads
                }
            """,
            wait_for=5  # Wait for downloads to start
        )
        
        result = await crawler.arun("https://example.com/downloads", config=config)
        
        if result.downloaded_files:
            print("Downloaded files:")
            for file_path in result.downloaded_files:
                print(f"- {file_path} ({os.path.getsize(file_path)} bytes)")
```

### Hooks & Authentication

```python
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from playwright.async_api import Page, BrowserContext

async def advanced_crawler_with_hooks():
    browser_config = BrowserConfig(headless=True, verbose=True)
    crawler = AsyncWebCrawler(config=browser_config)

    # Hook functions for different stages
    async def on_browser_created(browser, **kwargs):
        print("[HOOK] Browser created successfully")
        return browser

    async def on_page_context_created(page: Page, context: BrowserContext, **kwargs):
        print("[HOOK] Setting up page & context")
        
        # Block images for faster crawling
        async def route_filter(route):
            if route.request.resource_type == "image":
                await route.abort()
            else:
                await route.continue_()
        
        await context.route("**", route_filter)
        
        # Simulate login if needed
        # await page.goto("https://example.com/login")
        # await page.fill("input[name='username']", "testuser")
        # await page.fill("input[name='password']", "password123")
        # await page.click("button[type='submit']")
        
        await page.set_viewport_size({"width": 1080, "height": 600})
        return page

    async def before_goto(page: Page, context: BrowserContext, url: str, **kwargs):
        print(f"[HOOK] About to navigate to: {url}")
        await page.set_extra_http_headers({"Custom-Header": "my-value"})
        return page

    async def after_goto(page: Page, context: BrowserContext, url: str, response, **kwargs):
        print(f"[HOOK] Successfully loaded: {url}")
        try:
            await page.wait_for_selector('.content', timeout=1000)
            print("[HOOK] Content found!")
        except:
            print("[HOOK] Content not found, continuing")
        return page

    async def before_retrieve_html(page: Page, context: BrowserContext, **kwargs):
        print("[HOOK] Final actions before HTML retrieval")
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
        return page

    # Attach hooks
    crawler.crawler_strategy.set_hook("on_browser_created", on_browser_created)
    crawler.crawler_strategy.set_hook("on_page_context_created", on_page_context_created)
    crawler.crawler_strategy.set_hook("before_goto", before_goto)
    crawler.crawler_strategy.set_hook("after_goto", after_goto)
    crawler.crawler_strategy.set_hook("before_retrieve_html", before_retrieve_html)

    await crawler.start()
    
    config = CrawlerRunConfig()
    result = await crawler.arun("https://example.com", config=config)
    
    if result.success:
        print(f"Crawled successfully: {len(result.html)} chars")
    
    await crawler.close()
```

### Lazy Loading & Dynamic Content

```python
# Handle lazy-loaded images and infinite scroll
async def handle_lazy_loading():
    config = CrawlerRunConfig(
        # Wait for images to fully load
        wait_for_images=True,
        
        # Automatically scroll entire page to trigger lazy loading
        scan_full_page=True,
        scroll_delay=0.5,  # Delay between scroll steps
        
        # JavaScript for custom lazy loading
        js_code="""
            // Scroll and wait for content to load
            window.scrollTo(0, document.body.scrollHeight);
            
            // Click "Load More" if available
            const loadMoreBtn = document.querySelector('.load-more');
            if (loadMoreBtn) {
                loadMoreBtn.click();
            }
        """,
        
        # Wait for specific content to appear
        wait_for="css:.lazy-content:nth-child(20)",  # Wait for 20 items
        
        # Exclude external images to focus on main content
        exclude_external_images=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/gallery", config=config)
        
        if result.success:
            images = result.media.get("images", [])
            print(f"Loaded {len(images)} images after lazy loading")
            for img in images[:3]:
                print(f"- {img.get('src')} (score: {img.get('score', 'N/A')})")
```

### Network & Console Monitoring

```python
# Capture all network requests and console messages for debugging
async def monitor_network_and_console():
    config = CrawlerRunConfig(
        capture_network_requests=True,
        capture_console_messages=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        
        if result.success:
            # Analyze network requests
            if result.network_requests:
                requests = [r for r in result.network_requests if r.get("event_type") == "request"]
                responses = [r for r in result.network_requests if r.get("event_type") == "response"]
                failures = [r for r in result.network_requests if r.get("event_type") == "request_failed"]
                
                print(f"Network activity: {len(requests)} requests, {len(responses)} responses, {len(failures)} failures")
                
                # Find API calls
                api_calls = [r for r in requests if "api" in r.get("url", "")]
                print(f"API calls detected: {len(api_calls)}")
                
                # Show failed requests
                for failure in failures[:3]:
                    print(f"Failed: {failure.get('url')} - {failure.get('failure_text')}")
            
            # Analyze console messages
            if result.console_messages:
                message_types = {}
                for msg in result.console_messages:
                    msg_type = msg.get("type", "unknown")
                    message_types[msg_type] = message_types.get(msg_type, 0) + 1
                
                print(f"Console messages: {message_types}")
                
                # Show errors
                errors = [msg for msg in result.console_messages if msg.get("type") == "error"]
                for error in errors[:2]:
                    print(f"JS Error: {error.get('text', '')[:100]}")
```

### Session Management for Multi-Step Workflows

```python
# Maintain state across multiple requests for complex workflows
async def multi_step_session_workflow():
    session_id = "workflow_session"
    
    async with AsyncWebCrawler() as crawler:
        # Step 1: Initial page load
        config1 = CrawlerRunConfig(
            session_id=session_id,
            wait_for="css:.content-loaded"
        )
        
        result1 = await crawler.arun("https://example.com/step1", config=config1)
        print("Step 1 completed")
        
        # Step 2: Navigate and interact (same browser tab)
        config2 = CrawlerRunConfig(
            session_id=session_id,
            js_only=True,  # Don't reload page, just run JS
            js_code="""
                document.querySelector('#next-button').click();
            """,
            wait_for="css:.step2-content"
        )
        
        result2 = await crawler.arun("https://example.com/step2", config=config2)
        print("Step 2 completed")
        
        # Step 3: Form submission
        config3 = CrawlerRunConfig(
            session_id=session_id,
            js_only=True,
            js_code="""
                document.querySelector('#form-field').value = 'test data';
                document.querySelector('#submit-btn').click();
            """,
            wait_for="css:.results"
        )
        
        result3 = await crawler.arun("https://example.com/submit", config=config3)
        print("Step 3 completed")
        
        # Clean up session
        await crawler.crawler_strategy.kill_session(session_id)

# Advanced GitHub commits pagination example
async def github_commits_pagination():
    session_id = "github_session"
    all_commits = []
    
    async with AsyncWebCrawler() as crawler:
        for page in range(3):
            if page == 0:
                # Initial load
                config = CrawlerRunConfig(
                    session_id=session_id,
                    wait_for="js:() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"
                )
            else:
                # Navigate to next page
                config = CrawlerRunConfig(
                    session_id=session_id,
                    js_only=True,
                    js_code='document.querySelector(\'a[data-testid="pagination-next-button"]\').click();',
                    wait_for="js:() => document.querySelectorAll('li.Box-sc-g0xbh4-0').length > 0"
                )
            
            result = await crawler.arun(
                "https://github.com/microsoft/TypeScript/commits/main",
                config=config
            )
            
            if result.success:
                commit_count = result.cleaned_html.count('li.Box-sc-g0xbh4-0')
                print(f"Page {page + 1}: Found {commit_count} commits")
        
        await crawler.crawler_strategy.kill_session(session_id)
```

### SSL Certificate Analysis

```python
# Fetch and analyze SSL certificates
async def analyze_ssl_certificates():
    config = CrawlerRunConfig(
        fetch_ssl_certificate=True
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        
        if result.success and result.ssl_certificate:
            cert = result.ssl_certificate
            
            # Basic certificate info
            print(f"Issuer: {cert.issuer.get('CN', 'Unknown')}")
            print(f"Subject: {cert.subject.get('CN', 'Unknown')}")
            print(f"Valid from: {cert.valid_from}")
            print(f"Valid until: {cert.valid_until}")
            print(f"Fingerprint: {cert.fingerprint}")
            
            # Export certificate in different formats
            import os
            os.makedirs("certificates", exist_ok=True)
            
            cert.to_json("certificates/cert.json")
            cert.to_pem("certificates/cert.pem")
            cert.to_der("certificates/cert.der")
            
            print("Certificate exported in multiple formats")
```

### Advanced Page Interaction

```python
# Complex page interactions with dynamic content
async def advanced_page_interaction():
    async with AsyncWebCrawler() as crawler:
        # Multi-step interaction with waiting
        config = CrawlerRunConfig(
            js_code=[
                # Step 1: Scroll to load content
                "window.scrollTo(0, document.body.scrollHeight);",
                
                # Step 2: Wait and click load more
                """
                (async () => {
                    await new Promise(resolve => setTimeout(resolve, 2000));
                    const loadMore = document.querySelector('.load-more');
                    if (loadMore) loadMore.click();
                })();
                """
            ],
            
            # Wait for new content to appear
            wait_for="js:() => document.querySelectorAll('.item').length > 20",
            
            # Additional timing controls
            page_timeout=60000,  # 60 second timeout
            delay_before_return_html=2.0,  # Wait before final capture
            
            # Handle overlays automatically
            remove_overlay_elements=True,
            magic=True,  # Auto-handle common popup patterns
            
            # Simulate human behavior
            simulate_user=True,
            override_navigator=True
        )
        
        result = await crawler.arun("https://example.com/dynamic", config=config)
        
        if result.success:
            print(f"Interactive crawl completed: {len(result.cleaned_html)} chars")

# Form interaction example
async def form_interaction_example():
    config = CrawlerRunConfig(
        js_code="""
            // Fill search form
            document.querySelector('#search-input').value = 'machine learning';
            document.querySelector('#category-select').value = 'technology';
            document.querySelector('#search-form').submit();
        """,
        wait_for="css:.search-results",
        session_id="search_session"
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com/search", config=config)
        print("Search completed, results loaded")
```

### Local File & Raw HTML Processing

```python
# Handle different input types: URLs, local files, raw HTML
async def handle_different_inputs():
    async with AsyncWebCrawler() as crawler:
        # 1. Regular web URL
        result1 = await crawler.arun("https://example.com")
        
        # 2. Local HTML file
        local_file_path = "/path/to/file.html"
        result2 = await crawler.arun(f"file://{local_file_path}")
        
        # 3. Raw HTML content
        raw_html = "<html><body><h1>Test Content</h1><p>Sample text</p></body></html>"
        result3 = await crawler.arun(f"raw:{raw_html}")
        
        # All return the same CrawlResult structure
        for i, result in enumerate([result1, result2, result3], 1):
            if result.success:
                print(f"Input {i}: {len(result.markdown)} chars of markdown")

# Save and re-process HTML example
async def save_and_reprocess():
    async with AsyncWebCrawler() as crawler:
        # Original crawl
        result = await crawler.arun("https://example.com")
        
        if result.success:
            # Save HTML to file
            with open("saved_page.html", "w", encoding="utf-8") as f:
                f.write(result.html)
            
            # Re-process from file
            file_result = await crawler.arun("file://./saved_page.html")
            
            # Process as raw HTML
            raw_result = await crawler.arun(f"raw:{result.html}")
            
            # Verify consistency
            assert len(result.markdown) == len(file_result.markdown) == len(raw_result.markdown)
            print("✅ All processing methods produced identical results")
```

### Advanced Link & Media Handling

```python
# Comprehensive link and media extraction with filtering
async def advanced_link_media_handling():
    config = CrawlerRunConfig(
        # Link filtering
        exclude_external_links=False,  # Keep external links for analysis
        exclude_social_media_links=True,
        exclude_domains=["ads.com", "tracker.io", "spammy.net"],
        
        # Media handling
        exclude_external_images=True,
        image_score_threshold=5,  # Only high-quality images
        table_score_threshold=7,  # Only well-structured tables
        wait_for_images=True,
        
        # Capture additional formats
        screenshot=True,
        pdf=True,
        capture_mhtml=True  # Full page archive
    )
    
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://example.com", config=config)
        
        if result.success:
            # Analyze links
            internal_links = result.links.get("internal", [])
            external_links = result.links.get("external", [])
            print(f"Links: {len(internal_links)} internal, {len(external_links)} external")
            
            # Analyze media
            images = result.media.get("images", [])
            tables = result.media.get("tables", [])
            print(f"Media: {len(images)} images, {len(tables)} tables")
            
            # High-quality images only
            quality_images = [img for img in images if img.get("score", 0) >= 5]
            print(f"High-quality images: {len(quality_images)}")
            
            # Table analysis
            for i, table in enumerate(tables[:2]):
                print(f"Table {i+1}: {len(table.get('headers', []))} columns, {len(table.get('rows', []))} rows")
            
            # Save captured files
            if result.screenshot:
                import base64
                with open("page_screenshot.png", "wb") as f:
                    f.write(base64.b64decode(result.screenshot))
            
            if result.pdf:
                with open("page.pdf", "wb") as f:
                    f.write(result.pdf)
            
            if result.mhtml:
                with open("page_archive.mhtml", "w", encoding="utf-8") as f:
                    f.write(result.mhtml)
            
            print("Additional formats saved: screenshot, PDF, MHTML archive")
```

### Performance & Resource Management

```python
# Optimize performance for large-scale crawling
async def performance_optimized_crawling():
    # Lightweight browser config
    browser_config = BrowserConfig(
        headless=True,
        text_mode=True,  # Disable images for speed
        light_mode=True,  # Reduce background features
        extra_args=["--disable-extensions", "--no-sandbox"]
    )
    
    # Efficient crawl config
    config = CrawlerRunConfig(
        # Content filtering for speed
        excluded_tags=["script", "style", "nav", "footer"],
        exclude_external_links=True,
        exclude_all_images=True,  # Remove all images for max speed
        word_count_threshold=50,
        
        # Timing optimizations
        page_timeout=30000,  # Faster timeout
        delay_before_return_html=0.1,
        
        # Resource monitoring
        capture_network_requests=False,  # Disable unless needed
        capture_console_messages=False,
        
        # Cache for repeated URLs
        cache_mode=CacheMode.ENABLED
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        urls = ["https://example.com/page1", "https://example.com/page2", "https://example.com/page3"]
        
        # Efficient batch processing
        batch_config = config.clone(
            stream=True,  # Stream results as they complete
            semaphore_count=3  # Control concurrency
        )
        
        async for result in await crawler.arun_many(urls, config=batch_config):
            if result.success:
                print(f"✅ {result.url}: {len(result.markdown)} chars")
            else:
                print(f"❌ {result.url}: {result.error_message}")
```


**📖 Learn more:** [Complete Parameter Reference](https://docs.crawl4ai.com/api/parameters/), [Content Filtering](https://docs.crawl4ai.com/core/markdown-generation/), [Session Management](https://docs.crawl4ai.com/advanced/session-management/), [Network Capture](https://docs.crawl4ai.com/advanced/network-console-capture/)

**📖 Learn more:** [Hooks & Authentication](https://docs.crawl4ai.com/advanced/hooks-auth/), [Session Management](https://docs.crawl4ai.com/advanced/session-management/), [Network Monitoring](https://docs.crawl4ai.com/advanced/network-console-capture/), [Page Interaction](https://docs.crawl4ai.com/core/page-interaction/), [File Downloads](https://docs.crawl4ai.com/advanced/file-downloading/)

---

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.