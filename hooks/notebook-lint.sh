#!/usr/bin/env bash
# Hook: Notebook Lint (PostToolUse on Write)
# Validates that .ipynb files follow project conventions:
#   - Dynamic PROJECT_ROOT resolution cell
#   - Sufficient markdown documentation cells
set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')

# Only check .ipynb files
[[ "$FILE_PATH" != *.ipynb ]] && exit 0
[ ! -f "$FILE_PATH" ] && exit 0

WARNINGS=""

# Check for PROJECT_ROOT pattern in any code cell
if ! python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    nb = json.load(f)
code_cells = [c for c in nb.get('cells', []) if c['cell_type'] == 'code']
source_text = ' '.join(''.join(c['source']) for c in code_cells)
if 'PROJECT_ROOT' not in source_text:
    sys.exit(1)
" "$FILE_PATH" 2>/dev/null; then
  WARNINGS="${WARNINGS}⚠ Notebook missing PROJECT_ROOT resolution cell. Per CLAUDE.md conventions, every notebook must dynamically resolve the project root.\n"
fi

# Check for sufficient markdown cells (at least a title + one section)
if ! python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    nb = json.load(f)
md_cells = [c for c in nb.get('cells', []) if c['cell_type'] == 'markdown']
# Check for at least one heading
has_heading = any(
    any(line.strip().startswith('#') for line in c['source'])
    for c in md_cells
)
if len(md_cells) < 2 or not has_heading:
    sys.exit(1)
" "$FILE_PATH" 2>/dev/null; then
  WARNINGS="${WARNINGS}⚠ Notebook has insufficient documentation. Add markdown cells with section headers (# Title, ## Section).\n"
fi

# Check for hardcoded relative paths like ../data/ or data/
if python3 -c "
import json, sys
with open(sys.argv[1]) as f:
    nb = json.load(f)
code_cells = [c for c in nb.get('cells', []) if c['cell_type'] == 'code']
source_text = '\n'.join(''.join(c['source']) for c in code_cells)
import re
# Match path strings that use hardcoded relative data paths
if re.search(r'''['\"]\.\.?/data/''', source_text):
    sys.exit(1)
" "$FILE_PATH" 2>/dev/null; then
  WARNINGS="${WARNINGS}⚠ Notebook contains hardcoded relative paths (../data/ or data/). Use PROJECT_ROOT / 'data' / ... instead.\n"
fi

if [ -n "$WARNINGS" ]; then
  echo -e "$WARNINGS"
fi
