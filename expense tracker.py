import pandas as pd
import mysql.connector
from datetime import datetime

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="",  # Replace with your MySQL username
    password="",  # Replace with your MySQL password
    database="ExpenseTracker"
)

cursor = conn.cursor()

# Load CSV file into a Pandas DataFrame
df = pd.read_csv('transactions.csv')

# Map category names to category IDs
category_map = {}
cursor.execute("SELECT id, category_name FROM categories")
for category_id, category_name in cursor.fetchall():
    category_map[category_name] = category_id

# Validate and insert each transaction into the database
for index, row in df.iterrows():
    amount = row['amount']
    category = row['category']
    date = row['date']
    description = row['description']
    
    # Data validation checks
    if amount <= 0:
        print(f"Skipping row {index}: Invalid amount")
        continue
    
    if category not in category_map:
        print(f"Skipping row {index}: Invalid category '{category}'")
        continue
    
    try:
        # Check if date is in valid format
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print(f"Skipping row {index}: Invalid date format '{date}'")
        continue

    # Insert validated transaction
    cursor.execute("""
        INSERT INTO transactions (amount, category_id, date, description)
        VALUES (%s, %s, %s, %s)
    """, (amount, category_map[category], date, description))

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Transactions validated and inserted successfully!")


