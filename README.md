# Azure Functions Cucumber

Feature test Python Azure Functions locally and in pipelines.

## Goal

When developing Azure Functions, it can be helpful to have a self-contained test system that runs without resources in Azure. This is helpful for local development and especially in CI/CD Pipelines like Azure Pipelines, GitHub Actions, Travis, etc.

This repository provides solutions to feature test Azure Functions with several Azure components - steal whatever you need for your project.

## Components

- [x] Application: Docker Compose (`./bin/start`, `./bin/stop`) with
  - [x] Azure Functions Python
  - [ ] Azure Storage
  - [ ] Azure Key Vault
  - [ ] Azure Cosmos DB
  - [x] Wiremock
- [x] Testing
  - [x] Feature Tests with behave: `./bin/test`
  - [x] Unit Tests and coverage: `./bin/unit`
- [x] Linting: `./bin/lint`
  - [x] Static Type Checks with mypy
  - [x] Linting with pylint
  - [ ] Linting with flake8
- [x] Formatting: `./bin/format`
  - [x] Python
  - [x] Gherkin
  - [x] JSON
  - [x] Shell
- [ ] Upgrading / QoL
  - [x] Python Packages `./bin/upgrade`

## Running the System

Given Docker is installed (on Windows, WSL integration is recommended), use `./bin/start` to start the system and see the output. Once started, run `./bin/test` to run the feature tests.

## Details and notable Points of Interest

### Dockerfiles

The two Dockerfiles (`application/Dockerfile` and `development/Dockerfile`) are for development and testing only - do **not** use a Dockerfile to deploy your code to production.

All actions like testing, formatting, linting, etc. are done using a docker image and `./bin/dev` - so everyone (and every pipeline) uses the same packages.
