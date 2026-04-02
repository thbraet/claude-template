#!/usr/bin/env bash
# Hook: CRISP-DM Phase Gate (PreToolUse on Skill)
# Blocks later-phase skills if prerequisite phase artifacts are missing.
# Prevents skipping phases (e.g., running /build-model before Data Preparation).
set -euo pipefail

INPUT=$(cat)
SKILL=$(echo "$INPUT" | jq -r '.tool_input.skill // empty')

[ -z "$SKILL" ] && exit 0

PROJECT_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

# Check if a phase directory has at least one .md artifact
check_phase() {
  local phase_dir="$PROJECT_ROOT/docs/crisp-dm/$1"
  local phase_label="$2"

  if [ ! -d "$phase_dir" ]; then
    echo "$phase_label"
    return
  fi

  local count
  count=$(find "$phase_dir" -maxdepth 1 -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
  if [ "$count" -eq 0 ]; then
    echo "$phase_label"
  fi
}

# Map each skill to the phases it requires
REQUIRED_PHASES=""

case "$SKILL" in
  # Phase 1 skills and utility skills — no prerequisites
  define-business-objectives|assess-situation|determine-data-mining-goals|produce-project-plan)
    exit 0 ;;
  status|next|review-mr|sync-to-notion)
    exit 0 ;;

  # Phase 2 skills require Phase 1
  collect-initial-data|describe-data|explore-data|verify-data-quality)
    REQUIRED_PHASES="1-business-understanding:Phase 1 (Business Understanding)" ;;

  # Phase 3 skills require Phases 1-2
  select-data|clean-data|construct-data|integrate-data|format-data|select-features)
    REQUIRED_PHASES="1-business-understanding:Phase 1 (Business Understanding)
2-data-understanding:Phase 2 (Data Understanding)" ;;

  # Phase 4 skills require Phases 1-3
  select-modeling-techniques|generate-test-design|build-model|assess-model)
    REQUIRED_PHASES="1-business-understanding:Phase 1 (Business Understanding)
2-data-understanding:Phase 2 (Data Understanding)
3-data-preparation:Phase 3 (Data Preparation)" ;;

  # Phase 5 skills require Phases 1-4
  evaluate-results|review-process|determine-next-steps)
    REQUIRED_PHASES="1-business-understanding:Phase 1 (Business Understanding)
2-data-understanding:Phase 2 (Data Understanding)
3-data-preparation:Phase 3 (Data Preparation)
4-modeling:Phase 4 (Modeling)" ;;

  # Phase 6 skills require Phases 1-5
  plan-deployment|plan-monitoring|produce-final-report|review-project)
    REQUIRED_PHASES="1-business-understanding:Phase 1 (Business Understanding)
2-data-understanding:Phase 2 (Data Understanding)
3-data-preparation:Phase 3 (Data Preparation)
4-modeling:Phase 4 (Modeling)
5-evaluation:Phase 5 (Evaluation)" ;;

  # Unknown skill — don't block
  *) exit 0 ;;
esac

MISSING=""
while IFS=: read -r dir label; do
  [ -z "$dir" ] && continue
  result=$(check_phase "$dir" "$label")
  if [ -n "$result" ]; then
    MISSING="${MISSING}${result}, "
  fi
done <<< "$REQUIRED_PHASES"

if [ -n "$MISSING" ]; then
  MISSING=${MISSING%, }
  echo "{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"ask\",\"permissionDecisionReason\":\"CRISP-DM phase gate: missing prerequisite artifacts for ${MISSING}. Complete earlier phases first, or confirm to proceed anyway.\"}}"
fi
