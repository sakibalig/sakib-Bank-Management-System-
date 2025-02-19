# APIs API

## Endpoints

```mermaid
graph TD;
    apis[APIs API] --> |POST| create_api[Create API]
    apis --> |GET| list_apis[List APIs]
    apis --> |GET| get_api[Get API]
    apis --> |PATCH| update_api[Update API]
    apis --> |DELETE| delete_api[Delete API]
```

- **POST** `/api/apis`: Create a new API.
- **GET** `/api/apis`: Retrieve a list of APIs.
- **GET** `/api/apis/{api_id}`: Retrieve a specific API.
- **PATCH** `/api/apis/{api_id}`: Update a specific API.
- **DELETE** `/api/apis/{api_id}`: Delete a specific API.
