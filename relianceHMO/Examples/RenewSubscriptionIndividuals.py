from relianceHMO.retails import Retails

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "enrollees": [
        {
            "user_id": 345,
            "remove": [
                347
            ]
        }
    ]
}
result = Retails(header).Renew(body)

print(result)
