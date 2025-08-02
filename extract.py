import requests

# Fetch data
url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()

# Extract only desired currencies
currencies = ["INR", "EUR", "JPY", "GBP"]
rates = {curr: data["rates"][curr] for curr in currencies}

print("Filtered Rates:")
for curr, rate in rates.items():
    print(f"1 USD = {rate} {curr}")
