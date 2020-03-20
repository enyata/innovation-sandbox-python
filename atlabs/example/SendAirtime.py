from atlabs.airtime import Airtime

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "recipients": [{"phoneNumber": "+2349091271976", "amount": "1000", "currencyCode": "NGN"}]
}

result = Airtime(header).SendAirtime(body)
print(result)
