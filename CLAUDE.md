# LLM Wiki

A personal knowledge base maintained by Claude Code.
Based on Andrej Karpathy's LLM Wiki pattern.

## Purpose

This wiki is a structured, interlinked knowledge base for structuring all tech related knowledge gained from different podcast and youtube video summary files.
Claude maintains the wiki. The human curates sources, asks questions, and guides the analysis.

## Folder structure

```
app/                    -- code for the youtube summarizer, can be ignored entirely
raw/                    -- source documents (immutable -- never modify these)
raw/youtube             -- source documents from youtube
raw/podcasts            -- summarized source documents from podcasts
wiki/                   -- markdown pages maintained by Claude
wiki/Agentic AI         -- markdown pages maintained by Claude for the topic Agentic AI
wiki/Machine Learning   -- markdown pages maintained by Claude for the topic Machine Learning
wiki/Solution Architect -- markdown pages maintained by Claude for the topic Solution Architecture
wiki/RAG                -- markdown pages maintained by Claude for the topic RAG
wiki/Robotics           -- markdown pages maintained by Claude for the topic Robotics
wiki/index.md           -- table of contents for the entire wiki
wiki/log.md             -- append-only record of all operations
```

## Page types

Not every entity gets its own page. Use the following rules:

**Concept pages** (one file per concept): Major ideas, techniques, frameworks, and topics.
Examples for wiki/Agentic AI: `definition.md`, `main_ideas.md`, `common_failures.md`, `design_patterns.md`

## Page format

Every wiki page should follow this structure:

```markdown
# Page Title

**Summary**: One to two sentences describing this page.

**Sources**: List of raw source files this page draws from.

**Last updated**: Date of most recent update.

---

Main content goes here. Use clear headings and short paragraphs.

Link to related concepts using [[wiki-links]] throughout the text.

## Related pages

- [[related-concept-1]]
- [[related-concept-2]]
```

## AI dimensions — always apply

When writing or updating any wiki page, anchor content to these 4 orthogonal AI dimensions where relevant:

1. **Capability** — what does it do? (Predictive / Generative / Decision making)
2. **Application domain** — what type of data? (Tabular, Time series, Computer vision, NLP, ...)
3. **Learning paradigm** — how does it learn? (Supervised / Unsupervised / Self-supervised / RL)
4. **Model architecture** — what is it built with? (Linear / Tree / Neural network → CNN / RNN / Transformer)

These 4 dimensions are the shared frame of reference across the entire wiki. See `wiki/Solution Architect/foundations/Overview.md` for the full reference.

## Question answering

When the user asks a question:

1. Read `wiki/index.md` first to find relevant pages
2. Read those pages and synthesize an answer
3. Cite specific wiki pages in your response
4. If the answer is not in the wiki, say so clearly
5. If the answer is valuable, offer to save it as a new wiki page

Good answers should be filed back into the wiki so they compound over time.

## Writing content from conversation

When the user asks a question or requests an explanation (not an ingest):

1. Answer directly in the conversation first
2. If the content is substantial and reusable, offer to save it into an existing page or create a new one
3. Always prefer updating an existing page over creating a new one
4. Update `wiki/index.md` and append to `wiki/log.md` after any changes

**Perspective by subfolder** — adjust tone based on where the content lives:
- `wiki/Machine_Learning/` — practitioner perspective: concrete, technical, actionable. No source citations needed; state well-established facts directly.
- `wiki/Solution Architect/` — consulting perspective: structured, client-facing ready. Frame opinions as "in practice..." or "as an SA rule of thumb..."
- `wiki/Agentic AI/`, `wiki/RAG/`, `wiki/Robotics/` — cite the source file after factual claims: (source: filename.txt)

## Lint

When the user asks you to lint or audit the wiki:

- Check for contradictions between pages
- Find orphan pages (no inbound links from other pages)
- Identify concepts mentioned in pages that lack their own page
- Flag claims that may be outdated based on newer sources
- Check that all pages follow the page format above
- Report findings as a numbered list with suggested fixes

## Rules

- Never modify anything in the `raw/` folder
- Always update `wiki/index.md` and `wiki/log.md` after changes
- Keep page names lowercase with hyphens (e.g. `machine-learning.md`)
- Write in clear, plain language
- When uncertain about how to categorize something, ask the user
- To ingest a new source file, use the `/ingest` skill
