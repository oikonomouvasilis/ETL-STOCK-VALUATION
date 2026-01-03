import pandas as pd
import numpy as np

file_name = 'S&P 500 Historical Data.csv'

df = pd.read_csv(file_name)

# Clean data
df['Price'] = df['Price'].str.replace(',', '').astype(float)
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df = df.sort_values('Date')
df.set_index('Date', inplace=True)


# 1. Υπολογισμός μηνιαίων αποδόσεων απευθείας από την τιμή
monthly_returns = df['Price'].pct_change().dropna()
    
# 2. Υπολογισμός συνολικού πολλαπλασιαστή
n = len(monthly_returns)
cumulative_factor = (1 + monthly_returns).prod()
        
# 3. Υπολογισμός μηνιαίας γεωμετρικής μέσης
monthly_geometric_return = cumulative_factor ** (1/n) - 1
        
# 4. Ετησιοποίηση (ΣΩΣΤΗ ΛΟΓΙΚΗ)
annualized_geometric_return = (1 + monthly_geometric_return)**12 - 1

print(annualized_geometric_return)