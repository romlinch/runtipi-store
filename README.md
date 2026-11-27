# runtipi-store

Store [Runtipi](https://runtipi.io) personnel : des apps absentes du store officiel, ou adaptées (réglages, images, versions).

## Utiliser le store

Dans Runtipi : **Paramètres → App stores → Ajouter**, avec l'URL `https://github.com/romlinch/runtipi-store`.
Les apps apparaissent ensuite dans le store, à côté des apps officielles.

## Apps

| App | Description |
|---|---|
| `atelier-code` | Les enfants apprennent le JavaScript en codant leur propre jeu vidéo, guidés par un LLM |
| `bichon` | Archiveur d'e-mails en Rust, avec interface web |
| `calibre-web-automated` | Calibre-Web avec conversion, métadonnées et import automatiques |
| `crawl4ai` | Crawler et scraper web pour LLM, API REST |
| `crowdsec-web-ui` | Tableau de bord CrowdSec : alertes, décisions, métriques |
| `degoog` | Métamoteur de recherche privé |
| `frigate` | Enregistreur vidéo avec détection d'objets |
| `immich-machine-learning` | Backend ML d'Immich seul, pour un serveur Immich distant |
| `litellm` | Proxy LLM multi-fournisseurs avec API unifiée |
| `llama-cpp` | Serveur LLM local (mode routeur, chargement à la demande) |
| `music-assistant` | Bibliothèque musicale diffusée vers les enceintes connectées |
| `pi-pocket` | Interface web mobile pour l'agent de code Pi |
| `pocket-id` | Fournisseur OIDC à connexion par passkey |
| `rssmonster` | Lecteur RSS auto-hébergé |
| `shelfmark` | Recherche et demandes de livres et livres audio |
| `stable-diffusion-cpp` | Génération d'images locale, API compatible OpenAI |
| `tinyauth` | Serveur d'authentification minimal (forward auth) |
| `transmission-gluetun` | Transmission derrière un tunnel VPN Gluetun |
| `vector` | Envoie les logs des conteneurs Docker vers VictoriaLogs |
| `veille` | Lecteur RSS qui regroupe les articles d'un même sujet |
| `victoria-logs` | Base de logs avec recherche web, alimentée en syslog |
| `wallos` | Suivi des abonnements |

## Structure d'une app

```
apps/<id>/
├── config.json          # métadonnées, version, champs du formulaire (env_variable)
├── docker-compose.json  # services, variables ${VAR} remplies par le formulaire
└── metadata/
    ├── description.md
    └── logo.jpg
```

Le format est celui du [guide Runtipi](https://runtipi.io/docs/guides/create-your-own-app-store).

## Développement

```sh
bun install
bun test                                            # valide toutes les apps contre les schémas Runtipi
bun ./scripts/update-config.ts apps/<id>/config.json <version>   # version + tipi_version + updated_at
```

## Mises à jour (Renovate)

Renovate suit les tags d'image des `docker-compose.json` (et la release GitHub de `pi-pocket`),
puis ouvre une PR par app ; `postUpgradeTasks` met à jour `config.json` et relance les tests.
Les bases de données (postgres, redis…) sont exclues. Config : `renovate.json`.

- Automatique : workflow `.github/workflows/renovate.yml`, tous les jours, avec le secret `RENOVATE_TOKEN`
  (jeton fine-grained limité à ce dépôt). Les PR patch/minor sont fusionnées seules quand les tests passent ;
  les majeures attendent une revue.
- À la main : `./update.sh` (`DRY_RUN=full ./update.sh` pour simuler). Le jeton vient de `RENOVATE_TOKEN`,
  d'un fichier sops local s'il existe, sinon de `gh auth token`.
