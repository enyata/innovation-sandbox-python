from faker import Faker

header = {
    "base_url": "",
    "Sandbox-Key": str(Faker().text()),
    "Content-Type": "application/json"
}

body = {
    "CreateCheckoutToken": {
        "phoneNumber": str(Faker().phone_number()),
    },
    "CreatePremiumSubscription": {
        "shortCode": str(Faker().random_int()),
        "keyword": str(Faker().text()),
        "phoneNumber": str(Faker().phone_number()),
        "checkoutToken": str(Faker().text())
    },

    "DeletePremiumSubscription": {
        "shortCode": str(Faker().random_int()),
        "keyword": str(Faker().text()),
        "phoneNumber": str(Faker().phone_number()),
    },

    "FetchMessage": {
        "lastReceivedId": "12"
    },

    "FetchPremiumSubscription": {
        "shortCode": str(Faker().random_int()),
        "keyword": "innovation-sandbox",
        "lastReceivedId": "0"
    },
    "MediaUpload": {
        "phoneNumber": str(Faker().phone_number()),
        "url": str(Faker().text())
    },
    "QueueStatus": {
        "phoneNumber": str(Faker().phone_number()),
    },
    "SendAirtime": {
        "recipients": [{"phoneNumber": str(Faker().phone_number()), "amount": str(Faker().random_int()), "currencyCode": str(Faker().text())}, {"phoneNumber": str(Faker().phone_number()), "amount": str(Faker().random_int()), "currencyCode": str(Faker().text())}]
    },
    "SendMessage": {
        "to": str(Faker().phone_number()),
        "from": str(Faker().text()),
        "message": str(Faker().text())
    },
    "SendPremiumMessage": {
        "to": str(Faker().phone_number()),
        "from":	str(Faker().text()),
        "message": str(Faker().text()),
        "keyword": str(Faker().text()),
        "linkId": str(Faker().random_int()),
        "retryDurationInHours":	str(Faker().random_int())
    },
    "VoiceCall": {
        "callFrom": "FSI",
        "callTo": "+2349091271976"
    }
}

responses = {
    "CreateCheckoutToken": {
        "description": "Success",
        "token": str(Faker().text())
    },
    "CreatePremiumSubscription": {
        "shortCode": str(Faker().random_int()),
        "keyword": str(Faker().text()),
        "phoneNumber": str(Faker().phone_number()),
        "checkoutToken": str(Faker().text())
    },
    "DeletePremiumSubscription": {
        "status": "Success",
        "description": "Succeeded"
    },
    "FetchMessage": {
        "SMSMessageData": {
            "Messages": []
        }
    },
    "FetchPremiumSubscription": {
        "responses": []
    },
    "MediaUpload": {
        "test": "test"
    },
    "QueueStatus": {
        "status": "Success",
        "entries": [],
        "errorMessage": "None"
    },
    "SendAirtime": {
        "errorMessage": "None",
        "numSent": 2,
        "totalAmount": str(Faker().random_int()),
        "totalDiscount": "NGN 80.0000",
        "responses": [
            {
                "phoneNumber": str(Faker().phone_number()),
                "errorMessage": "None",
                "amount": str(Faker().random_int()),
                "status": "Sent",
                "requestId": str(Faker().text()),
                "discount": str(Faker().random_int())
            },
            {
                "phoneNumber": str(Faker().phone_number()),
                "errorMessage": "None",
                "amount": str(Faker().random_int()),
                "status": "Sent",
                "requestId": str(Faker().text()),
                "discount": str(Faker().random_int())
            }
        ]
    },
    "SendMessage": {
        "SMSMessageData": {
            "Message": "Sent to 1/1 Total Cost: NGN 2.2000",
            "Recipients": [
                {
                    "statusCode": 101,
                    "number": str(Faker().phone_number()),
                    "cost": str(Faker().random_int()),
                    "status": "Success",
                    "messageId": str(Faker().text())
                }
            ]
        }
    },
    "SendPremiumMessage": {
        "SMSMessageData": {
            "Message": "Sent to 1/1",
             "Recipients": [
                {
                    "statusCode": 101,
                    "number": str(Faker().phone_number()),
                    "cost": str(Faker().random_int()),
                    "status": "Success",
                    "messageId": str(Faker().text())
                }
            ]
        }
    },
    "VoiceCall": {
        "test": "test"

    }
}


class R:
    def __init__(self, text):
        self.status_code = 200
        self.text = text

    def json(self):
        return self.text
