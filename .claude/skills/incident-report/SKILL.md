---
name: incident-report
description: Generate a post-incident report following the Colruyt Group template. Use after resolving a production incident.
argument-hint: "[incident summary]"
user-invocable: true
---

# Post-Incident Report

Generate an incident report for: $ARGUMENTS

Use this template:

## Incident Report: [TITLE]

**Date**: [DATE]
**Severity**: P1 (Critical) | P2 (Major) | P3 (Minor) | P4 (Low)
**Duration**: [start time] - [end time] ([total duration])
**Affected systems**: [list]
**Impact**: [user-facing impact description]

### Timeline
| Time (UTC) | Event |
|---|---|
| HH:MM | [what happened] |

### Root Cause
[Technical explanation of what went wrong and why]

### Resolution
[What was done to fix it]

### Action Items
| Action | Owner | Priority | Due Date |
|---|---|---|---|
| [action] | [who] | [P1-P4] | [date] |

### Lessons Learned
- What went well:
- What went poorly:
- Where we got lucky:

### Detection
- How was the incident detected?
- How could we detect it faster next time?
