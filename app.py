from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional

app = Flask(__name__)

# --- Request model ---
class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

# --- Response model ---
class RegisterResponse(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    message: str

# --- Example: In-memory user list and auto-increment ---
users_db = []
next_id = 1

@app.route('/register', methods=['POST'])
def register():
    global next_id
    try:
        # Validate and parse input
        req_json = request.get_json()
        data = RegisterRequest(**req_json)
    except ValidationError as e:
        # Validation failed
        return jsonify({"error": e.errors()}), 400
    
    # Check for duplicate user (example, not production secure!)
    for u in users_db:
        if u['email'] == data.email or u['username'] == data.username:
            return jsonify({"error": "User with this username or email already exists."}), 409

    # "Register" the user
    user = {
        "user_id": next_id,
        "username": data.username,
        "email": data.email,
        "password": data.password  # Do NOT store plaintext in production!
    }
    users_db.append(user)
    response = RegisterResponse(
        user_id=next_id,
        username=data.username,
        email=data.email,
        message="User registered successfully"
    )
    next_id += 1
    return jsonify(response.dict()), 201

if __name__ == "__main__":
    app.run(debug=True)