# Agentic Collaboration

**Summary**: Building AI agents that connect and work together requires solving two distinct problems — external connectivity (MCP) and internal orchestration (ADK) — which are complementary, not competing, approaches.

**Sources**: `2026-05-19_MCP vs ADK_ How Modern AI Agents Connect and Work Together.txt`

**Last updated**: 2026-05-19

---

## The two core problems

Developers building [[agentic-ai-definition|agentic AI systems]] beyond simple chatbots face two fundamental questions:

1. **Connectivity** — How does an agent access external tools and data (APIs, databases, files, the web)?
2. **Orchestration** — How do you structure, run, and coordinate the agent itself, especially across multiple agents?

MCP and ADK each solve one of these problems. (source: `2026-05-19_MCP vs ADK_...`)

---

## MCP — Model Context Protocol

**What it is**: An open standard created by Anthropic that defines a clean, reusable protocol for how LLMs and agents communicate with external tools and data sources.

**Before MCP**: Every external integration required custom code — a new adapter per tool, per model. Non-reusable and expensive to maintain.
When you define tools directly in the agent, the agent owns everything. 
Without MCP every agent that wants weather data has to re-implement the tool or import your python module directly 

**How it works**:
- Defines a protocol (JSON-RPC) between an **LLM host** (the agent) and **MCP servers** that expose tools or data
- Local communication via standard input/output (e.g., IDE plugins accessing a filesystem)
- Remote communication via HTTP with streaming and authentication tokens

**Three key primitives**:
| Primitive | What it is |
|-----------|-----------|
| **Tools** | Functions the agent can call (e.g., "search the web", "run SQL query") |
| **Resources** | Data the agent can read (e.g., files, documentation, databases) |
| **Prompts** | Pre-built, reusable prompt templates |

**Key advantages**:
- **Reusability**: Write an MCP server wrapper once — any MCP-compatible client can use it, regardless of which LLM powers the agent
- **Model-agnostic**: Works with Claude, GPT, Gemini, and local models
- **Growing ecosystem**: Ready-made MCP servers exist for GitHub, Slack, Google Drive, Postgres, Jira, Figma, and more
- Separation of concerns: tool servers can be maintained, versioned, and deployed independently from agents that use them
- Multiple tools from one server: a single MCP server can expose dozens of tools and any agent just connects and gets them all via tools/list

(source: `2026-05-19_MCP vs ADK_...`)

---

## ADK — Agent Development Kit

**What it is**: An open-source Python framework from Google that provides structure for building and orchestrating AI agents, moving beyond simple LLM-plus-prompt setups.

**Core building blocks**: Agents, Tools, Memory, Events, Runners.

### Agent types

| Type | When to use |
|------|------------|
| **LLM-driven** | Flexible reasoning tasks — classic "think and act" loops |
| **Workflow** | Critical paths requiring strict control flow (sequential, loop, parallel steps) |
| **Custom** | Specialised behaviour not covered by the above |

Workflow agents are important: they allow developers to hardcode structure for predictable paths, reducing reliance on LLM decision-making where consistency matters more than flexibility.

### The Runner / yield mechanism

ADK's execution model separates the **Agent** (reasoning) from the **Runner** (control):

1. A user query arrives at the Runner
2. The Runner passes it to the Agent
3. The Agent executes its reasoning loop and *yields* back to the Runner when it needs to take an external action or report a state change
4. The Runner processes the update, handles side effects, and passes information back

This `yield` pattern makes agent behaviour **predictable and debuggable** — the Runner always has full control between steps, preventing runaway execution.

### Memory

- **Session state**: short-term working memory within a single conversation
- **Long-term memory**: persists across sessions (e.g., user preferences, past learnings)

### Multi-agent support

ADK is particularly strong for complex multi-agent architectures — a root orchestrator can delegate to specialised sub-agents (research, writing, validation) and even call other agents as tools. This directly implements the Level 4 pattern described in [[agentic-ai-definition]]. (source: `2026-05-19_MCP vs ADK_...`)

---

## MCP vs ADK: complementary layers

The choice is not "which one" — it is "which problem am I solving right now?":

| | MCP | ADK |
|--|-----|-----|
| **Solves** | Connectivity to external tools and data | Internal agent structure and orchestration |
| **Analogy** | The standardised plug/socket interface | The electrical system inside the building |
| **Scope** | Cross-agent, cross-model protocol | Single framework for building agents |
| **Created by** | Anthropic | Google |

In practice they compose: an ADK agent can register MCP servers as tool sources, getting structured orchestration *and* standardised connectivity in the same system. Together they address the engineering gaps that lead to the [[agentic-ai-failures|failure modes]] of unsafe tool use and hallucinated planning. (source: `2026-05-19_MCP vs ADK_...`)

---

## Related pages

- [[agentic-ai-definition]]
- [[agentic-ai-failures]]
- [[agent-os]]
