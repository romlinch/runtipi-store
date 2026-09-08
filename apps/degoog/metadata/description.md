# Degoog

Self-hosted, privacy-respecting metasearch engine. Degoog queries multiple search
engines on your behalf and returns aggregated results with no profiling, no logging
and no ads.

## Features

- Metasearch across many engines, configurable per instance
- Shortcuts / bangs, custom themes, extensions store
- Optional indexer for your own content
- No accounts, no tracking, no telemetry
- Can be set as the default search engine in any browser (OpenSearch)

## Configuration

| Field | Env variable | Notes |
| --- | --- | --- |
| Settings password | `DEGOOG_SETTINGS_PASSWORDS` | Required. Gates admin and extension-store actions. |
| Public instance | `DEGOOG_PUBLIC_INSTANCE` | When enabled, admin/store actions stay behind the password even on the LAN. |

**Security**: an instance without a settings password lets anyone install extensions,
which executes code on the server. Always set a strong password before exposing it.

## Data

Persisted under `${APP_DATA_DIR}/data` (settings, engines, plugins, indexer).

## Scaling

Upstream also ships Valkey (shared cache) and PostgreSQL (indexer backend) setups
for high-traffic public instances. This app is the minimal single-container variant
with in-memory cache, which is what a personal instance needs.

## Links

- Source: https://github.com/degoog-org/degoog
- Public instances: https://github.com/degoog-org/degoog/blob/main/PUBLIC_INSTANCES.md
