---
name: assess-situation
description: "CRISP-DM 1.2 — Assess Situation. Extracts resource inventories, requirements, risks, terminology, and cost-benefit information from source documents, then fills gaps interactively. Produces a structured situation assessment in docs/crisp-dm/1-business-understanding/."
argument-hint: "<path to meeting notes, Notion page URL, or project description>"
---

# /assess-situation — CRISP-DM 1.2: Assess Situation

> **Phase:** 1. Business Understanding | **Task:** 1.2 Assess Situation
>
> *"This task involves more detailed fact-finding about all of the resources, constraints, assumptions, and other factors that should be considered in determining the data analysis goal and project plan."*

## Purpose

This skill extracts as much information as possible from source documents (meeting notes, intake call transcripts, Notion pages, the 1.1 business objectives document, etc.) and then asks the user only about what's missing. It produces five outputs:

1. **Inventory of Resources** — hardware, data sources, knowledge sources, personnel
2. **Requirements, Assumptions & Constraints** — scheduling, accuracy, legal, budget, data access
3. **Risks & Contingencies** — business, organizational, financial, technical, and data risks with contingency plans
4. **Terminology** — business glossary and data mining glossary
5. **Costs & Benefits** — data collection, development, operating costs, and expected benefits

## Output Location

All artifacts are written to: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- If it exists, present its contents and ask: *"A situation assessment already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Also check if the 1.1 business objectives document exists:
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- If it exists, use it as an additional source — it contains stakeholders, constraints, and problem context that feed directly into the situation assessment.
- If it does not exist, warn the user: *"No business objectives document found (task 1.1). It's recommended to complete 1.1 first — proceed anyway?"*

### Step 2: Ingest Source Documents

Check if the user provided a reference (via `$ARGUMENTS` or in conversation):

- **File path** (e.g., `docs/meeting-notes.md`, `notes/intake-call.txt`) — Read the file(s)
- **Notion page URL** — Fetch via the Notion MCP tools (`mcp__notion__API-retrieve-a-page`, `mcp__notion__API-get-block-children`)
- **Pasted text** — Use the text directly from the conversation
- **No input provided** — Ask: *"Do you have meeting notes, an intake call transcript, or any other document I can extract from? You can provide a file path, a Notion URL, or paste the text directly. If not, I'll guide you through the questions manually."*

Read ALL provided sources (including the 1.1 document if available) before proceeding.

### Step 3: Extract and Map Information

After reading the source documents, map every piece of information to the required fields below. Use this checklist internally:

**Section A — Hardware Resources:**
- [ ] Base hardware available (compute, storage, GPUs)
- [ ] Hardware availability and scheduling conflicts
- [ ] Data mining tool hardware requirements

**Section B — Data Sources & Knowledge:**
- [ ] Data sources with types (databases, files, APIs, live vs. extract)
- [ ] Knowledge sources (domain experts, documentation, prior analyses)
- [ ] Available tools and techniques
- [ ] Relevant background knowledge

**Section C — Personnel:**
- [ ] Project sponsor
- [ ] System/database administrators and technical support
- [ ] Data mining experts, statisticians, data scientists
- [ ] Domain experts and their availability for later phases

**Section D — Requirements:**
- [ ] Target group profile (who will use results)
- [ ] Schedule requirements and deadlines
- [ ] Comprehensibility, accuracy, deployability requirements
- [ ] Security, legal, and privacy requirements
- [ ] Reporting requirements

**Section E — Assumptions:**
- [ ] Assumptions on data quality (accuracy, availability, completeness)
- [ ] Assumptions on external factors (economic, competitive, technical)
- [ ] Assumptions on model interpretability needs
- [ ] Starting-point assumptions (what was taken for granted at project kick-off)

**Section F — Constraints:**
- [ ] Legal and regulatory constraints (GDPR, data protection)
- [ ] Budget constraints (fixed costs, implementation costs)
- [ ] Timeline constraints
- [ ] Data access constraints (permissions, passwords, technical format)
- [ ] Resource constraints (staffing, availability)

**Section G — Risks & Contingencies:**
- [ ] Business risks (e.g., competitor beats us to solution)
- [ ] Organizational risks (e.g., sponsoring department loses funding)
- [ ] Financial risks (e.g., continued funding depends on initial results)
- [ ] Technical risks (e.g., infrastructure, tool limitations)
- [ ] Data risks (e.g., poor quality, insufficient coverage, access issues)
- [ ] Contingency plan for each identified risk

**Section H — Terminology:**
- [ ] Business terms specific to this domain/project
- [ ] Data mining terms relevant to this project (with business-context examples)

**Section I — Costs & Benefits:**
- [ ] Data collection costs
- [ ] Development and implementation costs
- [ ] Operating costs (ongoing maintenance, retraining, infrastructure)
- [ ] Hidden costs (repeated data extraction, workflow changes, training)
- [ ] Expected benefits when deployed (ROI, efficiency gains, cost savings)

### Step 4: Present Extracted Information and Ask About Gaps

Present what was extracted in a structured summary, organized by section. For each field, show one of:
- **Extracted:** the value found in the source document(s), with a quote or reference
- **Inferred from 1.1:** the value carried over from the business objectives document
- **Missing:** flag it clearly

Then ask the user to:
1. **Confirm or correct** the extracted information
2. **Fill in the missing fields**

Format the ask like this:

> Here's what I extracted from your [meeting notes / Notion page / transcript / 1.1 business objectives]. Please review and fill in the gaps:
>
> **Hardware Resources**
> - Base Hardware: **MISSING** — What compute resources are available?
> - Hardware Availability: **MISSING**
>
> **Data Sources & Knowledge**
> - Data Sources: *Guido Kuylit CSV (6y history), ODCF, ASB, Plato, Sales Forecast* ✓ (from 1.1)
> - Knowledge Sources: **MISSING** — Are there prior analyses or domain documentation?
> - ...
>
> **[continue for all sections]**
>
> Please confirm the extracted items are correct and provide the missing ones.

**Important rules for this step:**
- Ask about ALL missing fields in a single message — do not split into multiple rounds for gaps
- If a field is ambiguous in the source, present your best interpretation and ask for confirmation
- If risks seem incomplete, suggest common data science project risks relevant to the domain
- If costs are unknown, ask for rough order-of-magnitude estimates rather than exact figures

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

Write the file `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md` using this template:

```markdown
# 1.2 Situation Assessment

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 1. Business Understanding
> **Status:** Draft | Review | Approved

---

## Inventory of Resources

### Hardware Resources
| Resource | Description | Availability | Notes |
|----------|-------------|--------------|-------|
| [resource] | [description] | [availability] | [notes] |

### Data Sources
| Source | Type | Format | Access Method | Refresh | Volume | Quality Notes |
|--------|------|--------|---------------|---------|--------|---------------|
| [source] | [DB/API/File] | [format] | [how to access] | [frequency] | [size] | [known issues] |

### Knowledge Sources
| Source | Type | Contact / Location | Relevance |
|--------|------|-------------------|-----------|
| [source] | [Expert/Doc/Prior Analysis] | [who/where] | [what it covers] |

### Personnel
| Role | Name | Availability | Notes |
|------|------|-------------|-------|
| Project Sponsor | [name] | [availability] | |
| Domain Expert | [name] | [availability] | |
| Data Scientist | [name] | [availability] | |
| Technical Support | [name] | [availability] | |

---

## Requirements, Assumptions & Constraints

### Requirements
- **Target Group:** [who will consume the results]
- **Schedule:** [deadlines and milestones]
- **Accuracy:** [required accuracy / acceptable error margin]
- **Comprehensibility:** [must the model be explainable?]
- **Deployability:** [how will results be delivered — API, dashboard, report, integration?]
- **Security & Privacy:** [GDPR, data classification, access controls]
- **Reporting:** [what reports are expected and how often]

### Assumptions
| # | Assumption | Category | Impact if Wrong |
|---|-----------|----------|-----------------|
| 1 | [assumption] | [Data Quality / External / Model / Starting Point] | [what happens if false] |

### Constraints
| # | Constraint | Type | Mitigation |
|---|-----------|------|------------|
| 1 | [constraint] | [Legal / Budget / Timeline / Data Access / Resource] | [how to work within it] |

---

## Risks & Contingencies

| # | Risk | Category | Likelihood | Impact | Contingency Plan |
|---|------|----------|------------|--------|------------------|
| 1 | [risk description] | [Business / Organizational / Financial / Technical / Data] | [Low/Medium/High] | [Low/Medium/High] | [contingency] |

---

## Terminology

### Business Glossary
| Term | Definition | Example |
|------|-----------|---------|
| [term] | [definition in project context] | [concrete example] |

### Data Mining Glossary
| Term | Definition | Business Context Example |
|------|-----------|------------------------|
| [term] | [definition] | [example relevant to this project] |

---

## Costs & Benefits

### Costs
| Category | Item | Estimated Cost | Notes |
|----------|------|---------------|-------|
| Data Collection | [item] | [cost or effort] | [notes] |
| Development | [item] | [cost or effort] | [notes] |
| Operating | [item] | [cost or effort] | [notes] |
| Hidden | [item] | [cost or effort] | [notes] |

### Expected Benefits
| Benefit | Type | Estimated Value | Timeframe |
|---------|------|----------------|-----------|
| [benefit] | [Efficiency / Cost Reduction / Revenue / Quality] | [value if quantifiable] | [when realized] |

### Cost-Benefit Summary
[Brief narrative comparing total estimated costs against expected benefits. State whether the project appears justified from a cost-benefit perspective.]

---

## To Be Clarified

[List any items that could not be determined from the source documents or user input. Remove this section if everything is complete.]

---

## Source Documents

- [List the meeting notes, Notion pages, or other sources used to produce this document]
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`

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

> **Situation Assessment created** at `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
>
> **Summary:**
> - [N] resources inventoried ([N] data sources, [N] personnel, [N] hardware)
> - [N] requirements, [N] assumptions, [N] constraints documented
> - [N] risks identified with contingency plans
> - [N] business terms, [N] data mining terms defined
> - Cost-benefit assessment: [justified / needs further analysis / TBD]
> - [N] items still to be clarified (if any)
>
> **Next step in CRISP-DM:** Run `/define-data-mining-goals` to translate business objectives into technical data mining goals (Task 1.3).

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 1.2 artifact link.

## Quality Checks

Before finalizing the document, verify:
- [ ] Every identified risk has a contingency plan
- [ ] Every assumption states the impact if it turns out to be wrong
- [ ] Every constraint has a mitigation or workaround noted
- [ ] Data sources include access method and known quality issues
- [ ] Personnel list includes availability for later project phases
- [ ] Cost-benefit section addresses hidden costs (data extraction, workflow changes, training)
- [ ] All business terms are defined in plain language a non-domain-expert can understand
- [ ] No PII or sensitive data is included in the document
- [ ] Document cross-references the 1.1 business objectives where applicable
