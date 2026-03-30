---
name: produce-final-report
description: "CRISP-DM 6.3 — Produce Final Report. Compiles the complete project documentation including executive summary for stakeholders, technical report for the data science team, model card, and lessons learned. Produces a structured final report in docs/crisp-dm/6-deployment/."
argument-hint: "<optional: audience focus (executive/technical), or specific section to draft>"
---

# /produce-final-report — CRISP-DM 6.3: Produce Final Report

> **Phase:** 6. Deployment | **Task:** 6.3 Produce Final Report
>
> *"At the end of the project, the project leader and his team write up a final report. Depending on the deployment plan, this report may be only a summary of the project and its experiences (if they have not already been documented as an ongoing activity) or it may be a final and comprehensive presentation of the data mining result(s)."*

## Purpose

This skill produces the final project report that documents the entire data mining engagement from business objectives through deployment. It includes an executive summary for business stakeholders, a technical report for the data science team, a model card for governance, and a consolidated lessons-learned section. This is the definitive record of what was done, why, and what was achieved.

## Output Location

- Report: `docs/crisp-dm/6-deployment/6.3-final-report.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/6-deployment/6.3-final-report.md`
- If it exists, present its contents and ask: *"A final report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Read ALL prior CRISP-DM artifacts — this report synthesizes the entire project:
- Phase 1: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`, `1.2-situation-assessment.md`, `1.3-data-mining-goals.md`, `1.4-project-plan.md`
- Phase 2: `docs/crisp-dm/2-data-understanding/2.1-initial-data-collection.md`, `2.2-data-description.md`, `2.3-data-exploration.md`, `2.4-data-quality.md`
- Phase 3: `docs/crisp-dm/3-data-preparation/3.1-select-data.md`, `3.2-clean-data.md`, `3.3-construct-data.md`, `3.4-integrate-data.md`, `3.5-format-data.md`
- Phase 4: `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`, `4.2-test-design.md`, `4.3-model-building.md`, `4.4-model-assessment.md`
- Phase 5: `docs/crisp-dm/5-evaluation/` (all files present)
- Phase 6: `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`, `6.2-plan-monitoring.md`
- Rules: `.claude/rules/model-governance.md`

For each file: if it exists, ingest it. If it does not exist, note it as a gap. Do not fail — the report should document what was completed and what remains.

### Step 2: Extract and Synthesize

From all ingested documents, extract and organize:
- **Business context** (from 1.1, 1.2) — problem, objectives, success criteria, constraints
- **Data mining goals** (from 1.3) — technical success criteria, target metrics
- **Data summary** (from Phase 2) — sources, quality, key findings from exploration
- **Preparation decisions** (from Phase 3) — feature engineering, data transformations, key choices
- **Modeling results** (from Phase 4) — techniques tried, best model, performance
- **Evaluation outcomes** (from Phase 5) — stakeholder review, business validation
- **Deployment plan** (from 6.1, 6.2) — architecture, monitoring, maintenance

Present a high-level synthesis and ask the user if anything is missing or needs emphasis.

### Step 3: Draft Executive Summary

Write a 1-2 page executive summary that:
- States the business problem in non-technical terms
- Summarizes what was done (without technical jargon)
- Presents key results in business terms (not model metrics)
- Quantifies business impact (cost savings, efficiency gains, risk reduction)
- States deployment status and next steps
- Includes key risks and limitations in plain language

### Step 4: Draft Technical Report

Write a technical report that:
- Describes the full methodology (CRISP-DM phases completed)
- Documents data sources, volumes, and quality
- Summarizes feature engineering and preparation choices
- Reports all models tried with their performance metrics
- Explains the selected model and why it was chosen
- Documents the deployment architecture and monitoring plan
- Lists technical debt and known limitations
- Provides recommendations for future iterations

### Step 5: Draft Model Card

Following model governance rules, create a model card that includes:
- **Model details** — name, version, type, framework, training date
- **Intended use** — primary use case, intended users, out-of-scope uses
- **Training data** — sources, date range, size, preprocessing
- **Evaluation data** — validation/test set details
- **Performance metrics** — primary and secondary metrics with values
- **Fairness assessment** — performance across key subgroups
- **Limitations** — known failure modes, underperforming segments
- **Ethical considerations** — potential harms, mitigations
- **Recommendations** — how to use (and not use) the model

### Step 6: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/6-deployment
```

Write the file `docs/crisp-dm/6-deployment/6.3-final-report.md` using this template:

```markdown
# 6.3 Final Report

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 6. Deployment
> **Status:** Draft | Review | Approved

---

## Executive Summary

### Business Problem
[1-2 paragraphs describing the business problem in non-technical terms]

### What We Did
[1-2 paragraphs summarizing the approach — data collection, analysis, modeling — without jargon]

### Key Results
| Outcome | Value |
|---------|-------|
| [e.g., Forecast accuracy] | [in business terms, e.g., "within 3 carts of actual for 85% of store-days"] |
| [e.g., Improvement over current process] | [quantified, e.g., "40% reduction in workforce misallocation"] |
| [e.g., Coverage] | [e.g., "all CLP stores, all sections"] |

### Business Impact
[1 paragraph quantifying the business value — cost savings, efficiency gains, better decisions]

### Deployment Status
[Current status — deployed / deploying / ready for deployment]

### Key Risks and Limitations
- [Risk 1 in plain language]
- [Risk 2 in plain language]
- [Limitation 1 in plain language]

### Recommended Next Steps
1. [Next step 1]
2. [Next step 2]
3. [Next step 3]

---

## Technical Report

### Methodology
This project followed the CRISP-DM methodology across [N] phases:

| Phase | Status | Key Outcome |
|-------|--------|-------------|
| 1. Business Understanding | [status] | [one-line summary] |
| 2. Data Understanding | [status] | [one-line summary] |
| 3. Data Preparation | [status] | [one-line summary] |
| 4. Modeling | [status] | [one-line summary] |
| 5. Evaluation | [status] | [one-line summary] |
| 6. Deployment | [status] | [one-line summary] |

### Data Summary

#### Sources
| Source | Records | Date Range | Key Variables |
|--------|---------|-----------|---------------|
| [source] | [count] | [range] | [variables] |

#### Quality
- **Completeness:** [summary]
- **Key issues found:** [summary]
- **Remediation applied:** [summary]

### Feature Engineering
| Feature | Description | Source | Rationale |
|---------|-------------|--------|-----------|
| [feature] | [what it represents] | [derived from] | [why useful] |

### Modeling Results

#### Models Evaluated
| Model | [Primary Metric] | vs. Baseline | Selected |
|-------|------------------|-------------|----------|
| Baseline ([type]) | [value] | — | No |
| [Model A] | [value] | [+/- %] | [Yes/No] |
| [Model B] | [value] | [+/- %] | [Yes/No] |

#### Selected Model
- **Technique:** [technique + configuration]
- **Primary Metric:** [metric] = [value]
- **Key Hyperparameters:** [list]
- **Training Data:** [date range, size]
- **MLflow Run ID:** [run ID]

#### Error Analysis Summary
- **Best performing segments:** [segments]
- **Worst performing segments:** [segments]
- **Systematic biases:** [summary]

### Deployment Architecture
[Brief summary of serving pattern, infrastructure, rollout strategy — reference 6.1 for details]

### Monitoring Plan
[Brief summary of what is monitored, alert thresholds, retraining triggers — reference 6.2 for details]

### Technical Debt and Known Limitations
| Item | Description | Severity | Recommended Action |
|------|-------------|----------|-------------------|
| [item] | [description] | [High/Medium/Low] | [what to do] |

### Recommendations for Future Iterations
1. [Recommendation 1 — e.g., additional data sources to incorporate]
2. [Recommendation 2 — e.g., modeling approaches to explore]
3. [Recommendation 3 — e.g., infrastructure improvements]

---

## Model Card

### Model Details
| Field | Value |
|-------|-------|
| Model Name | [name] |
| Version | [version] |
| Type | [technique] |
| Framework | [e.g., scikit-learn, XGBoost, PyTorch] |
| Training Date | [date] |
| MLflow Run ID | [run ID] |
| Model Registry | [location] |

### Intended Use
- **Primary use case:** [what the model predicts and for whom]
- **Intended users:** [who consumes predictions]
- **Out-of-scope uses:** [what the model should NOT be used for]

### Training Data
- **Sources:** [data sources]
- **Date range:** [start — end]
- **Size:** [rows × features]
- **Preprocessing:** [summary of key transformations]

### Evaluation Data
- **Validation set:** [date range, size]
- **Test set:** [date range, size]
- **Splitting strategy:** [temporal split details]

### Performance Metrics
| Metric | Validation | Test | Threshold |
|--------|-----------|------|-----------|
| [primary] | [value] | [value] | [threshold] |
| [secondary] | [value] | [value] | [threshold] |

### Fairness Assessment
| Subgroup | [Primary Metric] | vs. Overall | Acceptable |
|----------|------------------|-------------|-----------|
| [subgroup] | [value] | [+/- %] | [Yes/No] |

### Limitations
- [Limitation 1 — specific, not vague]
- [Limitation 2]
- [Limitation 3]

### Ethical Considerations
- **Potential harms:** [what could go wrong if predictions are wrong]
- **Mitigations:** [what safeguards are in place]
- **Human oversight:** [where humans are in the loop]

### Recommendations
- **Use this model for:** [appropriate use cases]
- **Do not use this model for:** [inappropriate use cases]
- **Monitor:** [what to watch — reference 6.2]

---

## Project Artifacts Index

| Artifact | Location | Status |
|----------|----------|--------|
| Business Objectives | `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md` | [status] |
| Situation Assessment | `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md` | [status] |
| Data Mining Goals | `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md` | [status] |
| Project Plan | `docs/crisp-dm/1-business-understanding/1.4-project-plan.md` | [status] |
| Data Collection | `docs/crisp-dm/2-data-understanding/2.1-initial-data-collection.md` | [status] |
| Data Description | `docs/crisp-dm/2-data-understanding/2.2-data-description.md` | [status] |
| Data Exploration | `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md` | [status] |
| Data Quality | `docs/crisp-dm/2-data-understanding/2.4-data-quality.md` | [status] |
| Data Selection | `docs/crisp-dm/3-data-preparation/3.1-select-data.md` | [status] |
| Data Cleaning | `docs/crisp-dm/3-data-preparation/3.2-clean-data.md` | [status] |
| Data Construction | `docs/crisp-dm/3-data-preparation/3.3-construct-data.md` | [status] |
| Data Integration | `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md` | [status] |
| Data Formatting | `docs/crisp-dm/3-data-preparation/3.5-format-data.md` | [status] |
| Modeling Techniques | `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md` | [status] |
| Test Design | `docs/crisp-dm/4-modeling/4.2-test-design.md` | [status] |
| Model Building | `docs/crisp-dm/4-modeling/4.3-model-building.md` | [status] |
| Model Assessment | `docs/crisp-dm/4-modeling/4.4-model-assessment.md` | [status] |
| Deployment Plan | `docs/crisp-dm/6-deployment/6.1-plan-deployment.md` | [status] |
| Monitoring Plan | `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md` | [status] |
| Final Report | `docs/crisp-dm/6-deployment/6.3-final-report.md` | [status] |
| Project Review | `docs/crisp-dm/6-deployment/6.4-review-project.md` | [status] |

---

## To Be Clarified

[List any items that need further investigation or stakeholder input. Remove this section if everything is complete.]

---

## Source Documents

All CRISP-DM artifacts from Phases 1-6 (see Project Artifacts Index above).

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Project Manager | | | Pending |
| Business Stakeholder | | | Pending |
| MLOps Engineer | | | Pending |
| Data Protection Officer | | | Pending |
```

### Step 7: Summary and Next Steps

After writing the document, present a summary:

> **Final Report created** at `docs/crisp-dm/6-deployment/6.3-final-report.md`
>
> **Summary:**
> - Executive summary: [business problem, key results, impact]
> - Technical report: [N] phases documented, [N] models evaluated, selected model [technique] with [metric] = [value]
> - Model card: complete with intended use, limitations, fairness assessment
> - Project artifacts: [N] of [total] artifacts completed
>
> **Next step in CRISP-DM:** Proceed to **6.4 Review Project** — conduct a retrospective on the project process, capture lessons learned, and identify improvements for future iterations.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 6.3 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Executive summary is free of technical jargon — a non-technical stakeholder can understand it
- [ ] Business impact is quantified (not just "improved performance")
- [ ] Technical report covers all CRISP-DM phases that were completed
- [ ] All models evaluated are listed with metrics (not just the winner)
- [ ] Model card meets governance requirements (intended use, limitations, fairness)
- [ ] Fairness assessment covers key subgroups
- [ ] Ethical considerations are addressed honestly
- [ ] Technical debt is documented with recommended actions
- [ ] Future recommendations are concrete and prioritized
- [ ] Project artifacts index is complete and status is accurate
- [ ] No PII or sensitive data in the report
- [ ] All source documents are cross-referenced
- [ ] The report is self-contained enough to be understood without reading all source documents
