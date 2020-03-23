from union.enquiry import Enquiry

body = {
    "accountNumber": "0000791200",
    "accountType": "CASA"
}

params = {
    "access_token": "e7ce9048-446e-4b9c-8c2b-575a694144c9"
}

headers = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Content-Type": "application/json",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290"
}

result = Enquiry(headers).CustomerAndAccount(body, params)

print(result)