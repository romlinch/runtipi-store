# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Runtipi app store template for creating custom app stores. The repository follows a specific structure for managing containerized applications with standardized configuration files.

Official documentation: https://runtipi.io/docs/guides/create-your-own-app-store

## Development Commands

- **Install dependencies**: `bun install`
- **Run all tests**: `bun test`
- **Run a single test**: `bun test --test-name-pattern "app <app-name>"`
- **Update app config version**: `bun ./scripts/update-config.ts <path-to-any-file-in-app-dir> <new-version>`
  - Example: `bun ./scripts/update-config.ts apps/litellm/config.json 1.2.0`

## Core Architecture

### App Structure

Each app in `apps/<app-name>/` must contain:
- `config.json` - App metadata validated against `appInfoSchema` from `@runtipi/common/schemas`
- `docker-compose.json` - Docker service definitions validated against `dynamicComposeSchema`
- `metadata/logo.jpg` - App icon
- `metadata/description.md` - Detailed app documentation

### Configuration Flow

Form fields in `config.json` define user-configurable options with `env_variable` mappings. These environment variables are then substituted in `docker-compose.json` using `${VAR_NAME}` syntax. The `dynamic_config: true` flag enables runtime configuration management.

### Validation

Tests in `__tests__/apps.test.ts` validate all apps against the schemas. Run tests before committing new apps or changes.