Ingest a new source file into the wiki. Follow these steps exactly:

1. Check the arguments passed to this skill:
   - If a subfolder was provided (e.g. `/ingest wiki/Agentic AI`), use that as the target subfolder. Skip steps 2–3 and go straight to step 4.
   - If no subfolder was provided, ask the user for the file path (if not given) and proceed from step 2.
   - If a file path was provided but no subfolder, read the file first, then proceed to step 2.

   Valid subfolders are: `wiki/Agentic AI`, `wiki/Machine_Learning`, `wiki/Solution Architect`, `wiki/RAG`, `wiki/Robotics`.

2. Based on the content, decide which wiki subfolder(s) it belongs to. A single source may touch multiple subfolders — that is normal (10–15 pages is not unusual).

3. Tell the user which subfolder(s) you chose and why. Wait for confirmation before proceeding.

4. For each target subfolder, list only the files in that specific subfolder (do NOT glob all of `wiki/`). Read `wiki/index.md` only for the section relevant to that subfolder. Identify which existing page best fits the content. Always prefer updating an existing page over creating a new one. If no existing page fits, propose a new one and confirm with the user.

5. Discuss the 3–5 key takeaways from the source with the user. Do not write anything yet — wait for their input and direction.

6. Once the user has confirmed the direction, write or update the wiki pages:
   - Add content under appropriate headings
   - Add wiki-links ([[page-name]]) to connect related pages
   - Follow the page format from the root CLAUDE.md (Summary, Sources, Last updated, content, Related pages)
   - For pages in `wiki/Machine_Learning` or `wiki/Solution Architect`, anchor content to the 4 AI dimensions where relevant (Capability / Application domain / Learning paradigm / Model architecture)
   - Cite the source file after factual claims: (source: filename.txt)
   - If two sources disagree, note the contradiction explicitly

7. Update `wiki/index.md` with any new pages and one-line descriptions.

8. Append an entry to `wiki/log.md` with today's date, the source filename, and a summary of what changed.

Rule: never modify anything in the `raw/` folder.
