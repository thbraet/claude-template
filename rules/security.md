---
paths:
  - "**/*"
---
# Security Rules

- Never hardcode secrets, API keys, passwords, tokens, or connection strings
- Use environment variables or vault references for all sensitive values
- Never log PII (names, emails, addresses, phone numbers, national registry numbers)
- Flag any use of eval(), exec(), or dynamic code execution
- All HTTP clients must use HTTPS -- no plain HTTP except localhost
- Use parameterized queries -- never concatenate user input into SQL
- Dependencies must come from approved registries (artifactory.colruytgroup.com)
- Validate and sanitize all external input at system boundaries
- Do not disable SSL/TLS certificate verification
- Do not commit .env, .pem, .key, .p12, .pfx, or .jks files
