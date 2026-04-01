# Phase Status Email

Use this prompt to draft a stakeholder status email after completing a CRISP-DM phase.

## Template

Read the completed phase's documents from `docs/crisp-dm/` and the project plan from `docs/crisp-dm/1-business-understanding/1.4-project-plan.md`.

Then draft a concise email (under 200 words) with this structure:

**Subject:** [Project Name] — Phase [N] Complete: [Phase Name]

**Body:**

Hi [stakeholder],

Quick update on [project name]:

**Completed:** [Phase name] — [one-sentence summary of what was accomplished]

**Key findings:**
- [Finding 1 — most important insight, in business terms]
- [Finding 2]
- [Finding 3 — if applicable]

**Decisions needed:**
- [Any pending assumptions or questions requiring business input]
- [Or: "No decisions needed at this time"]

**Next up:** [Next phase name] — [what will happen, when it's expected]

**Risk flag:** [Any concerns or blockers, or "On track, no concerns"]

Best,
[Name]

Rules:
- No technical jargon
- Lead with what matters to the stakeholder
- Only flag risks that are actionable
- Include a timeline reference (from 1.4 project plan)
- If there are pending assumptions (from `/assumption-audit`), surface the highest-priority one
