CREATE DATABASE IF NOT EXISTS app_db;

USE app_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL UNIQUE,
    product_quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL UNIQUE,
    product_quantity INT NOT NULL,
    shipping_status VARCHAR(255) NOT NULL,
    estamited_dlivery DATE NOT NULL
);



INSERT INTO users (username, password) 
VALUES ('admin', 'admin')
ON DUPLICATE KEY UPDATE username='admin';

INSERT INTO products (product_name, product_quantity) 
VALUES 
  ('Dell Insprion 7577', '121'),
  ('Hp Gaming Screen', '100'),
  ('Logitech Mouse', '66'),
  ('Logitech Keyboard', '67');


INSERT INTO orders (product_name, product_quantity,shipping_status,estamited_dlivery) 
VALUES 
  ('Dell Insprion 7577', '1','Pending','2025-01-01'),
  ('Hp Gaming Screen', '1','Sent to customer','2024-12-12');
