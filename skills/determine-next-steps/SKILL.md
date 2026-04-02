---
name: determine-next-steps
description: "CRISP-DM 5.3 — Determine Next Steps. Synthesizes the results evaluation (5.1) and process review (5.2) into a formal decision on the project's path forward: deploy, iterate, or terminate. Produces an actionable decision document with deployment prerequisites, iteration plan, or project closure rationale in docs/crisp-dm/5-evaluation/."
argument-hint: "<optional: specific decision context or stakeholder directive to incorporate>"
---

# /determine-next-steps — CRISP-DM 5.3: Determine Next Steps

> **Phase:** 5. Evaluation | **Task:** 5.3 Determine Next Steps
>
> *"Depending on the results of the assessment of the data mining results, the project team decides how to proceed. The team decides whether to finish this project and move on to deployment, initiate further iterations, or set up new data mining projects."*

## Purpose

This skill produces the go/no-go decision for the project. It synthesizes findings from 5.1 (results evaluation) and 5.2 (process review) into one of three paths:

1. **Deploy** — proceed to Phase 6 with a deployment plan
2. **Iterate** — return to an earlier phase with a specific improvement plan
3. **Terminate** — close the project with documented rationale and learnings

This is the most consequential decision document in the CRISP-DM cycle.

## Output Location

All artifacts are written to: `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`
- If it exists, present its contents and ask: *"A next steps decision already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
  - If it exists, use it — it contains the results verdict. This is the primary input.
  - If it does not exist, warn: *"No results evaluation found (task 5.1). The next steps decision should be based on a formal evaluation. Run `/evaluate-results` first."*
- Read `docs/crisp-dm/5-evaluation/5.2-review-process.md`
  - If it exists, use it — it contains the process review and recommended actions.
  - If it does not exist, warn: *"No process review found (task 5.2). It's recommended to review the process before deciding next steps. Run `/review-process` first, or proceed based on 5.1 alone."*
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — business objectives are the ultimate benchmark.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — constraints, resources, and timeline inform feasibility.
- Read `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
  - If it exists, use it — compare actual progress against the original plan.
- Read `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
  - If it exists, use it — model recommendation and known limitations.

### Step 2: Extract Decision Inputs

From the ingested documents, extract:
- **Results verdict** (from 5.1) — Ready / Conditionally Ready / Not Ready
- **Success criteria pass rate** (from 5.1)
- **Residual risks** (from 5.1) — especially those rated "Needs Attention"
- **Deployment conditions** (from 5.1) — if conditionally ready
- **Process health** (from 5.2) — Strong / Adequate / Needs Improvement
- **Overlooked factors** (from 5.2) — especially critical ones
- **Recommended actions** (from 5.2) — critical actions before proceeding
- **Resource constraints** (from 1.2) — budget, timeline, team availability
- **Original timeline** (from 1.4) — how actual progress compares to plan

Present the extracted decision inputs and ask the user for any additional context.

### Step 3: Decision Framework

Apply this decision framework:

**Path A: Deploy (Proceed to Phase 6)**
Conditions:
- Results verdict is "Ready" or "Conditionally Ready" (with conditions addressable during deployment)
- No critical overlooked factors from 5.2
- Stakeholder sign-off obtained or obtainable
- Deployment resources and infrastructure are available
- Residual risks are acceptable or mitigatable

**Path B: Iterate (Return to Earlier Phase)**
Conditions:
- Results verdict is "Conditionally Ready" (with conditions requiring model work) or "Not Ready"
- Specific, actionable improvements are identified
- Resources and timeline allow for another iteration
- The expected improvement justifies the iteration cost

**Path C: Terminate (Close the Project)**
Conditions:
- The business problem has changed or is no longer relevant
- The data fundamentally cannot support the business objective
- The cost of further iteration exceeds the expected benefit
- External factors make the project infeasible

### Step 4: Build the Decision Recommendation

Based on the framework, build a structured recommendation:

**For Deploy:**
- List deployment prerequisites (from 5.1 conditions + 5.2 critical actions)
- Define the deployment scope (full rollout vs. phased/pilot)
- Identify Phase 6 tasks to prioritize
- Set the expected deployment timeline

**For Iterate:**
- Identify the target phase to return to (Phase 2, 3, or 4)
- Define specific tasks within that phase
- Set iteration objectives (what must improve, by how much)
- Estimate iteration duration
- Define a maximum number of iterations before re-evaluating

**For Terminate:**
- Document the rationale clearly
- Capture all learnings and reusable artifacts
- Identify any value that can be salvaged (e.g., data pipelines, EDA insights)
- Recommend follow-up actions (different approach, different problem framing)

### Step 5: Present Decision and Ask for Confirmation

Present the recommendation to the user:
- Recommended path: Deploy / Iterate / Terminate
- Key factors driving the recommendation
- What the next concrete actions are
- Timeline estimate

Ask the user:
1. **Do you agree with this recommendation?**
2. **Are there organizational or strategic factors that should change this decision?**
3. **Who needs to approve this decision?**

Wait for the user's response before continuing.

### Step 6: Clarification Round (if needed)

If the user disagrees or has additional context:
- Incorporate their input
- Reassess the recommendation if warranted
- Maximum 2 clarification rounds

### Step 7: Generate the Output Document

Create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/5-evaluation
```

Write the file `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md` using this template:

```markdown
# 5.3 Determine Next Steps

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 5. Evaluation
> **Status:** Draft | Review | Approved

---

## Decision Summary

- **Decision:** [Deploy / Iterate / Terminate]
- **Decision Date:** [date]
- **Results Verdict (5.1):** [Ready / Conditionally Ready / Not Ready]
- **Process Health (5.2):** [Strong / Adequate / Needs Improvement]
- **Confidence Level:** [High / Medium / Low]

---

## Decision Inputs

### From Results Evaluation (5.1)
- **Overall verdict:** [verdict]
- **Success criteria:** [N]/[M] passed
- **Key strengths:** [summary]
- **Key gaps:** [summary]
- **Residual risks:** [N] identified, [N] needing attention
- **Deployment conditions:** [list if conditionally ready]

### From Process Review (5.2)
- **Process health:** [health]
- **Critical overlooked factors:** [list or "None"]
- **Critical recommended actions:** [list or "None"]
- **Lessons learned:** [key lessons affecting this decision]

### Resource & Timeline Context
- **Original timeline (1.4):** [planned vs. actual]
- **Resources available for next phase:** [team, compute, time]
- **Budget remaining:** [if known]
- **Stakeholder urgency:** [how pressing is the business need?]

---

## Decision: [Deploy / Iterate / Terminate]

### Rationale

[2-3 paragraphs explaining why this path was chosen, connecting to the evidence from 5.1 and 5.2. Address both technical and business considerations.]

### Decision Factors

| Factor | Assessment | Weight | Supports |
|--------|-----------|--------|----------|
| Business objective alignment | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |
| Success criteria met | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |
| Residual risk level | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |
| Process maturity | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |
| Resource availability | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |
| Stakeholder readiness | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |
| Time pressure | [assessment] | [High/Medium/Low] | [Deploy/Iterate/Terminate] |

---

## Action Plan

[Include ONLY the section that matches the decision]

### Deployment Plan (if Deploy)

#### Prerequisites Before Deployment
| # | Prerequisite | Source | Owner | Target Date | Status |
|---|-------------|--------|-------|-------------|--------|
| 1 | [prerequisite] | [5.1/5.2 reference] | [who] | [date] | [Pending/Done] |

#### Deployment Scope
- **Scope:** [Full rollout / Phased rollout / Pilot]
- **Pilot stores/sections:** [if phased — which stores or sections first]
- **Pilot duration:** [how long before expanding]
- **Success criteria for expansion:** [what must hold during pilot]

#### Phase 6 Task Priorities
| Priority | Task | Description |
|----------|------|-------------|
| 1 | 6.1 Plan Deployment | [key focus areas] |
| 2 | 6.2 Plan Monitoring | [key focus areas] |
| 3 | 6.3 Produce Final Report | [key focus areas] |
| 4 | 6.4 Review Project | [key focus areas] |

#### Timeline
| Milestone | Target Date | Dependencies |
|-----------|-------------|-------------|
| Prerequisites complete | [date] | [deps] |
| Deployment plan finalized | [date] | [deps] |
| Monitoring in place | [date] | [deps] |
| Pilot launch | [date] | [deps] |
| Full rollout | [date] | [deps] |

### Iteration Plan (if Iterate)

#### Target Phase
- **Return to:** Phase [N] — [phase name]
- **Specific tasks:** [which tasks within the phase]

#### Iteration Objectives
| # | Objective | Current State | Target State | Metric |
|---|-----------|--------------|-------------|--------|
| 1 | [what to improve] | [current performance] | [target performance] | [how to measure] |

#### Iteration Scope
- **What changes:** [specific changes to make]
- **What stays:** [what does not need to change]
- **Estimated duration:** [time]
- **Maximum iterations:** [N] before re-evaluating the approach

#### Iteration Risks
| Risk | Mitigation |
|------|-----------|
| Iteration doesn't improve results | [what to do — e.g., "Try alternative approach X, then consider termination"] |
| Resources exhausted before improvement | [what to do] |

### Termination Plan (if Terminate)

#### Rationale for Termination
[Clear, honest explanation of why the project should not continue]

#### Salvageable Artifacts
| Artifact | Location | Reuse Potential |
|----------|----------|----------------|
| [e.g., data pipeline] | [path] | [how it could be reused] |
| [e.g., EDA findings] | [path] | [how it could be reused] |

#### Lessons for Future Projects
1. [lesson 1]
2. [lesson 2]

#### Recommended Follow-Up
[Alternative approaches, different problem framings, or future project ideas that emerged from this work]

---

## Approval

This decision requires approval from the following stakeholders:

| Role | Name | Decision | Date | Notes |
|------|------|----------|------|-------|
| Business Sponsor | | [Approve/Reject/Defer] | | |
| Lead Data Scientist | | [Approve/Reject/Defer] | | |
| Operations Lead | | [Approve/Reject/Defer] | | |
| [Other stakeholder] | | [Approve/Reject/Defer] | | |

---

## To Be Clarified

[List any decision factors that could not be resolved. Remove this section if everything is complete.]

---

## Source Documents

- 5.1 Evaluate Results: `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
- 5.2 Review Process: `docs/crisp-dm/5-evaluation/5.2-review-process.md`
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- 1.4 Project Plan: `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
- 4.4 Model Assessment: `docs/crisp-dm/4-modeling/4.4-model-assessment.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Business Sponsor | | | Pending |
| Lead Data Scientist | | | Pending |
| Operations Lead | | | Pending |
| Project Manager | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary based on the decision:

**If Deploy:**
> **Next Steps Decision created** at `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`
>
> **Decision: DEPLOY**
> - [N] prerequisites to complete before deployment
> - Deployment scope: [full / phased / pilot]
> - [N] stakeholder approvals needed
>
> **Next step in CRISP-DM:** Move to **Phase 6 (Deployment)**. Run `/plan-deployment` to begin planning the deployment infrastructure, rollout strategy, and monitoring (Task 6.1).

**If Iterate:**
> **Next Steps Decision created** at `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`
>
> **Decision: ITERATE**
> - Return to: Phase [N] — [phase name]
> - [N] iteration objectives defined
> - Maximum [N] iterations before re-evaluating
>
> **Next step in CRISP-DM:** Return to Phase [N]. Run `/[relevant command]` to begin the iteration.

**If Terminate:**
> **Next Steps Decision created** at `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`
>
> **Decision: TERMINATE**
> - [N] salvageable artifacts documented
> - [N] lessons captured for future projects
> - [N] follow-up recommendations made
>
> **Project closed.** Consider running `/produce-final-report` (Task 6.3) to formally document the project outcomes and learnings, even though deployment will not proceed.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 5.3 artifact link and update the Phase 5 status.

## Quality Checks

Before finalizing the document, verify:
- [ ] The decision is clearly stated (Deploy / Iterate / Terminate)
- [ ] The rationale connects to evidence from 5.1 and 5.2
- [ ] All decision factors are assessed and weighted
- [ ] The action plan is specific and actionable (not generic)
- [ ] Prerequisites (if deploying) are complete and owned
- [ ] Iteration objectives (if iterating) are measurable with defined targets
- [ ] Termination rationale (if terminating) is honest and captures learnings
- [ ] Stakeholder approval requirements are identified
- [ ] Timeline estimates are realistic given available resources
- [ ] No PII in the document
- [ ] Source documents are referenced for traceability
