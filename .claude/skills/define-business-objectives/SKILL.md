---
name: define-business-objectives
description: "CRISP-DM 1.1 — Determine Business Objectives. Guides the user through defining the business background, objectives, and success criteria for a data mining project. Produces a structured business objectives document in docs/crisp-dm/1-business-understanding/."
argument-hint: "[optional: project name or business problem description]"
---

# /define-business-objectives — CRISP-DM 1.1: Determine Business Objectives

> **Phase:** 1. Business Understanding | **Task:** 1.1 Determine Business Objectives
>
> *"The first objective of the data analyst is to thoroughly understand, from a business perspective, what the client really wants to accomplish. A possible consequence of neglecting this step is to expend a great deal of effort producing the right answers to the wrong questions."*

## Purpose

This skill guides the user through the first and most critical task of any CRISP-DM project: understanding and documenting the business objectives. It produces three outputs:

1. **Background** — organizational context, problem area, and current solution
2. **Business Objectives** — precisely stated business questions and expected benefits
3. **Business Success Criteria** — measurable criteria for a successful outcome

## Output Location

All artifacts are written to: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- If it exists, present its contents and ask: *"A business objectives document already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

### Step 2: Gather Background Information

Ask the user the following questions **one section at a time**. Do not dump all questions at once — have a conversation.

#### 2a: Organization Context

Ask:
> I need to understand the organizational context for this project. Please tell me:
>
> 1. **Which business unit / department** is sponsoring this project? (e.g., Marketing, Supply Chain, Finance, Store Operations)
> 2. **Who is the internal sponsor?** (the person funding or championing this)
> 3. **Who are the key stakeholders** who will use the results?
> 4. **Is the organization already familiar with data mining/ML**, or is this a first initiative?

Wait for the user's response before continuing.

#### 2b: Problem Area

Ask:
> Now let's define the problem area:
>
> 1. **What problem or opportunity** are we trying to address? (describe in general terms)
> 2. **What is the current status** — is this a new initiative or continuation of prior work?
> 3. **What motivated this project?** (e.g., business pain point, strategic initiative, regulatory requirement)
> 4. **Who is the target group** for the project results? (e.g., store managers, category managers, executive team)

Wait for the user's response before continuing.

#### 2c: Current Solution

Ask:
> How is this problem handled today?
>
> 1. **What solution is currently in place?** (e.g., manual process, rule-based system, existing model, Excel-based)
> 2. **What are its strengths and weaknesses?**
> 3. **How well is the current solution accepted** by its users?

Wait for the user's response before continuing.

### Step 3: Define Business Objectives

Ask:
> Let's now formulate the business objectives precisely:
>
> 1. **What is the primary business objective?** (one sentence, e.g., "Reduce fresh product waste by 15% across Belgian stores")
> 2. **What specific business questions** should this project answer? (list as many as relevant)
> 3. **Are there any constraints** the business has stated? (e.g., "must not reduce product availability", "must be explainable to store managers")
> 4. **What are the expected benefits** in business terms? (e.g., cost savings, revenue increase, efficiency gain)

**Important:** If objectives sound unattainable, gently challenge them and help reformulate into realistic goals.

Wait for the user's response before continuing.

### Step 4: Define Business Success Criteria

Ask:
> Finally, let's define how success will be measured from a business perspective:
>
> 1. **What specific, measurable criteria** determine if this project is successful? (e.g., "reduce churn rate by 10%", "achieve 20% improvement in forecast accuracy")
> 2. **Who will assess** whether these criteria are met?
> 3. **What is the timeframe** for achieving these results?

**Important:** Each success criterion must map to at least one of the business objectives defined above. Validate this mapping explicitly.

Wait for the user's response before continuing.

### Step 5: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/1-business-understanding
```

Write the file `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md` using this template:

```markdown
# 1.1 Business Objectives

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 1. Business Understanding
> **Status:** Draft | Review | Approved

---

## Background

### Organization Context
- **Sponsoring Unit:** [department]
- **Internal Sponsor:** [name, role]
- **Key Stakeholders:** [list]
- **Data Mining Maturity:** [description]

### Problem Area
- **Problem Domain:** [domain]
- **Problem Description:** [description]
- **Project Status:** [new / continuation]
- **Motivation:** [what triggered this]
- **Target Group:** [who will use results]

### Current Solution
- **Current Approach:** [description]
- **Strengths:** [list]
- **Weaknesses:** [list]
- **User Acceptance:** [level]

---

## Business Objectives

### Primary Objective
[one clear sentence]

### Business Questions
1. [question 1]
2. [question 2]
3. [...]

### Constraints
- [constraint 1]
- [constraint 2]

### Expected Benefits
- [benefit 1]
- [benefit 2]

---

## Business Success Criteria

| # | Criterion | Related Objective | Assessor | Timeframe |
|---|-----------|-------------------|----------|-----------|
| 1 | [measurable criterion] | [which objective] | [who assesses] | [when] |
| 2 | ... | ... | ... | ... |

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Sponsor | | | Pending |
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 6: Summary and Next Steps

After writing the document, present a summary:

> **Business Objectives document created** at `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
>
> **Summary:**
> - Primary objective: [restate]
> - [N] business questions defined
> - [N] success criteria defined
>
> **Next step in CRISP-DM:** Run `/assess-situation` to inventory resources, constraints, risks, and costs (Task 1.2).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to mark "Business Understanding" as "In Progress" if it was "Not Started".

## Quality Checks

Before finalizing the document, verify:
- [ ] Every success criterion is measurable (has a number or clear threshold)
- [ ] Every success criterion maps to at least one business objective
- [ ] Objectives are realistic and achievable
- [ ] The problem description is clear enough for someone outside the team to understand
- [ ] No PII or sensitive data is included in the document
