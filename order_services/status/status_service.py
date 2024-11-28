from flask import Flask, request, jsonify
import mysql.connector
import os 

app = Flask(__name__)

db_config = {
    'host': os.getenv('MYSQL_HOST', 'mysql-db'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'password'),
    'database': os.getenv('MYSQL_DATABASE', 'app_db')
}
@app.route('/status', methods=['GET'])
def list_status():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    query_select = "SELECT * FROM orders"
    cursor.execute(query_select)
    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({"orders": orders}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)