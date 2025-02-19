# Test Plans API

## Endpoints

```mermaid
graph TD;
    testplans[Test Plans API] --> |GET| list_test_plans[List Test Plans]
    testplans --> |GET| get_test_plan[Get Test Plan]
    testplans --> |POST| create_test_plan[Create Test Plan]
    testplans --> |PATCH| update_test_plan[Update Test Plan]
    testplans --> |DELETE| delete_test_plan[Delete Test Plan]
    testplans --> |GET| get_test_plan_status[Get Test Plan Status]
    testplans --> |GET| get_status_by_run_code[Get Status by Run Code]
    testplans --> |PATCH| update_status_by_run_code[Update Status by Run Code]
    testplans --> |POST| create_status[Create Status]
```

- **GET** `/api/testplans/org`: Retrieve test plans for an organization.
- **GET** `/api/testplans/{test_plan_id}`: Retrieve a specific test plan.
- **POST** `/api/testplans`: Create a new test plan.
- **PATCH** `/api/testplans/{test_plan_id}`: Update a specific test plan.
- **DELETE** `/api/testplans/{test_plan_id}`: Delete a specific test plan.
- **GET** `/api/testplans/test-plan/{test_plan_id}/status`: Retrieve status of a test plan.
- **GET** `/api/testplans/status/{run_code}`: Retrieve status by run code.
- **PATCH** `/api/testplans/status/{run_code}`: Update status by run code.
- **POST** `/api/testplans/status`: Create a new status.
