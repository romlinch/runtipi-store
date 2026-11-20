#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

echo "=== $(date) ==="
git pull --rebase

./update.sh

if ! git diff --quiet --exit-code || ! git diff --cached --quiet --exit-code; then
  git add -A
  git commit -m "chore: update $(date +%Y-%m-%d)"
  git push
  echo "Commité et poussé."
else
  echo "Aucun changement."
fi
