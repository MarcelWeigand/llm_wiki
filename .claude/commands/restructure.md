Restructure a wiki page to improve clarity and coherence. Follow these steps exactly:

1. The argument is the file path of the wiki page to restructure (e.g. `wiki/Agentic AI/agentic-ai-observability.md`). If no argument is provided, ask the user which page to restructure.

2. Read the target page in full.

3. Analyse the current structure for the following issues — check each explicitly:
   - **Redundancy**: sections or paragraphs that repeat the same point (often a sign of multiple ingestions)
   - **Merge candidates**: adjacent or thematically related sections that would read better as one
   - **Ordering**: foundational concepts buried after advanced ones; cause before effect; general before specific
   - **Fragmentation**: one idea split across several short sections that would be clearer as subsections under a single heading
   - **Broken or missing wiki-links**: concepts mentioned that have a page but are not linked
   - **Header granularity**: headings that are too narrow (single-sentence sections) or too broad (walls of text under one heading)
   - **Orphaned examples**: concrete examples that float disconnected — move them next to the concept they illustrate
   - **Summary drift**: the page **Summary** field no longer accurately describes the full content after additions

4. Present your findings as a numbered list of proposed changes with a one-line rationale for each. Then show a proposed new outline (heading tree only, no full content). Do NOT write anything yet — wait for the user to confirm, request changes, or reject specific proposals.

5. Once the user confirms, rewrite the page:
   - Preserve all factual content and source citations — do not add, remove, or alter facts
   - Merge, reorder, and rename sections as agreed
   - Remove duplicate passages (keep the clearest version)
   - Add or repair wiki-links ([[page-name]]) where concepts have a corresponding page
   - Update the **Summary** field if the scope has changed
   - Update **Last updated** to today's date
   - Keep the standard page format: Summary, Sources, Last updated, content, Related Pages

6. Append an entry to `wiki/log.md` with today's date, the page name, and a concise summary of what changed structurally.

Rules:
- Never modify anything in the `raw/` folder
- Never add new facts or content not already present in the page
- Never remove source citations
