from atlabs.sms import Sms

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
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