
from union.user import User

body = {
    "username": "user1",
    "oldPassword": "password2",
    "password": "password",
    "moduleId": "UNION_ONE",
    "clientSecret": "ABC"
}

params = {
    "access_token": "your-access-token-here"
}

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Content-Type": "application/json",
    "Sandbox-Key": "your-sandbox-key-here"
}

result = User(header).ChangeUsersCredentials(body, params)

print(result)
