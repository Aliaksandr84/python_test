# auth_utils.py (helper module)
import jwt
from functools import wraps
from flask import request, jsonify

SECRET_KEY = 'your-secret-key'  # In production, use os.environ or config

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', None)
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Authorization header missing or invalid'}), 401
        token = auth_header.split(" ")[1]
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token'}), 401
        # Optionally, put user info in Flask's `g` for later use
        request.user = data
        return f(*args, **kwargs)
    return decorated