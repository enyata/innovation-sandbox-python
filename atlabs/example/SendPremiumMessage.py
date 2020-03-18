from atlabs.sms import Sms

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
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

result = Sms(header).SendPremiumSms(body)
print(result)
