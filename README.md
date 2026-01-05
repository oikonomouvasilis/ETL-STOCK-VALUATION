# ETL Stock Valuation Project

This project provides tools for stock valuation using financial data from Finnhub API. It includes ETL (Extract, Transform, Load) processes to fetch stock data, calculate CAPM (Capital Asset Pricing Model) values, and store results in a SQLite database.

## Project Structure

- **DATABASE/**: Scripts for database management
  - `create_db.py`: Creates the SQLite database and financials table
  - `insert_csv.py`: Inserts CAPM data from CSV into the database
  - `check_db.py`: Lists all tables in the database
  - `check_table.py`: Displays all data in the financials table

- **FINANCIALS/**: Scripts for financial calculations
  - `CAPM.py`: Fetches stock symbols and calculates CAPM values
  - `DCF.py`: Example script for calculating Free Cash Flow (FCF)
  - `Finnhub_list of tickers.py`: Fetches and displays US stock symbols
  - `market_return.py`: Calculates annualized market return from S&P 500 data

## Prerequisites

- Python 3.x
- Required libraries: `finnhub-python`, `pandas`, `numpy`
- Finnhub API key (sign up at https://finnhub.io/)

## Installation

1. Install required packages:
   ```bash
   pip install finnhub-python pandas numpy
   ```

2. Replace the API key in the scripts with your own Finnhub API key.

## Usage

### Step 1: Calculate Market Return
Run `market_return.py` to get the annualized market return (used in CAPM):
```bash
python FINANCIALS/market_return.py
```
Update the `MARKET_RETURN` constant in `CAPM.py` with the output.

### Step 2: Fetch CAPM Data
Run `CAPM.py` to fetch stock data and calculate CAPM values:
```bash
python FINANCIALS/CAPM.py
```
This creates `market_capm_results.csv` with the results.

### Step 3: Setup Database
Create the database:
```bash
python DATABASE/create_db.py
```

### Step 4: Load Data into Database
Insert the CSV data into the database:
```bash
python DATABASE/insert_csv.py
```

### Step 5: Verify Data
Check the database contents:
```bash
python DATABASE/check_db.py
python DATABASE/check_table.py
```

## Additional Scripts

- `Finnhub_list of tickers.py`: Get a list of all US stock symbols
- `DCF.py`: Example of calculating Free Cash Flow for AAPL (modify ticker as needed)

## Notes

- API calls are rate-limited; scripts include delays to comply with Finnhub limits.
- The CAPM calculation uses a fixed risk-free rate; update as needed.
- Database uses SQLite for simplicity; can be adapted for other databases.

## License

This project is for educational purposes. Ensure compliance with Finnhub's terms of service.

