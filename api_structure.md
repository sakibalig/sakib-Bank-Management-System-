# API Structure Visualization

This document visualizes the structure of the APIs and their connections using Mermaid.js.

```mermaid
graph TD;
    api_router[API Router] --> organizations[Organizations API]
    api_router --> projects[Projects API]
    api_router --> folders[Folders API]
    api_router --> test_files[Test Files API]
    api_router --> apks[APKs API]
    api_router --> apk_versions[APK Versions API]
    api_router --> github[GitHub API]
    api_router --> apis[APIs API]
    api_router --> testplans[Test Plans API]
    api_router --> report[Report API]
    api_router --> slack[Slack API]
    api_router --> admin[Admin API]
```
