# Organizations API

## Endpoints

```mermaid
graph TD;
    organizations[Organizations API] --> |POST| create_org[Create Organization]
    organizations --> |GET| get_org[Get Organization]
    organizations --> |GET| list_orgs[List Organizations]
    organizations --> |PATCH| update_org[Update Organization]
    organizations --> |DELETE| delete_org[Delete Organization]
```

- **POST** `/api/organizations`: Create a new organization.
- **GET** `/api/organizations/{org_id}`: Retrieve a specific organization.
- **GET** `/api/organizations`: Retrieve a list of organizations.
- **PATCH** `/api/organizations/{org_id}`: Update a specific organization.
- **DELETE** `/api/organizations/{org_id}`: Delete a specific organization.
