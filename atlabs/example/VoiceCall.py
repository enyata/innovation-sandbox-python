from atlabs.voice import Voice

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "callFrom": "FSI",
    "callTo": "+2348123456789"
}

result = Voice(header).VoiceCall(body)
print(result)
