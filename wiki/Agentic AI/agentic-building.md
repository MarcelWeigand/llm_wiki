
# Building and Deploying AI Agents

**Summary**: Four paths for deploying AI agents — managed platform, foundation model infrastructure, custom infrastructure, and no-code — with trade-offs between speed, governance, and control.

**Last updated**: 2026-06-27

---

There are different ways how to deploy AI agents

![[Pasted image 20260626181340.png]]

Path 1: (mult-model, multi-framework hosting platform)
- pro: all agent components (monitoring etc) in one platform, governance, auto-trail, security of hyperscaler, for production scaler
- con: slow for prototype
--> governance and control, gives up speed

Path 2: use foundation models infrastructure
- pro: optimize for development speed
- con: model-specific, no governance, no enterprise integration, vendor-lockin
--> speed and control for dev, give up governance

Path 3: 
- pro: you chose the infra to run your agents on --> infra flexibility, full control 
- con: more engineering to do, 
--> speed and control, gives up governance

Path 4: (no infra, no code)
- pro: no code, drag and drop, agent is one node in automation --> accessability
- con: no governance etc. 
--> speed for non-developers, give up gov and control


![[Pasted image 20260630221305.png]]
