
from union.token import Token

body = {
    "client_secret": "secret",
    "client_id": "web01",
    "grant_type": "password",
    "username": "ubnclient01",
    "password": "w$777"
}

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Content-Type": "application/x-www-form-urlencoded",
    "Sandbox-Key": "your-sandbox-key-here"
}

result = Token(header).AccessTokenGenerator(body)

print(result)
