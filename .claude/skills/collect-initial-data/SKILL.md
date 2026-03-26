---
name: collect-initial-data
description: "CRISP-DM 2.1 — Collect Initial Data. Documents the data acquisition process, inventories received datasets, and records selection rationale and storage details. Produces a structured data collection report in docs/crisp-dm/2-data-understanding/."
argument-hint: "<path to data file, directory, or data source description>"
---

# /collect-initial-data — CRISP-DM 2.1: Collect Initial Data

> **Phase:** 2. Data Understanding | **Task:** 2.1 Collect Initial Data
>
> *"Acquire the data (or access to the data) listed in the project resources. This initial collection includes data loading, if necessary for data understanding. Note any issues encountered and any resolutions achieved."*

## Purpose

This skill documents how each data source was acquired, what was received, why it was selected, and where it is stored. It reads prior CRISP-DM documents to cross-reference the planned data sources against what was actually obtained. It produces four outputs:

1. **Data Acquisition Log** — how each source was obtained, access method, date, issues encountered
2. **Initial Data Inventory** — what was received (files, tables), row/column counts, date ranges
3. **Selection Rationale** — why each dataset is included, mapped to data mining goals
4. **Loading & Storage** — file locations, formats, sizes, how to load

## Output Location

All artifacts are written to: `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- If it exists, present its contents and ask: *"A data collection report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if prerequisite documents exist:
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — it provides business context and the problem domain.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — it contains the planned data source inventory, access methods, and known quality issues.
  - If it does not exist, note it but proceed.
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it defines what the data needs to support (target variable, features, granularity).
  - If it does not exist, warn the user: *"No data mining goals document found (task 1.3). Without it, I can't verify whether the collected data supports the modeling objectives. Proceed anyway?"*

### Step 2: Ingest Source Information

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path or directory** (e.g., `data/raw/`, `data/raw/transport_history.csv`) — List files and attempt to read/profile them
- **Data source description** — Use the text to document the acquisition
- **No input provided** — If the 1.2 situation assessment exists, extract the planned data sources from it and ask: *"Based on the situation assessment, these data sources were planned: [list]. Which ones have you acquired so far? Please provide file paths or describe how to access them."*

Read ALL provided sources before proceeding.

### Step 3: Profile Available Data

For each data file or table the user provides access to, run profiling code to extract basic metadata:

```python
import pandas as pd
import os

# For each data file:
# - file size
# - row count, column count
# - column names and dtypes
# - date range (if temporal data)
# - first few rows (head)
# - basic stats (describe)
```

If the data is not directly accessible (e.g., database not yet connected), document what is known from the user's description and mark the profiling as "Pending — awaiting access."

### Step 4: Extract and Map Information

After reading the source documents and profiling available data, map every piece of information to the required fields below. Use this checklist internally:

**Section A — Data Acquisition Log:**
- [ ] For each data source from 1.2: Was it acquired? If not, why?
- [ ] Acquisition method (file transfer, DB query, API call, manual extract)
- [ ] Date of acquisition / extraction
- [ ] Who provided the data or granted access
- [ ] Issues encountered during acquisition (access problems, format issues, delays)
- [ ] Resolutions applied

**Section B — Initial Data Inventory:**
- [ ] Dataset name and identifier
- [ ] Source system
- [ ] File format (CSV, Parquet, JSON, DB table, etc.)
- [ ] Row count
- [ ] Column count
- [ ] Date range covered
- [ ] File size
- [ ] Key fields (identifiers, dates, target variable)

**Section C — Selection Rationale:**
- [ ] For each dataset: which data mining goal(s) from 1.3 does it support?
- [ ] What role does it play? (target variable source, feature source, context/reference)
- [ ] Are there alternative sources that were considered and rejected?

**Section D — Loading & Storage:**
- [ ] Storage location (file path, database, cloud)
- [ ] Loading instructions (code snippet or command)
- [ ] Dependencies (libraries, credentials, VPN)
- [ ] Version control (DVC tracked? Git LFS?)

### Step 5: Present Extracted Information and Ask About Gaps

Present what was extracted in a structured summary, organized by section. For each field, show one of:
- **Extracted:** the value found in the source documents or profiling, with a reference
- **Profiled:** the value obtained from running code on the data
- **Inferred from 1.2:** the value carried over from the situation assessment
- **Missing:** flag it clearly

Then ask the user to:
1. **Confirm or correct** the extracted information
2. **Fill in the missing fields**

**Important rules for this step:**
- Ask about ALL missing fields in a single message — do not split into multiple rounds for gaps
- If a data source from 1.2 was not acquired, ask why and whether it is still planned
- If profiling revealed unexpected results (e.g., far fewer rows than expected), flag them

Wait for the user's response before continuing.

### Step 6: Clarification Round (if needed)

If the user's response still has gaps or ambiguities:
- Ask a focused follow-up covering only the remaining gaps
- Maximum 2 clarification rounds — after that, mark remaining gaps as "TBD" in the document and note them in a "To be clarified" section

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/2-data-understanding
```

Write the file `docs/crisp-dm/2-data-understanding/2.1-data-collection.md` using this template:

```markdown
# 2.1 Data Collection Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 2. Data Understanding
> **Status:** Draft | Review | Approved

---

## Data Acquisition Log

| # | Source (from 1.2) | Acquired? | Method | Date | Provider | Issues | Resolution |
|---|-------------------|-----------|--------|------|----------|--------|------------|
| 1 | [source name] | [Yes/No/Partial] | [method] | [date] | [who] | [issues] | [resolution] |

### Sources Not Yet Acquired
[List any planned data sources from 1.2 that have not been obtained, with reasons and expected timeline.]

---

## Initial Data Inventory

### Dataset 1: [dataset name]
- **Source System:** [origin]
- **File Format:** [CSV / Parquet / DB table / etc.]
- **Storage Location:** [file path or DB reference]
- **File Size:** [size]
- **Row Count:** [rows]
- **Column Count:** [columns]
- **Date Range:** [start] to [end]
- **Key Fields:** [identifiers, dates, target variable]
- **Extraction Date:** [when the data was extracted]

#### Column Summary
| # | Column Name | Data Type | Non-Null Count | Unique Values | Sample Values |
|---|-------------|-----------|----------------|---------------|---------------|
| 1 | [column] | [type] | [count] | [unique] | [examples] |

[Repeat for each dataset]

---

## Selection Rationale

| # | Dataset | Data Mining Goal (from 1.3) | Role | Justification |
|---|---------|---------------------------|------|---------------|
| 1 | [dataset name] | [goal reference] | [Target / Feature / Context] | [why this data is needed] |

### Rejected Alternatives
[List any data sources that were considered but not selected, with reasons.]

---

## Loading & Storage

### Loading Instructions

#### Dataset 1: [dataset name]
```python
# Loading code
import pandas as pd
df = pd.read_csv("[path]", ...)
```

- **Dependencies:** [libraries, credentials, VPN, etc.]
- **DVC Tracked:** [Yes/No]
- **Notes:** [encoding, delimiter, special handling]

[Repeat for each dataset]

### Storage Overview
| Dataset | Location | Format | Size | Version Controlled |
|---------|----------|--------|------|--------------------|
| [name] | [path] | [format] | [size] | [Yes (DVC) / No] |

---

## To Be Clarified

[List any items that could not be determined from the source documents or user input. Remove this section if everything is complete.]

---

## Source Documents

- [List the sources used to produce this document]
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
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

> **Data Collection Report created** at `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
>
> **Summary:**
> - [N] datasets acquired out of [M] planned
> - Total rows: [total], Total columns: [total]
> - Date range: [earliest] to [latest]
> - [N] data sources still pending acquisition
> - [N] issues encountered during acquisition
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/describe-data` to create a detailed data dictionary and surface statistics for each dataset (Task 2.2).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to mark "Data Understanding" as "In Progress" and add the 2.1 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Every data source from 1.2 is accounted for (acquired or explained why not)
- [ ] Every acquired dataset has row count, column count, date range, and file size
- [ ] Every dataset has a selection rationale mapped to a data mining goal from 1.3
- [ ] Loading instructions are provided and reproducible
- [ ] Storage locations are documented and accessible to the team
- [ ] Data is version-controlled (DVC) or a plan to version-control it is noted
- [ ] No PII or sensitive data is included in the document (use column names, not actual values with PII)
- [ ] Raw data files are not committed to git (only tracked via DVC or Git LFS)
- [ ] Document cross-references the 1.1, 1.2, and 1.3 documents where applicable
