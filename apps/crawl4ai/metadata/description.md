# Crawl4AI

Open-source web crawler built for LLM pipelines. It renders pages with headless Chromium and returns clean, chunked markdown instead of raw HTML.

## Features

- REST API (`/crawl`, `/md`, `/html`, `/screenshot`, `/pdf`) and an MCP endpoint at `/mcp/sse`
- Deep crawling with depth and page budgets
- Extraction via CSS/XPath selectors, regex, or an LLM
- Playground UI at `/playground`

## Usage

The API token is mandatory: without `CRAWL4AI_API_TOKEN` the server binds loopback only and Runtipi cannot reach it. Pass it on every call:

```bash
curl -X POST http://<host>:11235/md \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

## LLM extraction

The LLM fields point Crawl4AI at any OpenAI-compatible endpoint. With LiteLLM installed on the same Runtipi instance, use `http://litellm:4000/v1` as the base URL and a model id from your LiteLLM config as the provider (`openai/<model>`).

## Resources

Each open page costs roughly 400 MB of RAM. The memory limit defaults to 4 GB, which comfortably covers a handful of concurrent crawls; lower it on small hosts and raise it for batch workloads.
