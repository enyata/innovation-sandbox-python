from faker import Faker

header = {
    "base_url": "",
    "Sandbox-Key": str(Faker().text()),
    "Content-Type": "application/json"
}

body = {
    "CreateCheckoutToken": {
        "phoneNumber": "+2349091271976"
    },
    "CreatePremiumSubscription": {
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "phoneNumber": "+2349091271976",
        "checkoutToken": str(Faker().text())
    },

    "DeletePremiumSubscription": {
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "phoneNumber": "+2348123456789"
    },

    "FetchMessage": {
        "lastReceivedId": "12"
    },

    "FetchPremiumSubscription": {
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "lastReceivedId": "0"
    },
    "MediaUpload": {
        "phoneNumber": "+2349091271976",
        "url": "http://www.test_url_device.com"
    },
    "QueueStatus": {
        "phoneNumbers": "+2349091271976"
    },
    "SendAirtime": {
        "recipients": [{"phoneNumber": "+2348130155009", "amount": "1000", "currencyCode": "NGN"}, {"phoneNumber": "+2348130835009", "amount": "3000", "currencyCode": "NGN"}]
    },
    "SendMessage": {
        "to": "+2349091271976",
        "from": "FSI",
        "message": "Hello World"
    },
    "SendPremiumMessage": {
        "to": "+2349091271976",
        "from":	"FSI",
        "message": "Hello World",
        "keyword": "innovation-sandbox",
        "linkId": "12345",
        "retryDurationInHours":	"1"
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
        "shortCode": "19171",
        "keyword": "innovation-sandbox",
        "phoneNumber": "+2349091271976",
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
        "totalAmount": "NGN 4000.0000",
        "totalDiscount": "NGN 80.0000",
        "responses": [
            {
                "phoneNumber": "+2348130835009",
                "errorMessage": "None",
                "amount": "NGN 3000.0000",
                "status": "Sent",
                "requestId": "ATQid_e5c25b080a39ae3c177242b5abebd497",
                "discount": "NGN 60.0000"
            },
            {
                "phoneNumber": "+2348130155009",
                "errorMessage": "None",
                "amount": "NGN 1000.0000",
                "status": "Sent",
                "requestId": "ATQid_5a956cef4b4a076a49201b72c7933ca9",
                "discount": "NGN 20.0000"
            }
        ]
    },
    "SendMessage": {
        "SMSMessageData": {
            "Message": "Sent to 1/1 Total Cost: NGN 2.2000",
            "Recipients": [
                {
                    "statusCode": 101,
                    "number": "+2348130835009",
                    "cost": "NGN 2.2000",
                    "status": "Success",
                    "messageId": "ATXid_8d0ba37f1bd082e987a82fa3c0e1eb0f"
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
                    "number": "+2348130155009",
                    "cost": "0",
                    "status": "Success",
                    "messageId": "ATXid_9d680de1008e4028bd63ff84344e8a15"
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
