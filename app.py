from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, ValidationError, constr
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime

app = Flask(__name__)
SECRET_KEY = 'my_secret'

users_db = {}
next_id = 1

def make_error(code, message, details=None, status=400):
    error = {"code": code, "message": message}
    if details:
        error["details"] = details
    return jsonify({"error": error}), status

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

# In-memory feedback store (for example/demo)
feedback_db = []

class FeedbackRequest(BaseModel):
    user_email: constr(strip_whitespace=True, min_length=5, max_length=100)
    message: constr(strip_whitespace=True, min_length=1, max_length=1000)
    rating: int  # 1-5

    @classmethod
    def validate_rating(cls, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        return value

def make_error(code, message, details=None, status=400):
    error = {"code": code, "message": message}
    if details:
        error["details"] = details
    return jsonify({"error": error}), status

@app.route('/feedback', methods=['POST'])
def post_feedback():
    """
    Accepts a feedback submission.
    Request JSON must contain user_email, message, and rating (1-5).
    """
    try:
        json_data = request.get_json()
        data = FeedbackRequest(**json_data)
        if not (1 <= data.rating <= 5):
            return make_error("VALIDATION_FAILED", "Rating must be between 1 and 5.", status=400)
    except (ValidationError, TypeError) as e:
        details = (e.errors() if hasattr(e, "errors")
                   else [{"msg": str(e)}])
        return make_error("VALIDATION_FAILED", "Invalid input.", details, 400)

    feedback = {
        "id": len(feedback_db) + 1,
        "user_email": data.user_email,
        "message": data.message,
        "rating": data.rating,
        "submitted_at": datetime.datetime.utcnow().isoformat() + "Z"
    }
    feedback_db.append(feedback)
    return jsonify({
        "message": "Feedback received. Thank you!",
        "feedback_id": feedback["id"],
        "submitted_at": feedback["submitted_at"]
    }), 201


@app.route('/register', methods=['POST'])
def register():
    global next_id
    try:
        data = RegisterRequest(**request.get_json())
    except ValidationError as e:
        # Collect pydantic-style errors
        details = [{"field": ".".join(loc), "msg": err['msg']} for err in e.errors() for loc in [err['loc']]]
        return make_error("VALIDATION_FAILED", "Invalid input.", details, 400)
    # Check for duplicate
    if data.email in users_db:
        return make_error("CONFLICT", "User with this email already exists.", status=409)
    user = {
        "user_id": next_id,
        "username": data.username,
        "email": data.email,
        "password": generate_password_hash(data.password)
    }
    users_db[data.email] = user
    next_id += 1
    return jsonify({
        "user_id": user["user_id"],
        "username": user["username"],
        "email": user["email"],
        "message": "User registered successfully"
    }), 201

@app.route('/login', methods=['POST'])
def login():
    from pydantic import ValidationError
    class LoginRequest(BaseModel):
        email: EmailStr
        password: str
    try:
        data = LoginRequest(**request.get_json())
    except ValidationError as e:
        details = [{"field": ".".join(loc), "msg": err['msg']} for err in e.errors() for loc in [err['loc']]]
        return make_error("VALIDATION_FAILED", "Invalid input.", details, 400)
    user = users_db.get(data.email)
    if not user or not check_password_hash(user['password'], data.password):
        return make_error("AUTH_REQUIRED", "Invalid credentials.", status=401)
    token = jwt.encode(
        {
            "user_id": user["user_id"],
            "username": user["username"],
            "email": user["email"],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    return jsonify({"token": token}), 200

@app.route('/protected-data', methods=['GET'])
def protected_data():
    auth_header = request.headers.get('Authorization', None)
    if not auth_header or not auth_header.startswith('Bearer '):
        return make_error("AUTH_REQUIRED", "Authorization header missing or invalid.", status=401)
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return make_error("INVALID_TOKEN", "Token is invalid or expired.", status=401)
    except jwt.InvalidTokenError:
        return make_error("INVALID_TOKEN", "Token is invalid or expired.", status=401)
    return jsonify({
        "message": f"Hello, {payload.get('username', 'user')}! This is your protected data.",
        "user_id": payload.get('user_id'),
        "protected_stuff": [1, 2, 3]
    }), 200

@app.errorhandler(500)
def server_error(e):
    return make_error("SERVER_ERROR", "An internal server error occurred.", status=500)

if __name__ == "__main__":
    app.run(debug=True)