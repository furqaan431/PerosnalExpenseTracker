# Personal Expense Tracker

## Overview
The Personal Expense Tracker is a Python application designed to help users manage and categorize their financial transactions. It features an ETL (Extract, Transform, Load) process to gather data from multiple sources, a MySQL database for storing transaction details, and data visualizations using Matplotlib to track spending patterns.

## Features
- Add, categorize, and manage personal financial transactions.
- Extract data from various sources such as bank statements and receipts.
- Transform and load data into a structured MySQL database.
- Automated data aggregation and reporting.
- Data validation techniques to ensure accuracy and consistency.
- Visualizations to track spending patterns and provide actionable insights.

## Technologies Used
- **Python**: The main programming language for the application.
- **MySQL**: Database management system for storing transaction data.
- **Pandas**: Library for data manipulation and analysis.
- **Matplotlib**: Library for creating visualizations of financial data.

## Getting Started

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- MySQL Server
- Required Python libraries:

### Database Setup
1. Create a MySQL database named `ExpenseTracker`.
2. Create two tables: `categories` and `transactions`.

   ```sql
   CREATE TABLE categories (
       id INT AUTO_INCREMENT PRIMARY KEY,
       category_name VARCHAR(100) NOT NULL
   );

   CREATE TABLE transactions (
       id INT AUTO_INCREMENT PRIMARY KEY,
       amount DECIMAL(10, 2) NOT NULL,
       category_id INT,
       date DATE NOT NULL,
       description TEXT,
       FOREIGN KEY (category_id) REFERENCES categories(id)
   );

