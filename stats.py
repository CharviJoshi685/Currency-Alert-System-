import requests
import statistics

# --- Fetch data ---
url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()

# --- Select currencies ---
currencies = ["INR", "EUR", "JPY", "GBP"]
rates = {curr: data["rates"][curr] for curr in currencies}

# --- Demo yesterday's rates (in real project, load from saved CSV) ---
yesterday_rates = {
    "INR": rates["INR"] * 0.998,  # Slightly different for demo
    "EUR": rates["EUR"] * 1.002,
    "JPY": rates["JPY"] * 0.997,
    "GBP": rates["GBP"] * 1.001
}

# --- Calculate % change ---
percent_changes = {}
for curr in currencies:
    change = ((rates[curr] - yesterday_rates[curr]) / yesterday_rates[curr]) * 100
    percent_changes[curr] = round(change, 3)

# --- Calculate stats ---
average_rate = round(statistics.mean(rates.values()), 3)
std_dev = round(statistics.pstdev(rates.values()), 3)

# --- Display results ---
print("\nCurrent Rates (USD Base):")
for curr, rate in rates.items():
    print(f"1 USD = {rate} {curr}")

print("\nDaily % Change:")
for curr, change in percent_changes.items():
    print(f"{curr}: {change}%")

print(f"\nAverage rate (across selected currencies): {average_rate}")
print(f"Standard Deviation: {std_dev}")
