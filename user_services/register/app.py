import uuid
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import re
import requests # type: ignore

app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex
app.config['JWT_SECRET_KEY'] = uuid.uuid4().hex

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# In-memory user storage (replace with database in production)
users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not all(key in data for key in ('username', 'email', 'password')):
        return jsonify({"error": "Missing required fields"}), 400

    # Username validation
    if len(data['username']) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400

    # Email validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({"error": "Invalid email format"}), 400

    # Password strength validation
    if len(data['password']) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    # Check if username or email already exists
    if any(u['username'] == data['username'] for u in users):
        return jsonify({"error": "Username already exists"}), 409
    
    if any(u['email'] == data['email'] for u in users):
        return jsonify({"error": "Email already exists"}), 409

    # Hash password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create user
    user = {
        'username': data['username'],
        'email': data['email'],
        'password': hashed_password
    }
    users.append(user)

    # Attempt to automatically log in by calling login service
    try:
        login_response = requests.post('http://localhost:5001/login', json={
            'username': data['username'],
            'password': data['password']
        })
        
        if login_response.status_code == 200:
            return jsonify({
                "message": "User registered and logged in successfully",
                "token": login_response.json().get('access_token')
            }), 201
        else:
            return jsonify({
                "message": "User registered, but login failed",
                "error": login_response.json()
            }), 201
    except requests.RequestException as e:
        return jsonify({
            "message": "User registered, but could not automatically log in",
            "error": str(e)
        }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)