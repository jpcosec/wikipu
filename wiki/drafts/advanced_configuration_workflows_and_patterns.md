---
identity:
  node_id: "doc:wiki/drafts/advanced_configuration_workflows_and_patterns.md"
  node_type: "concept"
edges:
  - {target_id: "raw:raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md", relation_type: "documents"}
---

Visual representations of advanced Crawl4AI configuration strategies, proxy management, session handling, and identity-based crawling patterns.

## Details

Visual representations of advanced Crawl4AI configuration strategies, proxy management, session handling, and identity-based crawling patterns.

### User Agent and Anti-Detection Strategy Flow

```mermaid
flowchart TD
    A[Start Configuration] --> B{Detection Avoidance Needed?}
    
    B -->|No| C[Standard User Agent]
    B -->|Yes| D[Anti-Detection Strategy]
    
    C --> C1[Static user_agent string]
    C1 --> Z[Basic Configuration]
    
    D --> E{User Agent Strategy}
    E -->|Random| F[user_agent_mode: random]
    E -->|Static Custom| G[Custom user_agent string]
    E -->|Platform Specific| H[Generator Config]
    
    F --> I[Configure Generator]
    H --> I
    I --> I1[Platform: windows/macos/linux]
    I1 --> I2[Browser: chrome/firefox/safari]
    I2 --> I3[Device: desktop/mobile/tablet]
    
    G --> J[Behavioral Simulation]
    I3 --> J
    
    J --> K{Enable Simulation?}
    K -->|Yes| L[simulate_user: True]
    K -->|No| M[Standard Behavior]
    
    L --> N[override_navigator: True]
    N --> O[Configure Delays]
    O --> O1[mean_delay: 1.5]
    O1 --> O2[max_range: 2.0]
    O2 --> P[Magic Mode]
    
    M --> P
    P --> Q{Auto-Handle Patterns?}
    Q -->|Yes| R[magic: True]
    Q -->|No| S[Manual Handling]
    
    R --> T[Complete Anti-Detection Setup]
    S --> T
    Z --> T
    
    style D fill:#ffeb3b
    style T fill:#c8e6c9
    style L fill:#ff9800
    style R fill:#9c27b0
```

### Proxy Configuration and Rotation Architecture

```mermaid
graph TB
    subgraph "Proxy Configuration Types"
        A[Single Proxy] --> A1[ProxyConfig object]
        B[Proxy String] --> B1[from_string method]
        C[Environment Proxies] --> C1[from_env method]
        D[Multiple Proxies] --> D1[ProxyRotationStrategy]
    end
    
    subgraph "ProxyConfig Structure"
        A1 --> E[server: URL]
        A1 --> F[username: auth]
        A1 --> G[password: auth]
        A1 --> H[ip: extracted]
    end
    
    subgraph "Rotation Strategies"
        D1 --> I[round_robin]
        D1 --> J[random]
        D1 --> K[least_used]
        D1 --> L[failure_aware]
    end
    
    subgraph "Configuration Flow"
        M[CrawlerRunConfig] --> N[proxy_config]
        M --> O[proxy_rotation_strategy]
        N --> P[Single Proxy Usage]
        O --> Q[Multi-Proxy Rotation]
    end
    
    subgraph "Runtime Behavior"
        P --> R[All requests use same proxy]
        Q --> S[Requests rotate through proxies]
        S --> T[Health monitoring]
        T --> U[Automatic failover]
    end
    
    style A1 fill:#e3f2fd
    style D1 fill:#f3e5f5
    style M fill:#e8f5e8
    style T fill:#fff3e0
```

### Content Selection Strategy Comparison

```mermaid
sequenceDiagram
    participant Browser
    participant HTML as Raw HTML
    participant CSS as css_selector
    participant Target as target_elements
    participant Processor as Content Processor
    participant Output
    
    Note over Browser,Output: css_selector Strategy
    Browser->>HTML: Load complete page
    HTML->>CSS: Apply css_selector
    CSS->>CSS: Extract matching elements only
    CSS->>Processor: Process subset HTML
    Processor->>Output: Markdown + Extraction from subset
    
    Note over Browser,Output: target_elements Strategy  
    Browser->>HTML: Load complete page
    HTML->>Processor: Process entire page
    Processor->>Target: Focus on target_elements
    Target->>Target: Extract from specified elements
    Processor->>Output: Full page links/media + targeted content
    
    Note over CSS,Target: Key Difference
    Note over CSS: Affects entire processing pipeline
    Note over Target: Affects only content extraction
```

### Advanced wait_for Conditions Decision Tree

```mermaid
flowchart TD
    A[Configure wait_for] --> B{Condition Type?}
    
    B -->|CSS Element| C[CSS Selector Wait]
    B -->|JavaScript Condition| D[JS Expression Wait]
    B -->|Complex Logic| E[Custom JS Function]
    B -->|No Wait| F[Default domcontentloaded]
    
    C --> C1["wait_for: 'css:.element'"]
    C1 --> C2[Element appears in DOM]
    C2 --> G[Continue Processing]
    
    D --> D1["wait_for: 'js:() => condition'"]
    D1 --> D2[JavaScript returns true]
    D2 --> G
    
    E --> E1[Complex JS Function]
    E1 --> E2{Multiple Conditions}
    E2 -->|AND Logic| E3[All conditions true]
    E2 -->|OR Logic| E4[Any condition true]
    E2 -->|Custom Logic| E5[User-defined logic]
    
    E3 --> G
    E4 --> G
    E5 --> G
    
    F --> G
    
    G --> H{Timeout Reached?}
    H -->|No| I[Page Ready]
    H -->|Yes| J[Timeout Error]
    
    I --> K[Begin Content Extraction]
    J --> L[Handle Error/Retry]
    
    style C1 fill:#e8f5e8
    style D1 fill:#fff3e0
    style E1 fill:#ffeb3b
    style I fill:#c8e6c9
    style J fill:#ffcdd2
```

### Session Management Lifecycle

```mermaid
stateDiagram-v2
    [*] --> SessionCreate
    
    SessionCreate --> SessionActive: session_id provided
    SessionCreate --> OneTime: no session_id
    
    SessionActive --> BrowserLaunch: First arun() call
    BrowserLaunch --> PageLoad: Navigate to URL
    PageLoad --> JSExecution: Execute js_code
    JSExecution --> ContentExtract: Extract content
    ContentExtract --> SessionHold: Keep session alive
    
    SessionHold --> ReuseSession: Subsequent arun() calls
    ReuseSession --> JSOnlyMode: js_only=True
    ReuseSession --> NewNavigation: js_only=False
    
    JSOnlyMode --> JSExecution: Execute JS in existing page
    NewNavigation --> PageLoad: Navigate to new URL
    
    SessionHold --> SessionKill: kill_session() called
    SessionHold --> SessionTimeout: Timeout reached
    SessionHold --> SessionError: Error occurred
    
    SessionKill --> SessionCleanup
    SessionTimeout --> SessionCleanup
    SessionError --> SessionCleanup
    SessionCleanup --> [*]
    
    OneTime --> BrowserLaunch
    ContentExtract --> OneTimeCleanup: No session_id
    OneTimeCleanup --> [*]
    
    note right of SessionActive : Persistent browser context
    note right of JSOnlyMode : Reuse existing page
    note right of OneTime : Temporary browser instance
```

### Identity-Based Crawling Configuration Matrix

```mermaid
graph TD
    subgraph "Geographic Identity"
        A[Geolocation] --> A1[latitude/longitude]
        A2[Timezone] --> A3[timezone_id]
        A4[Locale] --> A5[language/region]
    end
    
    subgraph "Browser Identity"
        B[User Agent] --> B1[Platform fingerprint]
        B2[Navigator Properties] --> B3[override_navigator]
        B4[Headers] --> B5[Accept-Language]
    end
    
    subgraph "Behavioral Identity"
        C[Mouse Simulation] --> C1[simulate_user]
        C2[Timing Patterns] --> C3[mean_delay/max_range]
        C4[Interaction Patterns] --> C5[Human-like behavior]
    end
    
    subgraph "Configuration Integration"
        D[CrawlerRunConfig] --> A
        D --> B
        D --> C
        
        D --> E[Complete Identity Profile]
        
        E --> F[Geographic Consistency]
        E --> G[Browser Consistency]
        E --> H[Behavioral Consistency]
    end
    
    F --> I[Paris, France Example]
    I --> I1[locale: fr-FR]
    I --> I2[timezone: Europe/Paris]
    I --> I3[geolocation: 48.8566, 2.3522]
    
    G --> J[Windows Chrome Example]
    J --> J1[platform: windows]
    J --> J2[browser: chrome]
    J --> J3[user_agent: matching pattern]
    
    H --> K[Human Simulation]
    K --> K1[Random delays]
    K --> K2[Mouse movements]
    K --> K3[Navigation patterns]
    
    style E fill:#ff9800
    style I fill:#e3f2fd
    style J fill:#f3e5f5
    style K fill:#e8f5e8
```

### Multi-Step Crawling Sequence Flow

```mermaid
sequenceDiagram
    participant User
    participant Crawler
    participant Session as Browser Session
    participant Page1 as Login Page
    participant Page2 as Dashboard
    participant Page3 as Data Pages
    
    User->>Crawler: Step 1 - Login
    Crawler->>Session: Create session_id="user_session"
    Session->>Page1: Navigate to login
    Page1->>Page1: Execute login JS
    Page1->>Page1: Wait for dashboard redirect
    Page1-->>Crawler: Login complete
    
    User->>Crawler: Step 2 - Navigate dashboard
    Note over Crawler,Session: Reuse existing session
    Crawler->>Session: js_only=True (no page reload)
    Session->>Page2: Execute navigation JS
    Page2->>Page2: Wait for data table
    Page2-->>Crawler: Dashboard ready
    
    User->>Crawler: Step 3 - Extract data pages
    loop For each page 1-5
        Crawler->>Session: js_only=True
        Session->>Page3: Click page button
        Page3->>Page3: Wait for page active
        Page3->>Page3: Extract content
        Page3-->>Crawler: Page data
    end
    
    User->>Crawler: Cleanup
    Crawler->>Session: kill_session()
    Session-->>Crawler: Session destroyed
```

### Configuration Import and Usage Patterns

```mermaid
graph LR
    subgraph "Main Package Imports"
        A[crawl4ai] --> A1[AsyncWebCrawler]
        A --> A2[BrowserConfig]
        A --> A3[CrawlerRunConfig]
        A --> A4[LLMConfig]
        A --> A5[CacheMode]
        A --> A6[ProxyConfig]
        A --> A7[GeolocationConfig]
    end
    
    subgraph "Strategy Imports"
        A --> B1[JsonCssExtractionStrategy]
        A --> B2[LLMExtractionStrategy]
        A --> B3[DefaultMarkdownGenerator]
        A --> B4[PruningContentFilter]
        A --> B5[RegexChunking]
    end
    
    subgraph "Configuration Assembly"
        C[Configuration Builder] --> A2
        C --> A3
        C --> A4
        
        A2 --> D[Browser Environment]
        A3 --> E[Crawl Behavior]
        A4 --> F[LLM Integration]
        
        E --> B1
        E --> B2
        E --> B3
        E --> B4
        E --> B5
    end
    
    subgraph "Runtime Flow"
        G[Crawler Instance] --> D
        G --> H[Execute Crawl]
        H --> E
        H --> F
        H --> I[CrawlResult]
    end
    
    style A fill:#e3f2fd
    style C fill:#fff3e0
    style G fill:#e8f5e8
    style I fill:#c8e6c9
```

### Advanced Configuration Decision Matrix

```mermaid
flowchart TD
    A[Advanced Configuration Needed] --> B{Primary Use Case?}
    
    B -->|Bot Detection Avoidance| C[Anti-Detection Setup]
    B -->|Geographic Simulation| D[Identity-Based Config]
    B -->|Multi-Step Workflows| E[Session Management]
    B -->|Network Reliability| F[Proxy Configuration]
    B -->|Content Precision| G[Selector Strategy]
    
    C --> C1[Random User Agents]
    C --> C2[Behavioral Simulation]
    C --> C3[Navigator Override]
    C --> C4[Magic Mode]
    
    D --> D1[Geolocation Setup]
    D --> D2[Locale Configuration]
    D --> D3[Timezone Setting]
    D --> D4[Browser Fingerprinting]
    
    E --> E1[Session ID Management]
    E --> E2[JS-Only Navigation]
    E --> E3[Shared Data Context]
    E --> E4[Session Cleanup]
    
    F --> F1[Single Proxy]
    F --> F2[Proxy Rotation]
    F --> F3[Failover Strategy]
    F --> F4[Health Monitoring]
    
    G --> G1[css_selector for Subset]
    G --> G2[target_elements for Focus]
    G --> G3[excluded_selector for Removal]
    G --> G4[Hierarchical Selection]
    
    C1 --> H[Production Configuration]
    C2 --> H
    C3 --> H
    C4 --> H
    D1 --> H
    D2 --> H
    D3 --> H
    D4 --> H
    E1 --> H
    E2 --> H
    E3 --> H
    E4 --> H
    F1 --> H
    F2 --> H
    F3 --> H
    F4 --> H
    G1 --> H
    G2 --> H
    G3 --> H
    G4 --> H
    
    style H fill:#c8e6c9
    style C fill:#ff9800
    style D fill:#9c27b0
    style E fill:#2196f3
    style F fill:#4caf50
    style G fill:#ff5722
```

Generated from `raw/docs_postulador_refactor/future_docs/crawl4ai_custom_context (1).md`.