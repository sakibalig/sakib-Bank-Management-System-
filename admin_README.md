# Admin API

## Endpoints

```mermaid
graph TD;
    admin[Admin API] --> |GET| get_test_plan_analysis[Get Test Plan Analysis]
    admin --> |GET| get_test_plan[Get Test Plan]
    admin --> |GET| list_test_files_for_plan[List Test Files for Plan]
    admin --> |GET| get_test_file_for_plan[Get Test File for Plan]
    admin --> |GET| get_test_file[Get Test File]
```

- **GET** `/api/admin/test-plans/{test_plan_id}/analysis`: Retrieve analysis for a test plan.
- **GET** `/api/admin/test-plans/{test_plan_id}`: Retrieve a specific test plan.
- **GET** `/api/admin/test-plans/{test_plan_id}/test-files`: Retrieve test files for a test plan.
- **GET** `/api/admin/test-plans/{test_plan_id}/test-files/{test_file_id}`: Retrieve a specific test file for a test plan.
- **GET** `/api/admin/test-files/{test_file_id}`: Retrieve a specific test file.
