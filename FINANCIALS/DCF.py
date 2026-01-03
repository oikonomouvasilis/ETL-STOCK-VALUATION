import finnhub
import pprint
client = finnhub.Client(api_key="d4oua89r01qnosaap9s0d4oua89r01qnosaap9sg")  
ticker = "AAPL"     

    # Step 2: fetch financials-reported (annual) and compute FCFs list
resp = client.financials_reported(symbol=ticker)  # wrapper for /stock/financials-reported
    # The structure: resp['data'] is list of reports (check with print)
    # print available years and types
reports = resp.get('data', [])
print("Number of financial report items:", len(reports))

FCF = []

    # Keywords Finnhub typically uses for CFO and CAPEX:
CFO_KEYS = {
        "NetCashProvidedByOperatingActivities",
        "NetCashFlowsFromUsedInOperatingActivities",
        "NetCashProvidedByUsedInOperatingActivities"
    }

CAPEX_KEYS = {
        "CapitalExpenditures",
        "CapitalExpenditure",
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PurchasesOfPropertyPlantAndEquipment"
    }

for item in reports:
        year = item.get("year")
        cf_list = item["report"].get("cf", [])

        ocf = None
        capex = None

        for entry in cf_list:
            concept = entry.get("concept")
            value = entry.get("value")

            if concept in CFO_KEYS:
                ocf = value

            if concept in CAPEX_KEYS:
                capex = value

        if ocf is not None and capex is not None:
            FCF.append({
                "year": year,
                "ocf": ocf,
                "capex": capex,
                "fcf": ocf - capex
            })

    # Print results
print("\nExtracted FCFs:")
pprint.pprint(FCF)