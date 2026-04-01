---
name: assumption-audit
description: "Scan all CRISP-DM documentation for assumptions with status 'Pending verification' and open business questions. Produces a consolidated audit report for stakeholder review."
argument-hint: "<optional: 'pending' (default), 'all', or specific phase number>"
---

# /assumption-audit — Assumption & Question Tracker

> **Purpose:** Surface all unverified assumptions and open questions across the project.
>
> *"Unverified assumptions are hidden risks — surface them before they surface you."*

## Purpose

This skill scans all CRISP-DM documentation (`docs/crisp-dm/**/*.md`) for the "Assumptions & Business Validation" sections. It collects all assumptions, business questions, and feedback entries, then produces a consolidated audit report highlighting items that need attention.

## Output Location

Results are printed directly in the conversation as a structured report. Optionally write to `docs/crisp-dm/assumption-audit.md` if the user requests a persistent report.

## Workflow

### Step 1: Scan All CRISP-DM Documents

Read every `.md` file under `docs/crisp-dm/`:

```
docs/crisp-dm/1-business-understanding/*.md
docs/crisp-dm/2-data-understanding/*.md
docs/crisp-dm/3-data-preparation/*.md
docs/crisp-dm/4-modeling/*.md
docs/crisp-dm/5-evaluation/*.md
docs/crisp-dm/6-deployment/*.md
```

For each file, extract the "Assumptions & Business Validation" section and parse:

1. **Assumptions Made** table — extract ID, Assumption, Category, Rationale, Status
2. **Questions for Business** table — extract ID, Question, Related Assumption, Priority, Status
3. **Business Feedback Log** table — extract Date, Feedback Source, Related items, Feedback, Action, Changes

### Step 2: Categorize Findings

Group all extracted items by status:

**Assumptions:**
- `Pending verification` — needs stakeholder confirmation (HIGH priority)
- `Verified` — confirmed by business (informational)
- `Reworked (see feedback)` — was changed based on feedback (informational)
- `Rejected` — invalidated (check if downstream work was affected)

**Questions:**
- `Open` — needs an answer (HIGH priority)
- `Answered` — resolved (informational)
- `Closed` — no longer relevant (informational)

### Step 3: Assess Impact

For each pending/open item, assess:

1. **Downstream impact**: Which later-phase documents or code depend on this assumption?
2. **Risk level**: What happens if this assumption is wrong? (High/Medium/Low)
3. **Blocking**: Does this block progress on any current phase?

### Step 4: Generate Audit Report

Based on the argument:

- **"pending" or no argument**: Show only items needing attention
- **"all"**: Show all items across all statuses
- **Specific phase (e.g., "3")**: Show items from that phase only

**Report format:**

```
═══════════════════════════════════════════════
 ASSUMPTION AUDIT REPORT — [date]
═══════════════════════════════════════════════

PENDING VERIFICATION (action required)
──────────────────────────────────────
  [A1.2-3] "Store capacity is fixed at current levels"
    Source: docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md
    Category: Business constraint
    Risk: HIGH — capacity changes would invalidate demand forecasts
    Downstream: 3.3 (features), 4.3 (model training)

  [A3.2-1] "Missing ages are MCAR (missing completely at random)"
    Source: docs/crisp-dm/3-data-preparation/3.2-clean-data.md
    Category: Data quality
    Risk: MEDIUM — if MAR, imputation strategy should change
    Downstream: 3.3 (features), 4.3 (model accuracy)

OPEN QUESTIONS (awaiting answers)
─────────────────────────────────
  [Q1.1-2] "What is the acceptable false positive rate for the business?"
    Source: docs/crisp-dm/1-business-understanding/1.1-business-objectives.md
    Priority: High
    Related: A1.1-1
    Impact: Blocks threshold selection in Phase 5

SUMMARY
───────
  Assumptions:  12 total | 3 pending | 8 verified | 1 rejected
  Questions:     8 total | 2 open    | 5 answered | 1 closed
  Feedback log:  6 entries

  Action items: 5 items need stakeholder attention
  Highest risk: [A1.2-3] — capacity assumption affects entire modeling pipeline
```

### Step 5: Check for Missing Sections

Also flag any CRISP-DM document that is missing the "Assumptions & Business Validation" section entirely. Per project conventions, every document should have this section.

```
DOCUMENTS MISSING ASSUMPTION TRACKING
──────────────────────────────────────
  ⚠ docs/crisp-dm/3-data-preparation/3.4-integrate-data.md — no Assumptions section found
  ⚠ docs/crisp-dm/4-modeling/4.1-modeling-techniques.md — no Assumptions section found
```

### Step 6: Offer Next Steps

Based on findings, suggest:
- Which assumptions to prioritize for stakeholder review
- Whether any pending items are blocking current work
- If the user wants to save the report as `docs/crisp-dm/assumption-audit.md`
