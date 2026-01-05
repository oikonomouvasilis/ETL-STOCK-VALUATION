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

# Setup Finnhub client
client = finnhub.Client(api_key="d4oua89r01qnosaap9s0d4oua89r01qnosaap9sg")

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
