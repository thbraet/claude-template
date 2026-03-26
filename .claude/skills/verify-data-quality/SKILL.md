---
name: verify-data-quality
description: "CRISP-DM 2.4 — Verify Data Quality. Assesses completeness, correctness, consistency, and timeliness of acquired data. Produces a structured data quality report with severity ratings and recommendations in docs/crisp-dm/2-data-understanding/."
argument-hint: "<path to data file, dataset name, or specific quality concern>"
---

# /verify-data-quality — CRISP-DM 2.4: Verify Data Quality

> **Phase:** 2. Data Understanding | **Task:** 2.4 Verify Data Quality
>
> *"Examine the quality of the data, addressing questions such as: Is the data complete (does it cover all the cases required)? Is it correct, or does it contain errors and, if there are errors, how common are they? Are there missing values in the data? If so, how are they represented, where do they occur, and how common are they?"*

## Purpose

This skill performs a systematic data quality assessment across four dimensions: completeness, correctness, consistency, and timeliness. It runs actual validation code on the data, cross-references with prior CRISP-DM documents, and produces a quality scorecard with severity ratings and recommended actions. It produces five outputs:

1. **Completeness Assessment** — missing values, coverage gaps, missingness patterns
2. **Correctness Assessment** — range violations, type errors, business rule violations
3. **Consistency Assessment** — cross-field consistency, duplicates, referential integrity
4. **Timeliness Assessment** — data freshness, recording lag, temporal coverage gaps
5. **Quality Summary** — overall quality score, go/no-go recommendation, remediation plan

## Output Location

All artifacts are written to: `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
- If it exists, present its contents and ask: *"A data quality report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
  - If it exists, use it — it lists datasets and loading instructions.
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — it contains the data dictionary, expected types, and initial red flags.
  - If it does not exist, warn the user: *"No data description report found (task 2.2). It's recommended to complete 2.2 first so I have the data dictionary as a reference. Proceed anyway?"*
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — exploration findings may have flagged quality concerns worth verifying systematically.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — it contains data quality assumptions that should be validated.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** — Load and validate the specific file
- **Dataset name** — Look up in 2.1 for location and loading instructions
- **Specific quality concern** (e.g., "check for missing delivery dates") — Focus the assessment on that concern while still covering all dimensions
- **No input provided** — If the 2.1/2.2 documents exist, extract the dataset list and ask: *"Which dataset(s) should I assess for quality? Or should I assess all of them?"*

### Step 3: Run Quality Validation Code

For each dataset, generate and run validation code covering all four quality dimensions:

```python
import pandas as pd
import numpy as np

df = pd.read_csv("[path]")

# =====================
# COMPLETENESS
# =====================

# Missing values by column
missing = df.isnull().sum()
missing_pct = df.isnull().mean() * 100
missing_report = pd.DataFrame({
    'null_count': missing,
    'null_pct': missing_pct,
    'dtype': df.dtypes
}).sort_values('null_pct', ascending=False)
print("=== COMPLETENESS: Missing Values ===")
print(missing_report[missing_report['null_count'] > 0])

# Missing value patterns (are nulls random or correlated?)
# Check if certain rows have many missing fields
row_missing = df.isnull().sum(axis=1)
print(f"\nRows with any missing: {(row_missing > 0).sum()} ({(row_missing > 0).mean()*100:.1f}%)")
print(f"Rows with >50% missing: {(row_missing > len(df.columns)/2).sum()}")

# Coverage: date range completeness
# [Check for gaps in date coverage]

# =====================
# CORRECTNESS
# =====================

# Range checks for numeric fields
for col in df.select_dtypes(include='number').columns:
    print(f"\n{col}: min={df[col].min()}, max={df[col].max()}")
    # Flag negative values where they shouldn't exist
    # Flag values beyond expected range

# Type consistency checks
# [Check for mixed types in columns]

# Business rule checks
# [Custom checks based on domain — e.g., delivery_date >= order_date]

# =====================
# CONSISTENCY
# =====================

# Duplicate detection
dupes = df.duplicated()
print(f"\n=== CONSISTENCY: Duplicates ===")
print(f"Exact duplicates: {dupes.sum()}")

# Duplicate on key columns
# key_dupes = df.duplicated(subset=['store_id', 'date', 'section'])

# Cross-field consistency
# [Check logical relationships between fields]

# Referential integrity (if multiple datasets)
# [Check foreign keys match across tables]

# =====================
# TIMELINESS
# =====================

# Date coverage
# date_col = pd.to_datetime(df['date'])
# expected_dates = pd.date_range(date_col.min(), date_col.max(), freq='D')
# missing_dates = expected_dates.difference(date_col)
# print(f"\n=== TIMELINESS ===")
# print(f"Missing dates: {len(missing_dates)}")
```

### Step 4: Extract and Map Quality Issues

After running validation code and reading source documents, categorize every quality issue found:

**Section A — Completeness:**
- [ ] Per-field missing value counts and percentages
- [ ] Missingness patterns: MCAR (random), MAR (related to other fields), MNAR (related to the missing value itself)
- [ ] Record-level completeness (rows with many missing fields)
- [ ] Temporal coverage: gaps in date ranges
- [ ] Entity coverage: missing stores, sections, or other expected entities

**Section B — Correctness:**
- [ ] Out-of-range values (negative quantities, future dates, etc.)
- [ ] Type errors (numeric stored as string, dates as strings, etc.)
- [ ] Business rule violations (logical impossibilities)
- [ ] Encoding errors (garbled characters, wrong encoding)
- [ ] Precision issues (truncated decimals, rounding artifacts)

**Section C — Consistency:**
- [ ] Exact duplicate rows
- [ ] Key-based duplicates (same entity+date, different values)
- [ ] Cross-field inconsistencies (contradictory values)
- [ ] Cross-dataset inconsistencies (mismatched reference data)
- [ ] Naming inconsistencies (same entity with different names/codes)

**Section D — Timeliness:**
- [ ] Data freshness (how recent is the latest record?)
- [ ] Recording lag (delay between event and recording)
- [ ] Temporal gaps (missing days, weeks, or months)
- [ ] Timezone issues
- [ ] Retroactive corrections (records that change after initial recording)

### Step 5: Present Quality Findings and Ask for Input

Present the quality findings in a structured summary, organized by severity:

- **Critical** — blocks modeling; must be resolved before proceeding
- **Major** — significantly impacts data quality; should be resolved during data preparation
- **Minor** — cosmetic or low-impact; can be noted and handled if convenient

Then ask the user:
1. **Are any of these issues expected or known?** (e.g., "Yes, store X was closed for renovation")
2. **What are the business rules I should validate?** (domain-specific checks)
3. **Which issues should block progress to data preparation?**

Wait for the user's response before finalizing.

### Step 6: Clarification Round (if needed)

If the user's response reveals additional context or quality checks needed:
- Run additional validation code
- Maximum 2 clarification rounds — after that, finalize with what is known

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/2-data-understanding
```

Write the file `docs/crisp-dm/2-data-understanding/2.4-data-quality.md` using this template:

```markdown
# 2.4 Data Quality Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 2. Data Understanding
> **Status:** Draft | Review | Approved

---

## Quality Summary

### Overall Assessment

| Dataset | Completeness | Correctness | Consistency | Timeliness | Overall | Verdict |
|---------|-------------|-------------|-------------|------------|---------|---------|
| [name] | [score/5] | [score/5] | [score/5] | [score/5] | [avg] | [Go / Go with caveats / No-go] |

**Scoring Guide:** 5 = Excellent, 4 = Good, 3 = Acceptable, 2 = Poor, 1 = Critical

### Go/No-Go Recommendation
[Clear statement on whether the data quality is sufficient to proceed to Data Preparation (Phase 3). If "Go with caveats", list the caveats. If "No-go", list what must be fixed first.]

### Issue Summary
| Severity | Count | Blocking? |
|----------|-------|-----------|
| Critical | [n] | Yes |
| Major | [n] | No (but should fix in Phase 3) |
| Minor | [n] | No |

---

## Completeness

### Missing Values by Field

| # | Dataset | Field | Missing Count | Missing % | Pattern | Severity | Impact on Modeling |
|---|---------|-------|---------------|-----------|---------|----------|--------------------|
| 1 | [dataset] | [field] | [count] | [%] | [MCAR/MAR/MNAR] | [Critical/Major/Minor] | [how it affects the model] |

### Missingness Patterns
[Description of whether missing values are random or systematic. Include heatmap if helpful.]

### Coverage Gaps

#### Temporal Coverage
| Dataset | Expected Range | Actual Range | Missing Periods | Severity |
|---------|---------------|--------------|----------------|----------|
| [name] | [expected] | [actual] | [gaps] | [severity] |

#### Entity Coverage
| Dataset | Entity Type | Expected Count | Actual Count | Missing | Severity |
|---------|-------------|---------------|--------------|---------|----------|
| [name] | [e.g., stores] | [expected] | [actual] | [which are missing] | [severity] |

---

## Correctness

### Range Violations

| # | Dataset | Field | Rule | Violations | % | Examples | Severity | Recommended Action |
|---|---------|-------|------|------------|---|---------|----------|--------------------|
| 1 | [dataset] | [field] | [expected range] | [count] | [%] | [sample values] | [severity] | [action] |

### Business Rule Violations

| # | Rule | Description | Violations | % | Severity | Recommended Action |
|---|------|-------------|------------|---|----------|--------------------|
| 1 | [rule name] | [what should hold true] | [count] | [%] | [severity] | [action] |

### Type Errors

| # | Dataset | Field | Expected Type | Actual Issues | Count | Severity | Recommended Action |
|---|---------|-------|---------------|--------------|-------|----------|--------------------|
| 1 | [dataset] | [field] | [expected] | [what's wrong] | [count] | [severity] | [action] |

---

## Consistency

### Duplicates

| Dataset | Exact Duplicates | Key-Based Duplicates | Key Fields Used | Severity | Recommended Action |
|---------|-----------------|---------------------|-----------------|----------|--------------------|
| [name] | [count] | [count] | [fields] | [severity] | [action] |

### Cross-Field Inconsistencies

| # | Dataset | Fields | Rule | Violations | Severity | Recommended Action |
|---|---------|--------|------|------------|----------|--------------------|
| 1 | [dataset] | [field A, field B] | [logical relationship] | [count] | [severity] | [action] |

### Cross-Dataset Inconsistencies

| # | Dataset A | Dataset B | Join Key | Issue | Count | Severity | Recommended Action |
|---|-----------|-----------|----------|-------|-------|----------|--------------------|
| 1 | [dataset] | [dataset] | [key] | [mismatch description] | [count] | [severity] | [action] |

---

## Timeliness

### Data Freshness

| Dataset | Latest Record | Expected | Lag | Severity |
|---------|--------------|----------|-----|----------|
| [name] | [date] | [expected] | [days behind] | [severity] |

### Temporal Gaps

| Dataset | Gap Period | Duration | Affected Records | Possible Cause | Severity |
|---------|-----------|----------|-----------------|---------------|----------|
| [name] | [from–to] | [days] | [estimated] | [cause] | [severity] |

---

## Assumption Validation

[Cross-reference quality findings with assumptions from 1.2 Situation Assessment]

| # | Assumption (from 1.2) | Validated? | Evidence | Impact |
|---|----------------------|-----------|---------|--------|
| 1 | [assumption] | [Yes/No/Partially] | [what the data shows] | [impact if assumption is wrong] |

---

## Remediation Plan

### Critical Issues (Must Fix Before Phase 3)
| # | Issue | Dataset | Recommended Fix | Effort | Owner |
|---|-------|---------|----------------|--------|-------|
| 1 | [issue] | [dataset] | [how to fix] | [Low/Medium/High] | [who] |

### Major Issues (Fix During Phase 3 — Data Preparation)
| # | Issue | Dataset | Recommended Fix | Effort | Priority |
|---|-------|---------|----------------|--------|----------|
| 1 | [issue] | [dataset] | [how to fix] | [Low/Medium/High] | [1/2/3] |

### Minor Issues (Note and Monitor)
| # | Issue | Dataset | Notes |
|---|-------|---------|-------|
| 1 | [issue] | [dataset] | [context] |

---

## To Be Clarified

[List any items that need further investigation or domain expert input. Remove this section if everything is complete.]

---

## Source Documents

- [List the sources used]
- 2.1 Data Collection Report: `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- 2.2 Data Description Report: `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- 2.3 Data Exploration Report: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
| Data Engineer | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary:

> **Data Quality Report created** at `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
>
> **Summary:**
> - Overall quality verdict: [Go / Go with caveats / No-go]
> - [N] critical issues, [N] major issues, [N] minor issues
> - Completeness: [score/5] — [brief note]
> - Correctness: [score/5] — [brief note]
> - Consistency: [score/5] — [brief note]
> - Timeliness: [score/5] — [brief note]
> - [N] assumptions from 1.2 validated, [N] invalidated
> - [N] items still to be clarified (if any)
>
> **Phase 2 (Data Understanding) is now complete.** Next step in CRISP-DM: Begin **Phase 3 — Data Preparation** with data selection, cleaning, feature construction, and integration.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md`:
- Add the 2.4 artifact link
- Consider marking Phase 2 "Data Understanding" as "Complete" if all four documents (2.1–2.4) are in place

## Quality Checks

Before finalizing the document, verify:
- [ ] All four quality dimensions are assessed (completeness, correctness, consistency, timeliness)
- [ ] Every issue has a severity rating (Critical / Major / Minor)
- [ ] Every critical and major issue has a recommended remediation action
- [ ] The go/no-go recommendation is clearly stated with rationale
- [ ] Assumptions from 1.2 are cross-referenced and validated
- [ ] Missingness patterns are identified (MCAR/MAR/MNAR), not just counted
- [ ] Temporal coverage gaps are identified for time series data
- [ ] Duplicate detection covers both exact and key-based duplicates
- [ ] Business rule validation includes domain-specific checks
- [ ] Remediation plan distinguishes between "fix before Phase 3" and "fix during Phase 3"
- [ ] No PII or sensitive data values are included (use aggregated counts, not raw values)
- [ ] Document cross-references the 2.1, 2.2, 2.3, and 1.2 documents where applicable
