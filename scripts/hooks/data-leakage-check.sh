#!/usr/bin/env bash
# Hook: Data Leakage Check (PostToolUse on Write)
# Flags .fit() and .fit_transform() calls in src/*.py that may operate on
# non-training data, which is a common source of data leakage.
set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only check src/*.py files
[[ "$FILE_PATH" != */src/*.py ]] && exit 0
[ ! -f "$FILE_PATH" ] && exit 0

WARNINGS=""

# Find .fit() calls that don't reference 'train' in the surrounding context
# We check each match line for the word 'train' to reduce false positives
LEAKY_FIT=$(grep -n '\.fit(' "$FILE_PATH" 2>/dev/null \
  | grep -v '^\s*#' \
  | grep -vi 'train' \
  | grep -v '_fit' \
  || true)

if [ -n "$LEAKY_FIT" ]; then
  WARNINGS="${WARNINGS}⚠ Potential data leakage — .fit() calls without 'train' context:\n${LEAKY_FIT}\n  Ensure all .fit() calls use training data only (fit on train, transform on test).\n\n"
fi

# Find .fit_transform() calls — these should almost never be used on test data
LEAKY_FT=$(grep -n '\.fit_transform(' "$FILE_PATH" 2>/dev/null \
  | grep -v '^\s*#' \
  | grep -vi 'train' \
  || true)

if [ -n "$LEAKY_FT" ]; then
  WARNINGS="${WARNINGS}⚠ Potential data leakage — .fit_transform() without 'train' context:\n${LEAKY_FT}\n  Use .fit() on train, then .transform() on both train and test.\n"
fi

if [ -n "$WARNINGS" ]; then
  echo -e "$WARNINGS"
fi
