from relianceHMO.clients import Clients

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "transfer_code": "1234WXYZ",
    "company_name": "Justice League",
    "company_address": "85, outer space",
    "state_code": "NG-LA",
    "payment_frequency": "monthly",
    "company_admin": {
        "first_name": "Bruce",
        "last_name": "Wayne",
        "email_address": "bruce@wayne.corp",
        "phone_number": "08011122234"
    },
    "enrollees": [
        {
            "plan_id": 22,
            "first_name": "Bruce",
            "last_name": "Wayne",
            "email_address": "bruce@wayne.corp",
            "phone_number": "08011122234"
        },
        {
            "plan_id": 14,
            "first_name": "Barry",
            "last_name": "Allen",
            "email_address": "barry@flash.org",
            "phone_number": "08033344322"
        }
    ]
}

result = Clients(header).SignupCompany(body)

print(result)
