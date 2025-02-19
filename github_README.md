# GitHub API

## Endpoints

```mermaid
graph TD;
    github[GitHub API] --> |POST| init_installation[Initialize Installation]
    github --> |GET| get_installation_status[Get Installation Status]
    github --> |POST| handle_webhooks[Handle Webhooks]
    github --> |POST| create_repo[Create Repository]
    github --> |POST| push_code[Push Code]
    github --> |GET| get_integration[Get Integration]
    github --> |DELETE| delete_integration[Delete Integration]
    github --> |GET| list_repositories[List Repositories]
    github --> |POST| sync_with_github[Sync with GitHub]
```

- **POST** `/api/github/installation/init`: Initialize GitHub installation.
- **GET** `/api/github/installation/{session_id}/status`: Retrieve installation status.
- **POST** `/api/github/webhooks`: Handle GitHub webhooks.
- **POST** `/api/github/create_repo`: Create a new GitHub repository.
- **POST** `/api/github/push_code`: Push code to GitHub.
- **GET** `/api/github/integration`: Retrieve GitHub integration.
- **DELETE** `/api/github/integration`: Delete GitHub integration.
- **GET** `/api/github/repositories`: Retrieve GitHub repositories.
- **POST** `/api/github/sync`: Sync with GitHub.
