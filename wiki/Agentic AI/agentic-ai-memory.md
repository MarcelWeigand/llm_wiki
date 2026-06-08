
## Memory types that AI agents need

1. Working memory (RAM) = context window
	1. size limit (biggest is one million)

2. Semantic memory 
	1. .md files or vector databases --> gets loaded into session
	2. general knowledge 
	3. knowledge is always present in context

3. Procedural memory = agent skills
	1. skill.md file 
	2. skills use progressive disclosure --> agent doesn't load all of its skills into the context window --> only the skills that matches the task are loaded

4. Episodic memory 
	1. what it learned on previous runs 
	2. uses distillation = don't save everything from previous run, only the important information


--> not every agent needs necessarily all four
- simple reflex agent 
