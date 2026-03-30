---
name: clean-data
description: "CRISP-DM 3.2 — Clean Data. Raises data quality to the level required by the selected analysis techniques. Handles missing values, outliers, noise, encoding errors, and type corrections. Documents every cleaning decision with rationale and impact. Produces a structured data cleaning report in docs/crisp-dm/3-data-preparation/."
argument-hint: "<path to dataset or specific quality issues to address>"
---

# /clean-data — CRISP-DM 3.2: Clean Data

> **Phase:** 3. Data Preparation | **Task:** 3.2 Clean Data
>
> *"Raise the data quality to the level required by the selected analysis techniques. This may involve selection of clean subsets of the data, insertion of suitable defaults, or more ambitious techniques such as estimation of missing data by modeling."*

## Purpose

This skill addresses all data quality issues identified in Phase 2 (task 2.4) and any new issues surfaced during data selection (task 3.1). It documents every cleaning operation, its rationale, and its impact on the data. It produces four outputs:

1. **Cleaning Plan** — prioritized list of quality issues to address, mapped to 2.4 findings
2. **Missing Value Treatment** — strategy per field (drop, impute, flag), with justification
3. **Outlier & Noise Treatment** — detection method, treatment decision, and impact
4. **Cleaning Log** — every operation applied, before/after statistics, code references

## Output Location

All artifacts are written to: `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
- If it exists, present its contents and ask: *"A data cleaning report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
  - If it exists, use it — it contains the quality issues to address. This is the primary input.
  - If it does not exist, warn: *"No data quality report found (task 2.4). Without it, I'll need to assess quality issues from scratch. Run `/verify-data-quality` first, or provide specific quality issues to address."*
- Read `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
  - If it exists, use it — it defines which data is in scope for cleaning.
  - If it does not exist, warn: *"No data selection report found (task 3.1). I'll clean all available data, but it's better to select first. Proceed anyway?"*
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — data dictionary helps interpret field semantics for cleaning decisions.
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — modeling technique requirements influence cleaning strategy.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** — Read/profile the data to assess current quality state
- **Specific quality issues** — Focus cleaning on the described problems
- **No input provided** — Use the 2.4 quality report and 3.1 selection report to build a cleaning plan

Read ALL provided sources before proceeding.

### Step 3: Build Cleaning Plan

Based on the quality report (2.4) and data selection (3.1), build a prioritized cleaning plan:

**For each quality issue from 2.4:**
- Classify: Missing values / Outliers / Noise / Type errors / Encoding issues / Duplicates / Inconsistencies
- Assess severity: Critical (blocks modeling) / Major (degrades model quality) / Minor (cosmetic)
- Propose treatment with rationale
- Estimate impact (rows/fields affected)

**Cleaning strategy per category:**

**Missing values:**
- Per field: determine missingness pattern (MCAR / MAR / MNAR)
- Propose strategy: drop records, drop field, impute (mean/median/mode/model-based/forward-fill), or flag with indicator variable
- Never impute the target variable — drop incomplete target records
- Fit imputation on training data only — document this requirement

**Outliers:**
- Per field: define detection method (IQR, z-score, domain-specific thresholds)
- Propose treatment: cap/floor (winsorize), transform, flag, or remove
- Distinguish genuine extreme values from errors

**Noise & encoding errors:**
- Type mismatches (e.g., numeric stored as string)
- Encoding issues (character sets, date formats)
- Whitespace, case inconsistencies in categorical fields

**Duplicates:**
- Define deduplication key and strategy
- Document whether duplicates are exact or fuzzy

### Step 4: Present Cleaning Plan and Ask for Confirmation

Present the proposed plan in a structured summary organized by category and priority.

Ask the user to:
1. **Confirm or adjust** the proposed treatments
2. **Provide domain guidance** for ambiguous cases (e.g., "Is a delivery of 0 carts valid or an error?")
3. **Set thresholds** where defaults were assumed

Wait for the user's response before continuing.

### Step 5: Execute Cleaning (Code Generation)

After the plan is confirmed, generate reproducible cleaning code:

```python
# Generate cleaning pipeline code
# - Each step is a function with docstring explaining the rationale
# - Before/after statistics are logged
# - Cleaning is applied to a copy, never modifying raw data
# - Imputation parameters are fit on training data only
# - All operations are idempotent and reproducible
```

If data files are accessible, offer to run the cleaning code and report results. If not, generate the code as a script for the user to run.

### Step 6: Clarification Round (if needed)

If the user's response still has gaps:
- Ask a focused follow-up covering only the remaining decisions
- Maximum 2 clarification rounds — after that, mark remaining items as "TBD"

### Step 7: Generate the Output Document

Create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/3-data-preparation
```

Write the file `docs/crisp-dm/3-data-preparation/3.2-clean-data.md` using this template:

```markdown
# 3.2 Data Cleaning Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 3. Data Preparation
> **Status:** Draft | Review | Approved

---

## Cleaning Overview

- **Input data:** [reference to 3.1 selected data — datasets, row/field counts]
- **Quality issues addressed:** [count from 2.4, plus any new issues found]
- **Cleaning approach:** [conservative / aggressive / domain-guided]
- **Key principle:** Raw data is immutable — all cleaning applied to copies; imputation fitted on training data only

---

## Cleaning Plan

| # | Issue (from 2.4) | Category | Severity | Fields Affected | Records Affected | Treatment | Rationale |
|---|-----------------|----------|----------|-----------------|-----------------|-----------|-----------|
| 1 | [issue description] | Missing / Outlier / Noise / Duplicate / Inconsistency | Critical / Major / Minor | [fields] | [count or %] | [treatment] | [why this treatment] |

---

## Missing Value Treatment

### Summary
| Field | Missing Count | Missing % | Pattern | Treatment | Rationale |
|-------|--------------|-----------|---------|-----------|-----------|
| [field] | [count] | [%] | MCAR / MAR / MNAR | Drop / Impute (method) / Flag | [reason] |

### Imputation Details
| Field | Method | Parameters | Fit On | Notes |
|-------|--------|-----------|--------|-------|
| [field] | [mean/median/mode/model/ffill] | [parameters] | Training set only | [notes] |

### Missing Value Indicator Variables
| Original Field | Indicator Field | Purpose |
|---------------|----------------|---------|
| [field] | [field]_missing | Captures missingness signal for modeling |

---

## Outlier & Noise Treatment

### Outlier Detection
| Field | Method | Threshold | Outliers Found | Treatment | Rationale |
|-------|--------|-----------|---------------|-----------|-----------|
| [field] | IQR / Z-score / Domain | [threshold] | [count] | Cap / Remove / Keep / Flag | [reason] |

### Noise & Encoding Fixes
| # | Issue | Fields | Fix Applied | Records Affected |
|---|-------|--------|------------|-----------------|
| 1 | [description] | [fields] | [fix] | [count] |

---

## Duplicate Treatment

- **Deduplication key:** [fields used to identify duplicates]
- **Duplicates found:** [count] ([%] of total)
- **Strategy:** [keep first / keep last / aggregate / domain rule]
- **Records removed:** [count]

---

## Cleaning Impact

### Before vs. After

| Metric | Before Cleaning | After Cleaning | Change |
|--------|----------------|----------------|--------|
| Total records | [count] | [count] | [delta] |
| Total fields | [count] | [count] | [delta] |
| Records with any missing | [count] ([%]) | [count] ([%]) | [delta] |
| Total missing values | [count] | [count] | [delta] |
| Duplicate records | [count] | [count] | [delta] |

### Target Variable Impact
- **Records with missing target (dropped):** [count] ([%])
- **Target distribution before cleaning:** [summary stats]
- **Target distribution after cleaning:** [summary stats]
- **Assessment:** [whether cleaning significantly altered the target distribution]

---

## Cleaning Code

### Pipeline Location
- **Script:** `src/data/clean.py` (or notebook reference)
- **Dependencies:** [libraries]
- **Usage:** `python src/data/clean.py --input [path] --output [path]`

### Reproducibility Notes
- All random seeds documented
- Imputation parameters saved to [location] for inference-time reuse
- Cleaning is idempotent — running twice produces the same result
- Raw data is never modified

---

## To Be Clarified

[List any cleaning decisions that could not be finalized. Remove this section if everything is complete.]

---

## Source Documents

- 2.4 Data Quality Report: `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
- 3.1 Data Selection: `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- 2.2 Data Description: `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary:

> **Data Cleaning Report created** at `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
>
> **Summary:**
> - [N] quality issues addressed out of [M] from 2.4
> - [N] missing value treatments applied
> - [N] outlier treatments applied
> - [N] records removed ([%] of selected data)
> - [N] new indicator variables created
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/construct-data` to engineer features, derive new attributes, and generate records for modeling (Task 3.3).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 3.2 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Every quality issue from 2.4 is addressed or explicitly deferred with rationale
- [ ] Missing value treatment is documented per field (not just globally)
- [ ] Imputation is fit on training data only — this is explicitly stated
- [ ] Target variable records are dropped (never imputed) when target is missing
- [ ] Outlier detection methods and thresholds are explicit and reproducible
- [ ] Before/after statistics demonstrate the impact of cleaning
- [ ] Cleaning code is reproducible and idempotent
- [ ] Raw data is never modified — cleaning applies to copies
- [ ] No PII is included in the document
- [ ] Data leakage is not introduced through cleaning (e.g., imputing with global statistics including test data)
