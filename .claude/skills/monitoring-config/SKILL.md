---
name: monitoring-config
description: Generate monitoring configuration for a deployed model. Use during CRISP-DM Deployment to set up drift detection and alerting.
argument-hint: "[model name]"
user-invocable: true
---

# Monitoring Configuration (CRISP-DM Phase 6)

Set up monitoring for: $ARGUMENTS

Generate:
1. **Data drift detection** config (using Evidently AI or custom):
   - Reference dataset (training distribution)
   - Monitored features and drift methods (PSI, KS-test, Wasserstein)
   - Alert thresholds per feature
2. **Prediction drift** monitoring:
   - Prediction distribution tracking
   - Confidence score distribution
3. **Performance monitoring** (when labels become available):
   - Metrics tracked over time windows
   - Performance degradation thresholds
4. **Alerting rules**:
   - Who gets alerted (Slack channel, email)
   - Severity levels and escalation
5. **Retraining triggers**:
   - Automatic retraining conditions
   - Manual review triggers
6. **Dashboard config**: Metrics to display, refresh cadence
