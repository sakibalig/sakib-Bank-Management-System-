# Report API

## Endpoints

```mermaid
graph TD;
    report[Report API] --> |POST| create_report[Create Report]
    report --> |POST| add_logs_to_report[Add Logs to Report]
    report --> |GET| get_report[Get Report]
    report --> |PATCH| update_report[Update Report]
    report --> |POST| generate_report[Generate Report]
    report --> |POST| send_report_to_discord[Send Report to Discord]
    report --> |GET| check_approval[Check Approval]
```

- **POST** `/api/report`: Create a new report.
- **POST** `/api/report/{report_id}/logs`: Add logs to a report.
- **GET** `/api/report/{report_id}`: Retrieve a specific report.
- **PATCH** `/api/report/{report_id}`: Update a specific report.
- **POST** `/api/report/generate-report/{report_id}`: Generate a report.
- **POST** `/api/report/send-discord/{report_id}`: Send a report to Discord.
- **GET** `/api/report/check-approval/{channel_id}/{message_id}`: Check approval status.
