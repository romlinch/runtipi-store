# Vector (logs Docker)

Agent [Vector](https://vector.dev/) qui lit les logs de **tous les conteneurs Docker de l'hôte** via le socket Docker (en lecture seule) et les envoie à [VictoriaLogs](https://docs.victoriametrics.com/victorialogs/) (app `victoria-logs`) par son API Elasticsearch.

Champs envoyés, alignés sur les logs syslog :

- `hostname` : nom saisi à l'installation (ex. `Khadas`, `big`) ;
- `app_name` : nom du conteneur ;
- `image`, `container_id`, `stream` (stdout / stderr).

Exemples de requêtes : `hostname:Khadas app_name:~"traefik"`, `stream:stderr`.

Les conteneurs dont le nom commence par `vector_` (cet agent) sont exclus. Si VictoriaLogs est indisponible, Vector ralentit sa lecture et reprend là où il en était : Docker garde les logs entre-temps.

La configuration est copiée à l'installation dans `app-data/<store>/vector/data/vector.yaml`.

Source : https://github.com/vectordotdev/vector
