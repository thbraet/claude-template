---
name: construct-data
description: "CRISP-DM 3.3 — Construct Data. Engineers features, derives new attributes, generates new records, and transforms values for modeling. Documents every constructed feature with formula, source, and rationale. Produces a structured feature engineering report in docs/crisp-dm/3-data-preparation/."
argument-hint: "<feature ideas, target variable, or path to feature config>"
---

# /construct-data — CRISP-DM 3.3: Construct Data

> **Phase:** 3. Data Preparation | **Task:** 3.3 Construct Data
>
> *"This task includes constructive data preparation operations such as the production of derived attributes or entire new records, or transformed values for existing attributes."*

## Purpose

This skill engineers features and derives new attributes from the cleaned data (3.2) to maximize the predictive power of the modeling dataset. Every engineered feature is documented with its formula, source fields, and rationale. It produces four outputs:

1. **Feature Engineering Plan** — proposed features mapped to data mining goals and exploration hypotheses
2. **Derived Attributes** — new columns with formula, source, type, and rationale
3. **Generated Records** — any synthetic records (e.g., aggregations, time windows) with method and rationale
4. **Transformation Log** — all value transformations (scaling, encoding, binning) applied to existing fields

## Output Location

This skill produces two artifacts:

1. **Jupyter notebook** (primary): `notebooks/3.3-construct-data.ipynb` — contains all feature engineering code, feature statistics, inline outputs, and markdown narrative. This is the working artifact where features are developed and validated.
2. **Summary document**: `docs/crisp-dm/3-data-preparation/3.3-construct-data.md` — a structured summary of the feature engineering report extracted from the notebook. This is the CRISP-DM documentation artifact.

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/3.3-construct-data.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/3-data-preparation/3.3-construct-data.md` (the summary document)
- If either exists, present what's found and ask: *"A feature engineering [notebook/report/both] already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines target variable, prediction horizon, and output granularity.
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — it contains feature hypotheses and modeling implications from EDA.
- Read `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
  - If it exists, use it — it defines which fields are available and their roles.
- Read `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
  - If it exists, use it — it defines the cleaned data state and any indicator variables already created.
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — data dictionary helps understand field semantics.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **Feature ideas** — Use these as starting points for the feature engineering plan
- **Target variable** — Use this to guide feature construction around the prediction target
- **Feature config file** — Read and use as the feature engineering specification
- **No input provided** — Use exploration findings (2.3) and data mining goals (1.3) to propose features

Read ALL provided sources before proceeding.

### Step 3: Design Feature Engineering Plan

Based on the exploration findings and data mining goals, propose features in these categories:

**Temporal features (critical for time series forecasting):**
- Calendar features: day of week, week of year, month, quarter, holiday flags, promotion periods
- Lag features: target values at t-1, t-7, t-14, t-28 (same day last week, 2 weeks, 4 weeks)
- Rolling statistics: moving averages, moving medians, rolling std over 7/14/28-day windows
- Trend features: differences, growth rates, year-over-year changes
- Seasonal decomposition: extracted trend, seasonal, and residual components

**Aggregation features:**
- Cross-sectional aggregates: store-level averages, section-level totals, chain-wide patterns
- Hierarchical features: store's share of total, deviation from chain average

**Domain-specific features:**
- Retail calendar effects (Easter, Christmas, Belgian holidays, promotion weeks)
- Store characteristics (size, type, region, opening date)
- Section-specific patterns (food vs. non-food seasonality)

**Interaction features:**
- Store x Day-of-week patterns
- Section x Season patterns
- Meaningful interactions suggested by domain expertise

**Important constraints:**
- No features that use future information (data leakage)
- Lag and rolling features must respect the prediction horizon (3-6 weeks ahead)
- Features must be computable at prediction time with available data
- All features must be documented (name, formula, source, rationale) per project conventions

### Step 4: Present Feature Plan and Ask for Confirmation

Present the proposed features organized by category:

> **Proposed Features:**
>
> | # | Feature Name | Category | Source Fields | Formula / Logic | Rationale | Leakage Risk |
> |---|-------------|----------|---------------|----------------|-----------|-------------|
> | 1 | [name] | Temporal / Aggregate / Domain / Interaction | [fields] | [formula] | [why useful] | None / Low / Check |
>
> **Generated Records (if any):**
> - [description of any record generation, e.g., "aggregate daily records to weekly"]
>
> **Transformations:**
> - [description of any value transformations on existing fields]

Ask the user to:
1. **Confirm, adjust, or add** features
2. **Flag domain-specific features** that need expert validation
3. **Confirm the prediction horizon** to validate no leakage in lag features

Wait for the user's response before continuing.

### Step 5: Generate Feature Engineering Code

After the plan is confirmed, generate reproducible feature engineering code:

```python
# Generate feature engineering pipeline code
# - Each feature is a function with docstring (name, formula, source, rationale)
# - Lag/rolling features respect the prediction horizon
# - Temporal features use the correct calendar (Belgian holidays)
# - All transformations are fit on training data only
# - Feature pipeline is reusable for inference
```

If data files are accessible, offer to run the code and report feature statistics. If not, generate the code as a script.

### Step 6: Clarification Round (if needed)

If the user's response still has gaps:
- Ask a focused follow-up
- Maximum 2 clarification rounds — mark remaining as "TBD"

### Step 7: Create the Notebook and Generate the Output Document

First create the Jupyter notebook at `notebooks/3.3-construct-data.ipynb` using the `NotebookEdit` tool. The notebook is the primary artifact — all feature engineering code happens here.

**Notebook structure:**
- **Setup & Data Loading** — imports, load cleaned data from 3.2
- **Feature Engineering Plan** — markdown summary of proposed features
- **Temporal Features** — lag features, rolling statistics, calendar features
- **Aggregation Features** — cross-sectional aggregates, hierarchical features
- **Domain-Specific Features** — retail calendar effects, store characteristics
- **Interaction Features** — meaningful feature interactions
- **Value Transformations** — scaling, encoding, binning
- **Data Leakage Validation** — verify no future information in features
- **Feature Statistics** — summary statistics for all constructed features

Use the `NotebookEdit` tool to create and populate the notebook cell by cell. Run code cells to generate outputs inline.

Then create the summary document.

```bash
mkdir -p docs/crisp-dm/3-data-preparation
```

Write the file `docs/crisp-dm/3-data-preparation/3.3-construct-data.md` using this template:

```markdown
# 3.3 Data Construction Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 3. Data Preparation
> **Status:** Draft | Review | Approved

---

## Construction Overview

- **Input data:** [reference to 3.2 cleaned data — datasets, row/field counts]
- **Prediction horizon:** [from 1.3 — e.g., 3-6 weeks ahead]
- **Target variable:** [from 1.3]
- **Output granularity:** [from 1.3 — e.g., per store, per day, per section]
- **Features constructed:** [total count by category]

---

## Feature Catalog

### Temporal Features

| # | Feature Name | Formula / Logic | Source Fields | Window | Leakage Safe | Rationale |
|---|-------------|----------------|---------------|--------|-------------|-----------|
| 1 | [name] | [formula] | [fields] | [window if applicable] | Yes / Check | [reason] |

### Aggregation Features

| # | Feature Name | Formula / Logic | Source Fields | Aggregation Level | Rationale |
|---|-------------|----------------|---------------|-------------------|-----------|
| 1 | [name] | [formula] | [fields] | [store/section/chain] | [reason] |

### Domain-Specific Features

| # | Feature Name | Formula / Logic | Source Fields | Domain Rule | Rationale |
|---|-------------|----------------|---------------|-------------|-----------|
| 1 | [name] | [formula] | [fields] | [business rule or calendar] | [reason] |

### Interaction Features

| # | Feature Name | Formula / Logic | Source Fields | Rationale |
|---|-------------|----------------|---------------|-----------|
| 1 | [name] | [formula] | [fields] | [reason] |

---

## Generated Records

| # | Operation | Method | Input Records | Output Records | Rationale |
|---|-----------|--------|--------------|----------------|-----------|
| 1 | [e.g., weekly aggregation] | [method] | [count] | [count] | [reason] |

---

## Value Transformations

| # | Field | Transformation | Method | Parameters | Fit On | Rationale |
|---|-------|---------------|--------|-----------|--------|-----------|
| 1 | [field] | Scaling / Encoding / Binning / Log | [method] | [params] | Training set only | [reason] |

---

## Data Leakage Assessment

| # | Feature | Risk | Assessment | Mitigation |
|---|---------|------|-----------|------------|
| 1 | [feature] | [how it could leak] | Safe / Mitigated / Excluded | [action taken] |

**Prediction horizon validation:** All lag and rolling features use a minimum lag of [N] days, which exceeds the maximum prediction horizon of [M] weeks ([M*7] days). No feature uses information that would be unavailable at prediction time.

---

## Feature Statistics

| Feature | Non-Null | Mean | Std | Min | Median | Max | Unique | Dtype |
|---------|----------|------|-----|-----|--------|-----|--------|-------|
| [name] | [count] | [mean] | [std] | [min] | [median] | [max] | [unique] | [type] |

---

## Construction Code

### Pipeline Location
- **Script:** `src/features/build_features.py` (or notebook reference)
- **Dependencies:** [libraries]
- **Usage:** `python src/features/build_features.py --input [path] --output [path]`

### Reproducibility Notes
- All transformations fitted on training data only
- Feature pipeline is serializable for inference reuse
- Belgian holiday calendar sourced from [library/source]
- Random seeds documented where applicable

---

## To Be Clarified

[List any feature decisions that could not be finalized. Remove this section if everything is complete.]

---

## Source Documents

- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- 3.1 Data Selection: `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- 3.2 Data Cleaning: `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 8: Summary and Next Steps

After writing both artifacts, present a summary:

> **Data Construction complete.** Two artifacts created:
> - **Notebook:** `notebooks/3.3-construct-data.ipynb` — full feature engineering code with inline outputs
> - **Summary:** `docs/crisp-dm/3-data-preparation/3.3-construct-data.md` — structured report
>
> **Summary:**
> - [N] features constructed: [N] temporal, [N] aggregation, [N] domain, [N] interaction
> - [N] value transformations applied
> - [N] generated record operations
> - [N] data leakage risks assessed — all mitigated
> - Total features in modeling dataset: [count]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/integrate-data` to merge the constructed features with other data sources into a unified modeling dataset (Task 3.4).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 3.3 artifact link.

## Quality Checks

Before finalizing, verify:
- [ ] Jupyter notebook exists at `notebooks/3.3-construct-data.ipynb` with all feature engineering code and inline outputs
- [ ] Notebook cells are executed and outputs are saved (results render when opened)
- [ ] Every feature has a documented name, formula, source fields, and rationale
- [ ] No feature uses future information (data leakage check passed)
- [ ] Lag features respect the prediction horizon (minimum lag >= max forecast horizon)
- [ ] All transformations are fit on training data only
- [ ] Feature pipeline is reproducible and reusable for inference
- [ ] Domain-specific features use correct calendars and business rules
- [ ] Feature statistics are reported (non-null counts, distributions)
- [ ] Features connect to data mining goals (1.3) or exploration hypotheses (2.3)
- [ ] No PII is used as a feature
- [ ] Raw data is never modified — features are derived on copies
