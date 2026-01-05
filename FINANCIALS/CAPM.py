"""
CAPM Calculation Script

This script fetches stock symbols from Finnhub API, retrieves beta values for each stock,
calculates the Capital Asset Pricing Model (CAPM) values, and saves the results to a CSV file.

CAPM Formula: CAPM = Risk-Free Rate + Beta * (Market Return - Risk-Free Rate)

Process:
1. Fetches all US stock symbols from Finnhub.
2. Sorts symbols alphabetically.
3. For each symbol, fetches beta from company financials.
4. Filters out invalid beta values (None or 0).
5. Calculates CAPM for valid betas.
6. Saves results to 'market_capm_results.csv'.

Constants:
- RISK_FREE_RATE: Current risk-free rate (e.g., 10-year Treasury yield)
- MARKET_RETURN: Annualized market return (calculated separately)

Usage:
    Run this script directly: python CAPM.py
    Note: Requires a valid Finnhub API key. Rate limited to ~1 call per second.

Requirements:
    - finnhub-python library (pip install finnhub-python)
    - pandas library (pip install pandas)
    - Valid Finnhub API key
    - Internet connection for API calls
"""

import finnhub
import pandas as pd
import time

# 1. Setup Finnhub Client
# Replace with your own API key from https://finnhub.io/
API_KEY = "d4oua89r01qnosaap9s0d4oua89r01qnosaap9sg"
client = finnhub.Client(api_key=API_KEY)

# 2. Constants for CAPM calculation
# Risk-free rate (e.g., 10-year US Treasury yield)
RISK_FREE_RATE = 0.04139
# Market return (annualized geometric return of S&P 500)
MARKET_RETURN = 0.06346379099832156

def generate_full_market_capm():
    """
    Main function to generate CAPM values for all US stocks.

    Fetches symbols, calculates CAPM, and saves to CSV.

    Returns:
        pd.DataFrame: DataFrame with Ticker, Full Name, Beta, CAPM Value
    """
    # 3. Fetch all US stock symbols
    print("Fetching list of symbols from Finnhub...")
    symbols_data = client.stock_symbols('US')

    # Convert to DataFrame for easy sorting
    df_symbols = pd.DataFrame(symbols_data)

    # 4. Sort alphabetically by ticker symbol
    df_symbols = df_symbols.sort_values(by='symbol').reset_index(drop=True)

    results = []
    total = len(df_symbols)

    print(f"Starting processing for {total} companies. Please wait...")

    for index, row in df_symbols.iterrows():
        ticker = row['symbol']
        full_name = row['description']

        try:
            # 5. Fetch beta from company basic financials
            data = client.company_basic_financials(ticker, 'all')
            beta = data.get('metric', {}).get('beta')

            # 6. Filter: Reject if beta is None or 0
            if beta and beta != 0:
                # Calculate CAPM value
                capm_value = RISK_FREE_RATE + beta * (MARKET_RETURN - RISK_FREE_RATE)

                # Additional filter for CAPM != 0 (rare with beta != 0)
                if capm_value != 0:
                    results.append({
                        'Ticker': ticker,
                        'Full Name': full_name,
                        'Beta': beta,
                        'CAPM Value': capm_value
                    })
                    print(f"[{index+1}/{total}] {ticker}: Added (CAPM: {capm_value:.4f})")

            # 7. Rate limit handling (1 call per 1.1 seconds for safety)
            time.sleep(1.1)

        except Exception as e:
            print(f"Error for {ticker}: {e}")
            time.sleep(2)  # Wait longer on network errors
            continue

    # 8. Create final DataFrame
    df_final = pd.DataFrame(results)

    # 9. Save to CSV
    filename = "market_capm_results.csv"
    df_final.to_csv(filename, index=False, encoding='utf-8-sig')

    print(f"\nProcess completed!")
    print(f"Total companies with valid CAPM: {len(df_final)}")
    print(f"File saved as: {filename}")

    return df_final

# Execute the function if run directly
if __name__ == "__main__":
    final_df = generate_full_market_capm()