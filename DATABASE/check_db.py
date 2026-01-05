"""
Database Check Script

This script connects to the SQLite database 'valuation.db' located in the same directory
and lists all tables present in the database. It is useful for verifying the database
structure after creation or modification.

Usage:
    Run this script directly: python check_db.py
    It will print the list of tables in the database.

Requirements:
    - SQLite database file 'valuation.db' must exist in the same directory.
    - sqlite3 and os modules (standard library).
"""

import sqlite3
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the path to the database file
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

# Connect to the SQLite database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Execute a query to get all table names from the database schema
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print the results
print("Tables:", cursor.fetchall())

# Close the database connection
conn.close()
