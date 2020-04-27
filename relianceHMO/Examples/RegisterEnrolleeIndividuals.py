from relianceHMO.enrollees import Enrollees

header = {
    "base_url": "https://sandboxapi.fsi.ng",
    "Sandbox-Key": "your-sandbox-key-here",
    "Content-Type": "application/json"
}

body = {
    "enrollees": [
        {
            "payment_frequency": "monthly",
            "first_name": "John",
            "last_name": "Doe",
            "email_address": "dewo.1@kang.pe",
            "phone_number": "08132846940",
            "plan_id": 22,
            "can_complete_profile": "true",
            "profile": {
                "sex": "m",
                "date_of_birth": "1991-03-03",
                "first_name": "Doey",
                "last_name": "Doe",
                "primary_phone_number": "08159049122",
                "home_address": "Somewhere Awesome",
                "has_smartphone": "true",
                "profile_picture_filename": "ttffddzp.jpg",
                "enrollee_type": 1,
                "hmo_id": ""
            },
            "dependants": [
                {
                    "first_name": "Janet",
                    "last_name": "Dependant",
                    "email_address": "wu1uo389@gmail.com",
                    "phone_number": "08132046940",
                    "plan_id": 22
                }
            ]
        }
    ]
}

result = Enrollees(header).Register(body)

print(result)
