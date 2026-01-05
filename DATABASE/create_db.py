"""
Database Creation Script

This script creates a new SQLite database named 'valuation.db' in the current directory
if it doesn't already exist. It also creates a table called 'financials' with columns
for ticker, full_name, beta, and capm values.

Table Structure:
- ticker: TEXT (Primary Key) - Stock ticker symbol
- full_name: TEXT - Full company name
- beta: REAL - Beta coefficient
- capm: REAL - CAPM calculated value

Usage:
    Run this script directly: python create_db.py
    It will create the database and table, then print the database path.

Requirements:
    - sqlite3 and os modules (standard library).
    - Write permissions in the current directory.
"""

import sqlite3
import os

# Get the absolute path to the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the path for the database file
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

# Connect to the database (this creates it if it doesn't exist)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create the financials table if it doesn't already exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS financials (
    ticker TEXT PRIMARY KEY,
    full_name TEXT,
    beta REAL,
    capm REAL
)
""")

# Commit the changes and close the connection
conn.commit()
conn.close()

# Print success message with the database path
print(f"Database created successfully at:\n{DB_PATH}")
