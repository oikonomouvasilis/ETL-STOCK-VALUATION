"""
DCF Free Cash Flow Calculation Script

This script demonstrates how to calculate Free Cash Flow (FCF) for a given stock ticker
using financial data from Finnhub API. FCF is calculated as Operating Cash Flow minus
Capital Expenditures.

Formula: FCF = Operating Cash Flow - Capital Expenditures

Process:
1. Fetches reported financials for the ticker.
2. Extracts Operating Cash Flow (OCF) and Capital Expenditures (CAPEX) from cash flow statements.
3. Calculates FCF for each available year.
4. Prints the extracted FCF data.

Note: This is a basic example for one ticker (AAPL). Modify the ticker variable for other stocks.

Usage:
    Run this script directly: python DCF.py
    It will print the FCF data for the specified ticker.

Requirements:
    - finnhub-python library (pip install finnhub-python)
    - pprint module (standard library)
    - Valid Finnhub API key
"""

import finnhub
import pprint

# Setup Finnhub client with API key
client = finnhub.Client(api_key="d4oua89r01qnosaap9s0d4oua89r01qnosaap9sg")

# Specify the stock ticker to analyze
ticker = "AAPL"

# Step 1: Fetch financials-reported (annual) and compute FCFs list
resp = client.financials_reported(symbol=ticker)  # API call for reported financials

# The response structure: resp['data'] is a list of reports
reports = resp.get('data', [])
print("Number of financial report items:", len(reports))

FCF = []

# Keywords Finnhub typically uses for Operating Cash Flow (CFO)
CFO_KEYS = {
    "NetCashProvidedByOperatingActivities",
    "NetCashFlowsFromUsedInOperatingActivities",
    "NetCashProvidedByUsedInOperatingActivities"
}

# Keywords for Capital Expenditures (CAPEX)
CAPEX_KEYS = {
    "CapitalExpenditures",
    "CapitalExpenditure",
    "PaymentsToAcquirePropertyPlantAndEquipment",
    "PurchasesOfPropertyPlantAndEquipment"
}

# Process each financial report
for item in reports:
    year = item.get("year")
    cf_list = item["report"].get("cf", [])  # Cash flow section

    ocf = None
    capex = None

    # Search for OCF and CAPEX in the cash flow entries
    for entry in cf_list:
        concept = entry.get("concept")
        value = entry.get("value")

        if concept in CFO_KEYS:
            ocf = value

        if concept in CAPEX_KEYS:
            capex = value

    # Calculate FCF if both values are available
    if ocf is not None and capex is not None:
        FCF.append({
            "year": year,
            "ocf": ocf,
            "capex": capex,
            "fcf": ocf - capex
        })

# Print the results
print("\nExtracted FCFs:")
pprint.pprint(FCF)