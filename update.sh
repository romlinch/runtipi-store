#!/usr/bin/env bash
# Lance Renovate en local sur ce dépôt (crée les branches/PR sur GitHub).
# Les postUpgradeTasks sont autorisées par config.js à la racine.
# DRY_RUN=full ./update.sh  -> simulation, n'écrit rien.
set -euo pipefail

# Jeton fine-grained limité à ce dépôt, chiffré par sops dans le dépôt services ; repli : gh.
export RENOVATE_TOKEN="${RENOVATE_TOKEN:-$(sops decrypt ~/perso/dev/services/renovate/renovate.sops.env 2>/dev/null | sed -n 's/^RENOVATE_TOKEN=//p')}"
export RENOVATE_TOKEN="${RENOVATE_TOKEN:-$(gh auth token)}"
# ~/.npmrc pointe vers le registre pro, injoignable hors VPN.
export BUN_CONFIG_REGISTRY="https://registry.npmjs.org"
export LOG_LEVEL="${LOG_LEVEL:-INFO}"
export RENOVATE_DRY_RUN="${DRY_RUN:-}"

exec bunx renovate@40 romlinch/runtipi-store
