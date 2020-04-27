from relianceHMO.retails import Retails

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "Referral_code": "1122345",
    "enrollees": [
        {
            "payment_frequency": "monthly",
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "testuser1@kang.pe",
            "phone_number": "08132646940",
            "plan_id": 22,
            "can_complete_profile": True,
            "dependants": [
                {
                    "first_name": "Janet",
                    "last_name": "Dependant",
                    "email_address": "testuser2@kang.pe",
                    "phone_number": "08132646940",
                    "plan_id": 22
                },
                {
                    "first_name": "Fred",
                    "last_name": "Dependant",
                    "email_address": "testuser3@kang.pe",
                    "phone_number": "08132646940",
                    "plan_id": 24
                }
            ]
        },
        {
            "payment_frequency": "q",
            "first_name": "Ben",
            "last_name": "Stiller",
            "email_address": "snr22325@awsoo.com",
            "phone_number": "08132646940",
            "plan_id": 24,
            "can_complete_profile": False,
            "dependants": []
        }
    ]
}
result = Retails(header).SignupIndividuals(body)

print(result)
