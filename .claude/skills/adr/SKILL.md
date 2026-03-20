---
name: adr
description: Generate an Architecture Decision Record (ADR) for documenting significant technical decisions. Use when the user wants to document an architectural choice.
argument-hint: "[decision title]"
user-invocable: true
---

# Architecture Decision Record

Generate an ADR for: $ARGUMENTS

Use this template:

```markdown
# ADR-[NUMBER]: [TITLE]

**Date**: [TODAY]
**Status**: Proposed | Accepted | Deprecated | Superseded
**Deciders**: [who was involved]

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Consequences

### Positive
- [benefit 1]
- [benefit 2]

### Negative
- [trade-off 1]
- [trade-off 2]

### Risks
- [risk 1 and mitigation]

## Alternatives Considered
| Alternative | Pros | Cons | Why rejected |
|---|---|---|---|
| [option A] | ... | ... | ... |
| [option B] | ... | ... | ... |
```

Save to `docs/adr/` directory (create if it doesn't exist). Number sequentially based on existing ADRs.
