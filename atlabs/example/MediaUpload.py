from atlabs.voice import Voice

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "phoneNumber": "+2348123456789",
    "url": "link-to-media-file"
}

result = Voice(header).MediaUpload(body)
print(result)