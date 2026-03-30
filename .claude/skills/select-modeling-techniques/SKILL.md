---
name: select-modeling-techniques
description: "CRISP-DM 4.1 — Select Modeling Techniques. Evaluates candidate modeling approaches against data mining goals, data characteristics, and project constraints. Produces a structured technique selection report with rationale, assumption checks, and baseline definition in docs/crisp-dm/4-modeling/."
argument-hint: "<optional: specific technique to evaluate, or modeling constraint to consider>"
---

# /select-modeling-techniques — CRISP-DM 4.1: Select Modeling Techniques

> **Phase:** 4. Modeling | **Task:** 4.1 Select Modeling Techniques
>
> *"Select the actual modeling technique(s) to be used. Whereas in the business understanding phase you may already have selected a tool, this task refers to the specific modeling technique. If multiple techniques are applied, perform this task separately for each technique."*

## Purpose

This skill evaluates candidate modeling techniques against the data mining goals, data characteristics, and project constraints. It produces a structured comparison leading to a justified selection of techniques to build, always including a baseline.

## Output Location

All artifacts are written to: `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
- If it exists, present its contents and ask: *"A modeling technique selection report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines the target variable, prediction granularity, forecast horizon, and success criteria.
  - If it does not exist, warn: *"No data mining goals document found (task 1.3). It's strongly recommended to complete 1.3 first. Proceed anyway?"*
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — it contains patterns, distributions, temporal structure, and feature hypotheses that inform technique selection.
- Read `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
  - If it exists, use it — data quality issues may constrain which techniques are feasible.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — it contains constraints (interpretability, latency, compute budget) that affect technique selection.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Problem type** (regression, classification, time series forecasting, etc.)
- **Target variable** and its characteristics (continuous, discrete, distribution shape)
- **Prediction granularity** (per store, per day, per section, etc.)
- **Forecast horizon** (how far ahead)
- **Key data characteristics** (seasonality, trend, stationarity, multicollinearity, missing data patterns)
- **Success criteria** (metrics and thresholds from 1.3)
- **Constraints** (interpretability, latency, compute, team expertise)
- **Feature hypotheses** (from 2.3 — what predictors are available and promising)

Present what was extracted and what is missing. Ask the user to fill gaps.

### Step 3: Identify Candidate Techniques

Based on the problem type and data characteristics, propose candidate techniques. Always include:

1. **A naive baseline** — simplest possible approach (e.g., last-value forecast, historical average, seasonal naive)
2. **A simple statistical/ML baseline** — e.g., linear regression, ARIMA, exponential smoothing
3. **2-3 more sophisticated techniques** — chosen based on data characteristics and problem type

For each candidate, document:
- **Name and family** (e.g., LightGBM — gradient boosted trees)
- **Why considered** — what about the data/problem makes this technique suitable
- **Key assumptions** — what the technique assumes about the data
- **Assumption check** — whether the data satisfies these assumptions (reference 2.3 findings)
- **Strengths** for this specific problem
- **Weaknesses** for this specific problem
- **Interpretability** (high / medium / low)
- **Computational cost** (low / medium / high)
- **Implementation complexity** (low / medium / high)
- **Team familiarity** (if known)

### Step 4: Compare and Select

Create a comparison matrix and recommend which techniques to build. Selection criteria should include:
- Alignment with data mining goals and success criteria
- Suitability for the data characteristics
- Interpretability requirements
- Computational and operational constraints
- Team expertise
- Risk of overfitting vs. underfitting

Present the comparison and recommendation to the user for confirmation.

### Step 5: Document Modeling Assumptions

For each selected technique, document:
- **Data requirements** — what preprocessing is needed (scaling, encoding, stationarity transforms)
- **Hyperparameters to tune** — key hyperparameters and initial search ranges
- **Known limitations** — what the technique cannot capture
- **Fallback plan** — if this technique underperforms, what to try next

### Step 6: Present and Confirm

Present the full technique selection to the user and ask:
1. **Are there any techniques you'd like to add or remove?**
2. **Do the assumptions and constraints align with your understanding?**
3. **Is the baseline appropriate?**

Wait for the user's response before finalizing.

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/4-modeling
```

Write the file `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md` using this template:

```markdown
# 4.1 Modeling Technique Selection

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 4. Modeling
> **Status:** Draft | Review | Approved

---

## Problem Summary

- **Problem Type:** [regression / classification / time series forecasting / etc.]
- **Target Variable:** [name and description]
- **Prediction Granularity:** [per store, per day, per section, etc.]
- **Forecast Horizon:** [how far ahead]
- **Primary Success Metric:** [from 1.3, with threshold]
- **Secondary Metrics:** [from 1.3]

---

## Data Characteristics Affecting Technique Selection

| Characteristic | Finding (from EDA) | Impact on Technique Choice |
|---|---|---|
| Distribution of target | [from 2.3] | [e.g., high skew suggests log transform or tree-based methods] |
| Seasonality | [from 2.3] | [e.g., strong weekly pattern requires seasonal modeling] |
| Trend | [from 2.3] | [e.g., upward trend requires trend-aware methods] |
| Missing data | [from 2.4] | [e.g., 5% missing — tree methods handle natively] |
| Feature count | [from 2.2/2.3] | [e.g., moderate — no dimensionality reduction needed] |
| Sample size | [from 2.2] | [e.g., large — deep learning feasible] |
| Multicollinearity | [from 2.3] | [e.g., present — regularization or tree methods preferred] |

---

## Candidate Techniques

### Technique 1: [Name] (Baseline)
- **Family:** [e.g., naive forecast]
- **Why considered:** Every model must beat this to be useful
- **Assumptions:** [list]
- **Assumption check:** [met / partially met / not met — with evidence from 2.3]
- **Strengths:** [for this problem]
- **Weaknesses:** [for this problem]
- **Interpretability:** High
- **Computational cost:** Low
- **Implementation complexity:** Low

### Technique 2: [Name]
[same structure]

### Technique 3: [Name]
[same structure]

### Technique 4: [Name]
[same structure]

---

## Technique Comparison Matrix

| Criterion | [Technique 1] | [Technique 2] | [Technique 3] | [Technique 4] |
|---|---|---|---|---|
| Goal alignment | [rating] | [rating] | [rating] | [rating] |
| Assumption fit | [rating] | [rating] | [rating] | [rating] |
| Interpretability | [rating] | [rating] | [rating] | [rating] |
| Computational cost | [rating] | [rating] | [rating] | [rating] |
| Implementation effort | [rating] | [rating] | [rating] | [rating] |
| Handles seasonality | [Yes/No/Partial] | [Yes/No/Partial] | [Yes/No/Partial] | [Yes/No/Partial] |
| Handles missing data | [Yes/No/Partial] | [Yes/No/Partial] | [Yes/No/Partial] | [Yes/No/Partial] |
| Risk of overfitting | [Low/Medium/High] | [Low/Medium/High] | [Low/Medium/High] | [Low/Medium/High] |
| **Overall suitability** | [score] | [score] | [score] | [score] |

---

## Selected Techniques

| Priority | Technique | Role | Justification |
|---|---|---|---|
| 1 | [Baseline] | Benchmark | [why] |
| 2 | [Technique] | Primary candidate | [why] |
| 3 | [Technique] | Alternative | [why] |

---

## Modeling Assumptions & Requirements

### [Selected Technique 1]
- **Preprocessing required:** [scaling, encoding, stationarity transforms, etc.]
- **Key hyperparameters:** [list with initial search ranges]
- **Known limitations:** [what it cannot capture]
- **Fallback plan:** [if it underperforms]

### [Selected Technique 2]
[same structure]

---

## Techniques Considered but Not Selected

| Technique | Reason for Exclusion |
|---|---|
| [technique] | [why — e.g., too complex for current data size, doesn't handle seasonality] |

---

## To Be Clarified

[List any items that need further investigation or domain expert input. Remove this section if everything is complete.]

---

## Source Documents

- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- 2.4 Data Quality: `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Domain Expert | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary:

> **Modeling Technique Selection created** at `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
>
> **Summary:**
> - [N] candidate techniques evaluated
> - Baseline: [technique name]
> - Primary candidate: [technique name]
> - Key selection factors: [brief summary]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/generate-test-design` to define the train/validation/test strategy, evaluation metrics, and experiment tracking plan (Task 4.2).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 4.1 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] A simple baseline technique is always included
- [ ] Every candidate technique has a clear rationale for consideration
- [ ] Data assumptions are checked against actual EDA findings from 2.3
- [ ] The comparison matrix covers all relevant criteria
- [ ] Selected techniques map to data mining goals from 1.3
- [ ] Interpretability requirements from stakeholders are considered
- [ ] Preprocessing requirements are documented for each selected technique
- [ ] Fallback plans exist for each selected technique
- [ ] Techniques not selected have documented exclusion rationale
- [ ] No PII or sensitive data in the report
