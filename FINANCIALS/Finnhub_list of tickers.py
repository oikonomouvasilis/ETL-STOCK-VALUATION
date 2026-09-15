"""
Finnhub Stock Symbols Fetcher

This script fetches all US stock symbols and their descriptions from the Finnhub API,
filters to show only symbol and description, sorts alphabetically by symbol, and prints
the result.

Output:
- A pandas DataFrame with columns: symbol, description
- Sorted alphabetically by symbol

Usage:
    Run this script directly: python Finnhub_list of tickers.py
    It will print the sorted list of US stock symbols.

Requirements:
    - finnhub-python library (pip install finnhub-python)
    - pandas library (pip install pandas)
    - Valid Finnhub API key
"""

import finnhub
import pandas as pd

import os as _os
from pathlib import Path as _Path


def _finnhub_key() -> str:
    """
    Διαβάζει το Finnhub API key από το περιβάλλον ή από ένα .env δίπλα στο project.

    Το κλειδί ήταν κάποτε γραμμένο μέσα στον κώδικα, σε δημόσιο repo. Δεν
    ξαναμπαίνει: το .env είναι στο .gitignore και το .env.example δείχνει τι
    χρειάζεται χωρίς να αποκαλύπτει τίποτα.
    """
    if not _os.getenv("FINNHUB_API_KEY"):
        for parent in [_Path(__file__).resolve().parent, *_Path(__file__).resolve().parents[:2]]:
            env = parent / ".env"
            if env.exists():
                for line in env.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        _os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
                break
    key = _os.getenv("FINNHUB_API_KEY")
    if not key:
        raise SystemExit(
            "Λείπει το FINNHUB_API_KEY. "
            "Αντίγραψε το .env.example σε .env και βάλε το κλειδί σου από finnhub.io."
        )
    return key



# Setup Finnhub client
client = finnhub.Client(api_key=_finnhub_key())

# Fetch all US stock symbols
symbols = client.stock_symbols('US')

# Convert to DataFrame
df = pd.DataFrame(symbols)

# Filter to keep only symbol and description columns
df_filtered = df[['symbol', 'description']]

# Sort alphabetically by symbol
df_final = df_filtered.sort_values(by='symbol', ascending=True)

# Print the result
print(df_final)
