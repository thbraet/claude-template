---
name: review-project
description: "CRISP-DM 6.4 — Review Project. Conducts a structured retrospective on the data mining project: what went well, what didn't, process improvements, and knowledge captured for future projects. Produces a project review document in docs/crisp-dm/6-deployment/."
argument-hint: "<optional: specific aspect to review, or team member perspective>"
---

# /review-project — CRISP-DM 6.4: Review Project

> **Phase:** 6. Deployment | **Task:** 6.4 Review Project
>
> *"At this point, the resulting model is satisfactory and has been approved for deployment. The project leader and his team should assess what went right and what went wrong, what was done well and what needs to be improved."*

## Purpose

This skill facilitates a structured project retrospective that captures lessons learned, evaluates process effectiveness, identifies improvements for future CRISP-DM projects, and documents knowledge that would otherwise be lost. It is the final task in the CRISP-DM cycle, designed to compound organizational learning across data science projects.

## Output Location

- Review: `docs/crisp-dm/6-deployment/6.4-review-project.md`

## Workflow

### Step 1: Check for Existing Artifacts

Before starting, check if the output file already exists:
- Read `docs/crisp-dm/6-deployment/6.4-review-project.md`
- If it exists, present its contents and ask: *"A project review already exists. Do you want to (1) update it, (2) start fresh, or (3) skip this step?"*
- If it does not exist, proceed to Step 2.

Read the final report and project plan for context:
- Read `docs/crisp-dm/6-deployment/6.3-final-report.md`
  - If it exists, use it — the final report contains the full project summary.
- Read `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`
  - If it exists, use it — compare planned vs. actual timelines and milestones.
- Read `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
  - If it exists, use it — compare original objectives with actual outcomes.
- Read `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
  - If it exists, use it — review whether identified risks materialized.

### Step 2: Extract Information from Source Documents

From the ingested documents, extract:
- **Original objectives** (from 1.1) — what was the goal?
- **Planned timeline and milestones** (from 1.4) — what was the plan?
- **Identified risks** (from 1.2) — what risks were anticipated?
- **Actual outcomes** (from 6.3) — what was achieved?
- **Technical debt** (from 6.3) — what remains unresolved?

Present what was extracted and indicate what the review should focus on.

### Step 3: Assess Objectives vs. Outcomes

Discuss and document:
- **Business objectives** — were they met? Partially? Not at all?
- **Data mining goals** — were the technical success criteria achieved?
- **Scope** — did the scope change during the project? Why?
- **Timeline** — was the project delivered on time? What caused delays?
- **Budget** — was the project within budget? What drove cost overruns?

### Step 4: Phase-by-Phase Review

For each CRISP-DM phase, discuss:
- **What went well** — effective approaches, good decisions, things to repeat
- **What went wrong** — problems encountered, decisions that cost time or quality
- **Surprises** — things that were unexpected (positive or negative)
- **What we would do differently** — specific, actionable changes for next time

Guide the user through each phase with targeted questions:

**Phase 1 (Business Understanding):**
- Were the business objectives clear from the start?
- Did stakeholder alignment change during the project?

**Phase 2 (Data Understanding):**
- Were there data surprises that should have been caught earlier?
- Was the EDA sufficient to inform modeling decisions?

**Phase 3 (Data Preparation):**
- Was the data preparation effort proportional to its impact?
- Were there feature engineering approaches that particularly helped or hurt?

**Phase 4 (Modeling):**
- Was the baseline model adequate as a benchmark?
- Did the most complex model win, or was a simpler approach sufficient?

**Phase 5 (Evaluation):**
- Were stakeholders able to evaluate the model effectively?
- Was the evaluation process smooth or did it reveal unexpected issues?

**Phase 6 (Deployment):**
- Was the deployment plan realistic?
- Were there infrastructure surprises?

### Step 5: Capture Process Improvements

Discuss and document:
- **Tools and infrastructure** — what worked, what should change
- **Team and skills** — were the right people involved, skill gaps identified
- **Communication** — stakeholder engagement, documentation practices
- **Methodology** — was CRISP-DM applied effectively, where did it help most
- **Data access** — was data available when needed, governance friction
- **Experiment tracking** — was MLflow (or equivalent) used effectively

### Step 6: Capture Reusable Knowledge

Discuss and document:
- **Reusable code** — pipelines, utilities, or components that can be shared
- **Patterns** — approaches that worked well and should become standard practice
- **Anti-patterns** — approaches that should be avoided in future projects
- **Domain knowledge** — retail/supply chain insights gained during the project
- **Data insights** — understanding of data sources that will help future projects

### Step 7: Generate the Output Document

After gathering all information, create the output directory and write the document.

```bash
mkdir -p docs/crisp-dm/6-deployment
```

Write the file `docs/crisp-dm/6-deployment/6.4-review-project.md` using this template:

```markdown
# 6.4 Project Review

> **Project:** [project name]
> **Date:** [current date]
> **CRISP-DM Phase:** 6. Deployment
> **Status:** Draft | Review | Approved

---

## Review Overview

- **Project Duration:** [start date] — [end date]
- **Team Members:** [list]
- **Business Objective Met:** [Yes / Partially / No]
- **Data Mining Goal Met:** [Yes / Partially / No]
- **Deployed to Production:** [Yes / No / In Progress]

---

## Objectives vs. Outcomes

| Dimension | Planned | Actual | Assessment |
|-----------|---------|--------|-----------|
| Business objective | [original objective] | [what was achieved] | [Met / Partially / Not Met] |
| Primary metric target | [target] | [achieved] | [Met / Partially / Not Met] |
| Timeline | [planned end date] | [actual end date] | [On time / Delayed by X] |
| Scope | [original scope] | [final scope] | [Unchanged / Expanded / Reduced] |

### Scope Changes
| Change | Reason | Impact |
|--------|--------|--------|
| [what changed] | [why] | [time/quality/cost impact] |

---

## Phase-by-Phase Review

### Phase 1: Business Understanding
| Aspect | Assessment |
|--------|-----------|
| What went well | [specifics] |
| What went wrong | [specifics] |
| Surprises | [specifics] |
| Do differently | [specifics] |

### Phase 2: Data Understanding
| Aspect | Assessment |
|--------|-----------|
| What went well | [specifics] |
| What went wrong | [specifics] |
| Surprises | [specifics] |
| Do differently | [specifics] |

### Phase 3: Data Preparation
| Aspect | Assessment |
|--------|-----------|
| What went well | [specifics] |
| What went wrong | [specifics] |
| Surprises | [specifics] |
| Do differently | [specifics] |

### Phase 4: Modeling
| Aspect | Assessment |
|--------|-----------|
| What went well | [specifics] |
| What went wrong | [specifics] |
| Surprises | [specifics] |
| Do differently | [specifics] |

### Phase 5: Evaluation
| Aspect | Assessment |
|--------|-----------|
| What went well | [specifics] |
| What went wrong | [specifics] |
| Surprises | [specifics] |
| Do differently | [specifics] |

### Phase 6: Deployment
| Aspect | Assessment |
|--------|-----------|
| What went well | [specifics] |
| What went wrong | [specifics] |
| Surprises | [specifics] |
| Do differently | [specifics] |

---

## Risk Review

| Identified Risk (from 1.2) | Materialized | Impact | Mitigation Effectiveness |
|---------------------------|-------------|--------|------------------------|
| [risk] | [Yes/No/Partially] | [actual impact] | [effective / insufficient / not needed] |

### Unidentified Risks That Materialized
| Risk | Impact | How Detected | Recommended Mitigation for Future |
|------|--------|-------------|----------------------------------|
| [risk] | [impact] | [how we found out] | [what to do next time] |

---

## Process Improvements

### Tools and Infrastructure
| Area | Current State | Recommendation | Priority |
|------|--------------|---------------|----------|
| [area] | [what we used] | [what to change] | [High/Medium/Low] |

### Team and Skills
| Skill Area | Current State | Gap | Recommendation |
|-----------|--------------|-----|---------------|
| [area] | [team capability] | [what's missing] | [training / hiring / partnering] |

### Communication and Stakeholder Engagement
| Aspect | What Worked | What Didn't | Improvement |
|--------|------------|-------------|-------------|
| [aspect] | [specifics] | [specifics] | [recommendation] |

### CRISP-DM Process
| Phase | Methodology Assessment | Improvement |
|-------|----------------------|-------------|
| [phase] | [how well CRISP-DM was applied] | [what to change] |

---

## Reusable Knowledge

### Reusable Code and Pipelines
| Component | Location | Reuse Potential | Notes |
|-----------|----------|----------------|-------|
| [component] | [path/repo] | [High/Medium/Low] | [notes] |

### Patterns to Repeat
| Pattern | Context | Why It Worked |
|---------|---------|--------------|
| [pattern] | [when to apply it] | [why it was effective] |

### Anti-patterns to Avoid
| Anti-pattern | Context | Why It Failed | Alternative |
|-------------|---------|--------------|-------------|
| [anti-pattern] | [when it was tried] | [what went wrong] | [what to do instead] |

### Domain Knowledge Gained
| Insight | Relevance | Applies To |
|---------|-----------|-----------|
| [insight about retail/supply chain/stores] | [why it matters for data science] | [which future projects] |

### Data Source Insights
| Data Source | Key Learning | Impact on Future Projects |
|-------------|-------------|--------------------------|
| [source] | [what we learned about this data] | [how to use this knowledge] |

---

## Summary of Key Lessons

1. **[Lesson 1]** — [one sentence explaining the lesson and its impact]
2. **[Lesson 2]** — [one sentence]
3. **[Lesson 3]** — [one sentence]
4. **[Lesson 4]** — [one sentence]
5. **[Lesson 5]** — [one sentence]

---

## Action Items for Future Projects

| Action | Owner | Priority | Target |
|--------|-------|----------|--------|
| [specific action] | [who] | [High/Medium/Low] | [when or which project] |

---

## To Be Clarified

[List any items that need further discussion. Remove this section if everything is complete.]

---

## Source Documents

- 6.3 Final Report: `docs/crisp-dm/6-deployment/6.3-final-report.md`
- 1.1 Business Objectives: `docs/crisp-dm/1-business-understanding/1.1-business-objectives.md`
- 1.2 Situation Assessment: `docs/crisp-dm/1-business-understanding/1.2-situation-assessment.md`
- 1.4 Project Plan: `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| Lead Data Scientist | | | Pending |
| Project Manager | | | Pending |
| Business Stakeholder | | | Pending |
| Team Members | | | Pending |
```

### Step 8: Summary and Next Steps

After writing the document, present a summary:

> **Project Review created** at `docs/crisp-dm/6-deployment/6.4-review-project.md`
>
> **Summary:**
> - Business objective met: [Yes/Partially/No]
> - Data mining goal met: [Yes/Partially/No]
> - Key lessons: [top 3 lessons]
> - Process improvements: [N] recommendations
> - Reusable components: [N] identified
> - Action items: [N] for future projects
>
> **CRISP-DM cycle complete.** This concludes the Deployment phase and the full CRISP-DM methodology cycle. The project may now enter a new iteration (returning to Phase 1 with updated objectives) or transition to steady-state operations under the monitoring plan defined in 6.2.

Also update the CRISP-DM phase tracker in `.claude/CLAUDE.md` to add the 6.4 artifact link and mark Phase 6 as complete.

## Quality Checks

Before finalizing the document, verify:
- [ ] Objectives vs. outcomes comparison is honest (not just positive spin)
- [ ] Phase-by-phase review covers all completed phases
- [ ] Both successes and failures are documented with specifics
- [ ] Risk review compares identified risks against what actually happened
- [ ] Unidentified risks that materialized are captured
- [ ] Process improvements are concrete and actionable (not generic platitudes)
- [ ] Reusable code and patterns are identified with locations
- [ ] Anti-patterns are documented with alternatives
- [ ] Domain knowledge is captured for future projects
- [ ] Action items have owners and priorities
- [ ] The review is constructive, not blame-oriented
- [ ] Key lessons are concise enough to be remembered and applied
- [ ] No PII or sensitive data in the review
- [ ] All source documents are cross-referenced
