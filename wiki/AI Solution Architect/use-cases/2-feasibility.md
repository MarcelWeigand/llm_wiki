# Feasibility Assessment Workshop

**Summary**: Full-day workshop methodology for scoring shortlisted AI use cases on technical feasibility, data readiness, and business viability — and producing a ranked recommendation.

**Last updated**: 2026-06-25

---

**Goal**: Evaluate each shortlisted use case and produce a ranked, actionable recommendation for which to build first.

**Duration**: Full day (6–7 hours) or two half-days
**Participants**: Business unit leads (from ideation) + data owners + IT/data engineers + ideally one domain expert per use case

---

## Preparation (before the workshop)

- Send the shortlisted use cases to participants in advance — ask each to come with answers to: what data exists for this, where it lives, and who owns it
- Prepare a scoring scorecard (see below) — participants should understand the evaluation criteria before the session
- For each use case, do a 15-min pre-read: is this technically possible? Are there known pitfalls or precedents in this industry?

---

## Feasibility scoring scorecard

Score each use case on 5 dimensions, 1–3 scale (1 = low, 2 = medium, 3 = high):

| Dimension | What to assess | Score 1 | Score 2 | Score 3 |
|---|---|---|---|---|
| **Business value** | Revenue uplift, cost reduction, risk reduction, strategic importance | Marginal / unclear | Moderate, quantifiable | Large, clear ROI |
| **Data availability** | Does the right data exist and can it be accessed? | Data doesn't exist or inaccessible | Data exists but needs significant work | Data exists, accessible, reasonably clean |
| **Label / ground truth** | Can the model be trained and evaluated? | No labels, no way to create them | Labels can be created but it's expensive / slow | Labels already exist or easy to generate |
| **Technical complexity** | How hard is the ML problem? | Novel problem, unclear approach | Standard problem but complex integration | Well-understood problem with proven solutions |
| **Organizational readiness** | Will the output be adopted and acted on? | No clear owner, process change required | Owner exists but change management needed | Clear owner, output fits into existing workflow |

**Total score**: sum of 5 dimensions (max 15). Use as a relative ranking, not an absolute threshold.

---

## Workshop structure

### 1. Use case deep-dives (30 min each)

For each shortlisted use case, run a structured discussion:

- **Problem restatement**: confirm the problem definition from ideation — does everyone agree?
- **Data inventory**: what data exists? Where? In what format? Who owns it? Updated how frequently?
- **Label question**: how would you know if the model was right or wrong? Can you get historical examples of the outcome?
- **Integration question**: if the model works, what does someone do with its output? Which system / person receives it?
- **Score it live**: fill in the scorecard together with the room — surface disagreements explicitly

### 2. Cross-use-case ranking (45 min)

- Plot all use cases on a 2×2: business value (y-axis) vs. feasibility (x-axis)
- Discuss the top-right quadrant first (high value, high feasibility) — these are your quick wins
- Flag high-value / low-feasibility cases as strategic bets worth a data-readiness pre-project
- Low-value cases drop off regardless of feasibility

### 3. Recommendation build (30 min)

- Select 1–2 use cases to pilot immediately (top-right quadrant)
- Select 1–2 strategic bets for a data readiness track (high value, data gaps identified)
- Agree on what "done" looks like for the pilot: success metric, timeline, who owns it
- This recommendation comes out of the room — not from the SA alone

### 4. Next steps (15 min)

- Assign owners to each recommended use case
- Agree on data access steps needed before the pilot can start
- Schedule a follow-up to present the recommendation to leadership

---

## Output

A ranked use case recommendation with:

- **Pilot candidates** (1–2): ready to start, data access confirmed, owner named
- **Strategic bets** (1–2): high value but need a data readiness workstream first
- **Parking lot**: ideas dropped with a short reason — preserves goodwill and documents the decision

---

## Key SA principles for both workshops

**Stay problem-first, solution-second**: The moment you lead with "we could build an LLM that..." you anchor the group on technology. Let the business problem drive the conversation — the AI approach follows from the [[technical-framework]].

**Make the data question concrete early**: Most ideation workshops produce ideas that die in feasibility because nobody asked "does the data exist?" until it was too late. Ask it in ideation as a gut-check, confirm it in feasibility with the data owners in the room.

**Score together, don't score alone**: The scorecard filled in by the SA alone produces a recommendation the client doesn't own. Filled in together with the room, it produces a decision the client made — much easier to execute.

**Name the pilot success metric before you leave the room**: A use case without a defined success metric will be evaluated subjectively and usually fails politically even if it works technically. "Reduce unplanned downtime by 15% within 6 months" is a success metric. "Improve maintenance" is not.

**Separate technical feasibility from organizational readiness**: A technically perfect model that nobody acts on is a failed project. Organizational readiness (is there an owner? does the output fit into a workflow?) is as important as data availability.

---

## Related pages

- [[0-overview]] — Full lifecycle map
- [[1-ideation]] — Previous step: generating the shortlist
- [[3-scoping]] — Next step: turning the selected use case into a defined project
- [[technical-framework]] — Reference for assessing technical complexity during deep-dives
