from atlabs.sms import Sms

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
    "Content-Type": "application/json"
}

body = {
    "shortCode": "19171",
    "keyword": "innovation-sandbox",
    "lastReceivedId": "0"
}

result = Sms(header).FetchPremiumSubscription(body)
print(result)
