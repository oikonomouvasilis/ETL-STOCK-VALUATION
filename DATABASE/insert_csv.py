import sqlite3
import pandas as pd
import os

# Resolve paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "valuation.db")

CSV_PATH = os.path.join(BASE_DIR, "..", "market_capm_results.csv")
# ↑ one level up from DATABASE folder

# Load CSV
df = pd.read_csv(CSV_PATH)

# Rename columns
df = df.rename(columns={
    "Ticker": "ticker",
    "Full Name": "full_name",
    "Beta": "beta",
    "CAPM Value": "capm"
})

# Connect to DB
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Insert rows
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

conn.commit()
conn.close()

print("CSV successfully inserted into database.")
