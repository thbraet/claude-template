---
name: generate-test-design
description: "CRISP-DM 4.2 — Generate Test Design. Defines train/validation/test splitting strategy, cross-validation approach, evaluation metrics, baseline definition, and experiment tracking plan. Produces a structured test design document in docs/crisp-dm/4-modeling/."
argument-hint: "<optional: specific splitting concern, metric question, or CV strategy to evaluate>"
---

# /generate-test-design — CRISP-DM 4.2: Generate Test Design

> **Phase:** 4. Modeling | **Task:** 4.2 Generate Test Design
>
> *"Before we actually build a model, we need to generate a procedure or mechanism to test the model's quality and validity. The test design also needs to consider the appropriate evaluation criteria."*

## Purpose

This skill defines the experimental framework for model building: how data is split, how models are evaluated, what metrics matter, and how experiments are tracked. It ensures rigorous, reproducible evaluation that prevents data leakage and aligns technical metrics with business success criteria.

## Output Location

All artifacts are written to: `docs/crisp-dm/4-modeling/4.2-test-design.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/4-modeling/4.2-test-design.md`
- If it exists, present its contents and ask: *"A test design document already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines success criteria, metrics, and evaluation methodology requirements.
  - If it does not exist, warn: *"No data mining goals document found (task 1.3). It's strongly recommended to complete 1.3 first. Proceed anyway?"*
- Read `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
  - If it exists, use it — it defines which techniques will be built and their assumptions.
  - If it does not exist, warn: *"No modeling technique selection found (task 4.1). It's recommended to complete 4.1 first. Proceed anyway?"*
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — temporal patterns and data characteristics inform splitting strategy.
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — date ranges, sample sizes, and granularity inform split sizing.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Problem type** and whether it is a time series problem
- **Forecast horizon** (how far ahead predictions are needed)
- **Data date range** and total sample size
- **Temporal structure** (frequency, seasonality periods, structural breaks)
- **Granularity levels** (e.g., per store, per section) and group counts
- **Success criteria** (metrics and thresholds from 1.3)
- **Selected techniques** and their specific evaluation needs (from 4.1)
- **Known data quality issues** that may affect evaluation (from 2.4)

Present what was extracted and what is missing. Ask the user to fill gaps.

### Step 3: Design the Splitting Strategy

Based on the problem type and data characteristics, design the data splitting approach:

**For time series problems:**
- **Temporal split** — training ends at cutoff date, validation covers the forecast horizon after cutoff, test covers a subsequent period
- **Expanding window CV** — progressively larger training sets with fixed-size validation windows
- **Sliding window CV** — fixed-size training windows sliding forward
- Never use random splits for time series

**For non-time-series problems:**
- **Stratified split** — preserving target distribution and key group proportions
- **Grouped split** — ensuring all records from the same entity (store, customer) stay together
- **K-fold CV** — with stratification and/or grouping as needed

Document:
- Exact split ratios or dates
- Rationale for the chosen approach
- How the validation period aligns with the forecast horizon
- How the test set mimics the production use case
- Group handling (e.g., all data for a store stays in one fold)

### Step 4: Define Evaluation Metrics

Map data mining success criteria from 1.3 to specific evaluation metrics:

- **Primary metric** — the single metric used for model selection and comparison
- **Secondary metrics** — additional metrics that provide complementary views
- **Business translation** — how each metric translates to business impact

For each metric, document:
- Name and formula
- Why it was chosen (connection to business objective)
- Threshold for success (from 1.3)
- How to compute it (library, function)
- Aggregation level (overall, per store, per section)

Also define:
- **Baseline performance** — expected metric values for the baseline model
- **Minimum improvement** — how much better a model must be vs. baseline to justify its complexity

### Step 5: Define the Experiment Tracking Plan

Document how experiments will be logged in MLflow:

- **Experiment name** — naming convention
- **Run naming** — how individual runs are named
- **Parameters to log** — hyperparameters, data version, split configuration
- **Metrics to log** — all evaluation metrics, at all aggregation levels
- **Artifacts to log** — trained models, feature importance, prediction samples, plots
- **Tags** — technique family, phase (baseline/tuning/final), data version

### Step 6: Present and Confirm

Present the full test design to the user and ask:
1. **Does the splitting strategy correctly reflect how the model will be used in production?**
2. **Are the evaluation metrics aligned with what stakeholders care about?**
3. **Is the baseline definition appropriate?**
4. **Any concerns about data leakage in this design?**

Wait for the user's response before finalizing.

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/4-modeling
```

Write the file `docs/crisp-dm/4-modeling/4.2-test-design.md` using this template:

```markdown
# 4.2 Test Design

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 4. Modeling
> **Status:** Draft | Review | Approved

---

## Design Overview

- **Problem Type:** [time series forecasting / regression / classification]
- **Data Date Range:** [start] to [end]
- **Total Records:** [count]
- **Granularity:** [per store, per day, per section, etc.]
- **Forecast Horizon:** [N days/weeks ahead]
- **Selected Techniques:** [from 4.1]

---

## Data Splitting Strategy

### Approach: [Temporal Split / Expanding Window CV / Stratified K-Fold / etc.]

**Rationale:** [why this approach was chosen — must reference the problem type and data characteristics]

### Split Definition

| Set | Date Range / Criteria | Records | Proportion | Purpose |
|-----|----------------------|---------|------------|---------|
| Training | [range/criteria] | [count] | [%] | Model fitting |
| Validation | [range/criteria] | [count] | [%] | Hyperparameter tuning & model selection |
| Test | [range/criteria] | [count] | [%] | Final unbiased evaluation |

### Cross-Validation Design

- **Strategy:** [expanding window / sliding window / grouped K-fold / etc.]
- **Number of folds/windows:** [N]
- **Window sizes:** Training = [size], Validation = [size], Gap = [size if applicable]
- **Group handling:** [how store/section groups are handled]

```
[ASCII diagram showing the CV windows/folds]
```

### Data Leakage Prevention

| Risk | Mitigation |
|------|-----------|
| Future information in features | [how temporal features are computed — always using only past data] |
| Target leakage | [features excluded or lagged appropriately] |
| Preprocessing leakage | [fit on training only, transform validation/test] |
| Group leakage | [all records for an entity in same split] |

---

## Evaluation Metrics

### Primary Metric

| Attribute | Value |
|-----------|-------|
| **Name** | [e.g., MAE, RMSE, MAPE, wMAPE] |
| **Formula** | [mathematical formula] |
| **Why chosen** | [connection to business objective from 1.1/1.3] |
| **Success threshold** | [from 1.3] |
| **Aggregation** | [overall / per store / per section] |
| **Implementation** | [library.function or custom code reference] |

### Secondary Metrics

| Metric | Formula | Why Included | Threshold |
|--------|---------|-------------|-----------|
| [metric] | [formula] | [rationale] | [threshold if any] |

### Business Translation

| Technical Metric | Business Meaning | Example |
|-----------------|-----------------|---------|
| [e.g., MAE of 5 units] | [e.g., workforce misallocated by ~30 min/day] | [concrete scenario] |

---

## Baseline Definition

| Attribute | Value |
|-----------|-------|
| **Technique** | [e.g., seasonal naive — last week's same day] |
| **Expected performance** | [estimated metric values based on EDA] |
| **Minimum improvement** | [how much better a model must be to justify deployment] |
| **Justification** | [why this is the right baseline — not too easy, not too hard] |

---

## Experiment Tracking Plan (MLflow)

### Naming Conventions

- **Experiment name:** `[project-name]-[phase]` (e.g., `store-capacity-modeling`)
- **Run name:** `[technique]-[variant]-[timestamp]` (e.g., `lgbm-default-20260330`)

### What to Log

| Category | Items |
|----------|-------|
| **Parameters** | [list: hyperparameters, data version, split config, feature set version] |
| **Metrics** | [list: all evaluation metrics at all aggregation levels] |
| **Artifacts** | [list: trained model, feature importance, residual plots, prediction samples] |
| **Tags** | [list: technique family, phase, data version, author] |

### Experiment Comparison

- Models are compared on the **validation set** during development
- The **test set** is used only for the final selected model(s)
- All comparisons must include the baseline run as reference

---

## Reproducibility Requirements

- [ ] Random seed: [value, e.g., 42] — used consistently across all experiments
- [ ] Data version: tracked via DVC hash
- [ ] Code version: tracked via git commit SHA
- [ ] Environment: tracked via `requirements.txt` or `conda.yml`
- [ ] Split logic: deterministic given the above

---

## To Be Clarified

[List any items that need further investigation or domain expert input. Remove this section if everything is complete.]

---

## Source Documents

- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 4.1 Modeling Techniques: `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- 2.2 Data Description: `docs/crisp-dm/2-data-understanding/2.2-data-description.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Domain Expert | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary:

> **Test Design created** at `docs/crisp-dm/4-modeling/4.2-test-design.md`
>
> **Summary:**
> - Splitting strategy: [approach — e.g., temporal split with expanding window CV]
> - Training period: [range], Validation: [range], Test: [range]
> - Primary metric: [metric] (threshold: [value])
> - Baseline: [technique name]
> - [N] data leakage mitigations documented
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/build-model` to start building the baseline and candidate models according to this test design (Task 4.3).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 4.2 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Splitting strategy is appropriate for the problem type (temporal for time series, never random)
- [ ] Validation period aligns with the forecast horizon
- [ ] Test set mimics the production use case
- [ ] All data leakage risks are identified and mitigated
- [ ] Evaluation metrics map to data mining success criteria from 1.3
- [ ] Business translation of metrics is concrete and understandable
- [ ] Baseline is clearly defined with expected performance
- [ ] Minimum improvement threshold is specified
- [ ] MLflow experiment tracking plan is complete
- [ ] Reproducibility requirements are documented (seed, data version, code version)
- [ ] Cross-validation diagram is clear and correct
- [ ] Preprocessing is fit on training data only
- [ ] No PII or sensitive data in the report
