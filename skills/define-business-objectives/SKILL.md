---
name: define-business-objectives
description: "CRISP-DM 1.1 — Determine Business Objectives. Extracts business context from meeting notes, Notion pages, or other source documents, then fills gaps interactively. Produces a structured business objectives document in docs/crisp-dm/1-business-understanding/."
argument-hint: "<path to meeting notes, Notion page URL, or project description>"
---

# /define-business-objectives — CRISP-DM 1.1: Determine Business Objectives

> **Phase:** 1. Business Understanding | **Task:** 1.1 Determine Business Objectives
>
> *"The first objective of the data analyst is to thoroughly understand, from a business perspective, what the client really wants to accomplish. A possible consequence of neglecting this step is to expend a great deal of effort producing the right answers to the wrong questions."*

## Purpose

This skill extracts as much information as possible from source documents (meeting notes, intake call transcripts, Notion pages, etc.) and then asks the user only about what's missing. It produces three outputs:

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

### Step 2: Ingest Source Documents

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** (e.g., `docs/meeting-notes.md`, `notes/intake-call.txt`) — Read the file(s)
- **Notion page URL** — Fetch via the Notion MCP tools (`mcp__notion__API-retrieve-a-page`, `mcp__notion__API-get-block-children`)
- **Pasted text** — Use the text directly from the conversation
- **No input provided** — Ask: *"Do you have meeting notes, an intake call transcript, or any other document I can extract from? You can provide a file path, a Notion URL, or paste the text directly. If not, I'll guide you through the questions manually."*

Read ALL provided sources before proceeding.

### Step 3: Extract and Map Information

After reading the source documents, map every piece of information to the required fields below. Use this checklist internally:

**Section A — Organization Context:**
- [ ] Sponsoring business unit / department
- [ ] Internal sponsor (name and role)
- [ ] Key stakeholders (names, roles)
- [ ] Organization's data mining / ML maturity

**Section B — Problem Area:**
- [ ] Problem or opportunity description
- [ ] Project status (new vs. continuation)
- [ ] Motivation / trigger for the project
- [ ] Target group for results

**Section C — Current Solution:**
- [ ] Current approach in place
- [ ] Strengths of current approach
- [ ] Weaknesses of current approach
- [ ] User acceptance level

**Section D — Business Objectives:**
- [ ] Primary business objective (one sentence)
- [ ] Specific business questions
- [ ] Business constraints
- [ ] Expected benefits

**Section E — Business Success Criteria:**
- [ ] Measurable success criteria (with numbers/thresholds)
- [ ] Who assesses success
- [ ] Timeframe for results

### Step 4: Present Extracted Information and Ask About Gaps

Present what was extracted in a structured summary, organized by section. For each field, show one of:
- **Extracted:** the value found in the source document(s), with a quote or reference
- **Missing:** flag it clearly

Then ask the user to:
1. **Confirm or correct** the extracted information
2. **Fill in the missing fields**

Format the ask like this:

> Here's what I extracted from your [meeting notes / Notion page / transcript]. Please review and fill in the gaps:
>
> **Organization Context**
> - Sponsoring Unit: *[extracted value]* ✓
> - Internal Sponsor: *[extracted value]* ✓
> - Key Stakeholders: **MISSING** — Who are the key stakeholders?
> - Data Mining Maturity: *[extracted value]* ✓
>
> **Problem Area**
> - Problem Description: *[extracted value]* ✓
> - ...
>
> **[continue for all sections]**
>
> Please confirm the extracted items are correct and provide the missing ones.

**Important rules for this step:**
- Ask about ALL missing fields in a single message — do not split into multiple rounds for gaps
- If a field is ambiguous in the source, present your best interpretation and ask for confirmation
- If objectives sound unattainable, flag them and suggest realistic alternatives
- If success criteria are vague (no numbers), explicitly ask for measurable thresholds

Wait for the user's response before continuing.

### Step 5: Clarification Round (if needed)

If the user's response still has gaps or ambiguities:
- Ask a focused follow-up covering only the remaining gaps
- Maximum 2 clarification rounds — after that, mark remaining gaps as "TBD" in the document and note them in a "To be clarified" section

### Step 6: Generate the Output Document

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

## To Be Clarified

[List any items that could not be determined from the source documents or user input. Remove this section if everything is complete.]

---

## Source Documents

- [List the meeting notes, Notion pages, or other sources used to produce this document]

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Sponsor | | | Pending |
| Domain Expert | | | Pending |
| Data Scientist | | | Pending |
```

### Step 7: Summary and Next Steps

After writing the document, present a summary:

> **Business Objectives document created** at `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
>
> **Summary:**
> - Primary objective: [restate]
> - [N] business questions defined
> - [N] success criteria defined
> - [N] items still to be clarified (if any)
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
