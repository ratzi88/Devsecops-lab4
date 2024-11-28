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
@app.route('/add', methods=['POST'])
def add_product():
    
    # Get Product From users
    data = request.json
    product_name = data.get('product_name')
    product_quantity = data.get('product_quantity')
    
    if not product_name or not product_quantity:
        return jsonify({"error": "Product name and quantity are required"}), 400
    
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Check if the user already exists
    query_check = "SELECT * FROM products WHERE product_name = %s"
    cursor.execute(query_check, (product_name,))
    product = cursor.fetchone()

    if product:
        cursor.close()
        conn.close()
        return jsonify({"error": "Product already exists"}), 400
    
    # Insert the new product
    query_insert = "INSERT INTO products (product_name, product_quantity) VALUES (%s, %s)"
    cursor.execute(query_insert, (product_name, product_quantity))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Poduct registered successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)