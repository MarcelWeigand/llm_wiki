# Agentic AI Definition

**Summary**: Agentic AI systems are LLMs embedded in a plan-act-observe-adapt loop that iteratively pursue goals using tools

**Sources**: `2026-05-15_Why Agentic AI Fails_ Infinite Loops, Planning Errors, and More.txt`, `2026-05-15_Why AI Agents Need an Operating System.txt`, `2026-05-15_Agentic AI Systems, Clearly Explained.txt`

**Last updated**: 2026-05-15

---
## What is an agentic AI system?

A common misconception is that an agentic AI system is simply an LLM with access to tools. It is a much larger system that operates in a continuous **plan-act-observe-adapt** loop:

1. **Plan** — decide what action to take next
2. **Act** — execute that action via a tool or API
3. **Observe** — receive the result
4. **Adapt** — revise the plan based on the result, then repeat

This loop is what gives agents their power — iterating towards more consistent results — but also what introduces failure modes that don't exist in single-shot LLM usage. (source: `2026-05-15_Why Agentic AI Fails_...`)

A simpler framing of the same idea is the **Reason → Act** loop: the model reasons about what to do next, acts via a tool, observes the result, and repeats. (source: `2026-05-15_Agentic AI Systems, Clearly Explained.txt`)

---

## The four-level spectrum

AI systems exist on a spectrum of autonomy. Understanding where a system sits on this spectrum clarifies what "agentic" does and does not mean. (source: `2026-05-15_Agentic AI Systems, Clearly Explained.txt`)

### Level 1 — Chatbots
Examples: ChatGPT, Claude, Gemini in their base form.

Passive and prompt-driven. They wait for input, respond, and have no memory of past sessions, no knowledge of your business context, and no ability to take actions. Every interaction starts from scratch.

### Level 2 — AI Workflows
Examples: n8n, Zapier, Make.com.

Automated pipelines that chain together fixed steps — e.g., pull a YouTube transcript, send it to an LLM with a hardcoded prompt, post the result to a scheduler. Faster than manual work, but not adaptive: the system cannot make judgment calls, change strategy mid-run, or respond to unexpected results.

### Level 3 — Agentic Workflows (single agent)
The key distinction from Level 2: the **model itself decides the execution path** rather than following a fixed script. Given a goal, the agent autonomously chooses which tools to call, in what order, and adapts based on intermediate results via the Reason → Act loop.

Limitation: a single agent still has no persistent memory across sessions — it cannot learn from past runs or accumulate knowledge over time.

### Level 4 — Agentic AI Systems (multi-agent)
A coordinated team of specialised agents running as an integrated system. Key additions over a single agent:

- **Persistent memory**: the system remembers past performance, learned lessons, and user preferences across sessions
- **Skills**: folders of task-specific instructions that agents load on demand (e.g., carousel creation, clip extraction)
- **MCPs (Model Context Protocols)**: standardised connectors to external tools — schedulers, analytics dashboards, CRMs — allowing agents to act across the full tool ecosystem
- **Human-in-the-loop checkpoints**: the system handles most tasks autonomously but pauses for human review before high-stakes actions (e.g., publishing content)

This level corresponds to what the [[agent-os]] pattern is designed to support. (source: `2026-05-15_Agentic AI Systems, Clearly Explained.txt`)

---

## Related pages

- [[agentic-ai-failures]]
- [[agent-os]]