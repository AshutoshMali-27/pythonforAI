# Senior Agentic AI Engineer Roadmap
### A long-term curriculum from a .NET / enterprise background to Senior Agentic AI Architect

---

## Table of Contents

- [How to Use This Roadmap](#how-to-use-this-roadmap)
- [Knowledge Classification](#knowledge-classification)
- [Roadmap at a Glance](#roadmap-at-a-glance)
- [Level 1 — Foundation](#level-1--foundation)
  - [Chapter 1 — Python for AI Engineering](#chapter-1--python-for-ai-engineering)
  - [Chapter 2 — FastAPI and Async Service Foundations](#chapter-2--fastapi-and-async-service-foundations-postgres-redis-queues)
- [Level 2 — AI Application Developer](#level-2--ai-application-developer)
  - [Chapter 3 — LLM Fundamentals and Provider APIs](#chapter-3--llm-fundamentals-and-provider-apis)
  - [Chapter 4 — Prompt Engineering, Structured Outputs and Tool Calling](#chapter-4--prompt-engineering-structured-outputs-and-tool-calling)
  - [Chapter 5 — Embeddings, Vector Databases and RAG](#chapter-5--embeddings-vector-databases-and-rag)
  - [Chapter 6 — Advanced RAG](#chapter-6--advanced-rag)
- [Level 3 — Agentic AI Developer](#level-3--agentic-ai-developer)
  - [Chapter 7 — Agents from First Principles](#chapter-7--agents-from-first-principles-no-framework)
  - [Chapter 8 — State, Memory and Human-in-the-Loop](#chapter-8--state-memory-and-human-in-the-loop)
  - [Chapter 9 — LangChain and LangGraph](#chapter-9--langchain-and-langgraph)
  - [Chapter 10 — Model Context Protocol (MCP)](#chapter-10--model-context-protocol-mcp)
- [Level 4 — Advanced Agent Engineer](#level-4--advanced-agent-engineer)
  - [Chapter 11 — Planning, Reasoning and Multi-Agent Systems](#chapter-11--planning-reasoning-and-multi-agent-systems)
  - [Chapter 12 — Agentic System Design and Distributed Execution](#chapter-12--agentic-system-design-and-distributed-execution)
  - [Chapter 13 — Agentic AI Security Track](#chapter-13--agentic-ai-security-track)
  - [Chapter 14 — LLM Evaluation and Observability Track](#chapter-14--llm-evaluation-and-observability-track)
- [Level 5 — Production AI Engineer](#level-5--production-ai-engineer)
  - [Chapter 15 — Model Strategy](#chapter-15--model-strategy-routing-local-and-cloud-llms-serving-caching-cost)
  - [Chapter 16 — AI Infrastructure and Deployment Track](#chapter-16--ai-infrastructure-and-deployment-track)
- [Level 6 — Senior Agentic AI Architect](#level-6--senior-agentic-ai-architect)
  - [Chapter 17 — Enterprise AI Architecture, Patterns and System Design](#chapter-17--enterprise-ai-architecture-patterns-and-system-design)
- [Senior Engineer Skill Matrix](#senior-engineer-skill-matrix)
- [Portfolio Strategy](#portfolio-strategy)
- [Interview Preparation](#interview-preparation)
- [Common Mistakes and How to Avoid Them](#common-mistakes-and-how-to-avoid-them)
- [Suggested Timeline](#suggested-timeline-1015-hrsweek)
- [Progress Tracker](#progress-tracker)

---

## How to Use This Roadmap

You already know how to build systems: APIs, databases, microservices, Docker, enterprise constraints. What you're adding is a new kind of component: **a probabilistic, non-deterministic reasoning engine that can take actions.** Almost everything senior-level in agentic AI comes from one question:

> *How do I build reliable, secure, observable, affordable systems around a component that is sometimes wrong, sometimes slow, sometimes manipulated, and always expensive?*

### Mentoring principles

1. **Mechanism before framework.** You'll build a RAG pipeline and an agent loop by hand before touching LangChain or LangGraph. Frameworks change every six months; the mechanisms underneath them change slowly.
2. **Evaluation is the unit test of AI.** From Chapter 4 onward, every project has an eval set. Without evals you cannot improve a system you can't measure.
3. **Security and observability are built in from the start.** They get dedicated chapters, but each project applies them from day one.
4. **Your .NET experience is an asset.** Dependency injection, typed contracts, layered architecture, resilience patterns (Polly), and distributed systems thinking all transfer directly. The gaps are Python idioms, ML intuition, and AI-specific failure modes.

### Per-chapter learning structure

**Chapter → Concepts → Deep Technical Understanding → Tools → Architecture → Hands-on Implementation → Project → Testing → Production Considerations → Senior-Level Expectations**

We study **one chapter at a time**, moving on only when you say so.

**Suggested pace:** 10–15 hrs/week gives roughly 12–15 months end to end. Don't rush Levels 2–3; they're the core.

---

## Knowledge Classification

| Category | Items |
|---|---|
| **Understand deeply** (first principles; explain it on a whiteboard) | How LLMs generate text (tokens, attention, context, sampling); the context window as the fundamental constraint; embeddings and similarity search; the RAG pipeline end to end; the agent loop (reason → act → observe); tool-calling mechanics; state and memory design; evaluation methodology; prompt injection and the trust-boundary model; durable execution, idempotency, retries; async Python; cost and latency economics of inference; AI system design trade-offs |
| **Working knowledge** (build with it, read the docs as needed) | FastAPI, Pydantic, LangGraph, LangChain (core abstractions only), MCP SDKs, one vector DB deeply plus awareness of others, pgvector, Redis, Postgres, Docker, Kubernetes basics, one observability platform (Langfuse/LangSmith/Phoenix), one eval framework (Ragas/DeepEval/promptfoo), vLLM and Ollama, one cloud's AI stack (Azure AI Foundry/Azure OpenAI *or* AWS Bedrock), Terraform basics, GitHub Actions |
| **Optional / situational** | Kafka (only for high-throughput event-driven systems), Temporal (excellent but not universal), fine-tuning (LoRA/QLoRA), SGLang/TGI/TensorRT-LLM, GraphRAG/Neo4j, CrewAI/AutoGen-style multi-agent frameworks, Ray, quantization internals, training from scratch |
| **Currently important in industry** (as of late 2026; verify, since this space moves monthly) | MCP, LangGraph, structured outputs, reasoning models and test-time compute, model gateways/routing (LiteLLM, Portkey, cloud gateways), OpenTelemetry for GenAI, LLM-as-judge evaluation, OWASP Top 10 for LLM Apps and agentic security guidance, prompt caching, provider agent SDKs (OpenAI Agents SDK, Claude Agent SDK, Pydantic AI), pgvector-in-Postgres as the default vector store, human-in-the-loop approvals for agent actions |

---

## Roadmap at a Glance

| Level | Chapters | Flagship project |
|---|---|---|
| **1. Foundation** | 1. Python for AI Engineering · 2. FastAPI and async service foundations | Foundation projects F1, F2 |
| **2. AI Application Developer** | 3. LLM Fundamentals and Provider APIs · 4. Prompt Engineering, Structured Outputs and Tool Calling · 5. Embeddings, Vector DBs and RAG · 6. Advanced RAG | P1 Simple LLM app · P2 Production API AI app · P3 RAG app · P3+ |
| **3. Agentic AI Developer** | 7. Agents from First Principles · 8. State, Memory and HITL · 9. LangChain and LangGraph · 10. MCP | P4 Tool-using agent · P5 Stateful agent · P6 LangGraph workflow · P7 MCP application |
| **4. Advanced Agent Engineer** | 11. Planning, Reasoning and Multi-Agent · 12. Agentic System Design · 13. **Security track** · 14. **Evaluation and observability track** | P8 Multi-agent system · P6+ · S1 · E1 |
| **5. Production AI Engineer** | 15. Model Strategy · 16. **Infrastructure and deployment track** | M1 · I1 · **P9 Production-grade agent platform** |
| **6. Senior Agentic AI Architect** | 17. Enterprise AI Architecture and Patterns | **P10 Enterprise-grade autonomous AI application** |

---

# LEVEL 1 — FOUNDATION

**Goal:** become fluent in Python as a *production* language, not a scripting language, and build the async service skeleton every later project uses.

## Chapter 1 — Python for AI Engineering

**Why it matters:** The entire AI ecosystem (SDKs, eval tools, serving, data tooling) is Python-first. LLM apps are I/O-bound and concurrency-heavy, so weak async skills produce slow, fragile agents.

### Concepts to learn
- Python's model versus C#: dynamic typing with gradual static typing, duck typing, the GIL (and free-threaded Python's status), the data model (dunder methods), generators and iterators.
- **Type hints plus mypy/pyright** to keep compile-time safety: `TypedDict`, `Protocol` (structural interfaces), generics, `Literal`, `Annotated`.
- **Pydantic v2:** validation, serialization, settings management — the backbone of structured LLM output later.
- **asyncio in depth:** event loop, `async`/`await`, `gather`, `TaskGroup`, semaphores, cancellation, timeouts (`asyncio.timeout`), and why blocking calls inside async code are catastrophic.
  - .NET mapping: `Task` ≈ coroutine/Task, `SemaphoreSlim` ≈ `asyncio.Semaphore`, `CancellationToken` ≈ task cancellation.
- `httpx` (async HTTP), `tenacity` (retries — the Polly equivalent), context managers, decorators, dataclasses.
- Tooling: **uv**, `pyproject.toml`, ruff, pytest + pytest-asyncio, structlog.
- Data basics: JSON handling, numpy arrays (vectors), pandas at a working level.

### Deep understanding a senior needs
When async helps (network I/O fan-out) and when it doesn't (CPU-bound work → process pools); bounding concurrency to respect provider rate limits; how exceptions propagate in task groups.

### Project F1 — Async Multi-Source Content Fetcher Library
- **Problem:** Fetch and normalize content from 50+ URLs/APIs concurrently with bounded concurrency, retries with backoff and jitter, per-request timeouts, and typed results.
- **Architecture:** Library package → Protocol-based `Source` adapters → async orchestrator with semaphore → Pydantic result models.
- **Technologies:** Python 3.12+, uv, httpx, tenacity, Pydantic, structlog, pytest.
- **Features:** rate limiting, partial-failure handling, cancellation, CLI entrypoint.
- **Learning outcomes:** idiomatic async Python, typed design, packaging.
- **Security:** URL allowlisting, response size limits, no secrets in logs.
- **Testing:** unit tests with mocked transports (`respx`), concurrency tests, 90% coverage, mypy strict passing.
- **Deployment:** installable package; runs in a container.
- **Senior signal:** clean abstractions, strict typing, resilience designed rather than bolted on. Becomes your ingestion layer in Chapter 5.

---

## Chapter 2 — FastAPI and Async Service Foundations (Postgres, Redis, Queues)

**Why it matters:** Every AI system is ultimately a service: it streams responses, runs long jobs, stores state, and enforces auth. FastAPI is the industry-default Python AI API framework.

### Concepts to learn
- FastAPI: routing, dependency injection (vs ASP.NET Core DI), Pydantic request/response models, lifespan events, middleware, exception handlers, OpenAPI.
- **Streaming:** `StreamingResponse`, Server-Sent Events. LLM UX depends on token streaming.
- WebSockets for interactive agents.
- Background work: why `BackgroundTasks` isn't a queue; real queues with **Celery, arq, or Dramatiq** on Redis; task status APIs (202 Accepted + polling or webhooks).
- **PostgreSQL** from Python: SQLAlchemy 2.0 async or SQLModel, Alembic, connection pooling (asyncpg), JSONB for agent state.
- **Redis:** caching, rate limiting (token bucket / sliding window), distributed locks, pub/sub, streams.
- AuthN/AuthZ in FastAPI: OAuth2/OIDC with JWT, scopes, dependency-based authorization.
- pydantic-settings, 12-factor config, health/readiness endpoints, Uvicorn/Gunicorn workers.

### Deep understanding
Sync vs async endpoints (a sync `def` runs in a threadpool; a blocking call in an `async def` stalls the loop); why long LLM work belongs off the request path; connection pool sizing under concurrency.

### Project F2 — Async Job Processing API
- **Problem:** An API that accepts document-processing jobs, queues them, processes them asynchronously, and exposes status plus SSE progress streaming.
- **Architecture:** FastAPI → Postgres (jobs table) → Redis (queue + rate limiter) → worker(s) → SSE progress via Redis pub/sub.
- **Technologies:** FastAPI, SQLAlchemy async, Alembic, Redis, arq/Celery, Docker Compose.
- **Components:** API service, worker service, migration job, auth dependency.
- **Features:** JWT auth, per-user rate limits, idempotency keys on job submission, retries with dead-letter handling.
- **Learning outcomes:** the service skeleton reused for every AI project.
- **Security:** JWT validation, tenant scoping on every query, input size limits.
- **Testing:** pytest with `httpx.AsyncClient`, testcontainers for Postgres/Redis, idempotency tests.
- **Deployment:** Docker Compose; containerized with health checks.
- **Senior signal:** idempotency, dead-letter queues, correct async boundaries — the resilience vocabulary agentic systems depend on.

---

# LEVEL 2 — AI APPLICATION DEVELOPER

**Goal:** understand how LLMs behave, integrate them reliably, and ground them in your data.

## Chapter 3 — LLM Fundamentals and Provider APIs

**Why it matters:** Almost every production bug in AI apps traces back to a misunderstanding of how models work: context limits, tokenization, sampling, or statelessness. You don't need to train models, but you must reason about them like a systems engineer reasons about a database engine.

### Concepts (deep)
- **Tokens and tokenization** (BPE): why cost, limits, and some failures (counting letters, arithmetic) are token-level phenomena.
- **Transformer intuition:** embeddings → self-attention → next-token prediction. The model is a function from context to a probability distribution over the next token.
- **Inference mechanics:** prefill vs decode, KV cache, why output tokens cost more and are slower, **TTFT** and **TPOT/ITL**.
- **Sampling:** temperature, top-p, top-k, determinism limits (temperature 0 isn't guaranteed deterministic), logprobs.
- **Context windows:** "lost in the middle," context rot, why bigger context doesn't replace retrieval.
- **Model lifecycle:** pretraining → instruction tuning → RLHF/RLAIF → reasoning models (test-time compute, thinking tokens). Why models hallucinate: they optimize plausibility, not truth.
- **LLMs are stateless.** "Conversation" is resending history — the root of every memory design later.

### Provider APIs (working knowledge)
- Message formats (system/user/assistant/tool) across OpenAI, Anthropic, Google, Azure OpenAI/Bedrock.
- Streaming, usage fields, stop reasons, error types (429, 5xx, overloaded, context-length errors).
- **Prompt caching** and its cost/latency impact.
- Multimodal inputs (images/PDFs).
- Provider abstraction: LiteLLM vs your own thin adapter layer — understand the trade-offs.

### Architecture
A **provider abstraction layer** from day one: `LLMClient` interface → provider adapters → retry/timeout/fallback policy → usage accounting.

### Project P1 — Simple LLM Application: Multi-Provider Technical Document Assistant
- **Problem:** Summarize, explain, and Q&A over a pasted technical document across at least two providers, with streaming output and cost reporting.
- **Architecture:** CLI/FastAPI → provider abstraction → OpenAI/Anthropic/Azure adapters; token counting before sending; map-reduce summarization for oversized docs.
- **Technologies:** Python, httpx or official SDKs, token counters, FastAPI, Rich.
- **Features:** streaming, per-request cost/latency report, provider fallback on 429/5xx, configurable temperature, context-overflow strategy.
- **Components:** provider adapters, token budgeter, summarization strategies, usage logger.
- **Learning outcomes:** token economics, streaming, provider differences.
- **Security:** API keys from env/secret store only, never logged; document content treated as untrusted.
- **Testing:** mock providers for unit tests; 10 docs with expected-quality checks (first informal eval).
- **Deployment:** container with env-based config.
- **Senior signal:** clean provider abstraction with fallback and cost accounting, not a raw SDK call in a route handler.

---

## Chapter 4 — Prompt Engineering, Structured Outputs and Tool Calling

**Why it matters:** Prompts are the new source code, structured outputs are the new API contract, and tool calling is the primitive every agent is built on.

### Concepts
- **Prompt engineering as engineering:** system prompts, clear instructions, few-shot examples, delimiters/XML tags, chain-of-thought vs reasoning models (don't over-prompt reasoning models), templates, versioning, prompts as testable artifacts.
- Failure modes: instruction drift, format breakage, sycophancy, over-refusal, brittleness across model versions.
- **Structured outputs:** JSON mode vs schema-constrained decoding vs "please return JSON"; Pydantic schemas; validation + repair/retry loops; the **Instructor** pattern.
- **Tool/function calling mechanics:** the model emits a structured *request*; your code executes it; the result is fed back. The model never runs anything. Tool schemas, descriptions as prompts, parallel tool calls, tool choice modes.
- Classification, extraction, routing as structured-output tasks (highest-ROI enterprise use cases).

### Deep understanding
Tool descriptions are part of the prompt — bad descriptions produce bad tool selection. Every structured output must be validated because the LLM is an untrusted input source.

### Project P2 — Production API-Based AI Application: Support Ticket Intelligence Service
- **Problem:** Classify, extract entities (product, severity, customer, account ID), draft responses, and route thousands of support tickets through a production API.
- **Architecture:** FastAPI → auth → validation → prompt registry (versioned templates) → LLM layer (from P1) with structured outputs → Pydantic validation + repair loop → Postgres (results, audit) → Redis (cache, rate limits) → async batch endpoint via queue (from F2).
- **Technologies:** FastAPI, Pydantic, Instructor or native structured outputs, Postgres, Redis, arq/Celery, Docker Compose.
- **Features:** sync single-ticket endpoint, async batch endpoint, SSE-streamed draft reply, tool call (`get_customer_tier`) against a mock CRM, prompt A/B flags, per-tenant token budget.
- **Components:** API, prompt registry, LLM gateway module, validator, worker, audit log.
- **Learning outcomes:** structured outputs in production, first tool call, prompt lifecycle management.
- **Security:** PII redaction before sending to providers, tenant isolation, output validation before downstream use, rate limiting.
- **Testing:** **golden dataset of 100 labeled tickets** → accuracy/F1, extraction exact-match, schema-validity rate; prompt regression tests in CI (promptfoo or pytest).
- **Deployment:** containerized; CI runs evals on prompt changes.
- **Senior signal:** prompt changes gated by eval results in CI; outputs treated as untrusted data.

---

## Chapter 5 — Embeddings, Vector Databases and RAG

**Why it matters:** LLMs don't know your company's data, and fine-tuning is the wrong tool for knowledge. RAG is the dominant enterprise pattern; most agents are RAG plus tools.

### Concepts
- **Embeddings:** dense vectors, cosine vs dot product, dimensionality, model choice (quality, cost, multilingual, max input), matryoshka embeddings; never mix embedding models in one index.
- **Vector search internals:** exact kNN vs ANN; **HNSW** (recall/latency/memory via `ef`/`M`), IVF, product quantization; metadata filtering (pre- vs post-filter).
- **Vector DBs:** **pgvector** (default for your stack), Qdrant, Weaviate, Pinecone, Milvus, Azure AI Search, OpenSearch — know selection criteria.
- **RAG pipeline:** ingestion → parsing (PDF/HTML/Office, tables) → cleaning → **chunking** (fixed, recursive, semantic, structure-aware) → embedding → indexing → retrieval → context assembly → generation with **citations**.
- Keyword search (BM25) and why pure vector search fails on IDs, codes, exact terms.

### Deep understanding
Retrieval quality caps answer quality — most "hallucination" in RAG is retrieval failure. Chunking is a data-modeling decision.

### Project P3 — RAG Application: Enterprise Knowledge Assistant with Citations
- **Problem:** Accurate answers from thousands of internal documents, with citations and document-level permissions.
- **Architecture:** Ingestion worker (uses F1) → parsers → chunker → embedder → Postgres + pgvector (chunks, metadata, ACLs) → query API: query rewrite → hybrid retrieval (pgvector + full-text/BM25) → permission filter → context builder → LLM answer with inline citations → SSE stream.
- **Technologies:** FastAPI, pgvector, an embedding model, unstructured/docling-style parsers, Redis, Docker Compose.
- **Features:** incremental re-indexing (content hashing), document-level ACL filtering, citation linking, "I don't know" when retrieval is weak, feedback endpoint.
- **Components:** ingestion pipeline, indexer, retriever, answer generator, feedback store.
- **Learning outcomes:** full RAG mechanics without a framework.
- **Security:** **ACL enforcement at retrieval time (never trust the LLM to hide data)**, indirect prompt injection in documents, PII in corpus.
- **Testing:** golden Q&A set (50–100) with expected source docs → recall@k, MRR, answer faithfulness.
- **Deployment:** API and ingestion worker as separate containers.
- **Senior signal:** permission-aware retrieval, incremental ingestion, retrieval measured separately from generation.

---

## Chapter 6 — Advanced RAG

**Why it matters:** Naive RAG demos well and fails in production. Advanced RAG is where engineering judgment shows.

### Concepts
- **Retrieval:** hybrid search with reciprocal rank fusion, **re-ranking** (cross-encoders, hosted rerankers), query rewriting, multi-query, HyDE, query decomposition.
- **Indexing:** parent-child / small-to-big chunks, contextual chunk headers ("contextual retrieval"), summaries as index units, tables and images, metadata extraction.
- **Agentic RAG:** the model decides whether, what, and how often to retrieve (bridge to Level 3).
- **GraphRAG** and knowledge graphs (optional; when entity relationships matter).
- Long-context vs RAG trade-offs; caching retrieved context; freshness and deletion ("right to be forgotten" in vector stores).
- **RAG evaluation:** context precision/recall, faithfulness/groundedness, answer relevance (Ragas, DeepEval); component-level vs end-to-end eval.

### Project P3+ — Eval-Driven RAG Optimization
- **Problem:** Improve P3 measurably with an experiment harness proving which techniques help on *your* data.
- **Architecture:** Experiment runner → config matrix (chunking × retrieval × reranker × prompt) → eval pipeline → results dashboard.
- **Technologies:** Ragas/DeepEval, a reranker, MLflow or a Postgres results store.
- **Features:** A/B comparison of ≥5 techniques, cost/latency per configuration, regression gate.
- **Learning outcomes:** evidence-based optimization instead of cargo-culting.
- **Security:** test injection-laden documents in the corpus.
- **Testing:** the harness is the test; add adversarial and unanswerable questions.
- **Deployment:** eval runs in CI on pipeline changes.
- **Senior signal:** a written report like "Reranking improved recall@5 from 0.71 to 0.86 at +180 ms p50; we shipped it."

---

# LEVEL 3 — AGENTIC AI DEVELOPER

**Goal:** build systems where the LLM decides what to do next — and control that power.

## Chapter 7 — Agents from First Principles (No Framework)

**Why it matters:** Every framework wraps the same loop. Build it yourself and you can debug any framework and decide when not to use one.

### Concepts
- **Workflow vs agent:** workflows have predefined code paths; agents choose dynamically. Most production value comes from workflows with bounded agentic steps. Spectrum: prompt chaining → routing → parallelization → orchestrator-workers → evaluator-optimizer → autonomous agent.
- **The agent loop:** LLM call → tool calls → execute → append observations → repeat until stop. ReAct, tool-result formats, parallel tool execution.
- **Termination and control:** max iterations, token/cost budgets, timeouts, loop detection.
- **Tool design (most underrated skill):** clear names/descriptions, narrow scopes, idempotent tools, recoverable error messages, pagination/truncation, read vs write tools.
- **Error recovery:** tool errors returned as observations, not loop-killing exceptions.
- Context management within a run: growing history, summarization, tool-output truncation.

### Project P4 — Tool-Using Agent: Cloud Operations Assistant (raw loop, no framework)
- **Problem:** On-call engineers ask "Why is checkout latency high?" The agent investigates via read-only tools: metrics, logs, deployments, runbook search (RAG from P3).
- **Architecture:** FastAPI → agent runner (your loop) → tool registry (typed Pydantic schemas + permission metadata) → executors (mock Prometheus/log/deploy APIs + runbook RAG) → step-by-step SSE stream → Postgres run log.
- **Technologies:** Python, provider SDK with tool calling, FastAPI, Pydantic, Postgres.
- **Features:** parallel tool calls, max-steps and budget limits, output truncation, structured final report, full trajectory log.
- **Components:** agent loop, tool registry, executors, budget manager, trajectory store.
- **Learning outcomes:** deep understanding of the agent loop and tool design.
- **Security:** read-only tools; schema-validated arguments; log content treated as untrusted (injection via log lines is real).
- **Testing:** scripted mock-LLM tests for loop logic; **trajectory evaluation** on 20 incident scenarios (right tools? correct conclusion? step count?).
- **Deployment:** container; configurable model.
- **Senior signal:** budgets, termination guarantees, recoverable tool errors, trajectory-level evaluation.

---

## Chapter 8 — State, Memory and Human-in-the-Loop

**Why it matters:** Real agents span conversations, sessions, and days. They must remember, pause, wait for approval, and resume — where AI meets classic state management.

### Concepts
- **Stateless vs stateful agents:** request-scoped vs persisted state; where state lives; horizontal scaling implications.
- **Memory types:** short-term (working context), long-term (facts, preferences), episodic (past runs), semantic (knowledge), procedural (learned instructions). Write policies: what, when, who decides. Retrieval as RAG over history.
- Memory hygiene: summarization, compaction, decay, conflicting facts, user-visible and deletable memory.
- **Checkpointing:** persisting state at each step for crash recovery and pausing.
- **HITL patterns:** approval gates before side effects, edit-and-approve, escalation on low confidence, interrupt/resume, approval timeouts.
- Risk tiering of actions: read → reversible write → irreversible/financial.

### Project P5 — Stateful Agent: Personal Engineering Assistant with Memory and Approvals
- **Problem:** An assistant that manages tasks, tickets, and calendar across sessions, remembers preferences, and requires approval for writes.
- **Architecture:** FastAPI (REST + WebSocket) → agent runtime → Postgres checkpoint store (JSONB) → long-term memory (pgvector) → approval service (pending actions + notifications) → tools (mock Jira/calendar/email).
- **Technologies:** FastAPI, Postgres/pgvector, Redis (session cache, locks), agent loop from P4.
- **Features:** multi-session threads, memory extraction + retrieval, "what do you remember about me" view with delete, approval queue, resume after restart, per-thread locking.
- **Learning outcomes:** state persistence, memory design, interrupt/resume.
- **Security:** user-scoped memory isolation, approvals as an audit trail, write tools require an approval token bound to the exact arguments.
- **Testing:** crash-and-resume tests, memory recall evals, approval-bypass tests.
- **Deployment:** API + worker, persistent Postgres.
- **Senior signal:** approvals bound to exact parameters, crash-resumability, deletable memory.

---

## Chapter 9 — LangChain and LangGraph

**Why it matters:** LangGraph is among the most widely adopted frameworks for controllable, stateful agent orchestration. Having built the primitives, the framework becomes a productivity tool instead of a black box.

### Concepts
- **LangChain (working knowledge only):** chat model interface, messages, tools, retrievers, output parsers, integrations. Use it for integrations; avoid abstraction chains you can't debug.
- **LangGraph (deep working knowledge):** graphs as state machines, typed `State` with reducers, nodes, conditional edges, cycles, **checkpointers** (Postgres), threads, **interrupts** for HITL, time travel/replay, subgraphs, streaming modes, `Send` API for map-reduce, prebuilt ReAct agents vs custom graphs.
- Map every LangGraph feature to what you built in Chapters 7–8.
- Compare critically: OpenAI Agents SDK, Claude Agent SDK, Pydantic AI, LlamaIndex workflows, plain code. **Senior skill: knowing when a framework earns its complexity.**

### Project P6 — LangGraph Workflow: Insurance Claims Processing Pipeline
- **Problem:** Claims arrive as emails with attachments. Extract data, validate against policy (RAG), detect fraud signals, recommend payout, route high-value/suspicious claims to a human adjuster, draft customer communication.
- **Architecture:** Intake API → LangGraph: `extract → validate_policy (RAG) → fraud_check (parallel) → decide (conditional) → [interrupt: human review] → draft_response → finalize`. Postgres checkpointer, FastAPI approve/reject/edit endpoints, worker execution.
- **Technologies:** LangGraph, LangChain integrations, FastAPI, Postgres, pgvector, Redis, Langfuse/LangSmith.
- **Features:** deterministic steps where possible, LLM steps only where needed; editable human review; replay from any checkpoint; SLA timers on pending reviews.
- **Learning outcomes:** production LangGraph mixing deterministic and agentic nodes.
- **Security:** PII handling, attachment sanitization, adjuster RBAC, immutable audit trail of state transitions.
- **Testing:** node-level unit tests, graph path tests (every branch), eval set of 50 claims, replay-based regression.
- **Deployment:** containerized API + workers; traces in an observability tool.
- **Senior signal:** mostly deterministic graph; LLM steps isolated, evaluated, auditable — how regulated industries adopt agents.

---

## Chapter 10 — Model Context Protocol (MCP)

**Why it matters:** MCP standardizes how AI applications connect to tools and data, making integrations reusable across hosts. It's becoming the integration layer of enterprise AI.

### Concepts
- Architecture: **host → client → server**; primitives: **tools, resources, prompts**, plus sampling and elicitation.
- Transports: stdio (local) vs Streamable HTTP (remote); session handling.
- **Authorization for remote servers:** OAuth 2.1-based flows; token audience validation; no token passthrough.
- Server design: tool granularity, schemas, pagination, errors; resources vs tools.
- Risks: tool poisoning, rug-pull tool changes, confused deputy, over-permissive servers, third-party supply chain.
- MCP vs direct function calling vs A2A-style agent-to-agent protocols.
- The spec evolves — read the current version before building.

### Project P7 — MCP-Based Application: Enterprise Data MCP Gateway
- **Problem:** Multiple AI apps need governed access to the same internal systems (HR directory, ticketing, knowledge base).
- **Architecture:** 2–3 MCP servers (Python MCP SDK/FastMCP) over Streamable HTTP → OAuth (Keycloak/Entra ID) → per-tool scopes → audit logging; MCP client in the P6 agent + a desktop MCP host for testing.
- **Technologies:** MCP Python SDK, ASGI hosting, Keycloak or Entra ID, Postgres, OpenTelemetry.
- **Features:** scoped read/write tools, resource endpoints, prompt templates, per-user authorization to backends, rate limiting, tool-description change detector.
- **Learning outcomes:** protocol-level MCP understanding and enterprise auth.
- **Security:** least-privilege scopes, audience-bound tokens, input validation on every tool, no secrets in responses, allowlisted servers client-side.
- **Testing:** MCP Inspector, contract tests per tool, authorization matrix tests (user × tool × scope).
- **Deployment:** containerized servers behind a gateway.
- **Senior signal:** servers enforce the *end user's* permissions, not a god-mode service account.

---

# LEVEL 4 — ADVANCED AGENT ENGINEER

**Goal:** coordinate multiple agents, engineer for failure at distributed scale, and make systems secure and measurable.

## Chapter 11 — Planning, Reasoning and Multi-Agent Systems

**Why it matters:** Complex tasks exceed a single context window or skill set — but multi-agent systems multiply cost, latency, and failure modes. Seniors know when *not* to use them.

### Concepts
- **Planning:** plan-and-execute, re-planning, hierarchical decomposition, tree/graph-of-thought (concepts), reflection/self-critique, evaluator-optimizer loops.
- **Reasoning models:** when to spend test-time compute, reasoning-effort settings, cost/latency trade-offs.
- **Topologies:** supervisor/orchestrator-workers, hierarchical, handoffs (swarm-style), debate/critique, blackboard/shared state.
- **Context engineering:** focused context per sub-agent (the main real benefit), handoff payload design, shared vs isolated state.
- Failure modes: error compounding, infinite delegation, conflicting outputs, cost explosion, coordination overhead.
- A2A protocols (awareness).

### Project P8 — Multi-Agent System: Automated Due-Diligence Research Analyst
- **Problem:** Produce a sourced company due-diligence report (financials, news, competitors, risks) from web and internal sources.
- **Architecture:** LangGraph supervisor → planner → parallel specialists (financial, news, competitor, risk) via `Send` → fact-checker/critic → report writer → human review interrupt. Shared state holds claims with source attribution; each agent has isolated context and scoped tools (web search, internal RAG, MCP servers from P7).
- **Technologies:** LangGraph, MCP, web search API, pgvector, Langfuse, Redis.
- **Features:** per-agent budgets, global cost ceiling, claim-level citations, contradiction detection, re-planning on coverage gaps.
- **Learning outcomes:** orchestration, context isolation, system-level cost control.
- **Security:** web content is hostile — sub-agents reading web content get *no* write tools; output URLs sanitized.
- **Testing:** compare against a single-agent baseline on 20 companies (quality, cost, latency); per-agent evals; supervisor trajectory evals.
- **Deployment:** long-running queue-worker jobs with progress streaming.
- **Senior signal:** a benchmarked argument for why multi-agent beats single-agent here, by how much, at what cost.

---

## Chapter 12 — Agentic System Design and Distributed Execution

**Why it matters:** Agents are long-running, non-deterministic distributed processes that call unreliable services and take real actions. This separates a demo from a system — and your microservices background pays off most here.

| Topic | What a senior must understand for agents |
|---|---|
| **Stateless vs stateful agents** | Stateless workers + externalized state scale horizontally; in-memory state breaks under restarts and load balancing |
| **Sync vs async agents** | Sync for short interactive tasks (<30 s); async with job IDs, streaming, webhooks for longer; hybrid "sync first response, async continuation" |
| **Event-driven architecture** | Agents triggered by events; outbox pattern; event sourcing of agent steps for audit/replay |
| **Agent vs workflow orchestration** | LLM decides the next step vs code decides; combine as agent steps *inside* durable workflows |
| **Durable execution** | Temporal, LangGraph checkpointing, Azure Durable Functions, AWS Step Functions; survive crashes without re-executing completed side effects |
| **Idempotency** | LLM retries can re-issue tool calls → idempotency keys on every write tool; design for at-least-once + idempotent effects |
| **Retries** | Distinguish retrying the LLM call (safe), the tool call (only if idempotent), the whole step; backoff with jitter; retry budgets |
| **Timeouts** | Per-LLM-call, per-tool, per-step, per-run; streaming idle timeouts |
| **Circuit breakers** | Per provider and per tool; fall back to alternate model or degraded mode |
| **Rate limiting** | Provider RPM/TPM, per-tenant quotas, token-bucket admission control, priority queues |
| **Concurrency** | Per-thread locks (one active run per conversation), bounded fan-out, backpressure |
| **Distributed systems** | Consistency between agent state and external systems; sagas and compensating actions |
| **Fault tolerance** | Partial failures in parallel agents, graceful degradation, dead-letter queues for failed runs |
| **Human approval workflows** | Durable waits (hours/days), approval expiry, re-validating state before executing an approved action |
| **Long-running agents** | Heartbeats, progress checkpoints, cancellation, resumability, context compaction over hours |
| **Distributed task execution** | Work queues (Redis/SQS/Service Bus), Kafka for high-throughput streams and fan-out, autoscaling on queue depth |

**Kafka where relevant:** use it for high-volume event streams feeding many agent consumers, replayable event history, or multiple independent consumers. For simple job queues, Redis/SQS/Service Bus is simpler and correct.

### Project P6+ — Durable, Event-Driven Incident Response Agent
- **Problem:** Rebuild P4 to trigger automatically from alerts, run durably for hours, take remediation actions (restart, scale, rollback) with approvals, and survive any worker crash.
- **Architecture:** Alert source → Kafka topic (or SQS/Service Bus) → dispatcher → **Temporal workflow** (or LangGraph + Postgres checkpointer) wrapping agent steps as activities → idempotent tools → approval signal from Slack/Teams → saga compensation.
- **Technologies:** Temporal or LangGraph, Kafka/Redpanda, Postgres, Redis, FastAPI.
- **Features:** alert-storm deduplication, per-service concurrency limits, tool circuit breakers, approval expiry, event-sourced audit log.
- **Learning outcomes:** building agents with the discipline of payment systems.
- **Security:** per-environment action allowlists, prod approvals required, break-glass policy.
- **Testing:** **chaos tests** (kill workers mid-activity, inject timeouts, duplicate events) asserting no action executes twice.
- **Deployment:** Docker Compose with Temporal and Kafka; later K8s.
- **Senior signal:** proven exactly-once *effect* under chaos testing.

---

## Chapter 13 — Agentic AI Security Track

**Why it matters:** An agent is a program whose control flow can be influenced by any text it reads. Traditional appsec assumes code and data are separate; in LLM systems, **data can act as instructions.**

**Core mental model — the "lethal trifecta":** when an agent has (1) access to private data, (2) exposure to untrusted content, and (3) the ability to communicate externally, prompt injection can lead to data exfiltration. Design so no single context holds all three without controls.

| Threat / control | What to learn |
|---|---|
| **Prompt injection (direct)** | Jailbreaks, instruction override; why it can't be "patched" with prompts; defense in depth |
| **Indirect prompt injection** | Malicious instructions in documents, web pages, emails, tool outputs, RAG chunks — the most dangerous agent threat |
| **Tool abuse** | Model tricked into calling tools with attacker-chosen arguments; exfiltration via URLs, email, markdown image rendering |
| **Excessive agency** | Too much functionality, permission, autonomy → narrow tools, scoped credentials, approvals |
| **Data leakage / sensitive info exposure** | System prompt leakage, cross-tenant leakage via shared caches/memory/indexes, PII in logs and traces |
| **Insecure tool execution** | Code execution, shell, SQL — never string-build SQL from LLM output; parameterized, allowlisted operations |
| **Authentication** | Users → app (OIDC), app → providers, agent → tools (workload identity), MCP OAuth |
| **Authorization** | Enforce the *user's* permissions at the tool/data layer (on-behalf-of flows), not in the prompt |
| **Least privilege** | Per-tool, per-agent, per-tenant scopes; read-only by default; short-lived credentials |
| **Sandboxing** | Containers, gVisor, Firecracker microVMs, E2B-style sandboxes; no network by default |
| **Secrets management** | Key Vault / Secrets Manager, never in prompts or context, rotation, per-environment keys |
| **Data isolation** | Tenant-partitioned indexes or row-level security, per-tenant memory, namespaced cache keys |
| **Output validation** | Schema validation, HTML/markdown sanitization, URL allowlisting, never execute output directly |
| **Guardrails** | Llama Guard, injection classifiers, Azure AI Content Safety, Bedrock Guardrails, NeMo Guardrails, Presidio for PII. Guardrails reduce risk; they don't eliminate it |
| **OWASP & frameworks** | OWASP Top 10 for LLM Applications (2025: prompt injection, sensitive info disclosure, supply chain, data/model poisoning, improper output handling, excessive agency, system prompt leakage, vector/embedding weaknesses, misinformation, unbounded consumption), OWASP agentic AI threat guidance; MITRE ATLAS and NIST AI RMF (awareness) |

### Project S1 — Red-Team and Harden Your Agents
- **Problem:** Attack P3, P5, P7, and P8, then fix what you find.
- **Architecture:** Attack harness (garak / PyRIT / promptfoo red-teaming) → injected corpus docs, poisoned web pages, malicious MCP tool descriptions → findings DB → mitigations → regression suite.
- **Features:** threat model per system (STRIDE + LLM-specific), mitigation matrix, security regression suite in CI, sandboxed code-execution tool.
- **Learning outcomes:** attacker mindset and layered defenses.
- **Testing:** attack success rate before/after mitigation, tracked over time.
- **Senior signal:** threat model + measurable attack-success-rate reduction + honest residual-risk statement.

---

## Chapter 14 — LLM Evaluation and Observability Track

**Why it matters:** You can't unit-test your way to confidence with non-deterministic systems. Evaluation replaces "it worked when I tried it" with evidence; observability tells you what's happening in production. Together they are the feedback loop of AI engineering.

### Evaluation
- **Offline evaluation:** golden datasets (curation, versioning, stratification, refreshing from production failures), regression suites, experiment tracking.
- **Online evaluation:** sampled production scoring, A/B tests, shadow deployments, explicit and implicit user feedback.
- **LLM-as-a-judge:** rubric design, pairwise vs pointwise, judge biases (position, verbosity, self-preference), **calibration against human labels** (agreement / Cohen's kappa).
- **Human evaluation:** annotation guidelines, inter-annotator agreement, annotation queues.
- **Agent trajectory evaluation:** outcome success, path efficiency, tool sequence correctness, error recovery, pass@k vs pass^k.
- **Tool-call evaluation:** selection accuracy, argument correctness, unnecessary calls.
- **RAG evaluation:** context precision/recall, faithfulness, answer relevance, citation accuracy.
- **Hallucination measurement:** groundedness against sources, claim extraction + verification, unanswerable-question handling.
- **Benchmarking:** public benchmarks (limits, contamination) vs task-specific benchmarks (what matters).

### Observability
- **Tracing:** spans for LLM calls, tool calls, retrieval, agent steps; **OpenTelemetry GenAI semantic conventions**; trace-to-eval linking.
- **Metrics:** latency (TTFT, total, p50/p95/p99), tokens (input/output/cached), **cost per request/user/tenant/feature**, error rates, tool failure rates, steps per run.
- **Logging:** structured logs, correlation IDs, PII redaction, retention policies.
- **Production monitoring:** quality drift, model version changes, alerts on cost spikes and eval drops, dashboards.
- **Tools:** Langfuse, LangSmith, Arize Phoenix, W&B Weave, Datadog/Grafana; Ragas, DeepEval, promptfoo, Inspect.

### Project E1 — Evaluation and Observability Platform for Your Agents
- **Problem:** Instrument P6 and P8 end to end and build continuous evaluation.
- **Architecture:** OpenTelemetry → Langfuse/Phoenix (self-hosted) + Prometheus/Grafana → versioned golden datasets → CI eval gate → online sampler scoring 5% of production traces with calibrated judges → failures fed back into golden sets.
- **Features:** per-tenant/feature cost dashboard, latency SLO alerts, judge-vs-human calibration report, trajectory eval suite.
- **Learning outcomes:** the full production feedback loop.
- **Security:** PII redaction in traces, trace access control, retention limits.
- **Senior signal:** closed loop — production failure → dataset item → fix → regression test → deploy gate.

---

# LEVEL 5 — PRODUCTION AI ENGINEER

**Goal:** run AI systems reliably and economically at scale, on your own infrastructure or the cloud's.

## Chapter 15 — Model Strategy: Routing, Local and Cloud LLMs, Serving, Caching, Cost

**Why it matters:** Model choice is the biggest lever on cost, latency, quality, and data residency. Seniors design **model portfolios**, not single-model apps.

### Concepts
- **Cloud LLMs:** frontier vs small/fast, reasoning vs non-reasoning, pricing, data retention, regional availability, provisioned throughput vs pay-as-you-go.
- **Local/open-weight LLMs:** Llama, Qwen, Mistral, Gemma families (check what's current); licenses; when self-hosting makes sense (sovereignty, cost at volume, latency, customization).
- **Hugging Face ecosystem:** Hub, model cards, transformers, tokenizers, datasets, quantized formats (GGUF, AWQ, GPTQ).
- **Serving:** **Ollama** (dev), llama.cpp, **vLLM** (PagedAttention, continuous batching, OpenAI-compatible API), SGLang/TGI (awareness).
- **GPU basics:** VRAM math (params × bytes/param + KV cache), quantization trade-offs, batching vs latency, tensor parallelism, GPU types and cost.
- **Model routing:** rule-based vs classifier routing, cascades (cheap first, escalate on low confidence), fallbacks; **model gateways** (LiteLLM, Portkey, cloud gateways) for keys, quotas, logging, failover.
- **Caching:** exact-match cache, **semantic cache** (and its correctness risks), provider prompt caching (stable prefixes), embedding cache, tool-result cache.
- **Cost optimization:** token budgets, context trimming, batch APIs, small models for classification/extraction, distillation/fine-tuning (optional), cost attribution.
- **Performance:** streaming, parallel tool calls, speculative decoding (awareness), reducing agent step count (usually the biggest latency win).

### Project M1 — Multi-Model Gateway and Router
- **Problem:** Serve P2/P3/P8 through one gateway that routes each request to the cheapest model meeting quality requirements.
- **Architecture:** FastAPI or LiteLLM proxy → router (task classifier + cascade) → cloud providers + self-hosted vLLM (rented GPU) + Ollama for dev → Redis caches (exact + semantic with threshold) → per-tenant quotas → usage ledger in Postgres.
- **Features:** fallback chains, per-provider circuit breakers, budget enforcement, cost/quality dashboards.
- **Testing:** quality/cost/latency benchmarks per route with golden sets; load tests (Locust/k6).
- **Senior signal:** "Routing cut cost 62% with a 1.5% quality drop on our eval set — here's the Pareto curve."

---

## Chapter 16 — AI Infrastructure and Deployment Track

**Why it matters:** You know Docker and microservices; this chapter covers what's *different* for AI workloads: GPUs, long-running streaming connections, large model artifacts, bursty token-bound load, and eval-gated releases.

### Concepts
- **Docker for AI:** slim Python images, multi-stage builds with uv, CUDA base images, model weights as volumes rather than layers.
- **Kubernetes:** API and worker Deployments, HPA and **KEDA** (scale on queue depth), GPU node pools and device plugins, vLLM on K8s (KServe/llm-d-style serving awareness), ingress timeouts for SSE/WebSockets, PodDisruptionBudgets for long runs, NetworkPolicies to sandbox tool pods.
- **Cloud AI infrastructure** (deep on one, aware of the other):
  - *Azure (natural fit for .NET):* Azure OpenAI / AI Foundry, AI Search, AKS, Container Apps, Service Bus, Key Vault, Entra ID, API Management as AI gateway, Content Safety.
  - *AWS:* Bedrock (models, Knowledge Bases, Guardrails, AgentCore), SageMaker, EKS, ECS/Fargate, SQS, Secrets Manager, IAM.
- **CI/CD for AI:** lint/type/test → **eval gate** → security scans (deps, containers, red-team suite) → build → staging → smoke evals → canary/shadow → production. Version prompts, models, and datasets alongside code.
- **Infrastructure as Code:** Terraform (or Bicep/CDK), environment parity, secret references.
- Release strategies for model/prompt changes: feature flags, canaries, instant rollback.

### Project I1 — Deploy the Platform to Kubernetes on Azure or AWS
- **Problem:** Take P6+, E1, and M1 from Docker Compose to a production-shaped cloud deployment.
- **Architecture:** Terraform → AKS/EKS + managed Postgres + managed Redis + Key Vault/Secrets Manager + GPU node pool running vLLM → KEDA-scaled workers → GitHub Actions with eval gates → Grafana/Langfuse.
- **Senior signal:** one `git push` runs evals, security tests, and a canary with automatic rollback on eval or SLO regression.

---

## Flagship Project P9 — Production-Grade Agent Platform (culminates Chapters 12–16)

- **Problem:** Internal teams want to build and run agents without re-solving auth, tools, memory, evals, and observability. Build a **multi-tenant agent platform**.
- **Architecture:**
  - **Control plane:** agent registry (versioned definitions: graph, prompts, tools, model policy), tool registry (MCP servers with scopes), tenant/quota management, eval-suite registry.
  - **Data plane:** FastAPI gateway (OIDC authN, OPA/Cedar authZ) → run scheduler → durable execution workers (LangGraph/Temporal) → model gateway (M1) → MCP tool layer (P7) → sandboxed code execution → memory service (pgvector) → approval service.
  - **Cross-cutting:** OpenTelemetry tracing, cost ledger, input/output guardrails, audit log, eval runner.
- **Technologies:** FastAPI, LangGraph and/or Temporal, MCP, Postgres/pgvector, Redis, Kafka or cloud queue, vLLM + cloud models, Langfuse, OPA, K8s, Terraform, GitHub Actions.
- **Features:** deploy agents via config with versioning/rollback; per-tenant isolation (data, memory, cache, cost); approval workflows; replay any run; eval-gated version promotion; per-agent kill switch; SLO dashboards.
- **Components:** gateway, registry, scheduler, workers, model gateway, tool gateway, sandbox, memory, approval, eval, observability services.
- **Expected learning outcomes:** platform thinking; every Level 1–5 concept integrated.
- **Security:** tenant isolation tests, OBO authorization to tools, sandboxed execution, vault-managed secrets, guardrails, threat model, audit logs, kill switches.
- **Testing:** unit/integration/contract, chaos, tenant-isolation, red-team, load (concurrent runs, streaming connections), per-agent eval suites.
- **Deployment:** Terraform-provisioned K8s, GitOps (Argo CD optional), canary releases of agent versions.
- **What makes it senior-level:** you've built the *platform other engineers build on*, with governance, isolation, and a closed eval loop.

---

# LEVEL 6 — SENIOR AGENTIC AI ARCHITECT

## Chapter 17 — Enterprise AI Architecture, Patterns and System Design

**Why it matters:** At architect level the questions shift from "how do I build it" to "should we build it, what's the risk, what's the total cost, how does it fit the enterprise, and how do we govern 50 of these?"

### Concepts
- **AI system design method:** requirements (task, users, accuracy tolerance, latency, volume, risk tier) → build vs buy → autonomy level (assistive → copilot → supervised agent → autonomous) → architecture → eval plan → threat model → cost model → rollout plan.
- **Enterprise AI patterns:** central AI gateway, enterprise RAG with permission sync (SharePoint/Confluence), copilot-over-systems-of-record, agent-as-a-service platforms, HITL operations centers, event-driven autonomous agents, "AI in the workflow" vs "chat as UI."
- **Governance:** model inventory, AI risk classification, EU AI Act and similar regulatory awareness, data residency, audit and explainability, responsible-AI review, vendor risk.
- **Economics:** unit cost per task, ROI modeling, token and GPU capacity planning, cost/quality Pareto decisions.
- **Organizational architecture:** platform vs product teams, reusable components, evaluation standards, AI incident response and runbooks.
- **Architecture decision records** for model, framework, vector store, and autonomy choices.

### Flagship Project P10 — Enterprise-Grade Autonomous AI Application: Autonomous Procurement and Vendor Operations Agent
- **Problem:** A large enterprise processes thousands of purchase requests, vendor onboardings, and invoice exceptions monthly. Build an autonomous system that handles the routine majority end to end and escalates the rest, under strict financial controls.
- **Architecture:** Built **on P9**. Event sources (ERP events, email intake, portal) → Kafka → durable workflows: intake agent → policy/contract RAG → vendor-risk multi-agent assessment (sanctions, financial health, security questionnaire analysis) → decision engine (deterministic rules + LLM judgment with confidence thresholds) → approval tiers by amount and risk → action execution via MCP servers to the ERP (idempotent, saga-compensated) → audit and explainability reports.
- **Technologies:** everything from P9, plus ERP mock/sandbox, OPA policies for financial authority matrices, document intelligence for invoices, Kafka.
- **Features:** per-category autonomy levels, segregation of duties enforced in code, explanation record per decision, decision-quality drift monitoring, shadow-mode rollout (agent decides, humans execute, compare), monthly compliance reports.
- **Components:** domain agents, policy engine, approval service, ERP MCP servers, compliance reporter, shadow-mode comparator.
- **Expected learning outcomes:** designing autonomy responsibly in a high-stakes domain.
- **Security:** no agent holds payment authority; financial actions require policy approval + human sign-off above thresholds; vendor documents treated as hostile (invoice-based injection is a real fraud vector); full audit trail; SoD checks.
- **Testing:** shadow-mode accuracy vs humans on historical data, adversarial vendor documents, policy-matrix tests, chaos tests on ERP integration, regression evals per release.
- **Deployment:** phased rollout shadow → assisted → autonomous for low-value categories, with kill switches and automated rollback on quality drift.
- **Deliverables beyond code:** architecture document, ADRs, threat model, cost model, risk assessment, rollout plan, runbooks.
- **What makes it senior-level:** you can defend every autonomy decision to a CFO, CISO, and auditor.

---

# Senior Engineer Skill Matrix

| Area | Junior | Mid-level | Senior | Architect |
|---|---|---|---|---|
| **LLM fundamentals** | Calls APIs, basic prompts | Understands tokens, context, sampling | Reasons about inference cost/latency and model trade-offs | Designs model portfolios and procurement strategy |
| **Prompting / structured output** | Writes prompts | Templates, few-shot, JSON output | Versioned, eval-gated prompts; schema-validated outputs | Sets org-wide prompt/eval standards |
| **RAG** | Follows a tutorial | Builds a pipeline with a vector DB | Hybrid search, reranking, ACLs, measured retrieval quality | Enterprise knowledge architecture, permission sync, freshness governance |
| **Agents** | Uses a prebuilt agent | Builds tool-calling agents in a framework | Designs tools, budgets, state, HITL; knows when not to use agents | Defines autonomy levels and agent platform strategy |
| **Orchestration** | Linear chains | LangGraph graphs | Durable, resumable, idempotent workflows | Org-wide orchestration and platform choices |
| **Evaluation** | Manual testing | Golden sets, basic metrics | Calibrated judges, trajectory evals, CI gates, online eval | Evaluation strategy and quality SLAs across products |
| **Observability** | Print logs | Traces in one tool | OTel tracing, cost attribution, SLOs, drift alerts | Platform-wide AI observability standards |
| **Security** | Hides API keys | Basic input filtering | Threat models, least privilege, sandboxing, injection defense in depth | AI risk governance, OWASP/NIST alignment, audit readiness |
| **Infrastructure** | Runs locally | Docker, one cloud deploy | K8s, autoscaling, GPU serving, IaC, eval-gated CI/CD | Capacity planning, hybrid cloud/self-host strategy |
| **System design** | Single service | Service + queue | Distributed agent systems with fault tolerance | Enterprise architecture, build vs buy, cost/ROI |
| **Communication** | Explains own code | Documents designs | Writes ADRs, mentors, leads design reviews | Aligns executives, risk, legal, and engineering |

---

# Portfolio Strategy

Recruiters see hundreds of "chat with your PDF" repos. Quantity doesn't impress; **depth, evidence, and production thinking do.**

### Showcase three to four projects, not ten
1. **P3+ (Eval-driven RAG)** — proves you optimize with data, not hype.
2. **P6 / P6+ (Durable LangGraph/Temporal workflow)** — proves you build reliable, auditable agents.
3. **P9 (Agent platform)** — the centerpiece; proves platform and production thinking.
4. **P10 or S1 (Enterprise autonomous agent or red-team report)** — proves architect-level judgment or security depth.

### What each showcase repo needs
- README opening with the problem, an architecture diagram, and **measured results** (eval scores, cost per task, p95 latency, attack success rate before/after).
- ADRs explaining key choices and rejected alternatives.
- Threat model and eval report as documents in the repo.
- One-command local run (Docker Compose) and CI badges showing tests and eval gates.
- A 3–5 minute demo video that includes a failure being handled (approval gate, crash recovery, blocked injection).
- Blog posts on lessons learned (e.g., "What broke when we made our agent crash-safe").

### Leverage your background
Position yourself as an *enterprise engineer who builds AI systems properly*, not a career-switcher. An Azure/.NET-to-Python AI bridge (e.g., a Semantic Kernel vs LangGraph comparison, or an Azure-deployed platform) is a distinctive angle.

---

# Interview Preparation

| Area | What to prepare | Example questions |
|---|---|---|
| **Python** | asyncio, typing, generators, GIL, Pydantic, packaging | How do you bound concurrency to 20 LLM calls at once? What happens if you call a blocking SDK inside an async endpoint? |
| **FastAPI** | DI, async vs sync routes, streaming, middleware, auth | How would you stream tokens and handle client disconnects? How do you implement per-tenant rate limiting? |
| **LLMs** | Tokens, attention, KV cache, sampling, context limits, reasoning models | Why is output more expensive than input? Why doesn't temperature 0 guarantee determinism? When would you choose a reasoning model? |
| **RAG** | Chunking, hybrid search, reranking, eval metrics, ACLs | Users say answers are wrong — how do you debug it? How do you enforce document permissions? |
| **Agents** | Agent loop, tool design, termination, workflows vs agents | Design tools for a calendar agent. How do you stop runaway loops? When would you *not* build an agent? |
| **LangGraph** | State, reducers, checkpointers, interrupts, Send, subgraphs | How does resume-after-approval work internally? How do you fan out and merge? |
| **MCP** | Host/client/server, primitives, transports, OAuth | How do you secure a remote MCP server? What's tool poisoning? MCP vs direct function calling? |
| **AI system design** | End-to-end design with trade-offs | Design a support agent for 10M users. Design enterprise RAG over SharePoint with permissions. Design a coding agent that runs untrusted code. |
| **AI security** | Injection, excessive agency, OWASP LLM Top 10, sandboxing | An agent reads emails and can send emails — what could go wrong and how do you design it safely? |
| **Distributed systems** | Idempotency, retries, sagas, durable execution, backpressure | The agent timed out after calling "issue refund." Did the refund happen? How do you make this safe? |
| **Cloud** | Azure OpenAI/Bedrock, managed K8s, queues, secrets, private networking | How would you deploy with private endpoints and data residency constraints? GPU autoscaling approach? |
| **Production troubleshooting** | Latency, cost spikes, quality drops, provider outages | Costs doubled overnight — walk through your investigation. Quality dropped after a provider model update — what do you do? p95 latency is 40 s — where do you look? |

### AI system design interview framework
1. Clarify requirements and risk tier
2. Define success metrics and eval plan
3. High-level architecture
4. Deep dive: agent loop, state, tools
5. Failure modes and resilience
6. Security and threat model
7. Observability
8. Cost estimate
9. Scaling
10. Rollout plan

Practice 15–20 designs out loud.

---

# Common Mistakes and How to Avoid Them

1. **Learning frameworks before fundamentals.** You'll be lost when the abstraction leaks. *Fix:* build the raw loop first (Chapters 5 and 7).
2. **Using agents where a workflow would do.** Adds cost, latency, unpredictability. *Fix:* start deterministic; add agency only where the path can't be predetermined.
3. **No evaluation ("vibes-based development").** *Fix:* build a golden set before the first prompt iteration and grow it from failures.
4. **Trusting LLM output.** *Fix:* validate every output like user input; never execute or render it unsanitized.
5. **Relying on prompts for security** ("Never reveal secrets…"). *Fix:* enforce permissions in code at the tool and data layer.
6. **Broad tools and service-account credentials.** *Fix:* narrow tools, user-scoped authorization, approvals for writes.
7. **Ignoring cost until the bill arrives.** *Fix:* per-request cost attribution from P1 onward.
8. **Blaming the model for retrieval failures.** *Fix:* measure retrieval and generation separately.
9. **Over-stuffing context.** Degrades quality and costs more. *Fix:* deliberate context engineering.
10. **Non-idempotent tools with retries.** Duplicate emails, orders, refunds. *Fix:* idempotency keys on every write.
11. **Demo-driven development.** Happy paths hide the 20% of failure cases. *Fix:* test adversarial, ambiguous, unanswerable inputs.
12. **Chasing every new model and framework.** *Fix:* evaluate against your own benchmarks; adopt only on measured improvement.
13. **Multi-agent by default.** *Fix:* benchmark against a single agent; justify the complexity.
14. **Neglecting observability** until production is on fire. *Fix:* tracing from the first agent project.
15. **Underusing your .NET experience.** Resilience, DI, typed contracts, enterprise auth transfer directly — don't unlearn them in Python.

---

# Suggested Timeline (10–15 hrs/week)

| Months | Chapters | Milestone |
|---|---|---|
| 1 | 1–2 | Fluent async Python and FastAPI service skeleton |
| 2–3 | 3–4 | P1, P2 shipped with first eval set |
| 4–5 | 5–6 | P3 and eval-driven P3+ |
| 6–7 | 7–8 | Hand-built agent (P4) and stateful agent (P5) |
| 8–9 | 9–10 | LangGraph (P6) and MCP (P7) |
| 10–11 | 11–14 | Multi-agent (P8), durable systems (P6+), security and eval tracks |
| 12–14 | 15–16 | Model gateway, cloud deployment, P9 platform |
| 15+ | 17 | P10 capstone, portfolio polish, interview prep |

---

# Progress Tracker

| # | Chapter | Project | Status | Notes |
|---|---|---|---|---|
| 1 | Python for AI Engineering | F1 | ☐ | |
| 2 | FastAPI and Async Service Foundations | F2 | ☐ | |
| 3 | LLM Fundamentals and Provider APIs | P1 | ☐ | |
| 4 | Prompt Engineering, Structured Outputs, Tool Calling | P2 | ☐ | |
| 5 | Embeddings, Vector DBs and RAG | P3 | ☐ | |
| 6 | Advanced RAG | P3+ | ☐ | |
| 7 | Agents from First Principles | P4 | ☐ | |
| 8 | State, Memory and HITL | P5 | ☐ | |
| 9 | LangChain and LangGraph | P6 | ☐ | |
| 10 | MCP | P7 | ☐ | |
| 11 | Planning, Reasoning and Multi-Agent | P8 | ☐ | |
| 12 | Agentic System Design | P6+ | ☐ | |
| 13 | Security Track | S1 | ☐ | |
| 14 | Evaluation and Observability Track | E1 | ☐ | |
| 15 | Model Strategy | M1 | ☐ | |
| 16 | Infrastructure and Deployment Track | I1 + P9 | ☐ | |
| 17 | Enterprise AI Architecture | P10 | ☐ | |

---

> **The goal:** to confidently answer — *"How would you design, build, secure, evaluate, deploy, monitor, and scale this Agentic AI system in production?"*
