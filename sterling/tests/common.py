from faker import Faker

fake = Faker().random_number()

body = {
    "Referenceid": str(fake),
    "RequestType": str(fake),
    "Translocation": str(fake),
    "SessionID": str(fake),
    "FromAccount": str(fake),
    "ToAccount": str(fake),
    "Amount": str(fake),
    "DestinationBankCode": str(fake),
    "NEResponse": str(fake),
    "BenefiName": str(fake),
    "PaymentReference": str(fake),
    "OriginatorAccountName": str(fake),
    "translocation": str(fake)
}

responses = {"enquiry": {
    "message": "OK",
    "data": {
        "message": "success",
        "response": "success",
        "data": {
            "AccountName": str(Faker().name),
            "sessionID": str(fake),
            "AccountNumber": str(fake),
            "status": str(fake),
            "BVN": str(fake),
            "ResponseText": None
        }
    }
},

    "transfer": {
        "message": "OK",
        "data": {
            "message": "success",
            "response": "success",
            "responsedate": "null",
            "data": {
                "ResponseText": "Your transaction has been submitted for processing.",
                "status": str(fake),
            }
        }
    }
}

query = {
    "Referenceid": str(fake),
    "RequestType": str(fake),
    "Translocation": str(fake),
    "ToAccount": str(fake),
    "destinationbankcode": str(fake)
}


class R:
    def __init__(self, text):
        self.status_code = 200
        self.text = text
