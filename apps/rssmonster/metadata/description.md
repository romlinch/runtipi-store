# RSSMonster

Modern, self-hosted, multi-user RSS reader built with Vue and Express.

## Features

- Three-pane reading layout, keyboard shortcuts, installable web app
- Smart folders, tags, bookmarks, full-text search
- OPML import/export
- Fever and Google Reader API compatibility (mobile clients)
- Optional AI enrichment (summaries, embeddings, assistant) through a separate inference service

## First login

There is no default account. Open the app, select **Create an account**: the first
registered account becomes admin. Then disable **Allow registration** in the app
settings before exposing the instance publicly.

## Configuration

| Field | Env variable | Notes |
| --- | --- | --- |
| JWT secret | `JWT_SECRET` | Generated. Rotating it signs every user out. |
| Fever credential secret | `FEVER_CREDENTIAL_SECRET` | Generated. Also derives the key encrypting stored inference API keys. |
| Allow registration | `ALLOW_REGISTRATION` | Disabling it hides signup; existing accounts still log in. |

## Data

SQLite database under `${APP_DATA_DIR}/data`. Two containers share it: the web app
(runs migrations on start) and the crawl worker, which waits for the app to be healthy.

## Not included

The upstream MySQL profile adds MySQL, an AI worker and an inference service. SQLite
limits crawling and optional jobs to one at a time, which is fine for a personal
instance. AI enrichment needs the AI worker and an inference service reachable via
`INFERENCE_BASE_URL`.

## Links

- Source: https://github.com/pietheinstrengholt/rssmonster
- Documentation: https://pietheinstrengholt.github.io/rssmonster/
