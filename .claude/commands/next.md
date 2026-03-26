---
name: next
description: "Show the next CRISP-DM task to work on, based on which artifacts exist, their completeness, and what's still missing"
---

# /next — What Should I Work On Next?

Check the current progress of the CRISP-DM project, assess document completeness, and recommend the next task.

## Step 1: Read the Phase Tracker

Read `.claude/CLAUDE.md` to get the current phase tracker status.

## Step 2: Check Which Artifacts Exist and Assess Their Completeness

Attempt to read each artifact file listed below. For each file that exists, perform a **completeness assessment** (see Step 3). For files that don't exist, mark them as "Missing".

**Phase 1 — Business Understanding:**
- [ ] `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- [ ] `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- [ ] `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- [ ] `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

**Phase 2 — Data Understanding:**
- [ ] `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- [ ] `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- [ ] `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- [ ] `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`

**Phase 3 — Data Preparation:**
- [ ] `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.5-format-data.md`

**Phase 4 — Modeling:**
- [ ] `docs/crisp-dm/4-modeling/4.1-select-modeling-techniques.md`
- [ ] `docs/crisp-dm/4-modeling/4.2-generate-test-design.md`
- [ ] `docs/crisp-dm/4-modeling/4.3-build-model.md`
- [ ] `docs/crisp-dm/4-modeling/4.4-assess-model.md`

**Phase 5 — Evaluation:**
- [ ] `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
- [ ] `docs/crisp-dm/5-evaluation/5.2-review-process.md`
- [ ] `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`

**Phase 6 — Deployment:**
- [ ] `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
- [ ] `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md`
- [ ] `docs/crisp-dm/6-deployment/6.3-produce-final-report.md`
- [ ] `docs/crisp-dm/6-deployment/6.4-review-project.md`

## Step 3: Completeness Assessment (for each existing document)

For every document that exists, read it fully and check these five dimensions:

### 3a. Document Status
Extract the `**Status:**` field from the document header. Values: `Draft`, `Review`, `Approved`.

### 3b. Placeholder Detection
Scan the entire document for unfilled placeholders. Count occurrences of:
- `[TODO]`, `[TBD]`, `[TBC]`, `[PLACEHOLDER]` (case-insensitive)
- Template brackets that were never filled: `[description]`, `[name]`, `[value]`, `[duration]`, `[date]`, `[cost]`, etc. — any `[lowercase word]` pattern that looks like an unfilled template field
- Empty table cells in rows that should have content (a row where most cells are `|  |`)
- Sections that contain only the template instruction text (e.g., "one clear sentence", "list the meeting notes")

Do NOT count brackets that are intentional references (e.g., `[1.1-business-objectives.md]` links) or abbreviations (e.g., `[DB/API/File]`).

### 3c. "To Be Clarified" Section
Check if a `## To Be Clarified` section exists. If it does, extract each item listed. These are known gaps that the author flagged. If the section says to "Remove this section if everything is complete" and it's still present, that means there are open items.

### 3d. Sign-off Status
Check the `## Sign-off` table. Count how many sign-offs are `Pending` vs `Approved` vs empty.

### 3e. Required Sections Check
Verify that all major sections expected for this document type are present and non-empty. Use the corresponding skill file as the reference for what sections are required:

| Document | Required Sections Reference |
|----------|---------------------------|
| 1.1 | Background (Organization Context, Problem Area, Current Solution), Business Objectives (Primary Objective, Business Questions, Constraints, Expected Benefits), Business Success Criteria |
| 1.2 | Inventory of Resources (Hardware, Data Sources, Knowledge Sources, Personnel), Requirements/Assumptions/Constraints, Risks & Contingencies, Terminology, Costs & Benefits |
| 1.3 | Data Mining Problem Specification, Data Mining Goals (with Traceability table), Data Mining Success Criteria (with Baseline, Evaluation Methodology, Business-to-Technical Mapping), Scope & Constraints |
| 1.4 | Project Overview, Project Stages (with Stage Details for each), Dependencies, Risk-Adjusted Timeline, Tool & Technique Assessment, Communication & Governance |
| 2.1 | Data Acquisition Log, Initial Data Inventory (with Column Summary per dataset), Selection Rationale, Loading & Storage |
| 2.2 | Dataset Overview, Data Dictionary (per dataset with all fields), Surface Statistics (Numeric, Categorical, Temporal), Structural Notes (Join Keys, Format Details), Initial Observations |
| 2.3 | Exploration Overview, Univariate Analysis (Target + Key Features), Bivariate/Multivariate Analysis (Correlations, Feature-Target Relationships), Temporal Patterns (Trend, Seasonality, Structural Breaks), Subgroup Analysis, Key Findings, Feature Hypotheses, Modeling Implications |
| 2.4 | Quality Summary (Overall Assessment with scores, Go/No-Go), Completeness (Missing Values, Coverage Gaps), Correctness (Range Violations, Business Rule Violations, Type Errors), Consistency (Duplicates, Cross-Field, Cross-Dataset), Timeliness (Freshness, Temporal Gaps), Assumption Validation, Remediation Plan |

A section is "empty" if it contains only the heading, only template placeholder text, or fewer than 2 substantive lines of content.

### 3f. Assign Completeness Rating

Based on the five dimensions, assign each document one of:

- **Complete** — Status is Approved, no TBC items, no unfilled placeholders, all sign-offs approved, all required sections filled
- **Mostly Complete** — Document exists with substantive content in all required sections, but has minor gaps: Status is Draft/Review, 1-2 TBC items, or sign-offs still pending. Content is good enough for downstream tasks to build on.
- **Incomplete** — Document exists but has significant gaps: 3+ TBC items, unfilled placeholders/template text in required sections, or one or more required sections are empty/missing. Downstream tasks will be weakened by these gaps.
- **Stub** — Document exists but is mostly template text or placeholders. Little to no real content has been filled in.

## Step 4: Also Check for Non-Document Artifacts

Check for code and notebook artifacts that indicate progress:

- [ ] `notebooks/` — any EDA or exploration notebooks (Phase 2)
- [ ] `src/` or `pipelines/` — any feature engineering or data prep code (Phase 3)
- [ ] `models/` or MLflow experiment logs — any trained models (Phase 4)
- [ ] `reports/` — any evaluation reports or model cards (Phase 5)

## Step 5: Determine Next Task

Apply these rules in priority order:

1. **Incomplete documents in the current phase take priority over new tasks.** If 1.1 exists but is "Incomplete" or "Stub", recommend completing it before moving to 1.2. Use the appropriate `/command` with the "update" option.
2. **"Mostly Complete" documents do NOT block progress.** A document rated "Mostly Complete" is good enough to move forward — flag the open items but recommend the next sequential task.
3. **Within a phase, tasks are sequential.** Don't recommend 1.3 if 1.2 doesn't exist yet.
4. **A phase is complete when all its tasks are at least "Mostly Complete".**
5. **Phases are mostly sequential**, but CRISP-DM allows iteration — if earlier phase documents are "Incomplete" while later phases have started, flag this as a warning.
6. **TBC items that block downstream work get special attention.** If a TBC item in 1.1 is needed by 1.3 (e.g., a missing success criterion threshold), call it out explicitly.

## Step 6: Present the Status and Recommendation

Present the output in this exact format:

> ## CRISP-DM Progress
>
> | Phase | Tasks | Progress | Status |
> |-------|-------|----------|--------|
> | 1. Business Understanding | 4 | [N]/4 | [phase status] |
> | 2. Data Understanding | 4 | [N]/4 | [phase status] |
> | 3. Data Preparation | 5 | [N]/5 | [phase status] |
> | 4. Modeling | 4 | [N]/4 | [phase status] |
> | 5. Evaluation | 3 | [N]/3 | [phase status] |
> | 6. Deployment | 4 | [N]/4 | [phase status] |
>
> ### Current Phase: [phase name]
>
> | Task | Artifact | Completeness | Issues |
> |------|----------|-------------|--------|
> | 1.1 Determine Business Objectives | Exists | Mostly Complete | 5 TBC items, sign-offs pending |
> | 1.2 Assess Situation | Missing | — | — |
> | ... | ... | ... | ... |
>
> [For each document rated "Incomplete" or "Stub", list the specific gaps:]
>
> ### Document Gaps
>
> **1.1 Business Objectives** (Mostly Complete)
> - Status: Draft (not yet approved)
> - To Be Clarified (5 items):
>   - Variability threshold: What exact CV% does Koen consider "significant enough"?
>   - Financial impact: No simulation of over/understaffing costs in EUR yet
>   - [... list all items]
> - Sign-off: 0/4 approved
> - Unfilled placeholders: none
> - Missing sections: none
>
> [Repeat for each document that has gaps. Omit this section entirely if all existing documents are "Complete".]
>
> ---
>
> ## Next Up
>
> **[Task number]: [Task name]**
> [One sentence explaining what this task does and why it's next]
>
> Run: `/[command-name]`
>
> [If the recommendation is to complete an existing document rather than start a new one:]
> Run: `/[command-name]` — select "update" when prompted to address the gaps above
>
> **Tip:** [Any relevant context, e.g., "Have your meeting notes ready" or "This task will read your 1.1 and 1.2 documents automatically"]
>
> ### Also Consider
> [Optional section — only include if there are open TBC items or incomplete documents that don't block the next task but should be addressed soon. E.g., "The 5 TBC items in 1.1 should be clarified before starting 1.3, as the data mining goals depend on finalized success criteria."]

## Step 7: Update the Phase Tracker

If the phase tracker in `.claude/CLAUDE.md` is out of date (e.g., artifacts exist that aren't listed, or a phase status is wrong), update it to reflect the current state. Add artifact links for any completed tasks that are missing from the tracker.
