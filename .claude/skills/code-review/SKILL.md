---
name: code-review
description: Perform a standardized code review following Colruyt Group quality checklist. Use when asked to review code changes.
argument-hint: "[file or branch]"
user-invocable: true
---

# Code Review

Review the specified code changes (or current uncommitted changes if no argument given) against this checklist:

Target: $ARGUMENTS (if empty, review `git diff` output)

## Checklist

### Correctness
- [ ] Logic is correct and handles edge cases
- [ ] Error handling is appropriate and complete
- [ ] No off-by-one errors, null pointer risks, or race conditions

### Security
- [ ] No hardcoded secrets or credentials
- [ ] Input validation at system boundaries
- [ ] No SQL injection, XSS, or CSRF vulnerabilities
- [ ] Sensitive data is not logged or exposed

### Quality
- [ ] Code is readable and self-documenting
- [ ] No code duplication that should be extracted
- [ ] Functions have single responsibility
- [ ] Naming is clear and consistent

### Testing
- [ ] New code has corresponding tests
- [ ] Edge cases are tested
- [ ] Tests are deterministic (no flaky tests)

### Performance
- [ ] No N+1 queries or unbounded loops
- [ ] Appropriate use of caching, indexing, pagination
- [ ] No unnecessary memory allocation

### Compliance
- [ ] GDPR requirements met for any personal data handling
- [ ] Logging follows structured format without PII

Output a structured review with findings categorized as: CRITICAL, WARNING, SUGGESTION, PRAISE.
