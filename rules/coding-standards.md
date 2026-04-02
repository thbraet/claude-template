---
paths:
  - "**/*"
---
# Coding Standards

- Use descriptive, intention-revealing names for variables, functions, and classes
- Prefer explicit over implicit -- avoid magic numbers, unexplained constants
- Keep functions focused -- one responsibility per function
- Handle errors explicitly -- no empty catch blocks, no swallowed exceptions
- Use structured JSON logging with severity levels (DEBUG, INFO, WARN, ERROR)
- Include correlation IDs in log messages for distributed tracing
- Write self-documenting code -- add comments only for "why", not "what"
- Prefer composition over inheritance
- Keep cyclomatic complexity low -- extract complex conditionals into named functions
- Follow the principle of least surprise in API and function design
