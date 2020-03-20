from atlabs.sms import Sms

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "shortCode": "19171",
    "keyword": "innovation-sandbox",
    "phoneNumber": "+2348123456789"
}

result = Sms(header).DeletePremiumSubscription(body)
print(result)
