import pandas as pd
import json
from app import app
from data_quality.checker import check_not_null

def test_check_not_null_no_missing():
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [30, 25, 35]
    })
    result = check_not_null(df, ['id', 'name', 'age'])
    assert result == {'id': 0, 'name': 0, 'age': 0}

def test_check_not_null_with_missing():
    df = pd.DataFrame({
        'id': [1, None, 3],
        'name': ['Alice', None, 'Charlie'],
        'age': [30, 25, None]
    })
    result = check_not_null(df, ['id', 'name', 'age'])
    assert result == {'id': 1, 'name': 1, 'age': 1}

---

## 3. **Unit Test Feedback**

def test_feedback_success():
    client = app.test_client()
    payload = {
        "user_email": "testuser@example.com",
        "message": "Great app!",
        "rating": 5
    }
    response = client.post("/feedback", data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert "feedback_id" in data
    assert data["message"] == "Feedback received. Thank you!"

def test_feedback_invalid():
    client = app.test_client()
    payload = {
        "user_email": "a@b.c",  # too short for our min_length
        "message": "",
        "rating": 7              # invalid rating
    }
    response = client.post("/feedback", data=json.dumps(payload), content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert data["error"]["code"] == "VALIDATION_FAILED"