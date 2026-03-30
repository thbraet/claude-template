---
name: integrate-data
description: "CRISP-DM 3.4 — Integrate Data. Merges datasets from multiple sources into a unified analysis dataset. Documents join logic, key mappings, conflict resolution, and record reconciliation. Produces a structured data integration report in docs/crisp-dm/3-data-preparation/."
argument-hint: "<paths to datasets or join keys to use>"
---

# /integrate-data — CRISP-DM 3.4: Integrate Data

> **Phase:** 3. Data Preparation | **Task:** 3.4 Integrate Data
>
> *"These are methods whereby information is combined from multiple tables or records to create new records or values."*

## Purpose

This skill merges multiple cleaned and feature-engineered datasets into a single unified analysis dataset ready for modeling. It documents every join operation, key mapping, conflict resolution strategy, and the resulting dataset shape. It produces four outputs:

1. **Integration Plan** — which datasets to merge, join keys, join types, expected cardinality
2. **Key Mapping** — how identifiers align across datasets (e.g., DC drager codes to Plato section codes)
3. **Conflict Resolution** — how overlapping fields, duplicate keys, or mismatched granularity are handled
4. **Integration Result** — the unified dataset specification with shape, coverage, and quality metrics

## Output Location

All artifacts are written to: `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
- If it exists, present its contents and ask: *"A data integration report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
  - If it exists, use it — it defines which datasets are in scope.
- Read `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
  - If it exists, use it — it defines the cleaned data state.
- Read `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
  - If it exists, use it — it defines constructed features to include.
- Read `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
  - If it exists, use it — data dictionary helps identify join keys and field semantics.
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines the required output granularity.

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File paths** — Read/profile the datasets to identify join keys and overlaps
- **Join keys** — Use as the basis for the integration plan
- **No input provided** — Use the Phase 2 and 3 documents to propose an integration plan

Read ALL provided sources before proceeding.

### Step 3: Design Integration Plan

Based on the selected and cleaned datasets, design the merge strategy:

**Identify join relationships:**
- For each pair of datasets: What are the join keys? (store ID, date, section, product category)
- What is the join type? (inner, left, right, full outer)
- What is the expected cardinality? (1:1, 1:N, N:M)
- Are the keys directly compatible or do they need mapping? (e.g., DC drager codes to Plato sections)

**Assess granularity alignment:**
- Are all datasets at the same granularity (e.g., store x day x section)?
- If not, what aggregation or disaggregation is needed?
- What is the target granularity (from 1.3)?

**Plan conflict resolution:**
- Overlapping columns: which source takes precedence?
- Duplicate keys: how are they handled?
- Missing matches: what happens when a left join has no match?

**Plan the merge order:**
- Start with the primary dataset (usually the one containing the target variable)
- Add datasets in dependency order
- Document the expected row count after each join

### Step 4: Present Integration Plan and Ask for Confirmation

Present the proposed integration plan:

> **Integration Plan:**
>
> **Target granularity:** [e.g., store x day x section]
>
> | Step | Left Dataset | Right Dataset | Join Key(s) | Join Type | Expected Result |
> |------|-------------|---------------|-------------|-----------|-----------------|
> | 1 | [primary] | [secondary] | [keys] | left / inner | [expected rows] |
>
> **Key Mappings Required:**
> | Source A Field | Source B Field | Mapping Type | Notes |
> |---------------|---------------|-------------|-------|
> | [field] | [field] | Direct / Lookup table / Fuzzy | [notes] |
>
> **Conflict Resolution:**
> | Overlap | Resolution | Rationale |
> |---------|-----------|-----------|
> | [overlapping field] | Keep source A / Coalesce / Average | [reason] |

Ask the user to confirm or adjust.

Wait for the user's response before continuing.

### Step 5: Execute Integration (Code Generation)

After the plan is confirmed, generate reproducible integration code:

```python
# Generate integration pipeline code
# - Each join step is logged with before/after row counts
# - Key mappings are explicit lookup tables (not hardcoded)
# - Conflict resolution is documented in code comments
# - Assertions verify expected cardinality at each step
# - Final dataset shape is validated against target granularity
```

If data files are accessible, offer to run the code and report results. If not, generate the code as a script.

### Step 6: Clarification Round (if needed)

If the user's response still has gaps:
- Ask a focused follow-up
- Maximum 2 clarification rounds — mark remaining as "TBD"

### Step 7: Generate the Output Document

```bash
mkdir -p docs/crisp-dm/3-data-preparation
```

Write the file `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md` using this template:

```markdown
# 3.4 Data Integration Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 3. Data Preparation
> **Status:** Draft | Review | Approved

---

## Integration Overview

- **Target granularity:** [e.g., store x day x section — from 1.3]
- **Input datasets:** [count] datasets from 3.1/3.2/3.3
- **Integration method:** [sequential joins / star schema / denormalization]
- **Output:** Single unified analysis dataset

---

## Input Datasets

| # | Dataset | Source | Rows | Fields | Granularity | Role |
|---|---------|--------|------|--------|-------------|------|
| 1 | [name] | [3.1/3.2/3.3 reference] | [rows] | [fields] | [granularity] | Primary (target) / Feature source / Context |

---

## Key Mappings

### [Mapping Name — e.g., DC Drager to Plato Section]

| Source A Value | Source B Value | Notes |
|---------------|---------------|-------|
| [value] | [value] | [notes] |

- **Mapping coverage:** [%] of records mapped successfully
- **Unmapped records:** [count] — treatment: [drop / assign default / flag]
- **Mapping source:** [lookup table location or derivation method]

[Repeat for each non-trivial key mapping]

---

## Integration Steps

### Step 1: [Description]
- **Left:** [dataset] ([rows] rows)
- **Right:** [dataset] ([rows] rows)
- **Join keys:** [fields]
- **Join type:** [inner / left / right / full outer]
- **Expected cardinality:** [1:1 / 1:N / N:M]
- **Result:** [rows] rows, [fields] fields
- **Records lost (no match):** [count] ([%])
- **Duplicates introduced:** [count or "none"]

[Repeat for each integration step]

---

## Conflict Resolution

| # | Overlapping Field | Source A | Source B | Resolution | Rationale |
|---|-------------------|----------|----------|-----------|-----------|
| 1 | [field] | [dataset] | [dataset] | Keep A / Coalesce / Average / Rename | [reason] |

---

## Integrated Dataset Summary

- **Total rows:** [count]
- **Total fields:** [count]
- **Date range:** [start] to [end]
- **Stores covered:** [count] out of [total]
- **Sections covered:** [list]
- **Target variable completeness:** [%]

### Coverage Analysis
| Dimension | Values | Coverage |
|-----------|--------|----------|
| Stores | [count] | [%] of total CLP stores |
| Sections | [list] | [%] of target sections |
| Date range | [start] to [end] | [%] of requested range |

### Join Quality Metrics
| Step | Input Rows (L) | Input Rows (R) | Output Rows | Match Rate | Notes |
|------|---------------|----------------|-------------|------------|-------|
| 1 | [count] | [count] | [count] | [%] | [notes] |

---

## Integration Code

### Pipeline Location
- **Script:** `src/data/integrate.py` (or notebook reference)
- **Key mapping files:** [locations]
- **Dependencies:** [libraries]
- **Usage:** `python src/data/integrate.py --output [path]`

### Reproducibility Notes
- Join order is deterministic
- Key mapping tables are versioned
- Assertions validate row counts at each step
- Output dataset is saved to [format] at [location]

---

## To Be Clarified

[List any integration decisions that could not be finalized. Remove this section if everything is complete.]

---

## Source Documents

- 3.1 Data Selection: `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- 3.2 Data Cleaning: `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
- 3.3 Data Construction: `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
- 2.2 Data Description: `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
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

After writing the document, present a summary:

> **Data Integration Report created** at `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
>
> **Summary:**
> - [N] datasets merged into unified analysis dataset
> - [N] join operations performed
> - [N] key mappings applied ([%] coverage)
> - Final dataset: [rows] rows x [fields] fields
> - Date range: [start] to [end]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/format-data` to apply final formatting transformations for the modeling tool (Task 3.5).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 3.4 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] All selected datasets from 3.1 are included in the integration
- [ ] Join keys are explicitly documented for every merge step
- [ ] Key mappings are complete and coverage percentages are reported
- [ ] Row counts are tracked at every step (no unexplained growth or loss)
- [ ] Conflict resolution is documented for every overlapping field
- [ ] The final dataset matches the target granularity from 1.3
- [ ] Target variable completeness is acceptable for modeling
- [ ] Integration code is reproducible with assertions
- [ ] No PII is included in the document or key mapping tables
- [ ] No data leakage is introduced through integration (e.g., joining on future data)
