from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'mysql-db',
    'user': 'root',
    'password': 'password',
    'database': 'app_db'
}

@app.route('/list', methods=['GET'])
def list_products():
    """
    Retrieve the list of all products from the database.
    """
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Fetch all products
    query_select = "SELECT * FROM products"
    cursor.execute(query_select)
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({"products": products}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)