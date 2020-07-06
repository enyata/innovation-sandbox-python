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

mobile_wallet_transfer_body = {
    "Referenceid": str(fake),
    "RequestType": str(fake),
    "Translocation": str(fake),
    "amt": str(fake),
    "tellerid": str(fake),
    "frmacct": str(fake),
    "toacct": str(fake),
    "exp_code": str(fake),
    "paymentRef": str(fake),
    "remarks": str(fake)
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
    },
    "mobile_wallet_transfer": {
        "message": "Ok",
        "data": {
            "message": "success",
            "response": "success",
            "responsedata": "null",
            "data": {
                "ResponseText": "Your mobile wallet transaction has been submitted for processing.",
                "status": "00"
            }
        }
    },
    "bill_payment_advice":{
    "message": 'OK',
    "data": {
        "message": 'success',
        "response": 'success',
        "data": {
            "ResponseText": 'The list of all billing services available to a particular billing company.',
            "status": '00',
        }
    }
    },
    "biller_payment_items":{
    "message": 'OK',
    "data": {
        "message": 'success',
        "response": 'success',
        "data": {
            "ResponseText": 'The list of all billing services available to a particular billing company.',
            "status": '01',
        }
    }},
    "test_biller_isw": {
    "message": 'OK',
    "data": {
        "message": 'success',
        "response": 'success',
        "data": {
            "ResponseText": 'The list of all billing services available.',
            "status": '02',
        },
    },
}
}

query = {
    "Referenceid": str(fake),
    "RequestType": str(fake),
    "Translocation": str(fake),
    "ToAccount": str(fake),
    "destinationbankcode": str(fake)
}


get_biller_query = {
    "Referenceid": str(fake),
    "RequestType": str(fake),
    "Translocation": str(fake),
    "Bvn": str(fake)
}

class R:
    def __init__(self, text):
        self.status_code = 200
        self.text = text
