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
wiki/RAG                -- markdown pages maintained by Claude for the topic RAG
wiki/Robotics           -- markdown pages maintained by Claude for the topic Robotics
wiki/index.md           -- table of contents for the entire wiki
wiki/log.md             -- append-only record of all operations
```


##  Page types

Not every entity gets its own page. Use the following rules:

**Concept pages** (one file per concept): Major ideas, techniques, frameworks, and topics.
Examples for wiki/Agentic AI: `definition.md`, `main_ideas.md`, `common_failures.md`, `design_patterns.md`


## Ingest workflow


When the user adds a new source to `raw/youtube` and asks you to ingest it:

1. Read the full document (it is already a summary)
2. Decide one or more topics for the document based on its content. A topic should match one of the given subfolders under wiki/. Ask me first if it's the correct subfolder that you chose. 
3. Decide which existing page inside the chosen subfolders from step 2 best fits the topic and content of the source document. If there is no existing page yet, create a new one. Always try to update existing pages first before creating new pages. 
3. Discuss key takeaways with the user before writing anything
5. Add wiki-links ([[page-name]]) to connect related pages
6. Update `wiki/index.md` with new pages and one-line descriptions
7. Append an entry to `wiki/log.md` with the date, source name, and what changed


A single source may touch 10-15 wiki pages. That is normal.


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


## Citation rules


- Every factual claim should reference its source file
- Use the format (source: filename.pdf) after the claim
- If two sources disagree, note the contradiction explicitly
- If a claim has no source, mark it as needing verification


## Question answering


When the user asks a question:


1. Read `wiki/index.md` first to find relevant pages
2. Read those pages and synthesize an answer
3. Cite specific wiki pages in your response
4. If the answer is not in the wiki, say so clearly
5. If the answer is valuable, offer to save it as a new wiki page


Good answers should be filed back into the wiki so they compound over time.


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
