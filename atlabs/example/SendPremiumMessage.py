from atlabs.sms import Sms

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "to": "+2348123456789",
    "from": "FSI",
    "message": "Hello world!",
    "keyword": "innovation-sandbox",
    "linkId": "d",
    "retryDurationInHours": 1
}

result = Sms(header).SendPremiumMessage(body)
print(result)
