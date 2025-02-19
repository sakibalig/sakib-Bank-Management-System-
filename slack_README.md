# Slack API

## Endpoints

```mermaid
graph TD;
    slack[Slack API] --> |GET| authorize_slack[Authorize Slack]
    slack --> |GET| handle_oauth_callback[Handle OAuth Callback]
    slack --> |GET| list_channels[List Channels]
    slack --> |GET| list_workspaces[List Workspaces]
    slack --> |POST| send_message_to_channel[Send Message to Channel]
    slack --> |DELETE| delete_workspace[Delete Workspace]
```

- **GET** `/api/slack/authorize`: Authorize Slack.
- **GET** `/api/slack/oauth/callback`: Handle Slack OAuth callback.
- **GET** `/api/slack/channels`: Retrieve Slack channels.
- **GET** `/api/slack/workspaces`: Retrieve Slack workspaces.
- **POST** `/api/slack/channels/{channel_id}/messages`: Send messages to a Slack channel.
- **DELETE** `/api/slack/workspaces`: Delete a Slack workspace.
