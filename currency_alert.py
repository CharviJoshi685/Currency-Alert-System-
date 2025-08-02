import requests
from twilio.rest import Client

# --- Twilio credentials ---
ACCOUNT_SID = "ACa3e06508dcb7627d155ebb8bfdcb0cae"
AUTH_TOKEN = "cb9321f084b5cfb21263c586ad8f1925"
TWILIO_NUMBER = "+13412184197"  # Your Twilio trial number
MY_PHONE_NUMBER = "+918529107531"  # Your verified phone

# --- Currency settings ---
currencies = ["INR", "EUR", "JPY", "GBP"]
thresholds = {
    "INR": 90,   # Example: alert if USD/INR > 90
    "EUR": 0.95,
    "JPY": 150,
    "GBP": 0.80
}

# --- Fetch latest rates ---
url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()
rates = {curr: data["rates"][curr] for curr in currencies}

# --- Initialize Twilio client ---
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# --- Check each currency ---
for curr, rate in rates.items():
    if rate > thresholds[curr]:
        message = f"💱 Currency Alert! 1 USD = {rate:.2f} {curr} — above your limit of {thresholds[curr]}"
        client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_PHONE_NUMBER
        )
        print(f"📲 Alert sent for {curr} — {rate:.2f}")
    else:
        print(f"✅ {curr} is within safe range: {rate:.2f}")
