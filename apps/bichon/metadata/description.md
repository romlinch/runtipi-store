# Bichon

A lightweight, high-performance self-hosted email archiver written in Rust. Bichon synchronizes emails from IMAP servers, indexes them for full-text search, and provides a clean WebUI — with no external database required.

## Features

- **Multi-Account Sync** — Download and manage emails from multiple IMAP accounts
- **Full-Text Search** — Search across all accounts by sender, subject, body, date, and attachments
- **No External DB** — Pure Rust, self-contained, no PostgreSQL or Elasticsearch needed
- **Authentication** — Password and OAuth2 login with automatic token refresh
- **Storage Efficiency** — Transparent compression and message deduplication
- **Email Management** — Browse threads, bulk cleanup, and EML/attachment export
- **Multi-User** — Role-based access control (admin and user roles)
- **REST API** — OpenAPI-documented API with access-token authentication
- **Internationalization** — WebUI available in 18 languages

## Usage

1. Open the WebUI and log in with the default admin account
2. Add your IMAP accounts under Settings
3. Trigger a sync or let Bichon sync automatically
4. Search and browse your archived emails
