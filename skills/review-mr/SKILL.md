---
name: review-mr
description: "Review a merge request or branch diff as a senior developer and data scientist. Produces a structured review report with findings, severity levels, and a merge verdict."
argument-hint: "<optional: branch name, commit range, or 'staged' to review staged changes>"
---

# /review-mr — Code Review

> **Purpose:** Independent code review before merging to main.
>
> *"Every change to main should be reviewed by someone who didn't write it — even if that someone is an AI."*

## Purpose

This skill performs a structured code review of a branch diff (or staged changes) against `main`. It checks for correctness, data science rigor, security, compliance, and convention adherence. It produces a review report with actionable findings and a clear merge verdict.

## Output Location

The review is presented directly in the conversation as a structured report. No file artifacts are created — the review lives in the MR discussion, not in the repo.

## Workflow

### Step 1: Determine What to Review

Based on the argument provided:

- **No argument:** Review the current branch's diff against `main`.
  ```bash
  git log --oneline main..HEAD
  git diff main...HEAD
  ```
- **Branch name:** Check out and diff that branch against `main`.
  ```bash
  git log --oneline main..<branch>
  git diff main...<branch>
  ```
- **`staged`:** Review only staged changes.
  ```bash
  git diff --cached
  ```

If there are no changes to review, report that and stop.

### Step 2: Gather Context

Before reviewing code, understand the intent:

1. **Read commit messages** — what do they claim the changes do?
2. **Identify the CRISP-DM phase** — which phase do these changes belong to?
3. **Read related CRISP-DM docs** — if the changes touch a specific phase, read its existing artifacts for context.
4. **Check the branch name** — does it follow `feature/` or `bugfix/` conventions?

### Step 3: Review Changed Files

For each changed file, review systematically:

#### Python files (`.py`)
- [ ] Correctness: logic errors, off-by-one, wrong variable
- [ ] Data leakage: preprocessing fit on test data, future information in features
- [ ] Train-only fitting: imputers, encoders, scalers fit on train only
- [ ] Reproducibility: random seeds set, deterministic operations
- [ ] Error handling: explicit, no swallowed exceptions
- [ ] Security: no `eval()`/`exec()`, no hardcoded secrets, parameterized SQL
- [ ] Naming: descriptive, intention-revealing
- [ ] Complexity: functions focused on one thing, no deep nesting
- [ ] Imports: no unused imports, no circular dependencies
- [ ] Logging: structured JSON, no PII, appropriate severity levels

#### Jupyter notebooks (`.ipynb`)
- [ ] Path resolution: uses `PROJECT_ROOT` pattern, no hardcoded relative paths
- [ ] Narrative: markdown cells explain the "why", not just the "what"
- [ ] Reproducibility: can be run top-to-bottom without manual intervention
- [ ] Output hygiene: no excessive output, no PII in outputs
- [ ] Naming: follows `{task_number}-{descriptive-name}.ipynb` convention
- [ ] Cell structure: logical flow, setup cells first, no circular dependencies between cells
- [ ] Data access: reads from correct pipeline stage, writes to correct output location

#### CRISP-DM documents (`.md` in `docs/crisp-dm/`)
- [ ] Template compliance: follows the established section structure
- [ ] Assumptions section: present with proper ID format (`A{task}-{n}`)
- [ ] Questions section: present with proper ID format (`Q{task}-{n}`)
- [ ] Business Feedback Log: present (even if empty)
- [ ] Source Documents: references to upstream CRISP-DM artifacts
- [ ] Sign-off section: present with roles

#### Data files
- [ ] No raw data modifications (raw data is immutable)
- [ ] Processed data written to `data/processed/`
- [ ] No large files (>100MB) committed to git
- [ ] No PII in committed data files

#### Configuration and other files
- [ ] No secrets, tokens, or connection strings
- [ ] No `.env` files committed
- [ ] Dependencies pinned with exact versions

### Step 4: Check Cross-Cutting Concerns

After reviewing individual files, check:

1. **Consistency** — do the changes form a coherent, logical unit?
2. **Completeness** — is anything missing? (e.g., notebook without corresponding doc, feature code without tests)
3. **Commit hygiene** — one logical change per commit? Conventional Commits format?
4. **CRISP-DM alignment** — do the changes advance the stated CRISP-DM phase correctly?
5. **Documentation** — are new features/decisions documented?

### Step 5: Produce the Review Report

Present the review in this format:

```markdown
# Code Review Report

**Branch:** `<branch name>`
**Commits reviewed:** <N> commits (<first>..<last>)
**Files changed:** <N>
**CRISP-DM Phase:** <phase>
**Reviewer:** Code Review Agent (Senior DS/SWE)
**Date:** <date>

---

## Summary

<2-3 sentence summary of what the changes do and the overall quality assessment.>

---

## Findings

### CRITICAL

| # | File | Line(s) | Finding | Recommendation |
|---|------|---------|---------|----------------|
| 1 | `path/to/file.py` | L42-45 | <description> | <what to do> |

### HIGH

| # | File | Line(s) | Finding | Recommendation |
|---|------|---------|---------|----------------|

### MEDIUM

| # | File | Line(s) | Finding | Recommendation |
|---|------|---------|---------|----------------|

### LOW

| # | File | Line(s) | Finding | Recommendation |
|---|------|---------|---------|----------------|

### INFO (Positive Observations)

- <things done well — acknowledge good practices>

---

## Checklist Summary

| Category | Status | Notes |
|----------|--------|-------|
| Correctness | Pass/Fail | |
| Data Science Rigor | Pass/Fail/N/A | |
| Security | Pass/Fail | |
| Compliance (GDPR/PII) | Pass/Fail | |
| Coding Standards | Pass/Fail | |
| Notebook Standards | Pass/Fail/N/A | |
| CRISP-DM Conventions | Pass/Fail/N/A | |
| Git Conventions | Pass/Fail | |
| Documentation | Pass/Fail | |

---

## Verdict

**<APPROVE / REQUEST CHANGES / DISCUSS>**

<Justification for the verdict. If requesting changes, list the blocking items (CRITICAL and HIGH findings) that must be resolved before merge.>
```

### Step 6: Present Verdict and Next Steps

After the report:

- **If APPROVE:** Indicate the branch is ready to merge. Suggest the user create an MR on GitLab (the primary remote).
- **If REQUEST CHANGES:** List the blocking findings clearly. Offer to help fix any of them.
- **If DISCUSS:** Identify the items that need human judgment and present the trade-offs.

## Severity Definitions

| Severity | Definition | Examples |
|----------|-----------|---------|
| **CRITICAL** | Will cause incorrect results, data loss, or security breach | Data leakage, PII exposure, logic bug affecting predictions, hardcoded secrets |
| **HIGH** | Violates methodology or compliance requirements | Preprocessing fit on test data, unlogged experiment, missing model card, GDPR violation |
| **MEDIUM** | Reduces maintainability or violates conventions | Poor naming, missing docstring on public API, hardcoded magic numbers, convention violations |
| **LOW** | Minor improvement opportunity | Slightly better variable name, optional refactor, style suggestion |
| **INFO** | Positive observation or neutral note | Good test coverage, clean notebook narrative, well-structured commit messages |

## Quality Checks

Before finalizing the review:
- [ ] Every changed file was reviewed
- [ ] Findings reference specific files and line numbers
- [ ] Severity levels are applied consistently
- [ ] The verdict matches the findings (no APPROVE with unresolved CRITICAL/HIGH)
- [ ] Positive observations are included (not just complaints)
- [ ] Recommendations are actionable and specific
