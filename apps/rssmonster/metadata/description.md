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
- **Summary language** has no upstream setting. When set, the inference container
  patches a copy of its own source at startup: the bullet-summary prompt gains
  "in <language>, whatever the language of the article" and its token cap goes from
  250 to 400 (French needs more tokens), and a reminder follows the article text:
  with the instruction only before the content, qwen kept English on long English
  articles (0/2 vs 2/2 measured). Tags and scores are untouched. If a newer
  image no longer contains the patched lines, the container exits with
  `[summary-language] patch target not found` instead of silently summarizing in
  English: update the command in `docker-compose.json` along with the image tag.
- With a reasoning model, point **Generation model** at a variant with thinking
  disabled: RSSMonster caps answers at 100-400 tokens and the reasoning consumes them,
  leaving empty results that are still recorded as successful.

Not included from the upstream MySQL profile: MySQL itself. SQLite limits crawling
and AI jobs to one at a time, which is fine for a personal instance.

## Links

- Source: https://github.com/pietheinstrengholt/rssmonster
- Documentation: https://pietheinstrengholt.github.io/rssmonster/
