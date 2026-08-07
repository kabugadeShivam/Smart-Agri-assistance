from utils.market_matcher import match_market

results = match_market(

    crop="Onion",
    state="Maharashtra"

)

print("Markets Found:", len(results))

for market in results:

    print("-"*50)

    print("Market :", market["Market"])

    print("Price :", market["Modal_Price"])

    print("Trend :", market["Price_Trend"])

    print("Demand :", market["Demand"])