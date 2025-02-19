# APKs API

## Endpoints

```mermaid
graph TD;
    apks[APKs API] --> |POST| create_apk[Create APK]
    apks --> |GET| list_apks[List APKs]
    apks --> |GET| get_apk[Get APK]
    apks --> |PATCH| update_apk[Update APK]
    apks --> |DELETE| delete_apk[Delete APK]
```

- **POST** `/api/apks`: Create a new APK.
- **GET** `/api/apks/organization-apks`: Retrieve APKs for an organization.
- **GET** `/api/apks/{apk_id}`: Retrieve a specific APK.
- **PATCH** `/api/apks/{apk_id}`: Update a specific APK.
- **DELETE** `/api/apks/{apk_id}`: Delete a specific APK.
