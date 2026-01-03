import finnhub
import pandas as pd

client = finnhub.Client(api_key="d4oua89r01qnosaap9s0d4oua89r01qnosaap9sg")

symbols = client.stock_symbols('US')

df = pd.DataFrame(symbols)

df_filtered = df[['symbol', 'description']]

df_final = df_filtered.sort_values(by='symbol',ascending=True)

print(df_final)
