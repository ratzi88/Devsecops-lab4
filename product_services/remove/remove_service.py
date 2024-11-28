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

@app.route('/remove/<string:product_name>', methods=['DELETE'])
def remove_product(product_name):

    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Check if the product exists
    query_check = "SELECT * FROM products WHERE product_name = %s"
    cursor.execute(query_check, (product_name,))
    product = cursor.fetchone()

    if not product:
        cursor.close()
        conn.close()
        return jsonify({"error": f"Product with name '{product_name}' not found"}), 404

    # Remove the product
    query_delete = "DELETE FROM products WHERE product_name = %s"
    cursor.execute(query_delete, (product_name,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": f"Product with name '{product_name}' removed successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)
