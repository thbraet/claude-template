---
paths:
  - "**/*"
---
# Compliance & Privacy (GDPR)

- All processing of personal data must have a documented legal basis
- Implement data minimization -- only collect/store what is strictly necessary
- PII must be encrypted at rest and in transit
- Never log PII in application logs, error messages, or stack traces
- Support data subject rights: access, rectification, erasure, portability
- Data retention: follow project-specific retention policy, default to shortest practical period
- Cross-border data transfers require appropriate safeguards (SCCs, adequacy decisions)
- Anonymize or pseudonymize data in non-production environments
- Include privacy impact considerations when designing new features that handle personal data
- Audit trail: log who accessed what data and when (without logging the data itself)
