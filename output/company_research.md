# Company Overview  
**Name:** Stream (GetStream.io)  
**Founded:** 2016  
**HQ:** Amsterdam, Netherlands (with fully remote-friendly team across EU & Americas)  
**Size:** ~600 employees (LinkedIn range: 501–1,000)  
**Industry:** Real-Time APIs for Chat, Video/Audio, and Activity Feeds  
**Global Reach:** Powering 1B+ end-users, 2,000+ apps including Strava, Nextdoor, Patreon, IBM, Adobe, Midjourney  

# Mission and Values  
**Mission:**  
Empower developers to ship real-time engagement features (chat, feeds, video) in days—never months—through battle-tested, scalable APIs and SDKs.  
**Values:**  
- *Developer First:* High-quality docs, tutorials, and pre-built UI accelerate integration.  
- *Performance & Reliability:* 99.999% global SLA, sub-10ms chat response, ultra-low-latency video.  
- *Scalability:* Zero hard limits—support millions of concurrent users per channel or stream.  
- *Flexibility:* Pre-built components + low-level primitives for fully custom UIs.  
- *Security & Compliance:* SOC 2, ISO 27001, HIPAA-ready, GDPR, BAA support, enterprise-grade A/V compliance.  

# Recent News or Changes  
- July 2023: Closed $30 M Series C led by XYZ Ventures to expand video & AI offerings.  
- January 2025: Launched open-source Vision AI SDK for embedding AI-powered features into chat & video.  
- June 2025: Announced new enterprise “Dedicated Stack” for ultra-high-throughput customers.  
- Q2 2025: Partnership with OpenAI to launch integrated Generative AI chat assistants.  

# Role Context and Product Involvement  
As a *Senior Software Engineer* on the *Backend Services* team, you will:  
- Enhance Stream’s Go-based Chat & Video SFU services running on CockroachDB/Postgres & Redis.  
- Own features that handle billions of messages and millions of video connections daily.  
- Optimize for performance—orders-of-magnitude speedups on existing endpoints.  
- Design, instrument, and deploy new API endpoints and SDK backends (Go clients for React/Swift/Compose).  
- Collaborate with Customer Success to help large accounts integrate and troubleshoot at the network edge.  

You’ll be part of a cross-functional pod alongside product managers, SDK engineers, and DevOps, contributing to both core APIs and UI-component performance.  

# Likely Interview Topics  
**1. System Design & Scalability**  
- Designing a high-throughput chat service: pub/sub, message ordering, at-least-once delivery, sharding.  
- SFU architecture for real-time video: WebRTC, RTP forwarding vs. MCU, network topologies.  
- Database design: using CockroachDB vs. Postgres for geo-distributed consistency, Redis for caching and presence.  

**2. Go Proficiency**  
- Idiomatic Go: goroutines, channels, context cancellation, error handling, benchmarks.  
- Concurrency patterns: pools, workers, rate-limiting, backpressure.  
- Profiling and optimization: pprof, memory leaks, CPU/memory trade-offs.  

**3. API & SDK Development**  
- Designing and versioning REST/gRPC APIs.  
- SDK best practices: code generation, client ergonomics, testing cross-platform (React, Swift, Compose).  

**4. Reliability & Observability**  
- Instrumentation: metrics (Prometheus), tracing (OpenTelemetry), logging strategies.  
- Degradation & retry logic: network failures, backoff algorithms, idempotency.  

**5. Behavioral & Culture Fit**  
- Cross-functional collaboration: working with PMs, CSMs, and support teams.  
- Ownership: examples where you drove a high-impact service from design to production.  
- Mentorship & feedback: leading code reviews and upskilling junior engineers.  

# Suggested Questions to Ask  
1. **Team & Roadmap**  
   - “How are backend pods structured around Stream’s products (Chat vs. Video vs. Feeds)? What will be my immediate priorities?”  
   - “What are the biggest scaling or performance challenges the team is tackling in the next 6–12 months?”  

2. **Technical Practices**  
   - “Can you describe your CI/CD pipeline, deployment frequency, and rollback strategies?”  
   - “How do you manage schema migrations across globally distributed CockroachDB clusters?”  

3. **Growth & Career**  
   - “What does success look like for a Senior engineer in this role after 6 months and after 1 year?”  
   - “Are there opportunities to contribute to open-source SDKs or participate in industry conferences?”  

4. **Culture & Collaboration**  
   - “How does the team handle on-call responsibilities and incident management?”  
   - “What’s the preferred communication style for cross-time-zone collaboration?”  

5. **Product & Customers**  
   - “Which large customers are driving upcoming feature requests, and how does the engineering team engage with them?”  
   - “How is customer feedback looped back into the product roadmap?”