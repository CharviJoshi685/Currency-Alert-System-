import requests
import json

# Free API — no key required
url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)
data = response.json()

# Pretty print JSON
print(json.dumps(data, indent=4))

# Extract only needed currencies
rates = {curr: data["rates"][curr] for curr in ["INR", "EUR", "JPY", "GBP"]}
print("\nFiltered Rates:", rates)
