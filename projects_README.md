# Projects API

## Endpoints

```mermaid
graph TD;
    projects[Projects API] --> |POST| create_project[Create Project]
    projects --> |GET| list_projects[List Projects]
    projects --> |PATCH| update_project[Update Project]
    projects --> |PUT| archive_project[Archive Project]
    projects --> |GET| get_project[Get Project]
    projects --> |DELETE| delete_project[Delete Project]
```

- **POST** `/api/projects`: Create a new project.
- **GET** `/api/projects`: Retrieve a list of projects.
- **PATCH** `/api/projects/{project_id}`: Update a specific project.
- **PUT** `/api/projects/{project_id}/archive`: Archive a specific project.
- **GET** `/api/projects/{project_id}`: Retrieve a specific project.
- **DELETE** `/api/projects/{project_id}`: Delete a specific project.
