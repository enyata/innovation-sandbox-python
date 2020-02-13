body = {
            "Referenceid": "0101",
            "RequestType": "0101",
            "Translocation": "0101",
            "SessionID": "01",
            "FromAccount": "01",
            "ToAccount": "01",
            "Amount": "01",
            "DestinationBankCode": "01",
            "NEResponse": "01",
            "BenefiName": "01",
            "PaymentReference": "01",
            "OriginatorAccountName": "01",
            "translocation": "01"
        }

responses = {"enquiry" : {
    "message": "OK",
    "data": {
        "message": "success",
        "response": "success",
        "data": {
            "AccountName": "John Doe",
            "sessionID": "999232200107170915323048583333",
            "AccountNumber": " 0037514056",
            "status": "97",
            "BVN": "12345678901",
            "ResponseText" : None
        }
    }
},

"transfer" : {
    "message": "OK",
    "data": {
        "message": "success",
        "response": "success",
        "responsedate": "null",
        "data": {
            "ResponseText": "Your transaction has been submitted for processing.",
            "status": "00",
        }
    }
}
}

query = {
	"Referenceid": "01",
	"RequestType": "01",
	"Translocation": "01",
	"ToAccount": "0037514056",
	"destinationbankcode": "000001"
  }
class R:
    def __init__(self,text):
        self.status_code = 200
        self.text = text

