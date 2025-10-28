# Litellm

A unified LLM proxy server that provides a single standardized interface to interact with multiple language models across different providers.

## Features

- **Multi-Model Support**: Access various LLM providers through a single API
- **Provider Integration**: Support for OpenRouter, OpenAI, and other LLM providers
- **Database Persistence**: PostgreSQL backend for storing model configurations
- **API Gateway**: Standardized API endpoint for all LLM requests
- **Model Management**: Dynamic model registration and configuration
- **Worker Pool**: Configurable worker threads for handling concurrent requests
- **Authentication**: Master key-based API authentication

## Components

### Litellm Proxy Server
- High-performance proxy server built with Python
- Unified REST API for LLM interactions
- Automatic request routing to appropriate providers
- Support for streaming and non-streaming responses
- Built-in logging and monitoring

### PostgreSQL Database
- Persistent storage for model configurations
- Support for custom model definitions
- Database-backed model registry
- Data retention and backup capabilities

## Use Cases

- **API Consolidation**: Unify multiple LLM provider APIs into one endpoint
- **Cost Optimization**: Route requests to most cost-effective providers
- **Model Flexibility**: Switch between providers without changing application code
- **Multi-Tenant Systems**: Support multiple users/teams with separate configurations
- **Development & Testing**: Easy provider switching during development
- **Production Deployment**: Reliable, scalable LLM inference endpoint

## API Endpoints

### Main Proxy Port
- **4000**: Litellm proxy API (main port)

## Configuration

### Required Settings
- **Master API Key**: Authentication key for proxy requests
- **Database URL**: PostgreSQL connection string (pre-configured with internal database)

### Optional Settings
- **OpenRouter API Key**: For accessing OpenRouter models
- **Worker Threads**: Number of concurrent request handlers (default: 8)
- **Store Models in Database**: Enable/disable persistent model storage

## Getting Started

1. Install Litellm from the app store
2. Configure your API keys (Master Key is required)
3. Add provider API keys (OpenRouter, etc.) as needed
4. Access the proxy at `http://your-server:4000`
5. Send LLM requests to the unified API endpoint

## Example Usage

### Request to Litellm Proxy
```bash
curl -X POST http://localhost:4000/chat/completions \
  -H "Authorization: Bearer sk-1234" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openrouter/openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## Requirements

- Minimum 1GB RAM
- PostgreSQL database (included)
- API keys for LLM providers you want to use
- Network access to provider APIs

## Architecture

- **Scalable**: Horizontal scaling with load balancing
- **Stateless Proxy**: Requests routed independently
- **Database-Backed**: Persistent model registry
- **Provider Agnostic**: Easy to add new providers

## Documentation

- [Litellm GitHub](https://github.com/BerriAI/litellm)
- [Litellm Documentation](https://docs.litellm.ai/)
- [Provider Integration Guide](https://docs.litellm.ai/docs/providers)

## Security

- Master key authentication for all requests
- Secure credential storage in database
- Environment variable-based API key management
- HTTPS support (configure in your proxy)

## Troubleshooting

### Database Connection Issues
- Verify PostgreSQL service is running
- Check DATABASE_URL configuration
- Ensure network connectivity between services

### Provider API Errors
- Verify API keys are correctly set
- Check provider service status
- Review Litellm logs for detailed error messages

### Performance Optimization
- Adjust NUM_WORKERS based on system capacity
- Monitor database query performance
- Configure model caching where applicable