# POST /api/v1/support-request

Submit a support/ticket request.

- **Endpoint:** `/api/v1/support-request`
- **Method:** POST
- **Request Content-Type:** application/json

## Request Fields

| Field        | Type    | Required | Constraint                |
|--------------|---------|----------|---------------------------|
| user_email   | string  | Yes      | Valid email address       |
| subject      | string  | Yes      | 1-100 characters          |
| description  | string  | Yes      | 1-2048 characters         |
| priority     | int     | Optional | 1: High, 2: Medium, 3: Low|

## Request Example

```json
{
  "user_email": "alice@example.com",
  "subject": "App not loading",
  "description": "My app gets stuck at login.",
  "priority": 1
}