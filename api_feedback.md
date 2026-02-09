# POST /feedback

Accept user feedback for the application.

**Endpoint:** `/feedback`  
**Method:** POST  
**Content-Type:** application/json

## Request Body

| Field        | Type   | Required | Notes                  |
|--------------|--------|----------|------------------------|
| user_email   | string | Yes      | User's email           |
| message      | string | Yes      | Feedback message (1-1000 chars) |
| rating       | int    | Yes      | Integer 1 (bad) to 5 (great) |

```json
{
  "user_email": "user@example.com",
  "message": "Amazing app!",
  "rating": 5
}