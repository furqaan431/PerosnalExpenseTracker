import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="Furqaan@431",  # Replace with your MySQL password
    database="ExpenseTracker"
)

# Load the transactions from the database
query = """
    SELECT c.category_name, SUM(t.amount) as total_spent
    FROM transactions t
    JOIN categories c ON t.category_id = c.id
    GROUP BY c.category_name
"""
df = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Plot a pie chart for the total expenses by category
plt.figure(figsize=(8, 8))
plt.pie(df['total_spent'], labels=df['category_name'], autopct='%1.1f%%', startangle=90)
plt.title('Expense Distribution by Category')
plt.show()

