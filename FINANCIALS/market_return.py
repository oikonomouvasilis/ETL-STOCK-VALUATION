"""
Market Return Calculation Script

This script calculates the annualized geometric return of the S&P 500 index from
historical price data in a CSV file. It uses monthly returns to compute the
geometric mean and annualizes it.

Input File: 'S&P 500 Historical Data.csv'
Expected Columns: Date (MM/DD/YYYY), Price (with commas)

Process:
1. Load and clean the CSV data.
2. Convert dates and sort chronologically.
3. Calculate monthly percentage returns.
4. Compute cumulative factor from returns.
5. Calculate monthly geometric mean return.
6. Annualize to get yearly return.

Formula:
- Monthly Return = (Price_t - Price_{t-1}) / Price_{t-1}
- Cumulative Factor = Product(1 + Monthly Return) for all months
- Monthly Geometric Return = (Cumulative Factor)^(1/n) - 1
- Annualized Return = (1 + Monthly Geometric Return)^12 - 1

Usage:
    Run this script directly: python market_return.py
    It will print the annualized market return.

Requirements:
    - pandas library (pip install pandas)
    - numpy library (pip install numpy)
    - CSV file 'S&P 500 Historical Data.csv' in the same directory
"""

import pandas as pd
import numpy as np

# Name of the input CSV file
file_name = 'S&P 500 Historical Data.csv'

# Load the CSV data
df = pd.read_csv(file_name)

# Clean the Price column (remove commas and convert to float)
df['Price'] = df['Price'].str.replace(',', '').astype(float)

# Convert Date column to datetime and sort
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df = df.sort_values('Date')
df.set_index('Date', inplace=True)

# 1. Calculate monthly percentage returns
monthly_returns = df['Price'].pct_change().dropna()

# 2. Calculate cumulative multiplication factor
n = len(monthly_returns)
cumulative_factor = (1 + monthly_returns).prod()

# 3. Calculate monthly geometric mean return
monthly_geometric_return = cumulative_factor ** (1/n) - 1

# 4. Annualize the return (correct logic)
annualized_geometric_return = (1 + monthly_geometric_return)**12 - 1

# Print the result
print(annualized_geometric_return)