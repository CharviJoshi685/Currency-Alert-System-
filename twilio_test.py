from twilio.rest import Client

# Twilio credentials
ACCOUNT_SID = "ACa3e06508dcb7627d155ebb8bfdcb0cae"
AUTH_TOKEN = "cb9321f084b5cfb21263c586ad8f1925"

# Phone numbers
TWILIO_NUMBER = "+13412184197"       # Your Twilio trial number
MY_PHONE_NUMBER = "+918529107531"    # Your verified Indian number

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Send test SMS
message = client.messages.create(
    body="✅ INR is within safe range: 87.42\n✅ EUR is within safe range: 0.87\n✅ JPY is within safe range: 148.17\n✅ GBP is within safe range: 0.75",
    from_=TWILIO_NUMBER,
    to=MY_PHONE_NUMBER
)

print(f"✅ Message sent successfully! SID: {message.sid}")
