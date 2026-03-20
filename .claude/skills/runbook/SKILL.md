---
name: runbook
description: Generate an operations runbook for a deployed model. Use during CRISP-DM Deployment phase.
argument-hint: "[model/service name]"
user-invocable: true
---

# Operations Runbook (CRISP-DM Phase 6)

Generate a runbook for: $ARGUMENTS

# Runbook: [SERVICE NAME]

## Service Overview
- What: [what this model/service does]
- Owner: [team]
- On-call: [rotation]
- Architecture: [how it's deployed]

## Health Checks
- [ ] Endpoint: [health check URL]
- [ ] Expected response: [what "healthy" looks like]
- [ ] Dashboard: [monitoring URL]

## Common Issues & Resolutions
| Symptom | Likely Cause | Resolution |
|---|---|---|
| High latency | Model loading | Restart pod / check memory |
| Prediction drift alert | Data distribution change | Check upstream data, consider retraining |
| 5xx errors | Input schema mismatch | Check input validation logs |

## Retraining Procedure
1. [step-by-step retraining]

## Rollback Procedure
1. [step-by-step rollback]

## Escalation
| Severity | Response Time | Escalation |
|---|---|---|
| P1 | 15 min | [who] |
| P2 | 1 hour | [who] |
| P3 | Next business day | [who] |
