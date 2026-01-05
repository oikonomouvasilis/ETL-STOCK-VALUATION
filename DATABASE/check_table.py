"""
Table Content Check Script

This script connects to the SQLite database 'valuation.db' and retrieves all rows
from the 'financials' table. It prints the total number of rows and each row's data.
Useful for inspecting the contents of the financials table.

Usage:
    Run this script directly: python check_table.py
    It will display all data in the financials table.

Requirements:
    - SQLite database file 'valuation.db' with a 'financials' table.
    - sqlite3 and os modules (standard library).
"""

import sqlite3
import os

# Resolve the path to the database directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the path to the database file
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Execute a query to select all data from the financials table
cursor.execute("SELECT * FROM financials;")
rows = cursor.fetchall()

# Print the total number of rows
print(f"Total rows: {len(rows)}\n")

# Print each row
for row in rows:
    print(row)

# Close the database connection
conn.close()
