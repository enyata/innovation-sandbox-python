from atlabs.airtime import Airtime

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
    "Content-Type": "application/json"
}

body = {
    "recipients": [{"phoneNumber": "+2349091271976", "amount": "1000", "currencyCode": "NGN"}]
}

result = Airtime(header).SendAirtime(body)
print(result)
