import finnhub
import pandas as pd
import time

# 1. Ρύθμιση Client
API_KEY = "d4oua89r01qnosaap9s0d4oua89r01qnosaap9sg"
client = finnhub.Client(api_key=API_KEY)

# 2. Σταθερές (Risk-free rate & Market return)
RISK_FREE_RATE = 0.04139  #
MARKET_RETURN = 0.06346379099832156  #

def generate_full_market_capm():
    # 3. Λήψη όλων των συμβόλων
    print("Λήψη λίστας συμβόλων από τη Finnhub...")
    symbols_data = client.stock_symbols('US') #
    
    # Μετατροπή σε DataFrame για εύκολη ταξινόμηση
    df_symbols = pd.DataFrame(symbols_data)
    
    # 4. Ταξινόμηση A-Z βάσει του ticker (symbol)
    df_symbols = df_symbols.sort_values(by='symbol').reset_index(drop=True) #
    
    results = []
    total = len(df_symbols)
    
    print(f"Ξεκινάει η επεξεργασία για {total} εταιρείες. Παρακαλώ περιμένετε...")

    for index, row in df_symbols.iterrows():
        ticker = row['symbol']
        full_name = row['description'] #
        
        try:
            # 5. Λήψη Beta από τα οικονομικά στοιχεία
            data = client.company_basic_financials(ticker, 'all') #
            beta = data.get('metric', {}).get('beta')
            
            # 6. Φιλτράρισμα: Απόρριψη αν το beta είναι None ή 0
            if beta and beta != 0:
                # Υπολογισμός CAPM
                capm_value = RISK_FREE_RATE + beta * (MARKET_RETURN - RISK_FREE_RATE) #
                
                # Πρόσθετο φιλτράρισμα για CAPM != 0 (αν και με beta != 0 είναι σχεδόν αδύνατο να βγει 0)
                if capm_value != 0:
                    results.append({
                        'Ticker': ticker,
                        'Full Name': full_name,
                        'Beta': beta,
                        'CAPM Value': capm_value
                    })
                    print(f"[{index+1}/{total}] {ticker}: Προστέθηκε (CAPM: {capm_value:.4f})")
            
            # 7. Διαχείριση Rate Limit (1 κλήση ανά 1.1 δευτερόλεπτο για ασφάλεια)
            time.sleep(1.1) 
            
        except Exception as e:
            print(f"Σφάλμα στο {ticker}: {e}")
            time.sleep(2) # Περιμένουμε λίγο παραπάνω σε περίπτωση σφάλματος δικτύου
            continue

    # 8. Δημιουργία τελικού DataFrame
    df_final = pd.DataFrame(results)
    
    # 9. Αποθήκευση σε CSV
    filename = "market_capm_results.csv"
    df_final.to_csv(filename, index=False, encoding='utf-8-sig') #
    
    print(f"\nΗ διαδικασία ολοκληρώθηκε!")
    print(f"Συνολικές εταιρείες με έγκυρο CAPM: {len(df_final)}")
    print(f"Το αρχείο αποθηκεύτηκε ως: {filename}")
    
    return df_final

# Εκτέλεση της συνάρτησης
if __name__ == "__main__":
    final_df = generate_full_market_capm()