---
identity:
  node_id: "doc:wiki/drafts/configuration_objects_and_system_architecture.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

Visual representations of Crawl4AI's configuration system, object relationships, and data flow patterns.

## Details

Visual representations of Crawl4AI's configuration system, object relationships, and data flow patterns.

### Configuration Object Relationships

```mermaid
classDiagram
    class BrowserConfig {
        +browser_type: str
        +headless: bool
        +viewport_width: int
        +viewport_height: int
        +proxy: str
        +user_agent: str
        +cookies: list
        +headers: dict
        +clone() BrowserConfig
        +to_dict() dict
    }
    
    class CrawlerRunConfig {
        +cache_mode: CacheMode
        +extraction_strategy: ExtractionStrategy
        +markdown_generator: MarkdownGenerator
        +js_code: list
        +wait_for: str
        +screenshot: bool
        +session_id: str
        +clone() CrawlerRunConfig
        +dump() dict
    }
    
    class LLMConfig {
        +provider: str
        +api_token: str
        +base_url: str
        +temperature: float
        +max_tokens: int
        +clone() LLMConfig
        +to_dict() dict
    }
    
    class CrawlResult {
        +url: str
        +success: bool
        +html: str
        +cleaned_html: str
        +markdown: MarkdownGenerationResult
        +extracted_content: str
        +media: dict
        +links: dict
        +screenshot: str
        +pdf: bytes
    }
    
    class AsyncWebCrawler {
        +config: BrowserConfig
        +arun() CrawlResult
    }
    
    AsyncWebCrawler --> BrowserConfig : uses
    AsyncWebCrawler --> CrawlerRunConfig : accepts
    CrawlerRunConfig --> LLMConfig : contains
    AsyncWebCrawler --> CrawlResult : returns
    
    note for BrowserConfig "Controls browser\nenvironment and behavior"
    note for CrawlerRunConfig "Controls individual\ncrawl operations"
    note for LLMConfig "Configures LLM\nproviders and parameters"
    note for CrawlResult "Contains all crawl\noutputs and metadata"
```

### Configuration Decision Flow

```mermaid
flowchart TD
    A[Start Configuration] --> B{Use Case Type?}
    
    B -->|Simple Web Scraping| C[Basic Config Pattern]
    B -->|Data Extraction| D[Extraction Config Pattern]
    B -->|Stealth Crawling| E[Stealth Config Pattern]
    B -->|High Performance| F[Performance Config Pattern]
    
    C --> C1[BrowserConfig: headless=True]
    C --> C2[CrawlerRunConfig: basic options]
    C1 --> C3[No LLMConfig needed]
    C2 --> C3
    C3 --> G[Simple Crawling Ready]
    
    D --> D1[BrowserConfig: standard setup]
    D --> D2[CrawlerRunConfig: with extraction_strategy]
    D --> D3[LLMConfig: for LLM extraction]
    D1 --> D4[Advanced Extraction Ready]
    D2 --> D4
    D3 --> D4
    
    E --> E1[BrowserConfig: proxy + user_agent]
    E --> E2[CrawlerRunConfig: simulate_user=True]
    E1 --> E3[Stealth Crawling Ready]
    E2 --> E3
    
    F --> F1[BrowserConfig: lightweight]
    F --> F2[CrawlerRunConfig: caching + concurrent]
    F1 --> F3[High Performance Ready]
    F2 --> F3
    
    G --> H[Execute Crawl]
    D4 --> H
    E3 --> H
    F3 --> H
    
    H --> I[Get CrawlResult]
    
    style A fill:#e1f5fe
    style I fill:#c8e6c9
    style G fill:#fff3e0
    style D4 fill:#f3e5f5
    style E3 fill:#ffebee
    style F3 fill:#e8f5e8
```

### Configuration Lifecycle Sequence

```mermaid
sequenceDiagram
    participant User
    participant BrowserConfig as Browser Config
    participant CrawlerConfig as Crawler Config
    participant LLMConfig as LLM Config
    participant Crawler as AsyncWebCrawler
    participant Browser as Browser Instance
    participant Result as CrawlResult
    
    User->>BrowserConfig: Create with browser settings
    User->>CrawlerConfig: Create with crawl options
    User->>LLMConfig: Create with LLM provider
    
    User->>Crawler: Initialize with BrowserConfig
    Crawler->>Browser: Launch browser with config
    Browser-->>Crawler: Browser ready
    
    User->>Crawler: arun(url, CrawlerConfig)
    Crawler->>Crawler: Apply CrawlerConfig settings
    
    alt LLM Extraction Needed
        Crawler->>LLMConfig: Get LLM settings
        LLMConfig-->>Crawler: Provider configuration
    end
    
    Crawler->>Browser: Navigate with settings
    Browser->>Browser: Apply page interactions
    Browser->>Browser: Execute JavaScript if specified
    Browser->>Browser: Wait for conditions
    
    Browser-->>Crawler: Page content ready
    Crawler->>Crawler: Process content per config
    Crawler->>Result: Create CrawlResult
    
    Result-->>User: Return complete result
    
    Note over User,Result: Configuration objects control every aspect
```

### BrowserConfig Parameter Flow

```mermaid
graph TB
    subgraph "BrowserConfig Parameters"
        A[browser_type] --> A1[chromium/firefox/webkit]
        B[headless] --> B1[true: invisible / false: visible]
        C[viewport] --> C1[width x height dimensions]
        D[proxy] --> D1[proxy server configuration]
        E[user_agent] --> E1[browser identification string]
        F[cookies] --> F1[session authentication]
        G[headers] --> G1[HTTP request headers]
        H[extra_args] --> H1[browser command line flags]
    end
    
    subgraph "Browser Instance"
        I[Playwright Browser]
        J[Browser Context]
        K[Page Instance]
    end
    
    A1 --> I
    B1 --> I
    C1 --> J
    D1 --> J
    E1 --> J
    F1 --> J
    G1 --> J
    H1 --> I
    
    I --> J
    J --> K
    
    style I fill:#e3f2fd
    style J fill:#f3e5f5
    style K fill:#e8f5e8
```

### CrawlerRunConfig Category Breakdown

```mermaid
mindmap
  root((CrawlerRunConfig))
    Content Processing
      word_count_threshold
      css_selector
      target_elements
      excluded_tags
      markdown_generator
      extraction_strategy
    Page Navigation
      wait_until
      page_timeout
      wait_for
      wait_for_images
      delay_before_return_html
    Page Interaction
      js_code
      scan_full_page
      simulate_user
      magic
      remove_overlay_elements
    Caching Session
      cache_mode
      session_id
      shared_data
    Media Output
      screenshot
      pdf
      capture_mhtml
      image_score_threshold
    Link Filtering
      exclude_external_links
      exclude_domains
      exclude_social_media_links
```

### LLM Provider Selection Flow

```mermaid
flowchart TD
    A[Need LLM Processing?] --> B{Provider Type?}
    
    B -->|Cloud API| C{Which Service?}
    B -->|Local Model| D[Local Setup]
    B -->|Custom Endpoint| E[Custom Config]
    
    C -->|OpenAI| C1[OpenAI GPT Models]
    C -->|Anthropic| C2[Claude Models]
    C -->|Google| C3[Gemini Models]
    C -->|Groq| C4[Fast Inference]
    
    D --> D1[Ollama Setup]
    E --> E1[Custom base_url]
    
    C1 --> F1[LLMConfig with OpenAI settings]
    C2 --> F2[LLMConfig with Anthropic settings]
    C3 --> F3[LLMConfig with Google settings]
    C4 --> F4[LLMConfig with Groq settings]
    D1 --> F5[LLMConfig with Ollama settings]
    E1 --> F6[LLMConfig with custom settings]
    
    F1 --> G[Use in Extraction Strategy]
    F2 --> G
    F3 --> G
    F4 --> G
    F5 --> G
    F6 --> G
    
    style A fill:#e1f5fe
    style G fill:#c8e6c9
```

### CrawlResult Structure and Data Flow

```mermaid
graph TB
    subgraph "CrawlResult Output"
        A[Basic Info]
        B[HTML Content]
        C[Markdown Output]
        D[Extracted Data]
        E[Media Files]
        F[Metadata]
    end
    
    subgraph "Basic Info Details"
        A --> A1[url: final URL]
        A --> A2[success: boolean]
        A --> A3[status_code: HTTP status]
        A --> A4[error_message: if failed]
    end
    
    subgraph "HTML Content Types"
        B --> B1[html: raw HTML]
        B --> B2[cleaned_html: processed]
        B --> B3[fit_html: filtered content]
    end
    
    subgraph "Markdown Variants"
        C --> C1[raw_markdown: basic conversion]
        C --> C2[markdown_with_citations: with refs]
        C --> C3[fit_markdown: filtered content]
        C --> C4[references_markdown: citation list]
    end
    
    subgraph "Extracted Content"
        D --> D1[extracted_content: JSON string]
        D --> D2[From CSS extraction]
        D --> D3[From LLM extraction]
        D --> D4[From XPath extraction]
    end
    
    subgraph "Media and Links"
        E --> E1[images: list with scores]
        E --> E2[videos: media content]
        E --> E3[internal_links: same domain]
        E --> E4[external_links: other domains]
    end
    
    subgraph "Generated Files"
        F --> F1[screenshot: base64 PNG]
        F --> F2[pdf: binary PDF data]
        F --> F3[mhtml: archive format]
        F --> F4[ssl_certificate: cert info]
    end
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#ffebee
    style F fill:#f1f8e9
```

### Configuration Pattern State Machine

```mermaid
stateDiagram-v2
    [*] --> ConfigCreation
    
    ConfigCreation --> BasicConfig: Simple use case
    ConfigCreation --> AdvancedConfig: Complex requirements
    ConfigCreation --> TemplateConfig: Use predefined pattern
    
    BasicConfig --> Validation: Check parameters
    AdvancedConfig --> Validation: Check parameters
    TemplateConfig --> Validation: Check parameters
    
    Validation --> Invalid: Missing required fields
    Validation --> Valid: All parameters correct
    
    Invalid --> ConfigCreation: Fix and retry
    
    Valid --> InUse: Passed to crawler
    InUse --> Cloning: Need variation
    InUse --> Serialization: Save configuration
    InUse --> Complete: Crawl finished
    
    Cloning --> Modified: clone() with updates
    Modified --> Valid: Validate changes
    
    Serialization --> Stored: dump() to dict
    Stored --> Restoration: load() from dict
    Restoration --> Valid: Recreate config object
    
    Complete --> [*]
    
    note right of BasicConfig : Minimal required settings
    note right of AdvancedConfig : Full feature configuration
    note right of TemplateConfig : Pre-built patterns
```

### Configuration Integration Architecture

```mermaid
graph TB
    subgraph "User Layer"
        U1[Configuration Creation]
        U2[Parameter Selection]
        U3[Pattern Application]
    end
    
    subgraph "Configuration Layer"
        C1[BrowserConfig]
        C2[CrawlerRunConfig]
        C3[LLMConfig]
        C4[Config Validation]
        C5[Config Cloning]
    end
    
    subgraph "Crawler Engine"
        E1[Browser Management]
        E2[Page Navigation]
        E3[Content Processing]
        E4[Extraction Pipeline]
        E5[Result Generation]
    end
    
    subgraph "Output Layer"
        O1[CrawlResult Assembly]
        O2[Data Formatting]
        O3[File Generation]
        O4[Metadata Collection]
    end
    
    U1 --> C1
    U2 --> C2
    U3 --> C3
    
    C1 --> C4
    C2 --> C4
    C3 --> C4
    
    C4 --> E1
    C2 --> E2
    C2 --> E3
    C3 --> E4
    
    E1 --> E2
    E2 --> E3
    E3 --> E4
    E4 --> E5
    
    E5 --> O1
    O1 --> O2
    O2 --> O3
    O3 --> O4
    
    C5 -.-> C1
    C5 -.-> C2
    C5 -.-> C3
    
    style U1 fill:#e1f5fe
    style C4 fill:#fff3e0
    style E4 fill:#f3e5f5
    style O4 fill:#c8e6c9
```

### Configuration Best Practices Flow

```mermaid
flowchart TD
    A[Configuration Planning] --> B{Performance Priority?}
    
    B -->|Speed| C[Fast Config Pattern]
    B -->|Quality| D[Comprehensive Config Pattern]
    B -->|Stealth| E[Stealth Config Pattern]
    B -->|Balanced| F[Standard Config Pattern]
    
    C --> C1[Enable caching]
    C --> C2[Disable heavy features]
    C --> C3[Use text_mode]
    C1 --> G[Apply Configuration]
    C2 --> G
    C3 --> G
    
    D --> D1[Enable all processing]
    D --> D2[Use content filters]
    D --> D3[Capture everything]
    D1 --> G
    D2 --> G
    D3 --> G
    
    E --> E1[Rotate user agents]
    E --> E2[Use proxies]
    E --> E3[Simulate human behavior]
    E1 --> G
    E2 --> G
    E3 --> G
    
    F --> F1[Balanced timeouts]
    F --> F2[Selective processing]
    F --> F3[Smart caching]
    F1 --> G
    F2 --> G
    F3 --> G
    
    G --> H[Test Configuration]
    H --> I{Results Satisfactory?}
    
    I -->|Yes| J[Production Ready]
    I -->|No| K[Adjust Parameters]
    
    K --> L[Clone and Modify]
    L --> H
    
    J --> M[Deploy with Confidence]
    
    style A fill:#e1f5fe
    style J fill:#c8e6c9
    style M fill:#e8f5e8
```

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.