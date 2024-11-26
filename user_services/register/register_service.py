from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db_config = {
    'host': 'mysql-db',
    'user': 'root',
    'password': 'password',
    'database': 'app_db'
}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Check if the user already exists
    query_check = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query_check, (username,))
    user = cursor.fetchone()

    if user:
        cursor.close()
        conn.close()
        return jsonify({"error": "User already exists"}), 400

    # Insert the new user
    query_insert = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query_insert, (username, password))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
