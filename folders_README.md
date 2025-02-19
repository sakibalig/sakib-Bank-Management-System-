# Folders API

## Endpoints

```mermaid
graph TD;
    folders[Folders API] --> |POST| create_folder[Create Folder]
    folders --> |GET| get_folder[Get Folder]
    folders --> |GET| list_folders[List Folders]
    folders --> |PATCH| update_folder[Update Folder]
    folders --> |DELETE| delete_folder[Delete Folder]
```

- **POST** `/api/folders`: Create a new folder.
- **GET** `/api/folders/{folder_id}`: Retrieve a specific folder.
- **GET** `/api/folders/project/{project_id}`: Retrieve folders in a project.
- **PATCH** `/api/folders/{folder_id}`: Update a specific folder.
- **DELETE** `/api/folders/{folder_id}`: Delete a specific folder.
