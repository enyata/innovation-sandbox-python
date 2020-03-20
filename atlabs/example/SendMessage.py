from atlabs.sms import Sms

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "to": "+2348123456789",
    "from": "FSI",
    "message": "Hello world!"
}

result = Sms(header).SendSms(body)
print(result)
