from atlabs.token import Token

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
    "Content-Type": "application/json"
}

body = {
    "phoneNumber": "+2348123456789"
}

result = Token(header).CreateCheckoutToken(body)
print(result)
