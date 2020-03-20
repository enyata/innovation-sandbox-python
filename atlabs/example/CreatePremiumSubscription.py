from atlabs.sms import Sms

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "shortCode": "19171",
    "keyword": "innovation-sandbox",
    "phoneNumber": "+2348123456789",
    "checkoutToken": "CkTkn_65faa63e-cc95-41bb-812e-1c1d921df70b"
}

result = Sms(header).CreatePremiumSubscription(body)
print(result)
