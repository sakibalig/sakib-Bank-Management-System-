# Test Files API

## Endpoints

```mermaid
graph TD;
    test_files[Test Files API] --> |GET| get_test_file[Get Test File]
    test_files --> |POST| create_test_file[Create Test File]
    test_files --> |PATCH| update_test_file[Update Test File]
    test_files --> |DELETE| delete_test_file[Delete Test File]
```

- **GET** `/api/test-files/folder/{folder_id}`: Retrieve test files in a folder.
- **GET** `/api/test-files/{test_file_id}`: Retrieve a specific test file.
- **POST** `/api/test-files`: Create a new test file.
- **PATCH** `/api/test-files/{test_file_id}`: Update a specific test file.
- **DELETE** `/api/test-files/{test_file_id}`: Delete a specific test file.
