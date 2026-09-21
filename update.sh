#!/usr/bin/env bash
# Lance Renovate en local sur ce dépôt (crée les branches/PR sur GitHub).
# Les postUpgradeTasks sont autorisées par config.js à la racine.
# DRY_RUN=full ./update.sh  -> simulation, n'écrit rien.
set -euo pipefail

export RENOVATE_TOKEN="${RENOVATE_TOKEN:-$(gh auth token)}"
export LOG_LEVEL="${LOG_LEVEL:-INFO}"
export RENOVATE_DRY_RUN="${DRY_RUN:-}"

exec bunx renovate@40 romlinch/runtipi-store
