
from union.token import Token

body = {
    "client_secret": "secret",
    "client_id": "web01",
    "grant_type": "password",
    "username": "ubnclient01",
    "password": "w$777"
}

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Content-Type": "application/x-www-form-urlencoded",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290"
}

result = Token(header).AccessTokenGenerator(body)

print(result)
