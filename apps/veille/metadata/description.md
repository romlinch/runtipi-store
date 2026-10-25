# Veille

Lecteur RSS mono-utilisateur pensé pour suivre beaucoup de sources sans lire dix fois la même information.

- **Texte complet** : chaque article est extrait par crawl4ai ; les articles derrière un paywall sont écartés.
- **Notation par Jev** (modèle de décision TypeSafe) : qualité, publicité déguisée, titre racoleur, domaine (informatique, tech, news, culture) et tags définis dans la configuration.
- **Regroupement par sujet** : les articles qui traitent de la même actualité forment une seule carte, avec une synthèse en français de toutes les sources et un lien vers le meilleur article.
- **Lecture** : cartes avec image, tri par jour puis par intérêt, lu au fil du défilement et synchronisé entre appareils, favoris conservés au-delà des 15 jours de rétention, « Tout marquer comme lu ».

## Fichiers

L'image est une Debian nue : le binaire et la configuration vivent dans `app-data/<store>/veille/data/`.

- `bin/veille` : le serveur (compilé pour l'architecture de l'hôte) ;
- `config.toml` : flux, dossiers, domaines, tags, réglages IA (rechargé à chaud) ;
- `password-hash` : hash argon2 du mot de passe (`veille hash-password < fichier`) ;
- `veille.db`, `content/`, `images/` : données (15 jours, favoris conservés).

Le code et le script de déploiement (compilation sur l'hôte puis copie dans `data/`) sont dans le dépôt du projet, pas dans ce store.
