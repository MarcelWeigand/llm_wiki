# Agentic AI

**Summary**: Introducing failure modes distinct from base model hallucinations.

**Sources**: `2026-05-15_Why Agentic AI Fails_ Infinite Loops, Planning Errors, and More.txt`, `2026-05-15_Why AI Agents Need an Operating System.txt`

**Last updated**: 2026-05-15

---
## Failure mode 1: Infinite loops

**What it is**: The agent repeats similar or identical actions without making meaningful progress toward its goal.

**Example**: An agent tasked with finding a non-existent document keeps searching, evaluating the empty results, reformulating its query slightly, and searching again indefinitely.

**Root causes**:
- No **termination conditions** — the agent doesn't know when to give up
- No **action tracking** — the system doesn't detect that re-attempts aren't changing strategy
- No **progress tracking** — the system doesn't know if results are improving

**Mitigations**:
- Set a **maximum number of steps** or retries
- Track actions to force strategy changes when attempts are too similar
- Monitor progress metrics across iterations

**Impact**: Wastes compute resources and inflates API costs. (source: `2026-05-15_Why Agentic AI Fails_...`)

## Failure mode 2: Hallucinated planning

**What it is**: The agent produces a plan that looks plausible but is impossible to execute — it assumes capabilities or tools it doesn't actually have.

**Example**: Asked to book a flight under $500, the agent plans to call a travel API, filter by price, book the ticket, and send a confirmation email — but it has no travel API configured and no access to the user's email.

**Root causes**:
- **Tool capabilities are not clearly defined** — the agent doesn't know what its tools can and cannot do
- No **plan validation** before execution begins
- No **constraint checks** — the agent fills gaps with assumptions

**Mitigations**:
- Write tool schemas that explicitly describe both capabilities *and* limitations
- Use a **verifier agent** (multi-agent architecture) to review plans before execution
- Use **human-in-the-loop** review for high-risk plans
- Instruct the agent to ask for clarification rather than assume

**Impact**: Execution errors, wasted steps, incorrect outputs. (source: `2026-05-15_Why Agentic AI Fails_...`)

## Failure mode 3: Unsafe tool use

**What it is**: The agent executes an action that is technically permitted but is risky, destructive, or unintended.

**Examples**:
- An agent meant to delete *outdated* records deletes *active* records instead
- An agent sends autonomous emails with unreviewed content

**Root causes**:
- **Over-privileged tools** — tools have more access than necessary for their task
- No **approval workflow** for high-risk actions
- No distinction between read and write access

**Mitigations**:
- Apply the **principle of least agency**: grant only the minimum permissions required
- Implement **approval workflows** — require human confirmation before destructive actions
- **Tier tools by access level** (read-only / read-write / delete) and restrict accordingly

**Impact**: Can damage data integrity, company reputation, and operational stability. (source: `2026-05-15_Why Agentic AI Fails_...`)

## Key insight

Agentic AI failures are not random and are not caused by base model quality issues. They are **predictable, structural failures** caused by insufficient engineering discipline in system design. Applying the same rigour used in traditional software engineering — termination conditions, validation, least privilege — is the primary mitigation. (source: `2026-05-15_Why Agentic AI Fails_...`)

## Related pages

- [[agent-os]]
- [[agentic-ai-definition]]

