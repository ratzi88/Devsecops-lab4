-- Create the user (uncomment if needed)
CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Aauth123';

-- Create the database 'auth' if it does not exist
CREATE DATABASE IF NOT EXISTS auth;

-- Set the context to the 'auth' database
USE auth;

-- Grant privileges to 'auth_user' on the 'auth' database
GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

-- Create the 'user' table in the 'auth' database
CREATE TABLE `user` (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(55) NOT NULL UNIQUE,
    password VARCHAR(55) NOT NULL
);

-- Insert data into the 'user' table
INSERT INTO `user` (username, password) VALUES ('admin', 'admin');
