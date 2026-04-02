---
name: status
description: "Full CRISP-DM project status dashboard — shows all phases, task completeness, document gaps, and overall health"
---

# /status — CRISP-DM Project Status Dashboard

Generate a comprehensive status overview of all CRISP-DM phases and tasks, including document completeness assessment.

## Step 1: Read Project Context

Read `.claude/CLAUDE.md` to get the project name, business objective, and current phase tracker.

## Step 2: Read and Assess All Artifacts

Attempt to read every artifact file below. For each file that exists, perform the **completeness assessment** described in Step 3.

**Phase 1 — Business Understanding:**
- `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

**Phase 2 — Data Understanding:**
- `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`

**Phase 3 — Data Preparation:**
- `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
- `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
- `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
- `docs/crisp-dm/3-data-preparation/3.5-format-data.md`

**Phase 4 — Modeling:**
- `docs/crisp-dm/4-modeling/4.1-select-modeling-techniques.md`
- `docs/crisp-dm/4-modeling/4.2-generate-test-design.md`
- `docs/crisp-dm/4-modeling/4.3-build-model.md`
- `docs/crisp-dm/4-modeling/4.4-assess-model.md`

**Phase 5 — Evaluation:**
- `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
- `docs/crisp-dm/5-evaluation/5.2-review-process.md`
- `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`

**Phase 6 — Deployment:**
- `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
- `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md`
- `docs/crisp-dm/6-deployment/6.3-produce-final-report.md`
- `docs/crisp-dm/6-deployment/6.4-review-project.md`

## Step 3: Completeness Assessment (for each existing document)

For every document that exists, read it fully and assess these five dimensions:

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
Check if a `## To Be Clarified` section exists. If it does, extract each item listed. These are known gaps that the author flagged.

### 3d. Sign-off Status
Check the `## Sign-off` table. Count how many sign-offs are `Pending` vs `Approved` vs empty.

### 3e. Required Sections Check
Verify that all major sections expected for this document type are present and non-empty. Use the corresponding skill file as the reference for what sections are required:

| Document | Required Sections |
|----------|-------------------|
| 1.1 | Background (Organization Context, Problem Area, Current Solution), Business Objectives (Primary Objective, Business Questions, Constraints, Expected Benefits), Business Success Criteria |
| 1.2 | Inventory of Resources (Hardware, Data Sources, Knowledge Sources, Personnel), Requirements/Assumptions/Constraints, Risks & Contingencies, Terminology, Costs & Benefits |
| 1.3 | Data Mining Problem Specification, Data Mining Goals (with Traceability table), Data Mining Success Criteria (with Baseline, Evaluation Methodology, Business-to-Technical Mapping), Scope & Constraints |
| 1.4 | Project Overview, Project Stages (with Stage Details), Dependencies, Risk-Adjusted Timeline, Tool & Technique Assessment, Communication & Governance |
| 2.1 | Data Acquisition Log, Initial Data Inventory (with Column Summary per dataset), Selection Rationale, Loading & Storage |
| 2.2 | Dataset Overview, Data Dictionary (per dataset with all fields), Surface Statistics (Numeric, Categorical, Temporal), Structural Notes (Join Keys, Format Details), Initial Observations |
| 2.3 | Exploration Overview, Univariate Analysis (Target + Key Features), Bivariate/Multivariate Analysis (Correlations, Feature-Target Relationships), Temporal Patterns (Trend, Seasonality, Structural Breaks), Subgroup Analysis, Key Findings, Feature Hypotheses, Modeling Implications |
| 2.4 | Quality Summary (Overall Assessment with scores, Go/No-Go), Completeness (Missing Values, Coverage Gaps), Correctness (Range Violations, Business Rule Violations, Type Errors), Consistency (Duplicates, Cross-Field, Cross-Dataset), Timeliness (Freshness, Temporal Gaps), Assumption Validation, Remediation Plan |
| 3.1 | Selection Overview, Dataset Selection (with Excluded Datasets), Field Selection (per dataset with Data Leakage Assessment), Record Selection (Inclusion Criteria, Exclusion Criteria, Coverage Analysis), Selection Dependencies |
| 3.2 | Cleaning Overview, Cleaning Plan (prioritized issues), Missing Value Treatment (Summary, Imputation Details, Indicator Variables), Outlier & Noise Treatment, Duplicate Treatment, Cleaning Impact (Before vs After, Target Variable Impact), Cleaning Code |
| 3.3 | Construction Overview, Feature Catalog (Temporal, Aggregation, Domain-Specific, Interaction features), Generated Records, Value Transformations, Data Leakage Assessment, Feature Statistics, Construction Code |
| 3.4 | Integration Overview, Input Datasets, Key Mappings, Integration Steps (with row counts), Conflict Resolution, Integrated Dataset Summary (Coverage Analysis, Join Quality Metrics), Integration Code |
| 3.5 | Formatting Overview, Formatting Transformations (Type Casting, Column Operations, Encoding), Train/Validation/Test Split (Strategy, Boundaries, Statistics, Distribution Shift Check), Output Dataset Specification (Final Schema, File Locations, Loading Instructions, Version Control), Dataset Card |
| 5.1 | Evaluation Overview, Business Objective Alignment (Objectives Fully/Partially/Not Met), Business Success Criteria Assessment (Critical and Non-Critical Criteria Status), Business Impact Assessment (Value Delivered, Cost of Errors, Net Assessment), Risk & Limitation Assessment (Operational, Data, Business Risks, Conditions for Model Use), Stakeholder Readiness, Overall Verdict |
| 5.2 | Review Overview, Phase-by-Phase Review (Phase 1-4 with Status/Quality/Issues per task, Phase Assessment, Key Decisions), Cross-Phase Consistency, Overlooked Factors (Data, Modeling, Business Concerns), Methodology Assessment (What Worked Well, What Should Be Improved, Process Shortcuts), Lessons Learned (For This Project, For Future Projects), Recommended Actions Before Proceeding |
| 5.3 | Decision Summary, Decision Inputs (From 5.1, From 5.2, Resource & Timeline Context), Decision with Rationale and Decision Factors, Action Plan (Deployment Plan OR Iteration Plan OR Termination Plan with appropriate subsections), Approval |
| 6.1 | Deployment Overview, Serving Architecture (Serving Pattern, Inference Pipeline, Compute Infrastructure, Data Flow, Scaling Strategy, Dependency Management), Rollout Strategy (Approach, Rollout Phases, Validation Gates, Rollback Triggers, Rollback Procedure, Communication Plan), Operational Handover (Ownership, Runbook Summary, SLA, Access Control), Infrastructure Requirements (Cost Estimate, CI/CD Pipeline, Secrets Management) |
| 6.2 | Monitoring Overview, Data Drift Monitoring (Feature Drift, Label Drift, Schema Drift, Upstream Data Quality), Prediction Monitoring (Prediction Distribution, Prediction Quality, Business Metric Tracking), Alerting Strategy (Alert Levels, Alert Configuration, On-call Procedures), Retraining Strategy (Retraining Triggers, Retraining Pipeline, Validation Gates, Data Window), Maintenance Procedures (Scheduled Maintenance, Model Versioning, Data Retention, Decommissioning Criteria) |
| 6.3 | Executive Summary (Business Problem, What We Did, Key Results, Business Impact, Deployment Status, Key Risks, Recommended Next Steps), Technical Report (Methodology, Data Summary, Feature Engineering, Modeling Results, Deployment Architecture, Monitoring Plan, Technical Debt, Recommendations), Model Card (Model Details, Intended Use, Training Data, Evaluation Data, Performance Metrics, Fairness Assessment, Limitations, Ethical Considerations, Recommendations), Project Artifacts Index |
| 6.4 | Review Overview, Objectives vs. Outcomes (Scope Changes), Phase-by-Phase Review (all 6 phases), Risk Review (Identified Risks, Unidentified Risks), Process Improvements (Tools, Team/Skills, Communication, CRISP-DM Process), Reusable Knowledge (Code/Pipelines, Patterns, Anti-patterns, Domain Knowledge, Data Source Insights), Key Lessons, Action Items |

A section is "empty" if it contains only the heading, only template placeholder text, or fewer than 2 substantive lines of content.

### 3f. Assign Completeness Rating

- **Complete** — Status is Approved, no TBC items, no unfilled placeholders, all sign-offs approved, all required sections filled
- **Mostly Complete** — Substantive content in all required sections, but minor gaps: Status is Draft/Review, 1-2 TBC items, or sign-offs still pending. Good enough for downstream tasks.
- **Incomplete** — Significant gaps: 3+ TBC items, unfilled placeholders in required sections, or one or more required sections empty/missing. Downstream tasks weakened.
- **Stub** — Mostly template text or placeholders. Little to no real content filled in.

## Step 4: Check for Non-Document Artifacts

Check for code and notebook artifacts that indicate progress:

- `notebooks/` — any EDA or exploration notebooks (Phase 2)
- `src/` or `pipelines/` — any feature engineering or data prep code (Phase 3)
- `models/` or MLflow experiment logs — any trained models (Phase 4)
- `reports/` — any evaluation reports or model cards (Phase 5)

## Step 5: Present the Full Status Dashboard

Present the output in this exact format:

> # CRISP-DM Project Status
>
> **Project:** [project name from CLAUDE.md]
> **Date:** [current date]
> **Overall Progress:** [N]/24 tasks complete
>
> ---
>
> ## Phase Overview
>
> | Phase | Progress | Status | Health |
> |-------|----------|--------|--------|
> | 1. Business Understanding | [N]/4 | [In Progress / Complete / Not Started] | [see health rules below] |
> | 2. Data Understanding | [N]/4 | ... | ... |
> | 3. Data Preparation | [N]/5 | ... | ... |
> | 4. Modeling | [N]/4 | ... | ... |
> | 5. Evaluation | [N]/3 | ... | ... |
> | 6. Deployment | [N]/4 | ... | ... |
>
> **Health indicators:**
> - **On Track** — all existing documents are "Complete" or "Mostly Complete", no blockers
> - **Needs Attention** — one or more documents are "Incomplete" or have blocking TBC items
> - **At Risk** — documents are "Stub" or critical gaps exist that block downstream work
> - **—** — phase not started
>
> ---
>
> ## Detailed Task Status
>
> ### Phase 1: Business Understanding
>
> | Task | Document | Completeness | Status | TBC Items | Placeholders | Sign-offs |
> |------|----------|-------------|--------|-----------|-------------|-----------|
> | 1.1 Determine Business Objectives | Exists | Mostly Complete | Draft | 5 | 0 | 0/4 approved |
> | 1.2 Assess Situation | Missing | — | — | — | — | — |
> | 1.3 Determine Data Mining Goals | Missing | — | — | — | — | — |
> | 1.4 Produce Project Plan | Missing | — | — | — | — | — |
>
> [Repeat for each phase that has at least one existing document or is the current/next phase to work on. For phases that are entirely "Not Started" and not next, show a single summary row.]
>
> ---
>
> ## Document Health Details
>
> [For each document rated "Incomplete" or "Stub", show the specific gaps. For "Mostly Complete" documents, show a brief summary. Skip "Complete" documents.]
>
> ### 1.1 Business Objectives — Mostly Complete
> - **Status:** Draft
> - **To Be Clarified (5):**
>   1. [item 1]
>   2. [item 2]
>   3. [... all items]
> - **Sign-offs:** 0/4 approved (Sponsor, Domain Expert x2, Data Scientist — all Pending)
> - **Missing sections:** None
> - **Unfilled placeholders:** None
>
> [Repeat for each document that is not "Complete" or "Missing"]
>
> ---
>
> ## Code & Notebook Artifacts
>
> | Type | Location | Count | Phase |
> |------|----------|-------|-------|
> | EDA Notebooks | `notebooks/` | [N] files | Phase 2 |
> | Pipeline Code | `src/` | [N] files | Phase 3 |
> | Trained Models | `models/` | [N] artifacts | Phase 4 |
> | Reports | `reports/` | [N] files | Phase 5 |
>
> [Only show rows for artifact types that exist. If none exist, show "No code or notebook artifacts found yet."]
>
> ---
>
> ## Recommendations
>
> 1. **Next task:** [same recommendation logic as /next — what to work on next]
>    Run: `/[command]`
>
> 2. **Open gaps to address:** [list any "Incomplete" documents or blocking TBC items, ordered by priority]
>
> 3. **Approaching milestones:** [any deadlines or decision points extracted from existing documents, e.g., "Variability analysis due April 2026 per 1.1 success criteria"]

## Step 6: Update the Phase Tracker

If the phase tracker in `.claude/CLAUDE.md` is out of date, update it to reflect the current state. Add artifact links for any completed tasks that are missing from the tracker.
