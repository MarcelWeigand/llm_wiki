# Agentic AI Definition

**Summary**: Agentic AI systems are LLMs embedded in a plan-act-observe-adapt loop that iteratively pursue goals using tools

**Sources**: `2026-05-15_Why Agentic AI Fails_ Infinite Loops, Planning Errors, and More.txt`, `2026-05-15_Why AI Agents Need an Operating System.txt`, `2026-05-15_Agentic AI Systems, Clearly Explained.txt`, `2026-06-30_5 Types of AI Agents_ Autonomous Functions & Real-World Applications.txt`

**Last updated**: 2026-06-30

---
## What is an agentic AI system?

#### Loop

A common misconception is that an agentic AI system is simply an LLM with access to tools. It is a much larger system that operates in a continuous **plan-act-observe-adapt** loop:

1. **Plan** — decide what action to take next
2. **Act** — execute that action via a tool or API
3. **Observe** — receive the result
4. **Adapt** — revise the plan based on the result, then repeat

This loop is what gives agents their power — iterating towards more consistent results — but also what introduces failure modes that don't exist in single-shot LLM usage. (source: `2026-05-15_Why Agentic AI Fails_...`)

Example:
Notice the agent **decided on its own** to call three different tools, in a sensible order, before answering -- we never told it "first check weather, then flights, then hotels." That autonomous multi-step decision-making is the planning & reasoning loop at work.

**Key idea:** the loop is what makes the agent *autonomous* across multiple steps. Tools (Level 3) gave it hands; the loop gives it the ability to chain several actions together toward a goal.

A simpler framing of the same idea is the **Reason → Act** loop: the model reasons about what to do next, acts via a tool, observes the result, and repeats. (source: `2026-05-15_Agentic AI Systems, Clearly Explained.txt`)

Memory

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

## Classification by reasoning architecture

A second, orthogonal way to classify agents — by the sophistication of their internal reasoning, independent of how much autonomy or tool access they have in a system. This is the classic AI agent taxonomy. (source: `2026-06-30_5 Types of AI Agents_...`)

### Simple Reflex Agent — Reacts
Acts on predefined condition-action rules based only on the current perceived state ("what the world is like now"). No memory, no model of the environment. Example: a thermostat that turns on heat below a threshold. Effective in structured, predictable environments; fails in dynamic ones and cannot learn from past mistakes.

### Model-Based Reflex Agent — Remembers
Adds an internal model of the world: the agent's state, how the world evolves, and what its own actions do. This lets it infer parts of the environment it cannot currently observe. Example: a robotic vacuum that remembers cleaned areas and obstacles.

### Goal-Based Agent — Aims
Adds explicit goals. Uses its internal model to simulate the outcomes of possible actions ("what will it be like if I do Action A") and chooses actions that move it toward the goal, rather than simply matching a condition to a fixed action. Example: a self-driving car planning a route based on predicted outcomes of different turns.

### Utility-Based Agent — Evaluates
Adds a utility function: not just "does this reach the goal" but "how desirable is this outcome" (the expected utility of a future state). Ranks competing options and picks the best one, not just any option that satisfies the goal. Example: a drone delivery service optimizing simultaneously for speed, safety, and energy use.

### Learning Agent — Improves
The most adaptive type. Learns from experience via four components:
- **Performance element**: selects and executes actions — this is the agent behavior seen in the other four types
- **Critic**: observes outcomes via sensors and compares them to a performance standard, generating feedback
- **Learning element**: uses that feedback to update and improve the agent's behavior over time
- **Problem generator**: suggests new, exploratory actions to try rather than always doing what currently seems best

Example: a chess bot that learns from thousands of games, adjusting strategy based on wins and losses, and trying new moves suggested by the problem generator. (source: `2026-06-30_5 Types of AI Agents_...`)

### Summary table

| Type | Core capability | One-line |
|---|---|---|
| Simple Reflex | Condition → action rules | Reacts |
| Model-Based Reflex | + internal world model | Remembers |
| Goal-Based | + goal simulation | Aims |
| Utility-Based | + outcome ranking | Evaluates |
| Learning Agent | + critic/learning feedback loop | Improves |

### How this relates to the four-level spectrum

This classification is orthogonal to the four-level autonomy spectrum above: the reasoning-architecture axis describes *how sophisticated the agent's internal decision-making is*, while the autonomy spectrum describes *how much independence and tool access the agent has within a system*. A Level 3 single agent could internally be built as a goal-based or utility-based agent; a Level 4 multi-agent system typically combines learning agents with persistent memory and tool access.

Many complex use cases benefit from **multi-agent systems**, where multiple agents — potentially of different reasoning types — work cooperatively toward shared goals. Despite increasing sophistication, agents still perform best with a human in the loop for high-stakes decisions, at least for now. (source: `2026-06-30_5 Types of AI Agents_...`)

---

Different components of agents and their abstraction layer

![[Pasted image 20260626185259.png|395]]

---

## Related pages

- [[agentic-ai-failures]]
- [[agent-os]]
- [[agentic-ai-scaling]]