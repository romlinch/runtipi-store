# Atelier de code

Atelier pour apprendre le JavaScript aux enfants, entièrement dans le navigateur : pas d'IDE à installer.

- **Un objectif qui en jette** : la mission 0 montre un vrai jeu (une licorne attrape des fraises et fuit un fantôme). Les 14 missions suivantes le font construire ligne par ligne : variables, animation, `if`, clavier, hasard, collisions, tableaux, boucles.
- **Tout en français** : petite bibliothèque française (`fond`, `emoji`, `texte`, `touche`, `auHasard`…), mots-clés anglais traduits (aide-mémoire + survol dans l'éditeur), erreurs du navigateur traduites.
- **Pixel 🤖** : assistant Qwen via LiteLLM. À chaque question, la page lui envoie la mission, le code (numéroté) et la dernière erreur : il voit ce que fait l'enfant sans tool call. Consigne : guider, ne jamais donner la solution complète.
- **Un projet par enfant**, enregistré sur le serveur (`data/projets/<prénom>.json`, écriture atomique) : on retrouve son jeu depuis n'importe quel PC, et « 👀 Jouer au jeu de… » lance le jeu de sa sœur.

## Fichiers

`data/` est copié dans `app-data/<store>/atelier-code/data/` **à la première installation seulement** (comportement runtipi). Pour publier une nouvelle version de la page ou du serveur :

```bash
scp apps/atelier-code/data/{index.html,server.py} khadas@192.168.1.91:/var/lab/runtipi/app-data/romlinch/atelier-code/data/
```

`index.html` est relu à chaque requête (rien à redémarrer) ; `server.py` demande un redémarrage de l'app.

## Clé LiteLLM

Créer une clé virtuelle limitée au modèle (`models: ["qwen-nothink"]`) : le serveur impose aussi le modèle, mais la clé ne doit rien pouvoir faire d'autre.

## Développement local

```bash
LITELLM_KEY=... PROJETS_DIR=/tmp/projets uv run apps/atelier-code/data/server.py   # http://localhost:8000
```
