from atlabs.sms import Sms

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "lastReceivedId": "0"
}

result = Sms(header).FetchMessage(body)
print(result)
