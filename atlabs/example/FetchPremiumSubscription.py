from atlabs.sms import Sms

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "shortCode": "19171",
    "keyword": "innovation-sandbox",
    "lastReceivedId": "0"
}

result = Sms(header).FetchPremiumSubscription(body)
print(result)
