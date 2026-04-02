---
name: format-data
description: "CRISP-DM 3.5 — Format Data. Applies final formatting transformations to the integrated dataset for compatibility with modeling tools. Handles type casting, column ordering, train/validation/test splitting, and output serialization. Produces a structured data formatting report in docs/crisp-dm/3-data-preparation/."
argument-hint: "<target format, modeling tool, or path to dataset>"
---

# /format-data — CRISP-DM 3.5: Format Data

> **Phase:** 3. Data Preparation | **Task:** 3.5 Format Data
>
> *"Formatting transformations refer to primarily syntactic modifications made to the data that do not change its meaning, but might be required by the modeling tool."*

## Purpose

This skill applies final formatting transformations to the integrated dataset (3.4) so it is ready to be consumed by the modeling pipeline. It also creates the train/validation/test splits. It produces four outputs:

1. **Formatting Transformations** — type casts, column ordering, renaming, and encoding for the modeling tool
2. **Train/Validation/Test Split** — splitting strategy, date boundaries, and partition statistics
3. **Output Dataset Specification** — final schema, file format, storage location, and loading instructions
4. **Dataset Card** — summary metadata for the modeling-ready dataset

## Output Location

This skill produces two artifacts:

1. **Jupyter notebook** (primary): `notebooks/3.5-format-data.ipynb` — contains all formatting code, train/validation/test splitting, type casting, inline outputs, and markdown narrative. This is the working artifact where formatting operations are developed and validated.
2. **Summary document**: `docs/crisp-dm/3-data-preparation/3.5-format-data.md` — a structured summary of the data formatting report extracted from the notebook. This is the CRISP-DM documentation artifact.

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/3.5-format-data.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/3-data-preparation/3.5-format-data.md` (the summary document)
- If either exists, present what's found and ask: *"A data formatting [notebook/report/both] already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
  - If it exists, use it — it defines the integrated dataset to format.
  - If it does not exist, warn: *"No data integration report found (task 3.4). Without it, I need to know which dataset to format. Provide a file path or run `/integrate-data` first."*
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines evaluation methodology and splitting strategy.
- Read `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
  - If it exists, use it — it may specify modeling tools and technique requirements.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **Target format** — Use to determine output requirements (e.g., "Parquet for LightGBM")
- **Modeling tool** — Use to determine format constraints
- **File path** — Read/profile the dataset to assess current format
- **No input provided** — Use the Phase 3 documents and project plan to determine formatting needs

Read ALL provided sources before proceeding.

### Step 3: Design Formatting Plan

Based on the integrated dataset and modeling requirements, plan the formatting:

**Type casting:**
- Categorical fields: encode as appropriate type (category dtype, integer codes, one-hot)
- Numeric fields: ensure correct precision (float32 vs float64)
- Date fields: standardize format, extract or drop as needed
- Boolean fields: ensure consistent encoding (0/1 vs True/False)

**Column ordering and naming:**
- Target variable first or last (per modeling tool convention)
- Group features by type (temporal, aggregation, domain, interaction)
- Consistent naming convention (snake_case, no special characters)
- Drop any columns not needed for modeling (IDs used only for joins, intermediate fields)

**Train/Validation/Test split (critical for time series):**
- For time series: temporal split (not random!) respecting the prediction horizon
- Training set: earliest data up to cutoff date
- Validation set: data between training cutoff and test cutoff
- Test set: most recent data (held out, mimics production)
- Gap between sets: at least equal to the prediction horizon to prevent leakage
- Document the exact date boundaries
- Report class balance / target distribution in each split

**Output format:**
- File format: Parquet (preferred for tabular), CSV (if needed), or tool-specific format
- Compression: snappy (Parquet default)
- Storage location: `data/processed/` or project convention
- Version control: DVC tracking

### Step 4: Present Formatting Plan and Ask for Confirmation

Present the proposed plan:

> **Formatting Plan:**
>
> **Type Changes:**
> | Field | Current Type | Target Type | Reason |
> |-------|-------------|-------------|--------|
>
> **Split Strategy:**
> | Partition | Date Range | Records | % of Total | Target Mean |
> |-----------|-----------|---------|-----------|------------|
> | Train | [start] to [cutoff1] | [count] | [%] | [mean] |
> | Validation | [cutoff1 + gap] to [cutoff2] | [count] | [%] | [mean] |
> | Test | [cutoff2 + gap] to [end] | [count] | [%] | [mean] |
>
> **Output Format:** [format] at [location]

Ask the user to confirm or adjust.

Wait for the user's response before continuing.

### Step 5: Execute Formatting (Code Generation)

After the plan is confirmed, generate reproducible formatting code:

```python
# Generate formatting pipeline code
# - Type casting applied consistently
# - Temporal split with explicit date boundaries
# - Gap between splits >= prediction horizon
# - Split statistics logged
# - Output saved in specified format
# - DVC tracking configured
```

If data files are accessible, offer to run the code and report results. If not, generate the code as a script.

### Step 6: Clarification Round (if needed)

If the user's response still has gaps:
- Ask a focused follow-up
- Maximum 2 clarification rounds — mark remaining as "TBD"

### Step 7: Create the Notebook and Generate the Output Document

First create the Jupyter notebook at `notebooks/3.5-format-data.ipynb` using the `NotebookEdit` tool. The notebook is the primary artifact — all formatting code happens here.

**Notebook structure:**
- **Setup & Data Loading** — imports, load integrated data from 3.4
- **Type Casting** — code cells for type conversions with rationale
- **Column Operations** — renaming, reordering, dropping intermediate columns
- **Encoding** — categorical encoding implementations
- **Train/Validation/Test Split** — temporal split implementation with distribution checks
- **Split Statistics** — target distribution per split, distribution shift analysis
- **Output Serialization** — save formatted datasets to specified format
- **Dataset Card** — summary metadata for the modeling-ready dataset

Use the `NotebookEdit` tool to create and populate the notebook cell by cell. Run code cells to generate outputs inline.

Then create the summary document.

```bash
mkdir -p docs/crisp-dm/3-data-preparation
```

Write the file `docs/crisp-dm/3-data-preparation/3.5-format-data.md` using this template:

```markdown
# 3.5 Data Formatting Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 3. Data Preparation
> **Status:** Draft | Review | Approved

---

## Formatting Overview

- **Input dataset:** [reference to 3.4 integrated dataset]
- **Target modeling tool(s):** [tool(s) and version(s)]
- **Output format:** [Parquet / CSV / other]
- **Split strategy:** [temporal / stratified / custom]

---

## Formatting Transformations

### Type Casting

| # | Field | Original Type | Target Type | Method | Rationale |
|---|-------|--------------|-------------|--------|-----------|
| 1 | [field] | [type] | [type] | [cast / encode / parse] | [reason] |

### Column Operations

| # | Operation | Fields | Details |
|---|-----------|--------|---------|
| 1 | Rename | [fields] | [old -> new] |
| 2 | Reorder | [all] | [ordering logic] |
| 3 | Drop | [fields] | [reason — e.g., join-only ID, intermediate field] |

### Encoding

| # | Field | Original Values | Encoding | Method | Mapping |
|---|-------|----------------|----------|--------|---------|
| 1 | [field] | [values] | Integer / One-Hot / Ordinal | [method] | [mapping reference] |

---

## Train / Validation / Test Split

### Split Strategy

- **Method:** Temporal split (no random shuffling — time series data)
- **Prediction horizon:** [N] weeks ([N*7] days)
- **Gap between partitions:** [N] days (>= prediction horizon to prevent leakage)

### Split Boundaries

| Partition | Start Date | End Date | Gap After | Records | % of Total |
|-----------|-----------|----------|-----------|---------|-----------|
| Train | [date] | [date] | [N] days | [count] | [%] |
| Validation | [date] | [date] | [N] days | [count] | [%] |
| Test | [date] | [date] | — | [count] | [%] |

### Split Statistics

| Metric | Train | Validation | Test | Full Dataset |
|--------|-------|-----------|------|-------------|
| Records | [count] | [count] | [count] | [count] |
| Date range | [range] | [range] | [range] | [range] |
| Target mean | [value] | [value] | [value] | [value] |
| Target std | [value] | [value] | [value] | [value] |
| Target min | [value] | [value] | [value] | [value] |
| Target max | [value] | [value] | [value] | [value] |
| Stores | [count] | [count] | [count] | [count] |

### Distribution Shift Check

[Brief analysis of whether the target distribution shifts significantly across splits. Flag any concerns for modeling.]

---

## Output Dataset Specification

### Final Schema

| # | Field | Type | Role | Non-Null | Description |
|---|-------|------|------|----------|-------------|
| 1 | [field] | [type] | Target / Feature / ID | [count] | [brief description] |

### File Locations

| Partition | File | Format | Size | Rows | Columns |
|-----------|------|--------|------|------|---------|
| Train | `data/processed/train.[ext]` | [format] | [size] | [rows] | [cols] |
| Validation | `data/processed/val.[ext]` | [format] | [size] | [rows] | [cols] |
| Test | `data/processed/test.[ext]` | [format] | [size] | [rows] | [cols] |

### Loading Instructions

```python
import pandas as pd

train = pd.read_parquet("data/processed/train.parquet")
val = pd.read_parquet("data/processed/val.parquet")
test = pd.read_parquet("data/processed/test.parquet")

X_train, y_train = train.drop(columns=["[target]"]), train["[target]"]
X_val, y_val = val.drop(columns=["[target]"]), val["[target]"]
X_test, y_test = test.drop(columns=["[target]"]), test["[target]"]
```

### Version Control

- **DVC tracked:** [Yes / No — if Yes, provide .dvc file locations]
- **Data version:** [hash or tag]
- **Code version:** [git commit hash that produced this dataset]

---

## Dataset Card

| Property | Value |
|----------|-------|
| **Name** | [project]-modeling-dataset-v[version] |
| **Created** | [date] |
| **Created by** | [name] |
| **Source data** | [references to 2.1 datasets] |
| **Preparation pipeline** | 3.1 Select → 3.2 Clean → 3.3 Construct → 3.4 Integrate → 3.5 Format |
| **Records** | [total] (Train: [N], Val: [N], Test: [N]) |
| **Features** | [count] |
| **Target** | [name] — [description] |
| **Granularity** | [e.g., store x day x section] |
| **Date range** | [start] to [end] |
| **Known limitations** | [list any known data limitations relevant to modeling] |

---

## To Be Clarified

[List any formatting decisions that could not be finalized. Remove this section if everything is complete.]

---

## Source Documents

- 3.4 Data Integration: `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 1.4 Project Plan: `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Data Scientist | | | Pending |
| Data Engineer | | | Pending |
```

### Step 8: Summary and Next Steps

After writing both artifacts, present a summary:

> **Data Formatting complete.** Two artifacts created:
> - **Notebook:** `notebooks/3.5-format-data.ipynb` — full formatting code with inline outputs
> - **Summary:** `docs/crisp-dm/3-data-preparation/3.5-format-data.md` — structured report
>
> **Summary:**
> - [N] type casts, [N] renames, [N] columns dropped
> - Split: Train ([N] records, [dates]), Validation ([N] records, [dates]), Test ([N] records, [dates])
> - Gap between splits: [N] days (prediction horizon: [M] weeks)
> - Output: [format] files at `data/processed/`
> - DVC tracked: [Yes/No]
> - [N] items still to be clarified (if any)
>
> **Phase 3 complete!** The modeling-ready dataset is prepared.
>
> **Next step in CRISP-DM:** Run `/select-modeling-techniques` to choose candidate modeling approaches (Task 4.1, Phase 4: Modeling).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md`:
- Mark "Data Preparation" as "Complete"
- Add the 3.5 artifact link
- Mark "Modeling" as "Not Started" (if not already)

## Quality Checks

Before finalizing, verify:
- [ ] Jupyter notebook exists at `notebooks/3.5-format-data.ipynb` with all formatting code and inline outputs
- [ ] Notebook cells are executed and outputs are saved (results render when opened)
- [ ] All type casts are documented with rationale
- [ ] Train/validation/test split uses temporal ordering (not random) for time series
- [ ] Gap between splits is >= prediction horizon (no data leakage)
- [ ] Target distribution is reported per split (check for distribution shift)
- [ ] Output files are in the specified format at the documented locations
- [ ] Loading instructions are complete and runnable
- [ ] Dataset card summarizes the full preparation pipeline
- [ ] Data is version-controlled (DVC) or a plan is noted
- [ ] No PII in the final dataset or documentation
- [ ] Formatting pipeline is reproducible (same input → same output)
