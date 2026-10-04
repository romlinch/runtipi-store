# VictoriaLogs

Base de logs de [VictoriaMetrics](https://docs.victoriametrics.com/victorialogs/) : un seul binaire, peu de RAM, forte compression, recherche en [LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/) et interface web intégrée (`/select/vmui`).

L'interface est protégée par une authentification basique : utilisateur `admin`, mot de passe généré à l'installation.

## Alimentation

L'app écoute le syslog en TCP sur `127.0.0.1:5141` (hôte uniquement). Le rsyslog de l'hôte y relaie les logs, avec l'heure de réception en RFC 5424 :

```
template(name="VLogsFormat" type="string"
         string="<%PRI%>1 %timegenerated:::date-rfc3339% %HOSTNAME% %APP-NAME% %PROCID% - -%msg:::sp-if-no-1st-sp%%msg:::drop-last-lf%\n")

action(type="omfwd" target="127.0.0.1" port="5141" protocol="tcp" template="VLogsFormat"
       queue.type="LinkedList" queue.size="100000" queue.timeoutEnqueue="0"
       action.resumeRetryCount="-1" action.resumeInterval="10")
```

`queue.timeoutEnqueue="0"` : si l'app est arrêtée, la file garde 100 000 lignes puis les jette, sans jamais bloquer les autres actions du ruleset.

Les flux sont découpés par `hostname` et `app_name`. Exemples de requêtes :

- `hostname:OpenWrt app_name:upsmon`
- `app_name:kernel "banIP" | stats by (hostname) count()`

Source : https://github.com/VictoriaMetrics/VictoriaLogs
