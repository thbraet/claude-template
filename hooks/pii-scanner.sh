#!/usr/bin/env bash
# Hook: PII Scanner (PreToolUse on Write)
# Scans content being written to data/ for personally identifiable information.
# Checks for: email addresses, phone numbers, Belgian national registry numbers
# (rijksregisternummer), credit card numbers, and IBANs.
set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // empty')

# Only check writes to data/ directory
[[ "$FILE_PATH" != */data/* ]] && exit 0

# Skip empty content
[ -z "$CONTENT" ] && exit 0

HITS=""

# Email addresses
if echo "$CONTENT" | grep -qiE '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'; then
  HITS="${HITS}email addresses, "
fi

# Phone numbers (Belgian +32 and local 0x formats, also generic international)
if echo "$CONTENT" | grep -qE '(\+32|0[1-9])[0-9 ./-]{7,}'; then
  HITS="${HITS}phone numbers, "
fi

# Belgian national registry number (rijksregisternummer): YY.MM.DD-NNN.CC
if echo "$CONTENT" | grep -qE '[0-9]{2}\.[0-9]{2}\.[0-9]{2}-[0-9]{3}\.[0-9]{2}'; then
  HITS="${HITS}Belgian national registry numbers, "
fi

# Credit card numbers (4 groups of 4 digits)
if echo "$CONTENT" | grep -qE '\b[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}[- ]?[0-9]{4}\b'; then
  HITS="${HITS}credit card numbers, "
fi

# IBAN (2 letter country code + 2 check digits + up to 30 alphanum)
if echo "$CONTENT" | grep -qiE '\b[A-Z]{2}[0-9]{2}[A-Z0-9]{4}[0-9]{7,}([A-Z0-9]?){0,16}\b'; then
  HITS="${HITS}IBAN numbers, "
fi

if [ -n "$HITS" ]; then
  HITS=${HITS%, }
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"ask\",\"permissionDecisionReason\":\"PII detected in data file: possible ${HITS}. Verify this data is safe to write.\"}}"
fi
