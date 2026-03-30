---
name: plan-deployment
description: "CRISP-DM 6.1 — Plan Deployment. Designs the deployment architecture, serving infrastructure, rollout strategy, and operational handover plan for moving approved models into production. Produces a structured deployment plan in docs/crisp-dm/6-deployment/."
argument-hint: "<optional: deployment target, infrastructure constraints, or specific deployment question>"
---

# /plan-deployment — CRISP-DM 6.1: Plan Deployment

> **Phase:** 6. Deployment | **Task:** 6.1 Plan Deployment
>
> *"This task takes the evaluation results and determines a strategy for deployment. If a general procedure has been identified to create the relevant model(s), this procedure is documented here for later deployment."*

## Purpose

This skill produces a comprehensive deployment plan covering: serving architecture, inference pipeline design, rollout strategy (canary/blue-green/shadow), operational handover, rollback procedures, and infrastructure requirements. The plan bridges the gap between a validated model and a production system that delivers business value.

## Output Location

- Plan: `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
- If it exists, present its contents and ask: *"A deployment plan already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
  - If it exists, use it — it contains the recommended model, its performance, and known limitations.
  - If it does not exist, warn: *"No model assessment found (task 4.4). Deployment planning requires a recommended model."*
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — business context and success criteria shape deployment requirements.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — constraints, resources, and risks inform infrastructure choices.
- Read `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
  - If it exists, use it — timeline and governance requirements affect rollout strategy.
- Read `.claude/rules/model-governance.md`
  - Use it — deployment gates, model registry, and rollback requirements are mandatory.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Recommended model** (from 4.4) — technique, configuration, MLflow run ID, performance metrics
- **Known limitations** (from 4.4) — where the model fails, underperforming segments
- **Business requirements** (from 1.1) — prediction frequency, latency requirements, who consumes predictions
- **Infrastructure constraints** (from 1.2) — available compute, existing platforms, budget, team skills
- **Timeline** (from 1.4) — deployment deadline, phased rollout milestones
- **Governance requirements** (from model-governance.md) — model card, registry, monitoring mandate

Present what was extracted and what is missing. Ask the user to fill gaps.

### Step 3: Define Serving Architecture

Discuss and document:
- **Serving pattern** — batch (scheduled predictions), real-time (API), streaming, or hybrid
- **Inference pipeline** — data ingestion → preprocessing → prediction → post-processing → delivery
- **Compute infrastructure** — where the model runs (on-prem, cloud, edge)
- **Data flow** — how input data reaches the model and predictions reach consumers
- **Scaling strategy** — how the system handles load spikes (e.g., promotional periods)
- **Dependency management** — model dependencies, package versions, containerization

### Step 4: Define Rollout Strategy

Discuss and document:
- **Rollout approach** — canary, blue-green, shadow mode, phased store rollout, or big-bang
- **Rollout phases** — which stores/sections first, expansion criteria, timeline
- **Validation gates** — what metrics must pass before expanding to the next phase
- **Rollback triggers** — specific thresholds that trigger automatic or manual rollback
- **Rollback procedure** — exact steps to revert to the previous system (including data pipeline)
- **Communication plan** — who is notified at each phase, escalation path

### Step 5: Define Operational Handover

Discuss and document:
- **Ownership** — who owns the model in production (team, roles, on-call rotation)
- **Runbook** — operational procedures for common scenarios (model refresh, data pipeline failure, drift alert)
- **Access control** — who can retrain, redeploy, or roll back the model
- **SLA** — service level agreement for prediction delivery (latency, freshness, availability)
- **Support model** — how end users report issues, escalation path
- **Documentation** — where operational docs live, how they stay current

### Step 6: Define Infrastructure Requirements

Summarize:
- **Compute** — CPU/GPU, memory, storage for model serving
- **Data storage** — where predictions are stored, retention policy
- **Networking** — connectivity between data sources, model server, and consumers
- **CI/CD** — how model updates are tested and deployed (pipeline definition)
- **Secrets management** — how credentials for data sources and APIs are handled
- **Cost estimate** — monthly/annual infrastructure cost

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/6-deployment
```

Write the file `docs/crisp-dm/6-deployment/6.1-plan-deployment.md` using this template:

```markdown
# 6.1 Deployment Plan

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 6. Deployment
> **Status:** Draft | Review | Approved

---

## Deployment Overview

- **Model to Deploy:** [technique + configuration]
- **MLflow Run ID:** [run ID]
- **Model Registry Version:** [version]
- **Primary Metric:** [metric] = [value]
- **Target Go-Live Date:** [date]
- **Deployment Owner:** [team/person]

---

## Serving Architecture

### Serving Pattern
[Batch / Real-time / Streaming / Hybrid — with rationale]

### Inference Pipeline

```
[Data Source] → [Ingestion] → [Preprocessing] → [Model] → [Post-processing] → [Output]
```

| Stage | Component | Technology | Description |
|-------|-----------|------------|-------------|
| Ingestion | [component] | [tech] | [what it does] |
| Preprocessing | [component] | [tech] | [what it does] |
| Prediction | [component] | [tech] | [what it does] |
| Post-processing | [component] | [tech] | [what it does] |
| Delivery | [component] | [tech] | [what it does] |

### Compute Infrastructure
| Resource | Specification | Purpose |
|----------|--------------|---------|
| [resource] | [spec] | [purpose] |

### Data Flow
[Description of how data flows from source to prediction consumer, including any intermediate storage]

### Scaling Strategy
[How the system handles load — e.g., horizontal scaling, queue-based processing, scheduled batch windows]

### Dependency Management
| Dependency | Version | Pinned | Notes |
|------------|---------|--------|-------|
| [package] | [version] | [Yes/No] | [notes] |

---

## Rollout Strategy

### Approach
[Canary / Blue-green / Shadow / Phased / Big-bang — with rationale]

### Rollout Phases

| Phase | Scope | Duration | Entry Criteria | Exit Criteria |
|-------|-------|----------|---------------|---------------|
| 1 - Shadow | [N stores] | [duration] | [criteria] | [criteria] |
| 2 - Pilot | [N stores] | [duration] | [criteria] | [criteria] |
| 3 - Expansion | [N stores] | [duration] | [criteria] | [criteria] |
| 4 - Full rollout | All stores | Ongoing | [criteria] | — |

### Validation Gates
| Gate | Metric | Threshold | Measured Over |
|------|--------|-----------|--------------|
| [gate] | [metric] | [threshold] | [time window] |

### Rollback Triggers
| Trigger | Condition | Action | Owner |
|---------|-----------|--------|-------|
| [trigger] | [specific threshold] | [automatic/manual rollback] | [who] |

### Rollback Procedure
1. [Step 1 — e.g., switch traffic to previous model version]
2. [Step 2 — e.g., revert data pipeline to previous configuration]
3. [Step 3 — e.g., notify stakeholders]
4. [Step 4 — e.g., investigate root cause]

### Communication Plan
| Event | Audience | Channel | Owner |
|-------|----------|---------|-------|
| [event] | [who] | [how] | [who sends] |

---

## Operational Handover

### Ownership
| Role | Team/Person | Responsibility |
|------|------------|---------------|
| Model Owner | [team] | [what they own] |
| Data Pipeline Owner | [team] | [what they own] |
| Infrastructure Owner | [team] | [what they own] |
| On-call | [rotation] | [escalation path] |

### Runbook Summary
| Scenario | Procedure | Escalation |
|----------|-----------|-----------|
| Scheduled model refresh | [steps] | [who to contact] |
| Data pipeline failure | [steps] | [who to contact] |
| Prediction quality degradation | [steps] | [who to contact] |
| Infrastructure outage | [steps] | [who to contact] |

### SLA
| Metric | Target | Measurement |
|--------|--------|------------|
| Prediction freshness | [e.g., daily by 06:00] | [how measured] |
| Availability | [e.g., 99.5%] | [how measured] |
| Latency (if real-time) | [e.g., < 200ms p95] | [how measured] |

### Access Control
| Action | Required Role | Approval |
|--------|--------------|----------|
| View predictions | [role] | None |
| Retrain model | [role] | [approval process] |
| Deploy new version | [role] | [approval process] |
| Rollback | [role] | [approval process] |

---

## Infrastructure Requirements

### Cost Estimate
| Resource | Monthly Cost | Annual Cost | Notes |
|----------|-------------|-------------|-------|
| [resource] | [cost] | [cost] | [notes] |
| **Total** | **[total]** | **[total]** | |

### CI/CD Pipeline
[Description of how model updates flow from development to production — testing, staging, approval gates]

### Secrets Management
[How credentials for data sources, APIs, and infrastructure are stored and rotated]

---

## To Be Clarified

[List any items that need further investigation or stakeholder input. Remove this section if everything is complete.]

---

## Source Documents

- 4.4 Model Assessment: `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- 1.4 Project Plan: `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
- Model Governance: `.claude/rules/model-governance.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| MLOps Engineer | | | Pending |
| Infrastructure Lead | | | Pending |
| Business Stakeholder | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary:

> **Deployment Plan created** at `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
>
> **Summary:**
> - Serving pattern: [batch/real-time/hybrid]
> - Rollout strategy: [approach] across [N] phases
> - Target go-live: [date]
> - Rollback procedure: defined with [N] triggers
> - Infrastructure cost: [estimate]
> - Operational ownership: [team]
>
> **Next step in CRISP-DM:** Proceed to **6.2 Plan Monitoring and Maintenance** — define how model performance, data drift, and prediction quality will be monitored in production, and establish retraining triggers.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 6.1 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Serving architecture matches business requirements (latency, frequency, consumers)
- [ ] Inference pipeline covers all stages from data ingestion to prediction delivery
- [ ] Rollout strategy includes validation gates between phases
- [ ] Rollback triggers are specific and measurable (not vague)
- [ ] Rollback procedure is step-by-step and can be executed under pressure
- [ ] Operational ownership is clearly assigned (no orphaned responsibilities)
- [ ] Runbook covers the most likely failure scenarios
- [ ] SLA targets are realistic and measurable
- [ ] Access control follows principle of least privilege
- [ ] Infrastructure cost estimate exists (even if rough)
- [ ] CI/CD pipeline for model updates is described
- [ ] Secrets management follows security rules (no hardcoded credentials)
- [ ] Model governance requirements are satisfied (model card, registry, monitoring mandate)
- [ ] No PII or sensitive data in the deployment plan
- [ ] All prerequisite documents are cross-referenced
