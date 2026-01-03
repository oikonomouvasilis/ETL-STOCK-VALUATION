import sqlite3
import os

# Absolute path to DATABASE folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database path
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

# Connect (creates DB if it doesn't exist)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS financials (
    ticker TEXT PRIMARY KEY,
    full_name TEXT,
    beta REAL,
    capm REAL
)
""")

conn.commit()
conn.close()

print(f"Database created successfully at:\n{DB_PATH}")
