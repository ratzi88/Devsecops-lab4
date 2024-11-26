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
    product_quentity INT NOT NULL
);


INSERT INTO users (username, password) 
VALUES ('admin', 'admin')
ON DUPLICATE KEY UPDATE username='admin';
