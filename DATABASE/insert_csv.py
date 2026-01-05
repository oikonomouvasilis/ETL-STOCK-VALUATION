"""
CSV Data Insertion Script

This script reads data from a CSV file named 'market_capm_results.csv' located in the
parent directory, processes it, and inserts the data into the 'financials' table
in the 'valuation.db' SQLite database.

CSV File Expected Format:
- Columns: Ticker, Full Name, Beta, CAPM Value
- The script renames them to: ticker, full_name, beta, capm

Process:
1. Loads the CSV file.
2. Renames columns to match database schema.
3. Inserts each row into the database, replacing existing entries if any.

Usage:
    Run this script directly: python insert_csv.py
    Ensure 'market_capm_results.csv' exists in the parent directory.

Requirements:
    - pandas library (pip install pandas)
    - sqlite3 and os modules (standard library)
    - 'valuation.db' database with 'financials' table (run create_db.py first)
    - CSV file in the correct format
"""

import sqlite3
import pandas as pd
import os

# Resolve paths relative to this script's location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

# Path to the CSV file (one level up from DATABASE folder)
CSV_PATH = os.path.join(BASE_DIR, "..", "market_capm_results.csv")

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(CSV_PATH)

# Rename columns to match the database schema
df = df.rename(columns={
    "Ticker": "ticker",
    "Full Name": "full_name",
    "Beta": "beta",
    "CAPM Value": "capm"
})

# Connect to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Insert each row from the DataFrame into the database
for _, row in df.iterrows():
    cursor.execute("""
        INSERT OR REPLACE INTO financials (ticker, full_name, beta, capm)
        VALUES (?, ?, ?, ?)
    """, (
        row["ticker"],
        row["full_name"],
        row["beta"],
        row["capm"]
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()

# Print success message
print("CSV successfully inserted into database.")
