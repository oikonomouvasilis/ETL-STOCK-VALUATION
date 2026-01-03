import sqlite3
import os

# Resolve DB path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

# Connect to DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Fetch data
cursor.execute("SELECT * FROM financials;")
rows = cursor.fetchall()

# Print results
print(f"Total rows: {len(rows)}\n")
for row in rows:
    print(row)

conn.close()
