from union.enquiry import Enquiry

body = {
    "accountNumber": "0000791200",
    "accountType": "CASA"
}

params = {
    "access_token": "your-access-token-here"
}

headers = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Content-Type": "application/json",
    "Sandbox-Key": "your-sandbox-key-here"
}

result = Enquiry(headers).CustomerAndAccount(body, params)

print(result)
