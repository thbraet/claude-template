---
name: crosslink-docs
description: "Scan all CRISP-DM documentation and verify that every document's Source Documents section correctly links to the artifacts it depends on. Adds missing cross-references and reports broken links."
argument-hint: "<optional: specific phase number or 'all' (default: all)>"
---

# /crosslink-docs — Automated Document Cross-Linking

> **Purpose:** Ensure full traceability across CRISP-DM phases through document cross-references.
>
> *"If you can't trace a decision back to its source, you can't trust it."*

## Purpose

This skill scans all CRISP-DM documentation and verifies that inter-document references are complete and correct. Every document should link to the prior-phase artifacts it depends on, and every decision should be traceable back to its source. The skill identifies missing links, broken references, and orphaned documents.

## Output Location

1. **Cross-link report**: printed in conversation
2. **Document updates**: missing links added to each document's "Source Documents" section (with user confirmation)

## Workflow

### Step 1: Build Dependency Map

Define the expected cross-reference dependencies between CRISP-DM tasks:

```
1.1 → (none — root document)
1.2 → 1.1
1.3 → 1.1, 1.2
1.4 → 1.1, 1.2, 1.3

2.1 → 1.1, 1.2, 1.3
2.2 → 2.1
2.3 → 1.3, 2.1, 2.2
2.4 → 2.1, 2.2

3.1 → 1.3, 2.3, 2.4
3.2 → 2.4, 3.1
3.3 → 1.3, 2.3, 3.1
3.4 → 2.2, 3.1
3.5 → 3.1, 3.2, 3.3, 3.4
3.6 → 3.5

4.1 → 1.3, 2.3, 2.4
4.2 → 1.3, 4.1
4.3 → 4.1, 4.2
4.4 → 1.1, 4.1, 4.2, 4.3

5.1 → 1.1, 4.4
5.2 → (all prior phases)
5.3 → 5.1, 5.2

6.1 → 1.1, 4.4, 5.3
6.2 → 6.1
6.3 → (all prior phases)
6.4 → 1.4, 6.3
```

### Step 2: Scan Existing Documents

For each document in `docs/crisp-dm/`:

1. Read the file content
2. Look for a "Source Documents" or "References" or "Input Documents" section
3. Extract all document references (file paths, task numbers like "1.1", or document titles)
4. Record which documents are referenced and which are missing per the dependency map

### Step 3: Check Reference Validity

For each reference found:

1. **Does the target file exist?** Check that the referenced path resolves to an actual file
2. **Is the reference format consistent?** Prefer relative markdown links: `[1.1 Business Objectives](../1-business-understanding/1.1-business-objectives.md)`
3. **Is the reference bidirectional?** If doc A references doc B, does doc B's downstream impact section mention doc A? (informational only — don't enforce)

### Step 4: Generate Cross-Link Report

```
CROSS-LINK AUDIT — CRISP-DM Documents
══════════════════════════════════════

PHASE 1: Business Understanding
  1.1-business-objectives.md     ✓ No dependencies (root document)
  1.2-situation-assessment.md    ✓ References 1.1 ✓
  1.3-data-mining-goals.md       ✓ References 1.1 ✓, 1.2 ✓
  1.4-project-plan.md            ✓ References 1.1 ✓, 1.2 ✓, 1.3 ✓

PHASE 2: Data Understanding
  2.1-data-collection.md         ⚠ References 1.1 ✓, 1.3 ✓ | Missing: 1.2
  2.2-data-description.md        ✓ References 2.1 ✓
  2.3-data-exploration.md        ✓ References 1.3 ✓, 2.1 ✓, 2.2 ✓
  2.4-data-quality.md            ✓ References 2.1 ✓, 2.2 ✓

PHASE 3: Data Preparation
  3.1-select-data.md             ✗ References 2.4 ✓ | Missing: 1.3, 2.3
  3.2-clean-data.md              ✓ References 2.4 ✓, 3.1 ✓
  ...

BROKEN LINKS
  3.3-construct-data.md → "2.3-exploration.md" (should be "2.3-data-exploration.md")

MISSING SECTIONS
  4.2-test-design.md — no "Source Documents" section found

SUMMARY
  Documents scanned:  23
  Fully linked:       18
  Missing references: 7
  Broken links:       1
  Missing sections:   1
```

### Step 5: Offer Fixes

For each issue found, offer to fix it:

1. **Missing references**: Add the missing link to the "Source Documents" section
2. **Broken links**: Correct the file path
3. **Missing sections**: Add a "Source Documents" section with all required references

Present each fix and ask the user before applying:

```
Fix 1 of 7: Add missing reference in 3.1-select-data.md
  Add: - [1.3 Data Mining Goals](../1-business-understanding/1.3-data-mining-goals.md)
  Add: - [2.3 Data Exploration](../2-data-understanding/2.3-data-exploration.md)

Apply? [y/n/all]
```

If the user confirms "all", apply all fixes without further prompting.

### Step 6: Summary

Report the final state:
- Total references verified
- Issues found and fixed
- Remaining issues (if user declined some fixes)
