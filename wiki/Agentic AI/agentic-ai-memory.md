
# Agentic AI Memory

**Summary**: The four memory types AI agents can use — working memory (context window), semantic memory, procedural memory (skills), and episodic memory — and when each is needed.

**Last updated**: 2026-06-30

---

## Memory types that AI agents need

Each type is either **short-term** (lasts one session only) or **long-term** (persists across sessions until updated).

1. Working memory (RAM) = context window — **short-term**: exists only for the current conversation, discarded when the session ends
	1. size limit (biggest is one million)

2. Semantic memory — **long-term**: durable general knowledge that survives across sessions
	1. .md files or vector databases --> gets loaded into session
	2. general knowledge 
	3. knowledge is always present in context

3. Procedural memory = agent skills — **long-term**: durable task instructions that survive across sessions
	1. skill.md file 
	2. skills use progressive disclosure --> agent doesn't load all of its skills into the context window --> only the skills that matches the task are loaded

4. Episodic memory — **long-term**: durable record of what the agent learned on past runs, survives across sessions
	1. what it learned on previous runs 
	2. uses distillation = don't save everything from previous run, only the important information


--> not every agent needs necessarily all four
- simple reflex agent 
