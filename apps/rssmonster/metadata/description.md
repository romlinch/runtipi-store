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

SQLite database under `${APP_DATA_DIR}/data`, shared by the web app (runs migrations
on start), the crawl worker and the AI worker.

On first install both containers restart a few times: the image runs as a non-root
user and the data directories only become writable once Runtipi applies its
permissions after `docker compose up`. The worker does not wait for the app to be
healthy on purpose: that wait makes `compose up` fail, and Runtipi then skips the
permission step entirely.

## AI

Four containers: web app, crawl worker, AI worker and inference service. Every
capability (embeddings, summaries/tags, scoring, assistant) is sent to the single
OpenAI-compatible endpoint configured in the form, typically a LiteLLM gateway. No
model is downloaded or run locally, so the inference container stays small.

- **Enable AI** is the server-side switch. The inference container needs a base URL
  and a non-empty API key to start: without them it restarts in a loop, harmlessly.
- **Embedding model** cannot be changed once articles have vectors: RSSMonster does
  not migrate vectors between models.
- Timeouts are 15 minutes, to survive a cold model load on the gateway side.

Not included from the upstream MySQL profile: MySQL itself. SQLite limits crawling
and AI jobs to one at a time, which is fine for a personal instance.

## Links

- Source: https://github.com/pietheinstrengholt/rssmonster
- Documentation: https://pietheinstrengholt.github.io/rssmonster/
