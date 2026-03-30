---
name: assess-model
description: "CRISP-DM 4.4 — Assess Model. Evaluates trained models through error analysis, subgroup performance, overfitting assessment, and business impact translation. Produces a structured model assessment report with recommendations in docs/crisp-dm/4-modeling/."
argument-hint: "<optional: specific model to assess, MLflow run ID, or assessment question>"
---

# /assess-model — CRISP-DM 4.4: Assess Model

> **Phase:** 4. Modeling | **Task:** 4.4 Assess Model
>
> *"Whereas the Generate Test Design task describes how to evaluate the model, this task interprets the model results. The data mining engineer judges the success of the application of modeling and discovery techniques technically, then contacts business analysts and domain experts to discuss the results in the business context."*

## Purpose

This skill performs deep assessment of trained models beyond aggregate metrics. It analyzes where models succeed and fail, identifies systematic biases, evaluates overfitting risk, translates technical performance into business impact, and produces a justified recommendation on which model(s) to advance to Phase 5 (Evaluation).

## Output Location

This skill produces two artifacts plus visualizations:

1. **Jupyter notebook** (primary): `notebooks/4.4-model-assessment.ipynb` — contains all error analysis code, subgroup performance analysis, overfitting assessment, inline visualizations, and markdown narrative. This is the working artifact where model assessment happens.
2. **Summary document**: `docs/crisp-dm/4-modeling/4.4-model-assessment.md` — a structured summary of the model assessment report extracted from the notebook. This is the CRISP-DM documentation artifact.
3. **Assessment visualizations**: saved to `reports/figures/assessment/`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/4.4-model-assessment.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/4-modeling/4.4-model-assessment.md` (the summary document)
- If either exists, present what's found and ask: *"A model assessment [notebook/report/both] already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
  - If it exists, use it — it describes the selected techniques and their assumptions.
- Read `docs/crisp-dm/4-modeling/4.2-test-design.md`
  - If it exists, use it — it defines the evaluation metrics and success thresholds.
  - If it does not exist, warn: *"No test design found (task 4.2). Assessment requires knowing the evaluation framework."*
- Read `docs/crisp-dm/4-modeling/4.3-model-building.md`
  - If it exists, use it — it contains the results summary and MLflow run references.
  - If it does not exist, warn: *"No model building report found (task 4.3). There are no models to assess. Complete 4.3 first."*
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — business success criteria determine whether models are fit for purpose.
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — data mining success criteria provide technical thresholds.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Models built** (from 4.3) — techniques, configurations, validation metrics
- **Baseline performance** (from 4.3)
- **Success thresholds** (from 1.3) — technical metrics and minimum improvement
- **Business success criteria** (from 1.1) — what stakeholders need
- **Evaluation metrics** (from 4.2) — primary and secondary
- **Business metric translation** (from 4.2) — how technical metrics map to business impact

Present what was extracted and what is missing. Ask the user to fill gaps.

### Step 3: Perform Error Analysis

For each model (including baseline), generate code to analyze errors:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("reports/figures/assessment", exist_ok=True)

# Load predictions and actuals from MLflow or saved artifacts

# --- Residual analysis ---
residuals = actuals - predictions
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
# Residual distribution
axes[0, 0].hist(residuals, bins=50)
axes[0, 0].set_title("Residual Distribution")
# Residuals vs predicted
axes[0, 1].scatter(predictions, residuals, alpha=0.3)
axes[0, 1].axhline(y=0, color='r', linestyle='--')
axes[0, 1].set_title("Residuals vs Predicted")
# Residuals over time
axes[1, 0].plot(dates, residuals)
axes[1, 0].set_title("Residuals Over Time")
# QQ plot
from scipy import stats
stats.probplot(residuals, plot=axes[1, 1])
plt.tight_layout()
plt.savefig("reports/figures/assessment/residual_analysis_[model].png", dpi=150)
plt.close()

# --- Worst predictions ---
# Top N worst predictions with context
# --- Error by time period ---
# --- Error by segment ---
```

Analyze:
- **Residual distribution** — are errors normally distributed, biased, heavy-tailed?
- **Error patterns** — do errors correlate with time, magnitude, or features?
- **Worst predictions** — what do the worst cases have in common?
- **Systematic biases** — does the model consistently over- or under-predict for certain segments?

### Step 4: Assess Subgroup Performance

Evaluate model performance across key segments:

- **By store** — which stores have best/worst performance?
- **By section** — which product sections are hardest to predict?
- **By time period** — is performance stable across weeks, months, seasons?
- **By volume level** — does the model handle high-volume and low-volume days equally?
- **By day of week** — are certain days systematically harder?

For each segment, compute:
- Primary metric
- Relative performance vs. overall
- Whether the segment meets the success threshold

Flag segments where performance is unacceptable and recommend mitigation (e.g., separate models, additional features, data collection).

### Step 5: Assess Overfitting

Compare training and validation performance:

| Model | Train [Metric] | Validation [Metric] | Gap | Interpretation |
|-------|---------------|---------------------|-----|---------------|
| [model] | [value] | [value] | [value] | [overfit / underfit / good fit] |

Also assess:
- **Learning curves** — does validation performance plateau or degrade with more data?
- **Complexity vs. performance** — is the improvement from complex models worth the added risk?
- **Regularization sensitivity** — how much do results change with regularization strength?

### Step 6: Translate to Business Impact

Map technical metrics to business terms:

- **Primary metric in business terms** — e.g., "MAE of 5 carts means workforce planning is off by approximately 30 minutes per store per day"
- **Cost of errors** — what does over-prediction vs. under-prediction cost the business?
- **Error asymmetry** — is over-predicting worse than under-predicting (or vice versa)?
- **Aggregate business impact** — across all stores, what is the total cost/benefit of this prediction accuracy?

### Step 7: Formulate Recommendations

Based on all assessments, recommend:

1. **Model(s) to advance** — which model(s) should proceed to Phase 5 (Evaluation)?
2. **Justification** — why this model, connecting to both technical and business criteria
3. **Known limitations** — what the model cannot do, where it fails
4. **Risk assessment** — what could go wrong in production
5. **Next steps** — one of:
   - **Proceed to Evaluation (Phase 5)** — model is ready for stakeholder review
   - **Iterate on Modeling** — try additional techniques, features, or tuning
   - **Revisit Data Preparation (Phase 3)** — data issues limit model performance
   - **Revisit Data Understanding (Phase 2)** — need more data or better understanding

Present recommendations and ask the user for confirmation.

### Step 8: Create the Notebook and Generate the Output Document

After gathering all information, first create the Jupyter notebook at `notebooks/4.4-model-assessment.ipynb` using the `NotebookEdit` tool. The notebook is the primary artifact — all assessment code happens here.

**Notebook structure:**
- **Setup & Data Loading** — imports, load predictions and actuals from MLflow
- **Error Analysis** — residual distribution, residuals vs predicted, residuals over time, QQ plot
- **Worst Predictions** — identify and analyze the worst prediction cases
- **Subgroup Performance** — performance by store, section, time period, volume level
- **Overfitting Assessment** — train vs. validation comparison, learning curves
- **Business Impact Translation** — metric translation, error cost asymmetry
- **Model Selection Recommendation** — final recommendation with justification

Use the `NotebookEdit` tool to create and populate the notebook cell by cell. Run code cells to generate outputs inline. Save visualizations to `reports/figures/assessment/`.

Then create the summary document.

```bash
mkdir -p docs/crisp-dm/4-modeling
mkdir -p reports/figures/assessment
```

Write the file `docs/crisp-dm/4-modeling/4.4-model-assessment.md` using this template:

```markdown
# 4.4 Model Assessment Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 4. Modeling
> **Status:** Draft | Review | Approved

---

## Assessment Overview

- **Models Assessed:** [list]
- **Assessment Date:** [date]
- **Validation Period:** [date range]
- **Primary Metric:** [metric name]
- **Success Threshold:** [from 1.3]
- **MLflow Experiment:** [name and link]

---

## Results Summary

| Model | [Primary Metric] | vs. Baseline | Meets Threshold | Rank |
|-------|------------------|-------------|----------------|------|
| Baseline | [value] | — | [Yes/No] | [N] |
| [Model A] tuned | [value] | [+/- %] | [Yes/No] | [N] |
| [Model B] tuned | [value] | [+/- %] | [Yes/No] | [N] |

---

## Error Analysis

### Residual Distribution
![Residual Analysis](../../reports/figures/assessment/residual_analysis_[best_model].png)

- **Bias:** [positive / negative / unbiased — mean residual = X]
- **Spread:** [std of residuals = X]
- **Tail behavior:** [light / heavy — kurtosis = X]
- **Heteroscedasticity:** [present / absent — does error variance change with predicted value?]

### Worst Predictions

| Rank | Date | Store | Section | Actual | Predicted | Error | Possible Cause |
|------|------|-------|---------|--------|-----------|-------|---------------|
| 1 | [date] | [store] | [section] | [value] | [value] | [value] | [hypothesis] |

### Systematic Error Patterns

| Pattern | Description | Affected Segments | Severity |
|---------|-------------|------------------|----------|
| [pattern] | [description] | [which stores/sections/periods] | [High/Medium/Low] |

---

## Subgroup Performance

### By Store
| Store | [Primary Metric] | vs. Overall | Meets Threshold | Flag |
|-------|------------------|-------------|----------------|------|
| [store] | [value] | [+/- %] | [Yes/No] | [if problematic] |

### By Section
| Section | [Primary Metric] | vs. Overall | Meets Threshold | Flag |
|---------|------------------|-------------|----------------|------|
| [section] | [value] | [+/- %] | [Yes/No] | [if problematic] |

### By Time Period
| Period | [Primary Metric] | vs. Overall | Notes |
|--------|------------------|-------------|-------|
| [period] | [value] | [+/- %] | [e.g., "holiday weeks harder"] |

### By Volume Level
| Volume Bucket | [Primary Metric] | vs. Overall | Notes |
|--------------|------------------|-------------|-------|
| Low (< P25) | [value] | [+/- %] | [notes] |
| Medium (P25-P75) | [value] | [+/- %] | [notes] |
| High (> P75) | [value] | [+/- %] | [notes] |

### Underperforming Segments
| Segment | [Primary Metric] | Issue | Recommended Mitigation |
|---------|------------------|-------|----------------------|
| [segment] | [value] | [why it underperforms] | [separate model / more features / more data] |

---

## Overfitting Assessment

| Model | Train [Metric] | Validation [Metric] | Gap (%) | Verdict |
|-------|---------------|---------------------|---------|---------|
| [model] | [value] | [value] | [%] | [Overfit / Underfit / Good Fit] |

### Learning Curves
![Learning Curves](../../reports/figures/assessment/learning_curves.png)

- **Observations:** [do train and validation converge? does validation plateau?]

---

## Business Impact Translation

### Metric Translation
| Technical Metric | Value | Business Meaning |
|-----------------|-------|-----------------|
| [e.g., MAE = 5 carts] | [value] | [e.g., ~30 min workforce misallocation per store per day] |

### Error Cost Asymmetry
- **Over-prediction cost:** [what happens when we predict too high — e.g., overstaffing]
- **Under-prediction cost:** [what happens when we predict too low — e.g., understaffing, missed deliveries]
- **Recommended bias:** [should the model be biased toward over- or under-prediction?]

### Aggregate Business Impact
- **Across all stores:** [total cost/benefit of current model accuracy]
- **vs. current process:** [improvement over how it's done today]
- **vs. baseline model:** [incremental value of the best model over the simple baseline]

---

## Model Selection Recommendation

### Recommended Model(s)

| Attribute | Value |
|-----------|-------|
| **Model** | [technique + configuration] |
| **MLflow Run ID** | [run ID] |
| **Primary Metric** | [value] ([+/- %] vs. baseline) |
| **Justification** | [why this model — technical and business reasons] |
| **Known Limitations** | [what it cannot do, where it fails] |
| **Production Risks** | [what could go wrong] |

### Recommended Next Phase

**[Proceed to Evaluation / Iterate on Modeling / Revisit Data Preparation / Revisit Data Understanding]**

**Rationale:** [why this recommendation]

**If iterating, priorities:**
1. [first thing to try]
2. [second thing to try]
3. [third thing to try]

---

## To Be Clarified

[List any items that need further investigation or domain expert input. Remove this section if everything is complete.]

---

## Source Documents

- 4.1 Modeling Techniques: `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
- 4.2 Test Design: `docs/crisp-dm/4-modeling/4.2-test-design.md`
- 4.3 Model Building: `docs/crisp-dm/4-modeling/4.3-model-building.md`
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Domain Expert | | | Pending |
| Business Stakeholder | | | Pending |
```

### Step 9: Summary and Next Steps

After writing both artifacts, present a summary:

> **Model Assessment complete.** Two artifacts created:
> - **Notebook:** `notebooks/4.4-model-assessment.ipynb` — full assessment code with inline outputs
> - **Summary:** `docs/crisp-dm/4-modeling/4.4-model-assessment.md` — structured report
> - **Figures:** `reports/figures/assessment/` — assessment visualizations
>
> **Summary:**
> - [N] models assessed
> - Best model: [technique] with [metric]: [value] ([+/- %] vs. baseline)
> - Meets success threshold: [Yes/No]
> - [N] underperforming segments identified
> - [N] systematic error patterns found
> - Business impact: [one-line summary]
> - Recommendation: [Proceed to Evaluation / Iterate / Revisit]
>
> **Next step in CRISP-DM:** [Based on recommendation]
> - If proceeding: Move to **Phase 5 (Evaluation)** — review results with business stakeholders and assess whether the model meets business success criteria
> - If iterating: Return to the specific modeling task that needs improvement
> - If revisiting data: Return to Phase 3 (Data Preparation) or Phase 2 (Data Understanding)

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 4.4 artifact link.

## Quality Checks

Before finalizing, verify:
- [ ] Jupyter notebook exists at `notebooks/4.4-model-assessment.ipynb` with all assessment code and inline outputs
- [ ] Notebook cells are executed and outputs are saved (results render when opened)
- [ ] All models are compared against the baseline
- [ ] Error analysis goes beyond aggregate metrics to identify systematic patterns
- [ ] Subgroup performance covers all key segments (stores, sections, time periods, volume levels)
- [ ] Overfitting is assessed with train/validation comparison
- [ ] Business impact is quantified in stakeholder-understandable terms
- [ ] Error cost asymmetry is documented (over- vs. under-prediction)
- [ ] Worst predictions are analyzed for common causes
- [ ] Underperforming segments have recommended mitigations
- [ ] The recommendation connects to both technical and business success criteria
- [ ] Next steps are concrete and actionable
- [ ] All visualizations are saved to `reports/figures/assessment/`
- [ ] No PII or sensitive data in the report or visualizations
- [ ] MLflow run IDs are referenced for traceability
