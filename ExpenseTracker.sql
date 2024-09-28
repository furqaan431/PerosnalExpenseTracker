CREATE DATABASE ExpenseTracker;

USE ExpenseTracker;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10, 2),
    category_id INT,
    date DATE,
    description VARCHAR(255),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
