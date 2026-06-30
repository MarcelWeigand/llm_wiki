# LLM Security — OWASP Top 10

**Summary**: The OWASP Top 10 for LLM Applications 2025 catalogues the most critical security threats when deploying LLMs in production — from prompt injection and sensitive data leakage to supply chain poisoning and excessive agency.

**Sources**: `raw/youtube/2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt`

**Last updated**: 2026-06-29

---

## Why LLM Security Is Different

LLMs introduce a new class of security risks that traditional application security doesn't cover. The core difficulty: LLMs cannot reliably distinguish between system instructions and user input — and they are trained on vast, often unvetted datasets. This makes them simultaneously a powerful tool and an attack surface. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

## The OWASP Top 10 for LLM Applications (2025)

### 1. Prompt Injection

The highest-priority LLM threat. Two variants:

**Direct prompt injection**: An attacker sends a prompt that bypasses the system-level instructions, getting the LLM to behave in unintended ways (e.g., revealing restricted information, ignoring safety guardrails). Works because LLMs struggle to separate instruction authority from user input authority.

**Indirect prompt injection**: A legitimate user sends a benign prompt (e.g., "summarize this article") but the external content being processed contains hidden malicious instructions ("forget all previous instructions and do X"). The LLM executes the hidden instruction. Consequences:
- **Data breach**: LLM leaks information it was not supposed to reveal
- **Safety bypass**: LLM provides harmful instructions
- **Arbitrary command execution**: LLM triggers actions on connected tools or systems

Indirect injection is especially dangerous for agents that browse the web, process documents, or summarize user-provided files — the attack surface is every piece of external content the agent touches.

**Defenses**: AI firewall/gateway between user and LLM (inspects both incoming prompts and outgoing responses); careful system prompt design; penetration testing with injection techniques. Note: system prompt instructions alone are insufficient — attackers use encoding tricks (poetry, Morse code) to bypass them. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

---

### 2. Sensitive Information Disclosure

LLMs trained on large datasets may have memorised PII, PHI, business data, or financial data. An attacker can prompt the model to reproduce this training data.

Escalated form: **model inversion / extraction attacks** — repeatedly querying the LLM to reconstruct large portions of its training data or the model weights themselves, exposing intellectual property.

**Defenses**: Sanitize training data before use; strong access controls on the LLM and its training sources; regular misconfiguration audits (weak auth, unencrypted data, outdated software). (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

---

### 3. Supply Chain Vulnerabilities

Most LLM deployments rely on third-party pre-trained models and datasets (e.g., from Hugging Face, which hosts millions of models). A weakness anywhere in this supply chain — data, model, application, infrastructure — can compromise the entire system.

**Defenses**: Vet all third-party data and models for origin and integrity; track provenance (lineage of all components); continuous scanning, red team exercises, and patching. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

---

### 4. Data and Model Poisoning

Malicious or inaccurate data introduced into the training dataset subtly alters model behavior. Effects:
- **Wrong answers**: model confidently outputs incorrect information
- **Bias**: model develops and propagates harmful biases
- **Embedded malware**: malicious instructions encoded in model parameters

RAG systems are also at risk: a poisoned external knowledge base used for retrieval can produce bad outputs even from a clean base model. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

**Defenses**: Source verification for all training data; access controls on who can modify training data or model parameters; change control processes; secure RAG knowledge bases.

---

### 5. Improper Output Handling

LLM outputs fed unchecked into downstream systems or user interfaces can carry malicious payloads: XSS, SQL injection, remote code execution. A hallucinating or compromised LLM may generate code that exploits the consuming application.

**Defense**: Treat all LLM outputs as untrusted input — validate and sanitize before passing to any downstream system or rendering in a browser. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

---

### 6. Excessive Agency

An LLM with too many tool permissions or too much access to external systems becomes a high-value attack target. If compromised (e.g., via prompt injection), it can be hijacked to cause widespread real-world damage — including to health, safety, or financial systems.

This is the security framing of the [[agentic-ai-failures|unsafe tool use]] failure mode. The engineering mitigation is identical: apply the **principle of least agency** — restrict the LLM's capabilities to only what is strictly necessary for its intended function. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

See also [[agent-os]] for how the Identity Manager and Tool Manager kernel components enforce this at the infrastructure level.

---

### 7. System Prompt Leakage

The system prompt defines the agent's persona, guardrails, and — if poorly designed — may contain credentials or API keys. If an attacker tricks the LLM into revealing its system prompt, they get a map of the agent's constraints and potentially operational secrets they can exploit for further attacks.

**Defenses**: Never embed secrets or credentials directly in system prompts; use secure configuration management and input validation. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

See also [[context-engineering]] for guidance on what belongs in standing context vs. secure configuration.

---

### 8. Vector and Embedding Weaknesses

LLMs represent words and concepts as numerical vectors (embeddings). If these embeddings are exposed or manipulable, attackers can misinterpret model behavior or use them to reconstruct sensitive training data. This is an emerging attack surface as vector databases (used in [[RAG]]) become more prevalent.

---

### 9. Misinformation

LLMs can hallucinate — generating plausible but factually incorrect information with apparent confidence. This becomes a security risk when users rely on LLM outputs for critical decisions without verification.

**Defenses**: Encourage critical evaluation of LLM outputs; implement fact-checking against trusted sources (e.g., via RAG with verified knowledge bases). (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

---

### 10. Unbounded Consumption

Malicious or poorly designed prompts can cause an LLM to consume excessive resources (compute, memory, API calls), enabling denial-of-service attacks or driving up significant financial costs.

**Defenses**: Rate limiting, quotas, and monitoring on all LLM endpoints. (source: 2026-06-29_OWASP's Top 10 Ways to Attack LLMs_ AI Vulnerabilities Exposed.txt)

---

## Threat Map: OWASP → Engineering Mitigations

| OWASP Threat | Primary mitigation layer |
|---|---|
| Prompt injection | AI gateway / guardrails + pen testing |
| Sensitive info disclosure | Training data sanitization + access controls |
| Supply chain | Provenance tracking + red teaming |
| Data/model poisoning | Source verification + change control |
| Improper output handling | Output validation before downstream use |
| Excessive agency | Principle of least agency (tool permissions) |
| System prompt leakage | No secrets in prompts + config management |
| Vector/embedding weaknesses | Secure vector DB access controls |
| Misinformation | RAG with verified sources + user education |
| Unbounded consumption | Rate limiting + cost monitoring |

## Related Pages

- [[agentic-ai-failures]]
- [[agent-os]]
- [[harness-engineering]]
- [[context-engineering]]
- [[agentic-ai-observability]]
