---
name: evaluate-results
description: "CRISP-DM 5.1 — Evaluate Results. Assesses model results against business objectives and success criteria established in Phase 1. Determines whether the model genuinely solves the business problem, identifies residual risks, and produces a structured evaluation report in docs/crisp-dm/5-evaluation/."
argument-hint: "<optional: specific business question to evaluate against, or stakeholder concern>"
---

# /evaluate-results — CRISP-DM 5.1: Evaluate Results

> **Phase:** 5. Evaluation | **Task:** 5.1 Evaluate Results
>
> *"Evaluate the degree to which the model meets the business objectives and seek to determine if there is some business reason why this model is deficient. Compare results with the evaluation criteria defined at the start of the project."*

## Purpose

This skill bridges the gap between technical model assessment (Phase 4) and business decision-making. While task 4.4 evaluates models on technical metrics, task 5.1 evaluates whether the model actually solves the business problem. It answers: "Does this model deliver enough value to justify deployment?"

It produces three outputs:

1. **Business Objective Alignment** — systematic check of each business objective from 1.1 against model capabilities
2. **Success Criteria Evaluation** — formal pass/fail assessment against each business success criterion
3. **Risk & Limitation Assessment** — residual risks, failure modes, and conditions under which the model should not be trusted

## Output Location

All artifacts are written to: `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
- If it exists, present its contents and ask: *"An evaluation report already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check prerequisite documents:
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — it defines the business objectives and success criteria to evaluate against. This is the primary reference.
  - If it does not exist, warn: *"No business objectives found (task 1.1). Evaluation requires knowing the business success criteria. Run `/define-business-objectives` first."*
- Read `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
  - If it exists, use it — it maps business objectives to technical metrics.
- Read `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
  - If it exists, use it — it contains the technical assessment and recommended model(s).
  - If it does not exist, warn: *"No model assessment found (task 4.4). There are no assessed models to evaluate. Complete Phase 4 first."*
- Read `docs/crisp-dm/4-modeling/4.3-model-building.md`
  - If it exists, use it — it contains model performance details and MLflow references.
- Read `docs/crisp-dm/4-modeling/4.2-test-design.md`
  - If it exists, use it — it defines the evaluation framework and business metric translations.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — it documents constraints, risks, and stakeholder requirements.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Business objectives** (from 1.1) — what the business needs the model to do
- **Business success criteria** (from 1.1) — measurable thresholds for success
- **Data mining success criteria** (from 1.3) — technical metric thresholds
- **Business-to-technical mapping** (from 1.3/4.2) — how technical metrics translate to business outcomes
- **Model performance** (from 4.3/4.4) — what the recommended model(s) actually achieved
- **Known limitations** (from 4.4) — where models fail, underperforming segments
- **Constraints** (from 1.2) — operational, technical, and organizational constraints
- **Stakeholder requirements** (from 1.1/1.2) — who needs what from the model

Present what was extracted and what is missing. Ask the user to fill gaps.

### Step 3: Business Objective Alignment

For each business objective from 1.1, systematically evaluate:

| Business Objective | Model Capability | Evidence | Gap | Verdict |
|---|---|---|---|---|
| [objective from 1.1] | [what the model can/cannot do for this] | [metric/result from 4.3/4.4] | [what's missing or insufficient] | [Met / Partially Met / Not Met] |

For each objective rated "Partially Met" or "Not Met":
- Explain what would be needed to fully meet it
- Assess whether the gap is addressable (more data, better features, different model) or fundamental (wrong problem framing, insufficient data)
- Estimate the effort to close the gap

### Step 4: Business Success Criteria Assessment

For each business success criterion from 1.1, perform a formal pass/fail:

| Criterion | Threshold | Achieved | Pass/Fail | Notes |
|---|---|---|---|---|
| [criterion from 1.1] | [threshold] | [actual value] | [Pass/Fail] | [context] |

Calculate the overall pass rate and determine:
- **All criteria passed** — model is ready for deployment consideration
- **Critical criteria failed** — model is not ready; identify what must improve
- **Non-critical criteria failed** — model may be deployable with documented limitations

### Step 5: Risk & Limitation Assessment

Document residual risks that could affect deployment:

**Operational risks:**
- What happens when the model is wrong? What is the cost of errors?
- Are there scenarios where the model should not be used?
- How does model performance degrade over time (data drift, concept drift)?
- What is the fallback if the model fails?

**Data risks:**
- Does the model depend on data sources that may become unavailable?
- Are there data quality issues that could worsen in production?
- Does the training data adequately represent future conditions?

**Business risks:**
- Does the model create any compliance or privacy concerns?
- Could the model produce outputs that are unfair or biased across stores/regions?
- What is the reputational risk if the model performs poorly?

**Organizational risks:**
- Does the team have the capability to maintain the model?
- Is there stakeholder buy-in for using model-driven decisions?
- Does the model fit into existing workflows?

### Step 6: Stakeholder Readiness Assessment

Evaluate whether key stakeholders are ready for the model:

| Stakeholder | Role | Needs | Model Meets Needs? | Concerns | Ready? |
|---|---|---|---|---|---|
| [stakeholder] | [role] | [what they need from the model] | [Yes/Partially/No] | [concerns raised] | [Yes/No/TBD] |

If stakeholder input has not been gathered, flag this as a required action.

### Step 7: Present Evaluation Summary and Ask for Confirmation

Present the evaluation findings to the user:
- Overall verdict: Ready / Conditionally Ready / Not Ready
- Key strengths of the model
- Key gaps and risks
- Recommended conditions or limitations for deployment

Ask the user:
1. **Does this evaluation align with your understanding?**
2. **Are there business considerations I've missed?**
3. **Have stakeholders reviewed the model results?**

Wait for the user's response before continuing.

### Step 8: Clarification Round (if needed)

If the user's response reveals gaps:
- Ask a focused follow-up covering only the remaining questions
- Maximum 2 clarification rounds — after that, mark remaining items as "TBD"

### Step 9: Generate the Output Document

Create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/5-evaluation
```

Write the file `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md` using this template:

```markdown
# 5.1 Evaluate Results

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 5. Evaluation
> **Status:** Draft | Review | Approved

---

## Evaluation Overview

- **Model(s) Evaluated:** [from 4.4 recommendation]
- **Evaluation Date:** [date]
- **Business Objectives Reference:** `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- **Model Assessment Reference:** `docs/crisp-dm/4-modeling/4.4-model-assessment.md`
- **Overall Verdict:** [Ready / Conditionally Ready / Not Ready]

---

## Business Objective Alignment

| # | Business Objective | Model Capability | Evidence | Gap | Verdict |
|---|---|---|---|---|---|
| 1 | [objective] | [capability] | [metric/result] | [gap or "None"] | [Met / Partially Met / Not Met] |

### Objectives Fully Met
[Summary of objectives the model satisfies, with supporting evidence]

### Objectives Partially Met
[For each partially met objective: what's achieved, what's missing, and what it would take to close the gap]

### Objectives Not Met
[For each unmet objective: why, whether it's addressable, and recommended path forward]

---

## Business Success Criteria Assessment

| # | Criterion | Threshold | Achieved | Pass/Fail | Notes |
|---|---|---|---|---|---|
| 1 | [criterion] | [threshold] | [actual] | [Pass/Fail] | [context] |

**Overall:** [N]/[M] criteria passed

### Critical Criteria Status
[List criteria that are must-pass for deployment, and their status]

### Non-Critical Criteria Status
[List criteria that are desirable but not blocking, and their status]

---

## Business Impact Assessment

### Value Delivered
- **Primary value:** [what the model enables in business terms]
- **Quantified benefit:** [e.g., "X hours of workforce planning effort saved per week across Y stores"]
- **Improvement over current process:** [how the model compares to the existing approach]

### Cost of Errors
| Error Type | Frequency | Business Impact | Mitigation |
|---|---|---|---|
| Over-prediction | [how often] | [consequence — e.g., overstaffing cost] | [how to handle] |
| Under-prediction | [how often] | [consequence — e.g., understaffing, missed deliveries] | [how to handle] |

### Net Assessment
[One paragraph: does the value delivered outweigh the costs and risks? Is the model a net positive for the business?]

---

## Risk & Limitation Assessment

### Operational Risks
| Risk | Likelihood | Impact | Mitigation | Residual Risk |
|---|---|---|---|---|
| [risk] | [High/Medium/Low] | [High/Medium/Low] | [mitigation plan] | [Acceptable/Needs Attention] |

### Data Risks
| Risk | Likelihood | Impact | Mitigation | Residual Risk |
|---|---|---|---|---|
| [risk] | [High/Medium/Low] | [High/Medium/Low] | [mitigation plan] | [Acceptable/Needs Attention] |

### Business Risks
| Risk | Likelihood | Impact | Mitigation | Residual Risk |
|---|---|---|---|---|
| [risk] | [High/Medium/Low] | [High/Medium/Low] | [mitigation plan] | [Acceptable/Needs Attention] |

### Conditions for Model Use
[List specific conditions under which the model should and should not be used — e.g., "Do not use for stores open less than 6 months (insufficient training data)"]

---

## Stakeholder Readiness

| Stakeholder | Role | Needs Met? | Concerns | Sign-off Status |
|---|---|---|---|---|
| [name/role] | [role] | [Yes/Partially/No] | [concerns] | [Pending/Approved] |

### Outstanding Stakeholder Actions
[List any stakeholder reviews, approvals, or inputs still needed]

---

## Overall Verdict

### Assessment: [Ready / Conditionally Ready / Not Ready]

**Justification:** [2-3 sentences summarizing why this verdict]

**Strengths:**
1. [key strength]
2. [key strength]

**Weaknesses:**
1. [key weakness]
2. [key weakness]

**Conditions for Deployment** (if Conditionally Ready):
1. [condition that must be met]
2. [condition that must be met]

**Blocking Issues** (if Not Ready):
1. [issue that must be resolved]
2. [issue that must be resolved]

---

## To Be Clarified

[List any evaluation questions that could not be answered. Remove this section if everything is complete.]

---

## Source Documents

- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- 1.3 Data Mining Goals: `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- 4.2 Test Design: `docs/crisp-dm/4-modeling/4.2-test-design.md`
- 4.3 Model Building: `docs/crisp-dm/4-modeling/4.3-model-building.md`
- 4.4 Model Assessment: `docs/crisp-dm/4-modeling/4.4-model-assessment.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Business Sponsor | | | Pending |
| Domain Expert | | | Pending |
| Lead Data Scientist | | | Pending |
| Operations Lead | | | Pending |
```

### Step 10: Summary and Next Steps

After writing the document, present a summary:

> **Evaluation Report created** at `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
>
> **Summary:**
> - Overall verdict: [Ready / Conditionally Ready / Not Ready]
> - Business objectives: [N]/[M] met, [N] partially met, [N] not met
> - Success criteria: [N]/[M] passed
> - [N] risks identified ([N] acceptable, [N] need attention)
> - [N] stakeholder sign-offs pending
>
> **Next step in CRISP-DM:** Run `/review-process` to review the entire data mining process and identify lessons learned (Task 5.2).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 5.1 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Every business objective from 1.1 is evaluated with a clear verdict
- [ ] Every business success criterion from 1.1 has a formal pass/fail assessment
- [ ] Business impact is quantified in stakeholder-understandable terms
- [ ] Risk assessment covers operational, data, and business dimensions
- [ ] Conditions for model use (and non-use) are explicitly stated
- [ ] Stakeholder readiness is assessed — not just technical readiness
- [ ] The overall verdict is justified and connects to the evidence
- [ ] Deployment conditions (if conditionally ready) are specific and actionable
- [ ] No PII in the document
- [ ] Source documents are referenced for traceability
