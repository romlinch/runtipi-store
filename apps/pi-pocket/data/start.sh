#!/bin/sh
# Démarrage de pi-pocket : en root, installe les paquets apt demandés (perdus à chaque recréation du
# conteneur), puis tout le reste tourne en utilisateur node (uid 1000). Le tag de pi-pocket est cloné et
# installé une seule fois dans /home/node/app (volume persistant).
set -eu

TAG="${PI_POCKET_TAG:?PI_POCKET_TAG manquant}"
SRC="/home/node/app/pi-pocket-$TAG"
as_node() { setpriv --reuid=1000 --regid=1000 --init-groups env HOME=/home/node "$@"; }

if [ -n "${PI_POCKET_APT:-}" ]; then
  # shellcheck disable=SC2086 # liste de paquets séparés par des espaces
  apt-get update -qq && apt-get install -y -qq --no-install-recommends $PI_POCKET_APT
fi

mkdir -p /home/node/app /home/node/.ssh /workspace
chown 1000:1000 /home/node /home/node/app /home/node/.ssh /workspace
chmod 700 /home/node/.ssh

if [ ! -f "$SRC/.installed" ]; then
  rm -rf "$SRC"
  as_node git clone --quiet --depth 1 --branch "$TAG" https://github.com/TannerMidd/pi-pocket.git "$SRC"
  as_node sh -c "cd '$SRC' && npm ci --no-audit --no-fund"
  as_node touch "$SRC/.installed"
fi

cd "$SRC"
exec setpriv --reuid=1000 --regid=1000 --init-groups env HOME=/home/node PATH="/home/node/.local/bin:$PATH" \
  node bin/pi-pocket.js --host 0.0.0.0 --port 8787 --cwd /workspace
