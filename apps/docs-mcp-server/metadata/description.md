# Docs MCP Server

Docs MCP Server enhances your AI coding assistant by providing up-to-date, accurate documentation. It solves common AI documentation challenges like stale knowledge and code hallucinations by indexing and searching documentation from various sources.

## Features

- **Local and Private**: All data processing happens locally on your machine
- **Free and Open-Source**: MIT licensed with full source code availability
- **Multiple Sources**: Index documentation from websites, GitHub repositories, npm packages, PyPI packages, and local files
- **Web Interface**: Easy-to-use web interface for managing documentation sources
- **MCP Integration**: Built-in Model Context Protocol endpoints for AI integration

## Configuration

The application is pre-configured to work with Ollama by default for local, private embeddings. You can configure:

- **OpenAI API Key**: Pre-configured for Ollama (default: "ollama")
- **OpenAI API Base**: API endpoint URL (default: http://localhost:11434/v1 for Ollama)
- **Embedding Model**: Embedding model to use (default: nomic-embed-text for Ollama)
- **Port**: Configure the web interface port (default: 6280)

For OpenAI instead of Ollama, change the API key to your OpenAI key, set API base to https://api.openai.com/v1, and use text-embedding-3-small as the model.

## Usage

Once deployed, access the web interface to:

1. Add documentation sources (URLs, GitHub repos, npm/PyPI packages)
2. Index documentation content
3. Search through indexed documentation
4. Integrate with AI coding assistants via MCP endpoints

## MCP Endpoints

The server provides MCP (Model Context Protocol) endpoints at:
- `/sse` - Server-Sent Events endpoint
- `/mcp` - Main MCP endpoint

## Data Storage

Documentation data is stored persistently in the `/data` directory within the container, mapped to your Runtipi app data directory.