---
name: select-data
description: "CRISP-DM 3.1 — Select Data. Decides which datasets, tables, columns, and rows to include for analysis/modeling. Documents inclusion/exclusion rationale, relevance to data mining goals, and any data constraints. Produces a structured data selection report in docs/crisp-dm/3-data-preparation/."
argument-hint: "<path to data file, directory, or selection criteria>"
---

# /select-data — CRISP-DM 3.1: Select Data

> **Phase:** 3. Data Preparation | **Task:** 3.1 Select Data
>
> *"Decide on the data to be used for analysis. Criteria include relevance to the data mining goals, quality, and technical constraints such as limits on data volume or data types."*

## Purpose

This skill decides which datasets, fields, and records from the collected data (Phase 2) will be carried forward into the modeling dataset. It documents the rationale for every inclusion and exclusion decision. It produces three outputs:

1. **Dataset Selection** — which datasets from 2.1 are included/excluded, with reasons
2. **Field Selection** — which columns from each dataset are included/excluded, mapped to data mining goals
3. **Record Selection** — which rows are included/excluded (date ranges, store subsets, filters), with coverage analysis

## Output Location

All artifacts are written to: `docs/crisp-dm/3-data-preparation/3.1-select-data.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- If it exists, present its contents and ask: *"A data selection report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines target variable, features, granularity, and prediction horizon.
  - If it does not exist, warn: *"No data mining goals document found (task 1.3). Without it, I cannot verify which data supports the modeling objectives. Proceed anyway?"*
- Read `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
  - If it exists, use it — it lists all available datasets with their metadata.
  - If it does not exist, warn: *"No data collection report found (task 2.1). I need to know what data is available. Please provide file paths or run `/collect-initial-data` first."*
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — it provides data dictionaries and field-level detail.
- Read `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
  - If it exists, use it — it provides exploration findings, feature hypotheses, and modeling implications.
- Read `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`
  - If it exists, use it — it provides quality issues that may drive exclusion decisions.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path or directory** — List files and attempt to read/profile them
- **Selection criteria** — Use the criteria to guide selection decisions
- **No input provided** — Use the Phase 2 documents to propose a data selection plan and ask for confirmation

Read ALL provided sources before proceeding.

### Step 3: Analyze and Propose Selection

Based on the Phase 2 documents and any user input, analyze the available data and propose selections:

**Dataset-level analysis:**
- For each dataset from 2.1: Is it needed for the data mining goals from 1.3?
- Are there redundant datasets that overlap?
- Are there datasets with quality issues (from 2.4) severe enough to exclude?

**Field-level analysis:**
- For each field in each selected dataset: Does it serve as target, feature, identifier, or context?
- Flag fields with high missingness (from 2.4) or low variance (from 2.3)
- Flag fields that risk data leakage (encode the target or use future information)
- Flag fields that contain PII and must be excluded or pseudonymized

**Record-level analysis:**
- What date range should be included? (Consider data quality over time, regime changes, relevance)
- Should any stores, sections, or categories be excluded? (e.g., recently opened stores with insufficient history)
- What is the minimum record completeness threshold?
- Are there known anomalous periods to exclude (e.g., COVID lockdowns, system migrations)?

### Step 4: Present Selection Plan and Ask for Confirmation

Present the proposed selection in a structured summary:

> **Dataset Selection:**
> | Dataset | Decision | Reason | Data Mining Goal |
> |---------|----------|--------|-----------------|
> | [name] | Include / Exclude | [reason] | [goal from 1.3] |
>
> **Field Selection (per included dataset):**
> | Field | Decision | Role | Reason |
> |-------|----------|------|--------|
> | [name] | Include / Exclude / Transform | Target / Feature / ID / Context | [reason] |
>
> **Record Selection:**
> | Criterion | Value | Reason | Records Affected |
> |-----------|-------|--------|-----------------|
> | Date range | [start] to [end] | [reason] | [count or %] |
> | Store filter | [criteria] | [reason] | [count or %] |
>
> **Data Leakage Risks:**
> - [list any fields or patterns that could leak target information]
>
> **Coverage Analysis:**
> - Total records after selection: [count] ([%] of original)
> - Total fields after selection: [count] ([%] of original)
> - Date range: [start] to [end]

Ask the user to confirm or adjust the selection.

Wait for the user's response before continuing.

### Step 5: Clarification Round (if needed)

If the user's response raises new questions:
- Ask a focused follow-up covering only the remaining decisions
- Maximum 2 clarification rounds — after that, mark remaining decisions as "TBD" in the document

### Step 6: Generate the Output Document

Create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/3-data-preparation
```

Write the file `docs/crisp-dm/3-data-preparation/3.1-select-data.md` using this template:

```markdown
# 3.1 Data Selection Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 3. Data Preparation
> **Status:** Draft | Review | Approved

---

## Selection Overview

- **Purpose:** [what the selected data will be used for — reference data mining goals]
- **Selection approach:** [top-down from goals / bottom-up from available data / hybrid]
- **Key decisions:** [1-3 sentence summary of the most impactful selection choices]

---

## Dataset Selection

| # | Dataset | Source (from 2.1) | Decision | Rationale | Data Mining Goal (from 1.3) |
|---|---------|-------------------|----------|-----------|---------------------------|
| 1 | [name] | [source] | Include / Exclude | [reason] | [goal] |

### Excluded Datasets
[For each excluded dataset, explain why it was excluded and whether it might be reconsidered later.]

---

## Field Selection

### [Dataset 1 Name]

| # | Field | Data Type | Decision | Role | Rationale |
|---|-------|-----------|----------|------|-----------|
| 1 | [field] | [type] | Include / Exclude / Defer | Target / Feature / ID / Context / Excluded | [reason] |

**Summary:** [N] of [M] fields selected ([%])

[Repeat for each included dataset]

### Data Leakage Assessment

| # | Field / Pattern | Risk | Mitigation |
|---|----------------|------|------------|
| 1 | [field or pattern] | [how it could leak target information] | [exclusion / temporal guard / other] |

---

## Record Selection

### Inclusion Criteria

| # | Criterion | Value | Rationale | Records Affected |
|---|-----------|-------|-----------|-----------------|
| 1 | Date range | [start] to [end] | [reason] | [count or %] |
| 2 | Store filter | [criteria] | [reason] | [count or %] |
| 3 | Completeness threshold | [min fields non-null] | [reason] | [count or %] |

### Exclusion Criteria

| # | Criterion | Value | Rationale | Records Removed |
|---|-----------|-------|-----------|----------------|
| 1 | [anomalous periods] | [dates/conditions] | [reason] | [count or %] |

### Coverage Analysis

- **Total records before selection:** [count]
- **Total records after selection:** [count] ([%] retained)
- **Total fields after selection:** [count] ([%] retained)
- **Date range:** [start] to [end]
- **Stores covered:** [count] out of [total]
- **Sections covered:** [list]

---

## Selection Dependencies

| # | Decision | Depends On | Notes |
|---|----------|-----------|-------|
| 1 | [selection decision] | [what it depends on — e.g., quality remediation in 3.2] | [notes] |

---

## To Be Clarified

[List any selection decisions that could not be finalized. Remove this section if everything is complete.]

---

## Source Documents

- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 2.1 Data Collection: `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- 2.2 Data Description: `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- 2.3 Data Exploration: `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- 2.4 Data Quality: `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 7: Summary and Next Steps

After writing the document, present a summary:

> **Data Selection Report created** at `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
>
> **Summary:**
> - [N] datasets selected out of [M] available
> - [N] fields selected out of [M] total
> - [N] records retained ([%] of original)
> - Date range: [start] to [end]
> - [N] data leakage risks identified and mitigated
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/clean-data` to handle missing values, outliers, and quality issues in the selected data (Task 3.2).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to mark "Data Preparation" as "In Progress" and add the 3.1 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Every dataset from 2.1 is accounted for (selected or excluded with rationale)
- [ ] Every field in selected datasets has a documented role (target, feature, ID, context, or excluded)
- [ ] Data leakage risks are assessed and mitigated
- [ ] Record selection criteria are explicit and reproducible
- [ ] Coverage analysis confirms sufficient data for modeling goals
- [ ] PII fields are excluded or flagged for pseudonymization
- [ ] Selection decisions reference the data mining goals from 1.3
- [ ] Quality issues from 2.4 are considered in selection decisions
- [ ] No selection decision assumes data cleaning that hasn't happened yet (or is flagged as a dependency)
- [ ] Document cross-references Phase 2 documents where applicable
