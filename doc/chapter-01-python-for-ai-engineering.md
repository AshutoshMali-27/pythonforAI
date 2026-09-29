# Chapter 1 — Python for AI Engineering
### Level 1 · Foundation | Senior Agentic AI Engineer Roadmap

---

## Mentor's Opening

Before we write a single line of code, here's how this chapter works.

You already know how to build production software in .NET. That means we won't waste time explaining what a variable is or what an API does. What we *will* do is show you exactly where Python thinks differently from C#, where async Python will bite you if you don't respect it, and which Python patterns show up *constantly* in AI engineering codebases.

By the end of this chapter, you won't just "know Python" — you'll write Python the way the best AI engineers write it: **typed, async-safe, well-packaged, and resilient.**

---

## Chapter Structure

For every section:
1. **The concept explained** — with your .NET background as the anchor
2. **Code examples** — real, not toy examples
3. **The AI engineering connection** — exactly where this shows up in LLM/agent code
4. **The senior pitfalls** — what junior devs get wrong
5. **A mini-exercise** — so you apply it immediately

---

## Full Syllabus — Sections at a Glance

| # | Section | Core Theme |
|---|---|---|
| 1 | Python's Mental Model vs C# | The mindset shift |
| 2 | Type Hints and Static Analysis | Getting compile-time safety back |
| 3 | Pydantic v2 | The backbone of AI engineering |
| 4 | asyncio In Depth | The most critical section |
| 5 | Essential Libraries for AI Engineering | Your standard toolkit |
| 6 | Data Basics for AI Engineering | numpy, json, pandas |
| 7 | Packaging, Tooling and Project Setup | Professional Python project setup |

---

## Section 1 — Python's Mental Model vs C# (The Mindset Shift)

> *"Why does Python work this way?"*

### Topics
- How the Python runtime executes code (interpreted, bytecode, CPython)
- Dynamic typing vs static typing — and why that doesn't mean "no types"
- **Duck typing** and **structural subtyping** (the Python way of interfaces)
- The **data model**: how Python objects actually work (dunder/magic methods — `__repr__`, `__len__`, `__call__`, `__enter__`/`__exit__` etc.)
- **Generators and iterators**: what `yield` does, lazy evaluation, why the entire AI data pipeline world is built on generators
- Everything is an object (functions, classes, modules)
- **Mapping C# concepts → Python**:

| C# | Python |
|---|---|
| `interface` | `Protocol` |
| `IDisposable` | context manager (`with`) |
| `Func<T>` | callable |
| LINQ | comprehensions / generators |
| `using` | `with` |
| `IEnumerable<T>` | generator / iterator |
| `abstract class` | `ABC` or `Protocol` |

---

## Section 2 — Type Hints and Static Analysis (Writing Python Like a Senior)

> *"Getting your compile-time safety back"*

### Topics
- Why type hints exist and what they do (and don't do) at runtime
- Basic annotations: `str`, `int`, `list[str]`, `dict[str, Any]`, `Optional`, `Union`, `tuple`
- **`TypedDict`** — typed dictionaries (used constantly for LLM message formats)
- **`Protocol`** — structural interfaces, Python's answer to `interface` in C#
- **Generics** — `TypeVar`, `Generic[T]`, `list[T]`
- **`Literal`** — constraining to exact values (e.g., `Literal["user", "assistant", "system"]`)
- **`Annotated`** — attaching metadata to types (Pydantic uses this heavily)
- `mypy` and `pyright` — how to configure them, what `strict` mode means
- `@overload` for multiple signatures
- When to use `Any` (rarely) and when `object` is more correct

### Key Code Pattern
```python
from typing import Literal, TypedDict, Protocol, Annotated
from pydantic import Field

# LLM message format — you'll see this in every AI codebase
class Message(TypedDict):
    role: Literal["system", "user", "assistant", "tool"]
    content: str

# Protocol as interface
class LLMClient(Protocol):
    async def complete(self, messages: list[Message]) -> str: ...
```

---

## Section 3 — Pydantic v2 (The Backbone of AI Engineering)

> *"Your DataContract / DTO layer — but supercharged"*

### Topics
- What Pydantic is and why it dominates AI engineering (LLM outputs, API contracts, config)
- **`BaseModel`** — defining models, field types, defaults
- **Field validation**: `Field(...)`, `ge`, `le`, `min_length`, `pattern`, custom validators (`@field_validator`, `@model_validator`)
- **Serialization**: `.model_dump()`, `.model_dump_json()`, `.model_validate()`, aliases
- **Nested models** and `list[Model]`
- **`TypedDict` vs Pydantic BaseModel** — when to use which
- **`pydantic-settings`** — environment-based configuration (replaces `IConfiguration` from .NET)
- **Pydantic with LLMs** — defining structured output schemas, validation-and-repair loops
- Custom types: `SecretStr`, `HttpUrl`, `AwareDatetime`
- Pydantic v1 vs v2 differences (you'll see both in codebases)

### Key Code Pattern
```python
from pydantic import BaseModel, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Structured LLM output — the pattern you'll use from Chapter 4 onward
class TicketClassification(BaseModel):
    category: Literal["billing", "technical", "account", "other"]
    severity: int = Field(ge=1, le=5, description="1=low, 5=critical")
    summary: str = Field(min_length=10, max_length=200)
    requires_escalation: bool

    @field_validator("summary")
    @classmethod
    def summary_must_be_sentence(cls, v: str) -> str:
        if not v[0].isupper():
            raise ValueError("Summary must start with a capital letter")
        return v

# Config from environment — replaces IConfiguration / appsettings.json
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    openai_api_key: SecretStr
    model_name: str = "gpt-4o"
    max_tokens: int = 1000
    redis_url: str = "redis://localhost:6379"
```

---

## Section 4 — asyncio In Depth (The Most Critical Section)

> *"Where most Python AI engineers are secretly weak"*

### Topics
- Why LLM apps are I/O-bound, and why that makes async essential
- How the **event loop** actually works (single-threaded cooperative multitasking)
- `async def`, `await`, `coroutine` objects — what they are at a mechanical level
- `asyncio.run()` — the entry point
- **`asyncio.gather()`** — running coroutines concurrently (like `Task.WhenAll`)
- **`asyncio.TaskGroup`** (Python 3.11+) — safer structured concurrency
- **`asyncio.Semaphore`** — bounding concurrency (critical for LLM rate limits)
- **`asyncio.timeout()`** (3.11+) and `asyncio.wait_for()` — per-call timeouts
- **Task cancellation** — `task.cancel()`, `asyncio.CancelledError`, cleanup in `finally`
- **The #1 mistake: blocking calls inside async code** — `time.sleep` vs `asyncio.sleep`, sync SDK calls, CPU-bound work
- **`asyncio.to_thread()`** — safely offloading blocking work
- `asyncio.Queue` — async producer/consumer (you'll use this in agent pipelines)
- Debugging async code: `asyncio.get_event_loop().set_debug(True)`, detecting blocking calls

### C# → Python Async Mapping

| C# | Python asyncio |
|---|---|
| `Task` | coroutine / `asyncio.Task` |
| `Task.WhenAll(...)` | `asyncio.gather(...)` |
| `Task.WhenAny(...)` | `asyncio.wait(..., return_when=FIRST_COMPLETED)` |
| `SemaphoreSlim` | `asyncio.Semaphore` |
| `CancellationToken` | task cancellation / `asyncio.CancelledError` |
| `async/await` | `async/await` (same keywords!) |
| `ConfigureAwait(false)` | not needed (no sync context in asyncio) |

### Key Code Pattern — Bounded Concurrent LLM Calls
```python
import asyncio
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

# The pattern you'll use constantly: concurrent calls, bounded, with timeout
async def call_llm_bounded(
    prompts: list[str],
    max_concurrent: int = 10,
    timeout_seconds: float = 30.0,
) -> list[str]:
    semaphore = asyncio.Semaphore(max_concurrent)

    async def single_call(prompt: str) -> str:
        async with semaphore:                          # bounded concurrency
            async with asyncio.timeout(timeout_seconds):   # per-call timeout
                return await _call_provider(prompt)

    # Run all concurrently, up to max_concurrent at a time
    results = await asyncio.gather(
        *[single_call(p) for p in prompts],
        return_exceptions=True,   # don't let one failure cancel all
    )
    return results

# THE MISTAKE — blocking call inside async def stalls the entire event loop:
async def bad_example():
    import time
    time.sleep(5)          # ❌ freezes the loop — no other coroutines run
    await asyncio.sleep(5) # ✅ yields control — other coroutines run

# Offloading a blocking SDK call safely:
async def good_example(sync_sdk_client, prompt: str) -> str:
    return await asyncio.to_thread(sync_sdk_client.complete, prompt)  # ✅
```

### Senior Pitfalls
1. Calling a synchronous HTTP library (like `requests`) inside `async def` — stalls the event loop silently.
2. Not bounding concurrency — firing 1000 LLM calls simultaneously triggers 429s and exhausts connection pools.
3. Catching `Exception` and silently swallowing `asyncio.CancelledError` — always re-raise it.
4. Creating tasks without storing a reference — they get garbage collected mid-execution.
5. Mixing `asyncio.run()` calls — there is one event loop; don't create nested ones.

---

## Section 5 — Essential Libraries for AI Engineering

> *"Your standard toolkit"*

### `httpx` — Async HTTP Client
- The async replacement for `requests`
- Connection pooling, timeouts, retries, HTTP/2
- Used in every LLM provider call, tool execution, and ingestion

```python
import httpx

async def fetch_with_timeout(url: str) -> dict:
    async with httpx.AsyncClient(timeout=httpx.Timeout(10.0, connect=3.0)) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
```

### `tenacity` — Retry Logic (Your Polly)
- Exponential backoff, jitter, stop conditions, retry predicates
- Essential for every LLM provider call (429, 500, overloaded errors)

```python
from tenacity import (
    retry, stop_after_attempt, wait_exponential_jitter,
    retry_if_exception_type, before_sleep_log
)
import logging

logger = logging.getLogger(__name__)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential_jitter(initial=1, max=60),
    retry=retry_if_exception_type((httpx.HTTPStatusError, TimeoutError)),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
async def resilient_llm_call(prompt: str) -> str:
    return await call_provider(prompt)
```

### `structlog` — Structured Logging
- JSON logs, bound context (request ID, tenant ID, model name)
- Async-safe, compatible with standard `logging`
- Essential for observability from day one

```python
import structlog

log = structlog.get_logger()

async def process_request(request_id: str, tenant_id: str) -> None:
    log = log.bind(request_id=request_id, tenant_id=tenant_id)  # context sticks
    log.info("llm_call_start", model="gpt-4o", prompt_tokens=150)
    # ... call LLM ...
    log.info("llm_call_complete", completion_tokens=80, latency_ms=420)
```

### Context Managers
- `with` statement: `__enter__` / `__exit__` for sync, `async with` for async
- `@contextmanager` and `@asynccontextmanager` decorators
- Used for: DB connections, HTTP clients, locks, cost tracking spans

```python
from contextlib import asynccontextmanager
from typing import AsyncGenerator

@asynccontextmanager
async def tracked_llm_call(model: str) -> AsyncGenerator[None, None]:
    start = time.monotonic()
    try:
        yield
    finally:
        duration_ms = (time.monotonic() - start) * 1000
        log.info("llm_call", model=model, duration_ms=round(duration_ms, 2))
```

### Decorators
- `@functools.wraps` to preserve metadata
- Parameterized decorators (a function returning a decorator)
- Used for: retry wrappers, cost tracking, auth checks, caching

```python
import functools
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def require_auth(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        # check auth ...
        return await func(*args, **kwargs)
    return wrapper
```

### Topics also covered
- **`dataclasses`** — lightweight data containers vs Pydantic (when to use which)
- `pathlib` — file paths done right (replaces `os.path`)
- `functools` (`partial`, `lru_cache`, `reduce`)
- `itertools` and `collections` (`defaultdict`, `Counter`, `deque`)

---

## Section 6 — Data Basics for AI Engineering

> *"Just enough numpy, json, and pandas to not be dangerous"*

### JSON Handling
```python
import json
import orjson  # fast, handles bytes and datetime natively

# Standard
data = json.loads(response_text)
output = json.dumps(data, indent=2, ensure_ascii=False)

# orjson — faster, use for large payloads
data = orjson.loads(response_bytes)
output = orjson.dumps(data)  # returns bytes
```

### numpy — Embedding Vectors
You don't need all of numpy. You need this:

```python
import numpy as np

# Embeddings come back as lists of floats — convert to numpy arrays
embedding_a = np.array([0.1, 0.3, 0.5, ...], dtype=np.float32)
embedding_b = np.array([0.2, 0.1, 0.4, ...], dtype=np.float32)

# Cosine similarity (used in every RAG retrieval step)
def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# Batch similarity — a matrix (n_docs, dim) against a query (dim,)
scores = embeddings_matrix @ query_embedding  # dot product, vectorized
```

### pandas — Eval Datasets and Batch Results
```python
import pandas as pd

# Loading an eval dataset
df = pd.read_csv("golden_set.csv")

# Filtering, applying, aggregating — the three operations you'll use most
failures = df[df["score"] < 0.7]
df["category"] = df["ticket_text"].apply(classify)
summary = df.groupby("category")["score"].mean()

# Converting to/from dicts for Pydantic models
records = df.to_dict(orient="records")
df = pd.DataFrame([model.model_dump() for model in results])
```

### String Handling for Prompt Templates
```python
# F-strings — the standard for prompt building
system_prompt = f"""You are a support agent for {company_name}.
Today's date is {date.today().isoformat()}.
Respond in {language}."""

# Multiline strings with dedent — for clean indentation
from textwrap import dedent

prompt = dedent(f"""
    Classify the following ticket into one of these categories:
    {', '.join(categories)}

    Ticket: {ticket_text}

    Return JSON only.
""").strip()

# Why string concatenation is an antipattern for prompts:
# ❌ prompt = "Classify: " + text + "\nCategories: " + str(cats)
# ✅ Use f-strings or a template class — readable, testable, versionable
```

---

## Section 7 — Packaging, Tooling and Project Setup

> *"The professional Python project setup no tutorial teaches you"*

### `uv` — The Modern Python Package Manager
```bash
# Install uv (replaces pip, virtualenv, poetry)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a new project
uv init my-ai-app
cd my-ai-app

# Add dependencies
uv add fastapi pydantic pydantic-settings httpx tenacity structlog

# Add dev dependencies
uv add --dev pytest pytest-asyncio respx mypy ruff

# Run a script / command inside the venv
uv run python -m pytest
uv run mypy src/
```

### `pyproject.toml` — The Modern Project Manifest
```toml
[project]
name = "my-ai-app"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115",
    "pydantic>=2.9",
    "pydantic-settings>=2.6",
    "httpx>=0.27",
    "tenacity>=9.0",
    "structlog>=24.4",
    "openai>=1.50",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.3",
    "pytest-asyncio>=0.24",
    "respx>=0.21",
    "mypy>=1.11",
    "ruff>=0.7",
]

[tool.mypy]
strict = true
python_version = "3.12"

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B", "SIM"]

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
```

### Project Structure
```
my-ai-app/
├── pyproject.toml
├── .env                    # local secrets — never committed
├── .env.example            # template — committed
├── Dockerfile
├── src/
│   └── my_ai_app/
│       ├── __init__.py
│       ├── main.py         # FastAPI app (from Chapter 2)
│       ├── config.py       # pydantic-settings
│       ├── providers/      # LLM provider adapters (from Chapter 3)
│       │   ├── __init__.py
│       │   ├── base.py
│       │   └── openai.py
│       └── models/         # Pydantic models
│           └── __init__.py
└── tests/
    ├── conftest.py
    ├── test_providers/
    └── test_models/
```

### `ruff` — Linting and Formatting
```bash
uv run ruff check src/          # lint
uv run ruff check src/ --fix    # auto-fix safe issues
uv run ruff format src/         # format (replaces black + isort)
```

### `pytest` and `pytest-asyncio` — Testing Async Code
```python
# tests/conftest.py
import pytest
import pytest_asyncio

@pytest.fixture
def settings() -> Settings:
    return Settings(openai_api_key="test-key", model_name="gpt-4o-mini")

# tests/test_providers/test_openai.py
import pytest
import respx
import httpx

@pytest.mark.asyncio
async def test_llm_call_returns_content(settings: Settings) -> None:
    with respx.mock:
        respx.post("https://api.openai.com/v1/chat/completions").mock(
            return_value=httpx.Response(
                200,
                json={
                    "choices": [{"message": {"content": "Hello!"}}],
                    "usage": {"prompt_tokens": 10, "completion_tokens": 5},
                },
            )
        )
        client = OpenAIAdapter(settings)
        result = await client.complete([{"role": "user", "content": "Hi"}])
        assert result.content == "Hello!"
        assert result.usage.total_tokens == 15
```

### Dockerfile — Python AI App, Done Right
```dockerfile
# Multi-stage build — small final image
FROM python:3.12-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app
COPY pyproject.toml .
RUN uv sync --no-dev --frozen

FROM python:3.12-slim AS runtime
WORKDIR /app

# Copy venv from builder
COPY --from=builder /app/.venv /app/.venv
COPY src/ ./src/

ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Non-root user — security baseline
RUN useradd --no-create-home --shell /bin/false appuser
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.my_ai_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Chapter 1 — Project F1

### Async Multi-Source Content Fetcher Library

**Problem Statement**
Build a reusable Python library that fetches and normalizes content from 50+ URLs or APIs concurrently, with bounded concurrency, retries with backoff and jitter, per-request timeouts, and typed results.

This library becomes your **ingestion layer in Chapter 5 (RAG)**.

**Architecture**
```
Library Package
├── Protocol-based Source adapters   (interface contract)
├── Async orchestrator               (semaphore-bounded gather)
├── Pydantic result models           (typed outputs)
└── CLI entrypoint                   (click or argparse)
```

**Technologies**
- Python 3.12+, uv, httpx, tenacity, Pydantic v2, structlog, pytest, respx, mypy (strict)

**Features**
- [ ] Concurrent fetching with configurable max concurrency
- [ ] Per-request configurable timeouts
- [ ] Retry with exponential backoff and jitter on transient failures
- [ ] Partial failure handling — one failure doesn't cancel others
- [ ] `Protocol`-based `Source` adapter (HTTP, RSS, file)
- [ ] Typed `FetchResult` Pydantic model with status, content, error, latency
- [ ] Structured logging per request
- [ ] CLI: `uv run fetch --urls urls.txt --concurrency 20`

**Security Considerations**
- URL allowlist validation — reject private IP ranges (SSRF prevention)
- Response size limit — reject responses over a configurable max bytes
- No secrets logged — API keys redacted from structlog output
- Content-type validation — only process expected MIME types

**Testing Strategy**
- Unit tests with `respx` mocked transports for each adapter
- Concurrency tests — assert semaphore bounds are respected
- Retry tests — mock 429s and assert backoff behavior
- Timeout tests — mock slow responses and assert timeout fires
- SSRF tests — assert private IPs are rejected
- `mypy --strict` passes with zero errors
- 90%+ coverage

**Deployment**
- Installable as a package (`uv add git+https://...`)
- Also runnable as a Docker container for the CLI

**What Makes It Senior-Level**
- A clean `Source` Protocol — not a class hierarchy — so adapters are swappable
- Resilience (retry, timeout, partial failure) designed in, not bolted on
- Strict types throughout — `mypy --strict` is green
- The semaphore bound is visible in the API, not hidden in a magic constant

---

## Progress Checklist

### Sections
- [ ] Section 1 — Python's Mental Model vs C#
- [ ] Section 2 — Type Hints and Static Analysis
- [ ] Section 3 — Pydantic v2
- [ ] Section 4 — asyncio In Depth
- [ ] Section 5 — Essential Libraries for AI Engineering
- [ ] Section 6 — Data Basics for AI Engineering
- [ ] Section 7 — Packaging, Tooling and Project Setup

### Project F1
- [ ] Project structure created with `uv`
- [ ] `Source` Protocol defined and typed
- [ ] HTTP adapter implemented with httpx + tenacity
- [ ] Async orchestrator with semaphore and gather
- [ ] Pydantic result models
- [ ] structlog integration
- [ ] CLI entrypoint
- [ ] Tests written and passing (mypy strict, 90%+ coverage)
- [ ] Dockerized

---

## Key Takeaways

1. **Python is typed** — use `mypy --strict` from day one. Your .NET instincts are right.
2. **Blocking calls in async code are the silent killer** — always await, never `time.sleep`.
3. **Bound your concurrency** — a `Semaphore` is always needed when calling external APIs in a loop.
4. **Pydantic is everywhere** — learn v2 deeply, not just the basics.
5. **`uv` + `ruff` + `pyright`** — the modern Python toolchain; don't use pip/virtualenv/black/flake8 for new projects.
6. **Generators are lazy** — use them for large data streams in ingestion pipelines.
7. **`tenacity` is your Polly** — wrap every external call from the start.

---

*Next: Chapter 2 — FastAPI and Async Service Foundations (Postgres, Redis, Queues)*
