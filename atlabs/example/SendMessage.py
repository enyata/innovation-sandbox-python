from atlabs.sms import Sms

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
    "Content-Type": "application/json"
}

body = {
    "to": "+2348123456789",
    "from": "FSI",
    "message": "Hello world!"
}

result = Sms(header).SendSms(body)
print(result)