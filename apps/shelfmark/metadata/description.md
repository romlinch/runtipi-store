# Shelfmark

Shelfmark is a self-hosted web interface for searching and requesting books and audiobooks across multiple sources. Bring your own sources, metadata providers, and download clients to build a single hub for your digital library. Supports multiple users with a built-in request system, so you can share your instance with others and let them browse and request books on their own.

Works great alongside the following library tools, with support for automatic imports:

- [Calibre](https://calibre-ebook.com/)
- [Calibre-Web](https://github.com/janeczku/calibre-web)
- [Calibre-Web-Automated](https://github.com/crocodilestick/Calibre-Web-Automated)
- [Grimmory](https://github.com/grimmory-tools/grimmory)
- [Audiobookshelf](https://github.com/advplyr/audiobookshelf)

## Features

- **One-Stop Interface** - A clean, modern UI to search, browse, and download from multiple configured sources in one place
- **Multiple Sources** - Configurable web, torrent, usenet, and IRC source support
- **Audiobook Support** - Full audiobook search and download with dedicated processing
- **Flexible Search** - Search metadata providers (Hardcover, Open Library, Google Books) for rich book and audiobook discovery, or query configured sources directly
- **Multi-User & Requests** - Share your instance with others, let users browse and request books, and manage approvals with configurable notifications
- **Authentication** - Built-in login, OIDC single sign-on, proxy auth, and Calibre-Web database support
- **Real-Time Progress** - Unified download queue with live status updates across all sources
- **Network Flexibility** - Configurable proxy support, DNS settings, and optional Cloudflare handling for protected sources

## Search Modes

- **Universal** (recommended): search via metadata providers (Hardcover, Open Library, Google Books) for richer results, aggregating releases from multiple configured sources, with full audiobook support.
- **Direct**: queries configured sources directly.

## Volumes

- `${APP_DATA_DIR}/config` → `/config` — app configuration, database, and artwork cache
- `${ROOT_FOLDER_HOST}/media/data/books/ebooks` → `/books` — book download destination (shared with Calibre-Web-Automated ingest folder for automatic imports)

> **Tip**: Pointing the download volume to your CWA or Grimmory ingest folder enables automatic import.

## Tor Routing

To enable Tor routing, set the **Enable Tor routing** option to true. Note this requires running the container as root and additional `NET_ADMIN` / `NET_RAW` capabilities, which Runtipi may not grant by default — for full Tor support, prefer running the dedicated `docker-compose.tor.yml` from the upstream project manually.

## Project Scope

Shelfmark is a manual search and download tool, the entry point to your book library, not a library manager. It finds books, downloads them, and sends them to a configured destination. It intentionally does not track or manage your library, monitor authors/series for new releases, or queue future downloads.

## Disclaimer

Shelfmark is a search interface that displays results from external metadata providers and sources. It does not host, store, or distribute any content. Users are solely responsible for ensuring they have the legal right to download any material they access and for complying with copyright laws in their jurisdiction.
