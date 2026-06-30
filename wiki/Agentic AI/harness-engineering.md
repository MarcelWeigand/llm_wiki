# Harness Engineering

**Summary**: The practice of building reliable scaffolding around AI agents — designing what they know, what they can do, what gets checked, and how failures become constraints.

**Sources**: `AI Driven software development lifecycle.md`

**Last updated**: 2026-06-27

---

## What is harness engineering?

Harness engineering is the practice of building reliable execution environments around AI models. An AI agent is only as good as the scaffolding it operates in — and that scaffolding must be deliberately designed.

The core mindset: **every mistake a model makes becomes a constraint in the harness**. Rather than trying to make the model perfect, you iteratively tighten the scaffolding — encoding failures as rules, guardrails, and task definitions — until the agent behaves reliably without manual correction.

---

## What the harness includes

The harness has four layers. [[context-engineering]] is one of them — the information design layer. The others cover what the agent can do, how its actions are executed, and how failures are caught:

| Layer | What it covers | Examples |
|---|---|---|
| **Context engineering** | What the model sees | `CLAUDE.md`, skills, RAG, examples, memory |
| **Tool / permission layer** | What the model can do | Approved tools, sandboxing, least-privilege access |
| **Execution layer** | How actions are run | Hooks, retries, step limits, rollback mechanisms |
| **Observation layer** | How failures are caught | Monitoring, drift detection, human checkpoints |

The iterative mindset applies to all four layers. Some mistakes get fixed by adding a rule to the context layer (`CLAUDE.md`), others by adding a hook (execution), others by restricting a tool permission (access control). Knowing which layer to fix is the core skill of harness engineering.

---

## From vibe coding to agentic engineering

There is a spectrum of how developers work with AI coding agents:

```
Vibe coding          →       Agentic engineering
─────────────────────────────────────────────────
"Write me a function     "Here are my constraints,
 that does X"             my test suite, my schema,
                          my coding standards —
                          now build this feature end-to-end"
```

Vibe coding is prompt-level: you describe what you want and accept what you get. Agentic engineering is harness-level: you invest upfront in standing context, skills, and guardrails so the agent can work reliably with minimal hand-holding.

The bottleneck in agentic engineering is currently **requirements engineering** — translating intent into constraints the harness can enforce. A vague intent produces a vague harness; a precise scope document (see [[4-requirements]]) produces precise constraints.

![[Pasted image 20260627194718.png]]

![[Pasted image 20260627194816.png]]

---

## The iterative approach

1. Start with minimal standing context
2. Run the agent on a real task
3. When it makes a mistake, ask: which layer needs a constraint? Rule (context), guardrail (execution hook), tool restriction (permission), or task definition (skill)?
4. Encode the fix at the right layer
5. Repeat

Over time the harness gets tighter and the agent gets more reliable — not because the model improved, but because the scaffolding leaves less room for error.

![[Pasted image 20260627194940.png]]
![[Pasted image 20260627195401.png]]
![[Pasted image 20260627195440.png]]

---

## Related pages

- [[context-engineering]] — The information design layer of the harness in depth
- [[agentic-building]] — Deployment paths for AI agents
- [[agentic-ai-definition]]
- [[agent-os]]
