from nibss.utils.crypt import Crypt
from Crypto.Random import random

iv = ''.join(chr(random.randint(0, 23)) for i in range(16))
aes = ''.join(chr(random.randint(0, 23)) for i in range(16))

responses = {
    "single_bvn": {
        'message': 'OK',
        'data': {
            'ResponseCode': '00', 'BVN': '12345678901', 'FirstName': 'Uchenna', 'MiddleName': 'Chijioke',
            'LastName': 'Nwanyanwu', 'DateOfBirth': '22-Oct-1970', 'PhoneNumber': '07033333333',
            'RegistrationDate': '16-Nov-2014', 'EnrollmentBank': '900',
            'EnrollmentBranch': 'Victoria Island', 'WatchListed': 'NO'
        }
    },
    "multiple_bvn": {
        "message": "OK",
        "data": {"ResponseCode": "00", "ValidationResponses": [
            {
                "ResponseCode": "00", "BVN": "12345678901", "FirstName": "Uchenna", "MiddleName": "Innocent",
                "LastName": "Nwanyanwu", "DateOfBirth": "29-Oct-1995", "PhoneNumber": "07033333333",
                "RegistrationDate": "16-Dec-2014", "EnrollmentBank": "900", "EnrollmentBranch": "Victoria Island",
                "WatchListed": "NO"
            },
            {
                "ResponseCode": "00", "BVN": "12345678902", "FirstName": "Wale", "MiddleName": "Joshua",
                "LastName": "Odugbemi", "DateOfBirth": "29-Oct-1996", "PhoneNumber": "07033333334",
                "RegistrationDate": "16-Oct-2014", "EnrollmentBank": "900",
                "EnrollmentBranch": "No. 2 NIBSS Avenue, VI",
                "WatchListed": "YES"
            },
            {
                "ResponseCode": "00", "BVN": "12345678903", "FirstName": "Seun", "MiddleName": "Ogunjimi",
                "LastName": "Isaiah", "DateOfBirth": "29-Oct-1997", "PhoneNumber": "07033333336",
                "RegistrationDate": "16-Sept-2014", "EnrollmentBank": "900", "EnrollmentBranch": "Ikorodu",
                "WatchListed": "NO"
            }]}
    },
    "watchlist": {
        "message": "OK",
        "data": {
            "ResponseCode": "00",
            "BVN": "12345678901",
            "BankCode": "900",
            "Category": "1",
            "WatchListed": "YES"
        }
    },
    "record": {
        "message": "OK",
        "data": {
            "ResponseCode": "00",
            "BVN": "VALID",
            "FirstName": "VALID",
            "LastName": "VALID",
            "MiddleName": "INVALID",
            "AccountNumber": "VALID",
            "BankCode": "VALID"
        }
    },
    "records": {
        'message': 'OK',
        'data': {'ValidationResponses': [
            {
                'ResponseCode': '00',
                'BVN': 'VALID',
                'FirstName': 'VALID',
                'LastName': 'VALID',
                'MiddleName': 'INVALID',
                'AccountNumber': 'VALID',
                'BankCode': 'VALID'},
            {
                'ResponseCode': '00', 'BVN': 'VALID', 'FirstName': 'INVALID', 'LastName': 'VALID',
                'MiddleName': 'INVALID', 'AccountNumber': 'VALID', 'BankCode': 'VALID'
            }
        ]}
    },
    "fingerprint_data": {
        "message": "OK",
        "data": {
            "BVN": "12345678901",
            "ResponseCode": "00"
        }
    }

}

body = {
    "single_bvn": Crypt().encrypt(responses["single_bvn"], aes, iv),
    "multiple_bvn": Crypt().encrypt(responses["multiple_bvn"], aes, iv),
    "watchlist": Crypt().encrypt(responses["watchlist"], aes, iv),
    "record": Crypt().encrypt(responses["record"], aes, iv),
    "records": Crypt().encrypt(responses["records"], aes, iv),
    "fingerprint_data": Crypt().encrypt(responses["fingerprint_data"], aes, iv)
}


class R:
    def __init__(self, text):
        self.status_code = 200
        self.text = text
        self.headers = {'Aes_key': aes, 'Password': "fdgfudkjd", 'Ivkey': iv}
