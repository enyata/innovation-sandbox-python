from atlabs.token import Token

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "phoneNumber": "+2348123456789"
}

result = Token(header).CreateCheckoutToken(body)
print(result)
