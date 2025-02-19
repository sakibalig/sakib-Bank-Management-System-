# APK Versions API

## Endpoints

```mermaid
graph TD;
    apk_versions[APK Versions API] --> |POST| upload_apk_version[Upload APK Version]
    apk_versions --> |GET| list_releases[List Releases]
    apk_versions --> |POST| filter_releases[Filter Releases]
```

- **POST** `/api/apk-versions/{apk_id}/upload`: Upload a new APK version.
- **GET** `/api/apk-versions/{apk_id}/releases`: Retrieve releases for an APK.
- **POST** `/api/apk-versions/releases/filter`: Filter releases.
