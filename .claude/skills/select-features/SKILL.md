---
name: select-features
description: "CRISP-DM 3.6 — Select Features. Evaluates which engineered features improve generalization vs. inflate CV estimates. Uses forward selection, backward elimination, and group analysis to find the optimal feature subset. Produces a feature selection report and generates submissions/predictions with the selected subset."
argument-hint: "<optional: feature list, target metric, or path to formatted dataset>"
---

# /select-features — CRISP-DM 3.6: Select Features

> **Phase:** 3. Data Preparation | **Task:** 3.6 Select Features
>
> *"This task addresses the selection of features to include in modeling. Feature selection reduces dimensionality, removes noise, and improves generalization — especially critical for small datasets where the feature-to-sample ratio can cause overfitting."*

## Purpose

This skill evaluates which features from the engineered feature set (3.3/3.5) genuinely improve model generalization vs. those that inflate CV estimates but hurt out-of-sample performance. It is a **mandatory validation step** between data preparation and modeling, designed to catch feature overfitting before it wastes modeling effort.

It produces three outputs:
1. **Feature group analysis** — tests logical groups of features to identify which groups contribute signal vs. noise
2. **Forward selection curve** — incrementally adds features, tracking both CV accuracy and overfit gap (train - CV)
3. **Optimal feature subset** — the selected features with rationale, plus submission files for validation

## Why This Step Exists

On small datasets (< 5,000 rows), adding features can inflate CV estimates while hurting generalization:
- Each feature adds degrees of freedom that the model can use to memorize training noise
- CV estimates become optimistic because the same features are used across all folds
- The gap between CV accuracy and true out-of-sample accuracy grows with feature count

This step catches the problem early by measuring the **overfit gap** (train accuracy - CV accuracy) as features are added. When the gap exceeds a threshold (~3%), additional features are likely hurting generalization.

## Output Location

This skill produces two artifacts:

1. **Jupyter notebook** (primary): `notebooks/3.6-feature-selection.ipynb` — contains all feature selection experiments, forward selection curves, and submission generation code.
2. **Summary document**: `docs/crisp-dm/3-data-preparation/3.6-select-features.md` — a structured summary of the feature selection results.

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/3.6-feature-selection.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/3-data-preparation/3.6-select-features.md` (the summary document)
- If either exists, present what's found and ask: *"Feature selection [notebook/report/both] already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/3-data-preparation/3.5-format-data.md`
  - If it exists, use it — it defines the formatted feature set available for selection.
- Read `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
  - If it exists, use it — it documents the feature engineering rationale.
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines the primary metric and success thresholds.
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — it contains feature importance hypotheses from EDA.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Full feature list** from 3.5 (all available features after formatting)
- **Feature groups** from 3.3 (logical groupings: demographic, temporal, domain-specific, etc.)
- **Primary metric** from 1.3 (what we're optimizing for)
- **Dataset size** from 3.5 (rows in training set — determines risk of feature overfitting)
- **Feature hypotheses** from 2.3 (expected strongest predictors)

Present what was extracted and identify the core features (strongest expected predictors) vs. peripheral features.

### Step 3: Feature Group Analysis

Test logical groups of features to understand which groups contribute signal vs. noise.

For each group:
1. Evaluate using a **low-variance model** (e.g., Logistic Regression with L2) to measure true signal
2. Evaluate using a **moderate-variance model** (e.g., regularized Random Forest) to check if interactions matter
3. Record **CV accuracy**, **train accuracy**, and **overfit gap** (train - CV)

Groups to test:
- Core features only (top 3-5 strongest predictors from EDA)
- Core + each feature group added incrementally
- All features combined

Present results as a comparison table with CV accuracy and overfit gap per group.

### Step 4: Forward Feature Selection

Starting from the core feature set, greedily add the feature that most improves CV accuracy:

1. Evaluate the core seed set
2. For each remaining feature, evaluate the seed + that feature
3. Add the best-performing feature to the selected set
4. Repeat until all features are included

Track at each step:
- CV accuracy (mean and std across folds)
- Train accuracy
- Overfit gap (train - CV)
- Delta from previous step

### Step 5: Identify Optimal Subset

From the forward selection curve, identify:
1. **Optimal subset** — highest CV accuracy where overfit gap < 3% (configurable threshold)
2. **Peak CV subset** — highest CV accuracy regardless of gap (for comparison)
3. **Diminishing returns point** — where adding features yields < 0.1% CV improvement

If the optimal and peak subsets differ significantly, flag this as evidence of feature overfitting.

### Step 6: Generate Notebook

Create the Jupyter notebook at `notebooks/3.6-feature-selection.ipynb` containing:
- Setup and data loading (using PROJECT_ROOT convention)
- Feature group analysis (Step 3)
- Forward selection experiment (Step 4)
- Visualization: CV accuracy and overfit gap curves vs. number of features
- Optimal subset identification (Step 5)
- Submission generation with the optimal subset using multiple model families
- Conclusions summarizing which features help, which hurt, and the recommended subset

### Step 7: Generate Summary Document

Write `docs/crisp-dm/3-data-preparation/3.6-select-features.md` using this template:

```markdown
# 3.6 Feature Selection

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 3. Data Preparation
> **Status:** Draft | Review | Approved

---

## Selection Overview

- **Total features available:** [N] (from 3.5 formatting)
- **Features selected:** [M]
- **Features dropped:** [N - M]
- **Selection method:** Forward selection with overfit gap monitoring
- **Primary metric:** [metric from 1.3]

---

## Feature Group Analysis

| Group | Features | LR CV Accuracy | LR Overfit Gap | RF CV Accuracy | RF Overfit Gap |
|-------|----------|---------------|---------------|---------------|---------------|
| [group] | [N] | [accuracy] | [gap] | [accuracy] | [gap] |

### Key Findings
- [Which groups contribute most signal]
- [Which groups increase the overfit gap without improving CV]
- [Interactions between groups]

---

## Forward Selection Results

| Step | Feature Added | N Features | CV Accuracy | Overfit Gap | Delta |
|------|-------------|-----------|-------------|-------------|-------|
| [step] | [feature] | [N] | [accuracy] | [gap] | [delta] |

### Optimal Subset
- **Features ([M]):** [list]
- **CV Accuracy:** [accuracy]
- **Overfit Gap:** [gap]
- **Rationale:** [why this cutoff]

### Dropped Features
| Feature | Reason for Exclusion | Impact When Included |
|---------|---------------------|---------------------|
| [feature] | [increases gap / no CV benefit / hurts CV] | [specifics] |

---

## Generalization Risk Assessment

| Metric | Core Features Only | Optimal Subset | All Features |
|--------|-------------------|---------------|-------------|
| N features | [N] | [M] | [total] |
| CV accuracy | [acc] | [acc] | [acc] |
| Overfit gap | [gap] | [gap] | [gap] |
| Expected Kaggle/test gap | [est] | [est] | [est] |

---

## Assumptions & Business Validation

[Standard assumption tracking section per project convention]

---

## Source Documents

- 3.3 Construct Data: `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
- 3.5 Format Data: `docs/crisp-dm/3-data-preparation/3.5-format-data.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
```

### Step 8: Summary and Next Steps

After writing both artifacts, present:

> **Feature selection complete.**
>
> **Selected [M] of [N] features.** The optimal subset achieves [CV accuracy] with a [gap]% overfit gap, compared to [all-feature CV] with [all-feature gap]% gap using all [N] features.
>
> **Dropped features:** [list with brief reasons]
>
> **Next step:** Proceed to Phase 4 — Modeling (4.1 Select Modeling Techniques) using the selected feature subset.

## Quality Checks

Before finalizing:
- [ ] Forward selection used a low-variance model (LR or similar) to avoid selection bias
- [ ] Overfit gap is tracked at every step
- [ ] The optimal subset is chosen by generalization potential, not just highest CV
- [ ] Dropped features have documented rationale
- [ ] The notebook runs end-to-end without errors
- [ ] Submissions are generated with the selected subset
- [ ] The feature-to-sample ratio is reasonable (< 1:20 as a guideline)
- [ ] Core features from EDA are all retained (if they improve CV)
- [ ] No PII or sensitive data in any output
