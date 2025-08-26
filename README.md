flowchart TD
    A[User Submits Bug Report] --> B[BugFiner AI Analyzes Description]
    B --> C{Bug Repro Steps Identified?}
    C -- Yes --> D[Automated Browser Test]
    C -- No --> E[Request More Info]
    D --> F[Capture Logs & Screenshots]
    F --> G[Generate Markdown Report]
    G --> H[Dashboard Displays Report]
    H --> I[Developer Reviews & Fixes Bug]

    style A fill:#1f4068,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style B fill:#162447,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style C fill:#1a1a2e,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style D fill:#1f4068,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style E fill:#302b63,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style F fill:#162447,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style G fill:#1a1a2e,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style H fill:#1f4068,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
    style I fill:#302b63,stroke:#88c0d0,stroke-width:2px,color:#e0e0e0
