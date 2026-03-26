---
name: determine-data-mining-goals
description: "CRISP-DM 1.3 — Determine Data Mining Goals. Translates business objectives into technical data mining goals, specifies the problem type, and defines technical success criteria with benchmarks. Produces a structured data mining goals document in docs/crisp-dm/1-business-understanding/."
argument-hint: "<path to meeting notes, Notion page URL, or project context>"
---

# /determine-data-mining-goals — CRISP-DM 1.3: Determine Data Mining Goals

> **Phase:** 1. Business Understanding | **Task:** 1.3 Determine Data Mining Goals
>
> *"A business goal states objectives in business terminology. A data mining goal states project objectives in technical terms. For example, the business goal might be 'Increase catalog sales to existing customers.' A data mining goal might be 'Predict how many widgets a customer will buy, given their purchases over the past three years, demographic information, and the price of the item.'"*

## Purpose

This skill translates the business objectives from task 1.1 into technical data mining goals. It extracts as much information as possible from the existing CRISP-DM documents (1.1 business objectives and 1.2 situation assessment) and any additional source documents, then asks the user only about what's missing. It produces three outputs:

1. **Data Mining Goals** — technical goals mapped to business objectives, with problem type specification
2. **Data Mining Success Criteria** — measurable technical criteria with benchmarks and evaluation methodology
3. **Objective-to-Goal Traceability** — explicit mapping from business objectives to data mining goals

## Output Location

All artifacts are written to: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- If it exists, present its contents and ask: *"A data mining goals document already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if the prerequisite documents exist:
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it as a primary source — it contains the business objectives, success criteria, and problem context that must be translated into data mining goals.
  - If it does not exist, warn the user: *"No business objectives document found (task 1.1). It's strongly recommended to complete 1.1 first — proceed anyway?"*
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it as an additional source — it contains data sources, constraints, terminology, and risks that inform what's technically feasible.
  - If it does not exist, note it but proceed — 1.2 is helpful but not strictly required.

### Step 2: Ingest Source Documents

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** (e.g., `docs/meeting-notes.md`, `notes/technical-review.txt`) — Read the file(s)
- **Notion page URL** — Fetch via the Notion MCP tools (`mcp__notion__API-retrieve-a-page`, `mcp__notion__API-get-block-children`)
- **Pasted text** — Use the text directly from the conversation
- **No input provided** — If the 1.1 and/or 1.2 documents exist, those are sufficient to start extraction. If neither exists, ask: *"Do you have meeting notes, a technical review document, or any other material I can extract from? You can provide a file path, a Notion URL, or paste the text directly. If not, I'll guide you through the questions manually."*

Read ALL provided sources (including the 1.1 and 1.2 documents if available) before proceeding.

### Step 3: Extract and Map Information

After reading the source documents, map every piece of information to the required fields below. Use this checklist internally:

**Section A — Data Mining Problem Specification:**
- [ ] Problem type (regression, classification, clustering, association, anomaly detection, time series forecasting, etc.)
- [ ] Target variable(s) — what exactly is being predicted, classified, or grouped
- [ ] Prediction granularity — at what level (store, product, day, week, customer, etc.)
- [ ] Prediction horizon — how far ahead (if applicable)
- [ ] Input features expected — broad categories of predictors based on available data sources
- [ ] Key assumptions about the modeling approach

**Section B — Data Mining Goals:**
- [ ] For each business objective from 1.1, a corresponding data mining goal stated in technical terms
- [ ] Desired model output format (point forecast, probability, ranking, class label, etc.)
- [ ] Intended use of model output (decision support, automation, monitoring, etc.)
- [ ] Model interpretability requirements (black box acceptable vs. explainable required)

**Section C — Data Mining Success Criteria:**
- [ ] Primary evaluation metric(s) (RMSE, MAE, MAPE, accuracy, precision, recall, F1, AUC, lift, etc.)
- [ ] Threshold for each metric — what value constitutes success
- [ ] Baseline to beat (current approach, naive model, human judgment, etc.)
- [ ] Evaluation methodology (cross-validation, hold-out, time-based split, etc.)
- [ ] Business-to-technical criteria mapping — how technical metrics relate to business success criteria from 1.1

**Section D — Scope & Constraints:**
- [ ] What is explicitly out of scope for the data mining effort
- [ ] Known data limitations that constrain the approach (from 1.2 if available)
- [ ] Latency / performance requirements for model inference
- [ ] Retraining frequency expectations

### Step 4: Present Extracted Information and Ask About Gaps

Present what was extracted in a structured summary, organized by section. For each field, show one of:
- **Extracted:** the value found in the source document(s), with a quote or reference
- **Inferred from 1.1:** the value carried over from the business objectives document
- **Inferred from 1.2:** the value carried over from the situation assessment
- **Missing:** flag it clearly

Then ask the user to:
1. **Confirm or correct** the extracted information
2. **Fill in the missing fields**

Format the ask like this:

> Here's what I extracted from the existing CRISP-DM documents and your [additional sources]. Please review and fill in the gaps:
>
> **Data Mining Problem Specification**
> - Problem Type: *Time series forecasting (regression)* ✓ (inferred from 1.1: "predict incoming transport units")
> - Target Variable: *Number of transport units (carts, pallets, boxes)* ✓ (from 1.1)
> - Prediction Granularity: *Per store, per day, per section* ✓ (from 1.1)
> - Prediction Horizon: *3–6 weeks ahead* ✓ (from 1.1)
> - Input Features: **MISSING** — What categories of features do you expect to use? (e.g., historical volumes, promotions, calendar effects, weather)
> - Modeling Assumptions: **MISSING**
>
> **Data Mining Goals**
> - Goal 1: *[mapped from business objective 1]* ✓
> - Model Output Format: **MISSING** — Should the model produce point forecasts, prediction intervals, or both?
> - ...
>
> **[continue for all sections]**
>
> Please confirm the extracted items are correct and provide the missing ones.

**Important rules for this step:**
- Ask about ALL missing fields in a single message — do not split into multiple rounds for gaps
- If a field is ambiguous in the source, present your best interpretation and ask for confirmation
- If the problem type is unclear, suggest the most likely type with reasoning and ask for confirmation
- If success criteria are vague, propose specific metrics with reasonable thresholds based on domain knowledge
- If no baseline exists, suggest establishing one (e.g., naive forecast, current manual process accuracy)

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

Write the file `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md` using this template:

```markdown
# 1.3 Data Mining Goals

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 1. Business Understanding
> **Status:** Draft | Review | Approved

---

## Data Mining Problem Specification

- **Problem Type:** [regression / classification / clustering / time series forecasting / etc.]
- **Target Variable(s):** [what is being predicted or classified]
- **Prediction Granularity:** [level of detail — per store, per day, per product, etc.]
- **Prediction Horizon:** [how far ahead, if applicable]
- **Model Output Format:** [point forecast / probability / class label / ranking / prediction interval]
- **Intended Use of Output:** [decision support / automation / monitoring / reporting]
- **Interpretability Requirement:** [explainable required / black box acceptable / hybrid]

### Input Feature Categories
| Category | Examples | Source |
|----------|----------|--------|
| [category] | [example features] | [data source from 1.2] |

### Modeling Assumptions
- [assumption 1]
- [assumption 2]

---

## Data Mining Goals

### Objective-to-Goal Traceability

| # | Business Objective (from 1.1) | Data Mining Goal | Problem Type | Output |
|---|-------------------------------|------------------|--------------|--------|
| 1 | [business objective] | [technical data mining goal] | [type] | [what the model produces] |
| 2 | ... | ... | ... | ... |

### Goal Details

#### Goal 1: [goal name]
- **Business Objective:** [reference to 1.1]
- **Technical Description:** [detailed technical description of what the model should do]
- **Target Variable:** [specific variable]
- **Key Predictors:** [expected important features]
- **Output Format:** [what the model produces]

#### Goal 2: [goal name]
[repeat structure as needed]

---

## Data Mining Success Criteria

| # | Metric | Threshold | Baseline | Related Goal | Evaluation Method |
|---|--------|-----------|----------|--------------|-------------------|
| 1 | [metric name] | [target value] | [current baseline] | [which goal] | [how to evaluate] |
| 2 | ... | ... | ... | ... | ... |

### Baseline Definition
- **Current Approach:** [description of what the model must beat]
- **Baseline Performance:** [measured or estimated performance of current approach]
- **How Baseline Was Established:** [measurement method]

### Evaluation Methodology
- **Validation Strategy:** [cross-validation / time-based split / hold-out / etc.]
- **Test Period:** [specific period or approach for the test set]
- **Evaluation Frequency:** [how often model performance is reassessed]

### Business-to-Technical Criteria Mapping

| Business Success Criterion (from 1.1) | Technical Metric | Rationale |
|---------------------------------------|------------------|-----------|
| [business criterion] | [technical metric and threshold] | [why this metric captures business success] |

---

## Scope & Constraints

### In Scope
- [what the data mining effort will cover]

### Out of Scope
- [what is explicitly excluded]

### Known Data Limitations
- [limitation 1 — from 1.2 or user input]
- [limitation 2]

### Performance Requirements
- **Inference Latency:** [acceptable response time]
- **Retraining Frequency:** [how often the model should be retrained]
- **Data Freshness:** [how recent the input data must be]

---

## To Be Clarified

[List any items that could not be determined from the source documents or user input. Remove this section if everything is complete.]

---

## Source Documents

- [List the meeting notes, Notion pages, or other sources used to produce this document]
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Sponsor | | | Pending |
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 7: Summary and Next Steps

After writing the document, present a summary:

> **Data Mining Goals document created** at `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
>
> **Summary:**
> - Problem type: [problem type]
> - [N] data mining goals defined, mapped to [N] business objectives
> - [N] success criteria defined with baselines and evaluation methodology
> - Scope: [brief in-scope / out-of-scope summary]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/produce-project-plan` to create the project plan with stages, resources, and timeline (Task 1.4).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 1.3 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Every data mining goal maps to at least one business objective (traceability)
- [ ] Every success criterion has a measurable threshold (a number or clear boundary)
- [ ] Every success criterion specifies a baseline to beat
- [ ] The evaluation methodology is appropriate for the problem type (e.g., time-based split for time series)
- [ ] The problem type matches the business objective (e.g., don't use classification for a forecasting problem)
- [ ] Model output format matches what stakeholders need (from 1.1 and 1.2)
- [ ] Interpretability requirements align with the intended audience (from 1.2)
- [ ] Known data limitations from 1.2 are reflected in scope constraints
- [ ] No PII or sensitive data is included in the document
- [ ] Document cross-references both the 1.1 and 1.2 documents where applicable
