import requests
import csv
import os
from datetime import datetime

# --- Settings ---
currencies = ["INR", "EUR", "JPY", "GBP"]
csv_file = "currency_history.csv"

# --- Fetch latest rates ---
url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()
rates = {curr: data["rates"][curr] for curr in currencies}

# --- Get today's date ---
today = datetime.now().strftime("%Y-%m-%d")

# --- Save to CSV ---
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="") as file:
    writer = csv.writer(file)
    
    # Write header if file doesn't exist
    if not file_exists:
        writer.writerow(["Date"] + currencies)
    
    # Write today's data
    writer.writerow([today] + [rates[curr] for curr in currencies])

print(f"✅ Saved today's rates to {csv_file}")

# --- Load CSV & show last few entries ---
with open(csv_file, "r") as file:
    reader = list(csv.reader(file))
    for row in reader[-5:]:  # Last 5 entries
        print(row)
