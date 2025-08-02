import pandas as pd
import matplotlib.pyplot as plt

# --- Load saved CSV ---
csv_file = "currency_history.csv"
df = pd.read_csv(csv_file)

# --- Convert 'Date' column to datetime ---
df["Date"] = pd.to_datetime(df["Date"])

# --- Plot trends ---
plt.figure(figsize=(10, 6))
for col in df.columns[1:]:  # Skip 'Date'
    plt.plot(df["Date"], df[col], marker='o', label=col)

plt.title("Currency Trends (USD Base)")
plt.xlabel("Date")
plt.ylabel("Exchange Rate")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
