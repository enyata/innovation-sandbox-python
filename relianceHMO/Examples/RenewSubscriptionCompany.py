from relianceHMO.clients import Clients

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "transfer_code": "1234WXYZ",
    "add": [
        {
            "plan_id": 22,
            "firstname": "Princess",
            "lastname": "Diana",
            "email": "diana@amazon.com",
            "phone_number": "08041122234"
        }
    ],
    "remove": [
        "K2JhMYr5wDGMxZWdh",
        "z44JhMYyDGMxZ362hwe"
    ],
    "update": [
        {
            "plan_id": 24,
            "user_token": "Y2JhMWJhNDc4YWJkMGMxZWdh"
        }
    ]
}

result = Clients(header).RenewSubscriptionCompany(body)

print(result)
