---
name: complete-phase
description: "CRISP-DM phase transition gate — validates that all artifacts, notebooks, assumptions, and quality checks for a given phase are complete before moving to the next phase. Produces a phase completion summary."
argument-hint: "<phase number: 1-6>"
---

# /complete-phase — Phase Transition Checklist

> **Purpose:** Validate that a CRISP-DM phase is fully complete before moving on.
>
> *"Incomplete phases create hidden debt — validate before you advance."*

## Purpose

This skill performs a comprehensive completeness check on a CRISP-DM phase. It verifies that all required artifacts exist, documentation is populated (not just template stubs), assumptions are tracked, notebooks are present where expected, and cross-references to prior phases are intact. It produces a pass/fail gate report and updates the phase status in `.claude/CLAUDE.md`.

## Output Location

1. **Gate report**: printed in conversation
2. **Phase status update**: `.claude/CLAUDE.md` phase tracker table updated to "Complete" if all checks pass

## Workflow

### Step 1: Parse Phase Argument

Accept a phase number (1-6). If not provided, ask the user which phase to validate.

Map phase number to directory and expected artifacts:

```
Phase 1 → docs/crisp-dm/1-business-understanding/
  Required docs: 1.1-business-objectives.md, 1.2-situation-assessment.md,
                  1.3-data-mining-goals.md, 1.4-project-plan.md
  Required notebooks: (none — Phase 1 is document-driven)

Phase 2 → docs/crisp-dm/2-data-understanding/
  Required docs: 2.1-data-collection.md, 2.2-data-description.md,
                  2.3-data-exploration.md, 2.4-data-quality.md
  Required notebooks: 2.2-data-description.ipynb, 2.3-data-exploration.ipynb,
                       2.4-data-quality.ipynb

Phase 3 → docs/crisp-dm/3-data-preparation/
  Required docs: 3.1-select-data.md, 3.2-clean-data.md, 3.3-construct-data.md,
                  3.4-integrate-data.md, 3.5-format-data.md
  Required notebooks: 3.1-select-data.ipynb, 3.2-clean-data.ipynb,
                       3.3-construct-data.ipynb, 3.4-integrate-data.ipynb,
                       3.5-format-data.ipynb
  Optional: 3.6-feature-selection (notebook + doc)
  Required data: data/processed/ must contain stage outputs

Phase 4 → docs/crisp-dm/4-modeling/
  Required docs: 4.1-modeling-techniques.md, 4.2-test-design.md,
                  4.3-model-building.md, 4.4-model-assessment.md
  Required notebooks: 4.1-modeling-techniques.ipynb, 4.2-test-design.ipynb,
                       4.3-model-building.ipynb, 4.4-model-assessment.ipynb

Phase 5 → docs/crisp-dm/5-evaluation/
  Required docs: 5.1-evaluate-results.md, 5.2-review-process.md,
                  5.3-determine-next-steps.md
  Required notebooks: 5.1-evaluate-results.ipynb, 5.2-review-process.ipynb

Phase 6 → docs/crisp-dm/6-deployment/
  Required docs: 6.1-plan-deployment.md, 6.2-plan-monitoring.md,
                  6.3-final-report.md
  Optional: 6.4-review-project.md
```

### Step 2: Check Artifact Existence

For each required artifact, check if the file exists:
- Use `Glob` to find files in the phase directory
- Mark each artifact as present or missing

### Step 3: Check Document Completeness

For each existing document, verify it's not just a stub:

1. **Read the file** and check that it has substantive content (not just template headers)
2. **Minimum content threshold**: At least 500 characters of non-header content (excluding frontmatter and blank lines)
3. **Key sections present**: Check that the document has the expected sections for its task type
4. **Assumptions section**: Verify the "Assumptions & Business Validation" section exists and has at least one entry (per project convention)

### Step 4: Check Notebook Quality

For each required notebook, verify:

1. **File exists** as `.ipynb`
2. **Has output cells**: At least some code cells have been executed (outputs present)
3. **Has PROJECT_ROOT**: Dynamic path resolution cell is present
4. **Has markdown cells**: Documentation cells with section headers exist

### Step 5: Check Cross-Phase References

Verify that the phase's documents reference prior phases appropriately:

- Phase 2 docs should reference Phase 1 artifacts (business objectives, data mining goals)
- Phase 3 docs should reference Phase 2 artifacts (data quality, exploration findings)
- Phase 4 docs should reference Phase 3 artifacts (prepared data, selected features)
- Phase 5 docs should reference Phase 4 artifacts (model assessment) and Phase 1 (business objectives)
- Phase 6 docs should reference Phase 5 artifacts (evaluation results) and span the full project

Check by grepping for file path references or section names from prerequisite phases.

### Step 6: Check Assumption Status

Run a lightweight assumption audit for this phase only:

1. Read each doc in the phase directory
2. Extract the "Assumptions Made" table
3. Count assumptions by status: Pending, Verified, Reworked, Rejected
4. Count open questions
5. Flag if there are critical pending assumptions that should be resolved before advancing

### Step 7: Generate Gate Report

```
╔═══════════════════════════════════════════════════════════╗
║  PHASE COMPLETION GATE — Phase 3: Data Preparation       ║
╚═══════════════════════════════════════════════════════════╝

ARTIFACTS
  ✓ 3.1-select-data.md              exists, 2,340 chars, sections complete
  ✓ 3.2-clean-data.md               exists, 4,120 chars, sections complete
  ✓ 3.3-construct-data.md           exists, 3,890 chars, sections complete
  ✓ 3.4-integrate-data.md           exists, 1,280 chars, sections complete
  ✓ 3.5-format-data.md              exists, 2,760 chars, sections complete
  ⚠ 3.6-select-features.md          missing (optional)

NOTEBOOKS
  ✓ 3.1-select-data.ipynb           exists, has outputs, has PROJECT_ROOT
  ✓ 3.2-clean-data.ipynb            exists, has outputs, has PROJECT_ROOT
  ✓ 3.3-construct-data.ipynb        exists, has outputs, has PROJECT_ROOT
  ✓ 3.4-integrate-data.ipynb        exists, has outputs, has PROJECT_ROOT
  ✓ 3.5-format-data.ipynb           exists, has outputs, has PROJECT_ROOT

DATA OUTPUTS
  ✓ data/processed/train_clean.csv   exists
  ✓ data/processed/test_clean.csv    exists
  ✓ data/processed/train_features.csv exists
  ✓ data/processed/test_features.csv  exists
  ✓ data/processed/train_formatted.csv exists
  ✓ data/processed/test_formatted.csv  exists

CROSS-REFERENCES
  ✓ References Phase 2 data quality findings
  ✓ References Phase 2 exploration hypotheses
  ✗ 3.4-integrate-data.md missing reference to 2.2 data description

ASSUMPTIONS
  Total: 8 | Verified: 5 | Pending: 2 | Rejected: 1
  Open questions: 1
  ⚠ 2 assumptions still pending verification

───────────────────────────────────────────────────────────
VERDICT: ⚠ CONDITIONAL PASS
  - All required artifacts present and populated
  - 1 cross-reference gap (minor)
  - 2 pending assumptions (recommend resolving before Phase 4)

Proceed to Phase 4? [Recommended with noted caveats]
```

### Step 8: Update Phase Tracker

If the gate passes (all required artifacts exist and are populated):

1. Read `.claude/CLAUDE.md`
2. Update the CRISP-DM Phase Tracker table — change the phase status to "Complete"
3. Add links to all artifacts in the Key Artifacts column
4. Ask the user before writing the update

If the gate fails:
1. List all failing items with specific remediation steps
2. Suggest which skill to run to fix each gap (e.g., "Run `/clean-data` to produce 3.2 artifacts")
3. Do not update the phase tracker
