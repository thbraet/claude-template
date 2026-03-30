---
name: review-process
description: "CRISP-DM 5.2 — Review Process. Conducts a retrospective of the entire data mining process from Phase 1 through Phase 4. Identifies what worked well, what should be improved, methodology gaps, and lessons learned. Produces a structured process review in docs/crisp-dm/5-evaluation/."
argument-hint: "<optional: specific aspect of the process to review, or concern to investigate>"
---

# /review-process — CRISP-DM 5.2: Review Process

> **Phase:** 5. Evaluation | **Task:** 5.2 Review Process
>
> *"At this point, the resultant model appears to be satisfactory and to satisfy business needs. It is now appropriate to do a more thorough review of the data mining engagement in order to determine if there is some important factor or task that has somehow been overlooked."*

## Purpose

This skill performs a structured retrospective of the entire CRISP-DM process. It reviews each phase for completeness, methodology quality, and identifies overlooked factors that could affect deployment. This is the project's quality gate before deciding on next steps.

It produces three outputs:

1. **Phase-by-Phase Review** — assessment of each CRISP-DM phase's execution quality
2. **Methodology Assessment** — evaluation of data science practices, rigor, and potential oversights
3. **Lessons Learned** — actionable insights for this project's continuation and future projects

## Output Location

All artifacts are written to: `docs/crisp-dm/5-evaluation/5.2-review-process.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/5-evaluation/5.2-review-process.md`
- If it exists, present its contents and ask: *"A process review already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if the results evaluation exists:
- Read `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
  - If it exists, use it — its verdict informs the process review.
  - If it does not exist, warn: *"No results evaluation found (task 5.1). It's recommended to evaluate results before reviewing the process. Run `/evaluate-results` first, or proceed with process review only."*

### Step 2: Ingest All Phase Artifacts

Read ALL existing CRISP-DM documents to assess the complete process:

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
- `docs/crisp-dm/4-modeling/4.1-modeling-techniques.md`
- `docs/crisp-dm/4-modeling/4.2-test-design.md`
- `docs/crisp-dm/4-modeling/4.3-model-building.md`
- `docs/crisp-dm/4-modeling/4.4-model-assessment.md`

**Phase 5 — Evaluation:**
- `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`

For each file, note whether it exists, its completeness status, and any "To Be Clarified" items.

### Step 3: Phase-by-Phase Process Review

For each phase, assess:

**Execution Quality:**
- Were all tasks completed? Were any skipped or left incomplete?
- Was the documentation thorough and accurate?
- Were the right questions asked? Were there blind spots?
- Were findings from earlier phases properly carried forward?

**Methodology Rigor:**
- Phase 1: Were business objectives specific and measurable? Were success criteria quantified?
- Phase 2: Was data exploration thorough? Were quality issues fully identified?
- Phase 3: Was data leakage checked? Were transformations fit on training data only? Was feature engineering informed by domain knowledge?
- Phase 4: Was a baseline established first? Were experiments properly tracked? Was the evaluation framework sound?

**Key Decisions:**
- What were the critical decisions in each phase?
- Were they well-documented and justified?
- In hindsight, were they the right decisions?

### Step 4: Cross-Phase Consistency Check

Verify that the work is internally consistent:

- **Goals to metrics:** Do the evaluation metrics (4.2) trace back to the data mining goals (1.3) and business objectives (1.1)?
- **Data quality to cleaning:** Were all quality issues from 2.4 addressed in 3.2?
- **Exploration to features:** Were feature hypotheses from 2.3 implemented in 3.3?
- **Assumptions to validation:** Were data assumptions from 4.1 validated against exploration findings (2.3)?
- **Constraints to implementation:** Were operational constraints from 1.2 respected throughout?

### Step 5: Overlooked Factors Assessment

Systematically check for commonly overlooked issues:

**Data concerns:**
- Was the data representative of the deployment population?
- Were there temporal patterns not captured (regime changes, trend shifts)?
- Were there data sources identified in 1.2 that were never incorporated?
- Were there edge cases or rare events not handled?

**Modeling concerns:**
- Were alternative approaches considered and dismissed with good reason?
- Was the model tested on the most recent data (closest to deployment conditions)?
- Were feature importance results inspected for sensibility?
- Was the prediction horizon realistic for the business use case?

**Business concerns:**
- Were all stakeholders consulted at appropriate stages?
- Were operational constraints fully understood?
- Was the integration path into existing workflows considered?
- Were ethical or fairness considerations addressed?

### Step 6: Present Review Findings and Ask for Confirmation

Present the process review findings to the user:
- Overall process health: Strong / Adequate / Needs Improvement
- Key strengths of the process
- Key gaps or overlooked factors
- Items that should be revisited before deployment

Ask the user:
1. **Are there aspects of the process I've missed in this review?**
2. **Were there informal decisions or conversations not captured in documentation?**
3. **Are there known shortcuts or compromises made during the project?**

Wait for the user's response before continuing.

### Step 7: Clarification Round (if needed)

If the user's response reveals additional process issues:
- Incorporate them into the review
- Maximum 2 clarification rounds — after that, mark remaining items as "TBD"

### Step 8: Generate the Output Document

Create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/5-evaluation
```

Write the file `docs/crisp-dm/5-evaluation/5.2-review-process.md` using this template:

```markdown
# 5.2 Review Process

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 5. Evaluation
> **Status:** Draft | Review | Approved

---

## Review Overview

- **Review Date:** [date]
- **Phases Reviewed:** 1 through 4 (+ 5.1 if available)
- **Documents Assessed:** [N] of [M] expected artifacts exist
- **Overall Process Health:** [Strong / Adequate / Needs Improvement]
- **Results Evaluation Verdict (5.1):** [Ready / Conditionally Ready / Not Ready / Not Yet Evaluated]

---

## Phase-by-Phase Review

### Phase 1: Business Understanding

| Task | Status | Quality | Issues |
|------|--------|---------|--------|
| 1.1 Business Objectives | [Complete/Incomplete/Missing] | [Strong/Adequate/Weak] | [issues or "None"] |
| 1.2 Situation Assessment | [Complete/Incomplete/Missing] | [Strong/Adequate/Weak] | [issues or "None"] |
| 1.3 Data Mining Goals | [Complete/Incomplete/Missing] | [Strong/Adequate/Weak] | [issues or "None"] |
| 1.4 Project Plan | [Complete/Incomplete/Missing] | [Strong/Adequate/Weak] | [issues or "None"] |

**Phase Assessment:** [summary paragraph — was the business problem well-defined? Were success criteria specific enough?]

**Key Decisions:**
- [decision 1 — and whether it held up]
- [decision 2]

### Phase 2: Data Understanding

| Task | Status | Quality | Issues |
|------|--------|---------|--------|
| 2.1 Data Collection | [status] | [quality] | [issues] |
| 2.2 Data Description | [status] | [quality] | [issues] |
| 2.3 Data Exploration | [status] | [quality] | [issues] |
| 2.4 Data Quality | [status] | [quality] | [issues] |

**Phase Assessment:** [summary paragraph — was the data well-understood? Were quality issues identified early enough?]

**Key Decisions:**
- [decision 1]

### Phase 3: Data Preparation

| Task | Status | Quality | Issues |
|------|--------|---------|--------|
| 3.1 Select Data | [status] | [quality] | [issues] |
| 3.2 Clean Data | [status] | [quality] | [issues] |
| 3.3 Construct Data | [status] | [quality] | [issues] |
| 3.4 Integrate Data | [status] | [quality] | [issues] |
| 3.5 Format Data | [status] | [quality] | [issues] |

**Phase Assessment:** [summary paragraph — was data preparation rigorous? Was leakage avoided?]

**Key Decisions:**
- [decision 1]

### Phase 4: Modeling

| Task | Status | Quality | Issues |
|------|--------|---------|--------|
| 4.1 Modeling Techniques | [status] | [quality] | [issues] |
| 4.2 Test Design | [status] | [quality] | [issues] |
| 4.3 Model Building | [status] | [quality] | [issues] |
| 4.4 Model Assessment | [status] | [quality] | [issues] |

**Phase Assessment:** [summary paragraph — was modeling systematic? Was the baseline established?]

**Key Decisions:**
- [decision 1]

---

## Cross-Phase Consistency

| Check | Status | Finding |
|-------|--------|---------|
| Business objectives → evaluation metrics | [Consistent / Gap Found] | [details] |
| Data quality issues → cleaning actions | [Consistent / Gap Found] | [details] |
| Exploration hypotheses → engineered features | [Consistent / Gap Found] | [details] |
| Technique assumptions → data validation | [Consistent / Gap Found] | [details] |
| Operational constraints → implementation | [Consistent / Gap Found] | [details] |
| Data mining goals → model assessment criteria | [Consistent / Gap Found] | [details] |

### Gaps Identified
[For each gap found, describe the inconsistency and its potential impact]

---

## Overlooked Factors

### Data Concerns
| # | Factor | Severity | Description | Recommendation |
|---|--------|----------|-------------|----------------|
| 1 | [factor] | [Critical/Major/Minor] | [what was overlooked] | [what to do about it] |

### Modeling Concerns
| # | Factor | Severity | Description | Recommendation |
|---|--------|----------|-------------|----------------|
| 1 | [factor] | [Critical/Major/Minor] | [what was overlooked] | [what to do about it] |

### Business Concerns
| # | Factor | Severity | Description | Recommendation |
|---|--------|----------|-------------|----------------|
| 1 | [factor] | [Critical/Major/Minor] | [what was overlooked] | [what to do about it] |

---

## Methodology Assessment

### What Worked Well
1. [strength — e.g., "Thorough data exploration caught a critical join key mismatch before modeling"]
2. [strength]
3. [strength]

### What Should Be Improved
1. [weakness — e.g., "Feature engineering was not informed by domain expert input; some obvious retail features were missed"]
2. [weakness]
3. [weakness]

### Process Shortcuts or Compromises
| # | Shortcut | Phase | Impact | Acceptable? |
|---|----------|-------|--------|-------------|
| 1 | [what was skipped or simplified] | [phase] | [effect on results] | [Yes/No — with justification] |

---

## Lessons Learned

### For This Project
1. [lesson that should inform Phase 6 decisions — e.g., "The model performs poorly on new stores; deployment should exclude stores open < 6 months"]
2. [lesson]

### For Future Projects
1. [lesson that applies beyond this project — e.g., "Start stakeholder alignment earlier; waiting until Phase 5 caused rework"]
2. [lesson]

---

## Recommended Actions Before Proceeding

| # | Action | Priority | Phase to Revisit | Effort |
|---|--------|----------|------------------|--------|
| 1 | [action needed] | [Critical/High/Medium/Low] | [phase number or "N/A"] | [Small/Medium/Large] |

**Verdict:** [Proceed to 5.3 / Address critical actions first]

---

## To Be Clarified

[List any review questions that could not be answered. Remove this section if everything is complete.]

---

## Source Documents

[List all documents that were reviewed, with their completeness status]

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Project Manager | | | Pending |
| Domain Expert | | | Pending |
```

### Step 9: Summary and Next Steps

After writing the document, present a summary:

> **Process Review created** at `docs/crisp-dm/5-evaluation/5.2-review-process.md`
>
> **Summary:**
> - Overall process health: [Strong / Adequate / Needs Improvement]
> - Documents assessed: [N]/[M] artifacts exist
> - Cross-phase consistency: [N] gaps found
> - Overlooked factors: [N] identified ([N] critical)
> - [N] recommended actions before proceeding
>
> **Next step in CRISP-DM:** Run `/determine-next-steps` to decide whether to deploy, iterate, or revise the project (Task 5.3).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 5.2 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] All existing CRISP-DM documents were reviewed
- [ ] Each phase is assessed for execution quality and methodology rigor
- [ ] Cross-phase consistency is checked systematically
- [ ] Overlooked factors cover data, modeling, and business dimensions
- [ ] Lessons learned are actionable, not generic
- [ ] Recommended actions are prioritized and specific
- [ ] Process shortcuts or compromises are documented honestly
- [ ] The review is objective — acknowledging strengths, not just weaknesses
- [ ] No PII in the document
- [ ] Source documents are referenced for traceability
