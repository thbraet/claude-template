---
name: produce-project-plan
description: "CRISP-DM 1.4 — Produce Project Plan. Synthesizes all prior Business Understanding outputs (1.1–1.3) into a project plan with CRISP-DM stages, durations, resources, dependencies, decision points, and a tool & technique assessment. Produces a structured project plan in docs/crisp-dm/1-business-understanding/."
argument-hint: "<path to meeting notes, Notion page URL, or project context>"
---

# /produce-project-plan — CRISP-DM 1.4: Produce Project Plan

> **Phase:** 1. Business Understanding | **Task:** 1.4 Produce Project Plan
>
> *"Describe the intended plan for achieving the data mining goals and thereby achieving the business goals. The plan should specify the steps to be performed during the rest of the project, including the initial selection of tools and techniques."*

## Purpose

This skill synthesizes all prior Business Understanding outputs (1.1 business objectives, 1.2 situation assessment, 1.3 data mining goals) into a concrete project plan. It extracts as much information as possible from the existing CRISP-DM documents and any additional source documents, then asks the user only about what's missing. It produces two outputs:

1. **Project Plan** — CRISP-DM stages with durations, resources, inputs/outputs, dependencies, decision points, and risk-adjusted milestones
2. **Tool & Technique Assessment** — evaluation of candidate tools, platforms, and modeling techniques against project requirements

## Output Location

All artifacts are written to: `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
- If it exists, present its contents and ask: *"A project plan already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if the prerequisite documents exist:
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it as a primary source — it contains the business objectives, success criteria, constraints, and timeline expectations.
  - If it does not exist, warn the user: *"No business objectives document found (task 1.1). It's strongly recommended to complete 1.1 first — proceed anyway?"*
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — it contains resources, personnel, constraints, risks, costs, and available tools that directly feed the project plan.
  - If it does not exist, warn the user: *"No situation assessment found (task 1.2). Resource and risk information will be limited — proceed anyway?"*
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it contains the technical goals, success criteria, and scope that define what work needs to be done.
  - If it does not exist, warn the user: *"No data mining goals document found (task 1.3). Technical scope will be unclear — proceed anyway?"*

### Step 2: Ingest Source Documents

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** (e.g., `docs/meeting-notes.md`, `notes/planning-session.txt`) — Read the file(s)
- **Notion page URL** — Fetch via the Notion MCP tools (`mcp__notion__API-retrieve-a-page`, `mcp__notion__API-get-block-children`)
- **Pasted text** — Use the text directly from the conversation
- **No input provided** — If the 1.1, 1.2, and/or 1.3 documents exist, those are sufficient to start extraction. If none exist, ask: *"Do you have meeting notes, a planning document, or any other material I can extract from? You can provide a file path, a Notion URL, or paste the text directly. If not, I'll guide you through the questions manually."*

Read ALL provided sources (including the 1.1, 1.2, and 1.3 documents if available) before proceeding.

### Step 3: Extract and Map Information

After reading the source documents, map every piece of information to the required fields below. Use this checklist internally:

**Section A — Project Stages & Timeline:**
- [ ] Stages aligned to CRISP-DM phases (Data Understanding, Data Preparation, Modeling, Evaluation, Deployment)
- [ ] Duration estimates for each stage
- [ ] Start/end dates or relative scheduling
- [ ] Key milestones and checkpoints
- [ ] Decision points / go/no-go gates (e.g., after baseline model, after evaluation)
- [ ] Dependencies between stages

**Section B — Resources Per Stage:**
- [ ] Personnel assigned to each stage (from 1.2 personnel inventory)
- [ ] Hardware / compute resources needed per stage
- [ ] Data requirements per stage (which data sources, access needed when)
- [ ] External dependencies (vendor access, stakeholder reviews, legal approvals)

**Section C — Inputs & Outputs Per Stage:**
- [ ] Required inputs for each stage (documents, data, models, approvals)
- [ ] Expected outputs / deliverables for each stage
- [ ] Acceptance criteria for stage completion

**Section D — Risk-Adjusted Planning:**
- [ ] Risks from 1.2 mapped to affected stages
- [ ] Buffer time for high-risk stages
- [ ] Contingency triggers (when to activate contingency plans from 1.2)
- [ ] Critical path identification

**Section E — Tool & Technique Assessment:**
- [ ] Candidate modeling techniques (from 1.3 problem type)
- [ ] Candidate tools and platforms (from 1.2 available tools + additional options)
- [ ] Evaluation criteria for tools (cost, skill availability, scalability, integration)
- [ ] Evaluation criteria for techniques (interpretability, performance, data requirements, training time)
- [ ] Recommended tools and techniques with rationale
- [ ] Gaps requiring procurement, training, or proof-of-concept

**Section F — Communication & Governance:**
- [ ] Reporting cadence (weekly, bi-weekly, per-milestone)
- [ ] Stakeholder review points
- [ ] Documentation requirements per stage
- [ ] Experiment tracking approach (MLflow, etc.)
- [ ] Version control strategy for data and models (DVC, etc.)

### Step 4: Present Extracted Information and Ask About Gaps

Present what was extracted in a structured summary, organized by section. For each field, show one of:
- **Extracted:** the value found in the source document(s), with a quote or reference
- **Inferred from 1.1:** the value carried over from the business objectives document
- **Inferred from 1.2:** the value carried over from the situation assessment
- **Inferred from 1.3:** the value carried over from the data mining goals document
- **Missing:** flag it clearly

Then ask the user to:
1. **Confirm or correct** the extracted information
2. **Fill in the missing fields**

Format the ask like this:

> Here's what I extracted from the existing CRISP-DM documents and your [additional sources]. Please review and fill in the gaps:
>
> **Project Stages & Timeline**
> - Stages: *6 CRISP-DM phases identified* ✓
> - Duration estimates: **MISSING** — How long do you expect each phase to take? Any hard deadlines?
> - Decision points: *Go/no-go after baseline model* ✓ (inferred from 1.3)
> - Dependencies: **MISSING** — Are there external dependencies (e.g., data access approvals, vendor timelines)?
>
> **Resources Per Stage**
> - Personnel: *[names from 1.2]* ✓ (from 1.2)
> - Compute: *[resources from 1.2]* ✓ (from 1.2)
> - Data access timeline: **MISSING** — When will each data source be available?
>
> **Tool & Technique Assessment**
> - Problem type: *Time series forecasting* ✓ (from 1.3)
> - Candidate techniques: **MISSING** — Which modeling approaches are you considering? (e.g., ARIMA, Prophet, XGBoost, LSTM)
> - Available tools: *[tools from 1.2]* ✓ (from 1.2)
> - ...
>
> **[continue for all sections]**
>
> Please confirm the extracted items are correct and provide the missing ones.

**Important rules for this step:**
- Ask about ALL missing fields in a single message — do not split into multiple rounds for gaps
- If a field is ambiguous in the source, present your best interpretation and ask for confirmation
- If duration estimates are missing, suggest reasonable ranges based on project complexity and team size
- If candidate techniques are not specified, propose 2–3 appropriate techniques based on the problem type from 1.3
- If tool choices are unclear, suggest options based on the Colruyt Group tooling stack (MLflow, DVC, GitLab CI/CD)

Wait for the user's response before continuing.

### Step 5: Clarification Round (if needed)

If the user's response still has gaps or ambiguities:
- Ask a focused follow-up covering only the remaining gaps
- Maximum 2 clarification rounds — after that, mark remaining gaps as "TBD" in the document and note them in a "To be clarified" section

### Step 6: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/1-business-understanding
```

Write the file `docs/crisp-dm/1-business-understanding/1.4-project-plan.md` using this template:

```markdown
# 1.4 Project Plan

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 1. Business Understanding
> **Status:** Draft | Review | Approved

---

## Project Overview

- **Business Objective:** [one-line summary from 1.1]
- **Data Mining Goal:** [one-line summary from 1.3]
- **Estimated Duration:** [total project duration]
- **Team Size:** [number of people]
- **Key Constraint:** [most critical constraint from 1.2]

---

## Project Stages

### Stage Overview

| # | Stage | CRISP-DM Phase | Duration | Start | End | Owner | Decision Point |
|---|-------|---------------|----------|-------|-----|-------|----------------|
| 1 | Business Understanding | Phase 1 | [duration] | [start] | [end] | [owner] | [gate/review] |
| 2 | Data Understanding | Phase 2 | [duration] | [start] | [end] | [owner] | [gate/review] |
| 3 | Data Preparation | Phase 3 | [duration] | [start] | [end] | [owner] | [gate/review] |
| 4 | Modeling | Phase 4 | [duration] | [start] | [end] | [owner] | [gate/review] |
| 5 | Evaluation | Phase 5 | [duration] | [start] | [end] | [owner] | [gate/review] |
| 6 | Deployment | Phase 6 | [duration] | [start] | [end] | [owner] | [gate/review] |

### Stage Details

#### Stage 1: Business Understanding
- **Duration:** [duration]
- **Personnel:** [who is involved]
- **Inputs:** [what is needed to start]
- **Activities:**
  - [activity 1]
  - [activity 2]
- **Outputs / Deliverables:**
  - [deliverable 1]
  - [deliverable 2]
- **Completion Criteria:** [what defines "done"]
- **Decision Point:** [go/no-go criteria, if applicable]

#### Stage 2: Data Understanding
- **Duration:** [duration]
- **Personnel:** [who is involved]
- **Inputs:** [what is needed — documents, data access, etc.]
- **Activities:**
  - [activity 1]
  - [activity 2]
- **Outputs / Deliverables:**
  - [deliverable 1]
  - [deliverable 2]
- **Completion Criteria:** [what defines "done"]
- **Decision Point:** [go/no-go criteria, if applicable]

#### Stage 3: Data Preparation
- **Duration:** [duration]
- **Personnel:** [who is involved]
- **Inputs:** [what is needed]
- **Activities:**
  - [activity 1]
  - [activity 2]
- **Outputs / Deliverables:**
  - [deliverable 1]
  - [deliverable 2]
- **Completion Criteria:** [what defines "done"]
- **Decision Point:** [go/no-go criteria, if applicable]

#### Stage 4: Modeling
- **Duration:** [duration]
- **Personnel:** [who is involved]
- **Inputs:** [what is needed]
- **Activities:**
  - [activity 1]
  - [activity 2]
- **Outputs / Deliverables:**
  - [deliverable 1]
  - [deliverable 2]
- **Completion Criteria:** [what defines "done"]
- **Decision Point:** [go/no-go after baseline; go/no-go after champion model]

#### Stage 5: Evaluation
- **Duration:** [duration]
- **Personnel:** [who is involved]
- **Inputs:** [what is needed]
- **Activities:**
  - [activity 1]
  - [activity 2]
- **Outputs / Deliverables:**
  - [deliverable 1]
  - [deliverable 2]
- **Completion Criteria:** [what defines "done"]
- **Decision Point:** [deploy / iterate / abandon]

#### Stage 6: Deployment
- **Duration:** [duration]
- **Personnel:** [who is involved]
- **Inputs:** [what is needed]
- **Activities:**
  - [activity 1]
  - [activity 2]
- **Outputs / Deliverables:**
  - [deliverable 1]
  - [deliverable 2]
- **Completion Criteria:** [what defines "done"]
- **Decision Point:** [production sign-off]

---

## Dependencies

| # | Dependency | From Stage | To Stage | Type | Status | Mitigation if Delayed |
|---|-----------|------------|----------|------|--------|-----------------------|
| 1 | [dependency] | [stage] | [stage] | [Blocking / Non-blocking] | [Open / Resolved] | [what to do if late] |

---

## Risk-Adjusted Timeline

### Critical Path
[Describe the longest dependency chain that determines the minimum project duration.]

### Risk Buffers
| Stage | Base Duration | Buffer | Risk-Adjusted Duration | Rationale |
|-------|-------------|--------|----------------------|-----------|
| [stage] | [base] | [buffer] | [adjusted] | [which risk from 1.2 justifies the buffer] |

### Contingency Triggers
| Risk (from 1.2) | Affected Stage | Trigger Condition | Contingency Action | Impact on Timeline |
|-----------------|---------------|-------------------|-------------------|-------------------|
| [risk] | [stage] | [when to act] | [what to do] | [days added] |

---

## Tool & Technique Assessment

### Candidate Modeling Techniques

| # | Technique | Problem Fit | Interpretability | Data Requirements | Training Time | Pros | Cons |
|---|-----------|------------|-----------------|-------------------|---------------|------|------|
| 1 | [technique] | [how well it fits] | [high/medium/low] | [what it needs] | [estimate] | [advantages] | [disadvantages] |

### Recommended Techniques
- **Baseline:** [simple technique for establishing a floor — e.g., naive forecast, linear regression]
- **Primary:** [main technique(s) to explore]
- **Stretch:** [advanced technique if time/data permit]
- **Rationale:** [why these were chosen]

### Candidate Tools & Platforms

| # | Tool | Purpose | Availability | Cost | Skill Gap | Verdict |
|---|------|---------|-------------|------|-----------|---------|
| 1 | [tool] | [what it's used for] | [available / needs procurement] | [cost] | [team familiarity] | [Use / Evaluate / Skip] |

### Recommended Tool Stack
| Purpose | Tool | Notes |
|---------|------|-------|
| Experiment Tracking | [e.g., MLflow] | [notes] |
| Data Versioning | [e.g., DVC] | [notes] |
| Feature Engineering | [e.g., pandas, Spark] | [notes] |
| Modeling | [e.g., scikit-learn, XGBoost] | [notes] |
| Serving / Deployment | [e.g., FastAPI, Airflow] | [notes] |
| Monitoring | [e.g., Evidently, Grafana] | [notes] |
| CI/CD | [e.g., GitLab CI/CD] | [notes] |

---

## Communication & Governance

### Reporting Cadence
| Event | Frequency | Audience | Format |
|-------|-----------|----------|--------|
| [event] | [frequency] | [who] | [how — standup, report, dashboard] |

### Stakeholder Review Points
| Milestone | Expected Date | Reviewers | Decision Required |
|-----------|--------------|-----------|-------------------|
| [milestone] | [date] | [who reviews] | [what they decide] |

### Documentation Requirements
| Stage | Required Documentation |
|-------|----------------------|
| Data Understanding | Data dictionary, EDA report, data quality report |
| Data Preparation | Feature documentation, pipeline documentation |
| Modeling | Experiment logs (MLflow), model card |
| Evaluation | Evaluation report, fairness audit |
| Deployment | Runbook, monitoring plan, rollback procedure |

### Version Control Strategy
- **Code:** [e.g., Git via GitLab, branch strategy]
- **Data:** [e.g., DVC, Git LFS]
- **Models:** [e.g., MLflow Model Registry]
- **Experiments:** [e.g., MLflow Tracking]

---

## To Be Clarified

[List any items that could not be determined from the source documents or user input. Remove this section if everything is complete.]

---

## Source Documents

- [List the meeting notes, Notion pages, or other sources used to produce this document]
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Sponsor | | | Pending |
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
| Technical Lead | | | Pending |
```

### Step 7: Summary and Next Steps

After writing the document, present a summary:

> **Project Plan created** at `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
>
> **Summary:**
> - [N] stages planned across CRISP-DM phases
> - Estimated total duration: [duration]
> - [N] decision points / go-no-go gates defined
> - [N] dependencies identified
> - [N] risks mapped to stages with buffers
> - Tool stack: [brief summary of recommended tools]
> - Modeling approach: baseline ([technique]), primary ([technique])
> - [N] items still to be clarified (if any)
>
> **Phase 1 (Business Understanding) is now complete.** Next step in CRISP-DM: Begin **Phase 2 — Data Understanding** with data collection, initial exploration, and data quality assessment.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md`:
- Add the 1.4 artifact link
- Consider marking Phase 1 "Business Understanding" as "Complete" if all four documents (1.1–1.4) are in place

## Quality Checks

Before finalizing the document, verify:
- [ ] Every CRISP-DM phase (2–6) has a corresponding stage with duration, personnel, inputs, and outputs
- [ ] Every stage has clear completion criteria and deliverables
- [ ] Every decision point specifies what is being decided and by whom
- [ ] Dependencies are realistic and mitigation for delays is noted
- [ ] Risk buffers reference specific risks from the 1.2 situation assessment
- [ ] Baseline modeling technique is identified (not just advanced approaches)
- [ ] Tool recommendations align with Colruyt Group tooling (MLflow, DVC, GitLab CI/CD, Artifactory)
- [ ] Communication cadence matches stakeholder expectations from 1.1 and 1.2
- [ ] Documentation requirements include model card, experiment logs, and monitoring plan (per model governance rules)
- [ ] The critical path is identified and realistic given team size and constraints
- [ ] No PII or sensitive data is included in the document
- [ ] Document cross-references the 1.1, 1.2, and 1.3 documents where applicable
