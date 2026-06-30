# Agentic AI Evaluation

**Summary**: Evaluating AI agents means testing reasoning and emergent behavior across three scopes and three timings — all powered by the observability trace infrastructure.

**Sources**: `raw/youtube/2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt`, `raw/youtube/2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt`

**Last updated**: 2026-06-29

---

## Why Agent Evaluation Differs from Software Testing

Traditional software testing validates code paths defined at write-time — correctness is largely provable before release. Agent evaluation is different: because agents are non-deterministic, **production is the discovery phase**. You find out what needs to be tested by watching what actually happens in the wild, then build your eval suite from real traces. (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)

The shift: from testing code paths → testing **reasoning and decision quality**.

### Evals vs. Monitoring

Evals (offline evaluation against a curated dataset) are necessary but not sufficient. Because agents are also **unbounded** — they interact with real users across an open-ended space of inputs — pre-release testing systematically misses long-tail failure modes. The complement is continuous **production monitoring** with explicit and implicit signals. (source: 2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt)

- **Evals**: known failure modes, regression testing, benchmarking
- **Monitoring**: unknown failures, long-tail issues, real-time signal tracking

See [[agentic-ai-observability]] for the full signal taxonomy (explicit vs. implicit) and production experiment patterns.

## Three Evaluation Scopes

### Single-Step Evaluation
Validates a single agent decision in isolation — the unit test equivalent for agent reasoning. Asks: "did the agent make the right choice at this specific moment?" (e.g., did it check availability before scheduling a meeting?) Fast to run, clear pass/fail criteria, useful for regression testing individual tool-call decisions. (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)

### Full-Turn Evaluation (Trace)
Validates a complete agent run from input to final output — end-to-end trajectory assessment. Checks whether the agent performed well across multiple steps, including tool usage and state changes (e.g., did the coding agent produce working code?). Maps directly to a single [[agentic-ai-observability#Traces|trace]].

### Multi-Turn Evaluation (Thread)
Validates behavior across multiple conversation turns — the most realistic test of production behavior. Assesses whether the agent maintains context, remembers user preferences, and handles long-running interactions coherently. Maps to a [[agentic-ai-observability#Threads|thread]]. Hardest to set up but closest to real usage. (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)

| Scope | Maps to | Question it answers |
|-------|---------|---------------------|
| Single-step | Run | Did the agent make the right decision here? |
| Full-turn | Trace | Did the agent complete the task correctly? |
| Multi-turn | Thread | Does the agent behave coherently over time? |

## Three Evaluation Timings

### Offline (Pre-Ship)
Run before shipping to production against a static dataset. Good for catching regressions and benchmarking. The dataset is typically seeded from past production traces — a virtuous cycle where production failures become future regression tests.

### Online (Real-Time in Production)
Run immediately after each agent execution in production, without requiring ground truth. Useful for flagging issues before users report them. Common online checks: (source: 2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt)
- **Trajectory checks**: flag unusual or unexpected tool call patterns
- **Efficiency monitoring**: detect performance degradation trends
- **Quality scoring**: LLM-as-judge on live outputs
- **Failure alerts**: surface errors proactively

### Ad Hoc (Post-Ingestion Analysis)
Run some time after execution, triggered by user feedback or a hunch. Used for exploratory analysis — querying across traces to understand usage patterns, explain specific decisions, or compare successful vs. failed runs.

## How Observability Powers Evaluation

The trace infrastructure from [[agentic-ai-observability]] is not just for debugging — it is the foundation for all three evaluation strategies:

1. **Traces → Offline dataset**: Production traces become eval test cases. When a user reports failure, extract the trace, anonymize if needed, and add it as a regression test.
2. **Traces → Online evals**: Online evaluations run directly on production traces as they are captured — no separate data pipeline needed.
3. **Traces → Ad hoc insights**: AI-assisted analysis tools query across runs, traces, and threads to surface patterns and explain decisions.

This means investing in observability is not separate from evaluation — it *is* evaluation infrastructure.

## Related Pages

- [[agentic-ai-observability]]
- [[agentic-ai-failures]]
- [[harness-engineering]]
- [[agentic-ai-definition]]
