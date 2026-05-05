# Calibre-Web Automated

Calibre-Web Automated (CWA) is a self-hosted eBook library combining the modern Calibre-Web interface with Calibre's conversion engine and a full suite of automations.

## Features

- **Auto-Ingestion** — Drop files into a folder to automatically import and convert to your preferred format (EPUB, AZW3, etc.)
- **Metadata Enforcement** — Changes made in the UI are written back to the actual eBook files for cross-device consistency
- **EPUB Fixer** — Automatically repairs broken encoding and formatting issues for Send-to-Kindle compatibility
- **Send to eReader** — Send books directly to Kindle and other eReaders via email
- **KOReader Sync** — Sync reading progress from KOReader devices
- **Hardcover Integration** — Sync reading activity with your Hardcover.app account via API token
- **Auto Library Setup** — Automatically detects and registers your Calibre library on first start
- **OPDS Server** — Built-in OPDS catalog for compatible e-reader apps
- **Dark Mode** — Full dark mode support in the UI

## Configuration

- **eBook library** is mounted from `{data}/media/data/books/ebooks`
- **Hardcover token** can be set in the app settings for reading progress sync
- **Plugins** are persisted in the app data directory

## Usage

1. Access the WebUI and log in (default: `admin` / `admin123`)
2. Change the admin password immediately
3. Add IMAP credentials under Settings > Send to Kindle if needed
4. Drop eBooks into the ingest folder to start automating imports
