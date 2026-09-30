# CrowdSec Web UI

Tableau de bord auto-hébergé pour [CrowdSec](https://www.crowdsec.net/) :

- historique des alertes, conservé dans sa propre base SQLite (la LAPI n'en garde qu'un nombre limité) ;
- décisions actives et expirées, bannir / débannir une IP ;
- métriques d'exécution.

Il se connecte à l'API locale de CrowdSec avec un **compte machine** : après l'installation, enregistrer le mot de passe généré côté CrowdSec :

```
sudo cscli machines add crowdsec-web-ui --password '<mot de passe généré>' -f /dev/null
```

L'interface a sa propre authentification (compte administrateur créé à la première connexion).

Source : https://github.com/TheDuffman85/crowdsec-web-ui
