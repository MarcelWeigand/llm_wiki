# Context Engineering for AI Coding Agents

**Summary**: The information design layer of the harness — what goes into an AI agent's context window, the static vs dynamic decision, and how the four primitives map across GitHub Copilot and Claude Code.

**Sources**: `AI Driven software development lifecycle.md`, `wiki/GitHub Copilot Features.md`

**Last updated**: 2026-06-27

---

## What is context engineering?

Context engineering is the information design layer of the [[harness-engineering|harness]]. Of the four harness layers (context, tool permissions, execution, observation), context engineering is the one you tune most frequently and the one with the most direct influence on output quality.

More precisely: the discipline of **structuring knowledge so that intelligence can act on it effectively** — designing and optimizing everything the model sees before it generates a response.

Where prompt engineering focused on crafting a single message well, context engineering is about the whole information environment the agent operates in — what it always knows, what it loads on demand, what it retrieves dynamically, and what it discards.

---

## What goes into the context window

A model's context window can contain six types of information:

| Type | What it is | Example |
|---|---|---|
| **Instructions** | System prompts, rules, personas, constraints | `CLAUDE.md`, `agents.md`, skills |
| **Examples** | Few-shot demonstrations of desired input/output | Sample outputs appended to a prompt |
| **Memory** | Relevant information retrieved from past conversations or external storage | Retrieved conversation summaries, user preferences |
| **State** | Current application state, tool results, conversation history | File contents just read, test results just run |
| **Retrieved knowledge** | Documents, DB results, search outputs pulled in dynamically | RAG — see [[RAG]] |
| **Tool outputs** | Results from function calls, code execution, API responses | Output of a bash command, a grep result |

**Key skill: deciding what to leave out.** Noise hurts as much as missing information. Models are sensitive to position (earlier = more weight) and token limits force compression. Structuring context with clear delimiters (XML tags, markdown headers) helps the model parse it reliably.

---

## Static vs dynamic context

The most important design decision in context engineering is whether a piece of information should be **always present** or **loaded on demand**.

| | Static context | Dynamic context |
|---|---|---|
| **Loaded** | Every session, automatically | Only when the task calls for it |
| **Examples** | `CLAUDE.md`, `copilot-instructions.md` | Skills, prompts, RAG-retrieved chunks |
| **Best for** | Rules, constraints, shared mental model | Specialist knowledge, large workflows, task-specific data |
| **Risk** | Context bloat — loads even when irrelevant | Forgotten if never invoked |

![[Pasted image 20260627195032.png]]
![[Pasted image 20260627195127.png]]

**Skills are the primary dynamic context mechanism** in both Claude Code and GitHub Copilot. Rather than embedding every piece of specialized knowledge into the agent's system prompt, skills allow the agent to remain a lightweight generalist that flexes into a specialist role on demand — a reusable system prompt fragment that loads only when needed.

The `/ingest` skill in this wiki is an example: the full ingest workflow is only loaded when explicitly invoked, not on every session.

---

## The four core primitives

Both GitHub Copilot and Claude Code are AI coding agents. Despite different names, they share the same four primitives:

| Primitive | Purpose | Trigger |
|---|---|---|
| **Standing context** (static) | Rules and facts the agent always has | Every session, automatic |
| **On-demand tasks** (dynamic) | Stored workflows you invoke explicitly | You call it by name |
| **Specialized agents** | Separate agent instances with their own scope | Spawned for a specific job |
| **Automated triggers** | Actions that fire on events without you asking | Event-driven |

---

## How the primitives map across tools

| Primitive | GitHub Copilot | Claude Code |
|---|---|---|
| **Standing context** | `agents.md`, `.github/copilot-instructions.md` | `CLAUDE.md` (global → project → subfolder hierarchy) |
| **On-demand tasks** | **Prompts** | **Skills** (`.claude/commands/*.md`) |
| **Specialized agents** | **Custom agents** (`@docs-agent`, `@backend-agent`) | **Subagents** (Agent tool) |
| **Automated triggers** | **Hooks**, **Workflows** (GitHub Actions) | **Hooks** |

> **Naming trap**: GitHub Copilot calls its on-demand tasks "prompts" and its agent capability packages "skills." Claude Code calls its on-demand tasks "skills." These are different things with the same word — don't conflate them.

---

## When to use each primitive

### Standing context — use for rules that always apply
The right place for constraints that should never be forgotten: coding standards, wiki page format, folder structure, the 4 AI dimensions.

**Example (this wiki):** `CLAUDE.md` tells Claude to always update `index.md` and `log.md` after changes, to never modify `raw/`, and to anchor ML content to the 4 AI dimensions. These apply to every conversation — loading them on demand would mean they get forgotten.

**Wrong use:** Putting a complex multi-step workflow in CLAUDE.md. It loads every session whether needed or not, wastes context, and adds noise.

---

### On-demand tasks — use for explicit workflows
A stored prompt you invoke by name when you want to do a specific job. Not standing rules, not a specialist agent — just a reusable task definition.

**Example (Claude Code):** `/ingest` — the full ingest workflow for adding a YouTube summary to the wiki. Only relevant when explicitly ingesting a file, so it lives as a skill, not in CLAUDE.md.

**Example (GitHub Copilot):** A "write-release-notes" prompt that summarizes commits since the last tag into a structured changelog. You invoke it once per release.

**Rule of thumb:** If you find yourself writing the same multi-step instruction in chat more than twice, make it a skill/prompt.

---

### Specialized agents — use for isolated, bounded jobs
A separate agent instance with its own context window and potentially its own scope, tools, or instructions. Use when the job is large enough that you don't want it in your main context, or when you need parallel work.

**Example (GitHub Copilot):** `@docs-agent` — configured to only read and write markdown documentation. `@backend-agent` — knows your DB schema, API conventions, and always writes tests alongside new endpoints.

**Example (Claude Code):** The `Agent` tool spawns a subagent with a fresh context window. Use it for a large codebase search, a security review, or running tests — jobs where the output is what matters, not the working history.

**Key difference from on-demand tasks:** A skill injects instructions into *your* conversation. A subagent runs *separately* and returns a result. If you need the intermediate reasoning, use a skill. If you just need the answer, use a subagent.

---

### Automated triggers — use for guardrails that run without asking
Event-driven actions that fire on a specific trigger (file save, pre-commit, every prompt) without you invoking them. The right place for enforcement that must never be skipped.

**Example (GitHub Copilot hooks):** A hook that runs on every prompt to check for hardcoded secrets before Copilot responds.

**Example (Claude Code hooks):** A hook that runs after every tool call to enforce a linting check.

**Warning:** Hooks add latency to every interaction they fire on. Use them sparingly for high-value guardrails, not for optional enrichment.

---

## GitHub Copilot vs Claude Code

Both are AI coding agents. The difference is integration depth and design philosophy.

| | GitHub Copilot | Claude Code |
|---|---|---|
| **Primary home** | IDE (VS Code, JetBrains) + GitHub | CLI + IDE extensions |
| **Native integration** | GitHub PRs, code review, Actions, code search | General-purpose; integrates via CLI in any pipeline |
| **Agent model** | Named custom agents (`@backend-agent`) — persistent personas with fixed scope | Dynamic subagents spawned per-job via the Agent tool |
| **Standing context** | `agents.md` per agent + team-wide `copilot-instructions.md` | Hierarchical `CLAUDE.md`: global → project → subfolder |
| **Team vs solo** | Designed for team use — `copilot-instructions.md` enforces team standards across all members | Primarily single-user; project `CLAUDE.md` is shared via git |
| **CI/CD** | Workflows run natively in GitHub Actions | Runs via CLI; can be embedded in any CI pipeline |
| **Autonomy** | Copilot Workspace for autonomous multi-step tasks | Subagents + hooks enable autonomous multi-step work |
| **Harness granularity** | Agent-level scope (per agent persona) | Directory-level scope (CLAUDE.md per subfolder) |

**The core philosophical difference:** GitHub Copilot models specialization as **named agent personas** you switch between. Claude Code models it as **dynamic subagents** spawned for a job and discarded. Copilot's approach is more predictable; Claude Code's is more flexible.

---

## Related pages

- [[harness-engineering]] — The parent concept: full scaffolding around AI agents
- [[agentic-building]]
- [[agentic-ai-definition]]
- [[agent-os]]
