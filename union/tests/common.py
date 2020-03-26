from faker import Faker

header = {
    "base_url": "",
    "Sandbox-Key": str(Faker().text()),
    "Content-Type": "application/json"
}

body = {
    "AccessTokenGenerator": {
        "client_secret": str(Faker().text()),
        "client_id": str(Faker().text()),
        "grant_type": str(Faker().text()),
        "username": str(Faker().text()),
        "password": str(Faker().text())
    },
    "AccountEnquiry": {
        "accountNumber": str(Faker().credit_card_number()),
        "accountType": str(Faker().text())
    },
    "CustomerEnquiry": {
        "accountNumber": str(Faker().credit_card_number()),
        "accountType": str(Faker().text())
    },
    "CustomerAndAccountEnquiry": {
        "accountNumber": str(Faker().credit_card_number()),
        "accountType": str(Faker().text())
    },
    "ChangeUserCredentials": {
        "username": str(Faker().name()),
        "oldPassword": str(Faker().text()),
        "password": str(Faker().text()),
        "moduleId": "UNION_ONE",
        "clientSecret": str(Faker().text())
    }
}

responses = {
    "AccessTokenGenerator": {
        "message": "OK",
        "data": {
            "access_token": str(Faker().text()),
            "token_type": "bearer",
            "refresh_token": str(Faker().text()),
            "expires_in": Faker().random_int(),
            "scope": "read"
        }
    },
    "AccountEnquiry": {
        "message": "OK",
        "data": {
            "code": "00",
            "message": "Account Enquiry Successful",
            "accountNumber": str(Faker().random_int()),
            "accountName": str(Faker().name()),
            "accountBranchCode": Faker().random_int(),
            "customerNumber": str(Faker().credit_card_number()),
            "accountClass": str(Faker().random_int()),
            "accountCurrency": "NGN",
            "accountType": "Current",
            "availableBalance": str(Faker().random_int()),
            "customerAddress": str(Faker().address()),
            "customerEmail": str(Faker().email()),
            "customerPhoneNumber": str(Faker().phone_number())
        }
    },
    "CustomerEnquiry": {
        "message": "OK",
        "data": {
            "code": "00",
            "message": "Customer Enquiry Successful",
            "country": str(Faker().country()),
            "countryOfBirth": str(Faker().country()),
            "dob": str(Faker().date()),
            "nationality": "NG",
            "lastName": str(Faker().name()),
            "firstName": str(Faker().name()),
            "otherNames": str(Faker().name()),
            "customerType": "I",
            "email": str(Faker().email()),
            "phoneNumber": str(Faker().phone_number()),
            "idType": "OTHERS",
            "idNumber": str(Faker().random_int()),
            "countryOfIssue": str(Faker().country()),
            "effectiveDate": str(Faker().date()),
            "expiryDate": str(Faker().date()),
            "addressLine1": str(Faker().address()),
            "addressLine2": str(Faker().address()),
            "city": str(Faker().city()),
            "state": str(Faker().state()),
            "postalCode": str(Faker().random_int()),
            "bvn": str(Faker().random_int())
        }
    },
    "CustomerAndAccountEnquiry": {
        "message": "OK",
        "data": {
            "code": "00",
            "message": "Enquiry successful",
            "account": {
                "code": "00",
                "message": "Account Enquiry Successful",
                "accountNumber": str(Faker().random_int()),
                "accountName": str(Faker().name()),
                "accountBranchCode": Faker().random_int(),
                "customerNumber": str(Faker().credit_card_number()),
                "accountClass": str(Faker().random_int()),
                "accountCurrency": "NGN",
                "accountType": "Current",
                "availableBalance": str(Faker().random_int()),
                "customerAddress": str(Faker().address()),
                "customerEmail": str(Faker().email()),
                "customerPhoneNumber": str(Faker().phone_number())
            },
            "customer": {
                "code": "00",
                "message": "Customer Enquiry Successful",
                "country": str(Faker().country()),
                "countryOfBirth": str(Faker().country()),
                "dob": str(Faker().date()),
                "nationality": "NG",
                "lastName": str(Faker().name()),
                "firstName": str(Faker().name()),
                "otherNames": str(Faker().name()),
                "customerType": "I",
                "email": str(Faker().email()),
                "phoneNumber": str(Faker().phone_number()),
                "idType": "OTHERS",
                "idNumber": str(Faker().random_int()),
                "countryOfIssue": str(Faker().country()),
                "effectiveDate": str(Faker().date()),
                "expiryDate": str(Faker().date()),
                "addressLine1": str(Faker().address()),
                "addressLine2": str(Faker().address()),
                "city": str(Faker().city()),
                "state": str(Faker().state()),
                "postalCode": str(Faker().random_int()),
                "bvn": str(Faker().random_int())
            }
        }
    },
    "ChangeUserCredentials": {
        "message": "OK",
        "data": {
            "code": "00",
            "message": "Password changes successfully",
            "reference": str(Faker().text())
        }
    }

}

params = {
    "access_token": str(Faker().text())
}


class R:
    def __init__(self, text):
        self.status_code = 200
        self.text = text

    def json(self):
        return self.text
