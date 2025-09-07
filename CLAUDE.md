# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Runtipi app store template for creating custom app stores. The repository follows a specific structure for managing containerized applications with standardized configuration files.

## Core Architecture

- **apps/**: Each app directory contains:
  - `config.json`: App metadata, configuration options, and form fields
  - `docker-compose.json`: Docker service definitions with environment variables and volumes
  - `metadata/`: Visual assets (`logo.jpg`) and documentation (`description.md`)

- **App Configuration Schema**: Apps use `appInfoSchema` and `dynamicComposeSchema` from `@runtipi/common/schemas` for validation

- **Dynamic Configuration**: Apps support form fields for user input that map to environment variables

## Development Commands

- **Install dependencies**: `bun install`
- **Run tests**: `bun test`
- **Update app configurations**: `bun ./scripts/update-config.ts`

The test suite validates:
- Required files existence for each app
- Valid `config.json` against the schema
- Valid `docker-compose.json` against the schema

## App Structure Requirements

Each app must have:
1. `config.json` with complete metadata including categories, descriptions, and form fields
2. `docker-compose.json` with services, environment variables, and volumes
3. `metadata/logo.jpg` for the app icon
4. `metadata/description.md` for detailed app documentation

## Key Dependencies

- `@runtipi/common`: Provides validation schemas for app configurations
- `bun`: Runtime and test framework
- `zod-validation-error`: Enhanced validation error messages

## Configuration Management

Apps use environment variable substitution in `docker-compose.json` with form fields in `config.json` defining user-configurable options. The `dynamic_config` flag enables runtime configuration management.