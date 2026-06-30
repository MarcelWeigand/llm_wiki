Create or update a Summary.md file for a wiki subfolder. Follow these steps exactly:

1. The argument is the subfolder to summarize (e.g. `wiki/Agentic AI`). If no argument is provided, ask the user which subfolder to summarize.

   Valid subfolders: `wiki/Agentic AI`, `wiki/Machine_Learning`, `wiki/Solution Architect`, `wiki/RAG`, `wiki/Robotics`.

2. List all `.md` files in the target subfolder. Exclude `Summary.md` itself from the list.

3. Read every file in the list. For each file, extract 5–10 bullet points that capture the key ideas — use the actual content of the page, not the page title or summary field. Bullet points should be concrete and informative, not vague ("covers X" is bad; "traces are the source of truth, replacing stack traces" is good).

4. Build the Summary.md content using this exact format:

```
# Summary — <Subfolder Name>

Topics covered in `<subfolder path>/` and their key points.

| Topic | Key Points |
| ----- | ---------- |
| <Page title or concept name> | - point 1<br>- point 2<br>- point 3<br>... |
| <Next topic> | - point 1<br>- point 2<br>... |
```

   Rules for the table:
   - Use the page's `# Title` heading as the topic name (strip "Agentic AI" prefix if redundant, e.g. "Agentic AI Observability" → "Observability")
   - Separate bullet points within a cell with `<br>` (no newlines — Markdown tables require single-line cells)
   - Order rows from foundational/definitional topics to advanced/operational topics
   - If Summary.md already exists, replace it entirely with the updated version — do not append

5. Write the file to `<subfolder>/Summary.md`.

6. Append an entry to `wiki/log.md` with today's date and the subfolder name.

Rules:
- Never modify anything in the `raw/` folder
- Never modify any page other than Summary.md and wiki/log.md
- Do not create individual summaries for pages that are stubs (fewer than 5 substantive lines of content)
