---
name: describe-data
description: "CRISP-DM 2.2 — Describe Data. Examines gross properties of acquired data: volume, field counts, types, distributions, and surface-level quality. Produces a structured data description report with data dictionary in docs/crisp-dm/2-data-understanding/."
argument-hint: "<path to data file or directory, or dataset name>"
---

# /describe-data — CRISP-DM 2.2: Describe Data

> **Phase:** 2. Data Understanding | **Task:** 2.2 Describe Data
>
> *"Examine the 'gross' or 'surface' properties of the acquired data and report on the results. This includes the volume of the data (e.g., number of records, number of fields), the identities of the fields and any other surface-level characteristics discovered."*

## Purpose

This skill profiles each acquired dataset to produce a comprehensive data dictionary and surface-level statistics. It runs actual profiling code on the data when available, cross-references with the data collection report (2.1), and documents everything needed for downstream exploration and preparation. It produces three outputs:

1. **Data Dictionary** — field names, types, descriptions, units, allowed values, business meaning
2. **Surface Statistics** — record counts, value distributions, missing rates, unique counts
3. **Initial Observations** — anything surprising, noteworthy, or potentially problematic

## Output Location

This skill produces two artifacts:

1. **Jupyter notebook** (primary): `notebooks/2.2-data-description.ipynb` — contains all data profiling code, inline outputs, and markdown narrative. This is the working artifact where data description analysis happens.
2. **Summary document**: `docs/crisp-dm/2-data-understanding/2.2-data-description.md` — a structured summary of the data description report extracted from the notebook. This is the CRISP-DM documentation artifact.

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if output artifacts already exist:
- Check for `notebooks/2.2-data-description.ipynb` (the primary notebook)
- Check for `docs/crisp-dm/2-data-understanding/2.2-data-description.md` (the summary document)
- If either exists, present what's found and ask: *"A data description [notebook/report/both] already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If neither exists, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
  - If it exists, use it — it lists the acquired datasets, their locations, and loading instructions.
  - If it does not exist, warn the user: *"No data collection report found (task 2.1). It's recommended to complete 2.1 first so I know which datasets to profile. Proceed anyway?"*
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines the target variable and expected features, which helps contextualize the data dictionary.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path or directory** (e.g., `data/raw/transport_history.csv`) — Load and profile the file(s)
- **Dataset name** — Look up the dataset in the 2.1 data collection report for location and loading instructions
- **No input provided** — If the 2.1 document exists, extract the dataset list and ask: *"Based on the data collection report, these datasets are available: [list]. Which one(s) should I profile? Or should I profile all of them?"*

### Step 3: Run Profiling Code

For each dataset, generate and run profiling code:

```python
import pandas as pd

df = pd.read_csv("[path]")  # or appropriate loader

# Basic info
print(f"Shape: {df.shape}")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.1f} MB")
print(f"Duplicated rows: {df.duplicated().sum()}")

# Column-level profiling
print(df.dtypes)
print(df.describe(include='all'))
print(df.isnull().sum())
print(df.nunique())

# For each column: value_counts (top N), min, max, mean, std
for col in df.columns:
    print(f"\n--- {col} ---")
    print(f"  dtype: {df[col].dtype}")
    print(f"  nulls: {df[col].isnull().sum()} ({df[col].isnull().mean()*100:.1f}%)")
    print(f"  unique: {df[col].nunique()}")
    if df[col].dtype in ['object', 'category']:
        print(f"  top values: {df[col].value_counts().head(5).to_dict()}")
    else:
        print(f"  min: {df[col].min()}, max: {df[col].max()}")
        print(f"  mean: {df[col].mean():.2f}, std: {df[col].std():.2f}")

# Date range (if temporal)
date_cols = df.select_dtypes(include=['datetime64']).columns
for col in date_cols:
    print(f"{col}: {df[col].min()} to {df[col].max()}")
```

If the data is not directly accessible, document what is known from the 2.1 report and user description, and mark profiling results as "Pending — awaiting data access."

### Step 4: Extract and Map Information

After profiling and reading source documents, map every piece of information to the required fields below:

**Section A — Data Dictionary (per dataset):**
- [ ] Field name
- [ ] Data type (as stored)
- [ ] Semantic type (identifier, date, categorical, numeric continuous, numeric discrete, boolean, text, etc.)
- [ ] Business description (what does this field mean in business terms?)
- [ ] Unit of measurement (if applicable)
- [ ] Allowed/expected values or range
- [ ] Role in modeling (target, feature, identifier, filter, not used)
- [ ] Source (which system/table it originates from)

**Section B — Surface Statistics (per dataset):**
- [ ] Total record count
- [ ] Total column count
- [ ] Memory footprint
- [ ] Duplicate row count
- [ ] Date range (for temporal data)
- [ ] Per-column: null count, null %, unique count, top values (categorical) or min/max/mean/std (numeric)

**Section C — Structural Observations:**
- [ ] File format and encoding
- [ ] Delimiter (for CSV)
- [ ] Join keys between datasets
- [ ] Hierarchical or nested structures
- [ ] Grain / granularity (what does one row represent?)

**Section D — Initial Observations:**
- [ ] Fields with unexpected data types (e.g., numeric stored as string)
- [ ] Fields with suspiciously high cardinality
- [ ] Fields with very high null rates (>50%)
- [ ] Constant or near-constant fields
- [ ] Potential identifier leakage (IDs that correlate with target)
- [ ] Anything that contradicts expectations from 1.2 or 1.3

### Step 5: Present Profiling Results and Ask About Gaps

Present the profiling results in a structured summary. For each field in the data dictionary, show:
- **Profiled:** the value from code output
- **Needs Business Input:** fields where the data type is clear but the business meaning is not

Then ask the user to:
1. **Confirm or correct** field descriptions and types
2. **Provide business descriptions** for fields where the meaning isn't obvious from the name
3. **Clarify** any observations that look anomalous

**Important rules for this step:**
- Ask about ALL missing descriptions in a single message
- Group questions by dataset, not by field
- Highlight any red flags (unexpected nulls, suspicious ranges, type mismatches)

Wait for the user's response before continuing.

### Step 6: Clarification Round (if needed)

If the user's response still has gaps or ambiguities:
- Ask a focused follow-up covering only the remaining gaps
- Maximum 2 clarification rounds — after that, mark remaining gaps as "TBD" in the document

### Step 7: Create the Notebook and Generate the Output Document

After gathering all information, first create the Jupyter notebook at `notebooks/2.2-data-description.ipynb` using the `NotebookEdit` tool. The notebook is the primary artifact — all profiling code and analysis happens here.

**Notebook structure:**
- **Setup & Data Loading** — imports, configuration, load data using instructions from 2.1
- **Dataset Overview** — shape, memory usage, duplicates for each dataset
- **Column-Level Profiling** — dtypes, nulls, unique counts, value distributions per column
- **Surface Statistics** — describe() for numeric and categorical fields
- **Structural Notes** — join keys, format details, grain identification
- **Initial Observations** — red flags, noteworthy patterns, contradictions with prior documents

Use the `NotebookEdit` tool to create and populate the notebook cell by cell. Alternate between markdown cells (for narrative) and code cells (for profiling). Run code cells to generate outputs inline.

Then create the summary document. Create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/2-data-understanding
```

Write the file `docs/crisp-dm/2-data-understanding/2.2-data-description.md` using this template:

```markdown
# 2.2 Data Description Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 2. Data Understanding
> **Status:** Draft | Review | Approved

---

## Dataset Overview

| # | Dataset | Records | Columns | Date Range | Size | Grain |
|---|---------|---------|---------|------------|------|-------|
| 1 | [name] | [rows] | [cols] | [start–end] | [size] | [what one row represents] |

---

## Data Dictionary

### Dataset 1: [dataset name]

**Grain:** [what one row represents]
**Source:** [origin system]
**Records:** [row count] | **Columns:** [column count] | **Duplicates:** [count]

| # | Field | Stored Type | Semantic Type | Description | Unit | Valid Range / Values | Null % | Unique | Modeling Role |
|---|-------|-------------|---------------|-------------|------|---------------------|--------|--------|---------------|
| 1 | [field] | [int64] | [Numeric Continuous] | [business description] | [unit] | [range or values] | [%] | [count] | [Target / Feature / ID / Filter / Unused] |

[Repeat for each dataset]

---

## Surface Statistics

### Dataset 1: [dataset name]

#### Numeric Fields
| Field | Count | Mean | Std | Min | 25% | 50% | 75% | Max | Null % |
|-------|-------|------|-----|-----|-----|-----|-----|-----|--------|
| [field] | [n] | [mean] | [std] | [min] | [q1] | [median] | [q3] | [max] | [%] |

#### Categorical Fields
| Field | Count | Unique | Top Value | Top Freq | Null % |
|-------|-------|--------|-----------|----------|--------|
| [field] | [n] | [unique] | [top] | [freq] | [%] |

#### Temporal Fields
| Field | Min Date | Max Date | Gaps | Null % |
|-------|----------|----------|------|--------|
| [field] | [min] | [max] | [any gaps?] | [%] |

[Repeat for each dataset]

---

## Structural Notes

### Join Keys
| Dataset A | Key Field(s) | Dataset B | Key Field(s) | Relationship |
|-----------|-------------|-----------|-------------|--------------|
| [dataset] | [field(s)] | [dataset] | [field(s)] | [1:1 / 1:N / M:N] |

### Format Details
| Dataset | Format | Encoding | Delimiter | Header Row | Notes |
|---------|--------|----------|-----------|------------|-------|
| [name] | [CSV/Parquet/etc.] | [UTF-8/etc.] | [comma/tab/etc.] | [Yes/No] | [notes] |

---

## Initial Observations

### Red Flags
| # | Dataset | Field(s) | Observation | Severity | Action Needed |
|---|---------|----------|-------------|----------|---------------|
| 1 | [dataset] | [field] | [what was observed] | [High/Medium/Low] | [what to investigate] |

### Noteworthy Patterns
- [observation 1]
- [observation 2]

### Contradictions with Prior Documents
- [any mismatches between profiled data and expectations from 1.2/1.3]

---

## To Be Clarified

[List any items that could not be determined from profiling or user input. Remove this section if everything is complete.]

---

## Source Documents

- [List the sources used]
- 2.1 Data Collection Report: `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
| Data Engineer | | | Pending |
```

### Step 8: Summary and Next Steps

After writing both artifacts, present a summary:

> **Data Description complete.** Two artifacts created:
> - **Notebook:** `notebooks/2.2-data-description.ipynb` — full profiling code with inline outputs
> - **Summary:** `docs/crisp-dm/2-data-understanding/2.2-data-description.md` — structured report
>
> **Summary:**
> - [N] datasets profiled with [total fields] total fields
> - Data dictionary complete for [N]/[M] fields ([remaining] need business descriptions)
> - [N] red flags identified requiring investigation
> - [N] join relationships documented
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/explore-data` to perform deeper exploratory analysis — distributions, correlations, temporal patterns, and subgroup comparisons (Task 2.3).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 2.2 artifact link.

## Quality Checks

Before finalizing, verify:
- [ ] Jupyter notebook exists at `notebooks/2.2-data-description.ipynb` with all profiling code and inline outputs
- [ ] Notebook cells are executed and outputs are saved (results render when opened)
- [ ] Every field in every dataset is documented in the data dictionary
- [ ] Every field has a business description (or is marked TBD)
- [ ] Every field has a modeling role assigned (target, feature, ID, filter, unused)
- [ ] Surface statistics are generated from actual data (not guessed)
- [ ] Join keys between datasets are documented and relationship types specified
- [ ] Red flags are flagged with severity and recommended action
- [ ] The grain of each dataset is explicitly stated (what does one row represent?)
- [ ] No PII or sensitive data values are included (use aggregated stats, not raw values)
- [ ] Document cross-references the 2.1 and 1.3 documents where applicable
