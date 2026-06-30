# Wiki Log

Append-only record of all operations.

---

## 2026-05-15

**Source ingested**: `raw/youtube/2026-05-15_Why Agentic AI Fails_ Infinite Loops, Planning Errors, and More.txt`

**Pages created**:
- `Agentic AI/agentic-ai.md` — Agentic AI definition, plan-act-observe-adapt loop, and three failure modes (infinite loops, hallucinated planning, unsafe tool use)

**Index updated**: Added Agentic AI section with new page; scaffolded empty sections for Machine Learning, RAG, Robotics.

---

## 2026-05-15 (second ingest)

**Source ingested**: `raw/youtube/2026-05-15_Why AI Agents Need an Operating System.txt`

**Pages created**:
- `Agentic AI/agent-os.md` — Agent OS architecture: three-layer model, six kernel components, and how each addresses the failure modes in agentic-ai.md

**Pages updated**:
- `Agentic AI/agentic-ai.md` — Added source reference and link to agent-os.md

**Index updated**: Added agent-os.md to Agentic AI section.

---

## 2026-05-15 (third ingest)

**Source ingested**: `raw/youtube/2026-05-15_Agentic AI Systems, Clearly Explained.txt`

**Pages updated**:
- `Agentic AI/agentic-ai-definition.md` — Added: Reason → Act loop framing; four-level spectrum (chatbots → workflows → single agent → multi-agent systems); MCPs; skills; human-in-the-loop checkpoints

**Index updated**: Fixed paths to all three Agentic AI pages; updated description for agentic-ai-definition.md.

---

## 2026-05-19

**Source ingested**: `raw/youtube/2026-05-19_MCP vs ADK_ How Modern AI Agents Connect and Work Together.txt`

**Pages updated**:
- `Agentic AI/agentic-collaboration.md` — Written from scratch: MCP (connectivity protocol, primitives, ecosystem), ADK (orchestration framework, agent types, Runner/yield mechanism, memory, multi-agent support), and how the two compose together

**Index updated**: Added agentic-collaboration.md to Agentic AI section.

---

## 2026-06-09

**Source ingested**: `raw/youtube/2026-06-09_Building AI Agent Systems and Scaling Challenges in Agentic AI.txt`

**Pages updated**:
- `Agentic AI/agentic-ai-scaling.md` — Full rewrite from rough notes into proper wiki format: traditional vs agentic scaling, the agent loop under scale, error propagation (Washington example), system design as the core issue, multi-agent decomposition, horizontal vs vertical scaling trade-offs, and design principles for scalable systems

**Pages updated (cross-links added)**:
- `Agentic AI/agentic-ai-failures.md` — Added link to agentic-ai-scaling
- `Agentic AI/agentic-ai-definition.md` — Added link to agentic-ai-scaling

**Index updated**: Added agentic-ai-scaling.md to Agentic AI section.

---

## 2026-06-25

**Pages created**:
- `Solution Architect/foundations/model-architectures/neural-networks.md` — Per-architecture reference tables (MLP, CNN, RNN/LSTM, Transformer, GNN): how it works, best data types, when to use it; quick comparison summary table

**Index updated**: Added full Solution Architect section with all existing pages; added neural-networks.md entry.

---

## 2026-06-25 (second entry)

**New page created**: `wiki/Solution Architect/use-cases/Scoping.md`
- Covers AI project scoping and effort estimation: 5-phase WBS, complexity multipliers table, scoping document template, and overview of existing frameworks (CRISP-DM, ML Canvas, TDSP, MLOps maturity model)
- Written from conversation, not a raw source

**Index updated**: Added Scoping.md to Solution Architect use-cases section.

**Pages updated**: `wiki/Solution Architect/use-cases/Scoping.md`
- Added "What is scoping?" section: distinguishes scoping from feasibility, explains the three failures it prevents
- Added "Best practices" section: 8 concrete rules (success metric first, explicit data scope, out-of-scope list, PoC before production commitment, integration design, range estimates, named owner, annotation as separate workstream)

---

## 2026-06-25 (third entry)

**Restructured**: `wiki/Solution Architect/use-cases/` — full reorganization

Old files deleted:
- `3. Use Case Ideation + Feasibility Assessments.md`
- `2 - Framework for new AI use cases - technical and conceptional.md`
- `Scoping.md`
- `3.1 Use cases manufacturing - combined.md`
- `3.2 - Use cases Healthcare.md`
- `3.3 - Merantix Use cases.md`

New files created:
- `0-overview.md` — navigation page with lifecycle map and key distinctions
- `1-ideation.md` — ideation workshop (was Part 1 of the combined page)
- `2-feasibility.md` — feasibility workshop (was Part 2 of the combined page)
- `3-scoping.md` — scoping & effort estimation (was Scoping.md, content unchanged)
- `technical-framework.md` — AI dimension decision guide (was Framework page, content unchanged)
- `catalog-manufacturing.md` — manufacturing use cases (content unchanged)
- `catalog-healthcare.md` — healthcare placeholder
- `catalog-merantix.md` — Merantix examples (content unchanged)

`wiki/index.md` updated to reflect new structure.

---

## 2026-06-25 (fourth entry)

**New page created**: `wiki/Solution Architect/use-cases/4-requirements.md`
- Requirements engineering for AI projects: what makes it different from classical software (probabilistic requirements, data as first-class requirement, post-PoC revision), four requirement types (functional, non-functional, data, integration), when to run it, and common failures

**Page updated**: `wiki/Solution Architect/use-cases/0-overview.md`
- Added requirements engineering as Step 4 in the lifecycle diagram and table
- Added key distinction between scoping and requirements engineering

`wiki/index.md` updated with new entry.

---

## 2026-06-25 (fifth entry)

**Restructured**: `wiki/Agentic AI/context-engineering.md` split into two pages — 2026-06-27
- New page `harness-engineering.md`: what the harness includes (4-layer table), from vibe coding to agentic engineering, iterative approach + 5 images moved from context-engineering
- `context-engineering.md` updated: reframed as the information design layer of the harness, removed harness-engineering sections, updated Summary and Related pages
- `wiki/index.md` updated with new harness-engineering.md entry

---

**Wiki lint applied** — 2026-06-27

Broken links fixed:
- `2.1 - Regulated industries.md` — updated 2 stale links (`[[2 - Framework...]]` → `[[technical-framework]]`, `[[1 - Overview]]` → `[[Overview]]`)
- `2.2 - EU_AI_Act.md` — same 2 fixes
- `context-engineering.md` — removed 4 dead `[[harness-engineering]]` links (file deleted), removed from Sources

Index fixed:
- Solution Architect section: all 15 entries now have correct `AI%20Solution%20Architect/` prefix paths
- Machine Learning section: added 5 pages (Explainability, ML Ops, ML Deployment, Supervised ML Metrics, Supervised ML Classification Types)
- Agentic AI section: added `agentic-ai-memory.md` and `agentic-building.md`

Page format headers added to 7 pages:
- `Machine_Learning/Explainability.md`, `ML Ops.md`, `ML Deployment.md`, `Supervised ML - Metrics.md`, `Supervised ML - Classification Types.md`
- `Agentic AI/agentic-ai-memory.md`, `agentic-building.md`

---

**New page created**: `wiki/Agentic AI/context-engineering.md`
- The four context engineering primitives (standing context, on-demand tasks, specialized agents, automated triggers)
- Mapping across GitHub Copilot and Claude Code with naming-trap callout
- When to use each primitive with concrete examples
- GitHub Copilot vs Claude Code comparison table
- Harness engineering mindset section
- `wiki/index.md` updated

**Page updated**: `wiki/Agentic AI/context-engineering.md`
- Integrated content from `AI Driven software development lifecycle.md`
- Added formal definition of context engineering (evolution of prompt engineering)
- Added "What goes into the context window" table (instructions, examples, memory, state, retrieved knowledge, tool outputs)
- Added "Static vs dynamic context" section with design decision framing
- Added "From vibe coding to agentic engineering" spectrum with link to [[4-requirements]] and [[harness-engineering]]

---

## 2026-06-30 (second entry)

**Page updated**: `Agentic AI/agentic-ai-memory.md`
- Added short-term vs. long-term labels to each of the four memory types, with a one-sentence definition: working memory = short-term (lasts one session); semantic, procedural, and episodic = long-term (persist across sessions)
- Written from conversation, not a raw source

---

## 2026-06-30

**Source ingested**: `raw/youtube/2026-06-30_5 Types of AI Agents_ Autonomous Functions & Real-World Applications.txt`

**Pages updated**:
- `Agentic AI/agentic-ai-definition.md` — Added "Classification by reasoning architecture" section: the five classic agent types (Simple Reflex, Model-Based Reflex, Goal-Based, Utility-Based, Learning Agent) with definitions, examples, and the Learning Agent's four components (performance element, critic, learning element, problem generator); added a note clarifying this is orthogonal to the existing four-level autonomy spectrum; summary table included

**Index updated**: Updated agentic-ai-definition.md description to mention the new five-type classification.

---

## 2026-06-29 (eighth entry)

**Four new pages created** — written from conversation, not a raw source:

- `wiki/AI Solution Architect/foundations/data-readiness.md` — Six-dimension data readiness framework with traffic-light scoring; data architecture patterns for AI; used as a gate before scoping
- `wiki/AI Solution Architect/foundations/solution-architecture-patterns.md` — Six end-to-end patterns (batch, real-time API, RAG, agentic, human-in-the-loop, edge); comparison table; decision guide for pattern selection
- `wiki/AI Solution Architect/use-cases/build-vs-buy.md` — Four options (API, RAG, fine-tune, train from scratch); decision tree; decision matrix; common mistakes
- `wiki/AI Solution Architect/use-cases/business-case-roi.md` — Four value levers with quantification formulas; ROI framework with cost categories and time to value; executive business case structure; pitfalls

**Pages updated**:
- `foundations/Overview.md` — Added "Foundations reference pages" section linking all foundation pages
- `use-cases/0-overview.md` — Added build-vs-buy and business-case-roi as reference tools in the lifecycle table

**Index updated**: Added all 4 new pages to Solution Architect section.

---

## 2026-06-29 (seventh entry)

**New page created**: `wiki/Solution Architect/use-cases/5-production-rollout.md`
- Written from conversation, not a raw source
- Covers PoC → production transition from three perspectives: business (exit criteria, champion, cost), management (product owner, governance, compliance, comms), technical (reproducibility, monitoring, drift, shadow mode, fallback, integration, security)
- Includes failure modes table with root causes and preventions, and a go/no-go checklist

**Page updated**: `wiki/Solution Architect/use-cases/0-overview.md`
- Extended lifecycle from 4 to 5 steps: added Production Rollout as Step 5
- Updated lifecycle diagram to show PoC/Pilot as a milestone between Requirements and Production Rollout
- Added note distinguishing PoC from production rollout

**Index updated**: Added 5-production-rollout.md to Solution Architect section.

---

## 2026-06-29 (sixth entry)

**Source ingested**: `raw/youtube/2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt`

**Pages created**:
- `Agentic AI/llm-security.md` — Full OWASP Top 10 for LLM Applications 2025: all 10 threats with explanations, defenses, and a threat-map table linking each to its engineering mitigation layer

**Pages updated**:
- `Agentic AI/agentic-ai-failures.md` — Added cross-reference to [[llm-security]] in Related pages (excessive agency is the security framing of unsafe tool use)

**Index updated**: Added llm-security.md to Agentic AI section.

---

## 2026-06-29 (fifth entry)

**Summary generated**: `wiki/Agentic AI/Summary.md`
- Created full summary table for `wiki/Agentic AI/` covering 11 topics: Definition, Failures, Agent OS, Memory, Collaboration (MCP+ADK), Building & Deploying, Scaling, Harness Engineering, Context Engineering, Observability, Evaluation
- Skipped `Github Copilot Features.md` (stub — mostly image references)
- Ordered rows foundational → operational

---

## 2026-06-29 (fourth entry)

**Restructured**: `wiki/Agentic AI/agentic-ai-observability.md`
- Moved "The Three Observability Primitives" before "The Three Telemetry Pillars" (foundational before framework)
- Merged "From Evals to Monitoring", "Production Monitoring Signals", "Production Experiments" into one "Production Monitoring" section with subsections
- Moved "Security and Governance" to end of page (operational concern, not part of conceptual flow)
- Updated Summary to reflect full scope of page after three ingestions
- Added inline [[metrics]] link in the Telemetry Pillars table

---

## 2026-06-29 (third entry)

**Source ingested**: `raw/youtube/2026-06-29_Agentcore_observability_AWS`

**Pages updated**:
- `Agentic AI/agentic-ai-observability.md` — Added three new sections: "The Three Telemetry Pillars" (Logs/Traces/Metrics triad); "OpenTelemetry Standard" (Spans/Trace IDs/Sessions, distributed tracing via OTEL headers across multi-agent runtimes, OTEL Baggage for metadata propagation, framework support); "Security and Governance" (log-level PII redaction decoupled from prompt guardrails)

---

## 2026-06-29 (second entry)

**Source ingested**: `raw/youtube/2026-06-29_Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.txt`

**Pages updated**:
- `Agentic AI/agentic-ai-observability.md` — Added three new sections: "From Evals to Monitoring" (evals vs. continuous monitoring distinction), "Production Monitoring Signals" (explicit: error rate/latency/regenerations/cost; implicit: frustration/refusals/task failures/jailbreaking/laziness/forgetting/wins — detected via trained classifiers + regex), "Production Experiments" (A/B testing in production, non-chat agent applicability)
- `Agentic AI/agentic-ai-evaluation.md` — Added "Evals vs. Monitoring" sub-section clarifying that evals and monitoring are complementary, not alternatives; linked to observability page for signal taxonomy

---

## 2026-06-29

**Source ingested**: `raw/youtube/2026-06-29_Observability and Evals for AI Agents_ A Simple Breakdown.txt`

**Pages written from scratch**:
- `Agentic AI/agentic-ai-observability.md` — Three observability primitives (runs/traces/threads); why agents are non-deterministic; how traces replace stack traces; how observability enables debugging, offline eval datasets, and online monitoring
- `Agentic AI/agentic-ai-evaluation.md` — Three evaluation scopes (single-step, full-turn, multi-turn) mapped to runs/traces/threads; three timings (offline, online, ad hoc); how trace infrastructure powers all evaluation strategies; production as the discovery phase

**Index updated**: Added both new pages to Agentic AI section.

---

## 2026-06-27 (second entry)

**Page updated**: `wiki/Solution Architect/foundations/model-architectures/neural-networks.md`
- Added section "When to use neural networks on structured/tabular data": 5 conditions that override the tree-model default (scale, high-cardinality categoricals, multi-modal input, sequential row structure, differentiable system), plus note on specialist tabular NN architectures (TabNet, FT-Transformer, SAINT)
