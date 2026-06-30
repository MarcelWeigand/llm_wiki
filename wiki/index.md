# Wiki Index

Table of contents for all wiki pages.

---

## Agentic AI

- [agentic-ai-definition.md](Agentic%20AI/agentic-ai-definition.md) — What agentic AI is; the plan-act-observe-adapt loop; four-level autonomy spectrum from chatbots to multi-agent systems; five-type classification by reasoning architecture (reflex → model-based → goal-based → utility-based → learning)
- [agentic-ai-failures.md](Agentic%20AI/agentic-ai-failures.md) — Three main failure modes: infinite loops, hallucinated planning, unsafe tool use
- [agent-os.md](Agentic%20AI/agent-os.md) — The Agent OS: coordination layer providing scheduling, memory, tool management, identity, observability, and guardrails
- [agentic-collaboration.md](Agentic%20AI/agentic-collaboration.md) — MCP (connectivity) and ADK (orchestration): the two complementary standards for connecting and coordinating AI agents
- [agentic-ai-scaling.md](Agentic%20AI/agentic-ai-scaling.md) — Why scaling agentic AI is a system design problem; single-agent failure modes at scale; multi-agent decomposition; horizontal vs vertical scaling
- [context-engineering.md](Agentic%20AI/context-engineering.md) — The information design layer of the harness: what goes into the context window, static vs dynamic context, four primitives, GitHub Copilot vs Claude Code
- [harness-engineering.md](Agentic%20AI/harness-engineering.md) — The four harness layers (context, permissions, execution, observation); iterative constraint-building mindset; vibe coding vs agentic engineering
- [agentic-ai-memory.md](Agentic%20AI/agentic-ai-memory.md) — Four memory types for AI agents: working memory, semantic memory, procedural memory (skills), and episodic memory
- [agentic-building.md](Agentic%20AI/agentic-building.md) — Four paths for deploying AI agents: managed platform, foundation model infra, custom infra, and no-code
- [agentic-ai-observability.md](Agentic%20AI/agentic-ai-observability.md) — Three observability primitives (runs, traces, threads); why traces replace stack traces for non-deterministic agents
- [agentic-ai-evaluation.md](Agentic%20AI/agentic-ai-evaluation.md) — Three evaluation scopes (single-step, full-turn, multi-turn) and timings (offline, online, ad hoc); how traces power all evaluation strategies
- [llm-security.md](Agentic%20AI/llm-security.md) — OWASP Top 10 for LLM Applications 2025: prompt injection, excessive agency, supply chain, data poisoning, and 6 more threats with defenses

## Solution Architect

- [foundations/Overview.md](AI%20Solution%20Architect/foundations/Overview.md) — The 4 orthogonal AI dimensions: Capability, Application Domain, Learning Paradigm, Model Architecture
- [foundations/Metrics.md](AI%20Solution%20Architect/foundations/Metrics.md) — Metrics by capability type with use case examples
- [foundations/model-architectures/neural-networks.md](AI%20Solution%20Architect/foundations/model-architectures/neural-networks.md) — How each neural network family works, best data types, and when to use it (MLP, CNN, RNN/LSTM, Transformer, GNN)
- [domains/Computer Vision.md](AI%20Solution%20Architect/foundations/application-domains/Computer%20Vision.md) — All CV sub-tasks mapped to the 4 dimensions with architecture and metric guidance
- [foundations/data-readiness.md](AI%20Solution%20Architect/foundations/data-readiness.md) — Six-dimension data readiness framework (availability, volume, quality, labels, governance, architecture) with traffic-light scoring
- [foundations/solution-architecture-patterns.md](AI%20Solution%20Architect/foundations/solution-architecture-patterns.md) — Six end-to-end AI deployment patterns: batch, real-time API, RAG, agentic, human-in-the-loop, edge/embedded
- [regulations/2.1 - Regulated industries.md](AI%20Solution%20Architect/regulations/2.1%20-%20Regulated%20industries.md) — AI constraints in regulated industries
- [regulations/2.2 - EU_AI_Act.md](AI%20Solution%20Architect/regulations/2.2%20-%20EU_AI_Act.md) — EU AI Act summary for solution architects
- [use-cases/0-overview.md](AI%20Solution%20Architect/use-cases/0-overview.md) — Navigation page: lifecycle map and which page to use at each step
- [use-cases/1-ideation.md](AI%20Solution%20Architect/use-cases/1-ideation.md) — Half-day ideation workshop: generating a longlist of AI use case candidates
- [use-cases/2-feasibility.md](AI%20Solution%20Architect/use-cases/2-feasibility.md) — Full-day feasibility workshop: scoring and ranking shortlisted use cases
- [use-cases/3-scoping.md](AI%20Solution%20Architect/use-cases/3-scoping.md) — Phase-based WBS, effort multipliers, and scoping document template
- [use-cases/4-requirements.md](AI%20Solution%20Architect/use-cases/4-requirements.md) — Requirements engineering for AI: functional, non-functional, data, and integration requirements
- [use-cases/5-production-rollout.md](AI%20Solution%20Architect/use-cases/5-production-rollout.md) — PoC to production: business, management, and technical best practices; failure modes; go/no-go checklist
- [use-cases/technical-framework.md](AI%20Solution%20Architect/use-cases/technical-framework.md) — Decision guide: maps any AI use case to its 4 dimensions and architecture
- [use-cases/build-vs-buy.md](AI%20Solution%20Architect/use-cases/build-vs-buy.md) — When to use vendor API, RAG, fine-tune, or train from scratch — decision guide with matrix and common mistakes
- [use-cases/business-case-roi.md](AI%20Solution%20Architect/use-cases/business-case-roi.md) — Four value levers, ROI framework, executive business case structure, and common pitfalls
- [use-cases/catalog-manufacturing.md](AI%20Solution%20Architect/use-cases/catalog-manufacturing.md) — Manufacturing AI use cases with deep dives and AI dimensions
- [use-cases/catalog-healthcare.md](AI%20Solution%20Architect/use-cases/catalog-healthcare.md) — Healthcare AI use cases (placeholder)
- [use-cases/catalog-merantix.md](AI%20Solution%20Architect/use-cases/catalog-merantix.md) — Merantix-specific use case examples

## Machine Learning

- [Explainability.md](Machine_Learning/Explainability.md) — Model explainability (XAI): global vs local methods, SHAP, LIME, and feature importance techniques
- [ML Ops.md](Machine_Learning/ML%20Ops.md) — MLOps lifecycle: data management, experiment tracking, model registry, CI/CD, serving patterns, and drift detection
- [ML Deployment.md](Machine_Learning/ML%20Deployment.md) — Model deployment patterns: registry-at-runtime vs model-baked-in-image, trade-offs for each
- [Supervised ML - Metrics.md](Machine_Learning/Supervised%20ML%20-%20Metrics.md) — Regression and classification metrics: MAE, MSE, RMSE, R², and metrics for unbalanced datasets
- [Supervised ML - Classification Types.md](Machine_Learning/Supervised%20ML%20-%20Classification%20Types.md) — Four classification types: binary, multi-class, multi-label, and imbalanced

## RAG

*(no pages yet)*

## Robotics

*(no pages yet)*
