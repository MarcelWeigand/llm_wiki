# Agentic AI Observability

**Summary**: Observability for AI agents requires a fundamentally different approach than traditional software monitoring — covering three telemetry pillars (logs, traces, metrics), concrete primitives (runs, traces, threads), the OpenTelemetry open standard for distributed tracing, and continuous production monitoring with explicit and implicit signals.

**Sources**: `raw/youtube/2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt`, `raw/youtube/2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt`, `raw/youtube/2026-06-29_Agentcore_observability_AWS`

**Last updated**: 2026-06-29

---

## Why Agent Observability Is Different

Traditional software is deterministic: given the same input, you get the same output. Debugging means reading stack traces and stepping through code paths that are fully defined at write-time.

AI agents are **non-deterministic**. The LLM decides which tools to call, in what order, and with what arguments. Behavior emerges from the interaction of prompts, tools, memory, and external state — not from code alone. As a result, "you don't know what your agent will do until your users use it." (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)

This means:
- Code is no longer the source of truth — **traces are**
- Debugging is not about reading code paths but about reconstructing the **decision context at each step**
- Correctness is largely discovered in production, not proven before release

## The Three Observability Primitives

### Runs
A single execution step: one LLM call with its specific inputs and outputs. A run captures the system prompt, available tools, the AI's message, any tool calls made, and reasoning blocks (if extended thinking is enabled). Runs are the atomic unit of agent observability.

### Traces
A complete agent execution — all runs stitched together in chronological order, showing how each step influenced the next. Because earlier LLM calls shape later decisions, you need the full trace to understand *why* the agent behaved as it did at any given point. (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)

Traces are the primary debugging artifact for agents, equivalent to what stack traces are for software.

### Threads
Multi-turn conversations grouping multiple traces over time. A thread captures the full history of an agent interacting with a user across sessions. This is essential for agents with memory: a response in turn 3 may only make sense given what was said in turn 1. (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)

| Primitive | Scope | Use |
|-----------|-------|-----|
| Run | Single LLM call | Inspect one decision |
| Trace | Full agent execution | Debug a complete task |
| Thread | Multi-turn conversation | Understand long-running context |

## The Three Telemetry Pillars

Complete agent observability requires three complementary signal types — not just traces: (source: 2026-06-29_Agentcore_observability_AWS)

| Pillar | Tells you | Examples |
|--------|-----------|---------|
| **Logs** | What happened | Tool call inputs/outputs, LLM responses, errors |
| **Traces** | How it happened (execution path) | Span chain from goal to completion |
| **[[metrics]]** | How much / how well | Latency, token counts, error rates, cost |

These three pillars are complementary: logs give the raw record, traces give the causal chain, metrics give the aggregate picture for alerting and trending.

## OpenTelemetry — The Open Standard

Agent observability implementations increasingly converge on **OpenTelemetry (OTEL)** as the vendor-neutral standard, avoiding lock-in to any single platform. (source: 2026-06-29_Agentcore_observability_AWS)

**Core OTEL concepts mapped to agent primitives:**

| OTEL term | Agent equivalent | Description |
|-----------|-----------------|-------------|
| Span | Run | One action (LLM call, tool execution) — a JSON object with inputs, outputs, timing |
| Trace | Trace | Chain of spans tied together by a unique **Trace ID** |
| Session | Thread | Multi-turn conversation grouping multiple traces |

**Distributed tracing across systems**: When agents call across microservices, MCP servers, or separate microVMs, OTEL headers carry the Trace ID transparently across process boundaries. The entire multi-agent execution — orchestrator calling sub-agents on different runtimes — appears as a single unified trace with a tree-view showing per-component latency. (source: 2026-06-29_Agentcore_observability_AWS)

**OTEL Baggage**: Custom metadata (e.g. tenant ID, business unit, user tier) can be attached to a trace and automatically propagated across all service boundaries — enabling filtering and segmentation of traces without modifying each service.

Popular agent frameworks (Strands, LangGraph, CrewAI) are supported out of the box by OTEL-based platforms, which translate differing telemetry payloads into a unified view.

## How Traces Enable Debugging

1. **Manual debugging**: Run the agent locally on an ad-hoc query, inspect every run in the trace, and find where the reasoning went wrong — ideally in an interactive playground.
2. **Reproducing production failures**: When a user reports incorrect behavior, find the production trace, extract the state at the failure point, and replay it locally. The trace gives you the exact inputs the agent saw.
3. **Pattern analysis**: AI-assisted tools can query across many traces to surface common failure modes, explain specific decisions ("why did the agent call this tool here?"), and compare successful vs. failed executions.

## Production Monitoring

### From Evals to Monitoring

Traditional evaluation runs before release against a static dataset. But because agents are **non-deterministic and unbounded** — they use tools, make API calls, and behave differently across users — pre-release testing systematically misses long-tail failure modes that only emerge at scale. (source: 2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt)

The proposed shift: **test before release AND monitor continuously in production**. Evals catch known failure modes; monitoring catches the unknown ones. This extends rather than replaces the traces-as-eval-dataset approach — production traces surface what to test offline next.

> Note: this complements rather than contradicts the [[agentic-ai-evaluation]] page — evals remain valuable for regression testing; monitoring adds the continuous production layer.

### Signals

Good signals are the foundation of reliable agent monitoring. Two categories: (source: 2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt)

#### Explicit Signals
Objective and verifiable — measurable without understanding semantics:
- **Error rate** — tool call failures, API errors
- **Latency** — time to completion per step and end-to-end
- **Regenerations** — how often the agent retries or backtracks
- **Cost** — token usage and API spend

#### Implicit Signals
Semantic and nuanced — require trained classifiers to detect reliably:
- **User frustration** — tone and phrasing indicating dissatisfaction
- **Refusals** — agent declining to complete a task
- **Task failures** — agent unable to reach the goal
- **Jailbreaking attempts** — adversarial user inputs
- **Laziness** — incomplete or low-effort outputs
- **Forgetting** — failure to maintain context across turns
- **Incorrect language** — responding in the wrong language
- **Positive wins** — explicit user satisfaction signals (important to track, not just failures)

Implicit signals are detected via trained models — making them cost-effective and scalable. Even simple regex patterns remain valid: Anthropic's own Claude codebase uses regex to detect negative user prompts. (source: 2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt)

### Production Experiments

Rather than relying solely on static benchmark datasets, test prompt and configuration changes by running them against real production traffic and measuring signal impact — effectively A/B testing in production. Even a few hundred events can yield statistically useful results when paired with a well-defined signal set. (source: 2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt)

This also applies to **non-chat agents**: tool failures and capability gaps are detectable as signals regardless of whether the agent's interface is conversational. Agents can be instrumented to autonomously diagnose and report their own issues.

## Security and Governance

Traces and logs necessarily contain the full context of agent interactions — which can include PII, proprietary business data, or sensitive tool outputs. This is a governance risk that must be addressed at the infrastructure level. (source: 2026-06-29_Agentcore_observability_AWS)

**Mitigation**: Apply data protection policies at the log-group level to automatically redact or mask sensitive fields before they are stored or indexed. This decouples observability completeness from data exposure risk — you can capture everything without retaining sensitive content.

This is distinct from prompt-level guardrails (which prevent sensitive data from reaching the LLM) — log-level redaction protects data *after* the agent has run.

## Related Pages

- [[agentic-ai-evaluation]]
- [[agentic-ai-definition]]
- [[agentic-ai-failures]]
- [[harness-engineering]]
- [[agentic-ai-memory]]
- [[metrics]]
