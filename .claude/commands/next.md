---
name: next
description: "Show the next CRISP-DM task to work on, based on which artifacts exist and what's still missing"
---

# /next — What Should I Work On Next?

Check the current progress of the CRISP-DM project and recommend the next task.

## Step 1: Read the Phase Tracker

Read `.claude/CLAUDE.md` to get the current phase tracker status.

## Step 2: Check Which Artifacts Exist

Check for the existence and status of each artifact by attempting to read the following files. For each file that exists, check its `Status` field in the header (Draft / Review / Approved).

**Phase 1 — Business Understanding:**
- [ ] `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- [ ] `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- [ ] `docs/crisp-dm/1-business-understanding/1.3-data-mining-goals.md`
- [ ] `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

**Phase 2 — Data Understanding:**
- [ ] `docs/crisp-dm/2-data-understanding/2.1-data-collection.md`
- [ ] `docs/crisp-dm/2-data-understanding/2.2-data-description.md`
- [ ] `docs/crisp-dm/2-data-understanding/2.3-data-exploration.md`
- [ ] `docs/crisp-dm/2-data-understanding/2.4-data-quality.md`

**Phase 3 — Data Preparation:**
- [ ] `docs/crisp-dm/3-data-preparation/3.1-select-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.2-clean-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.3-construct-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.4-integrate-data.md`
- [ ] `docs/crisp-dm/3-data-preparation/3.5-format-data.md`

**Phase 4 — Modeling:**
- [ ] `docs/crisp-dm/4-modeling/4.1-select-modeling-techniques.md`
- [ ] `docs/crisp-dm/4-modeling/4.2-generate-test-design.md`
- [ ] `docs/crisp-dm/4-modeling/4.3-build-model.md`
- [ ] `docs/crisp-dm/4-modeling/4.4-assess-model.md`

**Phase 5 — Evaluation:**
- [ ] `docs/crisp-dm/5-evaluation/5.1-evaluate-results.md`
- [ ] `docs/crisp-dm/5-evaluation/5.2-review-process.md`
- [ ] `docs/crisp-dm/5-evaluation/5.3-determine-next-steps.md`

**Phase 6 — Deployment:**
- [ ] `docs/crisp-dm/6-deployment/6.1-plan-deployment.md`
- [ ] `docs/crisp-dm/6-deployment/6.2-plan-monitoring.md`
- [ ] `docs/crisp-dm/6-deployment/6.3-produce-final-report.md`
- [ ] `docs/crisp-dm/6-deployment/6.4-review-project.md`

## Step 3: Also Check for Non-Document Artifacts

Check for code and notebook artifacts that indicate progress:

- [ ] `notebooks/` — any EDA or exploration notebooks (Phase 2)
- [ ] `src/` or `pipelines/` — any feature engineering or data prep code (Phase 3)
- [ ] `models/` or MLflow experiment logs — any trained models (Phase 4)
- [ ] `reports/` — any evaluation reports or model cards (Phase 5)

## Step 4: Determine Next Task

Apply these rules in order:

1. **Within a phase, tasks are sequential.** Don't recommend 1.3 if 1.2 doesn't exist yet.
2. **A task is "done" if its artifact exists.** A task is "complete" if its status is "Approved". A task in "Draft" or "Review" status may need attention.
3. **A phase is complete when all its tasks have artifacts.**
4. **Phases are mostly sequential**, but CRISP-DM allows iteration — if earlier phase documents are in "Draft" while later phases have started, flag this.
5. **"To Be Clarified" sections** in existing documents represent open items that may block downstream work — flag these.

## Step 5: Present the Status and Recommendation

Present the output in this exact format:

> ## CRISP-DM Progress
>
> | Phase | Tasks | Done | Status |
> |-------|-------|------|--------|
> | 1. Business Understanding | 4 | [N]/4 | [status] |
> | 2. Data Understanding | 4 | [N]/4 | [status] |
> | 3. Data Preparation | 5 | [N]/5 | [status] |
> | 4. Modeling | 4 | [N]/4 | [status] |
> | 5. Evaluation | 3 | [N]/3 | [status] |
> | 6. Deployment | 4 | [N]/4 | [status] |
>
> ### Current Phase: [phase name]
>
> | Task | Artifact | Status |
> |------|----------|--------|
> | [task number and name] | [exists / missing] | [Draft / Review / Approved / —] |
>
> ### Open Items
> [List any "To Be Clarified" items from existing documents that may block the next task]
>
> ---
>
> ## Next Up
>
> **[Task number]: [Task name]**
> [One sentence explaining what this task does and why it's next]
>
> Run: `/[command-name]`
>
> **Tip:** [Any relevant context, e.g., "Have your meeting notes ready" or "This task will read your 1.1 and 1.2 documents automatically"]

## Step 6: Update the Phase Tracker

If the phase tracker in `.claude/CLAUDE.md` is out of date (e.g., artifacts exist that aren't listed, or a phase status is wrong), update it to reflect the current state. Add artifact links for any completed tasks that are missing from the tracker.
