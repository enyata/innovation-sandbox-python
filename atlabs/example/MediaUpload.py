from atlabs.voice import Voice

header = {
    "base_url": "https://innovation-sandbox-backend.herokuapp.com",
    "Sandbox-Key": "49264b2cc8fd68b33326c6d5468e5290",
    "Content-Type": "application/json"
}

body = {
    "phoneNumber": "+2348123456789",
    "url": "http://test.com"
}

result = Voice(header).MediaUpload(body)
print(result)
